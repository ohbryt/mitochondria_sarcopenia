#!/usr/bin/env python3
"""
WP5: split rat exercise epigenetic evidence from human multi-layer evidence.

The legacy Phase 4 ladder merged rat regulatory perturbation evidence with
human transcriptomic and biomarker evidence. This script keeps those evidence
classes separate and records mapping provenance before any exercise-regulated
gene claim is allowed.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


BASE_DIR = Path("/Volumes/4TB/exerciseomics/sarcopenia-multiomic-resource")
PHASE4_DIR = BASE_DIR / "output" / "phase4"
FIGURE_DIR = BASE_DIR / "output" / "figures"

SOURCE_DATASET = "MoTrPAC rat exercise training"
RAT_SPECIES = "Rattus norvegicus"
RAT_TISSUE = "skeletal_muscle_gastrocnemius"

HALLMARK_GENES = {
    "CDKN1A",
    "CDKN2A",
    "TP53",
    "RB1",
    "SERPINE1",
    "IL6",
    "IL1B",
    "TNF",
    "CXCL8",
    "CCL2",
    "NFKB1",
    "PTGS2",
    "MT-ND1",
    "MT-CO1",
    "ATP5A1",
    "SOD2",
    "COX4I1",
    "BECN1",
    "SQSTM1",
    "LAMP2",
    "ATG5",
    "ATG7",
    "PAX7",
    "MYOD1",
    "MYOG",
    "CD34",
    "KIT",
    "PSEN1",
    "APP",
    "UBB",
    "HSP90AA1",
    "HSPA1A",
}

ANCHOR_GENES = {"EDA2R", "HJV", "HAMP", "BMP6", "BMP2", "TFRC", "SLC40A1"}

# Curated local symbol mapping for genes present in the legacy rat exercise
# outputs. Unmapped entries are left explicit in the output table.
RAT_TO_HUMAN_ORTHOLOG = {
    "Arrdc2": "ARRDC2",
    "Cck": "CCK",
    "Egr1": "EGR1",
    "Egr2": "EGR2",
    "Fos": "FOS",
    "Fosb": "FOSB",
    "Fsip1": "FSIP1",
    "Gap43": "GAP43",
    "Hsp70": "HSPA1A",
    "Junb": "JUNB",
    "Jund": "JUND",
    "Mt1": "MT1",
    "Mt2": "MT2",
    "Nptx2": "NPTX2",
    "Nr4a3": "NR4A3",
    "Ripor1": "RIPOR1",
    "Scg2": "SCG2",
    "Vip": "VIP",
}

# This list is copied from recovery_gates.py, where it was used to recover
# gene labels for significant ATAC peaks. The coordinate-resolved peak-to-gene
# mapping file is not present in the local Phase 4 outputs, so these labels are
# retained as recovered provenance rather than treated as primary mapping.
RECOVERED_ATAC_GENE_LABELS = {
    "Nr4a3",
    "Fosb",
    "Fos",
    "Junb",
    "Jund",
    "Egr1",
    "Egr2",
    "Hsp70",
    "Mt1",
    "Mt2",
    "Vip",
    "Gap43",
    "Cck",
    "Scg2",
    "Nptx2",
    "Arrdc2",
}


@dataclass(frozen=True)
class RequiredInputs:
    methyl_dmr: Path = PHASE4_DIR / "methyl_skmgn_dmr.tsv"
    atac_dar: Path = PHASE4_DIR / "atac_skmgn_dar.tsv"
    overlap: Path = PHASE4_DIR / "exercise_reversible_regulatory_targets_fixed.tsv"
    legacy_ladder: Path = PHASE4_DIR / "regulatory_causality_ladder_fixed.tsv"
    wp3_replication: Path = BASE_DIR / "output/signatures/replication_matrix.tsv"
    wp4_panel_validation: Path = BASE_DIR / "output/validation/panel_external_validation.tsv"
    wp4_panel_manifest: Path = BASE_DIR / "output/validation/panel_manifest.tsv"
    phase3_biomarkers: Path = BASE_DIR / "output/phase3/biomarker_discovery_extended_fixed.tsv"
    phase2_anchor_expression: Path = BASE_DIR / "output/phase2/anchor_expression_by_celltype.tsv"


def read_tsv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Required input missing: {path}")
    return pd.read_csv(path, sep="\t")


def clean_bool(value: Any) -> bool:
    if pd.isna(value):
        return False
    if isinstance(value, (bool, np.bool_)):
        return bool(value)
    return str(value).strip().lower() in {"true", "1", "yes"}


def direction_from_logfc(logfc: float | int | None) -> str:
    if logfc is None or pd.isna(logfc):
        return "not_available"
    return "exercise_up" if float(logfc) > 0 else "exercise_down"


def map_rat_to_human(rat_gene: Any) -> tuple[str, str]:
    if pd.isna(rat_gene) or str(rat_gene).strip() == "":
        return "unmapped", "not_available"
    gene = str(rat_gene).strip()
    if gene in RAT_TO_HUMAN_ORTHOLOG:
        return RAT_TO_HUMAN_ORTHOLOG[gene], "curated_rat_to_human_symbol_mapping"
    if gene.upper().startswith("RGD") or gene.lower().startswith("mir"):
        return "unmapped", "no_curated_human_ortholog_in_local_mapping"
    return gene.upper(), "symbol_case_mapping_unverified"


def human_to_rat(human_gene: Any) -> str:
    if pd.isna(human_gene):
        return "unmapped"
    gene = str(human_gene).strip().upper()
    for rat, human in RAT_TO_HUMAN_ORTHOLOG.items():
        if human == gene:
            return rat
    return "unmapped"


def parse_locus(locus: Any) -> tuple[str, str]:
    if pd.isna(locus) or "-" not in str(locus):
        return "not_available", "not_available"
    start, end = str(locus).split("-", 1)
    return start, end


def panel_gene_map(panel_manifest: pd.DataFrame, panel_validation: pd.DataFrame) -> dict[str, dict[str, Any]]:
    panel_summary: dict[str, dict[str, Any]] = {}
    for _, manifest_row in panel_manifest.iterrows():
        genes_text = str(manifest_row.get("genes", ""))
        if genes_text == "split_specific":
            continue
        genes = [gene.strip().upper() for gene in genes_text.split(",") if gene.strip()]
        panel_name = str(manifest_row["panel_name"])
        validation_rows = panel_validation[panel_validation["panel_name"] == panel_name].copy()
        external_rows = validation_rows[validation_rows["split_type"] == "external_test_cohort"]
        best_external_auc = np.nan
        best_external_pr_auc = np.nan
        if len(external_rows) > 0:
            best_external_auc = float(external_rows["roc_auc"].max())
            best_external_pr_auc = float(external_rows["pr_auc"].max())
        success_any = bool(validation_rows["primary_auc_success"].map(clean_bool).any())
        strong_any = bool(validation_rows["strong_success"].map(clean_bool).any())

        if panel_name == "locked_hmsr_igf1_cdk6_col3a1":
            status = "locked_hmsr_panel_failed_external_validation"
        elif "literature" in panel_name and success_any:
            status = "literature_panel_conditional_success_with_leakage_caveat"
        elif success_any:
            status = "panel_success_in_at_least_one_split"
        else:
            status = "panel_tested_no_primary_success"

        for gene in genes:
            existing = panel_summary.get(gene, {})
            panel_names = sorted(set(str(existing.get("panel_names", "")).split(";")) | {panel_name})
            panel_names = [x for x in panel_names if x]
            panel_summary[gene] = {
                "biomarker_layer": 1,
                "panel_names": ";".join(panel_names),
                "biomarker_status": status
                if not existing
                else merge_panel_status(str(existing["biomarker_status"]), status),
                "biomarker_best_external_auc": np.nanmax(
                    [existing.get("biomarker_best_external_auc", np.nan), best_external_auc]
                ),
                "biomarker_best_external_pr_auc": np.nanmax(
                    [existing.get("biomarker_best_external_pr_auc", np.nan), best_external_pr_auc]
                ),
                "biomarker_primary_success_any": bool(
                    existing.get("biomarker_primary_success_any", False) or success_any
                ),
                "biomarker_strong_success_any": bool(
                    existing.get("biomarker_strong_success_any", False) or strong_any
                ),
                "biomarker_leakage_note": str(manifest_row.get("leakage_note", "")),
            }
    return panel_summary


def merge_panel_status(old_status: str, new_status: str) -> str:
    statuses = {old_status, new_status}
    if "locked_hmsr_panel_failed_external_validation" in statuses and any(
        "conditional_success" in status or "success" in status for status in statuses
    ):
        return "mixed_panel_evidence"
    if any("conditional_success" in status for status in statuses):
        return "literature_panel_conditional_success_with_leakage_caveat"
    if any("success" in status for status in statuses):
        return "panel_success_in_at_least_one_split"
    if "locked_hmsr_panel_failed_external_validation" in statuses:
        return "locked_hmsr_panel_failed_external_validation"
    return sorted(statuses)[0]


def build_wp3_map(replication: pd.DataFrame) -> dict[str, dict[str, Any]]:
    wp3 = replication.copy()
    wp3["gene_symbol"] = wp3["gene_symbol"].astype(str).str.upper()
    wp3["heterogeneity_flag"] = wp3["heterogeneity_flag"].map(clean_bool)
    replicated = (
        (wp3["meta_fdr"] <= 0.10)
        & (wp3["n_cohorts_detected"] >= 3)
        & (wp3["direction_consistency"] >= 0.75)
        & (~wp3["heterogeneity_flag"])
    )
    wp3["wp3_sarcopenia_replication_layer"] = replicated.astype(int)
    out: dict[str, dict[str, Any]] = {}
    for _, row in wp3.iterrows():
        gene = row["gene_symbol"]
        out[gene] = {
            "wp3_sarcopenia_replication_layer": int(row["wp3_sarcopenia_replication_layer"]),
            "wp3_replication_status": "cohort_aware_replicated"
            if int(row["wp3_sarcopenia_replication_layer"])
            else "not_replicated_by_wp3_threshold",
            "wp3_meta_direction": row["meta_direction"],
            "wp3_meta_beta": row["meta_beta"],
            "wp3_meta_fdr": row["meta_fdr"],
            "wp3_n_cohorts_detected": row["n_cohorts_detected"],
            "wp3_direction_consistency": row["direction_consistency"],
            "wp3_leave_one_cohort_out_rate": row["leave_one_cohort_out_replication_rate"],
            "wp3_heterogeneity_flag": bool(row["heterogeneity_flag"]),
        }
    return out


def build_anchor_map(anchor_expression: pd.DataFrame) -> dict[str, dict[str, Any]]:
    anchors = anchor_expression.copy()
    anchors["gene"] = anchors["gene"].astype(str).str.upper()
    out: dict[str, dict[str, Any]] = {}
    for gene, group in anchors.groupby("gene"):
        best = group.sort_values(["pct_expressing", "mean_expression"], ascending=False).head(1)
        out[gene] = {
            "cell_state_context_layer": 1,
            "cell_state_source": "phase2_anchor_expression_by_celltype",
            "cell_state_best_context": str(best["cell_type"].iloc[0]),
            "cell_state_best_age_group": str(best["age_group"].iloc[0]),
            "cell_state_max_pct_expressing": float(best["pct_expressing"].iloc[0]),
        }
    return out


def build_legacy_map(legacy_ladder: pd.DataFrame) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    for _, row in legacy_ladder.iterrows():
        raw_gene = str(row["gene"]).strip()
        mapped, _ = map_rat_to_human(raw_gene)
        gene = mapped if mapped != "unmapped" else raw_gene.upper()
        out[gene] = {
            "legacy_phase4_gene_label": raw_gene,
            "human_hallmark_layer": int(row["in_hallmark"]),
            "human_pseudobulk_layer": int(row["in_pseudobulk_de"]),
            "legacy_bulk_proxy_layer": int(row["in_bulk_de"]),
            "legacy_bulk_proxy_note": "MyoSpectrum/myopathy proxy AUC layer, not clinical sarcopenia validation"
            if int(row["in_bulk_de"])
            else "",
            "rat_legacy_methyl_layer": int(row["in_methyl_dmr"]),
            "rat_legacy_atac_layer": int(row["in_atac_peak"]),
        }
    return out


def build_phase3_map(phase3_biomarkers: pd.DataFrame) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    for _, row in phase3_biomarkers.iterrows():
        gene = str(row["biomarker"]).strip().upper()
        out[gene] = {
            "phase3_internal_proxy_biomarker_layer": 1,
            "phase3_internal_proxy_auc": row["auc"],
            "phase3_internal_proxy_direction": row["direction"],
            "phase3_internal_proxy_note": "internal MyoSpectrum proxy screen; Helsinki phenotype unavailable",
        }
    return out


def build_exercise_epigenetic_ladder(
    methyl_dmr: pd.DataFrame,
    atac_dar: pd.DataFrame,
    overlap: pd.DataFrame,
    human_evidence_genes: set[str],
) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []

    for _, row in methyl_dmr.iterrows():
        rat_gene = str(row.get("Symbol", "")).strip()
        human_gene, mapping_status = map_rat_to_human(rat_gene)
        start, end = parse_locus(row.get("Locus"))
        rows.append(
            {
                "evidence_id": f"methyl_dmr:{row['feature_ID']}",
                "evidence_layer": "methyl_dmr",
                "rat_feature_id": row["feature_ID"],
                "rat_gene": rat_gene or "unmapped",
                "human_ortholog": human_gene,
                "ortholog_mapping_status": mapping_status,
                "source_dataset": SOURCE_DATASET,
                "species": RAT_SPECIES,
                "tissue": RAT_TISSUE,
                "timepoint": row["comparison_group"],
                "comparison_group": row["comparison_group"],
                "exercise_logFC": row["logFC"],
                "exercise_direction": direction_from_logfc(row["logFC"]),
                "p_value": row["p_value"],
                "fdr": row["adj_p_value"],
                "chr": f"chr{row['Chr']}",
                "start": start,
                "end": end,
                "peak_mid": "not_applicable",
                "gene_distance_mapping": "methylation_output_symbol_annotation",
                "peak_to_gene_provenance": "not_applicable_methylation_symbol_annotation",
                "mapping_method": "MoTrPAC methylation DMR table Symbol field plus curated ortholog lookup",
                "human_muscle_relevance_in_current_outputs": int(human_gene in human_evidence_genes),
                "claim_scope": "rat_exercise_methylation_hit_only",
                "notes": "Gene-level exercise claim is limited to rat methylation evidence unless paired human evidence is present.",
            }
        )

    for _, row in atac_dar.iterrows():
        rows.append(
            {
                "evidence_id": f"atac_dar:{row['feature_ID']}:{row['comparison_group']}",
                "evidence_layer": "atac_dar",
                "rat_feature_id": row["feature_ID"],
                "rat_gene": "unmapped",
                "human_ortholog": "unmapped",
                "ortholog_mapping_status": "no_peak_to_gene_mapping_in_local_dar_table",
                "source_dataset": SOURCE_DATASET,
                "species": RAT_SPECIES,
                "tissue": RAT_TISSUE,
                "timepoint": row["comparison_group"],
                "comparison_group": row["comparison_group"],
                "exercise_logFC": row["logFC"],
                "exercise_direction": direction_from_logfc(row["logFC"]),
                "p_value": row["p_value"],
                "fdr": row["adj_p_value"],
                "chr": row["chr"],
                "start": row["peak_start"],
                "end": row["peak_end"],
                "peak_mid": row["peak_mid"],
                "gene_distance_mapping": "not_available",
                "peak_to_gene_provenance": "coordinate_only_local_DAR_table_no_gene_distance_mapping",
                "mapping_method": "MoTrPAC ATAC DAR coordinates only",
                "human_muscle_relevance_in_current_outputs": 0,
                "claim_scope": "exercise_chromatin_accessibility_feature_only_not_gene_regulatory",
                "notes": "No gene-level exercise-regulated claim is made for this DAR without peak-to-gene mapping.",
            }
        )

    dmr_by_gene = (
        methyl_dmr.assign(_rat_gene=methyl_dmr["Symbol"].astype(str))
        .drop_duplicates(subset="Symbol", keep="first")
        .set_index("_rat_gene")
    )
    for _, row in overlap.iterrows():
        rat_gene = str(row["gene"]).strip()
        human_gene, mapping_status = map_rat_to_human(rat_gene)
        dmr_row = dmr_by_gene.loc[rat_gene] if rat_gene in dmr_by_gene.index else None
        dmr_logfc = dmr_row["logFC"] if dmr_row is not None else np.nan
        dmr_timepoint = dmr_row["comparison_group"] if dmr_row is not None else "not_available"
        dmr_feature = dmr_row["feature_ID"] if dmr_row is not None else "not_available"
        rows.append(
            {
                "evidence_id": f"dmr_atac_overlap:{rat_gene}",
                "evidence_layer": "dmr_atac_overlap",
                "rat_feature_id": dmr_feature,
                "rat_gene": rat_gene,
                "human_ortholog": human_gene,
                "ortholog_mapping_status": mapping_status,
                "source_dataset": SOURCE_DATASET,
                "species": RAT_SPECIES,
                "tissue": RAT_TISSUE,
                "timepoint": dmr_timepoint,
                "comparison_group": dmr_timepoint,
                "exercise_logFC": dmr_logfc,
                "exercise_direction": direction_from_logfc(dmr_logfc),
                "p_value": dmr_row["p_value"] if dmr_row is not None else np.nan,
                "fdr": dmr_row["adj_p_value"] if dmr_row is not None else np.nan,
                "chr": f"chr{dmr_row['Chr']}" if dmr_row is not None else "not_available",
                "start": parse_locus(dmr_row["Locus"])[0] if dmr_row is not None else "not_available",
                "end": parse_locus(dmr_row["Locus"])[1] if dmr_row is not None else "not_available",
                "peak_mid": "not_available",
                "gene_distance_mapping": "DMR Symbol plus recovered ATAC gene label; coordinate-resolved peak distance unavailable",
                "peak_to_gene_provenance": "recovery_gates.py RECOVERED_ATAC_GENE_LABELS equivalent; exact DAR-to-gene mapping absent",
                "mapping_method": "DMR Symbol annotation intersected with recovered ATAC gene labels",
                "human_muscle_relevance_in_current_outputs": int(human_gene in human_evidence_genes),
                "claim_scope": "rat_exercise_epigenetic_hit_only",
                "notes": "Downgraded from exercise-reversible regulatory target because human muscle relevance and exact ATAC peak mapping are not established locally.",
            }
        )

    out = pd.DataFrame(rows)
    sort_order = {"dmr_atac_overlap": 0, "methyl_dmr": 1, "atac_dar": 2}
    out["_sort_layer"] = out["evidence_layer"].map(sort_order).fillna(9)
    out = out.sort_values(["_sort_layer", "rat_gene", "timepoint", "rat_feature_id"]).drop(columns="_sort_layer")
    return out


def disease_exercise_direction(disease_direction: str, exercise_direction: str) -> str:
    if not disease_direction or disease_direction == "not_available":
        return "exercise_only_no_replicated_human_disease_direction"
    if exercise_direction == "not_available":
        return "human_only_no_exercise_direction"
    if disease_direction == "case_up" and exercise_direction == "exercise_down":
        return "disease_up_exercise_down"
    if disease_direction == "case_down" and exercise_direction == "exercise_up":
        return "disease_down_exercise_up"
    if disease_direction == "case_up" and exercise_direction == "exercise_up":
        return "concordant_non_reversible_case_up_exercise_up"
    if disease_direction == "case_down" and exercise_direction == "exercise_down":
        return "concordant_non_reversible_case_down_exercise_down"
    return "direction_unresolved"


def claim_scope_for_row(row: dict[str, Any]) -> str:
    human_layers = row["n_human_layers"]
    rat_layers = row["rat_epigenetic_layers"]
    if rat_layers > 0 and human_layers == 0:
        return "rat_exercise_epigenetic_hit_only"
    if row["wp3_sarcopenia_replication_layer"] and rat_layers > 0:
        return "cross_species_directional_hypothesis_without_mechanistic_proof"
    if row["wp3_sarcopenia_replication_layer"]:
        return "human_sarcopenia_expression_association"
    if row["biomarker_layer"] and not row["biomarker_primary_success_any"]:
        return "biomarker_hypothesis_external_validation_failed_or_incomplete"
    if human_layers > 0:
        return "human_multilayer_association_no_regulatory_claim"
    return "insufficient_current_evidence"


def build_human_multilayer_evidence_ladder(
    methyl_dmr: pd.DataFrame,
    legacy_ladder: pd.DataFrame,
    wp3_replication: pd.DataFrame,
    panel_validation: pd.DataFrame,
    panel_manifest: pd.DataFrame,
    phase3_biomarkers: pd.DataFrame,
    anchor_expression: pd.DataFrame,
) -> pd.DataFrame:
    legacy = build_legacy_map(legacy_ladder)
    wp3 = build_wp3_map(wp3_replication)
    panel = panel_gene_map(panel_manifest, panel_validation)
    phase3 = build_phase3_map(phase3_biomarkers)
    anchors = build_anchor_map(anchor_expression)

    dmr_by_human: dict[str, dict[str, Any]] = {}
    for _, row in methyl_dmr.iterrows():
        rat_gene = str(row["Symbol"]).strip()
        human_gene, _ = map_rat_to_human(rat_gene)
        if human_gene == "unmapped":
            continue
        dmr_by_human[human_gene] = {
            "rat_ortholog": rat_gene,
            "rat_exercise_direction": direction_from_logfc(row["logFC"]),
            "rat_exercise_timepoint": row["comparison_group"],
            "rat_exercise_logFC": row["logFC"],
        }

    replicated_wp3_genes = {
        gene for gene, values in wp3.items() if values["wp3_sarcopenia_replication_layer"] == 1
    }
    candidate_genes = (
        set(legacy)
        | set(panel)
        | set(phase3)
        | set(anchors)
        | set(dmr_by_human)
        | set(replicated_wp3_genes)
        | HALLMARK_GENES
        | ANCHOR_GENES
    )

    rows: list[dict[str, Any]] = []
    for gene in sorted(candidate_genes):
        legacy_values = legacy.get(gene, {})
        wp3_values = wp3.get(gene, {})
        panel_values = panel.get(gene, {})
        phase3_values = phase3.get(gene, {})
        anchor_values = anchors.get(gene, {})
        dmr_values = dmr_by_human.get(gene, {})

        rat_ortholog = dmr_values.get("rat_ortholog", human_to_rat(gene))
        rat_legacy_methyl = int(legacy_values.get("rat_legacy_methyl_layer", 0))
        rat_legacy_atac = int(legacy_values.get("rat_legacy_atac_layer", 0))
        rat_epigenetic_layers = rat_legacy_methyl + rat_legacy_atac
        rat_epigenetic_status = (
            "rat_dmr_plus_recovered_atac_label"
            if rat_legacy_methyl and rat_legacy_atac
            else "rat_dmr_only"
            if rat_legacy_methyl
            else "recovered_atac_label_only"
            if rat_legacy_atac
            else "none"
        )

        disease_direction = str(wp3_values.get("wp3_meta_direction", "not_available"))
        exercise_direction = str(dmr_values.get("rat_exercise_direction", "not_available"))
        human_hallmark = int(legacy_values.get("human_hallmark_layer", int(gene in HALLMARK_GENES)))
        human_pseudobulk = int(legacy_values.get("human_pseudobulk_layer", 0))
        legacy_bulk_proxy = int(legacy_values.get("legacy_bulk_proxy_layer", 0))
        wp3_layer = int(wp3_values.get("wp3_sarcopenia_replication_layer", 0))
        biomarker_layer = int(panel_values.get("biomarker_layer", 0))
        phase3_layer = int(phase3_values.get("phase3_internal_proxy_biomarker_layer", 0))
        cell_state_layer = int(anchor_values.get("cell_state_context_layer", 0))

        n_human_layers = int(
            human_hallmark
            + human_pseudobulk
            + legacy_bulk_proxy
            + wp3_layer
            + biomarker_layer
            + phase3_layer
            + cell_state_layer
        )
        row_out: dict[str, Any] = {
            "human_gene": gene,
            "rat_ortholog": rat_ortholog,
            "ortholog_mapping_status": "curated_rat_to_human_symbol_mapping"
            if rat_ortholog != "unmapped"
            else "not_mapped_to_rat_exercise_gene",
            "rat_epigenetic_layers": rat_epigenetic_layers,
            "rat_epigenetic_status": rat_epigenetic_status,
            "rat_exercise_direction": exercise_direction,
            "rat_exercise_timepoint": dmr_values.get("rat_exercise_timepoint", "not_available"),
            "rat_exercise_logFC": dmr_values.get("rat_exercise_logFC", np.nan),
            "human_hallmark_layer": human_hallmark,
            "human_pseudobulk_layer": human_pseudobulk,
            "legacy_bulk_proxy_layer": legacy_bulk_proxy,
            "legacy_bulk_proxy_note": legacy_values.get("legacy_bulk_proxy_note", ""),
            "wp3_sarcopenia_replication_layer": wp3_layer,
            "wp3_replication_status": wp3_values.get(
                "wp3_replication_status", "not_tested_or_not_replicated"
            ),
            "wp3_meta_direction": disease_direction,
            "wp3_meta_beta": wp3_values.get("wp3_meta_beta", np.nan),
            "wp3_meta_fdr": wp3_values.get("wp3_meta_fdr", np.nan),
            "wp3_n_cohorts_detected": wp3_values.get("wp3_n_cohorts_detected", np.nan),
            "wp3_direction_consistency": wp3_values.get("wp3_direction_consistency", np.nan),
            "wp3_leave_one_cohort_out_rate": wp3_values.get(
                "wp3_leave_one_cohort_out_rate", np.nan
            ),
            "wp3_heterogeneity_flag": wp3_values.get("wp3_heterogeneity_flag", np.nan),
            "biomarker_layer": biomarker_layer,
            "panel_names": panel_values.get("panel_names", ""),
            "biomarker_status": panel_values.get("biomarker_status", ""),
            "biomarker_best_external_auc": panel_values.get("biomarker_best_external_auc", np.nan),
            "biomarker_best_external_pr_auc": panel_values.get(
                "biomarker_best_external_pr_auc", np.nan
            ),
            "biomarker_primary_success_any": bool(
                panel_values.get("biomarker_primary_success_any", False)
            ),
            "biomarker_strong_success_any": bool(
                panel_values.get("biomarker_strong_success_any", False)
            ),
            "biomarker_leakage_note": panel_values.get("biomarker_leakage_note", ""),
            "phase3_internal_proxy_biomarker_layer": phase3_layer,
            "phase3_internal_proxy_auc": phase3_values.get("phase3_internal_proxy_auc", np.nan),
            "phase3_internal_proxy_direction": phase3_values.get(
                "phase3_internal_proxy_direction", ""
            ),
            "phase3_internal_proxy_note": phase3_values.get("phase3_internal_proxy_note", ""),
            "cell_state_context_layer": cell_state_layer,
            "cell_state_source": anchor_values.get("cell_state_source", ""),
            "cell_state_best_context": anchor_values.get("cell_state_best_context", ""),
            "cell_state_best_age_group": anchor_values.get("cell_state_best_age_group", ""),
            "cell_state_max_pct_expressing": anchor_values.get(
                "cell_state_max_pct_expressing", np.nan
            ),
            "directionality_class": disease_exercise_direction(
                disease_direction if wp3_layer else "not_available", exercise_direction
            ),
            "n_human_layers": n_human_layers,
            "n_total_evidence_layers": n_human_layers + rat_epigenetic_layers,
            "source_dataset": "WP3 validation cohorts; Phase2 HLMA; Phase3 proxy biomarkers; WP4 external panel tests; MoTrPAC rat exercise",
            "species": "Homo sapiens; Rattus norvegicus when rat_epigenetic_layers > 0",
            "tissue": "human skeletal muscle cohorts; rat skeletal_muscle_gastrocnemius for exercise layers",
            "timepoint": dmr_values.get("rat_exercise_timepoint", "not_applicable_for_human_only_layers"),
            "mapping_method": "human gene symbol evidence joined to rat ortholog only when curated mapping exists",
            "regulatory_layer_mapping_provenance": "rat DMR Symbol annotation; recovered ATAC labels lack coordinate-resolved peak-to-gene distance",
        }
        row_out["claim_scope"] = claim_scope_for_row(row_out)
        rows.append(row_out)

    out = pd.DataFrame(rows)
    return out.sort_values(
        [
            "wp3_sarcopenia_replication_layer",
            "n_human_layers",
            "rat_epigenetic_layers",
            "human_gene",
        ],
        ascending=[False, False, False, True],
    )


def write_fig4_split(exercise: pd.DataFrame, human: pd.DataFrame) -> None:
    FIGURE_DIR.mkdir(parents=True, exist_ok=True)
    fig, axes = plt.subplots(1, 2, figsize=(11, 5.6), dpi=270)

    exercise_counts = pd.Series(
        {
            "DMR genes": int((exercise["evidence_layer"] == "methyl_dmr").sum()),
            "DAR features": int((exercise["evidence_layer"] == "atac_dar").sum()),
            "DMR+ATAC labels": int((exercise["evidence_layer"] == "dmr_atac_overlap").sum()),
            "Mapped orthologs": int(
                ((exercise["human_ortholog"] != "unmapped") & (exercise["evidence_layer"] != "atac_dar")).sum()
            ),
        }
    )
    colors_left = ["#3C8DAD", "#F39B4A", "#6B5B95", "#2E7D32"]
    axes[0].bar(exercise_counts.index, exercise_counts.values, color=colors_left)
    axes[0].set_title("Rat Exercise Epigenetic Evidence")
    axes[0].set_ylabel("Count")
    axes[0].tick_params(axis="x", rotation=30)
    axes[0].spines[["top", "right"]].set_visible(False)
    for idx, value in enumerate(exercise_counts.values):
        axes[0].text(idx, value + 0.5, str(value), ha="center", va="bottom", fontsize=9)

    human_counts = pd.Series(
        {
            "WP3 replicated": int(human["wp3_sarcopenia_replication_layer"].sum()),
            "Hallmark": int(human["human_hallmark_layer"].sum()),
            "Pseudobulk": int(human["human_pseudobulk_layer"].sum()),
            "Legacy bulk proxy": int(human["legacy_bulk_proxy_layer"].sum()),
            "Biomarker panel": int(human["biomarker_layer"].sum()),
            "Cell context": int(human["cell_state_context_layer"].sum()),
        }
    )
    colors_right = ["#2E7D32", "#6B5B95", "#3C8DAD", "#9E9E9E", "#C84B31", "#D4A017"]
    axes[1].bar(human_counts.index, human_counts.values, color=colors_right)
    axes[1].set_title("Human Multi-Layer Evidence")
    axes[1].set_ylabel("Genes")
    axes[1].tick_params(axis="x", rotation=35)
    axes[1].spines[["top", "right"]].set_visible(False)
    for idx, value in enumerate(human_counts.values):
        axes[1].text(idx, value + 0.8, str(value), ha="center", va="bottom", fontsize=9)

    fig.suptitle("Figure 4. Evidence Split: Exercise Epigenetics vs Human Disease Evidence", y=0.98)
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    fig.savefig(FIGURE_DIR / "fig4_ladder_split.png")
    fig.savefig(FIGURE_DIR / "fig4_ladder_split.pdf")
    plt.close(fig)


def write_readiness(exercise: pd.DataFrame, human: pd.DataFrame) -> None:
    dmr_count = int((exercise["evidence_layer"] == "methyl_dmr").sum())
    dar_count = int((exercise["evidence_layer"] == "atac_dar").sum())
    double_hit = exercise[exercise["evidence_layer"] == "dmr_atac_overlap"]
    downgraded = sorted(double_hit["rat_gene"].tolist())
    wp3_replicated = int(human["wp3_sarcopenia_replication_layer"].sum())
    locked = human[human["panel_names"].str.contains("locked_hmsr", na=False)]
    locked_status = sorted(set(locked["biomarker_status"].dropna().astype(str)))
    table_text = " ".join(
        list(exercise.columns)
        + list(human.columns)
        + exercise.fillna("").astype(str).agg(" ".join, axis=1).tolist()
        + human.fillna("").astype(str).agg(" ".join, axis=1).tolist()
    ).lower()
    no_causality = "causality" not in table_text and "causal" not in table_text
    text = f"""# WP5 Regulatory And Exercise Evidence Readiness

Generated: 2026-06-08

## Decision Context

WP5 separates rat exercise epigenetic perturbation evidence from human disease, cell-state, and biomarker evidence. The output supports hypothesis generation, not regulatory mechanism claims.

## Data Audit

- Rat DMR rows: {dmr_count}
- Rat DAR feature rows: {dar_count}
- Rat DMR plus recovered ATAC label rows: {len(double_hit)}
- Downgraded double-hit genes: {', '.join(downgraded)}
- Human WP3 cohort-aware replicated genes: {wp3_replicated}
- Locked HMSR panel gene statuses: {'; '.join(locked_status) if locked_status else 'not_present'}

## Claim Controls

- New WP5 table columns avoid causality language: {no_causality}
- DAR rows are feature-level only because the local DAR table has coordinates but no peak-to-gene distance mapping.
- `Vip`, `Gap43`, and `Cck` are labeled `rat_exercise_epigenetic_hit_only` unless current human evidence layers support stronger interpretation.
- The old MyoSpectrum bulk layer is retained only as `legacy_bulk_proxy_layer`.

## Outputs

- `output/phase4/exercise_epigenetic_ladder.tsv`
- `output/phase4/human_multilayer_evidence_ladder.tsv`
- `output/figures/fig4_ladder_split.png`
- `output/figures/fig4_ladder_split.pdf`
"""
    (PHASE4_DIR / "wp5_regulatory_evidence_readiness.md").write_text(text)


def main() -> None:
    inputs = RequiredInputs()
    PHASE4_DIR.mkdir(parents=True, exist_ok=True)
    FIGURE_DIR.mkdir(parents=True, exist_ok=True)

    methyl_dmr = read_tsv(inputs.methyl_dmr)
    atac_dar = read_tsv(inputs.atac_dar)
    overlap = read_tsv(inputs.overlap)
    legacy_ladder = read_tsv(inputs.legacy_ladder)
    wp3_replication = read_tsv(inputs.wp3_replication)
    panel_validation = read_tsv(inputs.wp4_panel_validation)
    panel_manifest = read_tsv(inputs.wp4_panel_manifest)
    phase3_biomarkers = read_tsv(inputs.phase3_biomarkers)
    anchor_expression = read_tsv(inputs.phase2_anchor_expression)

    human = build_human_multilayer_evidence_ladder(
        methyl_dmr=methyl_dmr,
        legacy_ladder=legacy_ladder,
        wp3_replication=wp3_replication,
        panel_validation=panel_validation,
        panel_manifest=panel_manifest,
        phase3_biomarkers=phase3_biomarkers,
        anchor_expression=anchor_expression,
    )
    human_evidence_genes = set(
        human.loc[human["n_human_layers"] > 0, "human_gene"].astype(str).str.upper()
    )
    exercise = build_exercise_epigenetic_ladder(
        methyl_dmr=methyl_dmr,
        atac_dar=atac_dar,
        overlap=overlap,
        human_evidence_genes=human_evidence_genes,
    )

    exercise.to_csv(PHASE4_DIR / "exercise_epigenetic_ladder.tsv", sep="\t", index=False)
    human.to_csv(PHASE4_DIR / "human_multilayer_evidence_ladder.tsv", sep="\t", index=False)
    write_fig4_split(exercise, human)
    write_readiness(exercise, human)

    print("WP5 complete")
    print(f"exercise_rows={len(exercise)}")
    print(f"human_rows={len(human)}")
    print(f"figure_png={FIGURE_DIR / 'fig4_ladder_split.png'}")


if __name__ == "__main__":
    main()
