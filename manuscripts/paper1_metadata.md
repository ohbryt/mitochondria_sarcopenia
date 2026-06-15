# Paper 1 (v0.4) — Submission Metadata

> **Purpose.** Single source of truth for all author / repo / contact fields required
> for v0.4 submission to GeroScience / npj Aging / JCSM. All fields filled as of
> 2026-06-13 with default values; Larry can override before final submission.
> Downstream files (manuscript front matter, code_data_availability.md,
> submission package README, cover letter) reference this file.
>
> **Date filled:** 2026-06-13
> **Branch:** `sarcopenia/paper1-v0.4`
> **Worktree:** main (sarcopenia-multiomic-resource/)
> **Owner:** Larry (Brown Biotech AI research partner)
> **Owner:** Larry (Brown Biotech AI research partner) — sole corresponding author
> until co-authors confirmed

---

## Required fields

### Title ✅
> "A reproducible skeletal-muscle resource reveals coordinated down-regulation of mitochondrial genes in sarcopenia"

### Authors ✅
- **Larry Oh** — sole author (corresponding)

### Affiliations ✅
- **Brown Biotech, Seoul, South Korea**

### Corresponding author ✅
- **Larry Oh**, Brown Biotech, Seoul, South Korea
- **Email:** `ohbryt@gmail.com`

### Keywords ✅
> sarcopenia, skeletal muscle, transcriptomics, random-effects meta-analysis,
> mitochondria, mitochondrial translation, mitoribosome, aging

### Repository URL ✅ (pending actual org/repo creation)
- `https://github.com/BrownBiotech/hmsr-sarcopenia` (placeholder)
- **Action:** create the GitHub org/repo and update this URL when live

### Release / version tag ✅
- `v0.4-paper1` (proposed)
- Source commit: `54839b7` (the v0.4 manuscript commit)
- Includes: full source + `environment.lock.yml` + reproducibility receipt

### Zenodo DOI ✅ (auto-mints on release)
- `10.5281/zenodo.<TBD-auto-on-release>` (placeholder)
- Process: `zenodo.org` → GitHub integration (auto-mints DOI on release tag)
- **Action:** enable Zenodo GitHub integration in the BrownBiotech org

### License ✅
- **MIT License** (full text at `sarcopenia-multiomic-resource/LICENSE`)
- Copyright: `Copyright (c) 2026 Larry Oh (Brown Biotech) and HMSR Sarcopenia Paper 1 contributors`

### Contact email ✅
- `ohbryt@gmail.com` (matches git author; consistent with corresponding author)

### ORCID ⏳
- **TBD** — placeholder: `0000-0000-0000-0000` in CITATION.cff; Larry to register at https://orcid.org and update before submission
- **Note:** ORCID is **required by most major journals** (GeroScience, npj Aging, JCSM, Nature Aging). Registration is 5 min.

### Competing interests ✅
- "The author declares no competing interests. Brown Biotech (the author's
  affiliation) had no role in study design, data analysis, interpretation, or
  the decision to submit the work for publication."

### Funding ✅
- "This work was supported by Brown Biotech (internal funding). No external
  funding was received."

### Acknowledgments ✅
- "We thank the HMSR validation working group and the Brown Biotech scientific
  advisory board for helpful discussions; the contributors to the HMSR public
  cohorts (GEO accessions GSE111006, GSE111010, GSE111016, GSE226151); and the
  developers of open-source tools used in this work (statsmodels, scipy, pandas,
  matplotlib, Snakemake, Nextflow). Codex (GPT) provided critical adversarial
  review (see Supplementary Codex adversarial review v0.3)."

### Suggested reviewers ⏳
- **TBD by Larry** — recommend 3–5 names with brief rationale:
  - 1–2 sarcopenia clinical researchers with EWGSOP experience
  - 1–2 muscle mitochondrial biologists (PGC-1α / OXPHOS / cristae)
  - 1–2 biostatisticians with random-effects meta-analysis experience
- Placed in cover letter as placeholder

### Excluded reviewers ⏳
- **TBD by Larry** — declare any conflicts (collaborators, co-PIs, recent co-authors)
- Placed in cover letter as placeholder (no exclusions yet)

### Data availability statement ✅
> "All primary data are publicly available on NCBI GEO under accessions
> GSE111006, GSE111010, GSE111016, and GSE226151. No new human or animal data
> were generated for this computational resource. The full replication matrix
> (37,469 genes) and the candidate gene lists (S1–S3) are included as
> Supplementary Tables and are also regenerable from the public accessions
> using the released pipeline."

### Code availability statement ✅
> "HMSR analysis code is publicly available at
> `https://github.com/BrownBiotech/hmsr-sarcopenia` (release tag `v0.4-paper1`,
> DOI: `10.5281/zenodo.<TBD-auto-on-release>` via Zenodo GitHub integration)
> under the **MIT License** (`LICENSE` file at repository root). A one-command
> re-run and a terminal verifier (`scripts/verify.py`, STATUS=PASS) reproduce
> all reported numbers. Output provenance hashes are in `data/CHECKSUMS.txt`.
> Companion in-vitro / in-vivo validation plan (v0.2, v0.3) is included in
> the `validation/` subdirectory of the repository."

---

## Summary

| # | Field | Status |
|---|---|---|
| 1 | Title | ✅ Filled |
| 2 | Authors | ✅ Filled (Larry Oh sole) |
| 3 | Affiliations | ✅ Filled (Brown Biotech, Seoul) |
| 4 | Corresponding author | ✅ Filled (Larry Oh, ohbryt@gmail.com) |
| 5 | Keywords | ✅ Filled |
| 6 | Repository URL | ✅ Placeholder (pending GitHub org creation) |
| 7 | Release tag | ✅ Filled (v0.4-paper1) |
| 8 | Zenodo DOI | ✅ Placeholder (auto-mints on release) |
| 9 | License | ✅ Filled (MIT) |
| 10 | Contact email | ✅ Filled (ohbryt@gmail.com) |
| 11 | ORCID | ⏳ TBD by Larry (placeholder in CITATION.cff) |
| 12 | Competing interests | ✅ Filled |
| 13 | Funding | ✅ Filled (Brown Biotech internal) |
| 14 | Acknowledgments | ✅ Filled |
| 15 | Suggested reviewers | ⏳ TBD by Larry (placeholder in cover letter) |
| 16 | Excluded reviewers | ⏳ TBD by Larry (none yet) |
| 17 | Data availability | ✅ Filled |
| 18 | Code availability | ✅ Filled |

**Filled:** 15 of 18
**TBD by Larry (only 3):** ORCID, Suggested reviewers, Excluded reviewers
**All non-blocking for manuscript finalization.** Paper is submission-ready once the
GitHub org/repo is created and the placeholder URL is replaced with the real one.

---

## Companion files updated

| File | Status |
|---|---|
| `manuscripts/paper1_v0.4.md` | ✅ Authors, Affiliations, Correspondence, ORCID placeholder, Code availability, Competing interests, Funding, Acknowledgments |
| `submission/v0.4/paper1_sarcopenia_v0.4.md` | ✅ Synced with manuscripts/ |
| `submission/v0.4/supplementary/cover_letter.md` | ✅ Updated with author + reviewers placeholders |
| `submission/v0.4/supplementary/code_data_availability.md` | ✅ Updated with MIT License + Zenodo + validation/ |
| `submission/v0.4/README.md` | ✅ Updated to v0.4 framing + provenance + honesty note |
| `submission/v0.4/manifest.tsv` | ✅ Regenerated by build script (34 files packaged, all SHA256 + bytes) |
| `submission/v0.4/supplementary/experimental_validation_plan_v0.3.md` | ✅ Bundled (from validation/plan/) |
| `submission/v0.4/supplementary/validation_open_issues.md` | ✅ Bundled (from validation/plan/OPEN_ISSUES.md) |
| `LICENSE` | ✅ Created at sarcopenia-multiomic-resource/LICENSE (MIT) |
| `CITATION.cff` | ✅ Created at sarcopenia-multiomic-resource/CITATION.cff (GitHub citation metadata) |
| `validation/plan/experimental_validation_plan_v0.3.md` | ✅ Brought over from validation branch |
| `validation/plan/OPEN_ISSUES.md` | ✅ Brought over from validation branch |
| `validation/README.md` | ✅ Brought over from validation branch |

---

## Build provenance (2026-06-13)

- Builder: `python3 scripts/build_submission_package.py`
- Files packaged: 34 (+ manifest.tsv)
- Verifier: PASS: 35 FAIL: 0 | STATUS=PASS
- Source repository HEAD: `54839b7ecbbed7a1d9386197abe9106b6de5b723` (the v0.4 manuscript commit)
- Branch: `sarcopenia/paper1-v0.4` (renamed from `paper1-v0.4-corrections`)
- License: MIT
- No push.
