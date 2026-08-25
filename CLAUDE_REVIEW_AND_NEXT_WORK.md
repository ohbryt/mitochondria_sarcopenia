# Claude scientific review and next-work contract

## Mission

Act as a skeptical senior reviewer, computational biologist, and translational
target-validation lead. Review the frozen PPM1K–BCKDK–BCKDH manuscript and its
evidence package, then prepare the next defensible revision. Do not begin by
assuming that the target hypothesis is correct.

The current manuscript is an integrative translational analysis, not a report
of a newly validated human drug target. Its intended contribution is to
reconcile supportive external human multi-omics and mouse causality with an
independent negative human transcript audit, and to define the measurements
needed to validate or falsify the axis.

## Workspace and immutable baseline

- Repository: `/Users/ocm/orca/projects/mitochondria_sarcopenia`
- Remote: `https://github.com/ohbryt/mitochondria_sarcopenia`
- Frozen baseline commit: `56c113e`
- Canonical manuscript:
  `manuscripts/ppm1k_bckdk_bckdh_v1.0.md`
- Frozen package: `submission/ppm1k_axis_v1.0/`
- Large read-only source resource:
  `/Volumes/4TB/exerciseomics/sarcopenia-multiomic-resource`

Treat `submission/ppm1k_axis_v1.0/` as immutable. Any accepted change must go
into new versioned paths, ending in `manuscripts/ppm1k_bckdk_bckdh_v1.1.md` and
`submission/ppm1k_axis_v1.1/`. Never silently replace or rewrite v1.0.

## Read-first order

1. Read `README.md:1-54` for the repository-wide scientific boundary.
2. Read the complete manuscript at
   `manuscripts/ppm1k_bckdk_bckdh_v1.0.md:1-145`.
3. Read `submission/ppm1k_axis_v1.0/README.md:1-35` and verify its
   `manifest.tsv` before trusting the package.
4. Read all PPM1K, BCKDK, BCKDHA, and BCKDHB files under
   `results/target_audits/`.
5. Inspect the extraction logic at
   `scripts/extract_target_evidence.py:26-140` and its test before assessing
   the target-level results.
6. Inspect `results/dataset_audit.csv`, `results/modality_detected.csv`, and
   the upstream frozen matrices named in each target claim JSON.
7. Inspect both figures for biological direction, legibility, and compliance
   with the intended journal's generative-image policy.

## Non-negotiable scientific boundaries

Preserve these boundaries unless new, file-backed evidence directly overturns
them:

- No individual gene is genome-wide significant in the existing HMSR analysis;
  the repository states this explicitly at `README.md:8-14`.
- PPM1K, BCKDK, BCKDHA, and BCKDHB are all `NOT_REPLICATED` in the current
  target audit. The exact reported values appear at
  `manuscripts/ppm1k_bckdk_bckdh_v1.0.md:57-70`.
- The four subsets represent only two independent source groups, as described
  at `manuscripts/ppm1k_bckdk_bckdh_v1.0.md:39-43`.
- A transcript null cannot be presented as evidence of normal phosphorylation
  or normal BCAA flux. Conversely, post-translational plausibility cannot be
  presented as proof that a flux defect exists in sarcopenic human muscle.
- BCKDK phosphorylates and inhibits BCKDH; PPM1K dephosphorylates and activates
  BCKDH. Do not use the incorrect symbol `BCDK`.
- BT2 is a liability-bearing mechanistic reference, not the proposed drug
  candidate. The current rationale is at
  `manuscripts/ppm1k_bckdk_bckdh_v1.0.md:76-80`.
- Do not conflate dietary or circulating BCAA abundance with intramuscular BCAA
  disposal or isotope-resolved mitochondrial flux; see
  `manuscripts/ppm1k_bckdk_bckdh_v1.0.md:99-101`.
- Do not call the axis “validated,” “clinically validated,” “a treatment,” or
  “a new drug target” without replicated activity-level human evidence and
  functional causality.
- Negative or contradictory results must remain visible in the abstract,
  results, discussion, figures, and cover letter.

## Phase 1 — independent review of v1.0

Perform the review before editing any manuscript or analysis output. Create
`reviews/claude_scientific_review_v1.0.md` with the following structure.

### 1. Verdict

Use exactly one verdict:

- `READY_FOR_v1.1_ANALYSIS`: the baseline is internally sound and the next
  analysis can proceed.
- `BLOCKED_SCIENCE`: a central biological or literature claim is unsupported,
  reversed, or materially overstated.
- `BLOCKED_REPRODUCIBILITY`: a reported result cannot be traced to data and
  deterministic code.

The verdict applies to beginning the next revision. It is not a claim that the
manuscript is ready for journal acceptance.

### 2. Findings

Report findings as blocker, major, or minor. Each finding must include:

- exact `file:line` evidence;
- the claim or output at risk;
- why it matters scientifically;
- the smallest defensible correction;
- whether the correction changes the abstract, conclusion, figure, or target
  nomination.

Prioritize substantive issues over wording preferences. Do not edit v1.0 while
reviewing it.

### 3. Required scientific checks

Answer each question with `YES`, `NO`, or `UNCERTAIN`, followed by evidence.

1. Are all numerical values in Table 1 identical to the machine-readable claim
   JSON and replication TSV files?
2. Does the extractor correctly distinguish cohort subsets from independent
   source groups at `scripts/extract_target_evidence.py:66-81`?
3. Is `NOT_REPLICATED` applied consistently with the stated gate at
   `scripts/extract_target_evidence.py:124-135`?
4. Does any wording imply that the HMSR transcript audit validates the axis?
5. Is the reconciliation between RNA nulls and phosphorylation/flux biology
   framed as a hypothesis rather than observed human activity evidence?
6. Does each citation support the exact nearby statement, especially references
   2 and 4-8 at `manuscripts/ppm1k_bckdk_bckdh_v1.0.md:137-144`?
7. Are the direction and labels in both conceptual figures biologically correct?
8. Does the BT2 section adequately separate on-target BCKDK inhibition from
   uncoupling, albumin displacement, and tryptophan effects?
9. Is prioritizing this axis over MARCHF5 justified by the stated evidence, or
   should the language be narrowed to “more testable hypothesis”?
10. Is the current contribution sufficient for the declared article type, or
    would a journal reasonably classify it as a Perspective, Hypothesis,
    Resource Note, or Brief Report until new human multi-omic analyses are added?
11. Are the competing-interest, funding, AI-disclosure, ethics, and data/code
    statements internally consistent at
    `manuscripts/ppm1k_bckdk_bckdh_v1.0.md:115-133`?
12. Does the submission package contain every claimed file, and does every
    manifest hash and byte count match?

### 4. Novelty assessment

Separate novelty into four categories and grade each as high, moderate, low, or
absent:

- target novelty;
- human-disease evidence novelty;
- computational-analysis novelty;
- translational-framework novelty.

Explicitly compare the manuscript with the Zuo et al. 2025 study and subsequent
BCKDK/BT2 literature. The present manuscript must not claim discovery of the
axis if that literature already established it. Identify the precise claim that
could still be academically novel and state what additional result would make
that claim publishable.

### 5. Citation audit

Verify references against PubMed, Crossref, or the publisher record when
network access is available. Record title, authorship, journal, year, volume,
pages or article number, DOI, experimental system, and the exact claim supported.
Prefer primary papers. Do not invent a citation or infer an unavailable result
from an abstract. Mark inaccessible full-text-dependent claims as uncertain.

## Review gate

If the verdict is `BLOCKED_SCIENCE` or `BLOCKED_REPRODUCIBILITY`, stop manuscript
revision. Produce a bounded remediation plan in the review file, but do not
manufacture positive evidence or change the target to make the narrative work.

Proceed to Phase 2 only after a `READY_FOR_v1.1_ANALYSIS` verdict or after every
blocker is resolved with file-backed evidence.

## Phase 2 — inventory additional human multi-omic evidence

The next objective is not to search for a dataset that produces the desired
answer. It is to determine whether independent human evidence supports an
activity-level BCAA-catabolic endotype.

### 2.1 Local-first dataset discovery

Search the 4 TB resource read-only before downloading anything. Build
`results/ppm1k_axis_v1.1/human_dataset_inventory.tsv` with one row per dataset
and these required fields:

- accession and source;
- local absolute path;
- tissue and anatomical site;
- species;
- case definition and control definition;
- sample count by group;
- age, sex, BMI, muscle type, fasting status, exercise status, diabetes, renal
  disease, cancer, and medication availability;
- assay modality;
- raw, processed, or summary-level availability;
- whether PPM1K/BCKDK/BCKDH protein, p-BCKDHA Ser293, BCAA/BCKA metabolites, or
  isotope flux is directly measured;
- participant independence or overlap with another dataset;
- licence and redistribution constraints;
- inclusion decision and reason.

Do not count multiple omics layers or reprocessed subsets from the same
participants as independent human replication.

### 2.2 Evidence hierarchy

Prioritize datasets in this order:

1. Human skeletal-muscle phosphoproteomics containing BCKDHA Ser293.
2. Matched muscle proteomics plus BCAA/BCKA metabolomics.
3. Muscle metabolomics with clinical strength or performance phenotypes.
4. Proteomics containing PPM1K, BCKDK, BCKDHA, BCKDHB, DBT, and DLD.
5. Single-nucleus or single-cell muscle expression capable of resolving cell
   composition and myofibre states.
6. Independent bulk muscle transcriptomics.
7. Circulating metabolomics without muscle tissue, treated as contextual only.

If no activity-level human dataset exists, state that as a result. Do not use
additional transcript cohorts as a substitute for phosphorylation or flux.

### 2.3 Preregister the analysis contract

Before outcome inspection, create
`analysis/ppm1k_axis_v1.1/ANALYSIS_CONTRACT.md`. It must define:

- primary endpoint;
- primary contrast;
- independent replication unit;
- prespecified BCAA-catabolic gene/protein set;
- covariates and missing-data policy;
- participant-overlap handling;
- normalization and batch strategy;
- effect-size model and heterogeneity estimator;
- multiple-testing family;
- direction-consistency rule;
- exclusion and sensitivity analyses;
- success, inconclusive, contradiction, and failure thresholds.

The preferred primary activity endpoint is p-BCKDHA Ser293 divided by total
BCKDHA. If unavailable, downgrade the evidence tier rather than redefining a
post hoc primary endpoint.

## Phase 3 — computational analyses

Implement analysis only after the contract is frozen. Keep all derived work
under `analysis/ppm1k_axis_v1.1/` and `results/ppm1k_axis_v1.1/`.

### 3.1 Reproduce the existing negative audit

Regenerate the four target artifacts from the frozen source matrices using
`scripts/extract_target_evidence.py:45-140`. Confirm exact hashes and values.
Any difference from v1.0 is a blocker until explained.

### 3.2 Pathway-level human analysis

Evaluate the prespecified BCAA-catabolic module rather than selecting genes by
their observed case-control effects. At minimum consider BCAT2, BCKDHA, BCKDHB,
DBT, DLD, BCKDK, and PPM1K, with additions justified before testing.

For each eligible human dataset:

- report standardized effect sizes and uncertainty, not only p-values;
- preserve cohort-level results before meta-analysis;
- model age and sex where estimable and report missing covariates;
- test muscle-type and study-source heterogeneity;
- perform leave-one-independent-study-out sensitivity analysis;
- distinguish participant-level replication from technical confirmation;
- report null and directionally discordant results in full;
- assess whether any pathway score is driven by fibre-type or immune/stromal
  composition;
- do not infer enzymatic activity from RNA abundance alone.

### 3.3 Multi-omic triangulation

Where data permit, test the ordered chain:

`PPM1K/BCKDK balance → p-BCKDHA Ser293 → BCKDH flux proxy → BCAA/BCKA state → muscle function`

Each arrow requires its own association and uncertainty. A correlation at one
arrow does not validate the entire chain. Prefer within-participant matched
omics and clinical phenotype data. Record whether mediation or causal language
is justified; observational mediation alone is not proof of causality.

### 3.4 Endotype analysis

Only attempt endotype discovery if sample size and modality depth are adequate.
Define clusters without using the downstream treatment-response label. Evaluate
stability by resampling and replication in an independent participant group.
The clinically useful endotype should combine elevated p-BCKDHA, impaired
BCAA/BCKA handling, and muscle dysfunction; transcript-only clusters are
exploratory.

### 3.5 Robustness and negative controls

Include, when estimable:

- alternative normalization;
- study-source-aware meta-analysis;
- age-, sex-, BMI-, diabetes-, renal-function-, fasting-, and activity-sensitive
  analyses;
- exclusion of acute exercise or injury samples;
- fibre-composition sensitivity;
- leave-one-study-out analysis;
- negative-control mitochondrial pathways and proteins;
- participant-overlap audit;
- analysis with and without the original Zuo et al. cohorts.

## Phase 4 — experimental validation design

Create `validation/ppm1k_axis_v1.1/EXPERIMENTAL_PLAN.md`. The decisive experiment
should use primary or engineered human muscle from independent older sarcopenic
donors, age-matched non-sarcopenic donors, and young reference donors. Treat the
donor, not the well, as the biological replicate.

### Required perturbations

- PPM1K overexpression or CRISPR activation;
- BCKDK knockdown or CRISPR interference;
- rescue with perturbation-resistant wild-type constructs;
- mechanism-breaking controls where feasible;
- BT2 as a liability-bearing reference only;
- at least one chemically distinct, better-characterized BCKDK inhibitor;
- vehicle and non-targeting controls.

### Required endpoint chain

1. Direct target engagement or verified genetic perturbation.
2. p-BCKDHA Ser293/total BCKDHA response.
3. Stable-isotope BCAA or BCKA oxidation and downstream carbon tracing.
4. Mitochondrial respiration, reserve, membrane potential, and proton leak.
5. Contractile specific force and recovery after fatigue.
6. Viability and structural integrity.

Muscle size, a transcript change, or circulating BCAA lowering alone cannot
satisfy the efficacy gate.

### Required safety and selectivity counterscreens

- BCKDK genetic-dependence test;
- weak-acid uncoupling and proton-leak assessment;
- albumin displacement;
- plasma or medium tryptophan and kynurenine-pathway metabolites;
- insulin signalling and mTOR dynamics;
- autophagic flux;
- broad mitochondrial toxicity;
- exposure-response durability;
- scaffold-dependent changes in BCKDK protein abundance.

Predefine go/no-go thresholds, power assumptions, exclusion rules, blinded
analysis, randomization, and donor-level statistical models before experiments.

## Phase 5 — manuscript v1.1

Revise only claims supported by completed analyses. Create, do not overwrite:

- `manuscripts/ppm1k_bckdk_bckdh_v1.1.md`;
- `figures/ppm1k_axis_v1.1/`;
- `submission/ppm1k_axis_v1.1/`;
- `submission/ppm1k_axis_v1.1/manifest.tsv`.

### Required editorial decisions

- Select a journal and article type based on the actual novelty after Phase 3.
- If no new independent activity-level human result is obtained, position the
  work as an integrative analysis, Perspective, or Hypothesis rather than a
  definitive target-discovery research article.
- Preserve the transcript non-replication in the title or abstract.
- State whether the added datasets are genuinely participant-independent.
- Separate observed results, external results, inference, and proposed work.
- Keep BT2 outside the candidate claim.
- Update the abstract, tables, figures, limitations, cover letter, disclosures,
  data availability, and frozen manifest together.
- Do not add a DOI, clinical claim, ethics approval, funding source, or author
  contribution that was not actually obtained.

## Required deliverables

Claude's next-work pass is complete only when the applicable artifacts exist:

1. `reviews/claude_scientific_review_v1.0.md`
2. `results/ppm1k_axis_v1.1/human_dataset_inventory.tsv`
3. `analysis/ppm1k_axis_v1.1/ANALYSIS_CONTRACT.md`
4. Reproducible analysis code and tests under `analysis/ppm1k_axis_v1.1/`
5. File-backed result tables under `results/ppm1k_axis_v1.1/`
6. `validation/ppm1k_axis_v1.1/EXPERIMENTAL_PLAN.md`
7. `manuscripts/ppm1k_bckdk_bckdh_v1.1.md`, only if evidence warrants revision
8. `submission/ppm1k_axis_v1.1/`, only after all package checks pass
9. A concise decision log describing which claims strengthened, weakened, or
   remained unresolved

## Acceptance criteria

- Every quantitative manuscript claim maps to a committed table, JSON, or
  deterministic analysis output.
- Every added dataset has a documented inclusion decision and participant-
  independence assessment.
- No analysis changes its endpoint, gene set, or success threshold after
  inspecting the target result without an explicit deviation record.
- All four existing target audits reproduce exactly or discrepancies are
  resolved before manuscript editing.
- Individual-cohort effects, heterogeneity, and leave-one-study-out results are
  reported, including nulls and opposite directions.
- Transcript, protein, phosphorylation, metabolite, flux, and function evidence
  are labelled as different evidence tiers.
- A claim of human activity-level support requires direct phosphorylation,
  protein, metabolite, or flux data from clinically relevant muscle—not RNA
  plausibility alone.
- A therapeutic nomination requires genetic dependence, target engagement,
  functional rescue, and separation from mitochondrial and tryptophan-related
  liabilities.
- Figures agree with the manuscript and contain no unsupported quantitative
  impression.
- v1.0 remains byte-for-byte unchanged.
- The v1.1 manifest matches every packaged file's SHA-256 and byte count.
- The review and final handoff list exact commands run and exact observed
  results; unrun checks are labelled as gaps.

## Verification commands

Run only commands supported by the available local inputs, and record exact
output in the review or reproducibility receipt.

```bash
git status --short
git rev-parse --short HEAD
python3 -m pytest -q tests/test_extract_target_evidence.py
python3 scripts/verify.py
git diff --check
```

Before running `scripts/verify.py`, confirm that all expected large input files
and checksums are present. A skipped or input-blocked verifier is a reported gap,
not a pass. Add focused tests for every new parser, data transformation, model,
and claims-export step. Do not claim that a command passed unless its output was
actually observed.

## Data, security, and repository constraints

- Treat `/Volumes/4TB/exerciseomics/sarcopenia-multiomic-resource` as read-only.
- Do not edit or redistribute restricted participant-level data.
- Do not print credentials, tokens, prompts, or ambient environment values.
- Do not commit caches, virtual environments, raw protected data, or large
  regenerable matrices.
- Do not force-push, rewrite history, or delete frozen packages.
- Preserve unrelated user changes in a dirty worktree.
- Use a new branch for v1.1 work and make small, evidence-scoped commits.
- Do not download duplicates when an identical local file is present; compare
  checksums and provenance first.

## Stop conditions

Stop and report rather than forcing a positive narrative when:

- a central citation cannot support the stated biological direction;
- the existing audit cannot be reproduced from its named inputs;
- participant overlap prevents a valid independent-replication claim;
- no activity-level human dataset exists;
- the only apparent support comes from transcript-level post hoc selection;
- the result depends on one study and fails leave-one-study-out analysis;
- the compound effect persists after BCKDK loss or is explained by uncoupling or
  tryptophan displacement;
- a required local source is missing or has a checksum mismatch;
- an authorship, funding, ethics, data-use, or journal-policy decision requires
  the principal investigator.

Absence of activity-level human evidence does not invalidate the research
programme. It changes the correct deliverable from a target-validation claim to
a transparent gap analysis and prospective validation protocol.

## Final handoff format

End the Claude pass with:

1. the exact review verdict;
2. blocker/major/minor findings with `file:line` evidence;
3. the academically novel claim, if any;
4. a table of added human datasets and independence status;
5. a table of completed versus pending evidence gates;
6. exact verification commands and observed outputs;
7. changed and newly created files;
8. residual risks;
9. one recommendation: `SUBMIT_AS_INTEGRATIVE_ARTICLE`,
   `REVISE_WITH_NEW_HUMAN_ANALYSIS`, or `HOLD_FOR_ACTIVITY_VALIDATION`.

Do not end with “more research is needed” alone. State exactly which missing
measurement or analysis controls the next decision.
