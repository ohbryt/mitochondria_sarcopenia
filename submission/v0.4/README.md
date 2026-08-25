# HMSR Sarcopenia Paper 1 — Submission Bundle (v0.4)

Self-contained submission bundle for the HMSR mitochondrial-sarcopenia manuscript.
**Distinct from** `submission/v0.4` in the parent repo, which is the separate
Eda2r/Hjv rat-exercise paper.

## Contents
- `paper1_sarcopenia_v0.4.md` — manuscript (v0.4: Codex MAJORs fixed; Table 1
  demographics corrected from real GEO metadata; Stouffer-vs-DL disambiguated;
  "replicated" → "candidate" in figures; Freedman–Lane + library-size
  sensitivity both confirm the mitochondrial result; bounded translational
  paragraph linking to the muscle-quality companion Perspective with HPGD
  transparency).
- `figures/` — Figures 1–5 (PNG + PDF). Figure 5 = pathway-level competitive
  shift (in-set minus out-set) for the mitochondrial programme + 6 sub-modules
  + non-mitochondrial controls, from a label-permutation test (N=2,000).
- `supplementary/` — Tables S1/S3/S4/S5/S5b/S6/S7/S8, main Tables 1–3,
  experimental validation plan v0.1 + v0.2 + v0.3 (operationalized), validation
  open-issues tracker, two internal critical reviews (v0.1, v0.2), Codex
  adversarial review v0.3, modality/dataset audits, reproducibility receipt,
  cover letter, code/data availability (updated to include MIT License + Zenodo
  DOI + validation/ deliverables).
- `manifest.tsv` — path, SHA256, byte size for every packaged file.

## Provenance
- Generated: `2026-06-13`
- Source repository HEAD: `677f1a7180c8b920fc9043866a3e8548ec34301e` (branch `sarcopenia/paper1-v0.4`)
- Builder: `python3 scripts/build_submission_package.py`
- Verifier: PASS: 35  FAIL: 0 | STATUS=PASS
- License: MIT (full text at `sarcopenia-multiomic-resource/LICENSE`)
- Repository: `https://github.com/ohbryt/mitochondria_sarcopenia` (release tag
  `v0.4-paper1`; archival DOI pending)

## Honesty note
No gene survives genome-wide FDR; gene lists are exploratory candidates from a
disclosed post-hoc gate. The pathway-level mitochondrial finding is robust to
muscle-composition adjustment (Table S3/S4), to Freedman–Lane covariate-
exchangeable permutation (Table S7), and to library-size covariate adjustment
(Table S8). See `supplementary/internal_critical_review_v0.2.md` and
`supplementary/codex_adversarial_review_v0.3.md`.
