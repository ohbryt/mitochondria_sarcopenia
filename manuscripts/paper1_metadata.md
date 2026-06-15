# Paper 1 (v0.4) — Submission Metadata

> **Purpose.** Single source of truth for all author / repo / contact fields required
> for v0.4 submission to GeroScience / npj Aging / JCSM. Larry fills in the TBD
> fields; downstream files (manuscript front matter, code_data_availability.md,
> submission package README, cover letter) reference this file.
>
> **Date:** 2026-06-13
> **Branch:** `sarcopenia/paper1-v0.4` (renamed from `paper1-v0.4-corrections` on 2026-06-13; the old name was a leftover from prior Eda2r/Hjv work)
> **Worktree:** main + `validation/aim2-causation`
> **Owner:** Larry (Brown Biotech AI research partner) — sole corresponding author
> until co-authors confirmed

---

## Required fields

### Title (proposed, pending approval)
**Current manuscript title (v0.4 §0):**
> "A reproducible skeletal-muscle resource reveals coordinated down-regulation of mitochondrial genes in sarcopenia"

**Note:** title is the journal-facing headline. The 22-word title is concise and
declarative. No change proposed. **TBD: confirm or revise.**

### Authors
**Current manuscript v0.4 §0:** `[Author list TBD]`
**Required:** full author list (Family name, Given name, ORCID iD)
**Order convention:** first author = lead analyst / computational lead; last
author = senior PI; middle authors = contributors in order of contribution

**Proposed (pending Larry's confirmation):**
- **Larry Oh** (sole author) — corresponding author; ORCID pending
- (Co-authors: TBD — HMSR collaboration members, Brown Biotech contributors)

**Action needed:** Larry to provide full author list + ORCID iDs.

### Affiliations
**Current manuscript v0.4 §0:** `[Affiliations TBD]`
**Required:** institutional affiliations with department, city, country for each author

**Proposed (pending Larry's confirmation):**
- **Brown Biotech** [city, country TBD]

**Action needed:** Larry to confirm institution details.

### Corresponding author
**Current manuscript v0.4 §0:** `[Corresponding author TBD]`
**Required:** name + email + postal address

**Proposed:** **Larry Oh** (Brown Biotech)
- **Email:** `ohbryt@gmail.com` (already used as git author)
- **Postal address:** TBD
- **Phone (optional):** TBD

**Action needed:** Larry to confirm + provide postal address.

### Keywords (current v0.4 §0)
> sarcopenia, skeletal muscle, transcriptomics, random-effects meta-analysis,
> mitochondria, mitochondrial translation, mitoribosome, aging

**No change proposed.** 8 keywords; most journals allow 5–10.

### Repository URL
**Current manuscript v0.4 §0 (Code availability):** `[HMSR repository URL TBD]`
**Current `submission/v0.4/supplementary/code_data_availability.md`:** no URL stated

**Proposed (TBD):**
- If pushing to GitHub: `https://github.com/<org>/hmsr-sarcopenia`
- If pushing to GitLab: `https://gitlab.com/<org>/hmsr-sarcopenia`
- If pushing to institutional: `https://<institution>.edu/~user/hmsr-sarcopenia`

**Action needed:** Larry to confirm hosting target + URL pattern.

### Release / version tag
**Proposed:** `v0.4-paper1` tag at commit `54839b7` (the v0.4 manuscript commit)
- Tag URL: `<repo>/releases/tag/v0.4-paper1`
- Includes: full source + `environment.lock.yml` + reproducibility receipt

**Action needed:** Larry to confirm tag name.

### Zenodo DOI
**Current:** not set
**Proposed:** mint after the v0.4-paper1 release is tagged
- Process: `zenodo.org` → GitHub integration (auto-mints DOI on release)
- DOI form: `10.5281/zenodo.<NNNNNNN>`
- Cited in: manuscript §Code availability, submission cover letter

**Action needed:** Larry to set up Zenodo GitHub integration and confirm auto-mint is enabled.

### License
**Status:** ✅ **MIT License** confirmed (2026-06-13)
- License file: `sarcopenia-multiomic-resource/LICENSE` (created today, full MIT text)
- Copyright: `Copyright (c) 2026 Larry Oh (Brown Biotech) and HMSR Sarcopenia Paper 1 contributors`
- Most permissive for academic re-use; maximizes re-use for the transcriptomic resource
- Will be cited in `submission/v0.4/supplementary/code_data_availability.md` and submission cover letter once the repo URL is set

### Contact email
**Current:** not set
**Proposed:** `ohbryt@gmail.com` (matches git author; consistent with corresponding author)

**No change proposed.** Larry to confirm or provide institutional email.

### ORCID
**Current:** not set
**Proposed:** Larry's ORCID iD (format: `0000-0000-0000-0000`)

**Action needed:** Larry to provide ORCID iD. If Larry doesn't have an ORCID yet,
register at https://orcid.org (5 min). ORCID is **required by most major journals**
(GeroScience, npj Aging, JCSM, Nature Aging).

### Competing interests
**Current:** not stated
**Proposed (default):** "The authors declare no competing interests."

**Action needed:** confirm; if Larry has a financial interest in Brown Biotech
(as the AI partner), this should be disclosed in the ICMJE form.

### Funding
**Current:** not stated
**Proposed:** "This work was supported by [TBD]." (or "No external funding.")

**Action needed:** Larry to provide funding source(s) or confirm "no external funding."

### Acknowledgments
**Current:** not stated
**Proposed:** "We thank the HMSR validation working group and the Brown Biotech
scientific advisory board for helpful discussions; the contributors to the
HMSR public cohorts (GEO accessions GSE111006, GSE111010, GSE111016, GSE226151);
and the developers of open-source tools used in this work (statsmodels, limma,
scipy, pandas, matplotlib, Snakemake, Nextflow)."

**Action needed:** Larry to confirm + add any specific acknowledgments.

### Suggested reviewers
**Current:** not set
**Proposed (suggest 3–5 names for journal submission):**
- TBD by Larry based on field knowledge. Suggestions might include: researchers
  in sarcopenia / mitochondrial biology / muscle aging / biostatistics.
- Most journals require suggested + excluded reviewers at submission.

**Action needed:** Larry to provide 3–5 names.

### Excluded reviewers
**Current:** not set
**Proposed:** Larry to provide any conflicts of interest (collaborators,
  co-PIs, recent co-authors).

**Action needed:** Larry to provide.

### Data availability statement
**Current (`submission/v0.4/supplementary/code_data_availability.md`):** "All
primary data are public on NCBI GEO: GSE111006, GSE111010, GSE111016, GSE226151."

**Proposed (manuscript §Data availability, expanded):**
> "All primary data are publicly available on NCBI GEO under accessions
> GSE111006, GSE111010, GSE111016, and GSE226151. No new human or animal data
> were generated for this computational resource. The full replication matrix
> (37,469 genes) and the candidate gene lists (S1–S3) are included as
> Supplementary Tables and are also regenerable from the public accessions
> using the released pipeline."

**Action needed:** no change — this is ready to paste into the manuscript.

### Code availability statement
**Current (v0.4 §Code availability):** `[HMSR repository URL TBD]`

**Proposed (expanded, to populate once repo URL is set):**
> "HMSR analysis code is publicly available at `<REPO_URL>` under the
> **MIT License**, release tag `v0.4-paper1` (DOI: 10.5281/zenodo.<NNNNNNN>).
> A one-command re-run and a terminal verifier (`scripts/verify.py`, STATUS=PASS)
> reproduce all reported numbers. Output provenance hashes are in
> `data/CHECKSUMS.txt`."

**Action needed:** once repo URL + Zenodo DOI are set, paste this statement into
v0.4 §Code availability.

---

## Summary of TBDs requiring Larry's input

| # | Field | Status | Action |
|---|---|---|---|
| 1 | Title | Proposed (v0.4 current) | Confirm or revise |
| 2 | Authors | TBD | Provide full list + ORCID iDs |
| 3 | Affiliations | TBD | Confirm Brown Biotech details |
| 4 | Corresponding author | Proposed (Larry Oh) | Confirm + provide postal address |
| 5 | Keywords | Set (v0.4 current) | No change |
| 6 | Repository URL | TBD | Confirm hosting target + URL pattern |
| 7 | Release tag | Proposed (`v0.4-paper1`) | Confirm tag name |
| 8 | Zenodo DOI | Not minted | Set up Zenodo integration + mint on release |
| 9 | License | ✅ **MIT** confirmed | Done 2026-06-13 |
| 10 | Contact email | Proposed (`ohbryt@gmail.com`) | Confirm or use institutional |
| 11 | ORCID | TBD | Provide or register |
| 12 | Competing interests | Proposed (none) | Confirm or disclose |
| 13 | Funding | TBD | Provide or confirm "no external funding" |
| 14 | Acknowledgments | Proposed | Confirm + add specifics |
| 15 | Suggested reviewers | TBD | Provide 3–5 names |
| 16 | Excluded reviewers | TBD | Provide conflicts of interest |
| 17 | Data availability | Ready | No change |
| 18 | Code availability | TBD (depends on #6, #8) | After #6 and #8 done, paste expanded statement |

**Critical path (must be done before submission):** Authors (#2), Affiliations (#3), Corresponding author postal (#4), Repository URL (#6), Zenodo DOI (#8), ORCID (#11).
**Non-blocking (can be done at proof stage):** Competing interests (#12), Funding (#13), Acknowledgments (#14), Suggested reviewers (#15), Excluded reviewers (#16).

---

## Companion files that reference this metadata

| File | Field references | Action after metadata is set |
|---|---|---|
| `manuscripts/paper1_v0.4.md` §0 | Authors, Affiliations, Correspondence | Edit front matter to fill TBDs |
| `manuscripts/paper1_v0.4.md` §Code availability | Repo URL, Zenodo DOI, License (MIT) | Expand the one-line `[HMSR repository URL TBD]` |
| `submission/v0.4/supplementary/code_data_availability.md` | Repo URL, Zenodo, License (MIT), Release tag | Add to the existing "Code" section |
| `submission/v0.4/cover_letter.md` (TBD) | Title, Authors, Highlights, Suggested reviewers | Draft + review |
| Submission package README | Repo URL, Release tag, DOI, License (MIT) | Add provenance block |
| `LICENSE` (new) | Copyright holder, year, license type | Created 2026-06-13 (MIT) |

---

## Decision checklist for Larry (one-shot)

1. **Confirm or revise** the proposed metadata above
2. **Provide the TBD values** (authors, affiliations, ORCID, postal address, repo URL, etc.)
3. **Approve the branch rename** `paper1-v0.4-corrections` → `sarcopenia/paper1-v0.4` ✅ **DONE 2026-06-13**
4. **Decide on the uncommitted Fig5 PDF** ✅ **DONE 2026-06-13 — reverted to HEAD (no real change)**
5. **Approve the license** (MIT) ✅ **DONE 2026-06-13 — LICENSE file created at `sarcopenia-multiomic-resource/LICENSE`**

**Remaining TBDs (12 of 18):** Authors, Affiliations, Corresponding author postal address, Repository URL, Release tag, Zenodo DOI, ORCID, Competing interests, Funding, Acknowledgments, Suggested reviewers, Excluded reviewers.

**Critical path (must be done before submission):** Authors, Affiliations, Corresponding author, Repository URL, Zenodo DOI, ORCID.
**Non-blocking (can be done at proof stage):** Competing interests, Funding, Acknowledgments, Suggested reviewers, Excluded reviewers.

Once the critical-path TBDs are decided, the paper is submission-ready.
