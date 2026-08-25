# MARCHF5 human sarcopenia evidence audit

Audit date: 2026-08-25

Machine-readable status: `NOT_REPLICATED`

## Result

The frozen HMSR bulk-transcriptomic outputs contain MARCHF5 measurements in
four strict human skeletal-muscle case-control subsets: 135 samples, including
53 sarcopenia cases and 82 controls. GSE111006, GSE111010, and GSE111016 belong
to the same GSE111017 study family; GSE226151 is independent. These are
therefore two independent source groups, not four independent replications.

The random-effects estimate is beta -0.0536203, SE 0.0486781, p=0.270667, and
genome-wide FDR=0.913816. The GSE111017 family points toward lower expression in
cases, while independent GSE226151 points upward. Heterogeneity I-squared is
43.1488%, the heterogeneity flag is true, and leave-one-cohort-out replication
is 0.25.

This provides direct human observational expression evidence, but it does not
support a replicated MARCHF5 association and cannot determine therapeutic
direction. It does not measure MARCHF5 ligase activity, substrate turnover,
continuous muscle function, causality, or treatment response.

## Claim-to-file map

| Claim | File |
|---|---|
| Exact cohort-level rows | `results/target_audits/MARCHF5_differential_by_cohort.tsv` |
| Exact random-effects row | `results/target_audits/MARCHF5_replication.tsv` |
| Counts, source hashes, gates, and status | `results/target_audits/MARCHF5_claims.json` |
| Deterministic extraction logic | `scripts/extract_target_evidence.py` |
| Dataset inclusion and modality | `results/dataset_audit.csv`; `results/modality_detected.csv` |

The two full source matrices are regenerable and intentionally not committed.
Their SHA-256 hashes are recorded in `MARCHF5_claims.json` and agree with
`data/CHECKSUMS.txt`.

## Reproduce the target audit

After generating the full HMSR result matrices:

```bash
python3 scripts/extract_target_evidence.py \
  --differential output/signatures/differential_by_cohort.tsv \
  --replication output/signatures/replication_matrix.tsv \
  --gene MARCHF5 \
  --output-dir results/target_audits \
  --audit-date 2026-08-25
```

The next defensible analysis is a preregistered, substrate-resolved MARCHF5
activity score tested against continuous strength or performance in independent
human datasets. Repeating the same single-gene case-control comparison is not a
new validation experiment.
