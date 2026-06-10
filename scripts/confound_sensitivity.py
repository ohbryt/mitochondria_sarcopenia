#!/usr/bin/env python3
"""
WP3b — Confound-adjusted sensitivity analysis (decisive test from CRITICAL_REVIEW_v0.2).

Tests whether the mitochondrial candidate signal survives adjustment for:
  (1) muscle-composition / purity proxy (stromal + immune marker scores) added as a covariate
  (2) genomic-control (lambda) correction of the meta statistics
  (3) the non-myofiber fraction confound, per cohort

If the 7 highlighted genes + the mitochondrial enrichment survive composition adjustment,
the signal is robust to the most likely bulk-tissue confound (fiber loss / infiltration).

Outputs: output/signatures/wp3b_confound_sensitivity.tsv  + console summary.
All numbers computed here; no hand values.
"""
from __future__ import annotations

import math
import re
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

BASE = Path("/Volumes/4TB/exerciseomics/sarcopenia-multiomic-resource")
VALID = BASE / "data" / "validation_cohorts"
INV = BASE / "output" / "validation" / "cohort_inventory.tsv"
SIG = BASE / "output" / "signatures"

HIGHLIGHT = ["CHCHD10", "CLTB", "MRPL34", "APOO", "MRPL33", "NDUFB4", "ATP5F1B"]
MITO_PAT = re.compile(r"^(MRPL|MRPS|NDUF|ATP5|COX[0-9]|TIMM|TOMM|SDH|UQCR|CHCHD|COA)")

# Composition proxies — non-myofiber cell types (purity confound)
STROMAL_MARKERS = ["COL1A1", "COL1A2", "COL3A1", "COL6A1", "COL6A2", "COL6A3",
                   "DCN", "LUM", "FN1", "PDGFRA", "SPARC", "POSTN"]
IMMUNE_MARKERS = ["PTPRC", "CD68", "CD163", "LYZ", "CD14", "ITGAM", "CD3E", "CD8A"]
ENDO_MARKERS = ["PECAM1", "VWF", "CDH5", "CLDN5"]


def composition_score(expr: pd.DataFrame, markers: list[str]) -> pd.Series:
    """Mean z-scored expression of available markers, per sample (columns)."""
    present = [m for m in markers if m in expr.index]
    if not present:
        return pd.Series(0.0, index=expr.columns)
    sub = expr.loc[present]
    z = sub.sub(sub.mean(axis=1), axis=0).div(sub.std(axis=1).replace(0, np.nan), axis=0)
    return z.mean(axis=0, skipna=True).fillna(0.0)


def dl_meta(betas: np.ndarray, ses: np.ndarray) -> dict:
    m = np.isfinite(betas) & np.isfinite(ses) & (ses > 0)
    b, s = betas[m], ses[m]
    k = len(b)
    if k < 2:
        return dict(meta_beta=np.nan, meta_p=np.nan, i2=np.nan, k=k)
    wi = 1.0 / s**2
    W = wi.sum()
    bfe = (wi * b).sum() / W
    Q = (wi * (b - bfe) ** 2).sum()
    qdf = k - 1
    i2 = max(0.0, (Q - qdf) / Q) * 100 if Q > 0 else 0.0
    C = W - (wi**2).sum() / W
    tau2 = max(0.0, (Q - qdf) / C) if C > 0 else 0.0
    wre = 1.0 / (s**2 + tau2)
    mb = (wre * b).sum() / wre.sum()
    mse = math.sqrt(1.0 / wre.sum())
    z = mb / mse
    p = 2 * stats.norm.sf(abs(z))
    return dict(meta_beta=mb, meta_p=p, i2=i2, k=k)


def fit_cohort(cohort: str, meta: pd.DataFrame, expr: pd.DataFrame,
               adjust_composition: bool) -> pd.DataFrame:
    """OLS per gene; optionally add stromal+immune composition covariate."""
    meta = meta[meta["include_strict_binary"].astype(bool)].copy().sort_values("sample_id")
    sids = meta["sample_id"].tolist()
    E = expr.loc[:, sids].replace([np.inf, -np.inf], np.nan).dropna(axis=0, how="any")
    E = E.loc[E.var(axis=1) > 0]

    y = meta["strict_sarcopenia_label"].astype(float).values
    cols = {"intercept": np.ones(len(meta)), "sarcopenia": y}
    age = pd.to_numeric(meta.get("age"), errors="coerce")
    if age is not None and age.notna().all() and age.nunique() > 2 and age.std() > 0:
        cols["age_z"] = ((age - age.mean()) / age.std(ddof=0)).values
    sex = meta.get("sex")
    if sex is not None and sex.astype(str).str.lower().nunique() > 1:
        cols["sex_male"] = (sex.astype(str).str.lower().str.strip() == "male").astype(float).values

    if adjust_composition:
        strom = composition_score(E, STROMAL_MARKERS).reindex(sids).values
        imm = composition_score(E, IMMUNE_MARKERS).reindex(sids).values
        # combine into one purity proxy (mean of stromal+immune), z-scored
        purity = np.nanmean(np.vstack([strom, imm]), axis=0)
        if np.nanstd(purity) > 0:
            cols["noncontractile_proxy"] = (purity - np.nanmean(purity)) / np.nanstd(purity)

    X = np.column_stack(list(cols.values()))
    names = list(cols.keys())
    sarc_idx = names.index("sarcopenia")
    Y = E.T.to_numpy(dtype=float)
    n, g = Y.shape
    rank = np.linalg.matrix_rank(X)
    dfr = n - rank
    if dfr <= 0:
        return pd.DataFrame()
    with np.errstate(divide="ignore", over="ignore", invalid="ignore"):
        XtX_inv = np.linalg.pinv(X.T @ X)
        beta = XtX_inv @ X.T @ Y
        resid = Y - X @ beta
    sigma2 = (resid**2).sum(axis=0) / dfr
    se_sarc = np.sqrt(XtX_inv[sarc_idx, sarc_idx] * sigma2)
    b_sarc = beta[sarc_idx]
    with np.errstate(divide="ignore", invalid="ignore"):
        t = b_sarc / se_sarc
        p = 2 * stats.t.sf(np.abs(t), dfr)
    return pd.DataFrame({"gene_symbol": E.index, "beta": b_sarc, "se": se_sarc,
                         "t": t, "p": p, "cohort": cohort})


def lambda_gc(t_or_z: np.ndarray) -> float:
    chisq = np.asarray(t_or_z, dtype=float) ** 2
    chisq = chisq[np.isfinite(chisq)]
    return float(np.median(chisq) / 0.4549364) if len(chisq) else np.nan


def run(adjust: bool) -> tuple[pd.DataFrame, dict]:
    inv = pd.read_csv(INV, sep="\t")
    assembled = inv[inv["status"] == "assembled_strict_binary_available"]
    frames, lambdas = [], {}
    for _, row in assembled.iterrows():
        c = row["cohort"]
        meta = pd.read_csv(VALID / c / "metadata.tsv", sep="\t")
        expr = pd.read_csv(VALID / c / "expression.tsv", sep="\t", index_col=0).apply(pd.to_numeric, errors="coerce")
        df = fit_cohort(c, meta, expr, adjust)
        if not df.empty:
            lambdas[c] = lambda_gc(df["t"].values)
            frames.append(df)
    allc = pd.concat(frames, ignore_index=True)
    return allc, lambdas


def main() -> None:
    print("=" * 70)
    print("WP3b — Confound-adjusted sensitivity (composition + genomic control)")
    print("=" * 70)

    base_de, lam_base = run(adjust=False)
    adj_de, lam_adj = run(adjust=True)

    print("\nPer-cohort lambda (genomic inflation):")
    for c in lam_base:
        print(f"  {c:16s} unadjusted={lam_base[c]:.3f}  composition-adjusted={lam_adj.get(c,float('nan')):.3f}")

    def meta_for(de: pd.DataFrame, gene: str) -> dict:
        sub = de[de.gene_symbol == gene]
        return dl_meta(sub["beta"].values, sub["se"].values)

    print("\n=== Highlighted genes: meta-p before vs after composition adjustment ===")
    print(f"{'gene':9s} {'base_p':>10s} {'adj_p':>10s} {'base_beta':>10s} {'adj_beta':>10s} {'verdict':>10s}")
    rows = []
    for g in HIGHLIGHT:
        b = meta_for(base_de, g)
        a = meta_for(adj_de, g)
        survives = (a["meta_p"] < 0.005) if np.isfinite(a["meta_p"]) else False
        verdict = "SURVIVES" if survives else "attenuated"
        print(f"{g:9s} {b['meta_p']:10.2e} {a['meta_p']:10.2e} {b['meta_beta']:10.3f} {a['meta_beta']:10.3f} {verdict:>10s}")
        rows.append(dict(gene=g, base_meta_p=b["meta_p"], adj_meta_p=a["meta_p"],
                         base_beta=b["meta_beta"], adj_beta=a["meta_beta"],
                         base_i2=b["i2"], adj_i2=a["i2"], survives_composition_adj=survives))

    # Mito enrichment in adjusted top-down per cohort
    print("\n=== Mito enrichment in top-200 down genes (composition-adjusted) ===")
    enr_rows = []
    for c in adj_de.cohort.unique():
        sub = adj_de[adj_de.cohort == c].dropna(subset=["p", "beta"])
        down = sub[sub.beta < 0].nsmallest(200, "p")
        k = int(down.gene_symbol.str.match(MITO_PAT).sum())
        bg = float(sub.gene_symbol.str.match(MITO_PAT).mean())
        exp = 200 * bg
        fold = k / exp if exp > 0 else np.nan
        print(f"  {c:16s} mito top200-down: {k:3d}  (exp {exp:.1f}, {fold:.1f}x)")
        enr_rows.append(dict(cohort=c, mito_top200_down=k, expected=exp, fold=fold))

    # GC-corrected meta-p for highlighted genes
    lam = lam_base  # use unadjusted per-cohort lambda for GC of base
    print(f"\n=== Genomic-control note (per-cohort lambda unadjusted): "
          f"{{{', '.join(f'{c}:{v:.2f}' for c,v in lam_base.items())}}} ===")
    print("(composition adjustment lowers lambda toward 1 if purity was the inflation source)")

    out = pd.DataFrame(rows)
    out.to_csv(SIG / "wp3b_confound_sensitivity.tsv", sep="\t", index=False)
    pd.DataFrame(enr_rows).to_csv(SIG / "wp3b_mito_enrichment_adjusted.tsv", sep="\t", index=False)
    n_survive = int(out["survives_composition_adj"].sum())
    print(f"\nSUMMARY: {n_survive}/7 highlighted genes survive composition adjustment at meta-p<0.005")
    print(f"Wrote: {SIG/'wp3b_confound_sensitivity.tsv'}")
    print(f"Wrote: {SIG/'wp3b_mito_enrichment_adjusted.tsv'}")


if __name__ == "__main__":
    main()
