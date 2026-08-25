#!/usr/bin/env python3
"""Extract an auditable single-target view from frozen HMSR result matrices."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from collections import defaultdict
from pathlib import Path


GENE_RE = re.compile(r"^[A-Za-z0-9_.-]+$")


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _read_matching_rows(path: Path, gene: str) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        if reader.fieldnames is None or "gene_symbol" not in reader.fieldnames:
            raise ValueError(f"{path} lacks a gene_symbol column")
        rows = [row for row in reader if row["gene_symbol"] == gene]
        return list(reader.fieldnames), rows


def _write_tsv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle, fieldnames=fieldnames, delimiter="\t", lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(rows)


def extract_target_evidence(
    *,
    differential_path: Path,
    replication_path: Path,
    gene: str,
    output_dir: Path,
    audit_date: str,
) -> dict[str, object]:
    gene = gene.upper()
    if not GENE_RE.fullmatch(gene):
        raise ValueError(f"invalid gene symbol: {gene!r}")

    differential_fields, cohort_rows = _read_matching_rows(differential_path, gene)
    replication_fields, meta_rows = _read_matching_rows(replication_path, gene)
    if not cohort_rows:
        raise ValueError(f"{gene} is absent from {differential_path}")
    if len(meta_rows) != 1:
        raise ValueError(
            f"expected exactly one {gene} row in {replication_path}; found {len(meta_rows)}"
        )

    cohort_rows.sort(key=lambda row: row["cohort"])
    meta = meta_rows[0]
    source_group_directions: dict[str, set[str]] = defaultdict(set)
    for row in cohort_rows:
        source_group_directions[row["source_group"]].add(row["direction"])

    collapsed_directions = {
        group: next(iter(directions)) if len(directions) == 1 else "mixed"
        for group, directions in sorted(source_group_directions.items())
    }
    meta_direction = meta["meta_direction"]
    source_groups_matching_meta = sum(
        direction == meta_direction for direction in collapsed_directions.values()
    )
    meta_fdr = float(meta["meta_fdr"])
    replicated_across_source_groups = source_groups_matching_meta >= 2

    cohort_output = output_dir / f"{gene}_differential_by_cohort.tsv"
    meta_output = output_dir / f"{gene}_replication.tsv"
    claims_output = output_dir / f"{gene}_claims.json"
    _write_tsv(cohort_output, differential_fields, cohort_rows)
    _write_tsv(meta_output, replication_fields, meta_rows)

    claims: dict[str, object] = {
        "protocol_id": "HMSR-TARGET-AUDIT-1.0.0",
        "audit_date": audit_date,
        "gene_symbol": gene,
        "detected_modality": "bulk_transcriptomics",
        "source_artifacts": {
            "differential_by_cohort": {
                "filename": differential_path.name,
                "sha256": _sha256(differential_path),
            },
            "replication_matrix": {
                "filename": replication_path.name,
                "sha256": _sha256(replication_path),
            },
        },
        "cohort_summary": {
            "cohorts_detected": len(cohort_rows),
            "independent_source_groups": len(source_group_directions),
            "strict_binary_samples": sum(int(row["n_samples"]) for row in cohort_rows),
            "cases": sum(int(row["n_cases"]) for row in cohort_rows),
            "controls": sum(int(row["n_controls"]) for row in cohort_rows),
            "source_group_directions": collapsed_directions,
        },
        "meta_result": {
            "direction": meta_direction,
            "beta": float(meta["meta_beta"]),
            "se": float(meta["meta_se"]),
            "p_value": float(meta["meta_p_value"]),
            "fdr": meta_fdr,
            "heterogeneity_i2": float(meta["heterogeneity_i2"]),
            "heterogeneity_flag": meta["heterogeneity_flag"].lower() == "true",
            "leave_one_cohort_out_replication_rate": float(
                meta["leave_one_cohort_out_replication_rate"]
            ),
        },
        "gates": {
            "genome_wide_fdr_below_0_05": meta_fdr < 0.05,
            "same_direction_in_at_least_two_independent_source_groups": (
                replicated_across_source_groups
            ),
            "functional_or_causal_evidence": False,
        },
        "status": (
            "SUPPORTED_OBSERVATIONAL_ASSOCIATION"
            if meta_fdr < 0.05 and replicated_across_source_groups
            else "NOT_REPLICATED"
        ),
    }
    claims_output.write_text(
        json.dumps(claims, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    return claims


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--differential", type=Path, required=True)
    parser.add_argument("--replication", type=Path, required=True)
    parser.add_argument("--gene", required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--audit-date", default="2026-08-25")
    return parser


def main() -> None:
    args = _parser().parse_args()
    claims = extract_target_evidence(
        differential_path=args.differential,
        replication_path=args.replication,
        gene=args.gene,
        output_dir=args.output_dir,
        audit_date=args.audit_date,
    )
    print(f"STATUS={claims['status']}")


if __name__ == "__main__":
    main()
