#!/usr/bin/env python3
"""
WP3c-perm — Correlation-aware permutation test for mitochondrial gene-set down-shift.

The hypergeometric (p=6.7e-18) and the plain Mann-Whitney (p=1.8e-64) BOTH assume
gene independence and are inflated on co-regulated modules. This test fixes that:
we permute the case/control label WITHIN each cohort and recompute the entire
per-gene meta statistic. Because all genes are recomputed under the same permuted
labels, the gene-gene correlation structure is preserved in the null, so the
empirical p-value is genuinely correlation-aware (this is what CAMERA approximates
analytically via a variance-inflation factor).

Statistic: competitive mean-meta-z difference (in-set minus out-set).
Both observed and null use the SAME fast fixed-effect inverse-variance meta-z for
consistency (validity comes from identical treatment, not from the meta flavour).

Output: output/signatures/wp3c_permutation.tsv + console summary.
Runtime: ~1-3 min for N permutations (vectorized OLS).
"""
from __future__ import annotations

import re
from pathlib import Path

import numpy as np
import pandas as pd

BASE = Path("/Volumes/4TB/exerciseomics/sarcopenia-multiomic-resource")
VALID = BASE / "data" / "validation_cohorts"
INV = BASE / "output" / "validation" / "cohort_inventory.tsv"
SIG = BASE / "output" / "signatures"

import os
N_PERM = int(os.environ.get("WP3C_NPERM", "2000"))
SEED = 42  # recorded; np.random.default_rng seeded (allowed — not global Math.random)

MITO_SETS = {
    "Mito_ALL": r"^(MRPL|MRPS|NDUF|ATP5|COX[0-9]|TIMM|TOMM|SDH|UQCR|CHCHD|COA|MICOS|IMMT|ATPAF)",
    "Mito_ComplexI_NDUF": r"^NDUF",
    "Mito_ComplexV_ATP5": r"^ATP5",
    "Mito_mitoribosome": r"^(MRPL|MRPS)",
    "Mito_cristae_MICOS": r"^(CHCHD|APOO|MICOS|IMMT|MICU)",
    "Mito_import_TIMM_TOMM": r"^(TIMM|TOMM)",
    "Mito_ComplexII_III_IV": r"^(SDH[ABCD]|UQCR|COX[0-9])",
    # control
    "Control_cyto_ribosome": r"^(RPL|RPS)",
    "Control_proteasome": r"^PSM",
    "Control_collagen": r"^COL[0-9]",
}


def load_cohort(c: str):
    meta = pd.read_csv(VALID / c / "metadata.tsv", sep="\t")
    meta = meta[meta["include_strict_binary"].astype(bool)].copy().sort_values("sample_id")
    sids = meta["sample_id"].tolist()
    E = pd.read_csv(VALID / c / "expression.tsv", sep="\t", index_col=0)
    E = E.loc[:, sids].apply(pd.to_numeric, errors="coerce")
    E = E.replace([np.inf, -np.inf], np.nan).dropna(axis=0, how="any")
    E = E.loc[E.var(axis=1) > 0]
    # covariate columns (age_z, sex_male) — fixed across permutations
    cov = {}
    age = pd.to_numeric(meta.get("age"), errors="coerce")
    if age is not None and age.notna().all() and age.nunique() > 2 and age.std() > 0:
        cov["age_z"] = ((age - age.mean()) / age.std(ddof=0)).to_numpy()
    sex = meta.get("sex")
    if sex is not None and sex.astype(str).str.lower().nunique() > 1:
        cov["sex_male"] = (sex.astype(str).str.lower().str.strip() == "male").astype(float).to_numpy()
    y = meta["strict_sarcopenia_label"].astype(float).to_numpy()
    return E.index.to_numpy(), E.to_numpy(dtype=float), y, cov


def cohort_z(Y: np.ndarray, y: np.ndarray, cov: dict) -> np.ndarray:
    """Vectorized OLS sarcopenia z-score for all genes (Y: genes x samples)."""
    n = Y.shape[1]
    cols = [np.ones(n), y] + list(cov.values())
    X = np.column_stack(cols)
    k = X.shape[1]
    dfr = n - np.linalg.matrix_rank(X)
    if dfr <= 0:
        return np.full(Y.shape[0], np.nan)
    XtXinv = np.linalg.pinv(X.T @ X)
    B = Y @ X @ XtXinv.T               # genes x k
    resid = Y - B @ X.T                # genes x samples
    sigma2 = (resid ** 2).sum(axis=1) / dfr
    se = np.sqrt(XtXinv[1, 1] * sigma2)
    with np.errstate(divide="ignore", invalid="ignore"):
        z = B[:, 1] / se
    return z


def build_master_index(cohorts):
    """Master gene list + per-cohort row->master index maps (vectorized scatter-add)."""
    master = sorted(set().union(*[set(genes) for genes, *_ in cohorts]))
    pos = {g: i for i, g in enumerate(master)}
    maps = [np.array([pos[g] for g in genes], dtype=np.intp) for genes, *_ in cohorts]
    return np.array(master), maps


def meta_z_fast(cohorts, maps, n_master, labels: list) -> np.ndarray:
    """Stouffer meta-z per master gene; pure-numpy scatter-add (no Python gene loop)."""
    sz = np.zeros(n_master)
    cnt = np.zeros(n_master)
    for (genes, Y, _y, cov), idx, yy in zip(cohorts, maps, labels):
        z = cohort_z(Y, yy, cov)
        finite = np.isfinite(z)
        np.add.at(sz, idx[finite], z[finite])
        np.add.at(cnt, idx[finite], 1.0)
    with np.errstate(divide="ignore", invalid="ignore"):
        mz = np.where(cnt > 0, sz / np.sqrt(cnt), np.nan)
    return mz


def main() -> None:
    print("=" * 70)
    print(f"WP3c-perm — label-permutation competitive test (N={N_PERM}, seed={SEED})")
    print("=" * 70)
    cohort_names = ["GSE111006_HSS", "GSE111010_JSS", "GSE111016_SSS", "GSE226151"]
    cohorts = [load_cohort(c) for c in cohort_names]
    master, maps = build_master_index(cohorts)
    nG = len(master)

    # precompute boolean set masks over master gene list
    set_masks = {name: np.array([bool(re.match(pat, g)) for g in master])
                 for name, pat in MITO_SETS.items()}

    def set_stat_vec(mz: np.ndarray, mask: np.ndarray) -> float:
        fin = np.isfinite(mz)
        inm = mask & fin
        outm = (~mask) & fin
        if inm.sum() < 3:
            return np.nan
        return float(mz[inm].mean() - mz[outm].mean())

    # observed
    base_labels = [y for (_, _, y, _) in cohorts]
    mz_obs = meta_z_fast(cohorts, maps, nG, base_labels)
    observed = {name: (set_stat_vec(mz_obs, m), int((m & np.isfinite(mz_obs)).sum()))
                for name, m in set_masks.items()}

    # permutations
    rng = np.random.default_rng(SEED)
    null_stats = {name: np.empty(N_PERM) for name in MITO_SETS}
    for p in range(N_PERM):
        labels = [rng.permutation(y) for (_, _, y, _) in cohorts]
        mz = meta_z_fast(cohorts, maps, nG, labels)
        for name, m in set_masks.items():
            null_stats[name][p] = set_stat_vec(mz, m)
        if (p + 1) % 500 == 0:
            print(f"  ... {p+1}/{N_PERM} permutations")

    rows = []
    for name in MITO_SETS:
        obs, n = observed[name]
        null = null_stats[name]
        null = null[np.isfinite(null)]
        # one-sided: how often null is as DOWN (<=) as observed
        emp_p = (1 + np.sum(null <= obs)) / (1 + len(null))
        null_mean = float(np.mean(null))
        null_sd = float(np.std(null))
        zvn = (obs - null_mean) / null_sd if null_sd > 0 else np.nan
        # parametric tail p (permutation null ~ Gaussian by CLT over many genes)
        from scipy import stats as _st
        param_p = float(_st.norm.sf(abs(zvn))) if np.isfinite(zvn) else np.nan
        rows.append(dict(gene_set=name, n_genes=n, observed_diff=obs,
                         null_mean=null_mean, null_sd=null_sd, z_vs_null=zvn,
                         perm_p_one_sided_down=emp_p, parametric_p=param_p))
    out = pd.DataFrame(rows).sort_values("observed_diff")
    out.to_csv(SIG / "wp3c_permutation.tsv", sep="\t", index=False)

    print("\n=== Permutation competitive test (observed in-minus-out mean meta-z) ===")
    disp = out.copy()
    for c in ["observed_diff", "null_mean", "null_sd", "z_vs_null"]:
        disp[c] = disp[c].map(lambda v: f"{v:+.3f}" if np.isfinite(v) else "NA")
    disp["perm_p_one_sided_down"] = disp["perm_p_one_sided_down"].map(lambda v: f"{v:.2e}")
    print(disp[["gene_set", "n_genes", "observed_diff", "null_sd", "z_vs_null", "perm_p_one_sided_down"]].to_string(index=False))
    print(f"\nN_PERM={N_PERM} → minimum resolvable p = {1/(N_PERM+1):.2e}")
    print(f"Wrote: {SIG/'wp3c_permutation.tsv'}")


if __name__ == "__main__":
    main()
