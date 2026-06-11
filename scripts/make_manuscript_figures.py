#!/usr/bin/env python3
"""
Generate all manuscript figures and tables for HMSR paper.

Outputs (output/manuscript_tables/, output/figures/):
  Table1_cohort_characteristics.tsv / .md
  Table2_top20_gate_pass.tsv / .md
  Table3_oxphos_genes.tsv / .md
  TableS1_all195_gate_pass.tsv
  Fig1_study_overview.pdf / .png
  Fig2_forest_plots.pdf / .png
  Fig3_volcano_meta.pdf / .png
  Fig4_heatmap_top50.pdf / .png
"""
from __future__ import annotations

import textwrap
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.gridspec as gridspec
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

BASE = Path("/Volumes/4TB/exerciseomics/sarcopenia-multiomic-resource")
SIG = BASE / "output" / "signatures"
TABLES = BASE / "output" / "manuscript_tables"
FIGS = BASE / "output" / "figures"
TABLES.mkdir(parents=True, exist_ok=True)
FIGS.mkdir(parents=True, exist_ok=True)

# Highlighted candidate genes. NOTE: label is "mitochondrial", NOT "OXPHOS".
# Only NDUFB4 (Complex I) and ATP5F1B (Complex V) are true OXPHOS subunits.
# CHCHD10/APOO = MICOS/cristae; MRPL33/MRPL34 = mitoribosome; CLTB = NOT mitochondrial.
MITO_GENES = ["CHCHD10", "MRPL34", "APOO", "MRPL33", "NDUFB4", "ATP5F1B"]
NON_MITO_OUTLIER = ["CLTB"]  # clathrin light chain B — shown separately
OXPHOS_GENES = MITO_GENES + NON_MITO_OUTLIER  # full highlight set (back-compat)
GENE_FUNCTION = {
    "NDUFB4": "Complex I (OXPHOS)",
    "ATP5F1B": "Complex V (OXPHOS)",
    "CHCHD10": "MICOS/cristae",
    "APOO": "MICOS/cristae",
    "MRPL33": "Mitoribosome",
    "MRPL34": "Mitoribosome",
    "CLTB": "Clathrin (NON-mito)",
}

COHORT_LABELS = {
    "GSE111006_HSS": "HSS\n(GSE111006)",
    "GSE111010_JSS": "JSS\n(GSE111010)",
    "GSE111016_SSS": "SSS\n(GSE111016)",
    "GSE226151":     "GESTALT\n(GSE226151)",
}
COHORT_COLORS = {
    "GSE111006_HSS": "#4C72B0",
    "GSE111010_JSS": "#DD8452",
    "GSE111016_SSS": "#55A868",
    "GSE226151":     "#C44E52",
}

# ── Load data ─────────────────────────────────────────────────────────────
gp   = pd.read_csv(SIG / "wp3_gate_pass.tsv", sep="\t")
rep  = pd.read_csv(SIG / "replication_matrix.tsv", sep="\t")
diff = pd.read_csv(SIG / "differential_by_cohort.tsv", sep="\t")
mod  = pd.read_csv(SIG / "model_audit.tsv", sep="\t")


# ── Table 1 — Cohort characteristics ────────────────────────────────────
def make_table1() -> pd.DataFrame:
    cohort_meta = {
        "GSE111006_HSS": dict(country="South Korea", sex="Male", design="Case/control"),
        "GSE111010_JSS": dict(country="Jamaica",     sex="Male", design="Case/control"),
        "GSE111016_SSS": dict(country="South Korea", sex="Female", design="Case/control"),
        "GSE226151":     dict(country="USA (GESTALT)", sex="Both", design="Case/control"),
    }
    rows = []
    for _, r in mod.iterrows():
        m = cohort_meta.get(r.cohort, {})
        rows.append({
            "Cohort ID": r.cohort.replace("_", " "),
            "GEO Accession": r.cohort.split("_")[0],
            "Country": m.get("country", "—"),
            "Sex": m.get("sex", "—"),
            "Study design": m.get("design", "—"),
            "Total samples": r.n_samples,
            "Cases": r.n_cases,
            "Controls": r.n_controls,
            "Genes tested": f"{r.n_genes_tested:,}",
            "Covariates": r.used_covariates.replace(",", ", "),
        })
    t = pd.DataFrame(rows)
    t.to_csv(TABLES / "Table1_cohort_characteristics.tsv", sep="\t", index=False)
    t.to_markdown(TABLES / "Table1_cohort_characteristics.md", index=False)
    print(f"Table 1: {len(t)} cohorts → {TABLES/'Table1_cohort_characteristics.tsv'}")
    return t


# ── Table 2 — Top 20 gate-pass genes ────────────────────────────────────
def make_table2() -> pd.DataFrame:
    cols = ["gene_symbol", "meta_direction", "meta_beta", "meta_se",
            "meta_p_value", "meta_fdr", "heterogeneity_i2",
            "direction_consistency", "leave_one_cohort_out_replication_rate"]
    t = gp.head(20)[cols].copy()
    t.columns = ["Gene", "Direction", "β (RE meta)", "SE", "p (meta)",
                 "FDR (BH)", "I² (%)", "Direction consistency", "LOCO rate"]
    t["β (RE meta)"] = t["β (RE meta)"].map("{:.3f}".format)
    t["SE"] = t["SE"].map("{:.3f}".format)
    t["p (meta)"] = t["p (meta)"].map("{:.2e}".format)
    t["FDR (BH)"] = t["FDR (BH)"].map("{:.3f}".format)
    t["I² (%)"] = t["I² (%)"].map("{:.1f}".format)
    t.to_csv(TABLES / "Table2_top20_gate_pass.tsv", sep="\t", index=False)
    t.to_markdown(TABLES / "Table2_top20_gate_pass.md", index=False)
    print(f"Table 2: top 20 gate-pass → {TABLES/'Table2_top20_gate_pass.tsv'}")
    return t


# ── Table 3 — highlighted mitochondrial candidates (corrected functional class) ──
def make_table3() -> pd.DataFrame:
    ox = gp[gp.gene_symbol.isin(OXPHOS_GENES)].sort_values("meta_p_value").copy()
    # True OXPHOS subunit flag and function
    ox["Function"] = ox.gene_symbol.map(GENE_FUNCTION)
    ox["OXPHOS subunit"] = ox.gene_symbol.map(
        lambda g: "Yes" if g in ("NDUFB4", "ATP5F1B") else "No"
    )
    ox["Mitochondrial"] = ox.gene_symbol.map(
        lambda g: "No (clathrin)" if g in NON_MITO_OUTLIER else "Yes"
    )
    # Per-cohort betas
    for cohort in ["GSE111006_HSS", "GSE111010_JSS", "GSE111016_SSS", "GSE226151"]:
        sub = diff[diff.cohort == cohort].set_index("gene_symbol")
        short = cohort.split("_")[0]
        ox[f"β {short}"] = ox.gene_symbol.map(
            lambda g: f"{sub.loc[g,'beta_sarcopenia']:.3f}" if g in sub.index else "—"
        )
    cols = (["gene_symbol", "Function", "OXPHOS subunit", "Mitochondrial",
             "meta_beta", "meta_se", "meta_p_value", "meta_fdr", "heterogeneity_i2"] +
            [f"β {c.split('_')[0]}" for c in ["GSE111006_HSS", "GSE111010_JSS",
                                               "GSE111016_SSS", "GSE226151"]])
    t = ox[cols].copy()
    t.columns = (["Gene", "Function", "OXPHOS subunit", "Mitochondrial",
                  "β (RE meta)", "SE", "p (meta)", "FDR (BH)", "I² (%)"] +
                 ["β HSS", "β JSS", "β SSS", "β GESTALT"])
    for col in ["β (RE meta)", "SE"]:
        t[col] = t[col].map("{:.4f}".format)
    t["p (meta)"] = t["p (meta)"].map("{:.2e}".format)
    t["FDR (BH)"] = t["FDR (BH)"].map("{:.3f}".format)
    t["I² (%)"] = t["I² (%)"].map("{:.1f}".format)
    t.to_csv(TABLES / "Table3_mito_candidates.tsv", sep="\t", index=False)
    t.to_markdown(TABLES / "Table3_mito_candidates.md", index=False)
    print(f"Table 3: highlighted mito candidates → {TABLES/'Table3_mito_candidates.tsv'}")
    return t


# ── Table S1 — All 195 gate-pass genes ──────────────────────────────────
def make_tableS1() -> None:
    gp.to_csv(TABLES / "TableS1_all195_gate_pass.tsv", sep="\t", index=False)
    print(f"Table S1: {len(gp)} genes → {TABLES/'TableS1_all195_gate_pass.tsv'}")


# ── Figure 1 — Study overview ────────────────────────────────────────────
def fig1_study_overview() -> None:
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")

    def box(x, y, w, h, text, color="#E8F4F8", fontsize=9, bold=False):
        rect = mpatches.FancyBboxPatch((x - w/2, y - h/2), w, h,
                                       boxstyle="round,pad=0.1",
                                       facecolor=color, edgecolor="#555", linewidth=1.2)
        ax.add_patch(rect)
        weight = "bold" if bold else "normal"
        ax.text(x, y, text, ha="center", va="center", fontsize=fontsize,
                fontweight=weight, wrap=True,
                multialignment="center")

    def arrow(x1, y1, x2, y2):
        ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle="->", color="#444", lw=1.5))

    # Title
    ax.text(5, 9.5, "HMSR: Multi-Cohort Sarcopenia Transcriptomic Resource",
            ha="center", va="center", fontsize=12, fontweight="bold")

    # WP2 cohorts
    cohort_info = [
        ("HSS\n(GSE111006)\nn=32", 1.5, 7.5, COHORT_COLORS["GSE111006_HSS"]),
        ("JSS\n(GSE111010)\nn=23", 3.5, 7.5, COHORT_COLORS["GSE111010_JSS"]),
        ("SSS\n(GSE111016)\nn=40", 5.5, 7.5, COHORT_COLORS["GSE111016_SSS"]),
        ("GESTALT\n(GSE226151)\nn=40", 7.5, 7.5, COHORT_COLORS["GSE226151"]),
    ]
    for label, x, y, color in cohort_info:
        box(x, y, 1.7, 1.2, label, color=color + "55", fontsize=8)

    box(4.5, 8.8, 8.0, 0.5, "WP2: 4 Cohorts  |  135 samples  |  53 sarcopenia cases  |  82 controls",
        color="#FFF9E6", fontsize=9, bold=False)

    for x in [1.5, 3.5, 5.5, 7.5]:
        arrow(x, 6.9, 4.5, 6.2)

    # WP3
    box(4.5, 5.7, 5.5, 0.8,
        "WP3: OLS DE per cohort  +  DerSimonian-Laird random-effects meta\n"
        "37,469 genes · BH-FDR genome-wide",
        color="#EEF4EE", fontsize=8.5, bold=False)

    arrow(4.5, 5.3, 4.5, 4.6)

    box(4.5, 4.2, 5.5, 0.8,
        "WP3 Gate: meta-p < 0.005 · direction = 1.0 · LOCO = 1.0 · I² < 50%\n"
        "→ 195 replicated genes  (141↓  54↑)",
        color="#FFF0F0", fontsize=8.5, bold=False)

    arrow(4.5, 3.8, 4.5, 3.1)

    box(4.5, 2.7, 5.5, 0.8,
        "Candidate set enriched for mitochondrial genes (26/195, ~9.5x)\n"
        "Highlighted: 6 mitochondrial (2 OXPHOS) + CLTB (non-mito outlier)",
        color="#FFF0F0", fontsize=8.5, bold=True)

    arrow(4.5, 2.3, 4.5, 1.6)

    box(4.5, 1.2, 5.5, 0.8,
        "WP5: Exercise epigenetic evidence ladder\n"
        "37 exercise epigenetic rows  |  90 human multilayer rows",
        color="#F0F0FF", fontsize=8.5)

    plt.tight_layout()
    for ext in ("pdf", "png"):
        p = FIGS / f"Fig1_study_overview.{ext}"
        fig.savefig(p, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"Fig 1 → {FIGS/'Fig1_study_overview.png'}")


# ── Figure 2 — Forest plots for 7 OXPHOS genes ──────────────────────────
def fig2_forest_plots() -> None:
    cohorts = ["GSE111006_HSS", "GSE111010_JSS", "GSE111016_SSS", "GSE226151"]
    short   = ["HSS", "JSS", "SSS", "GESTALT"]

    fig = plt.figure(figsize=(14, 12))
    gs = gridspec.GridSpec(4, 2, hspace=0.55, wspace=0.35)

    # Load per-cohort n for weight marker sizing
    diff_indexed = diff.set_index(["cohort", "gene_symbol"])
    re = rep.set_index("gene_symbol")

    axes = [fig.add_subplot(gs[r, c]) for r in range(4) for c in range(2)]
    # trim to 7
    axes = axes[:7]

    for ax_i, gene in enumerate(OXPHOS_GENES):
        ax = axes[ax_i]
        y_labels = short + ["RE meta"]
        y_pos = list(range(len(y_labels)))

        betas = []
        ses = []
        for cohort in cohorts:
            try:
                row = diff_indexed.loc[(cohort, gene)]
                betas.append(float(row["beta_sarcopenia"]))
                ses.append(float(row["se_sarcopenia"]))
            except KeyError:
                betas.append(np.nan)
                ses.append(np.nan)

        meta_b = float(re.loc[gene, "meta_beta"])
        meta_s = float(re.loc[gene, "meta_se"])
        meta_p = float(re.loc[gene, "meta_p_value"])
        i2 = float(re.loc[gene, "heterogeneity_i2"])

        betas.append(meta_b)
        ses.append(meta_s)

        colors = [COHORT_COLORS[c] for c in cohorts] + ["#333333"]
        sizes  = [40] * 4 + [120]

        for i, (b, s, col, sz) in enumerate(zip(betas, ses, colors, sizes)):
            if np.isnan(b):
                continue
            ci_lo = b - 1.96 * s
            ci_hi = b + 1.96 * s
            ax.plot([ci_lo, ci_hi], [i, i], color=col, lw=1.5, zorder=2)
            ax.scatter([b], [i], color=col, s=sz, zorder=3,
                       marker="D" if i == len(cohorts) else "o")

        ax.axvline(0, color="#999", lw=0.8, ls="--")
        ax.set_yticks(y_pos)
        ax.set_yticklabels(y_labels, fontsize=7.5)
        ax.set_xlabel("β (sarcopenia vs control)", fontsize=7)
        func = GENE_FUNCTION.get(gene, "")
        title_color = "#C44E52" if gene in NON_MITO_OUTLIER else "#222222"
        ax.set_title(f"{gene}  ({func})\np={meta_p:.2e}  I²={i2:.0f}%",
                     fontsize=8.5, fontweight="bold", color=title_color)
        ax.tick_params(axis="x", labelsize=7)
        ax.spines[["top", "right"]].set_visible(False)

        # Separator line before meta
        ax.axhline(len(cohorts) - 0.5, color="#ccc", lw=0.8, ls=":")

    fig.suptitle("Figure 2. Forest plots: highlighted mitochondrial candidates in sarcopenia\n"
                 "DL random-effects meta across 2 independent studies (4 sample sets); CLTB shown as non-mito outlier (red)",
                 fontsize=10, fontweight="bold", y=1.01)
    for ext in ("pdf", "png"):
        fig.savefig(FIGS / f"Fig2_forest_plots.{ext}", dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"Fig 2 → {FIGS/'Fig2_forest_plots.png'}")


# ── Figure 3 — Volcano plot (meta-analysis) ──────────────────────────────
def fig3_volcano() -> None:
    df = rep.copy()
    df = df.dropna(subset=["meta_p_value", "meta_beta"])
    df["neg_log10_p"] = -np.log10(df["meta_p_value"].clip(lower=1e-30))
    df["color"] = "#CCCCCC"
    gate = (
        (df["meta_p_value"] < 0.005) &
        (df["direction_consistency"] >= 1.0) &
        (df["leave_one_cohort_out_replication_rate"] >= 1.0) &
        (~df["heterogeneity_flag"])
    )
    df.loc[gate & (df["meta_beta"] < 0), "color"] = "#4C72B0"
    df.loc[gate & (df["meta_beta"] > 0), "color"] = "#C44E52"

    fig, ax = plt.subplots(figsize=(8, 6))
    # Background
    ax.scatter(df.loc[~gate, "meta_beta"], df.loc[~gate, "neg_log10_p"],
               c="#DDDDDD", s=5, alpha=0.4, lw=0, rasterized=True, label="Not replicated")
    # Gate-pass down
    m = gate & (df["meta_beta"] < 0)
    ax.scatter(df.loc[m, "meta_beta"], df.loc[m, "neg_log10_p"],
               c="#4C72B0", s=12, alpha=0.8, lw=0, label=f"Replicated ↓ (n={m.sum()})")
    # Gate-pass up
    m = gate & (df["meta_beta"] > 0)
    ax.scatter(df.loc[m, "meta_beta"], df.loc[m, "neg_log10_p"],
               c="#C44E52", s=12, alpha=0.8, lw=0, label=f"Replicated ↑ (n={m.sum()})")

    # Label 7 OXPHOS genes
    ox_df = df[df.gene_symbol.isin(OXPHOS_GENES)]
    for _, row in ox_df.iterrows():
        ax.annotate(row.gene_symbol,
                    xy=(row.meta_beta, row.neg_log10_p),
                    xytext=(row.meta_beta - 0.06, row.neg_log10_p + 0.12),
                    fontsize=7, color="#222",
                    arrowprops=dict(arrowstyle="-", color="#888", lw=0.6))

    ax.axhline(-np.log10(0.005), color="#888", lw=1, ls="--", label="p = 0.005")
    ax.axvline(0, color="#aaa", lw=0.8)
    ax.set_xlabel("Random-effects meta-β (sarcopenia vs control)", fontsize=10)
    ax.set_ylabel("−log₁₀(meta-p)", fontsize=10)
    ax.set_title("Figure 3. Meta-analysis volcano plot\n"
                 "37,469 genes across 4 sarcopenia cohorts", fontsize=10, fontweight="bold")
    ax.legend(fontsize=8, framealpha=0.7)
    ax.spines[["top", "right"]].set_visible(False)

    for ext in ("pdf", "png"):
        fig.savefig(FIGS / f"Fig3_volcano_meta.{ext}", dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"Fig 3 → {FIGS/'Fig3_volcano_meta.png'}")


# ── Figure 4 — Heatmap top 50 gate-pass genes ────────────────────────────
def fig4_heatmap() -> None:
    top50 = gp.head(50)["gene_symbol"].tolist()
    cohorts = ["GSE111006_HSS", "GSE111010_JSS", "GSE111016_SSS", "GSE226151"]

    # Build matrix: genes × cohorts (beta values)
    mat = []
    for gene in top50:
        row_vals = []
        for cohort in cohorts:
            sub = diff[(diff.cohort == cohort) & (diff.gene_symbol == gene)]
            if not sub.empty:
                row_vals.append(float(sub.iloc[0]["beta_sarcopenia"]))
            else:
                row_vals.append(np.nan)
        mat.append(row_vals)
    mat_arr = np.array(mat, dtype=float)

    fig, ax = plt.subplots(figsize=(5, 14))
    vmax = np.nanpercentile(np.abs(mat_arr), 95)
    im = ax.imshow(mat_arr, aspect="auto", cmap="RdBu_r",
                   vmin=-vmax, vmax=vmax, interpolation="nearest")

    ax.set_xticks(range(4))
    ax.set_xticklabels(["HSS", "JSS", "SSS", "GESTALT"], fontsize=9, fontweight="bold")
    ax.set_yticks(range(len(top50)))
    ax.set_yticklabels(top50, fontsize=7)
    ax.tick_params(top=True, labeltop=True, bottom=False, labelbottom=False)

    # Mark mitochondrial genes (red bold); CLTB non-mito outlier (orange italic)
    for i, gene in enumerate(top50):
        if gene in MITO_GENES:
            ax.get_yticklabels()[i].set_color("#C44E52")
            ax.get_yticklabels()[i].set_fontweight("bold")
        elif gene in NON_MITO_OUTLIER:
            ax.get_yticklabels()[i].set_color("#DD8452")
            ax.get_yticklabels()[i].set_fontstyle("italic")

    cbar = fig.colorbar(im, ax=ax, fraction=0.03, pad=0.02)
    cbar.set_label("β (sarcopenia vs control)", fontsize=8)
    ax.set_title("Figure 4. Top 50 candidate genes\n(mitochondrial: red bold; CLTB non-mito: orange italic)",
                 fontsize=9, fontweight="bold")

    for ext in ("pdf", "png"):
        fig.savefig(FIGS / f"Fig4_heatmap_top50.{ext}", dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"Fig 4 → {FIGS/'Fig4_heatmap_top50.png'}")


# ── Figure 5 — mitochondrial pathway enrichment (permutation) ────────────
def fig5_pathway_enrichment() -> None:
    perm_path = SIG / "wp3c_permutation.tsv"
    if not perm_path.exists():
        print("Fig 5 skipped (run pathway_permutation.py first)")
        return
    pm = pd.read_csv(perm_path, sep="\t")
    label = {
        "Mito_ALL": "Mitochondrial programme (all)",
        "Mito_ComplexI_NDUF": "  Complex I (NDUF)",
        "Mito_ComplexII_III_IV": "  Complex II/III/IV",
        "Mito_ComplexV_ATP5": "  Complex V (ATP5)",
        "Mito_mitoribosome": "  Mitoribosome (MRPL/MRPS)",
        "Mito_cristae_MICOS": "  Cristae / MICOS",
        "Mito_import_TIMM_TOMM": "  Import (TIMM/TOMM)",
        "Control_proteasome": "Control: proteasome",
        "Control_cyto_ribosome": "Control: cytoplasmic ribosome",
        "Control_collagen": "Control: collagen / ECM",
    }
    pm = pm[pm.gene_set.isin(label)].copy()
    pm["lab"] = pm.gene_set.map(label)
    pm["is_mito"] = pm.gene_set.str.startswith("Mito")
    pm = pm.sort_values("observed_diff")

    fig, ax = plt.subplots(figsize=(9, 6))
    ypos = np.arange(len(pm))
    colors = ["#C44E52" if m else "#888888" for m in pm.is_mito]
    ax.barh(ypos, pm.observed_diff, color=colors, edgecolor="#333", linewidth=0.6)
    # error bars from null SD (permutation spread)
    ax.errorbar(pm.observed_diff, ypos, xerr=pm.null_sd, fmt="none",
                ecolor="#444", elinewidth=0.8, capsize=2)
    ax.axvline(0, color="#000", lw=0.8)
    ax.set_yticks(ypos)
    ax.set_yticklabels(pm.lab, fontsize=8)
    ax.set_xlabel("Competitive shift in meta-z (in-set − out-set)", fontsize=9)
    ax.set_title("Figure 5. Coordinated down-regulation of the mitochondrial gene programme\n"
                 "Label-permutation competitive test (N=2000, correlation-aware); "
                 "error bars = permutation-null SD", fontsize=9, fontweight="bold")
    # annotate permutation p
    for y, (_, r) in zip(ypos, pm.iterrows()):
        ptxt = f"p={r.perm_p_one_sided_down:.1e}" if r.is_mito else f"p={r.perm_p_one_sided_down:.2f} (ns)"
        ax.text(r.observed_diff - np.sign(r.observed_diff) * 0.04 - 0.02, y, ptxt,
                va="center", ha="right" if r.observed_diff < 0 else "left", fontsize=6.5, color="#222")
    ax.spines[["top", "right"]].set_visible(False)
    ax.text(0.02, 0.02,
            "Mitochondrial sub-programmes (red) all shift down (p≤6e-3);\n"
            "cytoplasmic ribosome & proteasome controls not significant; collagen shifts up.",
            transform=ax.transAxes, fontsize=7, color="#555", va="bottom")
    for ext in ("pdf", "png"):
        fig.savefig(FIGS / f"Fig5_pathway_enrichment.{ext}", dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"Fig 5 → {FIGS/'Fig5_pathway_enrichment.png'}")


# ── Main ──────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("Generating manuscript tables...")
    make_table1()
    make_table2()
    make_table3()
    make_tableS1()

    print("\nGenerating manuscript figures...")
    fig1_study_overview()
    fig2_forest_plots()
    fig3_volcano()
    fig4_heatmap()
    fig5_pathway_enrichment()

    print("\nDone. All outputs in:")
    print(f"  Tables: {TABLES}")
    print(f"  Figures: {FIGS}")
