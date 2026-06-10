#!/usr/bin/env python3
"""
HMSR WP3 verifier — multiomics-analysis skill STEP 5.

Asserts universal gates + bulk_transcriptomics modality constraints.
Exits non-zero on any violation; emits STATUS=PASS/BLOCKED/NEEDS_REVIEW.
"""
from __future__ import annotations

import hashlib
import os
import sys
from pathlib import Path

import pandas as pd

BASE = Path("/Volumes/4TB/exerciseomics/sarcopenia-multiomic-resource")
OUTPUT = BASE / "output" / "signatures"
CHECKSUMS = BASE / "data" / "CHECKSUMS.txt"
ENV_YML = BASE / "environment.yml"

PASSES: list[str] = []
FAILS: list[str] = []


def ok(msg: str) -> None:
    PASSES.append(msg)
    print(f"  PASS  {msg}")


def fail(msg: str) -> None:
    FAILS.append(msg)
    print(f"  FAIL  {msg}")


# ── 1. Environment pinned ──────────────────────────────────────────────────
def check_env() -> None:
    if ENV_YML.exists():
        ok(f"environment.yml present: {ENV_YML.relative_to(BASE)}")
    else:
        fail(f"environment.yml missing at {ENV_YML.relative_to(BASE)}")


# ── 2. Required output files exist ────────────────────────────────────────
REQUIRED_FILES = [
    OUTPUT / "replication_matrix.tsv",
    OUTPUT / "differential_by_cohort.tsv",
    OUTPUT / "wp3_gate_pass.tsv",
    OUTPUT / "model_audit.tsv",
]


def check_files() -> None:
    for f in REQUIRED_FILES:
        if f.exists():
            ok(f"output present: {f.relative_to(BASE)}")
        else:
            fail(f"output missing: {f.relative_to(BASE)}")


# ── 3. Organism gate ───────────────────────────────────────────────────────
ALLOWED_ORGANISMS = {"Homo sapiens"}


def check_organisms() -> None:
    audit_path = BASE / "output" / "validation" / "cohort_inventory.tsv"
    if not audit_path.exists():
        fail("cohort_inventory.tsv missing — cannot verify organism gate")
        return
    inv = pd.read_csv(audit_path, sep="\t")
    if "organism" not in inv.columns:
        fail("cohort_inventory.tsv missing 'organism' column — organism gate CANNOT be enforced")
        return
    bad = inv[~inv["organism"].isin(ALLOWED_ORGANISMS)]
    included = inv[inv.get("recommended_model_role", pd.Series(dtype=str)).str.contains("candidate|training", na=False)]
    bad_included = included[~included["organism"].isin(ALLOWED_ORGANISMS)] if len(included) else pd.DataFrame()
    if bad_included.empty:
        ok(f"Organism gate: all {len(included)} included cohorts are Homo sapiens")
    else:
        for _, row in bad_included.iterrows():
            fail(f"Non-allowed organism in included cohort: {row.get('cohort','?')} → {row['organism']}")
    # Report excluded cohorts with non-allowed organisms as info only
    bad_excluded = inv[~inv["organism"].isin(ALLOWED_ORGANISMS)] if len(inv) else pd.DataFrame()
    if not bad_excluded.empty:
        ok(f"Excluded cohorts with non-standard organism entries: {bad_excluded['cohort'].tolist()} (excluded from analysis)")


# ── 4. bulk_transcriptomics method record ────────────────────────────────
def check_method_record() -> None:
    rep = OUTPUT / "replication_matrix.tsv"
    if not rep.exists():
        fail("replication_matrix.tsv missing — cannot verify method record")
        return
    df = pd.read_csv(rep, sep="\t", nrows=1)
    # DL RE meta columns must be present (not fixed-effect)
    for col in ("meta_beta", "meta_se", "tau_sq", "heterogeneity_i2"):
        if col in df.columns:
            ok(f"RE meta column present: {col}")
        else:
            fail(f"RE meta column missing: {col} (fixed-effect columns must not be used)")
    # genome-wide BH-FDR column must be present
    if "meta_fdr" in df.columns:
        ok("Genome-wide BH FDR column present: meta_fdr")
    else:
        fail("meta_fdr column missing — genome-wide BH must be applied")


# ── 5. WP3 gate columns ───────────────────────────────────────────────────
def check_gate_pass() -> None:
    gp = OUTPUT / "wp3_gate_pass.tsv"
    if not gp.exists():
        fail("wp3_gate_pass.tsv missing")
        return
    df = pd.read_csv(gp, sep="\t")
    required_cols = [
        "gene_symbol", "meta_p_value", "meta_fdr",
        "direction_consistency", "leave_one_cohort_out_replication_rate",
        "heterogeneity_flag",
    ]
    for col in required_cols:
        if col in df.columns:
            ok(f"gate_pass column present: {col}")
        else:
            fail(f"gate_pass column missing: {col}")
    # All rows must satisfy gate criteria
    if not df.empty:
        bad_p = df[df["meta_p_value"] >= 0.005]
        if bad_p.empty:
            ok(f"All {len(df)} gate-pass genes have meta_p < 0.005")
        else:
            fail(f"{len(bad_p)} gate-pass genes violate meta_p < 0.005")
        bad_dir = df[df["direction_consistency"] < 1.0]
        if bad_dir.empty:
            ok("All gate-pass genes have direction_consistency = 1.0")
        else:
            fail(f"{len(bad_dir)} gate-pass genes have direction_consistency < 1.0")
        bad_loco = df[df["leave_one_cohort_out_replication_rate"] < 1.0]
        if bad_loco.empty:
            ok("All gate-pass genes have LOCO replication_rate = 1.0")
        else:
            fail(f"{len(bad_loco)} gate-pass genes have LOCO rate < 1.0")
        bad_het = df[df["heterogeneity_flag"] == True]  # noqa: E712
        if bad_het.empty:
            ok("No gate-pass genes have heterogeneity_flag = True")
        else:
            fail(f"{len(bad_het)} gate-pass genes have heterogeneity_flag = True")


# ── 6. Checksums ──────────────────────────────────────────────────────────
def check_checksums() -> None:
    if not CHECKSUMS.exists():
        fail(f"CHECKSUMS.txt missing at {CHECKSUMS.relative_to(BASE)}")
        return
    ok(f"CHECKSUMS.txt present")
    lines = CHECKSUMS.read_text().splitlines()
    for line in lines:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split(None, 1)
        if len(parts) != 2:
            continue
        expected_hash, rel_path = parts
        full_path = BASE / rel_path
        if not full_path.exists():
            fail(f"Checksummed file missing: {rel_path}")
            continue
        actual = hashlib.sha256(full_path.read_bytes()).hexdigest()
        if actual == expected_hash:
            ok(f"Checksum OK: {rel_path}")
        else:
            fail(f"Checksum MISMATCH: {rel_path}")


# ── 7. OXPHOS sentinel genes ──────────────────────────────────────────────
OXPHOS_GENES = {"MRPL33", "MRPL34", "NDUFB4", "APOO", "ATP5F1B", "CHCHD10", "CLTB"}


def check_oxphos_genes() -> None:
    gp = OUTPUT / "wp3_gate_pass.tsv"
    if not gp.exists():
        return
    df = pd.read_csv(gp, sep="\t")
    found = set(df["gene_symbol"]) & OXPHOS_GENES
    if found == OXPHOS_GENES:
        ok(f"All 7 OXPHOS sentinel genes present in gate-pass: {sorted(found)}")
    else:
        missing = OXPHOS_GENES - found
        fail(f"OXPHOS sentinel genes missing from gate-pass: {sorted(missing)}")


# ── Main ──────────────────────────────────────────────────────────────────
def main() -> None:
    print("=" * 60)
    print("HMSR WP3 Verifier")
    print("=" * 60)

    check_env()
    check_files()
    check_organisms()
    check_method_record()
    check_gate_pass()
    check_checksums()
    check_oxphos_genes()

    print("=" * 60)
    print(f"PASS: {len(PASSES)}  FAIL: {len(FAILS)}")

    if FAILS:
        # checksums only → NEEDS_REVIEW; any other failure → BLOCKED
        non_checksum_fails = [f for f in FAILS if "Checksum" not in f and "CHECKSUMS" not in f]
        if non_checksum_fails:
            print("STATUS=BLOCKED")
            sys.exit(1)
        else:
            print("STATUS=NEEDS_REVIEW")
            sys.exit(2)
    else:
        print("STATUS=PASS")
        sys.exit(0)


if __name__ == "__main__":
    main()
