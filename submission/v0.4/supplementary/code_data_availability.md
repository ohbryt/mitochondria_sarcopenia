# Code & Data Availability

## Data
All primary data are public on NCBI GEO: GSE111006, GSE111010, GSE111016,
GSE226151. No new human/animal data were generated for the computational resource.

## Code
HMSR analysis code is provided in the repository (`pipeline/`, `scripts/`).
Environment pinned in `environment.yml` / `environment.lock.yml`. A one-command
re-run and a terminal verifier (`scripts/verify.py`, STATUS=PASS) reproduce all
reported numbers. Output provenance hashes are in `data/CHECKSUMS.txt`.

## Bundled supplementary tables
- Table S1: all 195 candidate genes with full meta-statistics.
- Table S2 (not bundled; regenerable): full 37,469-gene replication matrix.
- Table S3: composition-confound sensitivity (WP3b).
- Table S4: composition-adjusted mitochondrial enrichment per cohort.

## Scope / honesty statement
Gene-level findings are exploratory candidates (no genome-wide FDR survivor); the
pathway-level mitochondrial signal is robust to composition adjustment but a
non-composition technical factor in one cohort is not fully excluded without RIN/QC
metadata. See `internal_critical_review_v0.2.md` for the full self-audit.
