from __future__ import annotations

import csv
from pathlib import Path

from scripts.extract_target_evidence import extract_target_evidence


DIFF_FIELDS = [
    "cohort",
    "source_group",
    "gene_symbol",
    "n_samples",
    "n_cases",
    "n_controls",
    "direction",
]

META_FIELDS = [
    "gene_symbol",
    "meta_direction",
    "meta_beta",
    "meta_se",
    "meta_p_value",
    "meta_fdr",
    "heterogeneity_i2",
    "heterogeneity_flag",
    "leave_one_cohort_out_replication_rate",
]


def _write_tsv(path: Path, fields: list[str], rows: list[dict[str, object]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle, fieldnames=fields, delimiter="\t", lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(rows)


def test_extract_target_evidence_counts_independent_source_groups(tmp_path: Path) -> None:
    differential = tmp_path / "differential.tsv"
    replication = tmp_path / "replication.tsv"
    output = tmp_path / "out"
    rows = [
        {
            "cohort": "A1",
            "source_group": "family_a",
            "gene_symbol": "MARCHF5",
            "n_samples": 10,
            "n_cases": 5,
            "n_controls": 5,
            "direction": "case_down",
        },
        {
            "cohort": "A2",
            "source_group": "family_a",
            "gene_symbol": "MARCHF5",
            "n_samples": 12,
            "n_cases": 6,
            "n_controls": 6,
            "direction": "case_down",
        },
        {
            "cohort": "B",
            "source_group": "study_b",
            "gene_symbol": "MARCHF5",
            "n_samples": 20,
            "n_cases": 10,
            "n_controls": 10,
            "direction": "case_up",
        },
    ]
    meta = [
        {
            "gene_symbol": "MARCHF5",
            "meta_direction": "case_down",
            "meta_beta": -0.1,
            "meta_se": 0.05,
            "meta_p_value": 0.2,
            "meta_fdr": 0.8,
            "heterogeneity_i2": 45.0,
            "heterogeneity_flag": "True",
            "leave_one_cohort_out_replication_rate": 0.25,
        }
    ]
    _write_tsv(differential, DIFF_FIELDS, rows)
    _write_tsv(replication, META_FIELDS, meta)

    claims = extract_target_evidence(
        differential_path=differential,
        replication_path=replication,
        gene="MARCHF5",
        output_dir=output,
        audit_date="2026-08-25",
    )

    assert claims["status"] == "NOT_REPLICATED"
    assert claims["cohort_summary"] == {
        "cohorts_detected": 3,
        "independent_source_groups": 2,
        "strict_binary_samples": 42,
        "cases": 21,
        "controls": 21,
        "source_group_directions": {
            "family_a": "case_down",
            "study_b": "case_up",
        },
    }
    assert (
        claims["gates"]["same_direction_in_at_least_two_independent_source_groups"]
        is False
    )
    assert (output / "MARCHF5_differential_by_cohort.tsv").exists()
    assert (output / "MARCHF5_replication.tsv").exists()
    assert (output / "MARCHF5_claims.json").exists()
