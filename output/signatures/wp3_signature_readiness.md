# WP3 Cohort-Aware Disease Signatures

Generated: 2026-06-08

## Scope

Used 4 WP2 validation cohorts and 135 strict binary samples (53 sarcopenia cases, 82 controls). Proxy/pre-sarcopenia samples were excluded from disease differential models but retained in per-sample module score output.

## Model Audit

| Cohort | Samples | Cases | Controls | Genes Tested | Covariates Used | Covariates Dropped |
|---|---:|---:|---:|---:|---|---|
| GSE111006_HSS | 32 | 4 | 28 | 15362 | sarcopenia,age_z | sex_constant,source_platform_not_estimable_within_cohort,batch_not_available |
| GSE111010_JSS | 23 | 9 | 14 | 14914 | sarcopenia,age_z | sex_constant,source_platform_not_estimable_within_cohort,batch_not_available |
| GSE111016_SSS | 40 | 20 | 20 | 37073 | sarcopenia,age_z | sex_constant,source_platform_not_estimable_within_cohort,batch_not_available |
| GSE226151 | 40 | 20 | 20 | 17988 | sarcopenia,age_z,sex_male | source_platform_not_estimable_within_cohort,batch_not_available |

## Outputs

- `output/signatures/differential_by_cohort.tsv`: per-gene, per-cohort OLS coefficient for sarcopenia case versus control.
- `output/signatures/module_scores_by_cohort.tsv`: per-sample module scores from mean within-cohort gene z-scores.
- `output/signatures/module_differential_by_cohort.tsv`: Welch tests of module scores in strict case/control samples.
- `output/signatures/replication_matrix.tsv`: DerSimonian-Laird random-effects meta-analysis, leave-one-cohort-out direction checks, and heterogeneity flags.
- `output/signatures/wp3_gate_pass.tsv`: genes passing the WP3 multi-criteria gate (meta_p<0.005, direction_consistency=1.0, LOCO=1.0, heterogeneity_flag=False).

## Top Random-Effects Gene Signals

| gene_symbol   | meta_direction   |   meta_beta |   meta_p_value |   meta_fdr |   direction_consistency | heterogeneity_flag   |
|:--------------|:-----------------|------------:|---------------:|-----------:|------------------------:|:---------------------|
| CHCHD10       | case_down        |  -0.164074  |    7.46369e-06 |   0.254799 |                1        | False                |
| CLTB          | case_down        |  -0.144813  |    1.61427e-05 |   0.254799 |                1        | False                |
| NT5DC1P1      | case_down        |  -0.0223073 |    2.04008e-05 |   0.254799 |                1        | False                |
| CCDC28B       | case_down        |  -0.215803  |    4.74054e-05 |   0.303148 |                1        | False                |
| DYNLL2        | case_down        |  -0.137276  |    6.77979e-05 |   0.303148 |                1        | False                |
| GTF2F2        | case_down        |  -0.160775  |    6.9403e-05  |   0.303148 |                1        | False                |
| PLEKHJ1       | case_down        |  -0.170305  |    7.10443e-05 |   0.303148 |                1        | False                |
| FAM160A2      | case_up          |   0.28882   |    7.50688e-05 |   0.303148 |                1        | False                |
| EIF2B3        | case_down        |  -0.112021  |    8.15083e-05 |   0.303148 |                1        | False                |
| ZIC4          | case_up          |   0.172891  |    0.000100004 |   0.303148 |                0.666667 | True                 |

## Top Module Differences

| cohort        | module        |   effect_case_vs_control |    p_value |      fdr | direction   |
|:--------------|:--------------|-------------------------:|-----------:|---------:|:------------|
| GSE226151     | mitochondrial |                -0.428402 | 0.00465458 | 0.148946 | case_down   |
| GSE111016_SSS | mitochondrial |                -0.611316 | 0.0104146  | 0.166633 | case_down   |
| GSE226151     | inflammation  |                 0.395261 | 0.0691351  | 0.530203 | case_up     |
| GSE111006_HSS | senescence    |                 0.422633 | 0.0713897  | 0.530203 | case_up     |
| GSE111010_JSS | proteostasis  |                -0.280117 | 0.0828443  | 0.530203 | case_down   |
| GSE111006_HSS | inflammation  |                 0.303156 | 0.19668    | 0.877414 | case_up     |
| GSE111006_HSS | contractile   |                -0.583723 | 0.199744   | 0.877414 | case_down   |
| GSE111016_SSS | proteostasis  |                -0.164008 | 0.245653   | 0.877414 | case_down   |
| GSE111016_SSS | autophagy     |                -0.146374 | 0.33072    | 0.877414 | case_down   |
| GSE226151     | proteostasis  |                 0.175157 | 0.330793   | 0.877414 | case_up     |
| GSE111006_HSS | proteostasis  |                -0.235574 | 0.354135   | 0.877414 | case_down   |
| GSE111010_JSS | autophagy     |                -0.174799 | 0.381313   | 0.877414 | case_down   |

## Interpretation Guardrails

- These are observational case/control expression associations, not causal effects.
- Source/platform terms were not estimable within cohorts because all assembled cohorts use the same listed platform/instrument within cohort.
- Cross-cohort source effects are handled by per-cohort models and replication summaries, not by pooled adjustment.
- GSE111006/GSE111010/GSE111016 are related through the GSE111017 study family; GSE226151 is the independent source group.
- Myopathy proxy samples from earlier HMSR phases are not used here.
