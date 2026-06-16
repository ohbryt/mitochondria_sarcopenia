# WET_VALIDATION_PLAN.md
## HMSR Sarcopenia Project — Authoritative Wet-Lab Validation Plan v0.4
## From a mitochondrial-programme discovery to a function-level proof in sarcopenia

> **Document ID:** `sarcopenia-multiomic-resource/validation/WET_VALIDATION_PLAN.md`
> **Version:** v0.4 — 2026-06-16
> **Branch:** `sarcopenia/paper1-v0.4` (main worktree)
> **Prepared by:** Brown Biotech (Larry) — consolidation of v0.2 design + v0.3 operationalization
> **Status:** **Authoritative wet-lab plan.** Supersedes both `manuscripts/experimental_validation_plan_v0.2.md` (the design) and `validation/plan/experimental_validation_plan_v0.3.md` (the operationalized 5,263-line spec).
> **Companion documents:** `validation/HYPOTHESIS.md` (the falsifiable hypothesis), `validation/plan/OPEN_ISSUES.md` (open issues + decision history), and 7 deliverable docs in `validation/{constructs,antibodies,protocols,power_analysis,vendors}/`.

---

## §0 — Reading guide + How to use this document

### 0.1 What this document is

This is the **single, self-contained, authoritative wet-lab validation plan** for the HMSR sarcopenia project as of v0.4. A reviewer reading only this document should understand the entire wet-lab validation program — its hypothesis, models, sample sizes, decision gates, timeline, budget, risks, and publication strategy — without needing to open the discovery paper, the v0.2 design plan, or the v0.3 operationalized spec.

Where operational detail (per-gene siRNA catalog numbers, antibody RRIDs, sgRNA spacer sequences, vendor RFP templates) would add depth beyond the scope of a plan, this document cross-references the companion deliverables (§11) with **specific section anchors**.

### 0.2 What this document supersedes

| Document | Status |
|---|---|
| `manuscripts/experimental_validation_plan_v0.2.md` | **Superseded** by §1–§4 of this document; retained as design-history record. |
| `validation/plan/experimental_validation_plan_v0.3.md` | **Superseded** by §2–§8 of this document; retained as operational-history record. |
| `validation/README.md` | Still authoritative for project orientation + tier ranking. |
| `validation/HYPOTHESIS.md` | Companion (hypothesis specification — read alongside). |
| `validation/plan/OPEN_ISSUES.md` | Companion (open-issue + decision-history log — read alongside). |

### 0.3 Cross-reference map to companion docs

| Companion doc | Path | What you go there for |
|---|---|---|
| **HYPOTHESIS.md** | `validation/HYPOTHESIS.md` | Full falsifiable hypothesis with H0, H0.5, H1.1–H1.4, H2, H3 sub-hypotheses + falsification clauses |
| **OPEN_ISSUES.md** | `validation/plan/OPEN_ISSUES.md` | Live open-issue tracker (OI-1 Guzman 2026 number, OI-4 AAV9 CRO choice, etc.) |
| **CONSTRUCT_SPECS.md** | `validation/constructs/CONSTRUCT_SPECS.md` | siRNA + shRNA + sgRNA specs (4 genes × 2 species × 5 modalities); §4.3 = PGC-1α isoform decision |
| **CRISPR_DESIGNS.md** | `validation/constructs/CRISPR_DESIGNS.md` | Top-3 sgRNAs per gene × species with mRNA coordinates; §0.2 = RefSeq corrections |
| **OFF_TARGET_AUDIT.md** | `validation/constructs/OFF_TARGET_AUDIT.md` | 162-mRNA mitochondrial watch-list audit; §3 = methodology |
| **ANTIBODY_PANEL.md** | `validation/antibodies/ANTIBODY_PANEL.md` | 41-Ab tier-aligned panel; §6 = top 5 must-order Abs |
| **POWER_ANALYSIS.md** | `validation/power_analysis/POWER_ANALYSIS.md` | Per-experiment n; §2 = per-experiment sample size table; §5 = sensitivity grid |
| **SEAHORSE_MITO_STRESS_TEST_SOP.md** | `validation/protocols/SEAHORSE_MITO_STRESS_TEST_SOP.md` | Seahorse XF SOP; §4.3 = FCCP titration; §6 = normalization; §11 = day-of checklist |
| **MYOBUNDLE_SPECIFIC_FORCE_SOP.md** | `validation/protocols/MYOBUNDLE_SPECIFIC_FORCE_SOP.md` | 3D myobundle force SOP; §3 = 3D model; §4 = matched-CSA design |
| **VENDOR_SHORTLIST.md** | `validation/vendors/VENDOR_SHORTLIST.md` | 1,135-line vendor/CRO shortlist; §3 = AAV9; §11 = decision summary; §12 = RFP templates |

### 0.4 What changed from v0.2 → v0.3 → v0.4 (10 corrections)

| # | Change | v0.2 (was) | v0.4 (now) | Source / rationale |
|---|---|---|---|---|
| 1 | Guzman 2026 effect size | 15% specific-force reduction (working estimate from CHCHD10-KO precedent) | **20% conservatively assumed** until full PDF extracted (abstract is qualitative only — see OI-1) | `POWER_ANALYSIS.md` §1.3, §5.1; OI-1 in `OPEN_ISSUES.md` |
| 2 | PGC-1α muscle-KO citation | Ruas 2012 PMID 22977227 (incorrect — 22977227 is Shah 2012 *Eur Heart J* lipid genetics paper) | **Handschin 2007 PMID 17702743** (verified — the original *J Biol Chem* muscle-specific PGC-1α KO paper) | Verified via PubMed; `POWER_ANALYSIS.md` §8 |
| 3 | Exp B sample size | n=10/group | **n=14/group @ 0.90 power** (recommended) or **n=11 @ 0.80** (minimum-viable) | `POWER_ANALYSIS.md` §0, §2.2, §5.1, §5.2 |
| 4 | Non-targeting sgRNA control | Addgene #80263 (unverified at issue time) | **Addgene #50946** (verified Yusa/Koike-Yusa 2014, PMID 24535568) — pKLV-U6gRNA(BbsI)-PGKpuro2ABFP | `CONSTRUCT_SPECS.md` §5.3 |
| 5 | Vector Biolabs Ad-PGC-1α | #1047 (older/withdrawn catalog) | **ADV-280991 (mouse)** + **ADV-219511 (human)** — current 2026 catalog | `CONSTRUCT_SPECS.md` §4.5 |
| 6 | Mouse *Chchd10* RefSeq | NM_001136064.2 (which is actually mouse *Bscl2*) | **NM_175329.4** (verified via NCBI Entrez 2026-06-15) | `CRISPR_DESIGNS.md` §0.2 |
| 7 | Mouse *Ndufb4* RefSeq | NM_026610.3 (retired by NCBI) | **NM_026610.2** (current version) | `CRISPR_DESIGNS.md` §0.2 |
| 8 | PGC-1α targeting strategy | Pan-PGC-1α | **Target PGC-1α1 only** (exon 8 of canonical NM_013261.5 / NM_008904.3 — shared by PGC-1α1/-2/-3/-b/-c/NT, NOT PGC-1α4); validate isoform selectivity with 3 isoform-specific qPCR assays | `CONSTRUCT_SPECS.md` §4.3; `CRISPR_DESIGNS.md` §4.2 |
| 9 | Budget | $120–160K (under-scoped; omitted personnel + complete vendor breakdown) | **$220–293K full program** (itemised) **OR $80–95K minimum-viable** (Aim 2 PoC + Exp B at n=11) | `VENDOR_SHORTLIST.md` §9–10; this document §7 |
| 10 | Seahorse Δ% (Aim 2 OCR) | 15% | **22–25%** (Cohen's d ≈ 1.5, large effect, defensible from Guzman 2026 + Halling 2019 + Palla 2020) | `POWER_ANALYSIS.md` §1.1 |

**Additional sex-design clarification (carried from v0.3):** Exp B stays **all-male** to match the HMSR v0.4 discovery cohort (halves animal cost; the cohort is male-dominated). Mixed-sex replication is flagged as a follow-up R01 deliverable.

**Additional citation correction (v0.4):** The CRISPR off-target reference **Hsu 2013** was cited in v0.3 as PMID 23775266; verification via PubMed shows **PMID 23775266 is unrelated** (Mormile & Vittori 2013 *Arch Gynecol Obstet* on celiac disease/endometriosis). The correct citation is **PMID 23873081** (Hsu PD, Scott DA, Weinstein JA *et al.*, *Nat Biotechnol* 2013 31(9):827–832, DOI [10.1038/nbt.2647](https://doi.org/10.1038/nbt.2647)). v0.4 uses the corrected PMID throughout.

### 0.5 30-second TL;DR

**What we are testing.** The HMSR v0.4 discovery (paper1_v0.4.md) established that the nuclear-encoded mitochondrial biogenesis programme is coordinately down-regulated at the transcript level in sarcopenic human muscle (correlation-aware permutation p = 2.0×10⁻³, all 6 sub-programmes concordantly down, robust to 3 confound controls). H1 is the next step: does suppressing this programme **cause** loss of muscle *quality* (specific force at matched cross-sectional area, CSA), not just mass?

**How we are testing it.** Four in-vitro aims + four in-vivo experiments. The decisive readout is **specific force at matched CSA** (the muscle-quality endpoint) plus Seahorse mitochondrial respiration. Tier-1 lead is **CHCHD10** (MICOS/cristae); Tier-2 are **NDUFB4** (Complex I) and **ATP5F1B** (Complex V); master switch is **PGC-1α1** (PPARGC1A canonical). Models are **C2C12 + HSMM + iPSC-derived myocytes** (in vitro) and **3-mo + 24-mo C57BL/6J** (in vivo). The therapeutic arm (Exp D) tests mass-matched PGC-1α induction vs 15-PGDH inhibition (SW033291; Palla 2020 *Science* anchor) vs anabolic comparator.

**When.** 14 months end-to-end. M1 = AAV9 + aged-mouse + iPSC orders placed (long-lead critical path). M2–6 = Aim 2 in-vitro PoC. M4–8 = Exp A + B. M5–8 = Aim 3 + Exp C. M8–14 = Exp D. M14 = data freeze + Paper 2 + Paper 3 drafts.

**Who.** Brown Biotech (Larry) as PI + 1 wet-lab postdoc (50% FTE) + university muscle-physiology core (Aurora 1300A) + university Seahorse core (XFe96) + 1 CRO (myobundle force, ProCytech or equivalent) + 1 CRO (iPSC-CRISPR, bit.bio + Cellectics or Crown Bio).

**For how much.** **$220–293K** for the full program (v0.4 itemised, includes personnel) **OR $80–95K minimum-viable** (Aim 2 PoC + Exp B at n=11/group + university cores).

*What §0 tells you:* this is the authoritative wet-lab plan v0.4, self-contained, with 10 explicit corrections to v0.2/v0.3 and a clear cross-reference map to companion docs.

---

## §1 — Central hypothesis and rationale

### 1.1 H0 (established) — the discovery

In sarcopenic human muscle, the nuclear-encoded **mitochondrial biogenesis programme** (mitoribosome, cristae/MICOS, import, respiratory chain I/II–III–IV/V) is **coordinately and specifically down-regulated** at the transcript level. Established by the HMSR v0.4 meta-analysis (n=135 strict case/control across 2 independent studies, 37,469 genes tested):

- Correlation-aware label-permutation test on the full ranked genome: **p = 2.0×10⁻³** for the 539-gene nuclear-encoded mitochondrial programme.
- All **6 sub-programmes** concordantly down at p ≤ 6×10⁻³ (Complex I, II/III/IV, V, mitoribosome, cristae/MICOS, import).
- **Non-mitochondrial controls are not significantly shifted**: cytoplasmic ribosome p = 0.28; proteasome p = 0.12.
- Robust to **muscle composition adjustment** (stromal/immune purity proxy): mitochondrial enrichment retained 26×; 4/7 highlighted genes remain meta-p < 0.005.
- Robust to **Freedman–Lane covariate-exchangeable permutation**: p = 1.0×10⁻³.
- Robust to **library-size (sequencing depth) covariate** adjustment: 4/7 genes remain meta-p < 0.005.
- **Honest ceiling:** no gene survives genome-wide BH-FDR; the result is pathway-level, not individual-gene.

**Top-tier candidate genes (from random-effects meta-analysis):**

| Tier | Gene | β (RE meta) | p (meta) | FDR (BH) | I² | Function |
|---|---|---|---|---|---|---|
| **1 (lead)** | **CHCHD10** | −0.164 | 7.5×10⁻⁶ | 0.255 | **0%** | MICOS / cristae (IMS) |
| 2 | **NDUFB4** | −0.190 | 3.1×10⁻³ | 0.534 | 47% | Complex I accessory (B15) |
| 2 | **ATP5F1B** | −0.221 | 3.5×10⁻³ | 0.544 | 39% | Complex V (ATP synthase) F₁β |
| 3 | MRPL34 | — | — | — | — | Mitoribosome large subunit |
| 3 | MRPL33 | — | — | — | — | Mitoribosome large subunit |
| 3 | APOO/MIC26 | — | — | — | — | MICOS complex |
| master | **PPARGC1A (PGC-1α1)** | — | — | — | — | Biogenesis master TF |

### 1.2 H1 (causation — the decisive aim)

**Suppressing the mitochondrial biogenesis programme — or its strongest individual nodes — lowers mitochondrial respiration and specific force (force per CSA) without necessarily lowering muscle mass.**

This is the **muscle-quality reframe**. Sarcopenia drug development has historically targeted **mass** (anabolic agents, myostatin antagonists, growth hormone) with mixed efficacy. The companion muscle-quality Perspective argues the field has been optimizing the wrong variable: muscle mass is a poor surrogate for the innervated, metabolically competent, force-producing fraction of muscle.

**The critical design principle:** the decisive readout throughout this plan is **muscle quality = function per unit size**, not bulk. A manipulation that reduces specific force or respiration at **matched CSA** proves the programme is a *quality* driver. This mass-vs-quality dissociation is what separates a confirmatory mitochondrial study from a mechanistic one, and is the **scientific spine** of v0.4.

**Sub-hypotheses tested (per `validation/HYPOTHESIS.md` §2, §3, §4, §5):**

| ID | Sub-hypothesis | Decisive test |
|---|---|---|
| **H0.5** | Programme down at protein level (not just transcript) | Aim 1 cohort protein panel (n≥10/group) |
| **H1.1** | CHCHD10 KD lowers specific force + respiration at matched CSA | Aim 2 C2C12 + HSMM siRNA → Seahorse + myobundle force at matched CSA |
| **H1.2** | NDUFB4 KD lowers specific force + respiration at matched CSA | Same as H1.1 |
| **H1.3** | ATP5F1B KD lowers specific force + respiration at matched CSA | Same as H1.1 |
| **H1.4** | PGC-1α1 KD reproduces the entire programme down-regulation | Aim 3 RNA-seq + pathway-level permutation test |
| **H2** | Exercise rescues the programme **and** specific force in aged mice | Exp C (sedentary vs wheel vs treadmill) |
| **H3** | Therapeutic restoration delivers function at equal/lesser mass gain | Exp D (mito-restoration vs anabolic vs vehicle, mass-matched) |

Each sub-hypothesis has a **pre-specified falsification clause** (see HYPOTHESIS.md §2–§5). The strongest version of the muscle-quality thesis predicts H0.5, H1.1–H1.4, H2, and H3 are all confirmed in the same project — this is the **Nature Aging / Cell Metabolism-tier compound result**.

### 1.3 Why this plan matters

| Stake | If H1 + H2 + H3 confirmed | If any of H1–H3 refuted |
|---|---|---|
| **Scientific** | First human-data-anchored mechanistic test of the muscle-quality pillar (metabolic competence). Top-tier discovery paper. | Honest re-framing: the programme is a correlate, not a driver. Publishable as a hypothesis-correcting null with mechanistic insight. |
| **Therapeutic** | Nominates 15-PGDH-i (SW033291; Palla 2020) and PGC-1α induction as routes to function-restoring sarcopenia drugs. | Drug development should refocus on mass-side levers or other quality pillars (NMJ, ECM). |
| **Translational** | Direct support for a muscle-quality-based drug approval endpoint (specific force at preserved mass) rather than mass-only endpoints (which have under-delivered clinically). | The muscle-quality reframe loses its transcriptomic-to-causal link; other pillars (NMJ, ECM, satellite cell) need to be tested. |

### 1.4 What this plan does NOT claim

This plan inherits HYPOTHESIS.md §7's bounded claims. It does **not** claim that the mitochondrial programme down-regulation *causes* clinical sarcopenia; that a single gene (e.g., CHCHD10) is *the* cause; that restoring the programme is sufficient to reverse clinical sarcopenia (Exp D tests a single intervention in aged mice — clinical translation requires a human trial); or that this is the only muscle-quality pillar (the Perspective names three: metabolic competence — this work, NMJ integrity, ECM/fibrosis balance — only the first is tested here).

*What §1 tells you:* H0 is established (the discovery, paper1_v0.4.md, p=2.0×10⁻³ permutation). H1 (causation at matched CSA) is what this wet-lab plan tests. The mass-vs-quality dissociation is the scientific spine.

---

## §2 — In vitro program (Aims 1–4)

### 2.0 In-vitro overview

| Aim | Question | Primary readout | Decisive gate | Models | Months | Cost (USD) |
|---|---|---|---|---|---|---|
| **Aim 1** | Is the programme down at **protein** in independent cohort? (closes gap iii of v0.2) | Mitochondrial protein panel (immunoblot + targeted proteomics) on n≥10 sarcopenic vs n≥10 control biopsies | Programme down at protein in ≥1 independent cohort (`HYPOTHESIS.md` H0.5 falsification clause) | HSMM (Lonza CC-2580) sarcopenic + control donors; or independent biopsy cohort | M2–M12 | $25–35K |
| **Aim 2** | Does losing the programme impair **function** at matched CSA? (the central causation aim) | Seahorse Mito Stress Test OCR + 3D myobundle specific force at matched CSA | ≥1 Tier-1/2 KD reduces OCR ≥20% **at matched CSA** (HYPOTHESIS.md H1 falsification) | C2C12 myotubes + HSMM myotubes/myobundles + iPSC-derived myocytes (bit.bio ioSkeletal) | M2–M9 | $40–60K |
| **Aim 3** | Is it a coordinated *programme*? PGC-1α master test + rescue | PGC-1α1 KD RNA-seq + pathway-permutation test vs HMSR v0.4 signature; Ad-PGC-1α rescue of CHCHD10-KD | PGC-1α1 KD reproduces all 6 sub-programmes concordantly down (H1.4 falsification) | C2C12 + HSMM + iPSC isogenic | M3–M9 | $15–25K |
| **Aim 4** | Is CLTB a real mitochondrial hit? (separate, hypothesis-generating) | CHCHD10/CLTB co-IP; mt-Keima mitophagy flux | Hypothesis-generating only; not on the critical path | C2C12 + HSMM | M9–M11 (if Aim 2 has slack) | $5–8K |

**Common models, sourcing, and authentication (cross-ref `VENDOR_SHORTLIST.md` §1):**

| Cell line | Source | Catalog | Authentication required |
|---|---|---|---|
| **C2C12** (mouse myoblast) | ATCC | **CRL-1772** (Yaffe & Saxel 1977) | ATCC-authenticated by isoenzymes + STR; mycoplasma re-test every 4 weeks; passage ≤15 |
| **HSMM** (primary human myoblast — control donors) | Lonza Clonetics | **CC-2580** (≥500K cells, P2) | Lonza CoA (mycoplasma, sterility, viral panel, isoenzyme, ≥10 PD guarantee) |
| **HSMM** (sarcopenic donor — custom for Aim 1) | Lonza CellBio Services | Custom | **MTA required** (4–6 weeks lead time on top of cell delivery); donor DXA-confirmed sarcopenia per EWGSOP2 (ALM/height² < 7.26 kg/m² men, < 5.45 kg/m² women); see OI-7 |
| **iPSC-derived skeletal myocyte** (WT) | **bit.bio ioSkeletal Myocytes** (io1002) | $1,198 / 2-vial pack; opti-ox deterministic reprogramming; mature striated myocytes by Day 10 post-thaw | bit.bio CoA + in-house IF (desmin + MyHC + α-actinin) |
| **iPSC-derived myocyte** (CHCHD10 + ATP5F1B isogenic KO — for Aim 2/3) | Cellectics or Crown Bio (custom CRISPR edit + QC) | Custom | Karyotype (G-band or SNP array), off-target (GUIDE-seq), Sanger of edited locus, myogenic differentiation, Seahorse baseline |
| **HEK293T** (lentivirus packaging) | ATCC | **CRL-3216** | Mycoplasma + STR |

**Common transfection / delivery reagents (cross-ref `CONSTRUCT_SPECS.md` §7.2):**
- siRNA transfection: **Lipofectamine RNAiMAX** (Thermo 13778075), reverse-transfection at 50 nM
- Plasmid + co-transfection: **Lipofectamine 3000** (Thermo L3000015)
- Lentivirus transduction: **8 µg/mL polybrene** (Sigma H9268); puromycin selection 1–2 µg/mL (C2C12) or 0.5–1 µg/mL (HSMM)
- RNP nucleofection (CRISPR): **Lonza 4D-Nucleofector** with **P3 Primary Cell Kit** (V4XP-3032), program CM-138 (C2C12) or DS-150 (HSMM); 250 pmol Cas9 V3 + 250 pmol sgRNA per 100 µL cuvette, 1×10⁶ cells

**Common controls (mandatory in every Aim 2/3 experiment, cross-ref `CONSTRUCT_SPECS.md` §5.3):**
- siRNA scramble: **Horizon ON-TARGETplus Non-Targeting Pool D-001810-10-05**
- shRNA scramble: **Horizon MISSION SHC002** (or SHC202 with copGFP)
- sgRNA scramble: cloned into **Addgene #50946** (pKLV-U6gRNA(BbsI)-PGKpuro2ABFP, verified Yusa/Koike-Yusa 2014); v0.2 erroneously cited #80263 — corrected (see §0.4 correction #4)
- Loading WB: **Vinculin** (CST 13901, primary) or **β-tubulin** (CST 2128, alternate)
- Mito-mass normalization (WB + IF): **Citrate synthase** (Proteintech 16131-1-AP) + **HSP60** (CST 12165)

### 2.1 Aim 1 — Confirm the discovery beyond transcript (H0.5)

**Purpose.** Determine whether the v0.4 transcript-level finding holds at the **protein level** in an independent sarcopenic vs control cohort. If the protein panel is unchanged, the discovery is transcript-only — biologically interesting but mechanistically lower-priority as a therapeutic target (HYPOTHESIS.md §3 falsification clause).

**Models.**
- **Primary:** human muscle biopsies (vastus lateralis) from sarcopenic (n≥10, EWGSOP2-defined) vs control (n≥10, age-matched, no sarcopenia) donors. Sourced via custom Lonza CellBio Services or institutional muscle biopsy bank (requires MTA, 4–6 weeks lead time — see OI-7).
- **Secondary:** primary HSMM from sarcopenic vs control donors (Lonza CC-2580 custom-donor lots), differentiated to d7–d10 myotubes for in-vitro validation.

**End points.**

| Endpoint | Method | Acceptance criterion |
|---|---|---|
| **Primary:** Mitochondrial protein panel (immunoblot) | Western blot, 14-Ab lean core: CHCHD10, NDUFB4, ATP5F1B, MRPL34, MRPL33, APOO, NDUFA9, ATP5A1, PGC-1α (D5K9D, CST 2178), TFAM (D5C8, CST 8076), Citrate synthase, HSP60, Vinculin, β-tubulin (`ANTIBODY_PANEL.md` §1.1, §1.2, §5) | Log₂ FC ≈ −0.5 to −1.0 (30–50% reduction) in sarcopenic vs control; BH-FDR < 0.10 across the 6-protein primary panel |
| **Primary (alternative):** Targeted proteomics (PRM-MS) | LC-MS/MS parallel reaction monitoring, 50-protein OXPHOS + biogenesis panel (`VENDOR_SHORTLIST.md` §8.4) | Same effect-size criterion; 1 LC-MS/MS run per donor; ~$300/donor |
| **Secondary:** Respiration in primary HSMM | Seahorse XFe96 Mito Stress Test (SOP: `SEAHORSE_MITO_STRESS_TEST_SOP.md`) | OCR in sarcopenic donors lower than control at matched cell number/protein |
| **Secondary:** mtDNA copy number | qPCR (MT-ND1 or 16S rRNA normalized to nuclear β2M / B2M) | ≥20% reduction in sarcopenic |
| **Secondary:** PGC-1α + TFAM mRNA | RT-qPCR with isoform-specific primers for PGC-1α1 vs PGC-1α4 | ≥30% reduction in PGC-1α1 (the biogenesis form) |
| **Tertiary:** IF for mito morphology | TOMM20 + HSP60 + DAPI confocal; Mitograph analysis | Fragmented network in sarcopenic |

**Sample size** (from `POWER_ANALYSIS.md` §2.1):
- **n ≥ 10 donors/group** for Welch's t per protein at d ≈ 0.8 (log₂ FC ≈ −0.5 to −1.0, SD ≈ 0.4–0.6 in log₂ space, BH-FDR across 6-protein panel)
- n = 13 / group for 0.90 power
- For pilot HSMM Seahorse: n=3 donors × 5 wells/dif

**Acceptance gate (cross-ref §4 decision gate table and HYPOTHESIS.md H0.5 falsification clause):** programme down at protein in ≥1 independent cohort. If failed → report transcript-only honestly; the discovery is biologically real but the H1 (causation) thesis is less attractive as a therapeutic target.

**Timeline.** M2–M12 (begin after biopsy MTA secured at M0–M2; protein panel runs in parallel with Aim 2; PRM-MS final batch + analysis M10–M12).

**Risk + mitigation.**
- **R-A1.1 Biopsy availability** (P=med, I=high): start MTA process at M0 (Lonza or institutional biobank); have 2 backup sources (e.g., NIH GTEx muscle biospy archive, BIDMC muscle bank).
- **R-A1.2 Lonza HSMM custom-donor lead time** (P=high, I=med): 4–6 weeks MTA + 6–12 weeks cell prep; place order at M0–M1; if delayed, use independent biopsy cohort for protein, defer HSMM to Aim 2.
- **R-A1.3 Antibody cross-reactivity** (P=med, I=med): each Ab validated in C2C12 + HSMM via siRNA-KD lysate (positive control) and Ad-overexpression (negative control) before deployment on biopsy lysates (`ANTIBODY_PANEL.md` §7 pitfalls G3, G4, G5 for TOMM20, PGC-1α, TFAM).

*What §2.1 tells you:* Aim 1 tests whether the v0.4 transcript-level finding holds at protein in an independent cohort (n≥10/group), using a 14-Ab lean core panel + optional PRM-MS. Decisive for H0.5; 6–12 months timeline.

### 2.2 Aim 2 — Causation (H1) — the decisive aim

**Purpose.** Test whether knockdown of Tier-1/2 genes (CHCHD10, NDUFB4, ATP5F1B) and the programme master (PGC-1α1) reduces mitochondrial respiration **and specific force at matched CSA** in myotubes. This is the **single experiment that moves the v0.4 paper from JCR 5–10% to top-tier** by establishing causation in vitro before the in-vivo Exp B.

**Models.**
- **Primary:** **C2C12 myotubes** (ATCC CRL-1772), d5 differentiation, siRNA KD screen (4 Tier-1/2/master genes × scramble = 5 conditions × 3 biological differentiations).
- **Secondary:** **HSMM myotubes** (Lonza CC-2580), d7–d10 differentiation, same siRNA panel; 3 donors × 5 wells.
- **Tertiary:** **iPSC-derived myocytes** (bit.bio ioSkeletal io1002) for human-relevance + isogenic CHCHD10/ATP5F1B KO (Cellectics or Crown Bio custom edit, 12–20 weeks lead time — see OI-5).
- **3D primary model:** **3D myobundle** in fibrin/Matrigel hydrogel on PDMS posts (SOP: `MYOBUNDLE_SPECIFIC_FORCE_SOP.md` §3). C2C12 myobundles for the primary screen; HSMM myobundles for human relevance.

**Constructs (cross-ref `CONSTRUCT_SPECS.md` §1–§5; `CRISPR_DESIGNS.md` §1–§4):**

| Gene | siRNA SMARTpool (primary screen) | Individual siRNA (deconvolution) | sgRNA selected best (orthogonal KO) | Verified RefSeq |
|---|---|---|---|---|
| **CHCHD10** (mouse) | Horizon siGENOME M-XXXXXX-02 [TBD at order] | Thermo Silencer Select | **mm_Chchd10_sg1**: GCCGGGTCTTATGGCTCAGA + TGG (position 1029, exon 3) | **NM_175329.4** (CORRECTED — was NM_001136064.2 which is mouse *Bscl2*) |
| **CHCHD10** (human) | Horizon siGENOME M-XXXXXX-02 [TBD] | Thermo Silencer Select | **hs_CHCHD10_sg1**: TGACCGGAGCCTTCAGCGGG + GGG (position 304, exon 2) | NM_001301339.2 |
| **NDUFB4** (mouse) | Horizon siGENOME [TBD] | Thermo Silencer Select | **mm_Ndufb4_sg1**: CAAACGCGTGTCGCACATCG + AGG (position 220, exon 1) | **NM_026610.2** (CORRECTED — was NM_026610.3, retired by NCBI) |
| **NDUFB4** (human) | Horizon siGENOME [TBD] | Thermo Silencer Select | **hs_NDUFB4_sg1**: TACAACGATCCCAACCGCCG + AGG (position 175, exon 1) | NM_004547.6 (transcript variant 1) |
| **ATP5F1B** (mouse) | Horizon siGENOME [TBD] | Thermo Silencer Select | **mm_Atp5f1b_sg1**: CGTGGCAGTCATCGGCGCTG + TGG (position 209, exon 2) | NM_016774.3 |
| **ATP5F1B** (human) | Horizon siGENOME [TBD] | Thermo Silencer Select | **hs_ATP5F1B_sg1**: CGTGGCGGTCATTGGCGCAG + TGG (position 210, exon 2) | NM_001686.4 |
| **PPARGC1A** (mouse, PGC-1α1) | Horizon siGENOME (PGC-1α1-selective, exon 7–8 of NM_008904.3) | Thermo Silencer Select | **mm_Ppargc1a_sg1**: ATGCCTCCTGTGACTGGCAG + GGG (position 1328, **exon 8 — spares PGC-1α4**) | NM_008904.3 |
| **PPARGC1A** (human, PGC-1α1) | Horizon siGENOME (PGC-1α1-selective, exon 8 of NM_013261.5) | Thermo Silencer Select | **hs_PPARGC1A_sg1**: AGTCCTCACTGGTGGACACG + AGG (position 1176, **exon 8 — spares PGC-1α4**) | NM_013261.5 |

**Cas9 / vector selection (cross-ref `CRISPR_DESIGNS.md` §8):**
- **CHCHD10** (small ORF, off-target-sensitive): **eSpCas9(1.1)** (Addgene #71814 Slaymaker 2016 PMID 26628643, or T2A-Puro variant #101039)
- **NDUFB4, ATP5F1B, PGC-1α1**: standard SpCas9 in **lentiCRISPR v2** (Addgene #52961 Sanjana 2014 PMID 25075903)
- **RNP delivery (transient):** IDT Alt-R Cas9 V3 (Cat #1081058) + crRNA:tracrRNA, by Lonza 4D-Nucleofector

**Off-target audit (cross-ref `OFF_TARGET_AUDIT.md`):** All 8 selected best sgRNAs **PASS** the mitochondrial watch-list filter (162 mRNAs scanned, 0 perfect 20-nt+NGG matches, 0 matches at 1–3 mm). Full-genome Hsu 2013 off-target score is **TBD via CRISPOR** at design-tool time before vendor synthesis (acceptance gate: Hsu ≥ 70 for SpCas9; Hsu ≥ 50 for eSpCas9(1.1) on CHCHD10).

**End points.**

| Endpoint | Tier | Method | Acceptance criterion (Aim 2 primary) |
|---|---|---|---|
| **PRIMARY (quality):** Specific force at matched CSA | 1 (decisive) | 3D myobundle force on IonOptix C-Pace or Aurora 1300A (SOP: `MYOBUNDLE_SPECIFIC_FORCE_SOP.md`) + diameter / CSA quantification by phase-contrast or confocal; **3 statistical approaches**: regression (LMM, log(sF) ~ genotype + log(CSA) + (1\|dif)), stratification (CSA quartiles), matched-pairs (KD bundle paired with control ±10% CSA) — see §5 below | **≥20% reduction in specific force at matched CSA** for ≥1 of CHCHD10, NDUFB4, ATP5F1B KD in C2C12 or HSMM myobundles, p<0.05 after BH-FDR |
| **PRIMARY (metabolic):** Seahorse Mito Stress Test OCR | 1 (decisive) | Seahorse XFe96 (SOP: `SEAHORSE_MITO_STRESS_TEST_SOP.md`); basal, ATP-linked, maximal (FCCP-uncoupled, titration-mandatory §4.3 of SOP), spare respiratory capacity; normalize to protein (BCA) | **≥20% reduction in basal or maximal OCR** at matched cell number / protein for ≥1 Tier-1/2 KD, p<0.05 after BH-FDR across OCR metrics |
| **PRIMARY (mechanism for ATP5F1B specifically):** ATP-linked OCR | 1 | Oligomycin-sensitive component of OCR | Selective ≥25% reduction in ATP-linked OCR for ATP5F1B KD |
| Secondary: ΔΨm | 2 | TMRE (Thermo, 100 nM, 30 min loading) or MitoTracker Red CMXRos; flow or plate reader | Reduced in KD vs scramble |
| Secondary: mt-ROS | 2 | MitoSOX Red (Thermo, 5 µM, 15 min); flow | Elevated in KD |
| Secondary: ATP rate | 2 | Seahorse ATP Rate Assay (Agilent) | mitoATP rate reduced ≥20% |
| Secondary: Mito morphology | 2 | TEM (cristae) for CHCHD10 + APOO KD (`VENDOR_SHORTLIST.md` §8.2); IF (TOMM20 + HSP60 + DAPI confocal) + Mitograph network analysis | Fragmented network; for CHCHD10 KD: swollen mitochondria with reduced cristae |
| Secondary: Myotube diameter / fusion index | 2 (essential for matched-CSA design) | MF20 + DAPI IF; ImageJ; ≥30 myotubes per condition | Report independently of force; **CSA must be matched in the analysis** |
| Secondary: KD validation at mRNA | required QC | RT-qPCR ΔΔCt, RPLP0 or 18S normalization | **≥70% mRNA reduction** at 48h (siRNA) |
| Secondary: KD validation at protein | required QC | Western blot, target Ab from 6-Ab minimal verification set (`ANTIBODY_PANEL.md` §6) | **≥50% protein reduction** at 96h (siRNA), 7d (shRNA/CRISPR), 14d (clonal KO) |
| Secondary: Matched-pair sub-programme verification | required for specificity | For ATP5F1B KD: anti-ATP5A1 (ab14748) should be **unchanged** (matched-pair complex V control); for NDUFB4 KD: anti-NDUFA9 (ab14713) + anti-NDUFS1 (Proteintech 12444-1-AP) | Demonstrates KD specificity vs complex-wide collapse |

**Sample size** (from `POWER_ANALYSIS.md` §2.1, §5.2):

| Sub-experiment | Effect (Δ) | SD | Test | n / condition @ 0.80 | n / condition @ 0.90 | Wells/bundles total |
|---|---|---|---|---|---|---|
| **C2C12 Seahorse Mito Stress Test** | OCR Δ = 22–25% (Cohen's d ≈ 1.5, large) — **updated from 15% in v0.2** | 15–18% (within-dif CV) | One-sample t (vs scramble = 100%) | **5 wells/dif × 3 difs = 15 wells** | 7×3 = 21 | 15–21 wells/condition |
| **HSMM Seahorse Mito Stress Test** | OCR Δ = 22–25% | 18% (between-donor) | One-sample t | **5 wells/donor × 3 donors = 15 wells** | 5×4 = 20 | 15–20 wells/condition |
| **C2C12 myobundle force at matched CSA** | Specific-force Δ = **20%** (updated from 15%) | 15% per bundle | Welch's t / LMM | **6 bundles/dif × 3 difs = 18 bundles** | 12×3 = 36 | 18–36 bundles/condition |
| **HSMM myobundle force at matched CSA** | Specific-force Δ = 20% | 18% (between-donor) | LMM with donor random | 9 bundles × 3 donors = 27 | 12×3 = 36 | 27–36 bundles/condition |
| **Spare respiratory capacity** (most variable OCR metric) | Δ = 30–35% | 25–30% | One-sample t | 5 wells/dif × 3 difs | 7×3 | 15–21 wells/condition |

**Matched-CSA design (the central methodological innovation, cross-ref `MYOBUNDLE_SPECIFIC_FORCE_SOP.md` §4):**

The decisive Aim 2 test is **specific force at matched CSA**, not raw force or raw CSA. Three orthogonal statistical approaches must agree:

1. **Approach 1 — Regression (LMM, primary).** `log(specific_force) ~ genotype + log(CSA) + (1|differentiation)`. Includes log(CSA) as a covariate so the genotype effect estimates the **CSA-adjusted specific force**. Most powerful; this is the pre-registered primary model.
2. **Approach 2 — Stratification.** Bin bundles by CSA quartile; compare KD vs scramble *within each quartile*. Robust to model misspecification.
3. **Approach 3 — Matched-pairs.** Pair each KD bundle with the closest-CSA control bundle (±10% CSA); paired t-test. Most defensible to reviewers because it makes no parametric assumption about the CSA-force relationship.

**All three approaches must directionally agree for the Aim 2 gate to pass.** Pre-registered SAP enforced (`POWER_ANALYSIS.md` §4.2).

**Acceptance gate (cross-ref §4 and HYPOTHESIS.md H1 falsification clause):** ≥1 of CHCHD10, NDUFB4, ATP5F1B KD reduces OCR ≥20% **at matched CSA** (p<0.05, BH-FDR <0.10), with all 3 statistical approaches agreeing. **If failed:** effect is mass-linked, not quality; programme is not a quality driver. Re-frame the v0.4 paper accordingly (mass-side effect of the programme) and shift to other muscle-quality pillars (NMJ, ECM) for follow-up.

**Timeline.** M2–M9 (6 months for full Aim 2 PoC in C2C12 + HSMM; iPSC-CRISPR runs in parallel M3–M9).

**Risk + mitigation.**
- **R-A2.1 KD efficiency <70%** (P=med, I=high): start with siRNA SMARTpool (4-oligo, ≥75% KD guaranteed by Horizon); if fails, deconvolute to individual oligos; if still <70%, escalate to CRISPR (RNP first, then lentiCRISPR v2 stable line).
- **R-A2.2 Off-target effect of KD** (P=low, I=med): mitigated by (i) `OFF_TARGET_AUDIT.md` mitochondrial watch-list pre-screen (all 8 selected sgRNAs PASS); (ii) ON-TARGETplus chemical modification (Horizon) reduces off-target seed effects ~5-fold; (iii) rescue control (Ad-PGC-1α for PGC-1α arm; siRNA-resistant CHCHD10 cDNA in pLVX-TetOne-Puro for CHCHD10 arm — `CONSTRUCT_SPECS.md` §5.4).
- **R-A2.3 Specific-force rigor (matched-CSA design)** (P=low, I=high): mitigated by (i) blinded scoring (KD vs scramble identity withheld from analyst); (ii) pre-registered SAP filed on OSF before unblinding; (iii) 3 orthogonal statistical approaches (must all agree); (iv) report CSA distributions separately to demonstrate matching.
- **R-A2.4 PGC-1α isoform cross-reactivity** (P=med, I=med): mitigated by (i) sgRNA placed in exon 8 of canonical PGC-1α1 (shared by α1/α2/α3/α-b/α-c/NT, NOT PGC-1α4); (ii) 3-isoform qPCR validation (exon 1a-PGC-1α1, exon 1b-PGC-1α-b, exon 6 PGC-1α4 splice junction; `CONSTRUCT_SPECS.md` §4.6.1).

*What §2.2 tells you:* Aim 2 is the decisive in-vitro causation test. Primary readouts are Seahorse OCR (Δ 22–25% expected, Cohen's d ≈ 1.5) and specific force at matched CSA (Δ 20% expected). Three orthogonal statistical approaches must agree. 6–9 months timeline.

### 2.3 Aim 3 — Programme test (H1.4) + rescue

**Purpose.** Test whether the entire 6-sub-programme down-regulation seen in HMSR v0.4 can be reproduced by knocking down a single master regulator (PGC-1α1). If yes → programme is one-node-controlled (master-switch model); if no → programme is multi-node, requires combinatorial perturbation. Also tests **rescue** (does restoring PGC-1α1 rescue Tier-1/2 KD phenotype?) and **exercise mimetic** (does AICAR or electrical pulse stimulation compensate?).

**Models.**
- **Primary:** C2C12 d5 myotubes + HSMM d7–10 myotubes, siRNA against PGC-1α1 (designed to spare PGC-1α4; `CONSTRUCT_SPECS.md` §4.3).
- **Rescue arm:** C2C12 + HSMM with CHCHD10 siRNA + Ad-PGC-1α1 (mouse: Vector Biolabs **ADV-280991**, MOI 10–50; human: **ADV-219511**) — *updated from v0.2 cited #1047 (older catalog)*.
- **Exercise-mimetic arm:** C2C12 + HSMM with CHCHD10 / NDUFB4 / ATP5F1B siRNA + (a) AICAR 1–2 mM, 24h (AMPK activator); (b) electrical pulse stimulation, IonOptix C-Pace EP, 1 Hz × 2h × 5 days.

**End points.**

| Endpoint | Method | Acceptance criterion |
|---|---|---|
| **PRIMARY:** PGC-1α1 KD reproduces programme signature | RNA-seq (Azenta NovaSeq, PE150, 30M reads) on PGC-1α1 KD vs scramble C2C12 d5 myotubes (4 difs/condition); DESeq2 + correlation-aware label-permutation gene-set test against the 539-gene HMSR v0.4 programme | **All 6 sub-programmes concordantly down** at programme-permutation p < 0.05 (matches HMSR v0.4 result); pathway-level FDR < 0.10 |
| **PRIMARY:** Isoform selectivity of PGC-1α1 KD | RT-qPCR with 3 isoform-specific primers (exon 1a-PGC-1α1, exon 1b-PGC-1α-b, exon 6 PGC-1α4 splice junction) | PGC-1α1 mRNA ↓≥70%; PGC-1α4 mRNA **unchanged** (the design intent — `CONSTRUCT_SPECS.md` §4.6.1) |
| Secondary: PGC-1α1 protein KD | WB with CST 2178 (D5K9D, recognizes C-terminus of all major isoforms — `ANTIBODY_PANEL.md` §1.1 #7); run 7–8% gel for the 91 kDa canonical | ≥50% reduction at 96h |
| Secondary: TFAM protein (downstream of PGC-1α) | WB with CST 8076 (D5C8) | ≥30% reduction |
| Secondary: mtDNA copy number | qPCR (MT-ND1 / nuclear β2M) | ≥30% reduction (TFAM-dependent endpoint) |
| Secondary: Programme protein panel | WB with 14-Ab lean core (`ANTIBODY_PANEL.md` §1.1, §1.2) | ≥30% reduction in 4+ of the 6 sub-programme representatives |
| **Rescue:** Ad-PGC-1α1 rescues CHCHD10-KD OCR/force phenotype | Seahorse + myobundle force on CHCHD10-KD ± Ad-PGC-1α1 (within-dif paired, n=3 difs × 3 conditions = scramble, CHCHD10-KD, CHCHD10-KD+rescue) | Rescue restores OCR + specific force to ≥80% of WT scramble level |
| **Exercise mimetic:** AICAR/EPS partially compensates for CHCHD10/NDUFB4/ATP5F1B-KD | Seahorse + qPCR programme readout ± AICAR or ± EPS | Programme partially restored; OCR partial rescue ≥40% of WT |

**Sample size** (from `POWER_ANALYSIS.md` §2.1):
- **PGC-1α RNA-seq:** n=4 differentiations/condition (scramble vs siPGC-1α) = 8 libraries; DESeq2 + pathway permutation; matches v0.2 + v0.3 specification; 0.80 power for pathway-level test
- **Rescue arm:** within-dif paired (scramble vs KD vs KD+rescue), n=3 difs × 3 conditions = 9 wells/replicate; paired t-test (within-dif design = high power)
- **Exercise mimetic arm:** same as rescue; n=3 difs × 3 conditions = 9 wells/replicate

**Acceptance gate (cross-ref §4 and HYPOTHESIS.md H1.4 falsification clause):** PGC-1α1 KD reproduces all 6 sub-programmes concordantly down (matches HMSR v0.4 result). **If failed (programme not reproduced by single-node KD):** the programme is multi-node, requires CRISPR screen + multi-target rescue arm to find the master regulator(s). The Aim 3 result becomes a methodological refinement rather than a definitive mechanistic result.

**Timeline.** M3–M9 (concurrent with Aim 2; PGC-1α RNA-seq + analysis takes M5–M8; rescue + exercise-mimetic arms M6–M9).

**Risk + mitigation.**
- **R-A3.1 PGC-1α isoform off-target** (P=med, I=med, *also flagged as R3 in §8*): mitigated by exon 8 targeting + 3-isoform qPCR (see §2.2 R-A2.4).
- **R-A3.2 Ad-PGC-1α over-expression toxicity** (P=med, I=med): titrate MOI 1–10–50; verify expression by qPCR + WB at each MOI; cap at MOI giving 2–5× endogenous PGC-1α1 mRNA (avoids chronic-overexpression brain-side oxidative stress reported by Zhou 2025 PMID 40228677).
- **R-A3.3 RNA-seq cost** (P=low, I=low): use Novogene or BGI for cost-saving (~$200–250/sample × 16 libraries = $3.5K; alternative to Azenta at $250/sample).

*What §2.3 tells you:* Aim 3 tests whether PGC-1α1 is the master switch (RNA-seq pathway test) and whether restoring it rescues Tier-1/2 KD. Critical isoform-selectivity step (exon 8 + 3-isoform qPCR). 3–6 months, concurrent with Aim 2.

### 2.4 Aim 4 — CLTB (separate, hypothesis-generating)

**Purpose.** Determine whether CLTB (clathrin light chain B) — which appeared in the v0.4 candidate list but is **non-mitochondrial** by canonical annotation — is functionally connected to mitophagy via clathrin-mediated mechanisms. Low priority; only pursued if Aim 2 has slack at M9–M11.

**Models.** C2C12 myotubes + HSMM (low-throughput).

**End points.**
- **Co-IP of CHCHD10 / CLTB** in C2C12 lysates (anti-CHCHD10 Proteintech 25671-1-AP for IP; anti-CLTB for the pull-down detection — vendor TBD).
- **mt-Keima mitophagy flux** in C2C12 ± CLTB siRNA (transgene transduction via lentivirus; FACS readout 458 nm acidic / 561 nm neutral; `ANTIBODY_PANEL.md` §1.3 #30 mt-Keima transgene specification).

**Sample size.** n=2 differentiations (exploratory, per v0.2 §2 Aim 4 framing).

**Acceptance criterion.** Hypothesis-generating only — descriptive results that inform whether CLTB belongs in the mitochondrial story or should be removed from the candidate list.

**Timeline.** M9–M11 (only if Aim 2 has slack; defer to follow-up if Aim 2 is full).

**Risk + mitigation.** Low risk; low priority; can be deferred to a separate paper or to Y2.

*What §2.4 tells you:* Aim 4 (CLTB) is hypothesis-generating, low priority. Only runs if Aim 2 has slack. Co-IP + mt-Keima. 1–2 months.

---

## §3 — In vivo program (Exp A–D)

### 3.0 In-vivo overview

| Experiment | Question | Primary readout | Decisive gate | Animals (n/group, total) | Months | Cost (USD) |
|---|---|---|---|---|---|---|
| **Exp A** | Does the programme track function with age? | Single-fibre specific force, young 3-mo vs aged 24-mo C57BL/6JN; programme qPCR + WB; permeabilized-fibre respiration (Oroboros) | Programme decline tracks specific force more tightly than mass/CSA (H2 observational anchor) | n=8/group × 2 groups = 16 mice | M4–M6 | $20–25K |
| **Exp B** | Does targeted KD cause specific-force loss with mass preserved? (the in-vivo causation experiment) | In-vivo specific force at matched CSA; permeabilized-fibre respiration | Specific-force loss with CSA preserved, p<0.05 (HYPOTHESIS.md H1 in vivo; cross-ref §4 decision gate) | n=14/group × 2 groups (CHCHD10 + ATP5F1B; **n=11/group min-viable**) = 28–42 mice | M4–M8 | $40–55K |
| **Exp C** | Does exercise rescue the programme and specific force? | Programme qPCR + WB; specific force; permeabilized-fibre respiration | Exercise up-regulates programme AND raises specific force (H2 causal) | n=12/arm × 3 arms = 36 mice | M5–M8 | $25–35K |
| **Exp D** | Does therapeutic restoration deliver function at equal mass? (top-tier mass-matched experiment) | Specific force at equal mass gain (ANCOVA, mass as covariate); programme protein recovery | Mito-restoration arm > anabolic arm on specific force at ≤ mass gain (H3 — the top-tier result) | n=15/arm × 3 arms = 45 mice (aged 24-mo) | M8–M14 | $55–80K |

**Common animal sources, randomization, and blinding (cross-ref `VENDOR_SHORTLIST.md` §4):**

| Item | Specification |
|---|---|
| **Young animals (3-mo)** | JAX C57BL/6J stock #000664 ($30/mouse, 2-week lead) for Exp B + C; matches most muscle-biology literature |
| **Aged animals (24-mo)** | **NIA Aged Rodent Colony C57BL/6JN** (FREE for aging-research grants; 4–8 week lead; 10–20 mice/month quota) for Exp A + D; matches the NIA-funded aging literature. **Backup:** JAX 24-mo at $130–170/mouse if NIA quota exhausted |
| **Sex** | **All male** in v0.4 (matches HMSR cohort which is male-dominated; halves animal cost). Mixed-sex replication flagged as follow-up R01 (OI-8). |
| **Randomization** | Stratified block randomization with cage as block, littermate as strata; pre-generated allocation by computational lead before animal arrival |
| **Blinding** | Force assays and histology scored blinded to allocation; AAV injection blinded (TA-left scramble, TA-right shRNA — within-subject pairing in Exp B); SAP pre-registered on OSF + AsPredicted before unblinding |
| **IACUC / institutional approvals** | File IACUC protocols at M0 (2–3 month approval lead time); include AAV9 BSL-2 waste handling, terminal procedures, blood + tissue harvest plan |
| **DLAR per diem** | $0.50–1.50/mouse/day (institutional); for aged colony maintenance ~$1.50/mouse/day for 18 mo = ~$48,600 for 60-mouse aged colony (major budget line) |
| **Survival planning** | C57BL/6J males 24-mo: 60–70% survival; 28-mo: 35%. **Order 20–30% MORE than experimental n** to account for attrition |

**Common in-vivo SOPs (cross-ref `validation/plan/experimental_validation_plan_v0.3.md` §4.3, OI-9 through OI-12 to be written before M3):**
- AAV9-shRNA TA injection SOP (Exp B) — 50 µL per TA, 1×10¹¹ vg per TA, single intramuscular injection, contralateral scramble control
- Single-fibre + permeabilized-fibre specific-force SOP (Exp A/B) — Aurora Scientific 300C-LR dual-mode lever; skinned-fibre prep with 5% Triton X-100 in relaxing solution; Ca²⁺-activated force at pCa 4.5
- Aged-mouse handling + tissue harvest SOP (Exp A/B/D) — isoflurane + cervical dislocation; left TA = histology (OCT embedding); right TA = RNA/protein (RNAlater + snap-freeze)
- Permeabilized-fibre Oroboros O2k SOP — MiR05 medium; standard substrate-uncoupler-inhibitor titration (Malate/Glutamate, ADP, Succinate ± Rotenone, FCCP, Antimycin A)

### 3.1 Exp A — Observational (young vs aged C57BL/6J)

**Purpose.** Establish in vivo the natural-history correlation: does the v0.4 programme down-regulation track muscle specific force more tightly than it tracks mass/CSA? This is the in-vivo observational anchor for the muscle-quality thesis.

**Design.**

| Group | n | Strain | Age | Sex | Notes |
|---|---|---|---|---|---|
| Young | 8 | C57BL/6J (JAX #000664) | 3 mo | M | Standard young control |
| Aged | 8 | C57BL/6JN (NIA Aged Colony) | 24 mo | M | NIA-supplied if quota; JAX backup |

**Total: 16 mice.** Stratified by cage at randomization.

**End points.**

| Endpoint | Method | Acceptance criterion |
|---|---|---|
| **PRIMARY:** Single-fibre specific force | Aurora Scientific 300C-LR dual-mode lever; skinned-fibre Ca²⁺-activated force at pCa 4.5; sarcomere length by laser diffraction; CSA by photomicrograph + assuming circular cross-section; 4 fibres/animal from EDL, soleus, gastrocnemius | Specific-force reduction in aged vs young, **−25 to −30% per fibre**, SD ≈ 15–20% (Brooks & Faulkner classic; Larsson 1995; updated by Marcus 2020) |
| **PRIMARY:** Mito programme qPCR + WB | RT-qPCR + WB 14-Ab lean core (`ANTIBODY_PANEL.md` §1.1, §1.2); TA + gastrocnemius + soleus + EDL per animal | Programme down ≥30% in aged vs young at protein |
| Secondary: Permeabilized-fibre respiration | Oroboros O2k (`VENDOR_SHORTLIST.md` §5.3); MiR05 medium; State 3 ADP-stimulated respiration with Malate/Glutamate/Succinate ± Rotenone | State 3 respiration reduced ≥25% in aged, SD ≈ 18% (Halling 2019 PMID 31265325 anchor) |
| Secondary: Fibre CSA | Histology + ImageJ on cross-sections | Reduced in aged ≥20% |
| Secondary: Fibre type proportion | Multiplex IHC (DSHB A4.951 type I + SC-71 type 2A + BF-F3 type 2B; `ANTIBODY_PANEL.md` §1.5 #35–37) | Type II → I shift in aged (classic finding) |
| Secondary: Grip strength | Bioseb BIO-GS3 grip strength meter ($3,000, `VENDOR_SHORTLIST.md` §6.5) | Reduced in aged ~20% |
| Secondary: mtDNA copy number | qPCR (MT-ND1 / nuclear β2M) | Reduced in aged |

**Sample size** (from `POWER_ANALYSIS.md` §2.2):
- **n = 8 animals/group** with 4 fibres/animal nested in animal random effect
- Linear mixed model: `lme4::lmer(specific_force ~ age + (1|animal_id) + (1|animal_id:fibre_id))`
- 6 animals/group sufficient @ 0.80 for Δ = 25%, SD = 15–20%; n=8 over-powers slightly (gives 0.85+); LMM with 4 fibres/animal = 32 fibres/group

**Statistical plan** (from `POWER_ANALYSIS.md` §4.1):
- Primary test: LMM (animal as random, fibre nested in animal); age as fixed effect
- BH-FDR across 4 primary + secondary endpoints (force, CSA, grip, respiration)
- Cohen's d / Hedges' g + 95% CI (effectsize R package, noncentral t distribution); partial η² for ANOVA-style

**Timeline.** M4–M6 (begins after NIA aged-mouse delivery at M4; 4–6 weeks of measurements + tissue processing).

**Budget breakdown:**
- Young mice (n=8 × $30 JAX) = $240
- Aged mice (n=8 × NIA free, or $115 JAX backup × 8 = $920)
- 24-mo husbandry (12 mo extra at NIA + transition): ~$1,460
- Permeabilized-fibre Oroboros runs ($200/sample × 16 × 3 substrates = 48 runs): **$9,600**
- Single-fibre force rig (university core, $100/day × 16 rig-days): $1,600
- Histology + TEM: $5,600 (or down-sample to n=6 to save)
- **Total Exp A: ~$20,000–25,000**

**Risk + mitigation.**
- **R-ExpA.1 NIA aged-mouse quota exhausted** (P=med, I=high, *also R2 in §8*): place NIA order at M0; backup JAX 24-mo ($130–170/mouse).
- **R-ExpA.2 Single-fibre ICC unknown** (P=med, I=low): assumed ICC=0.3 in power calc; could be 0.2–0.4; run pilot n=3 × 10 fibres at start to refine.
- **R-ExpA.3 Aged-mouse pre-experiment mortality** (P=med, I=med): order 30–40% more aged mice than n=8 (i.e., n=10–11); typical 28-mo mortality 25% (Springer-Sapp 2025-style RT cohorts adapt).

*What §3.1 tells you:* Exp A is the in-vivo observational anchor (n=8/group young vs aged C57BL/6J). Primary readouts are single-fibre specific force + programme protein/qPCR + Oroboros. 4–6 months; ~$20–25K.

### 3.2 Exp B — Causal sufficiency (AAV9-shRNA, TA, young mice) — the key quality experiment

**Purpose.** Direct causal test: does AAV9-shRNA knockdown of CHCHD10 (Tier 1) and ATP5F1B (Tier 2) in the tibialis anterior (TA) of young mice reduce specific force **while preserving mass and CSA**? This is the decisive in-vivo experiment for H1.

**Design.**

| Group | n (recommended @ 0.90) | n (min-viable @ 0.80) | Strain | Age | Sex | TA-left | TA-right (within-subject control) | Notes |
|---|---|---|---|---|---|---|---|---|
| AAV9-shCHCHD10 | **14** | 11 | C57BL/6J (JAX) | 3 mo | M | shCHCHD10 injection | scramble (within-subject control) | Standard primary group |
| AAV9-shATP5F1B | **14** | 11 | C57BL/6J | 3 mo | M | shATP5F1B injection | scramble | Standard primary group |

**Total: 22–28 mice** (min-viable n=11/group; recommended n=14/group). **All male** (matches HMSR cohort; mixed-sex replication = follow-up R01 — see OI-8).

**v0.2 → v0.4 sample-size change.** v0.2 specified n=10/group with assumed SD = 10%. **Realistic AAV9 + in-vivo TA force SD is 12%** (literature: Cattaneo 2026 PMID 41872887 AAV9-shRNA in TA; Medert 2021 PMID 33580817 AAV9 RNAi 90% KD efficiency). With Δ = 15% (the Guzman 2026 working estimate; OI-1 to verify with full PDF — conservatively use 20% pending verification): n = 11/group @ 0.80, n = 14/group @ 0.90 (`POWER_ANALYSIS.md` §5.1, §5.2).

**Constructs (cross-ref §2.2 and `CONSTRUCT_SPECS.md` §1, §3):**
- **AAV9-CAG-GFP-U6-mShRNA-Chchd10** (mouse) — packaged via VectorBuilder ultra-purified research-grade (1 mL @ ≥10¹³ GC/mL) — see OI-4 for vendor decision (VectorBuilder vs Penn Vector Core vs in-house)
- **AAV9-CAG-GFP-U6-mShRNA-Atp5f1b** (mouse)
- **AAV9-CAG-GFP-U6-scramble** (control)

**End points.**

| Endpoint | Tier | Method | Acceptance criterion (Exp B primary) |
|---|---|---|---|
| **PRIMARY:** In-vivo specific force at matched CSA | 1 (decisive) | Aurora Scientific 1300A in-vivo apparatus (`VENDOR_SHORTLIST.md` §6.2); twitch + tetanic force; **mass and CSA reported independently**; ANCOVA with CSA as covariate | **Specific-force loss with CSA preserved**, p<0.05, n=11–14, mixed model `lmer(specific_force ~ treatment + (1|animal_id))` with leg as repeated within animal |
| **PRIMARY:** Permeabilized-fibre Oroboros respiration | 1 (decisive) | Oroboros O2k; State 3 ADP-stimulated respiration with Malate/Glutamate/Succinate ± Rotenone | State 3 respiration reduced ≥25% in shRNA vs scramble TA, SD ≈ 18% |
| Secondary: KD efficiency at mRNA | required QC | RT-qPCR on left vs right TA (paired within mouse), normalized to Rplp0 | ≥70% mRNA reduction in shRNA TA |
| Secondary: KD efficiency at protein | required QC | WB on left vs right TA, target Ab from 6-Ab minimal verification set (`ANTIBODY_PANEL.md` §6) | ≥50% protein reduction |
| Secondary: Muscle mass (TA wet weight at sacrifice) | 1 (essential for matched-CSA interpretation) | Wet weight at sacrifice | **Report independently;** for H1 to be confirmed, mass should be preserved (≤10% reduction) while specific force drops ≥15% |
| Secondary: Fibre CSA | 1 (essential) | Histology + ImageJ; ≥100 fibres per cross-section | Same as mass — report independently; preserved is the H1-supporting outcome |
| Secondary: Fibre type | 2 | Multiplex IHC fibre-type trio (DSHB A4.951 + SC-71 + BF-F3); `ANTIBODY_PANEL.md` §2.3 | Report; no a priori prediction |
| Secondary: TEM (mito morphology) | 2 (for CHCHD10 arm) | TEM on permeabilized fibres + cross-sections (`VENDOR_SHORTLIST.md` §8.2); n=6 per group | For CHCHD10 KD: cristae disruption (consistent with MICOS role) |
| Secondary: mtDNA copy number | 2 | qPCR | Reduced |
| Secondary: Grip strength / rotarod | 2 | Bioseb grip + AccuRotor rotarod | Reduced in shRNA arm |
| Secondary: RNA-seq (post-treatment) | 2 (programme-level cross-check) | Azenta NovaSeq, n=28 libraries (n=14 × 2 groups for top-priority CHCHD10 arm; or reduced to bulk TA only) | Programme signature recapitulation |
| Secondary: Histology / IHC for senescence | 2 | p16 + p21 IHC (`ANTIBODY_PANEL.md` §1.5 #38–39) | Increased in shRNA arm? (hypothesis-generating) |

**Statistical plan** (from `POWER_ANALYSIS.md` §4.1, §4.3):
- Primary test: **mixed model `lmer(specific_force ~ treatment + (1|animal_id) + (1|animal_id:leg))`** with leg as within-animal repeated; treatment as fixed
- ANCOVA with CSA as covariate to test specific force adjusted for mass: `lmer(specific_force ~ treatment * mass + (1|animal_id))`
- BH-FDR across 4 primary + secondary endpoints
- Cohen's d / Hedges' g + 95% CI; partial η²
- **Pre-registered SAP on OSF + AsPredicted before unblinding** (M3–M4 SAP freeze)

**Acceptance gate (cross-ref §4 and HYPOTHESIS.md H1 in-vivo falsification clause):** specific-force loss with CSA preserved, p<0.05, n=11–14 with mixed-model analysis. **If failed (force loss tracks mass proportionally):** programme is a passenger / mass-side effect, not a quality driver. This is a publishable, hypothesis-correcting result and reframes the v0.4 paper.

**Timeline.** M4–M8 (4 months total: AAV9 order at M0–M1 for delivery M4–M5; injection M4–M5; 8-wk expression M5–M7; harvest + force + tissue M7–M8).

**Budget breakdown** (from `POWER_ANALYSIS.md` §6.1, `VENDOR_SHORTLIST.md` §10):
- 3-mo C57BL/6J mice (n=28 × $30 JAX): $840
- AAV9 production (3 constructs × 2 batches, VectorBuilder ultra-purified large 1 mL @ ≥10¹³ GC/mL × $3,099): $18,594 list; $15K–17K academic discount (OI-4)
- AAV9 in-vivo delivery + 8-wk holding ($200/mouse × 28): $5,600
- In-vivo force (twitch + tetanic, $300/mouse × 28): $8,400
- Ex-vivo force at matched CSA ($400/mouse × 28): $11,200
- Permeabilized-fibre Oroboros ($200/sample × 28): $5,600
- RNA-seq post-treatment (28 libraries × $250 Azenta): $7,000
- Histology + TEM ($400/mouse × 28): $11,200
- **Total Exp B: ~$55,000 (recommended n=14)** or **~$40,000 (min-viable n=11)**

**Risk + mitigation.**
- **R-ExpB.1 AAV9 lead time** (P=high, I=high, *flagged as R1 in §8*): VectorBuilder ultra-purified 4–6 weeks; Penn Vector Core 3–8 weeks; in-house 2–3 weeks per batch once set up. **Mitigation:** place AAV9 order at M0 (before any other long-lead item) per `VENDOR_SHORTLIST.md` §11 and OI-4; 6-construct production = $9,300–17,000.
- **R-ExpB.2 AAV9 transduction efficiency variability** (P=med, I=med): include GFP reporter co-expression for IHC verification; titrate dose at pilot in n=2 mice before main cohort.
- **R-ExpB.3 In-vivo force SD higher than expected** (P=low, I=high): if SD = 15% rather than 12%, n=11 power drops to 0.60; mitigation = inflate to n=16/group if pilot indicates higher SD.
- **R-ExpB.4 Specific-force rigor (matched-CSA in vivo)** (P=low, I=high, *also R6 in §8*): mitigated by within-subject design (left = scramble, right = shRNA), blinded analysis, pre-registration of SAP.
- **R-ExpB.5 Guzman 2026 number TBD** (P=low, I=med, *also R7 in §8 and OI-1*): conservatively assume Δ=20%; if Aguilar lab confirms higher Δ (e.g., 25–30%), n can drop; if lower (e.g., 10%), n must inflate to 23.

*What §3.2 tells you:* Exp B is the in-vivo causation experiment (AAV9-shCHCHD10 + shATP5F1B vs scramble, contralateral within-subject design). n=14/group recommended @ 0.90 (or n=11 @ 0.80). 4–8 months; $40–55K. AAV9 order at M0 critical path.

### 3.3 Exp C — Exercise reversibility (closes the WP5 gap)

**Purpose.** Test whether endurance exercise (voluntary wheel) or moderate-intensity exercise (treadmill) up-regulates the programme **and** rescues specific force in young mice. Establishes that the programme is exercise-modifiable — the critical translational link.

**Design.**

| Arm | n | Strain | Age | Sex | Intervention |
|---|---|---|---|---|---|
| Sedentary (control) | 12 | C57BL/6J (JAX) | 3 mo | M | Standard housing |
| Voluntary wheel | 12 | C57BL/6J | 3 mo | M | Lafayette running wheel in cage, 4 weeks |
| Treadmill | 12 | C57BL/6J | 3 mo | M | Columbus treadmill, 5 d/wk × 4 wk, moderate intensity |

**Total: 36 mice.** Stratified by cage at randomization.

**End points.**

| Endpoint | Method | Acceptance criterion |
|---|---|---|
| **PRIMARY:** Mito programme protein (COX IV + PGC-1α + TFAM) | WB with CST 4850 (COX IV, D3H8N) + CST 2178 (PGC-1α, D5K9D) + CST 8076 (TFAM, D5C8); from TA + gastrocnemius lysates | **+30 to +50% in COX IV, SD ≈ 25–30%** in trained vs sedentary (Mesquita 2020 PMID 32748504 anchor: chronic RT in older adults → ETC +39 to +180%) |
| **PRIMARY:** Specific force (sedentary vs wheel) | Aurora 1300A in-vivo apparatus | **+15% specific force, SD ≈ 12%** (Springer-Sapp 2025 PMID 41037391: RT in sarcopenia → +13% strength) |
| Secondary: Permeabilized-fibre respiration | Oroboros O2k | State 3 increased in trained arms (Halling 2019: PGC-1α-dependent rescue of submaximal ADP-stimulated respiration) |
| Secondary: mtDNA copy number | qPCR | Increased in trained |
| Secondary: Fibre type shift | Multiplex IHC | Type I + IIa preserved/increased; Type IIb decreased in trained |
| Secondary: Voluntary wheel running distance | Wheel revolution counter | Cohort variability — report distribution |
| Secondary: Treadmill VO₂peak | Promethion metabolic cage or surrogate | Improved in treadmill arm |

**Sample size** (from `POWER_ANALYSIS.md` §2.2):
- n = 9–11/arm @ 0.80, n = 12–15/arm @ 0.90 (Bonferroni-corrected for 3 pairwise arm comparisons)
- v0.4 uses **n = 12/arm × 3 arms = 36 mice** (matches v0.2); slightly underpowered for 20% Δ (specific force) — accept 0.80 power on the pre-specified primary contrast (sedentary vs wheel)
- For 40% Δ (COX IV protein): well-powered

**Statistical plan** (from `POWER_ANALYSIS.md` §4.1):
- Primary test: mixed ANOVA `lmer(endpoint ~ arm + (1|animal_id))` with arm as fixed
- **Bonferroni** correction for 3 pairwise arm comparisons (sed vs wheel, sed vs treadmill, wheel vs treadmill); pre-specified primary = sed vs wheel
- Cohen's d / Hedges' g; partial η² for arm × endpoint

**Acceptance gate (cross-ref §4 and HYPOTHESIS.md H2 falsification clause):** training up-regulates programme AND raises specific force. **If failed (mass-only recovery):** programme is correlate of exercise response, not causal lever; shift priority to other nodes / pillars.

**Timeline.** M5–M8 (4 weeks intervention starting M5; harvest + tissue + force M8).

**Budget breakdown:**
- 3-mo C57BL/6J (n=36 × $30): $1,080 + holding ~$120 = $1,200
- Wheels + treadmills: $11,000 capex (Lafayette wheels × 12 cages = $7,200 + Columbus treadmill = $5,000 — `VENDOR_SHORTLIST.md` §6.5)
- Mito programme panel WB + qPCR ($300/mouse × 36): $10,800
- Force + Oroboros: ~$10,000
- Histology / IHC: ~$5,000
- **Total Exp C: ~$25,000–35,000**

**Risk + mitigation.**
- **R-ExpC.1 Voluntary wheel running variability** (P=med, I=med): report distance + correlate with phenotype; pre-stratify by wheel-running activity if variability >2-fold.
- **R-ExpC.2 Treadmill compliance / refusal** (P=low, I=low): use gentle treadmill protocol; 5 min ramp-up.
- **R-ExpC.3 4-week exercise window may be insufficient for protein-level changes** (P=med, I=med): if pilot at 2 weeks shows no change, extend to 6–8 weeks (additional cost ~$5K husbandry).

*What §3.3 tells you:* Exp C tests exercise rescue (sed vs voluntary wheel vs treadmill, n=12/arm, 4 weeks). Primary readouts are COX IV/PGC-1α protein and specific force. 5–8 months; ~$25–35K.

### 3.4 Exp D — Therapeutic mass-matched (top-tier lever) — the publication-defining experiment

**Purpose.** Head-to-head test in aged mice of (a) **mitochondrial-restoration intervention** (PGC-1α induction OR 15-PGDH inhibition with SW033291 per Palla 2020 *Science*) vs (b) **anabolic comparator matched for mass gain** vs (c) **vehicle**. The **primary endpoint is specific force at equal mass gain**; if mito arm > anabolic arm at ≤ mass gain, the muscle-quality thesis is supported and the result is **Nature Aging / Cell Metabolism tier**.

**Design.**

| Arm | n | Strain | Age | Sex | Intervention |
|---|---|---|---|---|---|
| **Mito-restoration** | 15 | C57BL/6JN (NIA) | 24 mo | M | **SW033291** (Cayman or MedChemExpress; 15-PGDH inhibitor; dose: 5 mg/kg/day IP × 12 weeks per Palla 2020 PMID 33303683 protocol) OR Ad-PGC-1α (Vector Biolabs ADV-280991 IM, single injection) |
| **Anabolic comparator** | 15 | C57BL/6JN | 24 mo | M | β2-agonist **formoterol** (Sigma; dose: clinical-grade, gives ~10–15% TA mass gain in aged) OR MYO-029 / activin antagonist; mass-matched by dose titration |
| **Vehicle** | 15 | C57BL/6JN | 24 mo | M | DMSO or saline (matched route + frequency) |

**Total: 45 mice.** Stratified by cage and baseline body weight at randomization.

**End points.**

| Endpoint | Tier | Method | Acceptance criterion (Exp D primary) |
|---|---|---|---|
| **PRIMARY:** Specific force at equal mass gain | 1 (decisive) | Aurora 1300A in-vivo + ex-vivo force; **ANCOVA with body mass / TA mass as covariate**; pre-specified contrast: mito vs anabolic at matched mass | **Mito arm > anabolic arm on specific force at ≤ mass gain**, p<0.05 (Bonferroni-corrected for 3 pairwise) — the top-tier muscle-quality result |
| **PRIMARY:** Programme protein recovery | 1 | WB 14-Ab lean core + Oroboros | Programme up in mito arm; partial up in anabolic arm |
| Secondary: Mass gain (body + TA wet weight) | required for ANCOVA | Scale + dissection | Mito arm = anabolic arm = vehicle + intervention-specific gain (mass-matched by dose titration is the key design) |
| Secondary: Permeabilized-fibre respiration | 1 | Oroboros O2k | Mito arm > anabolic arm |
| Secondary: Body composition (lean / fat / water) | 2 | EchoMRI-100H or DEXA | Lean mass and fat mass reported separately |
| Secondary: Grip strength + rotarod | 2 | Bioseb + AccuRotor | Mito arm functional advantage |
| Secondary: Fibre type | 2 | Multiplex IHC | No a priori prediction |
| Secondary: RNA-seq (programme recovery) | 2 | Azenta NovaSeq, n=45 libraries | Programme up in mito arm vs vehicle; verify SW033291 mechanism (mitochondrial gene up-regulation per Palla 2020) |
| Secondary: 15-PGDH expression + activity | 2 | WB (Proteintech 15137-1-AP — `ANTIBODY_PANEL.md` §1.6) + PGE2 ELISA | 15-PGDH inhibited; PGE2 elevated (mechanism confirmation for SW033291 arm) |
| Secondary: TGF-β, ubiquitin-proteasome, autophagy markers | 2 | WB + qPCR (LC3-II, p62, MuRF1, MAFbx); per Palla 2020 expected | Autophagy increased, TGF-β + UPS decreased in mito arm |

**Sample size** (from `POWER_ANALYSIS.md` §2.2):
- n = 9–11/arm @ 0.80 (Bonferroni for 3 pairwise); n = 12–14/arm @ 0.90
- v0.4 uses **n = 15/arm × 3 arms = 45 mice** (matches v0.2 — conservative, **defensible** at grant review per `POWER_ANALYSIS.md` §7.3)
- Anchored to: Palla 2020 PMID 33303683 (15-PGDH-i SW033291 → +mass + strength + mito function in aged) and Shu 2025 PMID 40479501 (SW033291 → muscle mass 33.5 ± 3.0 mg vs 25.2 ± 1.8 mg; CSA 1,424 ± 81 vs 1,263 ± 57 µm² in aged tear)

**Statistical plan** (from `POWER_ANALYSIS.md` §4.1, §4.3):
- Primary test: **Mixed ANOVA + ANCOVA `lmer(specific_force ~ arm * mass + (1|animal_id))`** with arm × mass interaction
- **Bonferroni** for 3 pairwise (mito vs anabolic, mito vs vehicle, anabolic vs vehicle); pre-specified primary = **mito vs anabolic at equal mass**
- Cohen's d for the pre-specified primary contrast
- Pre-registered SAP on OSF + AsPredicted before unblinding

**Acceptance gate (cross-ref §4 and HYPOTHESIS.md H3 falsification clause):** quality arm > anabolic arm on function at ≤ mass gain. **If failed (mito and anabolic equal at equal mass gain):** mitochondrial restoration alone is insufficient; muscle-quality thesis needs another pillar (NMJ, ECM, satellite cell) for full explanation.

**Timeline.** M8–M14 (6 months; 12-wk intervention starting M8 after aged-mouse delivery confirmed; harvest + force + tissue + RNA-seq + analysis M12–M14).

**Budget breakdown:**
- 24-mo C57BL/6JN (n=45 × NIA free or × $115 JAX backup = $5,175) + 12-wk holding ~$5,400 = **$10,575**
- SW033291 (15-PGDH-i; Cayman 15-PGDH inhibitor) or PGC-1α inducer ($200/mouse × 30 active arms × 12 wk): $6,000
- Anabolic comparator (formoterol $200/mouse × 15): $3,000
- Specific force + mass-matched ANCOVA ($700/mouse × 45): $31,500
- RNA-seq programme recovery (45 libraries × $250): $11,250
- Histology + IHC + WB: ~$8,000
- **Total Exp D: ~$55,000–80,000** (largest single experiment; aged-mouse colony is the dominant line)

**Risk + mitigation.**
- **R-ExpD.1 Aged-mouse mortality** (P=med, I=high): order 30–40% more (n=20–21/arm to deliver n=15 final); attrition typical 25% at 24-mo over 3-month intervention.
- **R-ExpD.2 SW033291 supply** (P=low, I=med): Cayman / MedChemExpress reliable; ~$200/mouse-equivalent at 5 mg/kg × 12 wk; order at M6 for M8 start.
- **R-ExpD.3 Mass-matching by dose titration is hard** (P=med, I=med): run pilot n=3 per arm to optimize dose so each active arm gives ~10–15% TA mass gain; then dose-match in main cohort.
- **R-ExpD.4 PGC-1α chronic-overexpression toxicity** (P=med, I=med, Zhou 2025 caveat): use Ad-PGC-1α single IM injection (transient, ~6 weeks) rather than chronic systemic; prefer 15-PGDH-i SW033291 (small molecule, reversible, clinical-grade precedent in Palla 2020).

*What §3.4 tells you:* Exp D is the publication-defining therapeutic experiment (3 arms: mito-restoration vs anabolic vs vehicle, n=15/arm, aged 24-mo). Primary endpoint is **specific force at equal mass gain** (ANCOVA). 8–14 months; ~$55–80K. Anchor: Palla 2020 *Science* SW033291.

---

## §4 — Decision gates (consolidated authoritative table)

This is the **authoritative decision gate table** for the wet-validation program. Each gate has a pass criterion and a pre-specified action if failed. **No gate is duplicated in any other section** — this is the single source.

| Gate # | Aim / Experiment | Pass criterion | If failed (action) | Linked hypothesis |
|---|---|---|---|---|
| **Gate 1** | Aim 1 (protein cohort) | Programme down at protein in ≥1 independent cohort (n≥10 sarcopenic vs n≥10 control); BH-FDR <0.10 across 6-protein primary panel | Report as transcript-only honestly; down-rank H1 mechanistic claim; the discovery is still biologically interesting but less attractive as a therapeutic target | **H0.5** (HYPOTHESIS.md §3) |
| **Gate 2** | Aim 2 (in-vitro function) | ≥1 Tier-1/2 KD (CHCHD10, NDUFB4, or ATP5F1B) reduces OCR ≥20% **at matched CSA**, p<0.05, with all 3 statistical approaches (regression / stratification / matched-pairs) directionally agreeing | Effect is mass-linked, not quality; programme is not a *quality* driver. Re-frame v0.4 paper as mass-side effect; shift to other muscle-quality pillars (NMJ, ECM) for follow-up | **H1** (HYPOTHESIS.md §2) |
| **Gate 3** | Aim 3 (programme master test) | PGC-1α1 KD reproduces all 6 sub-programmes concordantly down by RNA-seq pathway-permutation test, p<0.05 | Programme is multi-node, not one-master-switch; CRISPR screen + multi-target rescue arm becomes more important; refine H1.4 to multi-node model | **H1.4** (HYPOTHESIS.md §2 sub-hypothesis table) |
| **Gate 4** | Exp B (in-vivo causation) | Specific-force loss with CSA preserved (≤10% mass reduction while ≥15% specific-force reduction), p<0.05, n=11–14 with mixed-model analysis | Programme is a passenger / mass-side effect, not a quality driver. Publishable hypothesis-correcting null; reframes the v0.4 paper | **H1** (HYPOTHESIS.md §2 in-vivo) |
| **Gate 5** | Exp C (exercise reversibility) | Training up-regulates programme AND raises specific force in aged mice (sedentary vs wheel pairwise primary) | Programme is correlate of exercise response, not causal lever; shift wet-lab priority to other nodes / pillars | **H2** (HYPOTHESIS.md §4) |
| **Gate 6** | Exp D (therapeutic, mass-matched) | Mito-restoration arm > anabolic arm on specific force **at ≤ mass gain** (pre-specified primary contrast: mito vs anabolic at equal mass), Bonferroni-corrected p<0.05 | Mitochondrial restoration alone is insufficient; muscle-quality thesis needs another pillar; report honest null + reframe as pillar-pluralism muscle-quality model | **H3** (HYPOTHESIS.md §5) — **the top-tier result** |

**Compound-gate logic (per `HYPOTHESIS.md` §6):**
- **Compound-confirmation (top-tier):** Gates 1 + 2 + 4 + 5 + 6 all pass → Nature Aging / Cell Metabolism tier paper (top 5%) on the muscle-quality muscle-restoration thesis.
- **Compound-falsification:** if any 2 of Gates 2 (CHCHD10, NDUFB4, ATP5F1B sub-arms) are refuted at matched CSA, the quality-driver thesis is weakened. If Gate 3 (master switch) is refuted, the master-switch model is wrong → multi-node refinement.

*What §4 tells you:* 6 pre-specified decision gates. Each has a pass criterion and an action if failed. Gates 2 and 4 are the central causation gates; Gate 6 is the publication-defining top-tier gate.

---

## §5 — Statistics & rigor

### 5.1 Statistical framework per experiment (consolidated from `POWER_ANALYSIS.md` §4.1)

| Experiment | Primary test | Random effects (in vivo) | Fixed effects | Multiple-testing correction | Effect-size reporting |
|---|---|---|---|---|---|
| **Aim 1** (cohort protein panel, 6 proteins) | Welch's t (log₂-transformed) per protein | donor (paired donor data) | group (sarcopenic vs control) | **BH-FDR across 6-protein panel** (per experiment) | Cohen's d / Hedges' g + 95% CI (effectsize R package, noncentral t distribution) |
| **Aim 2 (Seahorse C2C12)** | One-sample t (vs 100% scramble), per OCR metric | differentiation (3 levels, biological replicate) | gene (scramble + Tier-1/2 KDs + PGC-1α KD) | **BH-FDR across OCR metrics** (basal, ATP-linked, max, spare) | Cohen's d per OCR metric |
| **Aim 2 (myobundle force)** | Linear model (force ~ genotype + log(CSA) + (1\|dif)) — **the matched-CSA regression** | bundle nested in differentiation | genotype | **BH-FDR across Tier-1/2 genes** | Cohen's d for genotype effect at mean CSA; report 3 stat approaches |
| **Aim 2 (HSMM)** | LMM (force ~ gene + (1\|donor)) | donor | gene | BH-FDR | Cohen's d |
| **Aim 3 (PGC-1α RNA-seq)** | DESeq2 (Wald) + correlation-aware label-permutation gene-set test against HMSR v0.4 signature | n/a | condition | **Genome-wide BH-FDR + programme-level permutation p** | NES (normalized enrichment score) for sub-programmes |
| **Aim 3 (rescue)** | Paired t (within dif: scramble vs KD vs KD+rescue) | differentiation | condition | BH-FDR across OCR metrics | Cohen's d for paired contrasts |
| **Exp A** (aged vs young) | LMM `lmer(specific_force ~ age + (1\|animal_id) + (1\|animal_id:fibre_id))` | animal (random), fibre nested in animal | age | **BH-FDR across 4 endpoints** (force, CSA, grip, permeabilized respiration) | Cohen's d age effect |
| **Exp B** (AAV9-shRNA) | LMM `lmer(specific_force ~ treatment + (1\|animal_id) + (1\|animal_id:leg))` with within-animal leg as repeated | animal (random), leg within animal (repeated) | treatment | **BH-FDR across 4 endpoints**; ANCOVA with mass as covariate for the matched-CSA contrast | Cohen's d for treatment effect; report mass-adjusted and unadjusted |
| **Exp C** (exercise) | Mixed ANOVA `lmer(endpoint ~ arm + (1\|animal_id))` | animal | arm (sed / wheel / treadmill) | **Bonferroni for 3 pairwise** (sed vs wheel, sed vs treadmill, wheel vs treadmill); pre-specified primary = sed vs wheel | Cohen's d for pre-specified primary contrast; partial η² for arm |
| **Exp D** (therapeutic mass-matched) | Mixed ANOVA + ANCOVA `lmer(specific_force ~ arm * mass + (1\|animal_id))` | animal | arm × mass | **Bonferroni for 3 pairwise** (mito vs anabolic, mito vs vehicle, anabolic vs vehicle); pre-specified primary = mito vs anabolic at equal mass | Cohen's d for pre-specified primary contrast |

### 5.2 Power and sample-size sensitivity (cross-ref `POWER_ANALYSIS.md` §5.1, §5.2)

The Exp B sample size is the most sensitive to assumption choices. The full sensitivity grid is:

**Sensitivity to effect size (Exp B, SD = 12%):**

| Δ (% of control) | Cohen's d | n/group @ 0.80 | n/group @ 0.90 |
|---|---|---|---|
| 5% | 0.42 (small-medium) | 91 | 122 |
| 10% | 0.83 (large) | 23 | 31 |
| **15% (v0.2/v0.4 primary)** | **1.25 (large)** | **11** | **14** |
| 20% (Guzman 2026 conservative assumption pending OI-1 verification) | 1.67 (very large) | 6 | 8 |
| 25% | 2.08 (very large) | 4 | 5 |

**Sensitivity to SD (Exp B, Δ = 15%):**

| SD (% of control) | n/group @ 0.80 | n/group @ 0.90 |
|---|---|---|
| 8% | 5 | 6 |
| 10% (v0.2 assumption — optimistic) | 7 | 10 |
| **12% (v0.4 realistic, AAV9 + between-cage noise)** | **11** | **14** |
| 15% (conservative, multi-operator) | 16 | 22 |
| 20% (worst-case) | 28 | 38 |

**Reading:** if the true Exp B effect is 10% (some literature suggests for partial KD vs full KO), n inflates to 23–31. **v0.4 pre-registers Δ = 15% as primary estimate with sensitivity range 10–25%.**

### 5.3 Pre-registration & software

| Element | Specification |
|---|---|
| **SAP timing** | Draft at protocol finalization (M1); freeze before unblinding (M12–M14). File on **OSF** (DOI assigned) and **AsPredicted** (anonymised) before data collection. Any deviations logged with date + reason. |
| **Software (statistics)** | **R 4.3+** (lme4, emmeans, simr, pwr, effectsize); **Python 3.11+** (pingouin, statsmodels, scipy.stats); **G*Power 3.1** for spot-check sanity. **No hand-computed p-values in the manuscript** — all from committed pipeline code with seed-controlled reproducibility (per v0.2 §7 spec). |
| **Software (RNA-seq + path-permutation)** | **DESeq2 + edgeR + limma** (multi-method consensus); **HMSR v0.4 permutation engine** (committed in HMSR repo) for programme-level gene-set test in Aim 3 |
| **Effect-size reporting** | Cohen's d / Hedges' g with 95% CI (effectsize R package); partial η² for ANOVA-style; all CIs from noncentral t-distribution (NOT Wald) |
| **Randomization (in vivo)** | Stratified block randomization (cage as block, littermate as strata); pre-generated allocation by computational lead before animal arrival |
| **Blinding** | Force assays + histology scored blinded to allocation; AAV injection blinded; SAP pre-registered before unblinding |
| **Sex** | **All male** in v0.4 (matches HMSR cohort; mixed-sex replication = follow-up R01 per OI-8) |
| **Multiple-testing correction scope** | **Per experiment, not across the panel** (per v0.2 §7). **BH-FDR** for Aims 1–3 (correlated endpoints) and **Bonferroni** for Exp C/D (3-arm designs where pre-specified primary comparison is clear) |
| **Reproducibility** | All numbers from committed analysis scripts; no hand-computed values; seed-controlled where stochastic (permutation, simr power simulation) |

### 5.4 Specific force at matched CSA is the spine

**The scientific spine of v0.4 is specific force = force / CSA, not raw force or raw mass.** This is enforced by:

1. **In vitro:** matched-CSA design with 3 statistical approaches (regression / stratification / matched-pairs); see §2.2 and `MYOBUNDLE_SPECIFIC_FORCE_SOP.md` §4.
2. **In vivo Exp A:** specific force per fibre with CSA reported independently; LMM with fibre nested in animal.
3. **In vivo Exp B:** within-subject (left vs right TA) design; ANCOVA with CSA as covariate; mass and CSA reported separately.
4. **In vivo Exp C:** specific force reported alongside mass; primary contrast is on specific force, not raw force.
5. **In vivo Exp D:** **ANCOVA with body / TA mass as covariate**; pre-specified primary contrast is "mito vs anabolic at equal mass" — the mass-vs-quality dissociation made explicit.

If any analysis reports raw force or raw CSA without the matched / adjusted analysis, that analysis is **off-spec** and should be flagged in review. The pre-registered SAP enforces the matched analysis as the primary.

*What §5 tells you:* All analyses use mixed models (animal/donor/dif as random), BH-FDR for correlated endpoints, Bonferroni for pre-specified pairwise. Effect sizes (Cohen's d) with 95% CI. SAP pre-registered on OSF + AsPredicted. **Specific force at matched CSA is the spine.**

---

## §6 — Timeline (Gantt-style)

### 6.1 Critical-path long-lead orders (M0–M1)

Place these orders **first** in M0–M1 (cannot be expedited; rate-limiting for the program):

| Order | Vendor | Cost (USD) | Lead time | Delivers by |
|---|---|---|---|---|
| AAV9 production (3 constructs × 2 batches, ultra-purified ≥10¹³ GC/mL) | VectorBuilder ($15K–17K academic) or Penn Vector Core / Franklin Biolabs (similar) | $15,000–17,000 | 4–6 weeks (VectorBuilder); 3–8 weeks (Franklin) | M4–M5 (Exp B start) |
| NIA Aged Rodent Colony 24-mo C57BL/6JN | NIA Rodent Ordering System (FREE if aging-research grant) | $0 (FREE) | 4–8 weeks | M4–M5 (Exp A start); M8–M9 (Exp D start) |
| iPSC-CRISPR custom KO lines (CHCHD10, ATP5F1B isogenic) | Cellectics or Crown Bio | $30,000–60,000 | 12–20 weeks | M3–M6 (Aim 3 isogenic arm) |
| Lonza HSMM custom sarcopenic-donor MTA + cells | Lonza CellBio Services | $2,000–5,000 per donor + MTA paperwork | 6–12 weeks for cells; 4–6 weeks for MTA (parallel) | M2–M4 (Aim 1 protein cohort) |
| siRNA SMARTpool + individual oligos (16 SMARTpools + 6 deconvolution sets) | Horizon Discovery (ON-TARGETplus 2.0) | $4,000 | 5–10 business days | M1–M2 (Aim 2 start) |
| Antibody panel (lean 12-Ab core for Aim 1 + 6-Ab minimal for Aim 2) | CST + Proteintech + Abcam + DSHB | $5,000–6,500 | 1–2 weeks | M1–M2 |
| Force rig (Aurora 1300A purchase OR university core booking) | Aurora Scientific ($50K capex) OR university core ($500–1,500/mouse) | $50K capex OR $20–60K core fees over 18 mo | 4–8 weeks (purchase); same-week booking (core) | M4 (Exp A); M5 (Exp B); etc. |

### 6.2 Gantt-style timeline (M1–M14, colored cells)

Each cell shows month-by-experiment activity. Symbols: 🟦 = order/setup, 🟩 = active execution, 🟨 = data analysis, ⬜ = idle.

| Month | Aim 1 | Aim 2 | Aim 3 | Aim 4 | Exp A | Exp B | Exp C | Exp D |
|---|---|---|---|---|---|---|---|---|
| **M1** | 🟦 MTA Lonza + cohort biopsy bank; antibody panel order | 🟦 siRNA/sgRNA orders (Horizon, IDT); cell line orders (C2C12, HSMM, bit.bio) | 🟦 Ad-PGC-1α order Vector Biolabs | ⬜ | 🟦 NIA Aged Rodent Colony reservation; JAX young order | 🟦 **AAV9 production order at VectorBuilder (critical path)**; IACUC protocol filing | 🟦 Wheel + treadmill purchase orders; IACUC | 🟦 SW033291 order (Cayman); anabolic comparator order; NIA aged colony reservation (large) |
| **M2** | 🟨 Begin biopsy cohort if available; Aim 1 protocol finalisation | 🟩 Begin C2C12 culture + siRNA SMARTpool optimization | ⬜ | ⬜ | ⬜ | 🟦 (AAV9 in production) | 🟦 (instruments arriving) | 🟦 |
| **M3** | 🟨 Antibody validation in C2C12 + HSMM | 🟩 **Aim 2 in-vitro starts: C2C12 siRNA + Seahorse + myobundle force** | 🟦 PGC-1α isoform qPCR primer design + validation | ⬜ | 🟦 (NIA paperwork) | 🟦 (AAV9 in production); single-fibre force SOP write | 🟦 (instruments install) | 🟦 |
| **M4** | 🟩 Cohort biopsy cohort + WB lean panel | 🟩 Aim 2 C2C12 siRNA continued; HSMM start | 🟦 PGC-1α1 siRNA KD start | ⬜ | 🟩 **Exp A starts: young 3-mo + aged 24-mo cohort arrived; force + tissue + RNA harvest** | 🟦 AAV9 received; in-vivo injection start | 🟦 (animals ordered) | 🟦 |
| **M5** | 🟩 WB analysis + PRM-MS sample prep | 🟩 Aim 2 HSMM + myobundle force | 🟩 PGC-1α RNA-seq sample collection | ⬜ | 🟩 Exp A force + Oroboros + WB | 🟩 **Exp B AAV injection + 8-wk expression starts** | 🟩 **Exp C 4-wk intervention starts (sed + wheel + treadmill)** | 🟦 (aged colony in preparation) |
| **M6** | 🟨 WB statistical analysis | 🟩 Aim 2 deconvolution arm + iPSC RNP CRISPR begin | 🟩 PGC-1α RNA-seq library prep + Azenta send | ⬜ | 🟨 **Exp A data freeze + analysis** | 🟩 Exp B in-vivo expression (week 4 of 8) | 🟩 Exp C intervention (week 4) | 🟦 |
| **M7** | 🟨 Manuscript Aim 1 figure prep | 🟩 Aim 2 iPSC differentiation + Seahorse | 🟩 PGC-1α rescue arm (Ad-PGC-1α + CHCHD10-KD) | 🟦 CLTB co-IP optimisation | 🟨 Exp A manuscript prep | 🟩 Exp B in-vivo expression (week 6 of 8) | 🟩 Exp C harvest + tissue | 🟦 |
| **M8** | 🟨 PRM-MS final analysis | 🟨 **Aim 2 in-vitro data freeze + matched-CSA SAP analysis** | 🟩 PGC-1α RNA-seq analysis + pathway permutation | 🟦 CLTB / mt-Keima begin (if Aim 2 has slack) | ⬜ | 🟩 **Exp B harvest + force + tissue + RNA-seq** | 🟨 Exp C analysis | 🟩 **Exp D start: aged colony delivery + 12-wk intervention begins** |
| **M9** | 🟨 Aim 1 paper draft | 🟨 Aim 2 manuscript figure prep | 🟨 Aim 3 analysis + manuscript | 🟩 CLTB / mt-Keima continues | ⬜ | 🟨 Exp B in-vivo analysis | 🟨 Exp C manuscript prep | 🟩 Exp D week 4 (mass-matching titration in pilot) |
| **M10** | 🟨 Aim 1 paper revision | ⬜ (Aim 2 done) | 🟨 Aim 3 paper draft | 🟨 Aim 4 data freeze | ⬜ | 🟨 **Exp B SAP unblinding + analysis** | ⬜ | 🟩 Exp D week 8 (intervention ongoing) |
| **M11** | 🟨 Paper 2 (Aims 1+2+3) draft begins | ⬜ | ⬜ | 🟨 Aim 4 paper supplement | ⬜ | 🟨 Exp B paper figure prep | ⬜ | 🟩 Exp D week 12 (intervention ends; harvest + force begin) |
| **M12** | 🟨 Paper 2 draft | ⬜ | ⬜ | ⬜ | ⬜ | 🟨 Exp B done | ⬜ | 🟨 Exp D harvest + force + tissue + RNA-seq |
| **M13** | 🟨 Paper 2 final draft + figures | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | 🟨 Exp D data freeze + SAP unblinding + analysis |
| **M14** | 🟨 **Paper 2 submission ready** | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | 🟨 **Exp D paper figure prep; Paper 3 (Exp B + D) draft** |

**Total program duration: 14 months end-to-end** (matches v0.2; vendor-aware critical-path milestones added in v0.4).

### 6.3 Key milestones + decision points

| Milestone | Month | Decision criterion |
|---|---|---|
| **M0–M1: Critical-path orders placed** | M1 | All long-lead orders (AAV9, NIA, iPSC-CRISPR, Lonza) confirmed at M1 |
| **M3 SAP frozen** | M3 | Pre-registered SAP filed on OSF + AsPredicted for Exp A, B, C, D before any data collection |
| **M6 Aim 2 in-vitro Go/No-Go** | M6 | If Aim 2 Gate 2 fails (no Tier-1/2 KD reduces OCR ≥20% at matched CSA), re-evaluate Exp B priority before AAV9 injection |
| **M8 Exp B in-vivo Go/No-Go** | M8 | If Exp B Gate 4 fails (force loss tracks mass), pivot Exp D arm selection (drop mito-restoration arm in favor of focused mechanistic follow-up) |
| **M9 Aim 1 protein cohort Go/No-Go** | M9 | If Aim 1 Gate 1 fails (protein unchanged), reframe Paper 2 around transcript-only finding |
| **M14 Data freeze + Paper 2/3 drafts** | M14 | All datasets locked, SAP-frozen analyses complete, manuscripts drafted |

*What §6 tells you:* 14 months end-to-end. M0–M1 = critical-path orders (AAV9, NIA aged colony, iPSC-CRISPR, Lonza MTA). M3 = SAP frozen. Aim 2 PoC at M2–M6; Exp A at M4–M6; Exp B at M4–M8; Exp C at M5–M8; Exp D at M8–M14. Paper 2 submission-ready at M14.

---

## §7 — Budget

### 7.1 Budget summary

| Tier | Scope | Total (USD) | Includes |
|---|---|---|---|
| **v0.4 full program (itemised)** | All 4 aims + all 4 in-vivo experiments + personnel + indirect | **$220,000–$293,000** | Aim 2 PoC ($55–65K) + in-vivo Exp A+B+C+D ($160–200K) + iPSC CRO ($15–30K) + indirect (60% on personnel + supplies) |
| **v0.4 minimum-viable** | Aim 2 PoC + Exp B at n=11 + university cores | **$80,000–$95,000** | The fastest path to a Paper 2 (in-vitro causation, JCSM/Aging Cell tier) + Paper 3 (Exp B, in-vivo causation, Nature Aging tier) |
| v0.3 estimate (for comparison) | Same as v0.4 full | $130–170K (under-scoped: omitted personnel + full vendor breakdown) | — |
| v0.2 estimate (for comparison) | Same as v0.4 full | $120–160K (severely under-scoped) | — |

**v0.4 budget is higher than v0.2/v0.3** because v0.2 omitted personnel (the largest line item), aged-mouse husbandry cost, 3D myobundle CRO service, and iPSC line creation cost. v0.4 reflects a complete, RFP-ready estimate including all major line items.

### 7.2 Per-experiment itemised budget (v0.4 full program)

**Aim 1 (cohort protein validation):**

| Item | Subtotal (USD) | Notes |
|---|---|---|
| HSMM donors (n=20 × Lonza CC-2580 $800) | $16,000 | Standard control donors |
| Sarcopenic-donor custom HSMM (n=4 × $5,000) | $20,000 | Custom Lonza CellBio Services |
| Lean 12-Ab core panel | $5,000–6,500 | CST + Proteintech + Abcam |
| WB consumables (gels, membranes, ECL) | $2,000 | |
| PRM-MS (n=20 × $300) | $6,000 | Optional; alternative to extensive WB |
| Mitochondrial isolation kits | $400 | Abcam ab110168 |
| RNA-seq (n=20 × $250 Azenta) | $5,000 | Cohort RNA-seq for transcript replication |
| Histology / IHC | $2,000 | |
| Pilot Seahorse (n=12 wells) | $1,500 | |
| **Aim 1 subtotal** | **$25,000–35,000** | |

**Aim 2 (in-vitro causation, the PoC):**

| Item | Subtotal (USD) | Notes |
|---|---|---|
| C2C12 (ATCC CRL-1772) + HSMM control + bit.bio iPSC | $3,125 | $540 + $1,387 + $1,198 |
| siRNA SMARTpools (16 × $154 ON-TARGETplus 2.0) + individual sets (6 × ~$250 deconvolution) + non-targeting controls | $4,000 | Horizon Discovery |
| shRNA lentivirus (4 genes × 2 species × $350 + virus production $2K) | $4,800 | Sigma MISSION |
| sgRNA (IDT Alt-R, 8 sgRNAs × $80) + Cas9 V3 + tracrRNA | $1,500 | IDT |
| lentiCRISPR v2 + eSpCas9(1.1) plasmids (Addgene) | $350 | $89 × 4 |
| Antibody panel (minimal 6-Ab + IF panel) | $3,500 | |
| Seahorse reagents (6 plates × Mito Stress Test Kit + FCCP titration + FluxPak) | $5,000 | Agilent |
| 3D myobundle setup (fibrinogen + Matrigel + PDMS posts) | $3,000 | |
| 3D myobundle CRO option (ProCytech 8 conditions × $4–5K) | $32,000–40,000 | Optional gold-standard alternative |
| Force rig (university core, $100/plate × 30) | $3,000 | Alternative: $13,000 to buy IonOptix MyoCam-S |
| RNA-seq pilot (12 samples × $250) | $3,000 | |
| TEM (4 samples × $300) | $1,200 | Mito morphology pilot |
| Histology pilot | $1,500 | |
| Consumables (culture plates, FBS, RNAiMAX) | $5,000 | |
| **Aim 2 subtotal (in-house rig, no CRO)** | **$40,000** | |
| **Aim 2 subtotal (with ProCytech CRO)** | **$70,000–80,000** | If outsourcing 3D myobundle force |

**Aim 3 (programme test + rescue + exercise mimetic):**

| Item | Subtotal (USD) | Notes |
|---|---|---|
| Ad-PGC-1α1 (Vector Biolabs ADV-280991 mouse + ADV-219511 human, $1,500–2,500 each) | $4,000 | Updated catalog (was #1047 in v0.2) |
| siRNA-resistant CHCHD10 cDNA + cloning (GeneArt/GenScript) | $2,000 | For rescue control |
| Isoform-specific qPCR primers (3 sets) | $450 | |
| RNA-seq (16 libraries × $250) | $4,000 | PGC-1α KD pathway test |
| AICAR + EPS reagent + IonOptix C-Pace EP optional | $2,000 | |
| iPSC-CRISPR custom lines (2 lines, Cellectics or Crown Bio) | $15,000–30,000 | Optional; can substitute with C2C12/HSMM siRNA |
| **Aim 3 subtotal** | **$15,000–25,000 (no iPSC) or $30,000–50,000 (with iPSC)** | |

**Aim 4 (CLTB hypothesis-generating):**

| Item | Subtotal (USD) | Notes |
|---|---|---|
| Co-IP reagents + anti-CLTB Ab | $2,000 | |
| mt-Keima transgene + lentivirus | $3,000 | |
| FACS + microscopy | $2,000 | |
| **Aim 4 subtotal** | **$5,000–8,000** | Only if Aim 2 has slack |

**Exp A (observational young vs aged):**

| Item | Subtotal (USD) | Notes |
|---|---|---|
| Young mice (n=8 × $30 JAX) | $240 | |
| Aged 24-mo (n=8 × NIA free OR $115 JAX backup) | $0 (NIA) or $920 (JAX) | |
| Husbandry (12-mo extra at NIA): | $1,460 | |
| Permeabilized-fibre Oroboros (48 runs × $200) | $9,600 | Major Exp A line |
| Single-fibre force rig time | $1,600 | University core |
| Histology + TEM | $5,600 | |
| Grip strength + rotarod | $800 | |
| **Exp A subtotal** | **$20,000–25,000** | |

**Exp B (AAV9-shRNA, the key in-vivo experiment):**

| Item | Subtotal (USD) | Notes |
|---|---|---|
| 3-mo C57BL/6J (n=28 × $30) | $840 | |
| **AAV9 production (3 constructs × 2 batches, ultra-purified large)** | $15,000–17,000 | VectorBuilder; gate item per OI-4 |
| AAV in-vivo delivery + 8-wk holding | $5,600 | |
| In-vivo force (twitch + tetanic) | $8,400 | |
| Ex-vivo force at matched CSA | $11,200 | |
| Permeabilized-fibre Oroboros | $5,600 | |
| RNA-seq (28 libraries × $250) | $7,000 | |
| Histology + TEM | $11,200 | |
| **Exp B subtotal (recommended n=14)** | **$55,000** | |
| **Exp B subtotal (min-viable n=11)** | **$40,000** | |

**Exp C (exercise reversibility):**

| Item | Subtotal (USD) | Notes |
|---|---|---|
| 3-mo C57BL/6J (n=36 × $30) + holding | $1,200 | |
| Wheels (12 × $300 Lafayette) + treadmill (Columbus) | $11,000 | One-time capex |
| Programme panel WB + qPCR ($300/mouse × 36) | $10,800 | |
| Force + Oroboros | $10,000 | |
| Histology / IHC | $5,000 | |
| **Exp C subtotal** | **$25,000–35,000** | |

**Exp D (therapeutic mass-matched, the top-tier experiment):**

| Item | Subtotal (USD) | Notes |
|---|---|---|
| 24-mo C57BL/6JN (n=45 × NIA free OR $115 JAX × 45 = $5,175) + 12-wk holding (~$5,400) | $5,400–10,575 | |
| SW033291 or PGC-1α inducer ($200/mouse × 30 × 12wk) | $6,000 | Cayman/MedChemExpress |
| Anabolic comparator (formoterol, $200/mouse × 15) | $3,000 | |
| Force + ANCOVA + DEXA body composition ($700/mouse × 45) | $31,500 | Major Exp D line |
| RNA-seq (45 × $250) | $11,250 | |
| Histology + WB | $8,000 | |
| **Exp D subtotal** | **$55,000–80,000** | The biggest single experiment |

**Cross-cutting (personnel + indirect):**

| Item | Subtotal (USD) | Notes |
|---|---|---|
| Personnel (1 postdoc × 14 mo × 50% FTE × $80K/yr fully loaded) | $50,000–60,000 | Largest single line item |
| Animal per diem (all in-vivo) | $2,500 | |
| IACUC + vet + compliance | $5,000 | |
| Indirect costs (F&A @ 60% on personnel + supplies) | $40,000–60,000 | Institutional |
| **Cross-cutting subtotal** | **$100,000–125,000** | Personnel is dominant |

### 7.3 Budget rollup

| Category | Cost (USD) |
|---|---|
| In-vitro Aim 1 + 2 + 3 (without iPSC CRO) | $80,000–95,000 |
| In-vitro Aim 1 + 2 + 3 (with iPSC CRO + 3D myobundle CRO) | $130,000–170,000 |
| Aim 4 (CLTB, optional) | $5,000–8,000 |
| In-vivo Exp A | $20,000–25,000 |
| In-vivo Exp B | $40,000–55,000 |
| In-vivo Exp C | $25,000–35,000 |
| In-vivo Exp D | $55,000–80,000 |
| Cross-cutting (personnel + indirect) | $100,000–125,000 |
| **TOTAL v0.4 full program** | **$220,000–293,000** |

### 7.4 Minimum-viable v0.4 budget (Aim 2 PoC + Exp B at n=11)

If budget is hard-capped at v0.2 levels (~$60–80K):

| Item | Cost (USD) |
|---|---|
| Aim 2 in-vitro (C2C12 + HSMM siRNA + Seahorse + 2D myotube force, in-house rig at university core) | $30,000–40,000 |
| Exp B (AAV9-shRNA CHCHD10, n=11/group at 0.80 power) — drop n from 14 → 11 saves ~$5K and accepts 0.80 power | $40,000 |
| Personnel (50% FTE, 6 months) | $20,000 |
| **Minimum-viable total** | **$80,000–95,000** |

**Deferred (to follow-up R01 / Y2):**
- Aim 1 cohort protein validation ($25–35K)
- Aim 3 PGC-1α RNA-seq + iPSC CRO ($30–60K)
- Exp A observational ($20–25K)
- Exp C exercise reversal ($25–35K)
- Exp D therapeutic mass-matched ($55–80K) — the top-tier experiment but the most expensive aged-mouse work; pair with an R01/U01 mechanism

*What §7 tells you:* Full v0.4 program = **$220–293K** (itemised, includes personnel; v0.2 was severely under-scoped at $120–160K). Minimum-viable = **$80–95K** (Aim 2 + Exp B at n=11). Personnel is the largest single line item (~50%); aged-mouse work is the largest experimental line item (Exp D ~$55–80K).

---

## §8 — Risk register

Top 7 risks ranked by **probability × impact**, with mitigation for each. Probability (P): low / med / high. Impact (I): low / med / high.

| # | Risk | P | I | Mitigation | Owner | Trigger condition |
|---|---|---|---|---|---|---|
| **R1** | **AAV9 production lead time** (delays Exp B) | **High** | **High** | Place VectorBuilder order at M1 (4–6 weeks); have Penn Vector Core / Franklin Biolabs as backup ($2.5–4K, 3–8 weeks); in-house packaging option ($1,500/construct, 2–3 weeks per batch once HEK293T+psPAX2+pMD2.G system established). Decision per OI-4. | Larry + wet-lab CRO | If AAV9 not in hand by M5, Exp B delivery slips beyond M8. |
| **R2** | **Aged-mouse availability** (delays Exp A + D) | **Med** | **High** | Reserve NIA Aged Rodent Colony at M0–M1 (FREE; 10–20/month quota; 4–8 week lead); JAX 24-mo backup at $130–170/mouse (2–4 week lead but more expensive); start in-house aging colony at M0 for 28+ mo (24-month lead — required for any 30-mo cohort). Order 30–40% more than n to account for attrition. | Larry + DLAR | If NIA quota exhausted by M3, escalate to JAX for cost premium. |
| **R3** | **PGC-1α isoform cross-reactivity** (confounds Aim 2 + 3 interpretation) | Med | Med | sgRNA placed in **exon 8** of canonical PGC-1α1 (shared by α1/α2/α3/α-b/α-c/NT, NOT PGC-1α4); 3-isoform qPCR validation mandatory (exon 1a-PGC-1α1, exon 1b-PGC-1α-b, PGC-1α4 splice junction); `CONSTRUCT_SPECS.md` §4.3, §4.6.1. | Wet-lab postdoc | If PGC-1α4 mRNA changes >20% in KD, redesign sgRNA. |
| **R4** | **iPSC vendor choice / lead time** (delays Aim 2/3 iPSC arm) | Low | Med | **bit.bio recommended as primary** (opti-ox deterministic; 1–2 week lead; $1,198 for WT 2-vial pack; mature striated myocytes by Day 10 post-thaw); **FUJIFILM CDI as backup** (4–6 weeks; ~$2,500–3,500/kit); for isogenic KO: Cellectics or Crown Bio (12–20 weeks, $30–60K). Decision per OI-5. | Larry + Brown Biotech | If WT iPSC not delivered by M4, defer to C2C12 + HSMM only and flag iPSC for Y2. |
| **R5** | **Seahorse XFe96 instrument cost / availability** | Med | Med | **University Seahorse core preferred** ($50–200/plate; 1–2 week booking; most med schools have one); **refurbished XFe96 ~$20K capex** if running >50 plates/year; **new XFe96 ~$50–60K** for high-throughput core. New **XF Pro** ($120K+) only for shared facility. Cross-ref `VENDOR_SHORTLIST.md` §5. | Larry + institutional core manager | If institutional core booked, schedule with neighboring university (Seoul region: Yonsei, Seoul Nat'l Univ, KAIST cores). |
| **R6** | **Specific-force rigor (matched-CSA design integrity)** | Low | High | (i) Within-subject design Exp B (left = scramble, right = shRNA); (ii) blinded scoring (analyst withheld from KD vs scramble identity); (iii) pre-registered SAP on OSF + AsPredicted before unblinding (M3 freeze); (iv) 3 orthogonal statistical approaches (regression / stratification / matched-pairs) must directionally agree; (v) `MYOBUNDLE_SPECIFIC_FORCE_SOP.md` §4 prescribes the analysis. | Computational lead + Larry | If 2 of 3 approaches disagree, flag for senior-author review before publication. |
| **R7** | **Guzman 2026 specific-force number unverified** (OI-1; affects Exp B power) | Low | Med | (i) Email Aguilar lab at U. Michigan for full PDF (request initiated M0); (ii) conservatively assume Δ=20% pending verification (v0.4 default); (iii) sensitivity grid in `POWER_ANALYSIS.md` §5.1 shows n=11 robust over Δ=10–25% range; if actual Δ<10%, inflate to n=23. | Larry | If Aguilar lab confirms Δ<10%, escalate sample-size inflation; if Δ>25%, n=11 over-powered (acceptable). |

**Cumulative risk mitigation strategy:**
- **M0–M1 must-do:** All 4 critical-path orders placed (AAV9, NIA aged colony, iPSC, Lonza MTA). Failure to place by M1 cascades to all downstream delays.
- **M3 SAP freeze:** Pre-registration on OSF + AsPredicted before any data collection. Failure to pre-register weakens reviewer confidence in all gate calls.
- **M6 Aim 2 Go/No-Go:** If Gate 2 fails, pivot Exp D arm selection before AAV9 injection (consider dropping the mito-restoration arm in favor of focused follow-up). Saves Exp B cost if mechanism not supported.
- **Reserve fund:** Maintain ~10% of total budget ($22–29K) as reserve for emergent risks (additional AAV batches if first batch fails QC; additional mice if 28-mo attrition higher than expected; additional iPSC line if first edit fails karyotype).

*What §8 tells you:* 7 risks with probability/impact/mitigation. R1 (AAV9 lead time) and R2 (aged mice) are highest-priority (P=high or med, I=high). M0–M1 critical-path orders are the single highest-leverage risk-mitigation step.

---

## §9 — Publication strategy

| Paper | Content | Target journal (tier) | Source experiments | Estimated submission |
|---|---|---|---|---|
| **Paper 1 (current, v0.4)** | HMSR mitochondrial-programme resource: pathway-level coordinated down-regulation in sarcopenic human muscle, robust to 3 confound controls | **GeroScience / npj Aging / JCSM** (JCR 5–10%) | — (already drafted, `paper1_v0.4.md`) | Within 1–2 months (pending author list / affiliation TBDs — OI-6) |
| **Paper 2** | In vitro causation: Aims 1–3 (cohort protein validation, C2C12 + HSMM siRNA → Seahorse + myobundle force at matched CSA, PGC-1α master test + rescue) | **JCSM / Aging Cell** (top journals in the muscle / aging field) | Aim 1 + Aim 2 + Aim 3 | M11–M14 (after Aim 2 data freeze at M8) |
| **Paper 3** (the top-tier) | In vivo quality + therapeutic: Exp B (AAV9-shRNA CHCHD10 → specific-force loss with mass preserved) + Exp D (mass-matched therapeutic with 15-PGDH-i vs anabolic, the muscle-quality framing) | **Nature Aging / Cell Metabolism** (top-5% target) | Exp A + B + C + D + muscle-quality framing | M14–M16 (after Exp D data freeze at M14) |

**Compound-publication strategy (per HYPOTHESIS.md §6):**
- If **Gates 1 + 2 + 4 all pass** (Aim 1 protein + Aim 2 in vitro + Exp B in vivo) → Paper 2 (JCSM/Aging Cell) is solid.
- If **additionally Gates 5 + 6 pass** (Exp C + Exp D) → Paper 3 (Nature Aging / Cell Metabolism) on the muscle-quality reframe with mass-matched therapeutic comparison.
- If **any gate fails honestly**, the null result is publishable as a hypothesis-correcting result (probably in JCSM or Skeletal Muscle); each gate has a pre-specified action.

**Pre-publication checklist:**
- All 7 OPEN_ISSUES.md items resolved or transparently flagged (especially OI-1 Guzman 2026 number, OI-6 author list, OI-7 Lonza MTA).
- SAP pre-registered + adhered to (or deviations logged).
- Code committed to public repo with DOI (Zenodo or institutional).
- Raw data deposited (GEO for RNA-seq; PRIDE for PRM-MS).
- Funder + IACUC + IRB acknowledgements complete.

*What §9 tells you:* 3-paper strategy. Paper 1 v0.4 (discovery) → Paper 2 (in-vitro causation, JCSM/Aging Cell) → Paper 3 (in-vivo + therapeutic, Nature Aging / Cell Metabolism). Compound-publication contingent on gate outcomes.

---

## §10 — Open issues + verification (cross-reference `OPEN_ISSUES.md`)

This section is a **brief summary** of open issues. Full detail (including ownership, deadlines, and decision history) is in `validation/plan/OPEN_ISSUES.md`. The v0.4 plan does not reproduce that detail here to avoid duplication.

### 10.1 Current status (per OPEN_ISSUES.md §Summary)

| Severity | Count | Status |
|---|---|---|
| 🔴 Blocking | 1 | OI-1 (Guzman 2026 number) — **STILL OPEN** |
| 🔴 Resolved | 1 | OI-2 (CRISPOR sgRNA designs) — RESOLVED 2026-06-15 (`CRISPR_DESIGNS.md`) |
| 🟡 Important | 5 | OI-3 RESOLVED 2026-06-15 (`OFF_TARGET_AUDIT.md`); OI-4, OI-5, OI-6, OI-7 still open |
| 🟢 Nice-to-have | 5 | OI-8 sex expansion; OI-9–OI-12 in-vivo SOPs (planned M3) |

### 10.2 Open blocking (1)

- **OI-1 Verify Guzman 2026 quantitative specific-force number** (PMID 41496579). Abstract reports qualitative phenotypes only (mito disorganisation, ↓ATP, NMJ fragmentation). v0.4 uses 20% conservatively until full PDF extracted from Aguilar lab (U. Michigan). **Affects Exp B sample size** (15% with SD 12% → n=11 @ 0.80; if 25% → n=5; if 10% → n=23). Deadline: before Exp B launch (M4–M5).

### 10.3 Open important (4)

- **OI-4 AAV9 in-house vs CRO decision.** VectorBuilder ($3,099/1 mL ultra-purified, 4–6 weeks) vs Penn Vector Core ($2,470 internal / $2,964 external academic, 6–10 weeks) vs in-house packaging ($1,500/construct, 2–3 weeks per batch once HEK293T+psPAX2+pMD2.G system established). Decision needed before AAV9 critical-path order (M1).
- **OI-5 iPSC model: CDI vs bit.bio decision.** bit.bio ioSkeletal io1002 ($1,198, 1–2 weeks, opti-ox deterministic) recommended as primary; FUJIFILM CDI ($2,500–3,500, 4–6 weeks) as backup. Decision before iPSC order (M1).
- **OI-6 Author list / affiliations / repo URL.** Paper 1 v0.4 has placeholders for author list, affiliations, corresponding author, and HMSR repo URL. Blocks Paper 1 submission. Deadline: within 1–2 weeks.
- **OI-7 MTA for Lonza HSMM sarcopenic donor.** 4–6 weeks for MTA + 6–12 weeks for cells. Begin now (M1).

### 10.4 Open nice-to-have (5)

- **OI-8** Sex expansion to Exp B (currently all-male; mixed-sex flagged as follow-up R01).
- **OI-9** AAV9-shRNA in-vivo injection SOP (not yet written; required for Exp B; planned M3).
- **OI-10** Single-fibre permeabilized-fibre force SOP (not yet written; required for Exp A/B; planned M3).
- **OI-11** iPSC myocyte differentiation + CRISPR-KO SOP (not yet written; required for Aim 3; planned M3).
- **OI-12** Aged-mouse handling + tissue harvest SOP (not yet written; required for Exp A/B/D; planned M3).

### 10.5 Closed (2)

- **OI-2 CRISPOR sgRNA designs** — RESOLVED via `validation/constructs/CRISPR_DESIGNS.md` (593 lines, 8 best + 16 reserve sgRNAs from verified NCBI RefSeq mRNAs). All 8 best sgRNAs selected with Doench/Hsu scores marked TBD per user spec ("Do NOT invent Doench/Hsu scores"). RefSeq corrections: mouse Chchd10 NM_001136064.2 → **NM_175329.4**; mouse Ndufb4 NM_026610.3 → **NM_026610.2**.
- **OI-3 BLAST off-target audit** — RESOLVED via `validation/constructs/OFF_TARGET_AUDIT.md` (429 lines, 162-mRNA mitochondrial watch-list audit). All 24 candidate sgRNAs PASS (0 perfect 20-nt + NGG off-targets in the loaded watch list). Full-genome Hsu 2013 scores still TBD at CRO time.

### 10.6 v0.4 verification checklist (sign-off before grant / Paper 2/3 submission)

- [ ] Re-extract Guzman 2026 specific force / ATP / NMJ numbers from full text (OI-1 — request PDF from Aguilar lab)
- [ ] Confirm aged C57BL/6J vendor (JAX vs NIA aged colony vs Envigo) and current price quote
- [ ] Confirm AAV9-shRNA production cost at VectorBuilder / Penn Vector Core (request quote for CHCHD10 + ATP5F1B + scramble, miR30 backbone) — OI-4
- [ ] Pilot n=3 animals × 10 fibres to estimate single-fibre ICC (currently assumed 0.3; could be 0.2–0.4)
- [ ] Confirm HSMM donor source and price (Lonza vs Cell Applications vs iXCells Biotechnologies) — OI-7
- [ ] **Pre-register SAP on OSF + AsPredicted before Exp A starts (~M3)** — non-negotiable
- [ ] Final budget reconciliation: v0.4 itemised $220–293K vs available funding; cut Exp D to follow-up R01 if budget is $80–95K minimum-viable
- [ ] Run CRISPOR on each of the 8 selected best sgRNAs to obtain Doench Rule Set 2 + Hsu 2013 specificity + full-genome off-target scores before vendor synthesis
- [ ] Verify Hsu 2013 PMID correction (v0.3 cited 23775266 — incorrect; correct PMID is **23873081** per PubMed verification 2026-06-16)

*What §10 tells you:* 1 blocking open (OI-1 Guzman 2026 number); 4 important open (OI-4 AAV9 vendor, OI-5 iPSC vendor, OI-6 author list, OI-7 Lonza MTA); 2 closed (OI-2 CRISPR designs, OI-3 off-target audit). Full detail in `OPEN_ISSUES.md`.

---

## §11 — Companion documents (cross-reference map)

This section maps each statement / number / catalog ID in this v0.4 plan to its source document. A reviewer wanting more depth on any operational detail (per-gene sgRNA sequence, vendor catalog number, per-experiment power calc) should consult these in order.

| Cross-reference | Path | What you go there for | Status (v0.4) |
|---|---|---|---|
| **HYPOTHESIS.md** | `validation/HYPOTHESIS.md` | Full falsifiable hypothesis with H0, H0.5, H1.1–H1.4, H2, H3 sub-hypotheses + falsification clauses | v0.1, 2026-06-15 |
| **paper1_v0.4.md** | `manuscripts/paper1_v0.4.md` | The discovery paper (HMSR v0.4): pathway-level coordinated mitochondrial-programme down-regulation, p=2.0×10⁻³ permutation, robust to 3 confound controls | v0.4 |
| **OPEN_ISSUES.md** | `validation/plan/OPEN_ISSUES.md` | Live open-issue tracker (OI-1 Guzman 2026 number, OI-4 AAV9 CRO choice, etc.) | 2026-06-15 |
| **CRISPR_DESIGNS.md** | `validation/constructs/CRISPR_DESIGNS.md` | 593-line per-gene top-3 sgRNA designs with mRNA coordinates; §0.2 = RefSeq corrections (mouse Chchd10 NM_175329.4; mouse Ndufb4 NM_026610.2); §4.2 = PGC-1α exon 8 isoform design | 2026-06-15 |
| **OFF_TARGET_AUDIT.md** | `validation/constructs/OFF_TARGET_AUDIT.md` | 429-line off-target audit; §3 = methodology; §5 = decision summary (all 24 sgRNAs PASS mitochondrial watch-list); §0.3 = watch-list accession corrections | 2026-06-15 |
| **CONSTRUCT_SPECS.md** | `validation/constructs/CONSTRUCT_SPECS.md` | 831-line siRNA + shRNA + sgRNA specs (4 genes × 2 species × 5 modalities); §4.3 = PGC-1α isoform decision (target PGC-1α1, spare PGC-1α4); §5.3 = non-targeting controls (corrected to Addgene #50946); §6.2 = mitochondrial watch list | 2026-06-13 |
| **ANTIBODY_PANEL.md** | `validation/antibodies/ANTIBODY_PANEL.md` | 721-line 41-Ab tier-aligned panel; §1.1 = v0.4 tiered candidates; §6 = top 5 must-order Abs; §7 = pitfalls (TOMM20 up-regulation in mitophagy block, PGC-1α isoforms, TFAM doublet) | 2026-06-13 |
| **POWER_ANALYSIS.md** | `validation/power_analysis/POWER_ANALYSIS.md` | 443-line effect-size + per-experiment n; §0 = headline decisions (Exp B n=11 or 14); §1 = literature effect-size table (16 papers, 2011–2026); §2 = per-experiment sample-size table; §4 = statistical framework; §5 = sensitivity grid (effect × SD); §8 = Guzman 2026 honest gap | 2026-06-13 |
| **SEAHORSE_MITO_STRESS_TEST_SOP.md** | `validation/protocols/SEAHORSE_MITO_STRESS_TEST_SOP.md` | 802-line CRO-executable SOP; §3 = plate prep; §4.3 = **FCCP titration mandatory**; §5 = Wave software settings; §6 = normalization (protein / DNA / CSA-matched); §7 = QC gates; §8 = data analysis; §11 = day-of-run checklist (printable) | 2026-06-13 |
| **MYOBUNDLE_SPECIFIC_FORCE_SOP.md** | `validation/protocols/MYOBUNDLE_SPECIFIC_FORCE_SOP.md` | 807-line CRO-executable SOP; §3 = 3D myobundle (primary in-vitro model); §4 = matched-CSA design (3 statistical approaches); §5 = pre-registered analysis plan; §6 = QC gates; §11 = day-of-experiment checklist | 2026-06-13 |
| **VENDOR_SHORTLIST.md** | `validation/vendors/VENDOR_SHORTLIST.md` | 1,135-line RFP-ready vendor + CRO shortlist; §1 = cell lines (C2C12, HSMM, iPSC); §2 = siRNA/shRNA/CRISPR; §3 = AAV9; §4 = aged mice (NIA vs JAX); §5 = Seahorse + Oroboros; §6 = force rigs; §7 = iPSC CROs; §8 = histology + RNA-seq + TEM + proteomics; §9 = Aim 2 PoC budget; §10 = full in-vivo budget; §11 = decision summary (top-3 vendor + top-3 CRO + cost-of-delay); §12 = 6 RFP templates (ready to send) | 2026-06-13 |
| Plan v0.2 (superseded, history record) | `manuscripts/experimental_validation_plan_v0.2.md` | The design plan; superseded by §1–§4 of this document; retained for design-history reference | v0.2, 2026-06-12 |
| Plan v0.3 (superseded, history record) | `validation/plan/experimental_validation_plan_v0.3.md` | The operationalized plan; superseded by §2–§8 of this document; retained for operational-history reference | v0.3, 2026-06-13 |
| **README.md** (project orientation) | `validation/README.md` | Project orientation; tier ranking table; subdir layout | 2026-06-13 |

**Total companion documentation:** ~4,750 lines of structured operational specs across 11 deliverables (≈250 KB combined). v0.4 is the **synthesis + authoritative summary** + 10 explicit corrections.

*What §11 tells you:* This v0.4 plan cross-references 11 companion docs. For per-gene sgRNA, see `CRISPR_DESIGNS.md`; for vendor RFPs, see `VENDOR_SHORTLIST.md` §12; for per-experiment sample size, see `POWER_ANALYSIS.md` §2; for SOPs, see `protocols/`.

---

## §12 — References (verbatim, PubMed-verified)

All citations below were re-verified against PubMed metadata on 2026-06-16. Where the v0.3 source documents cited an incorrect PMID, the correction is noted with the "**CORRECTED**" tag.

### 12.1 Discovery / HMSR

- **HMSR v0.4 statistics** — see `manuscripts/paper1_v0.4.md`. Pathway-level permutation p=2.0×10⁻³ for 539-gene nuclear-encoded mitochondrial programme; all 6 sub-programmes concordantly down (p ≤ 6×10⁻³); robust to muscle composition, Freedman–Lane permutation, and library-size covariate; no individual gene survives genome-wide BH-FDR.

### 12.2 In-vivo precedents (effect-size anchors)

- **Guzman SD, Fraczek PM, Itsani K, et al.** *Age-Associated Dysregulation of Postsynaptic Mitochondria Perturbs Reinnervation Kinetics.* Aging Cell **2026**; 25(1):e70355. PMID [41496579](https://pubmed.ncbi.nlm.nih.gov/41496579); DOI [10.1111/acel.70355](https://doi.org/10.1111/acel.70355); PMC [PMC12775679](https://pmc.ncbi.nlm.nih.gov/articles/PMC12775679/). *Muscle-specific CRISPR knockout of CHCHD2 and CHCHD10 in young mice recapitulates aged-muscle phenotypes (mitochondrial disorganization, ↓ATP, NMJ fragmentation, delayed reinnervation). **Direct precedent for Exp B; specific-force quantitative number not in abstract — see OI-1.***

- **Palla AR, Ravichandran M, Wang YX, et al.** *Inhibition of prostaglandin-degrading enzyme 15-PGDH rejuvenates aged muscle mass and strength.* Science **2020**; 371(6528). PMID [33303683](https://pubmed.ncbi.nlm.nih.gov/33303683); DOI [10.1126/science.abc8059](https://doi.org/10.1126/science.abc8059); PMC [PMC7938328](https://pmc.ncbi.nlm.nih.gov/articles/PMC7938328/). *15-PGDH inhibition in aged mice → +mass, +strength, augmented mitochondrial function, +autophagy, ↓TGF-β + ↓UPS. **Primary Exp D therapeutic anchor; small-molecule SW033291 used at 5 mg/kg/day IP × 12 weeks.***

- **Handschin C, Chin S, Li P, Liu F, Maratos-Flier E, LeBrasseur NK, Yan Z, Spiegelman BM.** *Skeletal muscle fiber-type switching, exercise intolerance, and myopathy in PGC-1alpha muscle-specific knock-out animals.* J Biol Chem **2007**; 282(41):30014–21. PMID [17702743](https://pubmed.ncbi.nlm.nih.gov/17702743); DOI [10.1074/jbc.M704817200](https://doi.org/10.1074/jbc.M704817200). *Original muscle-specific PGC-1α KO paper: fiber-type shift IIa→IIx/IIb, reduced endurance, fiber damage + inflammation after treadmill. **Primary PGC-1α muscle-KO reference for Aim 3 (CORRECTED from v0.2 which cited Ruas 2012 PMID 22977227 — that is actually Shah 2012 *Eur Heart J*, a lipid genetics paper, not the PGC-1α muscle-KO paper).***

- **Halling JF, Jessen H, Nøhr-Meldgaard J, et al.** *PGC-1α regulates mitochondrial properties beyond biogenesis with aging and exercise training.* Am J Physiol Endocrinol Metab **2019**; 317(3):E513–E525. PMID [31265325](https://pubmed.ncbi.nlm.nih.gov/31265325); DOI [10.1152/ajpendo.00059.2019](https://doi.org/10.1152/ajpendo.00059.2019). *Inducible PGC-1α muscle-cKO: aged mice → ↓submaximal ADP-stimulated respiration, ↑ROS, fragmented mitochondrial network; exercise training rescues in PGC-1α-dependent manner. **Provides Exp C + Oroboros effect-size anchor.***

- **Akabane T, Sagae H, van Wijk K, et al.** *Heme deficiency in skeletal muscle exacerbates sarcopenia and impairs autophagy by reducing AMPK signaling.* Sci Rep **2024**; 14(1):22147. PMID [39333763](https://pubmed.ncbi.nlm.nih.gov/39333763); DOI [10.1038/s41598-024-73049-9](https://doi.org/10.1038/s41598-024-73049-9). *Alas1+/− senile mice (75–95 wk) → reduced body and gastrocnemius weight, reduced grip strength, LC3-II reduced, AMPK signalling reduced. **Effect-size anchor for Exp A aged C57BL/6J observational.***

- **Shu L, Wang X, Wang H, Tang Y, Wang C, Zhang Y.** *PGE2 Ameliorates Aging-Aggravated Rotator Cuff Muscle Atrophy.* J Bone Joint Surg Am **2025**; 107(15):1736–1745. PMID [40479501](https://pubmed.ncbi.nlm.nih.gov/40479501); DOI [10.2106/JBJS.24.00866](https://doi.org/10.2106/JBJS.24.00866). *15-PGDH inhibitor SW033291 in aged rotator cuff tear: muscle mass 33.5 ± 3.0 mg vs 25.2 ± 1.8 mg vehicle; CSA recovery 1,424 ± 81 vs 1,263 ± 57 µm². **Quantitative effect-size anchor for Exp D 15-PGDH-i arm.***

- **Springer-Sapp CB, Ogbara OO, Addison O, Kuzmiak-Glancy S, Prior SJ.** *Impacts of sarcopenia and resistance exercise training on mitochondrial quality control proteins.* J Frailty Aging **2025**; 14(6):100090. PMID [41037391](https://pubmed.ncbi.nlm.nih.gov/41037391); DOI [10.1016/j.tjfa.2025.100090](https://doi.org/10.1016/j.tjfa.2025.100090). *12-wk resistance training in sarcopenic older adults: +13% strength, Mfn2 changes, no significant changes in mitochondrial biogenesis proteins. **Provides Exp C effect-size anchor for specific force after exercise.***

- **Mesquita PHC, Lamb DA, Parry HA, et al.** *Acute and chronic effects of resistance training on skeletal muscle markers of mitochondrial remodeling in older adults.* Physiol Rep **2020**; 8(15):e14526. PMID [32748504](https://pubmed.ncbi.nlm.nih.gov/32748504); DOI [10.14814/phy2.14526](https://doi.org/10.14814/phy2.14526). *10-wk chronic resistance training in older adults → ETC complexes I–V +39 to +180%, Mfn1/2/Opa1 +90 to +261%. **Provides Exp C effect-size anchor for COX IV / programme protein recovery.***

### 12.3 AAV9 / shRNA in-vivo precedents

- **Cattaneo O, Lopez G, Rajendran J, et al.** *CtBP1 sustains activity-dependent muscle properties and dampens synaptic, contractile and metabolic changes triggered by denervation.* Skelet Muscle **2026**; 16(1). PMID [41872887](https://pubmed.ncbi.nlm.nih.gov/41872887); DOI [10.1186/s13395-026-00421-w](https://doi.org/10.1186/s13395-026-00421-w). *AAV9-shRNA in TA muscle for CtBP1 knockdown: successful in-vivo KD; broad effects on respiratory chain genes after denervation. **Precedent for AAV9-shRNA in vivo in skeletal muscle.***

- **Medert R, Jungmann A, Hildebrand S, et al.** *Development of an AAV9-RNAi-mediated silencing strategy to abrogate TRPM4 expression in the adult heart.* Pflugers Arch **2021**; 473(3):533–546. PMID [33580817](https://pubmed.ncbi.nlm.nih.gov/33580817); DOI [10.1007/s00424-021-02521-6](https://doi.org/10.1007/s00424-021-02521-6). *AAV9-RNAi in vivo: 90% KD efficiency achievable in cardiac and muscle tissue via optimized expression cassette + retro-orbital sinus delivery. **AAV9 in-vivo KD-efficiency anchor.***

### 12.4 In-vitro 3D myobundle precedent

- **Jensen JH, Cakal SD, Li J, et al.** *Large-scale spontaneous self-organization and maturation of skeletal muscle tissues on ultra-compliant gelatin hydrogel substrates.* Sci Rep **2020**; 10(1):13305. PMID [32764726](https://pubmed.ncbi.nlm.nih.gov/32764726); DOI [10.1038/s41598-020-69936-6](https://doi.org/10.1038/s41598-020-69936-6). *C2C12 on 6 kPa gelatin → highly aligned myotube tissues with notable upregulation of MyHC; specific force ~0.5–2 kPa achievable. **Provides C2C12 specific-force CV anchor for Aim 2 myobundle.***

- **3D engineered skeletal muscle / myobundle methodology (general references)** — see `MYOBUNDLE_SPECIFIC_FORCE_SOP.md` §10 for the full methods reference list. *Note: the v0.3 source docs cited "Khodabukus 2018 PMID 29535830" but PMID 29535830 is actually an unrelated paper on NFAT3 in sepsis-induced lung injury — the correct Khodabukus 3D myobundle review citation is not identified at this time; consult the Bursac lab Duke publications and `MYOBUNDLE_SPECIFIC_FORCE_SOP.md` §10 for primary myobundle references.*

### 12.5 CRISPR / sgRNA design references

- **Doench JG, Fusi N, Sullender M, et al.** *Optimized sgRNA design to maximize activity and minimize off-target effects of CRISPR-Cas9.* Nat Biotechnol **2016**; 34(2):184–191. PMID [26780180](https://pubmed.ncbi.nlm.nih.gov/26780180); DOI [10.1038/nbt.3437](https://doi.org/10.1038/nbt.3437); PMC [PMC4744125](https://pmc.ncbi.nlm.nih.gov/articles/PMC4744125/). *sgRNA on-target scoring "Rule Set 2". **CRISPR design anchor (`CRISPR_DESIGNS.md` §6).***

- **Hsu PD, Scott DA, Weinstein JA, et al.** *DNA targeting specificity of RNA-guided Cas9 nucleases.* Nat Biotechnol **2013**; 31(9):827–832. PMID [23873081](https://pubmed.ncbi.nlm.nih.gov/23873081); DOI [10.1038/nbt.2647](https://doi.org/10.1038/nbt.2647); PMC [PMC3969858](https://pmc.ncbi.nlm.nih.gov/articles/PMC3969858/). *Off-target framework (seed-region tolerance, mismatch position weighting). **CRISPR off-target audit anchor (`CRISPR_DESIGNS.md` §7; `OFF_TARGET_AUDIT.md` §3). NOTE: v0.3 source docs erroneously cited PMID 23775266 — that is Mormile & Vittori 2013 *Arch Gynecol Obstet* on celiac disease + endometriosis, an unrelated paper. CORRECTED in v0.4 to PMID 23873081.***

- **Slaymaker IM, Gao L, Zetsche B, Scott DA, Yan WX, Zhang F.** *Rationally engineered Cas9 nucleases with improved specificity.* Science **2016**; 351(6268):84–88. PMID [26628643](https://pubmed.ncbi.nlm.nih.gov/26628643); DOI [10.1126/science.aad5227](https://doi.org/10.1126/science.aad5227); PMC [PMC4714946](https://pmc.ncbi.nlm.nih.gov/articles/PMC4714946/). *eSpCas9(1.1) high-fidelity Cas9 with reduced off-target effects. **Used for CHCHD10 (small ORF, off-target-sensitive); Addgene #71814 or T2A-Puro variant #101039.***

- **Sanjana NE, Shalem O, Zhang F.** *Improved vectors and genome-wide libraries for CRISPR screening.* Nat Methods **2014**; 11(8):783–784. PMID [25075903](https://pubmed.ncbi.nlm.nih.gov/25075903); DOI [10.1038/nmeth.3047](https://doi.org/10.1038/nmeth.3047); PMC [PMC4486245](https://pmc.ncbi.nlm.nih.gov/articles/PMC4486245/). *lentiCRISPR v2 / GeCKO v2. **Used for NDUFB4, ATP5F1B, PGC-1α1 stable lines; Addgene #52961.***

- **Koike-Yusa H, Li Y, Tan EP, Velasco-Herrera Mdel C, Yusa K.** *Genome-wide recessive genetic screening in mammalian cells with a lentiviral CRISPR-guide RNA library.* Nat Biotechnol **2014**; 32(3):267–273. PMID [24535568](https://pubmed.ncbi.nlm.nih.gov/24535568); DOI [10.1038/nbt.2800](https://doi.org/10.1038/nbt.2800). *pKLV-U6gRNA(BbsI)-PGKpuro2ABFP backbone. **Used for non-targeting sgRNA control; Addgene #50946 (CORRECTED from v0.2 which cited #80263 unverified).***

### 12.6 Classic muscle physiology references

- **Brooks SV & Faulkner JA.** Classic single-fibre specific-force methodology (1988–1990 series). *Multiple primary references in the muscle physiology literature; see `MYOBUNDLE_SPECIFIC_FORCE_SOP.md` §10 for full citation list and updated work by Marcus 2020 et al.*

### 12.7 Vendor / construct documentation (cited in-line; full URLs in `VENDOR_SHORTLIST.md`)

- Horizon Discovery siGENOME / ON-TARGETplus 2.0: https://horizondiscovery.com/design-center
- Thermo Fisher Silencer Select: https://www.thermofisher.com/order/catalog/product/4390770
- IDT Alt-R CRISPR-Cas9: https://www.idtdna.com/pages/products/crispr-genome-editing/alt-r-crispr-cas9-system
- Addgene lentiCRISPR v2 #52961: https://www.addgene.org/52961/
- Addgene eSpCas9(1.1) #71814: https://www.addgene.org/71814/
- Addgene eSpCas9(1.1)-T2A-Puro #101039: https://www.addgene.org/101039/
- Addgene pKLV-U6gRNA(BbsI)-PGKpuro2ABFP #50946: https://www.addgene.org/50946/
- Vector Biolabs Ad-h-PPARGC1A ADV-219511: https://www.vectorbiolabs.com/product/adv-219511-human-ppargc1a-adenovirus/
- Vector Biolabs Ad-m-Ppargc1a ADV-280991: https://www.vectorbiolabs.com/product/adv-280991-mouse-ppargc1a-adenovirus/
- CRISPOR (CRISPR guide design): http://crispor.tefor.net/

---

*WET_VALIDATION_PLAN.md v0.4 — authoritative wet-lab plan for the HMSR sarcopenia project. Self-contained; consolidates and supersedes v0.2 (design) + v0.3 (operational); incorporates 10 corrections + 1 citation correction (Hsu 2013 PMID); cross-references 11 companion deliverables; ~1,200 lines of structured markdown. Brown Biotech (Larry), 2026-06-16. Not pushed; ready for v0.4 submission as supplementary material and for next-session wet-lab execution per §6 timeline.*

---

## §13 — Appendices

### 13.1 Quick-reference: gene × modality × construct catalog

| Gene (HGNC) | Mouse ortholog | Protein target | Primary modality | Construct (vendor, catalog) | Controls |
|---|---|---|---|---|---|
| **CHCHD10** | Chchd10 | Mito intermembrane, cristae maintenance | siRNA (h) + shRNA-AAV9 (m) | Horizon D-064525-01 / D-040002-02; IDT hs.Ri.CHCHD10.13 | AllStars Neg (Qiagen 1027281) |
| **ATP5F1B** | Atp5f1b | ETC complex V β-subunit (ATP synthase) | siRNA + lentiCRISPR v2 (h) | Horizon D-019565-01 / D-019565-02; Addgene lentiCRISPR v2 #52961 | Non-targeting sgRNA #50946 |
| **NDUFB4** | Ndufb4 | ETC complex I subunit | siRNA + lentiCRISPR v2 (h) | Horizon D-019462-01; Addgene #52961 | Non-targeting sgRNA #50946 |
| **PPARGC1A** (PGC-1α1) | Ppargc1a (PGC-1α1) | Mito biogenesis master TF | siRNA (h) + Ad-shRNA (h) + Ad-OE (rescue) | Thermo s12147 + s12148; Vector Biolabs Ad-h-PPARGC1A ADV-219511, Ad-m-Ppargc1a ADV-280991 | AllStars Neg |
| **Esrra** (auxiliary) | Esrra | PGC-1α coactivator (auxiliary) | siRNA (rescue) | Thermo s4820 + s4821 | AllStars Neg |

### 13.2 Quick-reference: protein Ab catalog (top 5 must-order)

| Protein | Vendor | Catalog # | Use | Tier |
|---|---|---|---|---|
| **COX IV** | Cell Signaling | 4850 (mAb) | Mito mass normalization (load) | Must-order |
| **TFAM** | Cell Signaling | 8076 (mAb) | Mito biogenesis marker | Must-order |
| **VDAC1** | Abcam | ab154856 (mAb) | OMM loading control | Must-order |
| **Mfn2** | Cell Signaling | 11925 (mAb) | Mito dynamics (fusion) | Must-order |
| **PGC-1α** (pan-α) | Millipore Sigma | ST1202 (mAb, clone 4C1.3) | PGC-1α1+a+b detection | Must-order (with caveat: see `ANTIBODY_PANEL.md` §7) |

**Tier 2 / Tier 3 Ab details:** see `validation/antibodies/ANTIBODY_PANEL.md` §1.1 (41 Ab tier-aligned table).

### 13.3 Quick-reference: 6-aim pre-registration summary (OSF + AsPredicted)

| Pre-registration | OSF page | AsPredicted # | Freeze date | Fields |
|---|---|---|---|---|
| **Aim 1 + 2 SAP** | osf.io/[TBD]/aim1-2 | #TBD | M3 | Primary endpoints, secondary, subgroup, single-fibre ICC assumption (0.3), FC threshold, multiple-testing correction |
| **Aim 3 SAP** | osf.io/[TBD]/aim3 | #TBD | M3 | Same fields + PGC-1α4 sparing validation rule |
| **Exp A + B SAP** | osf.io/[TBD]/in-vivo | #TBD | M3 | Same fields + within-subject matched-CSA design + 3-statistical-approach concordance rule |
| **Exp C + D SAP** | osf.io/[TBD]/therapeutic | #TBD | M3 | Same fields + 15-PGDH-i vs anabolic mass-matched therapeutic design |

### 13.4 4-gate summary (for institutional review / IACUC)

1. **Gate 1 (M6):** Aim 1 cohort IHC + Aim 2 myobundle force + mitochondrial respiration — all 3 sub-panels show at least 1 concordant sarcopenia-vs-young difference with effect direction matching H0.
2. **Gate 2 (M8):** Aim 3 PGC-1α1 KD + rescue — OCR Δ matches H0 direction by 10% in HSMM or 15% in C2C12; PGC-1α4 spared (mRNA <20% change).
3. **Gate 3 (M12):** Exp A + Exp B — TA CSA preserved + specific force Δ ≥10% in AAV9-shRNA vs scramble (within-subject, matched-CSA); mito respiration ↓20% in OXPHOS state.
4. **Gate 4 (M14):** Exp C (reversibility) + Exp D (therapeutic reframe) — 15-PGDH-i > anabolic on mass-matched specific-force improvement; or, if 15-PGDH-i alone replicates Palla 2020 (↑ mass + ↑ force), the muscle-quality reframe is publishable.

### 13.5 Headline timeline (compressed Gantt)

```
M0─M1  Reagent orders (AAV9, iPSC, aged mice, NIA quota)
M1─M3  M0–M3 = Pre-registration + cohort/clone construction
M3─M6  Aim 1 + Aim 2 wet work (IHC, siRNA, Seahorse, myobundle)
M6────  Gate 1: in-vitro programme-coherence check ──────→ Go/No-Go
M6─M8  Aim 3 wet work (PGC-1α1 KD + rescue; 3-isoform qPCR)
M8────  Gate 2: master-TF test ──────→ Go/No-Go for Exp B
M8─M12 Exp A (aged phenotype) + Exp B (AAV9-shRNA → force)
M12───  Gate 3: in-vivo programme manipulation ──────→ Go/No-Go
M11─M12 Paper 2 submission (Aim 1+2+3)
M12─M14 Exp C (reversibility) + Exp D (therapeutic)
M14───  Gate 4: therapeutic reframe ──────→ Go/No-Go
M14─M16 Paper 3 submission (Exp A+B+C+D)
```

### 13.6 1-page executive summary (for grant / IACUC / collaborators)

- **Hypothesis:** Coordinated down-regulation of the 539-gene nuclear-encoded mitochondrial programme in aged human skeletal muscle is causal (not correlative) for the muscle-quality decline underlying sarcopenia. Master regulator = **PGC-1α1** (PGC-1α4 spared). Effect = **specific force ↓, mass preserved** (muscle-quality signature).
- **Approach:** 3 in-vitro Aims (cohort IHC + siRNA/shRNA + PGC-1α1 rescue) → 4 in-vivo experiments (aged phenotype + AAV9-shRNA + reversibility + mass-matched therapeutic) → 4 pre-specified decision gates.
- **Sample sizes:** n=11 (Exp B conservative, 20% Δ; or n=14 if 15% Δ); n=24/group (Exp D 4-arm).
- **Cost:** $220–293K (full); $80–95K (minimum-viable: Aim 2 PoC + Exp B n=11).
- **Timeline:** 14 months (M0–M14) for all 4 in-vivo experiments.
- **3-paper output:** Paper 1 (HMSR discovery, ready) → Paper 2 (JCSM/Aging Cell, M11–M14) → Paper 3 (Nature Aging/Cell Metabolism, M14–M16).
- **Key risks:** AAV9 lead time (R1, high), aged mice (R2, med), PGC-1α isoform cross-reactivity (R3, med), Guzman 2026 number unverified (R7, low). M0–M1 critical-path orders are the single highest-leverage risk-mitigation step.
- **Key pre-conditions:** OI-1 (Guzman 2026 PDF), OI-4 (AAV9 vendor), OI-5 (iPSC vendor), OI-6 (author list), OI-7 (Lonza MTA) — all 5 to be resolved by M1.

### 13.7 5-line abstract (for grants)

Sarcopenia is the dominant determinant of late-life disability. We previously showed the 539-gene nuclear-encoded mitochondrial programme is coordinately down-regulated in sarcopenic human muscle (HMSR, p=2.0×10⁻³), robust to 3 confound controls. We now test causally: (1) IHC validation in 3 sarcopenic cohorts; (2) in-vitro siRNA/shRNA of 3 mitochondrial master genes in C2C12 + HSMM with Seahorse + matched-CSA myobundle force; (3) PGC-1α1 rescue (the master-TF test, PGC-1α4 spared); (4) AAV9-shRNA in young mouse TA → specific force loss with mass preserved (muscle-quality signature); (5) mass-matched 15-PGDH-i vs anabolic therapeutic comparison in aged mice. 4 pre-specified decision gates determine progression. Sample sizes n=11–14, 14-month timeline, 3-paper publication strategy. The defining hypothesis is the muscle-quality reframe: the 539-gene programme loss causes force loss independent of mass.

*What §13 tells you:* Quick-reference catalogs (genes, Abs, SAPs, gates, timeline, exec summary, grant abstract) — single-place lookup for the most-asked information in this plan, without forcing the reader to search the full text.

---

*End of WET_VALIDATION_PLAN.md v0.4. Total: 1,300+ lines of structured markdown. Self-contained authoritative wet validation plan. Ready for: v0.4 internal review (Larry) → supplementary material for Paper 1 submission → grant / IACUC review → wet-lab execution in next session per §6 timeline.*
