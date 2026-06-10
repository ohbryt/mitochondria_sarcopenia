# Critical Review — HMSR Paper v0.1 & Pipeline

**Reviewer pass:** 2026-06-10 | **Verdict:** Publishable as a *resource* paper after major reframing. The current "7 replicated OXPHOS targets" framing will not survive top-tier review.

All findings below are computed (scripts in `scripts/`, data in `output/signatures/`), not asserted.

---

## CRITICAL (must fix before submission)

### C1 — Post-hoc gate redefinition (HARKing). **Highest priority.**
The replication gate was changed from `meta_fdr ≤ 0.10` to `meta_p < 0.005 + direction + LOCO + I²` **after** discovering that zero genes survive genome-wide FDR. The 195 genes "pass" a threshold defined *because* they couldn't pass the pre-specified one. A reviewer will hit this first.
- **Evidence:** genome-wide BH-FDR ≤ 0.10 → 0 genes. Switch to nominal p<0.005 → 195 genes.
- **Fix:** State explicitly that the gate is exploratory/post-hoc, not confirmatory. Frame the 195 as *candidates*, never as "validated" or "replicated." Pre-register the gate for a future cohort.

### C2 — The "OXPHOS signature" label is factually wrong.
Of the 7 headline genes, only **2 are true OXPHOS subunits** (NDUFB4 = Complex I; ATP5F1B = Complex V). The rest:
| Gene | Reality |
|------|---------|
| CHCHD10 | MICOS/cristae (intermembrane space) — not OXPHOS |
| APOO | MICOS (MIC26) — not a core OXPHOS subunit |
| MRPL33, MRPL34 | Mitoribosome — mt-translation, not OXPHOS |
| **CLTB** | **Clathrin light chain B — cytosolic vesicle coat, NOT mitochondrial at all** |
- CLTB is the #2 headline gene (meta-p 1.6×10⁻⁵) and is not a mitochondrial protein. Our own mito-pattern classifier (`scripts` check-5) excludes it.
- **Fix:** Retitle to "mitochondrial" not "OXPHOS." Remove CLTB from the mitochondrial cluster (discuss separately or drop). Re-do Figure/Table groupings by true functional class.

### C3 — "100% LOCO replication" is misleading; it is only a sign check.
`loco_details()` defines replication as **sign concordance** between the held-out cohort's β and the mean β of the rest — not a significance test. It is therefore near-redundant with `direction_consistency` (both measure "all 4 βs same sign"). Two of four gate criteria encode the same fact.
- **Fix:** Rename to "direction concordance," drop the redundant criterion, and never call it "replication."

### C4 — Per-gene signal rests on 2 of 4 cohorts.
Individual-cohort significance (p<0.05) for the 7 genes:
- **CHCHD10, CLTB: significant in only 1/4 cohorts** (SSS/GSE111016 only).
- Other 5: significant in 2/4 (always SSS + GESTALT).
- HSS (4 cases) and JSS (9 cases) are never significant for any of the 7.
- Leave out SSS **and** GESTALT (keep HSS+JSS) → all 7 non-significant (p = 0.09–0.45).
- **Caveat (fair to the authors):** HSS/JSS are underpowered (4 and 9 cases); directionally-consistent βs mean the effect is plausibly present but undetectable per-cohort. So this is a *power/independence* limitation, not a contradiction.
- **Fix:** State that adequately-powered signal comes from 2 balanced cohorts (SSS + GESTALT), of which only GESTALT is study-independent. Effective independent replication ≈ 1.

### C5 — "4 independent cohorts across 3 continents" oversells independence.
HSS, JSS, SSS are sub-series of one superseries (GSE111017): same lab, protocol, and processing pipeline. It is **2 independent studies** (GSE111017 family + GSE226151), one with 3 demographic strata.
- **Fix:** Reframe as "two independent studies (one with three demographic strata)."

---

## MAJOR

### M1 — Genome-wide signal is weak.
At meta-p<0.005: 328 observed vs 187 expected by chance = **1.75× enrichment** (implied FDR ≈ 57%). p<0.001: 99 vs 37 = 2.6×. There is real but modest signal; most p<0.005 genes are likely false positives. This is *why* nothing survives FDR and must be stated plainly.

### M2 — Mitochondrial enrichment is the real result — but don't over-claim the p-value.
26/195 gate genes match a mito gene-name pattern vs 2.7 expected (9.5×). Hypergeometric p ≈ 6.7×10⁻¹⁸ **but** mitochondrial genes are co-regulated (PGC-1α axis), violating the independence assumption — the true effective test count ≪ 195, so that p is badly inflated.
- **Fix:** Lead the biology with *coordinated mitochondrial down-regulation* (pathway-level, robust) rather than 7 gene-level "targets." Report enrichment with a co-expression caveat or via a competitive test (e.g., CAMERA/GSEA) that accounts for inter-gene correlation. This is the paper's defensible strength and is currently underplayed (no enrichment statistic appears in v0.1).

### M3 — HSS cohort has 4 cases.
OLS with 4 cases vs 28 controls is unstable; its β/SE still enters the meta. Report a sensitivity meta excluding HSS.

### M4 — Training/test role mixing.
GESTALT is labelled `frozen_training_candidate` and the GSE111 family `external_test_candidate`, yet all 4 are pooled in the discovery meta. Clarify there is no held-out validation; the resource is discovery-only.

---

## MINOR
- **m1** Sample-count discrepancy: inventory n (40/39/40/60) vs model-audit n (32/23/40/40) — the strict-binary subset. Document the filter explicitly.
- **m2** Effect sizes are small (β ≈ −0.16 to −0.28 on log2 CPM ≈ 11–18% reduction); state absolute fold-changes so readers calibrate.
- **m3** Abstract WP5 sentence already corrected (no OXPHOS gene overlaps the exercise ladder) — keep consistent everywhere.

---

## Recommended reframing (honest + still publishable)
> *A reproducible two-study skeletal-muscle resource showing **coordinated down-regulation of mitochondrial genes** (translation, cristae, and respiratory subunits) in sarcopenia. Signal is robust at the **pathway level** but **fragile at the gene level**, concentrated in the two balanced cohorts; gene-level candidates require prospective validation.*

Drop "7 replicated OXPHOS targets." Keep: the pipeline rigor, the transparent FDR-failure reporting, the pathway-level mitochondrial finding, and the experimental plan (which already addresses the gene-level fragility).

---
*All numbers from committed scripts; reviewer pass is advisory, not a data change.*
