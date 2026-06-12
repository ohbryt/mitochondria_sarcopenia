#!/usr/bin/env python3
"""
WP3d/WP3e — Two sensitivity analyses closing the Codex v0.3 review:

WP3e — Library-size QC covariate sensitivity.
  Cases have ~7-9% lower sequencing depth than controls in 3/4 cohorts (JSS 0.93,
  SSS 0.93, MOS 0.91), a potential compositional confound. We add per-sample
  log10(library size), z-scored, as a covariate and re-test the 7 highlighted genes
  + the mitochondrial enrichment.

WP3d — Freedman-Lane covariate-exchangeable permutation.
  The WP3c label-permutation holds age/sex fixed, so its null is not fully
  covariate-exchangeable (Codex MAJOR). Freedman-Lane (1983) fixes this: fit the
  reduced model Y~Z (covariates only), permute the reduced-model residuals, add back
  the reduced fitted values, refit the full model Y*~sarcopenia+Z. This permutes only
  the part of expression orthogonal to the covariates, so the null respects the
  age/sex structure. We recompute the gene-set competitive statistic over N permutations.

Output: output/signatures/wp3de_sensitivity.tsv + console summary.
"""
from __future__ import annotations

import os
import re
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

BASE = Path("/Volumes/4TB/exerciseomics/sarcopenia-multiomic-resource")
VALID = BASE / "data" / "validation_cohorts"
SIG = BASE / "output" / "signatures"

N_PERM = int(os.environ.get("WP3D_NPERM", "2000"))
SEED = 42
HIGHLIGHT = ["CHCHD10", "CLTB", "MRPL34", "APOO", "MRPL33", "NDUFB4", "ATP5F1B"]
MITO_PAT = re.compile(r"^(MRPL|MRPS|NDUF|ATP5|COX[0-9]|TIMM|TOMM|SDH|UQCR|CHCHD|COA|MICOS|IMMT|ATPAF)")
COHORTS = ["GSE111006_HSS", "GSE111010_JSS", "GSE111016_SSS", "GSE226151"]


def load(c: str):
    m = pd.read_csv(VALID / c / "metadata.tsv", sep="\t")
    m = m[m["include_strict_binary"].astype(bool)].copy().sort_values("sample_id")
    sids = m["sample_id"].tolist()
    E = pd.read_csv(VALID / c / "expression.tsv", sep="\t", index_col=0)
    E = E.loc[:, sids].apply(pd.to_numeric, errors="coerce").replace([np.inf, -np.inf], np.nan).dropna(axis=0, how="any")
    E = E.loc[E.var(axis=1) > 0]
    rc = pd.read_csv(VALID / c / "raw_counts.tsv", sep="\t", index_col=0)
    libsize = rc.reindex(columns=sids).sum(axis=0)
    lib_z = np.log10(libsize.to_numpy(dtype=float))
    lib_z = (lib_z - lib_z.mean()) / (lib_z.std(ddof=0) or 1.0)
    y = m["strict_sarcopenia_label"].astype(float).to_numpy()
    cov = {}
    age = pd.to_numeric(m.get("age"), errors="coerce")
    if age is not None and age.notna().all() and age.nunique() > 2 and age.std() > 0:
        cov["age_z"] = ((age - age.mean()) / age.std(ddof=0)).to_numpy()
    sex = m.get("sex")
    if sex is not None and sex.astype(str).str.lower().nunique() > 1:
        cov["sex_male"] = (sex.astype(str).str.lower().str.strip() == "male").astype(float).to_numpy()
    return E.index.to_numpy(), E.to_numpy(dtype=float), y, cov, lib_z


def ols_sarc_z(Y, y, cov, extra=None):
    """Vectorized OLS sarcopenia z for all genes (Y: genes x samples)."""
    n = Y.shape[1]
    cols = [np.ones(n), y] + list(cov.values())
    if extra is not None:
        cols.append(extra)
    X = np.column_stack(cols)
    dfr = n - np.linalg.matrix_rank(X)
    if dfr <= 0:
        return np.full(Y.shape[0], np.nan)
    XtXinv = np.linalg.pinv(X.T @ X)
    with np.errstate(divide="ignore", over="ignore", invalid="ignore"):
        B = Y @ X @ XtXinv.T
        resid = Y - B @ X.T
        sigma2 = (resid ** 2).sum(axis=1) / dfr
        se = np.sqrt(XtXinv[1, 1] * sigma2)
        z = B[:, 1] / se
    return z


# ───────────────────── WP3e: library-size covariate ─────────────────────
def dl_meta_p(betas, ses):
    import math
    m = np.isfinite(betas) & np.isfinite(ses) & (ses > 0)
    b, s = betas[m], ses[m]
    k = len(b)
    if k < 2:
        return np.nan
    wi = 1 / s**2
    W = wi.sum(); bfe = (wi*b).sum()/W
    Q = (wi*(b-bfe)**2).sum(); qdf = k-1
    C = W - (wi**2).sum()/W
    tau2 = max(0.0, (Q-qdf)/C) if C > 0 else 0.0
    wre = 1/(s**2+tau2)
    mb = (wre*b).sum()/wre.sum(); mse = math.sqrt(1/wre.sum())
    return float(2*stats.norm.sf(abs(mb/mse)))


def ols_sarc_beta_se(Y, y, cov, extra):
    n = Y.shape[1]
    cols = [np.ones(n), y] + list(cov.values()) + [extra]
    X = np.column_stack(cols)
    dfr = n - np.linalg.matrix_rank(X)
    XtXinv = np.linalg.pinv(X.T @ X)
    with np.errstate(divide="ignore", over="ignore", invalid="ignore"):
        B = Y @ X @ XtXinv.T
        resid = Y - B @ X.T
        sigma2 = (resid**2).sum(axis=1)/dfr
        se = np.sqrt(XtXinv[1, 1]*sigma2)
    return B[:, 1], se


def run_libsize(cohorts):
    print("\n=== WP3e — library-size covariate sensitivity (7 highlighted genes) ===")
    # per gene collect beta/se across cohorts
    from collections import defaultdict
    store = defaultdict(lambda: ([], []))
    for genes, Y, y, cov, lib_z in cohorts:
        b, se = ols_sarc_beta_se(Y, y, cov, lib_z)
        for g, bb, ss in zip(genes, b, se):
            store[g][0].append(bb); store[g][1].append(ss)
    rows = []
    for g in HIGHLIGHT:
        if g in store:
            p = dl_meta_p(np.array(store[g][0]), np.array(store[g][1]))
            rows.append(dict(gene=g, libadj_meta_p=p, survives=bool(p < 0.005)))
            print(f"  {g:9s} libsize-adjusted meta-p = {p:.2e}  {'SURVIVES' if p<0.005 else 'attenuated'}")
    n_surv = sum(r["survives"] for r in rows)
    print(f"  -> {n_surv}/7 survive at meta-p<0.005 after library-size adjustment")
    return rows


# ───────────────────── WP3d: Freedman-Lane permutation ─────────────────────
def stouffer_meta(per_cohort_z, maps, nG):
    sz = np.zeros(nG); cnt = np.zeros(nG)
    for z, idx in zip(per_cohort_z, maps):
        fin = np.isfinite(z)
        np.add.at(sz, idx[fin], z[fin]); np.add.at(cnt, idx[fin], 1.0)
    with np.errstate(divide="ignore", invalid="ignore"):
        return np.where(cnt > 0, sz/np.sqrt(cnt), np.nan)


def run_freedman_lane(cohorts):
    print(f"\n=== WP3d — Freedman-Lane covariate-exchangeable permutation (N={N_PERM}) ===")
    master = sorted(set().union(*[set(g) for g, *_ in cohorts]))
    posn = {g: i for i, g in enumerate(master)}
    maps = [np.array([posn[g] for g in genes], dtype=np.intp) for genes, *_ in cohorts]
    nG = len(master)

    SETS = {
        "Mito_ALL": MITO_PAT,
        "Mito_ComplexI_NDUF": re.compile(r"^NDUF"),
        "Mito_ComplexV_ATP5": re.compile(r"^ATP5"),
        "Mito_mitoribosome": re.compile(r"^(MRPL|MRPS)"),
        "Mito_cristae_MICOS": re.compile(r"^(CHCHD|APOO|MICOS|IMMT|MICU)"),
        "Mito_import": re.compile(r"^(TIMM|TOMM)"),
        "Mito_ComplexII_III_IV": re.compile(r"^(SDH[ABCD]|UQCR|COX[0-9])"),
        "Control_cyto_ribosome": re.compile(r"^(RPL|RPS)"),
        "Control_proteasome": re.compile(r"^PSM"),
    }
    masks = {k: np.array([bool(p.match(g)) for g in master]) for k, p in SETS.items()}

    # precompute per-cohort reduced-model fitted F, residuals R, full-model extractors
    pc = []
    for genes, Y, y, cov, lib_z in cohorts:
        n = Y.shape[1]
        Z = np.column_stack([np.ones(n)] + list(cov.values()))           # reduced design (covars only)
        HZ = Z @ np.linalg.pinv(Z.T @ Z) @ Z.T
        F = Y @ HZ.T                                                       # reduced fitted (genes x n)
        R = Y - F                                                          # reduced residuals
        W = np.column_stack([np.ones(n), y] + list(cov.values()))         # full design (sarc = col 1)
        WtWinv = np.linalg.pinv(W.T @ W)
        cX = (WtWinv @ W.T)[1]                                            # X-coef extractor (1 x n)
        HW = W @ WtWinv @ W.T
        dfr = n - np.linalg.matrix_rank(W)
        seX_const = np.sqrt(WtWinv[1, 1])
        pc.append((F, R, cX, HW, dfr, seX_const, n))

    def set_diff(mz, mask):
        fin = np.isfinite(mz); inm = mask & fin; outm = (~mask) & fin
        return float(mz[inm].mean() - mz[outm].mean()) if inm.sum() >= 3 else np.nan

    def perm_zvecs(perms):
        zs = []
        for (F, R, cX, HW, dfr, seX_const, n), perm in zip(pc, perms):
            Ystar = F + R[:, perm]
            with np.errstate(divide="ignore", over="ignore", invalid="ignore"):
                bX = Ystar @ cX
                resid = Ystar - Ystar @ HW.T
                sigma2 = (resid**2).sum(axis=1) / dfr
                se = seX_const * np.sqrt(sigma2)
                zs.append(bX / se)
        return zs

    ident = [np.arange(p[6]) for p in pc]
    mz_obs = stouffer_meta(perm_zvecs(ident), maps, nG)
    observed = {k: set_diff(mz_obs, m) for k, m in masks.items()}

    rng = np.random.default_rng(SEED)
    null = {k: np.empty(N_PERM) for k in SETS}
    for i in range(N_PERM):
        perms = [rng.permutation(p[6]) for p in pc]
        mz = stouffer_meta(perm_zvecs(perms), maps, nG)
        for k, m in masks.items():
            null[k][i] = set_diff(mz, m)
        if (i+1) % 500 == 0:
            print(f"  ... {i+1}/{N_PERM}")

    rows = []
    for k in SETS:
        nn = null[k][np.isfinite(null[k])]
        obs = observed[k]
        emp_p = (1 + np.sum(nn <= obs)) / (1 + len(nn))
        z = (obs - nn.mean()) / (nn.std() or np.nan)
        rows.append(dict(gene_set=k, observed_diff=obs, fl_perm_p=emp_p, fl_z_vs_null=z))
        tag = "down" if obs < 0 else "up"
        print(f"  {k:24s} obs={obs:+.3f} ({tag}) FL_perm_p={emp_p:.2e} z={z:+.2f}")
    return rows


def main():
    print("=" * 70)
    print("WP3d/3e — Freedman-Lane + library-size sensitivities (Codex closure)")
    print("=" * 70)
    cohorts = [load(c) for c in COHORTS]
    lib_rows = run_libsize(cohorts)
    fl_rows = run_freedman_lane(cohorts)

    pd.DataFrame(fl_rows).to_csv(SIG / "wp3d_freedman_lane.tsv", sep="\t", index=False)
    pd.DataFrame(lib_rows).to_csv(SIG / "wp3e_libsize_sensitivity.tsv", sep="\t", index=False)
    print(f"\nWrote: {SIG/'wp3d_freedman_lane.tsv'}")
    print(f"Wrote: {SIG/'wp3e_libsize_sensitivity.tsv'}")


if __name__ == "__main__":
    main()
