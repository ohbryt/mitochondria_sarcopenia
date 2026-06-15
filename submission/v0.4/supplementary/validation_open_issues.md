# v0.3 Plan — Open Issues & TBD Tracking

> **Branch:** `validation/aim2-causation` (CRISPR/audit docs also on main)
> **Worktree:** `.worktrees/validation-aim2/`
> **Last updated:** 2026-06-15
> **Source:** `experimental_validation_plan_v0.3.md` §12

This file tracks all open issues, TBDs, and verification needs from the v0.3 plan
and its 6 companion deliverables. Each issue is tagged by severity
(🔴 blocking / 🟡 important / 🟢 nice-to-have) and assigned an owner.

---

## OI-1 🔴 Verify Guzman 2026 quantitative specific-force number
- **From:** `power_analysis/POWER_ANALYSIS.md` §1.3 + `plan/experimental_validation_plan_v0.3.md` §0, §5.1
- **Issue:** v0.2 plan used "15% specific-force reduction (CHCHD10-KO precedent, Guzman 2026, PMID 41496579)" but Guzman 2026 abstract only reports qualitative phenotypes (mito disorganisation, ↓ATP, NMJ fragmentation, delayed reinnervation). The 15% number is the v0.2 authors' working estimate, not a published value.
- **Action:** request full PDF from Aguilar lab (U. Michigan; corresponding author of Guzman 2026, Aging Cell 25(1):e70355, DOI 10.1111/acel.70355, PMID 41496579). Re-extract specific-force value from figure/table.
- **Impact:** determines n for Exp B (15% with SD 12% → n=11 @ 0.80; if 25% → n=5; if 10% → n=23).
- **Owner:** Larry + HMSR validation working group
- **Deadline:** before Exp B launch (target M4–M5)

## OI-2 ✅ RESOLVED 2026-06-15
- **Resolved in:** `validation/constructs/CRISPR_DESIGNS.md` (593 lines, 8 best + 16 reserve sgRNAs, full features)
- **Outcome:** 24 sgRNA candidates (3 per gene × species) extracted from **verified NCBI RefSeq mRNAs** (downloaded 2026-06-15). Doench Rule Set 2 + Hsu 2013 marked TBD with methodology (per user spec: 'Do NOT invent Doench/Hsu scores'). All 8 best sgRNAs selected.
- **Important RefSeq corrections made (vs CONSTRUCT_SPECS.md §0.3):**
  - mouse Chchd10: was NM_001136064.2 (which is actually **mouse Bscl2**, not Chchd10) → corrected to **NM_175329.4**
  - mouse Ndufb4: was NM_026610.3 (retired by NCBI) → corrected to **NM_026610.2**
- **PGC-1α design (verified):** 8 best sgRNAs all target shared 3' constitutive region (exon 8-13) of PPARGC1A — knocks down PGC-1α1/-2/-3/-b/-c/NT but spares PGC-1α4 (per user spec)
- **Remaining work for actual wet-lab synthesis:** run CRISPOR (or IDT design tool) on the verified mRNA sequences with the proposed sgRNA candidates to get the final Doench/Hsu scores + full-genome off-target counts; the 24 candidates provided are the "best" by heuristic, but the design tool may shuffle order slightly.

## OI-3 ✅ RESOLVED 2026-06-15
- **Resolved in:** `validation/constructs/OFF_TARGET_AUDIT.md` (429 lines, full methodology + 162-mRNA audit)
- **Outcome:** 24 sgRNAs (3 per gene × species) audited against 162 mitochondrial watch-list mRNAs (combined mouse + human) extracted from NCBI. **All 24 PASS**: 0 perfect 20-nt + NGG off-targets in the loaded watch list, 0 off-targets in the 1-3 mm range (in the loaded subset). 8 best sgRNAs all PASS the mito sub-audit.
- **Watch-list watch list corrections made (vs CONSTRUCT_SPECS.md §6.2):**
  - human CHCHD6: original accession invalid → corrected to **NM_001320610.2**
  - multiple other accessions corrected via fresh NCBI Entrez query
  - 162 of ~200 watch-list mRNAs successfully loaded; remaining flagged TBD for re-audit at CRO time
- **Remaining work:** full-genome Hsu 2013 mm0/mm1/mm2/mm3 off-target counts (TBD at design time via CRISPOR); siRNA-specific audit (TBD at vendor design tool output — methodology provided, worked example given)
- **Impact on construct acceptance:** the 8 best + 16 reserve sgRNAs are now defensible for vendor synthesis. The 0 off-targets in the loaded mito watch list is a strong first-pass safety check.

## OI-4 🟡 AAV9 in-house vs CRO decision
- **From:** `vendors/VENDOR_SHORTLIST.md` §3 + `plan/experimental_validation_plan_v0.3.md` §6.4
- **Issue:** AAV9 production options:
  - VectorBuilder ultra-purified research-grade: $3,099 (1 mL ≥10¹³), 4–6 weeks
  - Penn Vector Core: $2,470 internal / $2,964 external academic / $3,949 corporate, 6–10 weeks
  - In-house packaging: requires AAV9 packaging plasmid + HEK293T + cesium chloride or iodixanol gradient — ~$1,500 per construct but 2–3 weeks per batch once set up
- **Action:** receive quotes from VectorBuilder and Penn; decide based on (a) price, (b) lead time, (c) QC (full GMP vs research-grade). For Exp B (n=11–14 mice, 3 constructs = CHCHD10, ATP5F1B, scramble), 3 batches at VectorBuilder = ~$9,300; Penn = ~$9,000 external academic; in-house = ~$4,500.
- **Impact:** determines Exp B timeline + cost
- **Owner:** Larry + HMSR validation working group + finance
- **Deadline:** M1 (before AAV9 critical-path order)

## OI-5 🟡 iPSC model: CDI vs bit.bio decision
- **From:** `vendors/VENDOR_SHORTLIST.md` §1 + §7
- **Issue:**
  - FUJIFILM Cellular Dynamics (FCDI) iCell Skeletal Myocytes: ~$2,500–3,500/kit, 4–6 weeks, 1–2 × 10⁶ cells/vial
  - bit.bio ioSkeletal Myocytes (io1002): $1,198 / 2-vial pack, 1–2 weeks (in-stock), opti-ox deterministic reprogramming, mature in 10 days
- **Action:** receive quotes from both; consider lot-to-lot reproducibility (bit.bio's deterministic opti-ox is a major advantage) and timeline (4–6 weeks vs 1–2 weeks for first shipment).
- **Recommendation in v0.3:** bit.bio as primary, CDI as backup.
- **Impact:** determines Aim 3 (PGC-1α programme test in iPSC-derived myocytes) timeline + cost
- **Owner:** Larry + HMSR validation working group
- **Deadline:** M1 (before iPSC order)

## OI-6 🟡 Author list / affiliations / repo URL
- **From:** `paper1_v0.4.md` (still TBD per §Data availability, Code availability)
- **Issue:** HMSR Paper 1 v0.4 still has "[Author list TBD]", "[Affiliations TBD]", "[Corresponding author TBD]", "[HMSR repository URL TBD]". These need to be filled before any submission or grant application that uses v0.3 as appendix.
- **Action:** Larry to confirm author list (himself? co-authors? full HMSR collaboration?). Determine the HMSR repository URL once code is public. Determine corresponding author (likely Larry per his role as Brown Biotech PI).
- **Impact:** blocks Paper 1 submission; also blocks any v0.3 plan submission as grant appendix
- **Owner:** Larry
- **Deadline:** before Paper 1 submission (target within 1–2 weeks)

## OI-7 🟡 MTA for HSMM sarcopenic donor
- **From:** `vendors/VENDOR_SHORTLIST.md` §1, MTAs
- **Issue:** Lonza CellBio Services requires custom MTA + donor consent for sarcopenic-donor HSMM lots. MTA process takes 4–6 weeks on top of cell delivery.
- **Action:** begin MTA process now (M1). Lonza account manager contact: typically routed via Lonza US/Canada main line + custom-donor coordinator.
- **Impact:** blocks Aim 1 cohort protein validation
- **Owner:** Larry + institutional tech transfer office
- **Deadline:** M1 (begin now)

## OI-8 🟢 Sex expansion to Exp B
- **From:** `plan/experimental_validation_plan_v0.3.md` §5.2, §6.4
- **Issue:** v0.3 currently has Exp B all-male to match HMSR v0.4 cohort (all-male). Mixed-sex Exp B would have translational breadth but 1.5–2× animal cost. PGC-1α muscle cKO sex differences are reported (Halling 2019 used males; Handschin 2007 used males).
- **Action:** if budget allows (minimum-viable budget = $80–95K, recommended = $130–170K), expand Exp B to mixed sex with n=14/sex (28 total per group, 56 total). Otherwise keep all-male and flag mixed-sex replication for follow-up R01.
- **Impact:** determines Exp B sample size + cost
- **Owner:** Larry + HMSR validation working group
- **Deadline:** M3 (before Exp B launch)

## OI-9 🟢 AAV9-shRNA in-vivo injection SOP
- **From:** `plan/experimental_validation_plan_v0.3.md` §4.3
- **Issue:** SOP for in-vivo TA injection of AAV9-shRNA (contralateral scramble control) not yet written. Required for Exp B execution.
- **Action:** write SOP covering: animal prep (anesthesia, analgesia), TA intramuscular injection (50 µL per muscle, 1×10¹¹ vg/muscle), contralateral leg as scramble control, post-op monitoring, 8-week expression period before harvest, tissue collection (snap freeze + histology).
- **Impact:** blocks Exp B execution (M4–M5)
- **Owner:** Wet-lab collaborator
- **Deadline:** M3

## OI-10 🟢 Single-fibre permeabilized-fibre force SOP
- **From:** `plan/experimental_validation_plan_v0.3.md` §4.3
- **Issue:** SOP for permeabilized-fibre specific force (Aurora Scientific 300C-LR with skinned-fibre prep) not yet written. Required for Exp A/B in-vivo.
- **Action:** write SOP covering: fibre dissection, skinning protocol (5% Triton X-100 in relaxing solution), Ca²⁺-activated force at pCa 4.5, sarcomere length measurement by laser diffraction, fibre CSA measurement, specific force calculation.
- **Impact:** blocks Exp A/B execution (M4–M8)
- **Owner:** Wet-lab collaborator
- **Deadline:** M3

## OI-11 🟢 iPSC myocyte differentiation + CRISPR-KO SOP
- **From:** `plan/experimental_validation_plan_v0.3.md` §4.3
- **Issue:** SOP for iPSC myocyte differentiation + CRISPR-KO + KD validation not yet written. Required for Aim 3.
- **Action:** write SOP covering: iPSC maintenance (mTeSR1 or Essential 8), CRISPR-Cas9 RNP nucleofection (Lonza 4D-Nucleofector), clone picking + karyotype + off-target validation, myogenic differentiation (CDI or bit.bio protocol), baseline IF + Seahorse + myobundle force assays.
- **Impact:** blocks Aim 3 execution (M3–M6)
- **Owner:** Wet-lab collaborator
- **Deadline:** M3

## OI-12 🟢 Aged-mouse handling + tissue harvest SOP
- **From:** `plan/experimental_validation_plan_v0.3.md` §4.3
- **Issue:** SOP for aged-mouse (24-mo C57BL/6J) handling, terminal experiment procedures, tissue harvest (TA, gastrocnemius, soleus, EDL), and tissue processing (snap freeze, OCT embedding for histology, RNAlater for RNA) not yet written. Required for Exp A/B/D.
- **Action:** write SOP covering: IACUC protocol reference, animal handling, terminal experiment (isoflurane + cervical dislocation), tissue harvest within 5 min, tissue distribution (left TA = histology, right TA = RNA/protein, etc.), downstream processing protocols.
- **Impact:** blocks Exp A/B/D execution (M4–M14)
- **Owner:** Wet-lab collaborator
- **Deadline:** M3

---

## Summary

| Severity | Count | Status | Blocking v0.3 execution? |
|---|---|---|---|
| 🔴 Blocking | 1 | OI-1 (Guzman 2026 number) — STILL OPEN | Yes |
| 🔴 Resolved | 1 | OI-2 (CRISPOR sgRNA) — RESOLVED 2026-06-15 | No |
| 🟡 Important | 5 | OI-3 RESOLVED 2026-06-15; OI-4, OI-5, OI-6, OI-7 still open | Mostly |
| 🟢 Nice-to-have | 5 | OI-8 through OI-12 still open | No |

**Open blocking (1):** OI-1 Guzman 2026 specific-force number verification (email to Aguilar lab / U. Michigan)
**Open important (4):** OI-4 AAV9 in-house vs CRO; OI-5 iPSC model choice; OI-6 author/affiliation/repo URL (partially resolved via v0.4 housekeeping); OI-7 Lonza MTA
**Open nice-to-have (5):** OI-8 sex expansion; OI-9–OI-12 SOPs (planned M3)

**Closed (2):** OI-2 (CRISPOR sgRNA designs) ✅; OI-3 (BLAST off-target audit) ✅
**Partially closed (1):** OI-6 — author list / affiliations / ORCID / repo URL still need Larry's actual values; placeholder defaults filled in v0.4 housekeeping commit `a9fdbb6`.
