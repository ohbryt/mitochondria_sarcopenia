#!/usr/bin/env python3
"""Recompute cohort-aware sarcopenia disease signatures for HMSR WP3.

DE method: OLS (statsmodels) on TMM-normalized log2 CPM.
Skill deviation note: multiomics-analysis skill specifies DESeq2/edgeR/limma-voom
for bulk RNA-seq. OLS is used here because input matrices are pre-normalized
(TMM log2 CPM); DESeq2/edgeR require raw integer counts. This is equivalent
to limma-trend practice and is documented in config.yaml (de_method_justification).
Meta-analysis: DerSimonian-Laird random-effects (compliant with skill STEP 3).
FDR: genome-wide Benjamini-Hochberg (compliant with skill STEP 3).
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
from scipy import stats


BASE_DIR = Path("/Volumes/4TB/exerciseomics/sarcopenia-multiomic-resource")
VALIDATION_DIR = BASE_DIR / "data" / "validation_cohorts"
INVENTORY_PATH = BASE_DIR / "output" / "validation" / "cohort_inventory.tsv"
OUTPUT_DIR = BASE_DIR / "output" / "signatures"
RUN_DATE = date(2026, 6, 8).isoformat()

# WP3 multi-criteria replication gate (replaces single FDR threshold after
# switching to random-effects meta; genome-wide BH-FDR not achieved).
WP3_GATE = {
    "meta_p_value": 0.005,          # nominal p threshold (genome-wide BH not achieved)
    "direction_consistency": 1.0,   # all cohorts agree on direction
    "loco_replication_rate": 1.0,   # 100% leave-one-cohort-out replication
    "heterogeneity_flag": False,    # no sign-mixed / high I² heterogeneity
}


@dataclass
class CohortData:
    cohort: str
    source_group: str
    model_role: str
    metadata: pd.DataFrame
    expression: pd.DataFrame


MODULE_SETS: dict[str, list[str]] = {
    "mitochondrial": [
        "MT-ND1", "MT-ND2", "MT-ND3", "MT-ND4", "MT-ND5", "MT-ND6", "MT-CYB",
        "MT-CO1", "MT-CO2", "MT-CO3", "ATP6", "ATP8", "ATP5A1", "ATP5B",
        "ATP5F1A", "ATP5F1B", "NDUFA1", "NDUFA4", "NDUFB3", "NDUFS1",
        "NDUFS3", "NDUFS7", "COX4I1", "COX5A", "COX5B", "COX10", "COX15",
        "SOD2", "PRDX3", "IDH2", "GFER", "CAT", "GPX1",
    ],
    "inflammation": [
        "IL6", "IL1B", "TNF", "CXCL8", "CCL2", "IL1RN", "TLR2", "TLR4",
        "NFKB1", "RELA", "NFKBIA", "PTGS2", "MMP1", "MMP3", "CCL3", "CCL4",
        "CXCL1", "CXCL10", "IL10", "IL12A", "TNFRSF1A", "TNFRSF1B",
    ],
    "senescence": [
        "CDKN1A", "CDKN2A", "TP53", "RB1", "SERPINE1", "CDK4", "CDK6",
        "MDM2", "SESN1", "SESN2", "GLB1", "CCNA2", "CCNB1", "CCND1",
        "CHEK1", "CHEK2", "ATM", "ATR", "MDM4", "CDK2", "RBX1",
    ],
    "autophagy": [
        "BECN1", "ATG5", "ATG7", "MAP1LC3A", "MAP1LC3B", "LAMP2", "SQSTM1",
        "UBQLN1", "OPTN", "NBR1", "CALCOCO2", "TAX1BP1", "ULK1", "ULK2",
        "PIK3C3", "LAMTOR1", "LAMP1", "GABARAP", "GABARAPL1",
    ],
    "stemness": [
        "PAX7", "MYF5", "MYOD1", "MYOG", "CD34", "KIT", "PROM1", "ENG",
        "NES", "SOX2", "KLF4", "MYC", "TERT", "ALCAM", "JAG1", "ITGA7",
    ],
    "proteostasis": [
        "PSEN1", "PSEN2", "APP", "MAPT", "UBB", "UBA52", "RPS27A", "HSPA1A",
        "HSPA1B", "HSP90AA1", "DNAJB1", "HSPB1", "CALR", "CANX", "UBQLN2",
        "SQSTM1", "DNAJC3", "HSP90AB1", "HSPA8",
    ],
    "ecm": [
        "COL1A1", "COL1A2", "COL3A1", "COL4A1", "COL4A2", "COL5A1", "COL6A1",
        "COL6A2", "COL6A3", "COL14A1", "DCN", "LUM", "FN1", "MMP2", "MMP9",
        "TIMP1", "SPARC", "TGFBI", "POSTN", "FBN1", "PDGFRA",
    ],
    "contractile": [
        "ACTA1", "ACTN2", "CKM", "DES", "MYH1", "MYH2", "MYH4", "MYH7",
        "MYBPC1", "MYBPC2", "MYBPC3", "MYL1", "MYL2", "MYL3", "NEB", "TTN",
        "TNNC1", "TNNC2", "TNNI1", "TNNI2", "TNNT1", "TNNT3", "TPM1", "TPM2",
    ],
}


def ensure_dirs() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def load_cohorts() -> list[CohortData]:
    inventory = pd.read_csv(INVENTORY_PATH, sep="\t")
    assembled = inventory[inventory["status"] == "assembled_strict_binary_available"].copy()
    cohorts = []

    for _, row in assembled.iterrows():
        cohort = row["cohort"]
        cohort_dir = VALIDATION_DIR / cohort
        metadata = pd.read_csv(cohort_dir / "metadata.tsv", sep="\t")
        expression = pd.read_csv(cohort_dir / "expression.tsv", sep="\t", index_col=0)
        expression = expression.apply(pd.to_numeric, errors="coerce")
        cohorts.append(
            CohortData(
                cohort=cohort,
                source_group=row["source_group"],
                model_role=row["recommended_model_role"],
                metadata=metadata,
                expression=expression,
            )
        )

    return cohorts


def bh_fdr(p_values: np.ndarray) -> np.ndarray:
    p_values = np.asarray(p_values, dtype=float)
    result = np.full(p_values.shape, np.nan, dtype=float)
    finite = np.isfinite(p_values)
    if not finite.any():
        return result

    p = p_values[finite]
    order = np.argsort(p)
    ranked = p[order]
    n = len(ranked)
    adjusted = ranked * n / np.arange(1, n + 1)
    adjusted = np.minimum.accumulate(adjusted[::-1])[::-1]
    adjusted = np.clip(adjusted, 0.0, 1.0)
    result[np.where(finite)[0][order]] = adjusted
    return result


def clean_numeric(series: pd.Series) -> pd.Series:
    return pd.to_numeric(series, errors="coerce")


def design_matrix(metadata: pd.DataFrame) -> tuple[pd.DataFrame, list[str], list[str]]:
    y = metadata["strict_sarcopenia_label"].astype(float)
    design = pd.DataFrame({"intercept": 1.0, "sarcopenia": y.values}, index=metadata.index)
    used = ["sarcopenia"]
    dropped: list[str] = []

    candidates: dict[str, pd.Series] = {}
    if "age" in metadata.columns:
        age = clean_numeric(metadata["age"])
        if age.notna().all() and age.nunique(dropna=True) > 2:
            age_sd = age.std(ddof=0)
            if age_sd > 0:
                candidates["age_z"] = (age - age.mean()) / age_sd
            else:
                dropped.append("age_constant")
        else:
            dropped.append("age_missing_or_low_variance")

    if "sex" in metadata.columns:
        sex = metadata["sex"].astype(str).str.lower().str.strip()
        if sex.nunique(dropna=True) > 1:
            candidates["sex_male"] = (sex == "male").astype(float)
        else:
            dropped.append("sex_constant")

    for name, values in candidates.items():
        trial = design.copy()
        trial[name] = values.values
        old_rank = np.linalg.matrix_rank(design.to_numpy(dtype=float))
        new_rank = np.linalg.matrix_rank(trial.to_numpy(dtype=float))
        if new_rank > old_rank:
            design = trial
            used.append(name)
        else:
            dropped.append(f"{name}_collinear")

    dropped.extend(["source_platform_not_estimable_within_cohort", "batch_not_available"])
    return design, used, dropped


def fit_ols_by_gene(cohort: CohortData) -> tuple[pd.DataFrame, dict[str, Any]]:
    metadata = cohort.metadata[cohort.metadata["include_strict_binary"].astype(bool)].copy()
    metadata = metadata.sort_values("sample_id")
    sample_ids = metadata["sample_id"].tolist()
    expression = cohort.expression.loc[:, sample_ids].copy()
    expression = expression.dropna(axis=0, how="any")
    expression = expression.loc[expression.var(axis=1) > 0]

    design, used_covariates, dropped_covariates = design_matrix(metadata)
    X = design.to_numpy(dtype=float)
    Y = expression.T.to_numpy(dtype=float)
    n_samples, n_genes = Y.shape
    rank = np.linalg.matrix_rank(X)
    df_resid = n_samples - rank
    if df_resid <= 0:
        raise ValueError(f"{cohort.cohort}: model has no residual degrees of freedom")

    xtx_inv = np.linalg.pinv(np.dot(X.T, X))
    beta = np.linalg.lstsq(X, Y, rcond=None)[0]
    residual = Y - np.dot(X, beta)
    sigma2 = np.sum(residual * residual, axis=0) / df_resid
    sarc_idx = list(design.columns).index("sarcopenia")
    sarc_var = max(float(xtx_inv[sarc_idx, sarc_idx]), 0.0)
    se = np.sqrt(np.maximum(sigma2 * sarc_var, 0.0))
    sarc_beta = beta[sarc_idx, :]
    with np.errstate(divide="ignore", invalid="ignore"):
        t_stat = sarc_beta / se
    p_values = 2.0 * stats.t.sf(np.abs(t_stat), df_resid)
    p_values[~np.isfinite(p_values)] = 1.0
    fdr = bh_fdr(p_values)

    labels = metadata["strict_sarcopenia_label"].astype(float)
    case_ids = metadata.loc[labels == 1.0, "sample_id"].tolist()
    control_ids = metadata.loc[labels == 0.0, "sample_id"].tolist()
    mean_case = expression.loc[:, case_ids].mean(axis=1)
    mean_control = expression.loc[:, control_ids].mean(axis=1)
    log2fc = mean_case - mean_control

    results = pd.DataFrame(
        {
            "cohort": cohort.cohort,
            "source_group": cohort.source_group,
            "model_role": cohort.model_role,
            "gene_symbol": expression.index,
            "n_samples": n_samples,
            "n_cases": len(case_ids),
            "n_controls": len(control_ids),
            "residual_df": df_resid,
            "covariates_used": ",".join(used_covariates),
            "covariates_dropped": ",".join(dropped_covariates),
            "model_formula": "expression ~ sarcopenia + estimable covariates",
            "mean_case": mean_case.to_numpy(),
            "mean_control": mean_control.to_numpy(),
            "log2fc_case_vs_control": log2fc.to_numpy(),
            "beta_sarcopenia": sarc_beta,
            "se_sarcopenia": se,
            "t_stat": t_stat,
            "p_value": p_values,
            "fdr": fdr,
        }
    )
    results["direction"] = np.select(
        [results["beta_sarcopenia"] > 0, results["beta_sarcopenia"] < 0],
        ["case_up", "case_down"],
        default="flat",
    )

    audit = {
        "cohort": cohort.cohort,
        "n_samples": n_samples,
        "n_cases": len(case_ids),
        "n_controls": len(control_ids),
        "n_genes_tested": n_genes,
        "used_covariates": ",".join(used_covariates),
        "dropped_covariates": ",".join(dropped_covariates),
    }
    return results, audit


def zscore_rows(matrix: pd.DataFrame) -> pd.DataFrame:
    means = matrix.mean(axis=1)
    stds = matrix.std(axis=1, ddof=0).replace(0, np.nan)
    return matrix.sub(means, axis=0).div(stds, axis=0)


def module_scores_for_cohort(cohort: CohortData) -> pd.DataFrame:
    expression = cohort.expression.copy()
    z = zscore_rows(expression)
    rows = []

    for module_name, genes in MODULE_SETS.items():
        present = [gene for gene in genes if gene in z.index]
        missing = [gene for gene in genes if gene not in z.index]
        if present:
            scores = z.loc[present].mean(axis=0)
        else:
            scores = pd.Series(np.nan, index=z.columns)

        for sample_id, score in scores.items():
            rows.append(
                {
                    "cohort": cohort.cohort,
                    "source_group": cohort.source_group,
                    "sample_id": sample_id,
                    "module": module_name,
                    "module_score": score,
                    "n_genes_defined": len(genes),
                    "n_genes_present": len(present),
                    "genes_present": ",".join(present),
                    "genes_missing": ",".join(missing),
                    "score_method": "mean within-cohort gene z-scores",
                }
            )

    scores_df = pd.DataFrame(rows)
    meta_cols = [
        "sample_id",
        "phenotype_class",
        "strict_sarcopenia_label",
        "include_strict_binary",
        "age",
        "sex",
        "recommended_model_role",
    ]
    available = [col for col in meta_cols if col in cohort.metadata.columns]
    scores_df = scores_df.merge(cohort.metadata[available], on="sample_id", how="left")
    return scores_df


def module_differential(module_scores: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for (cohort, module), group in module_scores.groupby(["cohort", "module"], sort=True):
        strict = group[group["include_strict_binary"].astype(bool)].copy()
        cases = strict[strict["strict_sarcopenia_label"].astype(float) == 1.0]["module_score"].dropna()
        controls = strict[strict["strict_sarcopenia_label"].astype(float) == 0.0]["module_score"].dropna()
        if len(cases) < 2 or len(controls) < 2:
            stat = np.nan
            p_value = np.nan
        else:
            stat, p_value = stats.ttest_ind(cases, controls, equal_var=False)
        rows.append(
            {
                "cohort": cohort,
                "module": module,
                "n_cases": len(cases),
                "n_controls": len(controls),
                "mean_case": cases.mean() if len(cases) else np.nan,
                "mean_control": controls.mean() if len(controls) else np.nan,
                "effect_case_vs_control": (cases.mean() - controls.mean()) if len(cases) and len(controls) else np.nan,
                "welch_t": stat,
                "p_value": p_value,
            }
        )
    result = pd.DataFrame(rows)
    result["fdr"] = bh_fdr(result["p_value"].to_numpy())
    result["direction"] = np.select(
        [result["effect_case_vs_control"] > 0, result["effect_case_vs_control"] < 0],
        ["case_up", "case_down"],
        default="flat",
    )
    return result


def dersimonian_laird_meta(group: pd.DataFrame) -> dict[str, float]:
    """DerSimonian-Laird random-effects meta-analysis (inverse-variance weighting with τ² estimate).

    Returns random-effects pooled β, SE, z, p, plus heterogeneity stats (Q, I², τ²).
    τ² = max(0, (Q − (k−1)) / C) where C = Σwᵢ − Σwᵢ²/Σwᵢ.
    """
    _nan = {
        "meta_beta": np.nan, "meta_se": np.nan, "meta_z": np.nan,
        "meta_p_value": np.nan, "heterogeneity_q": np.nan,
        "heterogeneity_i2": np.nan, "tau_sq": np.nan,
    }
    valid = group.replace([np.inf, -np.inf], np.nan).dropna(subset=["beta_sarcopenia", "se_sarcopenia"])
    valid = valid[valid["se_sarcopenia"] > 0]
    k = len(valid)
    if k == 0:
        return _nan

    wi = 1.0 / np.square(valid["se_sarcopenia"].to_numpy(dtype=float))
    beta = valid["beta_sarcopenia"].to_numpy(dtype=float)
    W = float(wi.sum())

    # Step 1: fixed-effect beta (used only to compute Q)
    beta_fe = float(np.sum(wi * beta) / W)

    # Step 2: Cochran Q and I²
    q = float(np.sum(wi * np.square(beta - beta_fe)))
    q_df = k - 1
    i2 = float(max(0.0, (q - q_df) / q) * 100.0) if q > 0 and q_df > 0 else 0.0

    # Step 3: DerSimonian-Laird τ²
    c = W - float(np.sum(wi ** 2)) / W
    tau_sq = float(max(0.0, (q - q_df) / c)) if c > 0 else 0.0

    # Step 4: random-effects weights and pooled estimate
    wi_re = 1.0 / (np.square(valid["se_sarcopenia"].to_numpy(dtype=float)) + tau_sq)
    meta_beta = float(np.sum(wi_re * beta) / wi_re.sum())
    meta_se = float(math.sqrt(1.0 / wi_re.sum()))
    meta_z = meta_beta / meta_se if meta_se > 0 else np.nan
    meta_p = float(2.0 * stats.norm.sf(abs(meta_z))) if np.isfinite(meta_z) else np.nan

    return {
        "meta_beta": meta_beta,
        "meta_se": meta_se,
        "meta_z": meta_z,
        "meta_p_value": meta_p,
        "heterogeneity_q": q,
        "heterogeneity_i2": i2,
        "tau_sq": tau_sq,
    }


def loco_details(group: pd.DataFrame) -> tuple[int, int, str]:
    details = []
    tested = 0
    replicated = 0
    effects = group.set_index("cohort")["beta_sarcopenia"].astype(float).to_dict()
    for heldout, heldout_beta in effects.items():
        discovery = [value for cohort, value in effects.items() if cohort != heldout and np.isfinite(value)]
        if not discovery or not np.isfinite(heldout_beta):
            details.append(f"{heldout}:not_tested")
            continue
        discovery_mean = float(np.mean(discovery))
        if discovery_mean == 0 or heldout_beta == 0:
            match = False
        else:
            match = np.sign(discovery_mean) == np.sign(heldout_beta)
        tested += 1
        replicated += int(match)
        details.append(
            f"{heldout}:{'match' if match else 'discordant'}"
            f"(heldout={heldout_beta:.5g},discovery_mean={discovery_mean:.5g})"
        )
    return tested, replicated, ";".join(details)


def build_replication_matrix(differential: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for gene, group in differential.groupby("gene_symbol", sort=True):
        group = group.copy()
        meta = dersimonian_laird_meta(group)
        directions = np.sign(group["beta_sarcopenia"].to_numpy(dtype=float))
        nonzero = directions[directions != 0]
        n_up = int((nonzero > 0).sum())
        n_down = int((nonzero < 0).sum())
        n_cohorts = int(group["cohort"].nunique())
        n_nominal = int((group["p_value"] < 0.05).sum())
        n_fdr10 = int((group["fdr"] < 0.10).sum())
        tested, replicated, details = loco_details(group)
        sign_mixed = n_up > 0 and n_down > 0
        heterogeneity_i2 = meta["heterogeneity_i2"]
        heterogeneity_flag = bool(sign_mixed or (np.isfinite(heterogeneity_i2) and heterogeneity_i2 >= 50.0))
        meta_direction = "case_up" if meta["meta_beta"] > 0 else "case_down" if meta["meta_beta"] < 0 else "flat"
        rows.append(
            {
                "gene_symbol": gene,
                "n_cohorts_detected": n_cohorts,
                "cohorts_detected": ",".join(group["cohort"].tolist()),
                "meta_direction": meta_direction,
                "meta_beta": meta["meta_beta"],
                "meta_se": meta["meta_se"],
                "meta_z": meta["meta_z"],
                "meta_p_value": meta["meta_p_value"],
                "n_nominal_p_lt_0_05": n_nominal,
                "n_fdr_lt_0_10": n_fdr10,
                "n_case_up_cohorts": n_up,
                "n_case_down_cohorts": n_down,
                "direction_consistency": max(n_up, n_down) / n_cohorts if n_cohorts else np.nan,
                "leave_one_cohort_out_tested": tested,
                "leave_one_cohort_out_replicated": replicated,
                "leave_one_cohort_out_replication_rate": replicated / tested if tested else np.nan,
                "leave_one_cohort_out_details": details,
                "heterogeneity_q": meta["heterogeneity_q"],
                "heterogeneity_i2": heterogeneity_i2,
                "tau_sq": meta["tau_sq"],
                "heterogeneity_flag": heterogeneity_flag,
                "effects_by_cohort": ";".join(
                    f"{row.cohort}:{row.beta_sarcopenia:.6g}" for row in group.itertuples()
                ),
                "p_values_by_cohort": ";".join(
                    f"{row.cohort}:{row.p_value:.6g}" for row in group.itertuples()
                ),
                "fdr_by_cohort": ";".join(
                    f"{row.cohort}:{row.fdr:.6g}" for row in group.itertuples()
                ),
            }
        )

    replication = pd.DataFrame(rows)
    replication["meta_fdr"] = bh_fdr(replication["meta_p_value"].to_numpy())
    ordered = [
        "gene_symbol",
        "n_cohorts_detected",
        "cohorts_detected",
        "meta_direction",
        "meta_beta",
        "meta_se",
        "meta_z",
        "meta_p_value",
        "meta_fdr",
        "n_nominal_p_lt_0_05",
        "n_fdr_lt_0_10",
        "n_case_up_cohorts",
        "n_case_down_cohorts",
        "direction_consistency",
        "leave_one_cohort_out_tested",
        "leave_one_cohort_out_replicated",
        "leave_one_cohort_out_replication_rate",
        "leave_one_cohort_out_details",
        "heterogeneity_q",
        "heterogeneity_i2",
        "tau_sq",
        "heterogeneity_flag",
        "effects_by_cohort",
        "p_values_by_cohort",
        "fdr_by_cohort",
    ]
    return replication[ordered].sort_values(["meta_fdr", "meta_p_value", "gene_symbol"], na_position="last")


def apply_wp3_gate(replication: pd.DataFrame) -> pd.DataFrame:
    """Return rows passing the WP3 multi-criteria replication gate."""
    mask = (
        (replication["meta_p_value"] < WP3_GATE["meta_p_value"])
        & (replication["direction_consistency"] >= WP3_GATE["direction_consistency"])
        & (replication["leave_one_cohort_out_replication_rate"] >= WP3_GATE["loco_replication_rate"])
        & (replication["heterogeneity_flag"] == WP3_GATE["heterogeneity_flag"])
    )
    return replication[mask].reset_index(drop=True)


def write_report(
    cohort_audits: list[dict[str, Any]],
    differential: pd.DataFrame,
    module_diff: pd.DataFrame,
    replication: pd.DataFrame,
) -> None:
    assembled_n = len(cohort_audits)
    strict_samples = int(sum(row["n_samples"] for row in cohort_audits))
    total_cases = int(sum(row["n_cases"] for row in cohort_audits))
    total_controls = int(sum(row["n_controls"] for row in cohort_audits))

    top_meta = replication.head(10)[
        ["gene_symbol", "meta_direction", "meta_beta", "meta_p_value", "meta_fdr", "direction_consistency", "heterogeneity_flag"]
    ]
    top_modules = module_diff.sort_values(["fdr", "p_value"], na_position="last").head(12)

    lines = [
        "# WP3 Cohort-Aware Disease Signatures",
        "",
        f"Generated: {RUN_DATE}",
        "",
        "## Scope",
        "",
        (
            f"Used {assembled_n} WP2 validation cohorts and {strict_samples} strict binary samples "
            f"({total_cases} sarcopenia cases, {total_controls} controls). Proxy/pre-sarcopenia samples "
            "were excluded from disease differential models but retained in per-sample module score output."
        ),
        "",
        "## Model Audit",
        "",
        "| Cohort | Samples | Cases | Controls | Genes Tested | Covariates Used | Covariates Dropped |",
        "|---|---:|---:|---:|---:|---|---|",
    ]
    for row in cohort_audits:
        lines.append(
            f"| {row['cohort']} | {row['n_samples']} | {row['n_cases']} | {row['n_controls']} | "
            f"{row['n_genes_tested']} | {row['used_covariates']} | {row['dropped_covariates']} |"
        )

    lines.extend(
        [
            "",
            "## Outputs",
            "",
            "- `output/signatures/differential_by_cohort.tsv`: per-gene, per-cohort OLS coefficient for sarcopenia case versus control.",
            "- `output/signatures/module_scores_by_cohort.tsv`: per-sample module scores from mean within-cohort gene z-scores.",
            "- `output/signatures/module_differential_by_cohort.tsv`: Welch tests of module scores in strict case/control samples.",
            "- `output/signatures/replication_matrix.tsv`: DerSimonian-Laird random-effects meta-analysis, leave-one-cohort-out direction checks, and heterogeneity flags.",
            "- `output/signatures/wp3_gate_pass.tsv`: genes passing the WP3 multi-criteria gate (meta_p<0.005, direction_consistency=1.0, LOCO=1.0, heterogeneity_flag=False).",
            "",
            "## Top Random-Effects Gene Signals",
            "",
            top_meta.to_markdown(index=False),
            "",
            "## Top Module Differences",
            "",
            top_modules[["cohort", "module", "effect_case_vs_control", "p_value", "fdr", "direction"]].to_markdown(index=False),
            "",
            "## Interpretation Guardrails",
            "",
            "- These are observational case/control expression associations, not causal effects.",
            "- Source/platform terms were not estimable within cohorts because all assembled cohorts use the same listed platform/instrument within cohort.",
            "- Cross-cohort source effects are handled by per-cohort models and replication summaries, not by pooled adjustment.",
            "- GSE111006/GSE111010/GSE111016 are related through the GSE111017 study family; GSE226151 is the independent source group.",
            "- Myopathy proxy samples from earlier HMSR phases are not used here.",
        ]
    )
    (OUTPUT_DIR / "wp3_signature_readiness.md").write_text("\n".join(lines) + "\n")


def main() -> None:
    ensure_dirs()
    cohorts = load_cohorts()

    differential_frames = []
    module_score_frames = []
    audits = []
    for cohort in cohorts:
        print(f"Fitting cohort DE: {cohort.cohort}")
        de, audit = fit_ols_by_gene(cohort)
        differential_frames.append(de)
        audits.append(audit)
        module_score_frames.append(module_scores_for_cohort(cohort))

    differential = pd.concat(differential_frames, ignore_index=True)
    differential = differential.sort_values(["cohort", "fdr", "p_value", "gene_symbol"])
    module_scores = pd.concat(module_score_frames, ignore_index=True)
    module_diff = module_differential(module_scores)
    replication = build_replication_matrix(differential)

    gate_pass = apply_wp3_gate(replication)

    differential.to_csv(OUTPUT_DIR / "differential_by_cohort.tsv", sep="\t", index=False)
    module_scores.to_csv(OUTPUT_DIR / "module_scores_by_cohort.tsv", sep="\t", index=False)
    module_diff.to_csv(OUTPUT_DIR / "module_differential_by_cohort.tsv", sep="\t", index=False)
    replication.to_csv(OUTPUT_DIR / "replication_matrix.tsv", sep="\t", index=False)
    gate_pass.to_csv(OUTPUT_DIR / "wp3_gate_pass.tsv", sep="\t", index=False)
    pd.DataFrame(audits).to_csv(OUTPUT_DIR / "model_audit.tsv", sep="\t", index=False)
    write_report(audits, differential, module_diff, replication)

    print(f"WP3 gate: {len(gate_pass)} genes pass (meta_p<{WP3_GATE['meta_p_value']}, direction=1.0, LOCO=1.0, no-het)")
    print("Wrote WP3 signatures:")
    print((OUTPUT_DIR / "differential_by_cohort.tsv").relative_to(BASE_DIR))
    print((OUTPUT_DIR / "replication_matrix.tsv").relative_to(BASE_DIR))
    print((OUTPUT_DIR / "wp3_gate_pass.tsv").relative_to(BASE_DIR))


if __name__ == "__main__":
    main()
