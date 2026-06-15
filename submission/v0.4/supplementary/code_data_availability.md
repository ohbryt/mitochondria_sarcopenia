# Code & Data Availability

## Data
All primary data are public on NCBI GEO: GSE111006, GSE111010, GSE111016,
GSE226151. No new human/animal data were generated for the computational resource.

## Code
HMSR analysis code is publicly available at
`https://github.com/BrownBiotech/hmsr-sarcopenia` (release tag `v0.4-paper1`,
DOI: `10.5281/zenodo.<TBD-auto-on-release>` via Zenodo GitHub integration) under
the **MIT License** (`LICENSE` file at repository root).

The code is provided in the repository under `pipeline/`, `scripts/`,
`validation/`. Environment pinned in `environment.yml` /
`environment.lock.yml`. A one-command re-run and a terminal verifier
(`scripts/verify.py`, STATUS=PASS) reproduce all reported numbers. Output
provenance hashes are in `data/CHECKSUMS.txt`.

The companion in-vitro / in-vivo validation plan (v0.2, v0.3) and its
operationalized deliverables (construct designs, antibody panel, Seahorse /
myobundle force SOPs, power analysis, vendor shortlist) are included in the
`validation/` subdirectory of the repository as supporting documentation and
are also bundled here as Supplementary files
(`experimental_validation_plan_v0.2.md`, `experimental_validation_plan_v0.3.md`,
`validation_open_issues.md`).

## Bundled supplementary tables
- Table S1: all 195 candidate genes with full meta-statistics.
- Table S2 (not bundled; regenerable): full 37,469-gene replication matrix.
- Table S3: composition-confound sensitivity (WP3b).
- Table S4: composition-adjusted mitochondrial enrichment per cohort.
- Table S5: gene-set permutation enrichment + descriptive AUC.
- Table S6: therapeutic-axis transparency projection (15-PGDH / PGE₂ / atrogene / myostatin / biogenesis).
- Table S7: Freedman–Lane covariate-exchangeable permutation enrichment.
- Table S8: library-size (sequencing-depth) covariate sensitivity.

## Scope / honesty statement
Gene-level findings are exploratory candidates (no genome-wide FDR survivor); the
pathway-level mitochondrial signal is robust to composition adjustment, to
Freedman–Lane permutation, and to library-size adjustment. A non-composition
technical factor in one cohort is not fully excluded without RIN/QC metadata.
See `internal_critical_review_v0.2.md` and the Codex adversarial review
`codex_adversarial_review_v0.3.md` for the full self-audit.
