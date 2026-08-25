# HMSR — Human Skeletal-Muscle Sarcopenia Multi-omic Resource

This repository contains the analysis code, frozen outputs, manuscript, and
validation package for a reproducible human skeletal-muscle sarcopenia study.
The primary analysis combines four strict case-control subsets using
cohort-specific models and random-effects meta-analysis.

## Scientific boundary

No individual gene survives genome-wide false-discovery-rate correction. Gene
lists are exploratory candidates. The reported mitochondrial signal is a
pathway-level result supported by muscle-composition, permutation, and
library-size sensitivity analyses; it is not evidence that a specific gene or
drug treats sarcopenia.

## Start here

- `submission/v0.4/paper1_sarcopenia_v0.4.md` — submission manuscript
- `submission/v0.4/README.md` — frozen submission-bundle inventory
- `submission/v0.4/manifest.tsv` — file hashes and sizes
- `results/modality_detected.csv` — structured modality audit
- `results/dataset_audit.csv` — dataset inclusion decisions
- `docs/MARCHF5_HUMAN_EVIDENCE.md` — reproducible negative target audit
- `manuscripts/ppm1k_bckdk_bckdh_v1.0.md` — integrative target-validation manuscript
- `submission/ppm1k_axis_v1.0/` — frozen manuscript, figures, and auditable target evidence
- `pipeline/` and `scripts/` — analysis and verification code
- `validation_bundle_v0.4/` — experimental-validation handoff

## Reproducibility

The package pins its environment in `environment.yml` and
`environment.lock.yml`. Large public input matrices and regenerable full result
matrices are not committed; their expected hashes and provenance are recorded
in `data/CHECKSUMS.txt` and the submission reproducibility receipt.

```bash
conda env create -f environment.yml
conda activate hmsr-sarcopenia
python3 pipeline/recompute_disease_signatures.py
python3 scripts/confound_sensitivity.py
python3 scripts/pathway_permutation.py
python3 scripts/sensitivity_freedman_libsize.py
python3 scripts/make_manuscript_figures.py
python3 scripts/verify.py
```

The pipeline expects the public cohort inputs described by the dataset audit.
Do not treat a verifier result as evidence unless those inputs and all checksum
targets are present.

## Citation and license

Citation metadata are in `CITATION.cff`. The project is released under the MIT
License. A permanent archive DOI should be added only after it has actually
been minted.
