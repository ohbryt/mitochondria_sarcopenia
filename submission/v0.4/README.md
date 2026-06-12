# HMSR Sarcopenia Paper 1 — Submission Bundle (v0.2)

Self-contained submission bundle for the HMSR mitochondrial-sarcopenia manuscript.
**Distinct from** `submission/v0.4` in the parent repo, which is the separate
Eda2r/Hjv rat-exercise paper.

## Contents
- `paper1_sarcopenia_v0.2.md` — manuscript (OXPHOS→mitochondrial corrected; post-hoc
  gate disclosed; two-independent-studies framing; composition-robustness result).
- `figures/` — Figures 1–4 (PNG + PDF).
- `supplementary/` — Tables S1/S3/S4, main Tables 1–3, experimental validation plan,
  two internal critical reviews, modality/dataset audits, reproducibility receipt,
  cover letter, code/data availability.
- `manifest.tsv` — path, SHA256, byte size for every packaged file.

## Provenance
- Generated: `2026-06-12`
- Source repository HEAD: `54839b7ecbbed7a1d9386197abe9106b6de5b723`
- Builder: `python3 scripts/build_submission_package.py`
- Verifier: PASS: 35  FAIL: 0 | STATUS=PASS

## Honesty note
No gene survives genome-wide FDR; gene lists are exploratory candidates from a
disclosed post-hoc gate. The pathway-level mitochondrial finding is robust to
muscle-composition adjustment (Table S3/S4). See
`supplementary/internal_critical_review_v0.2.md`.
