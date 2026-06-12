# Codex Adversarial Review - HMSR Sarcopenia Paper 1 v0.3

**Verdict: No-needs-major.** The pathway-level mitochondrial signal is reproducible and probably defensible as an exploratory resource result, but v0.3 does not clear a JCR 5-10% resource/physiology journal as written because the central statistic is described inconsistently, the covariate-adjusted permutation null is not fully exchangeability-correct, the figures still leak "replicated" language, and Table 1 misreports cohort demographics.

Reviewed at repo HEAD `495ee23`; no manuscript, pipeline, or output files were intentionally edited.

## Findings Table

| Severity | Issue | File:line | Specific number or logic | Suggested fix |
|---|---|---|---|---|
| MAJOR | Headline pathway statistic mixes meta-analysis flavours in the Results. The text says the `-1.14` competitive shift comes from ranking all genes by random-effects meta-z, but `wp3c_permutation.tsv` is generated from a Stouffer recomputation, not DL random-effects. | `manuscripts/paper1_v0.3.md:141-144`; `manuscripts/paper1_v0.3.md:347-349`; `scripts/pathway_permutation.py:99-110`; `output/signatures/wp3c_permutation.tsv:5` | `Mito_ALL observed_diff=-1.137435` is the Stouffer permutation statistic. The same broad set on DL `replication_matrix.tsv` gives in-set mean z `-0.854407`, out-set mean z `0.060455`, competitive diff `-0.914862`, not `-1.14`. | Either rerun WP3c using the exact DL statistic or change Results to say the inferential permutation uses Stouffer meta-z, while DL meta-z/AUC are descriptive companion estimates. |
| MAJOR | The permutation preserves gene-gene correlation, but it is not a fully covariate-exchangeability-aware permutation for the age/sex-adjusted regression. Labels are permuted within cohort while age/sex covariates remain fixed. | `scripts/pathway_permutation.py:60-68`; `scripts/pathway_permutation.py:140-147`; `manuscripts/paper1_v0.3.md:148-152` | Age is imbalanced in the two driver cohorts: SSS cases 72.75 vs controls 70.20 years; GESTALT cases 71.55 vs controls 67.65 years. The exact run emitted overflow/divide warnings inside the vectorized OLS (`scripts/pathway_permutation.py:82-83`), consistent with some permuted designs becoming ill-conditioned. | Use a Freedman-Lane / residual-permutation procedure for the sarcopenia term after covariate adjustment, or a stratified/matched label permutation that preserves sex and age-bin structure. Report the count of non-finite gene statistics per permutation. |
| MAJOR | Table 1 cohort demographics are wrong relative to local metadata. This is a credibility problem, not a statistical subtlety. | `manuscripts/paper1_v0.3.md:96-114`; `data/validation_cohorts/GSE111006_HSS/metadata.tsv:2`; `data/validation_cohorts/GSE111016_SSS/metadata.tsv:2` | Manuscript: HSS "South Korea" and SSS "South Korea/Female". Local metadata: HSS is Hertfordshire/Caucasian descent/male; SSS is Singapore Sarcopenia Study/Chinese descent/male. JSS and GESTALT labels are consistent with metadata. | Replace country/sex/population labels using the curated metadata; do not infer demographics from acronym expansion. |
| MAJOR | The submitted figure generator still calls the post-hoc gate "replicated genes", contradicting the corrected manuscript text. | `scripts/make_manuscript_figures.py:212-214`; `scripts/make_manuscript_figures.py:336-340`; `manuscripts/paper1_v0.3.md:333-339` | Figure 1 text says `-> 195 replicated genes`; Figure 3 legend says `Replicated down/up`. The manuscript correctly says the gate is post-hoc and candidates are not validated. | Change all figure/table labels to "candidate", "gate-pass", or "direction-concordant"; reserve "replication" for independent significance or a prospective cohort. |
| MAJOR | Residual technical/QC confounding is honestly stated for RIN/batch, but existing raw counts permit an unrun library-size/QC sensitivity. | `manuscripts/paper1_v0.3.md:248-253`; `data/validation_cohorts/GSE226151/metadata.tsv:1-4`; `output/signatures/model_audit.tsv:5` | No local metadata columns contain `RIN`, batch, lane, read/QC, or library-size fields beyond constant `library_strategy`. But raw count library sizes are derivable: GESTALT case mean 13,496,042 vs control mean 14,770,576 reads, ratio 0.914; SSS ratio 0.930. | Add a sensitivity with log library size or total assigned counts as a QC covariate where raw counts exist, plus an age-matched/age-residual sensitivity for GESTALT and SSS. |
| MINOR | Gene-set definitions are regex-based and internally inconsistent: `Mito_ALL` is not the union of the six subprogrammes. | `scripts/pathway_permutation.py:37-48`; `scripts/pathway_enrichment.py:40-55` | `Mito_ALL` has 539 genes; the union of six mito subprogrammes has 537. `Mito_ALL` omits 10 subprogramme genes (`APOO`, `APOOL`, `MICU1/2/3`, `APOOP*`) and adds 12 genes (`ATPAF1/2`, `COA*`, `COA6-AS1`, `COASY`). Gate enrichment is 26/195 with the WP3b regex but 27/195 with WP3c `Mito_ALL`. | Freeze a curated MitoCarta/GO/HGNC list, make aggregate = union + explicitly listed additions, and exclude pseudogene/antisense matches unless intentionally included. |
| MINOR | No control-set leakage was found, which is good, but this should be documented. | `scripts/pathway_permutation.py:37-48`; `output/signatures/wp3c_permutation.tsv:9-11` | `Mito_ALL ∩ Control_cyto_ribosome = 0`; `MRPL/MRPS` are not captured by `^(RPL|RPS)`. Proteasome/collagen controls also have zero overlap with `Mito_ALL`. | Add a small set-overlap audit TSV so reviewers can see this without re-running code. |
| MINOR | Composition proxy is useful but should not be called a definitive purity/deconvolution control. | `scripts/confound_sensitivity.py:34-39`; `scripts/confound_sensitivity.py:90-97`; `manuscripts/paper1_v0.3.md:224-253` | Marker coverage is good (12 stromal markers, 5-8 immune markers), and proxy-label correlations are weak (GESTALT r=0.144; SSS r=-0.036), so it is not just a recoding of case status. But marker averages can absorb true disease biology and do not estimate myofiber fraction. | Keep the result as "robust to a stromal/immune marker proxy", not "purity artifact excluded"; add deconvolution when a muscle reference/QC-annotated dataset is available. |
| MINOR | OLS on log2 CPM is defensible for normalized matrices, but no limma-trend/voom or empirical-Bayes sensitivity is shown despite local raw counts existing. | `pipeline/recompute_disease_signatures.py:4-9`; `manuscripts/paper1_v0.3.md:320-325`; `output/validation/cohort_inventory.tsv:2-5` | Current OLS SEs drive DL weights and gene-level p-values. The permutation p is internally calibrated to the same OLS statistic, but gene-level rankings and highlighted candidates may differ under limma-trend/voom. | Add a secondary limma-trend/voom sensitivity from raw counts where available, at least for the highlighted genes and Mito_ALL statistic. |
| MINOR | DerSimonian-Laird implementation is correct, but the gate still contains a redundant LOCO criterion. | `pipeline/recompute_disease_signatures.py:349-397`; `pipeline/recompute_disease_signatures.py:400-421`; `pipeline/recompute_disease_signatures.py:508-516`; `manuscripts/paper1_v0.3.md:333-339` | For all 4-cohort genes, `direction_consistency=1.0` and `leave_one_cohort_out_replication_rate=1.0` were exactly equivalent: 2,033 genes had both; zero had one without the other. The manuscript discloses this, but config/code still dress the same sign check as two gate criteria. | Drop LOCO from the formal gate or rename it everywhere as a derived direction-concordance audit. |
| MINOR | Manuscript verifier count is stale. | `manuscripts/paper1_v0.3.md:358-362`; `scripts/verify.py:206-219` | The manuscript says `STATUS=PASS, 28/28`; rerun printed `PASS: 32 FAIL: 0 STATUS=PASS`. | Update the number or avoid hard-coding the pass count. |
| MINOR | CLTB is mostly handled honestly, but table/figure labels still blur "six mitochondrial plus CLTB". | `manuscripts/paper1_v0.3.md:170-185`; `manuscripts/paper1_v0.3.md:382-385`; `scripts/make_manuscript_figures.py:305-307` | Table 2 title says "Seven highlighted mitochondrial candidates" while the table includes struck-through CLTB; Figure 2 title says "highlighted mitochondrial candidates" and only the subtitle separates CLTB. | Rename to "six mitochondrial candidates plus non-mitochondrial CLTB outlier" everywhere. |
| MINOR | The word "collapse" overstates what transcriptomics measured. | `manuscripts/paper1_v0.3.md:48-49`; `manuscripts/paper1_v0.3.md:154-160`; `manuscripts/paper1_v0.3.md:269-280` | WP3c supports a coordinated mitochondrial transcript-programme down-shift. It does not directly measure mitochondrial content, biogenesis flux, respiration, or collapse. | Use "coordinated mitochondrial transcript-programme down-regulation"; reserve "biogenesis collapse" for assays of PGC-1/TFAM/mtDNA/protein/respiration or validation experiments. |

## Re-run Log

Commands run from `/Volumes/4TB/exerciseomics`:

```bash
git rev-parse --short HEAD
# 495ee23

python3 sarcopenia-multiomic-resource/scripts/verify.py
# PASS: 32  FAIL: 0
# STATUS=PASS

python3 sarcopenia-multiomic-resource/scripts/confound_sensitivity.py
# GSE111006_HSS lambda 1.396 -> 1.626
# GSE111010_JSS lambda 0.926 -> 0.885
# GSE111016_SSS lambda 1.220 -> 1.318
# GSE226151 lambda 1.928 -> 1.912
# 4/7 highlighted genes survive composition adjustment at meta-p<0.005

WP3C_NPERM=2000 python3 sarcopenia-multiomic-resource/scripts/pathway_permutation.py
# Seed 42; output hash unchanged.
# Mito_ALL p=0.001999, observed_diff=-1.137435, z_vs_null=-3.167438
# Subprogram p-values: Complex I 0.0009995; Complex II/III/IV 0.0009995;
# Complex V 0.003498; mitoribosome 0.005997; cristae/MICOS 0.0004998;
# import 0.002999. Controls: cytoribosome 0.278861; proteasome 0.118441;
# collagen 0.768616.
# Runtime warnings occurred at pathway_permutation.py:82-83 during matmul.

WP3C_NPERM=2000 python3 - <<'PY'
# imported pathway_permutation.py, set SEED=123, redirected SIG to /private/tmp/hmsr_perm_seed123
PY
# Seed 123; conclusion stable.
# Mito_ALL p=0.0009995, observed_diff=-1.137435, z_vs_null=-3.138206
# Subprogram p-values: Complex I 0.0009995; Complex II/III/IV 0.0009995;
# Complex V 0.002999; mitoribosome 0.005497; cristae/MICOS 0.0004998;
# import 0.002999. Controls: cytoribosome 0.276862; proteasome 0.116442;
# collagen 0.756122.
```

Checksum spot-check:

- `data/CHECKSUMS.txt` contains 9 output checksums; all 9 matched actual files.
- The exact WP3b/WP3c reruns left no git diff in their tracked TSV outputs.

Traceability spot-checks:

| Manuscript number | Source checked |
|---|---|
| 135 strict samples, 53 cases, 82 controls | `output/signatures/model_audit.tsv:2-5` sums to 135/53/82 |
| 37,469 genes and zero FDR <=0.10 | `output/signatures/replication_matrix.tsv` has 37,469 rows, min meta FDR 0.254799 |
| 328 genes at p<0.005 vs 187 expected; 99 at p<0.001 vs 37 expected | computed from `replication_matrix.tsv` as 328/(37469*0.005)=1.7508 and 99/(37469*0.001)=2.6422 |
| 195 candidates, 141 down and 54 up | `output/signatures/wp3_gate_pass.tsv` has 195 rows, 141 negative meta_beta and 54 positive |
| WP3c Mito_ALL p=2.0e-3, n=539 | `output/signatures/wp3c_permutation.tsv:5` |
| WP3b 4/7 survival and p-values | `output/signatures/wp3b_confound_sensitivity.tsv:2-8` |

Mandatory figure/statistic checks:

- WP3c is a **competitive** statistic (`in-set mean meta-z - out-set mean meta-z`), not a self-contained test of whether mitochondrial genes are down versus zero. That is appropriate for the manuscript's specificity claim, but the text should keep saying "relative/competitive shift" rather than implying an absolute programme-level effect independent of the rest of the transcriptome.
- Figure 5 was visually checked against `output/signatures/wp3c_permutation.tsv:2-11`. Bars, error bars (`null_sd`), and displayed p-labels match the TSV after rounding. No Figure 5 mismatch was found.

## What Is Genuinely Strong

- The manuscript is unusually honest about the gene-level ceiling: no genome-wide FDR hit, post-hoc gate, candidates not validated.
- The two-study independence correction is in the prose and abstract; it no longer sells four independent replications.
- CLTB is explicitly identified as non-mitochondrial in the manuscript text.
- The label-permutation design does preserve gene-gene correlation for the chosen competitive statistic, and the p-values are not seed-fragile at 2,000 permutations.
- The stromal/immune proxy sensitivity is a real improvement over v0.2: 4/7 highlighted genes survive, GESTALT enrichment remains high, and lambda does not fall after adjustment.
- HSS is not driving the six mitochondrial highlighted genes; excluding HSS leaves all six meta-p<0.015.
- The DL random-effects code uses the standard Q, C, tau^2, random-effects weights, beta_RE, and SE_RE formulas.

## Prior Review Closure

| Prior item | Status | Rationale |
|---|---|---|
| v0.1 C1 post-hoc gate/HARKing | Partial | Main text closed it; figures still say "replicated genes". |
| v0.1 C2 OXPHOS label and CLTB | Partial | Text mostly fixed; verifier still says "OXPHOS sentinel", and table/figure titles still blur CLTB with mitochondrial candidates. |
| v0.1 C3 LOCO as replication | Partial | Methods disclose LOCO is direction concordance; code/config/figures still retain replication wording and redundant gate logic. |
| v0.1 C4 per-gene signal rests on balanced cohorts | Closed | Text and HSS-excluded sensitivity state the gene-level fragility. |
| v0.1 C5 four independent cohorts overclaim | Closed in prose | Manuscript says two independent studies, but Table 1 demographics are wrong. |
| v0.1 M1 weak genome-wide signal | Closed | FDR failure and weak p-count enrichment are stated plainly. |
| v0.1 M2 correlation-aware enrichment | Partial | WP3c is a real correlation-aware label permutation, but Results/Methods mix DL and Stouffer statistics and covariate permutation needs tightening. |
| v0.1 M3 HSS 4-case sensitivity | Closed | HSS-excluded p-values are reported and reproduced. |
| v0.1 M4 training/test role mixing | Mostly closed | Manuscript frames the resource as discovery; `model_role` names still say frozen_training/external_test in outputs. |
| v0.1 minor strict subset count | Closed | Strict sample counts are explicit and traceable. |
| v0.1 minor effect-size calibration | Partial | Betas are shown; fold-change interpretation is still not spelled out. |
| v0.1 WP5 overlap wording | Closed | Exercise epigenetic evidence is now framed as a gap. |
| v0.2 N1 lambda inflation flag | Partial | Lambda is reported and composition sensitivity run; residual technical/age/QC explanations remain open. |
| v0.2 N2 GESTALT concentration | Partial | GESTALT/SSS enrichment is shown, but the text could be clearer that the independent driver remains high-lambda. |
| v0.2 N3 down-skew/compositional signature | Partial | Composition proxy addresses the most obvious purity artifact; no non-compositional normalization sensitivity is shown. |
| v0.2 N4 residual age confounding | Open | Age gaps are adjusted in OLS but not sensitivity-tested or stated in Limitations. |
| v0.2 required RNA-quality/composition covariates | Partial | Composition done; RIN/batch not locally available; library-size sensitivity is feasible but not run. |
| v0.2 required cell-type deconvolution | Open | Not done; acknowledged indirectly. |
| v0.2 required leave-GESTALT-out | Open | HSS-excluded sensitivity is present; GESTALT-excluded pathway/gene sensitivity is not reported. |
| v0.2 required age-matched subset | Open | Not reported. |

## Bottom Line

The manuscript has crossed from "overclaimed gene list" to a credible exploratory mitochondrial pathway resource, but it is not submission-ready at the target tier. Fix the statistic wording or recompute the permutation with DL, repair the covariate-aware permutation null, correct cohort metadata, purge "replicated" from figures/code-facing outputs, and add library-size/age/GESTALT-out sensitivities. After those changes, the paper would likely be "yes-with-minor" as a resource paper.
