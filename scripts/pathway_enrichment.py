#!/usr/bin/env python3
"""
WP3c-descriptive — gene-set DIRECTION/EFFECT-SIZE summary on the full ranked meta-z.

NOTE ON INFERENCE: the AUC and mean-z here are valid DESCRIPTIVE effect sizes
(correlation inflates variance, not the point estimate). The Mann-Whitney p-values
below are NOT correlation-aware — mitochondrial genes are co-regulated, so these
p-values are inflated exactly like the hypergeometric. Use them only to rank/sort.
The valid, correlation-aware INFERENCE is the label-permutation test in
`pathway_permutation.py` (-> wp3c_permutation.tsv), which preserves gene-gene
correlation under the null. This script is the descriptive companion to that test.

Decomposes the mitochondrial program into sub-modules (OXPHOS complexes I-V,
mitoribosome, MICOS/cristae, import) and benchmarks against non-mitochondrial
control sets for specificity, all on the FULL ranked list (gate-independent).

Output: output/signatures/wp3c_pathway_enrichment.tsv + console summary.
"""
from __future__ import annotations

import re
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

BASE = Path("/Volumes/4TB/exerciseomics/sarcopenia-multiomic-resource")
SIG = BASE / "output" / "signatures"

rep = pd.read_csv(SIG / "replication_matrix.tsv", sep="\t")
rep = rep.dropna(subset=["meta_z"]).copy()
rep["gene_symbol"] = rep["gene_symbol"].astype(str)

# ── Gene sets (pattern-based + curated), mitochondrial sub-programs ──────────
def by_pattern(pat: str) -> set[str]:
    p = re.compile(pat)
    return set(rep.loc[rep.gene_symbol.str.match(p), "gene_symbol"])

GENE_SETS: dict[str, set[str]] = {
    # Mitochondrial sub-programs
    "Mito: respiratory Complex I (NDUF)": by_pattern(r"^NDUF"),
    "Mito: ATP synthase Complex V (ATP5)": by_pattern(r"^ATP5"),
    "Mito: Complex II/III/IV (SDH/UQCR/COX)": by_pattern(r"^(SDH[ABCD]|UQCR|COX[0-9]|COX[12][0-9]?$|COX4|COX5|COX6|COX7|COX8)"),
    "Mito: mitoribosome (MRPL/MRPS)": by_pattern(r"^(MRPL|MRPS)"),
    "Mito: cristae/MICOS (CHCHD/APOO/IMMT/MICOS)": (by_pattern(r"^(CHCHD|APOO|MICOS|IMMT|APOOL|MICU)")),
    "Mito: import (TIMM/TOMM)": by_pattern(r"^(TIMM|TOMM)"),
    # Aggregate mitochondrial
    "Mito: ALL (broad nuclear-encoded)": by_pattern(r"^(MRPL|MRPS|NDUF|ATP5|COX[0-9]|TIMM|TOMM|SDH|UQCR|CHCHD|COA|MICOS|IMMT|ATP5F|ATPAF)"),
    # Non-mitochondrial CONTROL sets (specificity benchmark)
    "Control: cytoplasmic ribosome (RPL/RPS)": by_pattern(r"^(RPL|RPS)(?!.*MT)"),
    "Control: proteasome (PSM)": by_pattern(r"^PSM"),
    "Control: collagen/ECM (COL)": by_pattern(r"^COL[0-9]"),
    "Control: histone (HIST/H[1-4])": by_pattern(r"^(HIST|H2A|H2B|H3C|H4C)"),
}


def competitive_test(in_genes: set[str]) -> dict:
    """Descriptive in-set vs out-set summary (AUC + mean-z valid; U_p NOT
    correlation-aware -> ranking only; see pathway_permutation.py for inference)."""
    z = rep.set_index("gene_symbol")["meta_z"]
    in_z = z[z.index.isin(in_genes)].to_numpy()
    out_z = z[~z.index.isin(in_genes)].to_numpy()
    n_in = len(in_z)
    if n_in < 3:
        return dict(n=n_in, direction="NA", U_p=np.nan, mean_z=np.nan, auc=np.nan)
    # two-sided Mann-Whitney on signed z (tests if set is shifted up/down vs rest)
    U, p = stats.mannwhitneyu(in_z, out_z, alternative="two-sided")
    auc = U / (len(in_z) * len(out_z))  # prob(in > out); <0.5 means set shifted DOWN
    direction = "down" if np.median(in_z) < 0 else "up"
    return dict(n=n_in, direction=direction, U_p=float(p),
                mean_z=float(np.mean(in_z)), median_z=float(np.median(in_z)), auc=float(auc))


def main() -> None:
    print("=" * 72)
    print("WP3c — Competitive gene-set enrichment on full ranked meta-z (N=%d genes)" % len(rep))
    print("=" * 72)
    rows = []
    for name, genes in GENE_SETS.items():
        r = competitive_test(genes)
        rows.append(dict(gene_set=name, **r))
    out = pd.DataFrame(rows)
    # BH across all sets
    pvals = out["U_p"].to_numpy()
    finite = np.isfinite(pvals)
    bh = np.full(len(pvals), np.nan)
    if finite.any():
        pv = pvals[finite]
        order = np.argsort(pv)
        ranked = pv[order]
        n = len(ranked)
        adj = np.minimum.accumulate((ranked * n / np.arange(1, n + 1))[::-1])[::-1]
        bh_sorted = np.clip(adj, 0, 1)
        tmp = np.empty(n)
        tmp[order] = bh_sorted
        bh[np.where(finite)[0]] = tmp
    out["U_fdr"] = bh

    out = out.sort_values("U_p", na_position="last")
    cols = ["gene_set", "n", "direction", "mean_z", "auc", "U_p", "U_fdr"]
    disp = out[cols].copy()
    disp["mean_z"] = disp["mean_z"].map(lambda v: f"{v:+.3f}" if np.isfinite(v) else "NA")
    disp["auc"] = disp["auc"].map(lambda v: f"{v:.3f}" if np.isfinite(v) else "NA")
    disp["U_p"] = disp["U_p"].map(lambda v: f"{v:.2e}" if np.isfinite(v) else "NA")
    disp["U_fdr"] = disp["U_fdr"].map(lambda v: f"{v:.2e}" if np.isfinite(v) else "NA")
    print(disp.to_string(index=False))

    out.to_csv(SIG / "wp3c_pathway_enrichment.tsv", sep="\t", index=False)
    print(f"\nWrote: {SIG/'wp3c_pathway_enrichment.tsv'}")

    # Lead-program callout
    mito = out[out.gene_set.str.startswith("Mito:") & ~out.gene_set.str.contains("ALL")]
    mito_sig = mito[(mito.U_fdr < 0.05) & (mito.direction == "down")]
    print("\n=== Mitochondrial sub-programs significantly DOWN (FDR<0.05, competitive) ===")
    for _, r in mito_sig.sort_values("mean_z").iterrows():
        print(f"  {r.gene_set:48s} n={int(r.n):3d} mean_z={r.mean_z:+.3f} AUC={r.auc:.3f} FDR={r.U_fdr:.1e}")
    ctrl = out[out.gene_set.str.startswith("Control:")]
    ctrl_sig = ctrl[(ctrl.U_fdr < 0.05) & (ctrl.direction == "down")]
    print(f"\nSpecificity: {len(ctrl_sig)}/{len(ctrl)} non-mito control sets also down at FDR<0.05 "
          f"({', '.join(ctrl_sig.gene_set.str.replace('Control: ','')) if len(ctrl_sig) else 'none'})")


if __name__ == "__main__":
    main()
