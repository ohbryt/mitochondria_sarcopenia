# HMSR Sarcopenia Paper 1 — Reproducibility Receipt

**Generated:** 2026-06-10
**Source repository HEAD:** `00a60ae42f00ebed4dba9b68aee70a8a8f92ff0e`
**Verifier:** PASS: 30  FAIL: 0 | STATUS=PASS
**Environment:** `environment.yml` / `environment.lock.yml` (Python 3.14.4; numpy 1.26.4, pandas 2.3.3, scipy 1.17.1, statsmodels 0.14.6, scikit-learn 1.8.0)

## Code → claim map

| Script | SHA256 (16) | Role |
|---|---|---|
| `pipeline/recompute_disease_signatures.py` | `f26387429544ff5a` | WP3 DE + DL random-effects meta + gate |
| `pipeline/split_regulatory_exercise_evidence.py` | `dba28748f7eea0e5` | WP5 evidence split |
| `scripts/confound_sensitivity.py` | `30fe547f6fbae158` | WP3b composition + genomic-control sensitivity |
| `scripts/make_manuscript_figures.py` | `6e020c46539677c8` | Figures 1-4 + Tables 1-3 |
| `scripts/verify.py` | `db564bb30ea25380` | Terminal verifier gate |

## Re-run (one path)

```bash
conda env create -f environment.yml && conda activate hmsr-sarcopenia
python3 pipeline/recompute_disease_signatures.py     # WP3 + gate
python3 pipeline/split_regulatory_exercise_evidence.py  # WP5
python3 scripts/confound_sensitivity.py              # WP3b sensitivity
python3 scripts/make_manuscript_figures.py           # figures + tables
python3 scripts/verify.py                            # terminal gate (expect STATUS=PASS)
```

## Large regenerable inputs (not bundled; hashes in data/CHECKSUMS.txt)
- `output/signatures/replication_matrix.tsv` (37,469-gene DL meta matrix; Supplementary Table S2)
- `output/signatures/differential_by_cohort.tsv` (per-cohort OLS DE)

All reported numbers are produced by the committed scripts above; none are hand-computed.
