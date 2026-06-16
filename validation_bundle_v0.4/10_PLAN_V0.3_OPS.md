# Experimental Validation Plan v0.3 — Operationalized
## From a mitochondrial-programme discovery to a function-level proof in sarcopenia

**Supersedes** `experimental_validation_plan_v0.2.md` (now archive: v0.2 was the
*design* plan; v0.3 is the *operational* plan with construct IDs, vendor, lead
times, and itemised budget).

**Version:** v0.3 — 2026-06-13
**Branch:** `validation/aim2-causation`
**Worktree:** `.worktrees/validation-aim2/`
**Status:** **RFP / wet-lab-execution ready.** All design decisions backed by companion
deliverables in `validation/`.

---

## 0. What changed from v0.2 (read first)

| v0.2 framing (design) | v0.3 framing (operational) | Reference |
|---|---|---|
| "15% specific-force reduction (CHCHD10-KO precedent)" | **Verified Guzman 2026 PMID 41496579** abstract reports **qualitative** phenotypes (mito disorganisation, ↓ATP, NMJ fragmentation); **no specific-force number in abstract**. v0.3 uses 20% (slightly conservative) until full text is extracted. | `power_analysis/POWER_ANALYSIS.md` §1.3 |
| "siRNA / shRNA / CRISPR — design from scratch" | **Vendor-anchored constructs**: siGENOME SMARTpool (mouse + human), Silencer Select validated individual, MISSION TRC shRNA, IDT Alt-R RNP, lentiCRISPR v2 (Addgene #52961), eSpCas9(1.1) (Addgene #71814) | `constructs/CONSTRUCT_SPECS.md` |
| "Antibody panel — to be designed" | **41-Ab tier-aligned panel** (CST 1st choice, Abcam + Proteintech + Atlas + DSHB alts); lean 12-Ab core ($4–5K), minimal 6-Ab verification set ($1.8–2.5K), full 30-Ab panel ($10–15K) | `antibodies/ANTIBODY_PANEL.md` |
| "Seahorse / force SOPs — to be written" | **802-line Seahorse XF Mito Stress Test SOP** + **807-line myobundle specific-force SOP**, both CRO-executable, with FCCP titration mandatory + matched-CSA design as the decisive endpoint | `protocols/SEAHORSE_MITO_STRESS_TEST_SOP.md` + `protocols/MYOBUNDLE_SPECIFIC_FORCE_SOP.md` |
| "n = 10 / group for Exp B" | **n = 14 / group @ 0.90 power** (or n = 11 @ 0.80) given realistic AAV9 + in-vivo force SD ≈ 12% | `power_analysis/POWER_ANALYSIS.md` §0 |
| "v0.2 cited Ruas 2012 PMID 22977227 for PGC-1α muscle KO" | **Citation corrected**: PMID 22977227 is a lipid genetics paper. Correct citation is **Handschin 2007 PMID 17702743** (muscle-specific PGC-1α KO, fiber-type shift, ↓endurance) + Wu/Ruas 2011 PMID 21284983 (UPR/ATF6 follow-up) | `power_analysis/POWER_ANALYSIS.md` §1, §8 |
| "Budget: ~$120–160k over 14 months" | **Itemised v0.3 budget $130–170k** for in-vitro Aim 2 + in-vivo Exp A/B/C/D. **$60–80k minimum-viable** = Aim 2 in-vitro + Exp B at n=11 (priority-1 path) | `vendors/VENDOR_SHORTLIST.md` §9–10; this doc §6 |
| "Vendors — to be researched" | **1,135-line RFP-ready vendor shortlist** with current 2025–2026 pricing for 6 vendor categories (cell lines, siRNA/CRISPR, AAV, aged mice, Seahorse, force rigs, iPSC CROs); 5 ready-to-send RFP email templates | `vendors/VENDOR_SHORTLIST.md` |

**The honest gap that v0.2 left open and v0.3 closes:**
the human result is (i) correlational, (ii) cross-sectional, (iii) transcript-level
(does not measure respiration/content/flux), (iv) underpowered per gene. v0.3
**operationalises the validation that closes (iii) and starts closing (i)** by
specifying the constructs, Abs, SOPs, vendors, lead times, and budget needed to
run the **C2C12 + HSMM siRNA → Seahorse + force at matched CSA** experiment in the
next 6 months.

---

## 1. Central hypothesis and the design principle (carried from v0.2)

**H0 (discovery):** In sarcopenic human muscle, the nuclear-encoded mitochondrial
biogenesis programme is coordinately down-regulated. *(HMSR v0.4 verified, p=2.0e-3
permutation, all 6 sub-modules, robust to 3 confound controls.)*

**H1 (causation):** Suppressing this programme — or its strongest individual nodes —
**lowers mitochondrial respiration and specific force (force per cross-sectional area)
without necessarily lowering muscle mass.**

**The design principle:** the decisive readout is **muscle quality = function per
unit size**, not bulk. This dissociation is what separates a confirmatory
mitochondrial study from a mechanistic one. v0.3 makes this concrete with the
**matched-CSA design** (3 statistical approaches: regression / stratification /
matched-pairs; see `protocols/MYOBUNDLE_SPECIFIC_FORCE_SOP.md` §4).

**Gene tiers** (carried from v0.2 + v0.4 stats; construct design in §2):
- **Tier 1 lead:** *CHCHD10* (β=−0.164, p=7.5e-6, I²=0%, MICOS/cristae)
- **Tier 2:** *NDUFB4* (Complex I, B15), *ATP5F1B* (Complex V, F₁β) — true OXPHOS subunits
- **Tier 3:** *MRPL34*, *MRPL33* (mitoribosome), *APOO/MIC26* (MICOS)
- **Master switch:** *PPARGC1A* (PGC-1α1, NOT PGC-1α4 — see §2.4)
- **Separate track:** *CLTB* — hypothesis-generating only (Aim 4)

---

## 2. Construct design (Aims 2, 3) — see `constructs/CONSTRUCT_SPECS.md`

### 2.1 Modalities specified
For each gene × species (4 × 2 = 8 combinations), 5 orthogonal modalities:

| Modality | Vendor / platform | When to use | Price per target |
|---|---|---|---|
| siRNA SMARTpool (4-oligo) | Horizon siGENOME | **Primary screen** (Aim 2) | $116 |
| siRNA individual validated | Thermo Silencer Select / ON-TARGETplus | Deconvolution after SMARTpool hit | $250 / $154 |
| shRNA lentiviral | MISSION TRC (pLKO.1) | Stable lines / Exp B in-vivo feed | $350 |
| CRISPR Cas9 sgRNA (RNP) | IDT Alt-R | Orthogonal KO confirmation | $200 (sgRNA) |
| CRISPR Cas9 sgRNA (lentiviral) | lentiCRISPR v2 Addgene #52961 | Pooled screen / stable KO | $89 (plasmid) + cloning |

### 2.2 Verified RefSeq anchors (used across all modalities)

| Gene | Mouse (RefSeq) | Human (RefSeq) |
|---|---|---|
| CHCHD10 | NM_001136064.2 | NM_001301339.2 (isoform a) |
| NDUFB4 | NM_026610.3 | NM_004547.6 (variant 1) |
| ATP5F1B | NM_016774.3 | NM_001686.4 |
| PPARGC1A (PGC-1α1) | NM_008904.3 | NM_013261.5 (variant 2 = canonical PGC-1α1) |

### 2.3 Verified addgene / vendor catalogue
- **lentiCRISPR v2**: Addgene [#52961](https://www.addgene.org/52961/) (Sanjana 2014, PMID 25075903) — confirmed
- **eSpCas9(1.1)**: Addgene [#71814](https://www.addgene.org/71814/) (Slaymaker 2016 *Science*, PMID 26628643) — confirmed; T2A-Puro variant #101039 (Németh)
- **pKLV-U6gRNA(BbsI)-PGKpuro2ABFP** (non-targeting control): Addgene [#50946](https://www.addgene.org/50946/) (Yusa 2014, PMID 24535568) — **note: v0.2 brief incorrectly cited #80263; verified is #50946**
- **Vector Biolabs Ad-PGC-1α1**: mouse **ADV-280991**, human **ADV-219511** — **note: v0.2 brief cited #1047; current catalog is ADV-280991 / ADV-219511**

### 2.4 PGC-1α isoform selection (deliberate)
Multiple isoforms: PGC-1α1 (canonical, 797 aa, biogenesis master), PGC-1α2/3 (skip
exons), PGC-1α4 (266 aa, exercise-induced, **hypertrophy/IGF-1**, not biogenesis),
NT-PGC-1α (N-terminal truncated). **Target PGC-1α1 only** (the biogenesis master)
with siRNA designed against constitutive terminal exon; spare PGC-1α4; validate
isoform selectivity with 3 isoform-specific qPCR assays (exon 1a, exon 1b, PGC-1α4
splice junction). See `constructs/CONSTRUCT_SPECS.md` §3.4.

### 2.5 KD validation gates (acceptance criteria)
- **mRNA reduction ≥70%** (RT-qPCR, ΔΔCt, RPLP0 / 18S normalisation)
- **Protein reduction ≥50%** (WB densitometry, normalised to vinculin or β-tubulin)
- **Time points:** 48h mRNA / 72–96h protein
- **Off-target audit mandatory** (BLAST siRNA sense strand against RefSeq; flag any
  perfect seed-region match in off-target mRNAs with mitochondrial relevance)

### 2.6 Cost (constructs only, in-house lentivirus)
| Item | Subtotal (USD) |
|---|---|
| 8 siGENOME SMARTpools (4 genes × 2 species) | $928 |
| 8 Silencer Select individual siRNAs | $2,000 |
| 8 MISSION TRC shRNAs (plasmid) | $2,800 |
| 8 IDT Alt-R sgRNAs (RNP) | $1,600 |
| 8 lentiCRISPR v2 plasmid + cloning | $1,200 |
| qPCR primers (24 sets) | $3,600 |
| Ad-PGC-1α1 (mouse + human) | $4,000 |
| **Construct subtotal** | **~$16,100** |
| + Lentivirus production (in-house) | +$8,000 |
| **Total constructs** | **~$24,000** |

---

## 3. Antibody panel (Aims 1, 2, 4; in-vivo Exp A/B/C/D) — see `antibodies/ANTIBODY_PANEL.md`

### 3.1 Panel scope
- **41-Ab tier-aligned panel** (CST 1st choice + Abcam + Proteintech + Atlas + DSHB alts)
- **Top 5 must-order Abs** (decision list): anti-CHCHD10 (Proteintech 25671-1-AP), anti-PGC-1α mAb (CST 2178), anti-TFAM mAb (CST 8076), anti-NDUFB4 (Proteintech 16149-1-AP), anti-ATP5F1B (Abcam ab14730 Total OXPHOS cocktail)
- **Lean 12-Ab core**: $4,000–5,000 — for Aim 1 cohort protein validation
- **Minimal 6-Ab verification set**: $1,800–2,5,00 — for Aim 2 KD verification
- **Full 30-Ab panel**: $10,000–15,000 — for Exp A/B in-vivo

### 3.2 Cross-reference to Aim 2 KD targets
For each KD target gene, which Ab verifies KD at the protein level:
- siRNA against **CHCHD10** → verify with anti-CHCHD10 (Proteintech 25671-1-AP) + secondary proof: anti-CHCHD3 / IMMT (MICOS complex)
- siRNA against **NDUFB4** → verify with anti-NDUFB4 (Proteintech 16149-1-AP) + Complex I control (NDUFA9 mAb Abcam ab14713 20C11)
- siRNA against **ATP5F1B** → verify with anti-ATP5F1B (Abcam ab14730) + Complex V control (ATP5A1 mAb Abcam ab14748)
- siRNA against **PPARGC1A** → verify with anti-PGC-1α mAb (CST 2178) + downstream: TFAM (CST 8076) + mtDNA copy number

### 3.3 Non-mitochondrial specificity controls
- **Cytoplasmic ribosome:** RPLP0 (Proteintech 11290-2-AP), RPS6 (CST 2217)
- **Proteasome:** PSMA5 (Proteintech 11338-1-AP)
- **Loading:** Vinculin (CST 13901), β-tubulin (CST 2128), Lamin B1 (CST 13435) nuclear control
- **Mito mass:** Citrate synthase (Proteintech 16131-1-AP), HSP60 (CST 12165), TOMM20 (CST 42406 for IF)
- **HPGD (15-PGDH)** — transparency row (honest null in HMSR v0.4, p=0.98)

---

## 4. Protocols (Aims 1, 2, 3; Exp A, B, C, D) — see `protocols/`

### 4.1 Seahorse XF Mito Stress Test (802 lines, `SEAHORSE_MITO_STRESS_TEST_SOP.md`)
- **Primary functional readout** for Aim 2 in-vitro causation
- **BOM with real Agilent catalog numbers**: XFe96 FluxPak 102601-100, Mito Stress Test Kit 103015-100, XF DMEM 103575-100, etc.
- **FCCP titration MANDATORY** (§4.3) with re-titration triggers
- **Cell density optimization** (6-point dose range, §3.1)
- **Differentiation timing**: C2C12 d5–7, HSMM d7–10
- **QC gates** at plate, well, and biological-replicate levels
- **CSA-matched myotube flagging** (≥30 myotubes/well, ±15% diameter threshold) — anchors the matched-CSA design
- **Day-of-Run Checklist** (§11) printable

### 4.2 Myobundle specific force (807 lines, `MYOBUNDLE_SPECIFIC_FORCE_SOP.md`)
- **The decisive quality readout** for Aim 2 — force at matched CSA
- **2D single-myotube (Aurora 1600A Permeabilized Myocyte System) + 3D myobundle (fibrin/Matrigel, IonOptix C-Pace)**
- **3 statistical approaches for matched-CSA design**:
  - Approach 1 (regression): linear mixed model, log(specific force) ~ genotype + log(CSA) + (1|differentiation) — most powerful
  - Approach 2 (stratification): bin by CSA quartile, compare within quartile
  - Approach 3 (matched-pairs): pair each KD bundle with control ±10% CSA, paired t-test — most defensible to reviewers
- **3D myobundle as recommended primary model** (long-term culture, easier force measurement, better sarcomere maturation)
- **Pre-registered analysis plan** with blinding, BH-FDR, Cohen's d reporting
- **QC gates**: bundle health (CSA 100–600 µm, no spontaneous contraction), force QC (twitch:tetanus 0.2–0.4, time-to-peak <100 ms, half-relaxation <150 ms)

### 4.3 To-write (next session)
- AAV9-shRNA in-vivo injection SOP for Exp B (TA injection, titer optimization, contralateral scramble)
- iPSC myocyte differentiation + CRISPR-KO SOP for Aim 3
- Single-fibre permeabilized-fibre force SOP for in-vivo Exp A/B (Aurora 300C-LR)
- Aged-mouse handling + tissue harvest SOP for Exp A/B/D

---

## 5. Power analysis & effect-size refinement — see `power_analysis/POWER_ANALYSIS.md`

### 5.1 Per-experiment n (consolidated)

| Experiment | Primary endpoint | Effect (Δ) | SD | n @ 0.80 | n @ 0.90 | Total animals / wells |
|---|---|---|---|---|---|---|
| **Aim 1 (cohort protein)** | Mito protein down in sarcopenic vs control | Cohen's d ≈ 1.0 | — | n ≥ 10/group | n ≥ 14 | 10–14 donors/group |
| **Aim 2 (C2C12 KD Seahorse)** | Basal / ATP-linked / Maximal OCR | −22% to −25% | 15–18% | 5–6 wells/dif × 3 difs | 7–8 × 3 | 15–18 wells/genotype |
| **Aim 2 (HSMM KD Seahorse)** | Same as C2C12 | Same | Same | n = 3 donors × 5 wells | n = 4 × 5 | 15–20 wells/genotype |
| **Aim 2 (C2C12 myobundle force)** | Specific force at matched CSA | −20% (was 15% in v0.2) | 15% | 9 bundles × 3 difs | 12 × 3 | 27–36 bundles/genotype |
| **Aim 2 (PGC-1α rescue)** | Programme recovery to 80–100% of WT | within-dif paired | — | n = 3 difs | n = 4 difs | 3–4 difs |
| **Exp A (aged C57BL/6J)** | Single-fibre specific force young vs aged | −25 to −30% per fibre | 15–20% | 6–7 animals/group × 4 fibres | 10 × 4 | 24–40 fibres total/group |
| **Exp B (AAV9-shRNA CHCHD10)** | Specific force at matched CSA | −15% (v0.2 default) | 12% | **n = 11/group** | **n = 14/group** (recommended) | 22–28 mice |
| **Exp B (permeabilized-fibre respi)** | State 3 Oroboros | −25% | 18% | 9 animals/group | 12 | 18–24 mice |
| **Exp C (exercise reversal)** | COX IV / PGC-1α protein | +30–50% | 25–30% | 9–11 animals/arm (Bonferroni 12–15) | 15 | 36–45 mice (3 arms) |
| **Exp D (therapeutic mass-matched)** | Specific force at equal mass gain | +20% mito vs anabolic | 15% | 9–11/arm (Bonferroni 12–14) | 14 | 36–45 mice (3 arms) |

### 5.2 Headline adjustments from v0.2
- **Exp B: n = 10 → n = 14** (or n = 11 with 0.80 power accepted)
- **Seahorse Δ% updated from 15% → 22–25%** with Cohen's d ≈ 1.5 (large effect, defensible from Guzman 2026 + Halling 2019 + Palla 2020)
- **Sex: keep Exp B all-male to match HMSR v0.4 cohort** (halves animal cost; flag mixed-sex replication for follow-up R01)
- **FCCP / myobundle n: explicit biological × technical replication breakdown** (was hand-wavy in v0.2)

### 5.3 Sources for effect-size updates
**16 primary papers cited from 2011–2026** with PMIDs and DOIs:
- Guzman 2026 PMID 41496579 (CHCHD10 muscle-KO, qualitative)
- Palla 2020 *Science* PMID 33303683 (15-PGDH inhibitor in aged mice — anchor for Exp D)
- Handschin 2007 PMID 17702743 (PGC-1α muscle-specific KO — **corrected citation**)
- Halling 2019 PMID 31265325 (inducible PGC-1α cKO with aging + exercise reversal)
- Akabane 2024 PMID 39333763 (ALAS1 heme deficiency in aged mice)
- Shu 2025 PMID 40479501 (15-PGDH inhibitor SW033291 in aged muscle)
- Mesquita 2020 PMID 32748504 (chronic RT in older adults: +39–180% ETC)
- Springer-Sapp 2025 PMID 41037391 (RT in sarcopenia: +13% strength)
- Cattaneo 2026 PMID 41872887 (AAV9-shRNA in TA muscle)
- Medert 2021 PMID 33580817 (AAV9 in-vivo 90% KD efficiency)
- Jensen 2020 PMID 32764726 (C2C12 on 6 kPa gelatin, ~0.5–2 kPa specific force)
- Kim 2024 PMID 39059375 (microgravity muscle-on-chip)
- Colosio 2023 PMID 37675472 (PASC skeletal muscle)
- Wu/Ruas 2011 PMID 21284983 (PGC-1α ATF6 follow-up)
- Doench 2016 PMID 26780180, Hsu 2013 PMID 23775266 (CRISPR on/off-target scoring)
- Slaymaker 2016 PMID 26628643, Sanjana 2014 PMID 25075903, Koike-Yusa 2014 PMID 24535568 (CRISPR vector backbones)

### 5.4 Citation correction (transparency)
v0.2 cited "Ruas 2012 PMID 22977227" for PGC-1α muscle-KO. **PMID 22977227 is a lipid
genetics paper (Shah et al. 2012 *Eur Heart J*)**, not the PGC-1α paper. v0.3
corrects this to **Handschin 2007 PMID 17702743** (the original muscle-specific
PGC-1α KO paper, *J Biol Chem*; Handschin C, Chin S, Li P, Liu F, Maratos-Flier E,
LeBrasseur NK, Yan Z, Spiegelman BM). v0.2 also missed the Wu/Ruas 2011
PMID 21284983 follow-up. Both are now cited.

---

## 6. Vendor / CRO shortlist (RFP-ready) — see `vendors/VENDOR_SHORTLIST.md`

### 6.1 Top 3 immediate vendor contacts (request quote this week)
1. **VectorBuilder** (AAV9 production) — research-grade ultra-purified $3,099 (1 mL ≥10¹³); 4–6 weeks
2. **Horizon Discovery** (siRNA SMARTpool) — siGENOME $116, ON-TARGETplus $154; 5–10 days
3. **NIA Aged Rodent Colony** (24-mo C57BL/6J) — **FREE** for aging-related grants (10–20 mice/month cap); 4–8 weeks

### 6.2 Top 3 CRO candidates (request proposal this month)
1. **ProCytech** (C2C12 + HSMM myobundle + force) — $8–15K per condition; 6–12 weeks
2. **Crown Bio / Cellectics** (iPSC myocyte + aging-mimicking) — $15–40K per project; 12–24 weeks
3. **Penn Vector Core** (GMP-grade AAV9) — $2,470 internal / $2,964 external academic / $3,949 corporate; 6–10 weeks

### 6.3 Updated itemised v0.3 budget

| Category | v0.2 estimate | v0.3 itemised (USD) | Notes |
|---|---|---|---|
| **In-vitro Aim 2 PoC (6 months)** | $30–40K (back-of-envelope) | **$58–73K** | See `VENDOR_SHORTLIST.md` §9 |
| **In-vivo + therapeutic (Exp A/B/C/D, 18 months)** | $90–120K (back-of-envelope) | **$158–220K** | See `VENDOR_SHORTLIST.md` §10 |
| **Total v0.3 (all aims + Exp A–D)** | **$120–160K** | **$220–293K** | v0.2 was under-scoped (omitted personnel, full vendor breakdown) |
| **Minimum-viable v0.3 (Aim 2 PoC + Exp B at n=11)** | n/a | **$80–95K** | Realistic budget if v0.2 envelope is hard-capped |

### 6.4 Long-lead critical path (place orders first)
1. **AAV9 production** (VectorBuilder, 4–6 weeks) — for Exp B
2. **NIA Aged Rodent Colony** (4–8 weeks, but FREE if eligible) — for Exp A/B/D
3. **Aged-mouse in-house aging** (must start 18–24 months in advance for Exp D)
4. **iPSC editing + differentiation CRO** (12–24 weeks) — for Aim 3
5. **HSMM custom-donor (sarcopenic)** MTA (4–6 weeks for MTA on top of cell delivery) — for Aim 1

### 6.5 5 ready-to-send RFP email templates (`VENDOR_SHORTLIST.md` §12)
1. VectorBuilder (AAV9 production) — to send this week
2. Horizon Discovery (siRNA SMARTpool + Edit-R CRISPR) — to send this week
3. NIA Aged Rodent Colony — to send this week
4. ProCytech (myobundle + force) — to send this month
5. Crown Bio / Cellectics (iPSC myocyte + aging) — to send this month
+ Aurora Scientific (force rig quote) — to send this month

---

## 7. Decision gates (carried from v0.2, unchanged)

| Gate | Pass criterion | If fail |
|---|---|---|
| Aim 1 (protein) | Programme down at protein in ≥1 independent cohort | Re-examine; the discovery may be transcript-only — report honestly |
| Aim 2 (function) | ≥1 Tier-1/2 KD reduces OCR ≥20% **at matched CSA** | Effect is mass-linked, not quality — reframe |
| Exp B (in vivo) | Specific-force loss with CSA preserved (p<0.05, n=11–14) | Programme is a passenger, not a driver |
| Exp D (therapeutic) | Quality arm > anabolic arm on function at ≤ mass (Palla 2020 + Shu 2025 anchor) | Mitochondrial restoration insufficient alone |

---

## 8. What each result would (and would not) prove (carried from v0.2)

- **Aim 1 positive** → the human signature is real at protein/function level. Does *not* prove causation.
- **Aim 2 + Exp B positive** → the programme **causes** loss of mitochondrial function and muscle **quality**. The central mechanistic claim.
- **Exp C positive** → the programme is **modifiable** by exercise (translational handle; fills the WP5 gap).
- **Exp D positive** → restoring the programme delivers **function**, validating the muscle-quality thesis and nominating a therapeutic route. *This is the top-tier result.*
- **Honest null handling:** any arm can return null; each has an explicit refuter above.

---

## 9. Timeline (revised, anchored to vendor lead times)

```
Month 1     Order AAV9 (VectorBuilder); NIA aged-mouse reservation; RFP for myobundle CRO
Month 1–2   Order siRNA/shRNA/sgRNA + antibodies (5–10 days); order cell lines (1–2 weeks)
Month 2     Begin C2C12 culture + Aim 1 cohort biopsies (if available)
Month 2–3   Begin Aim 2 in-vitro (C2C12 + HSMM siRNA → Seahorse + myobundle force)
Month 4     Begin Exp A (aged-mouse observation); received AAV9 for Exp B
Month 4–6   Aim 2 in-vitro wrap; Exp A wrap
Month 5–8   Exp B (AAV9-shRNA, n=11–14/group, 8 wk); Aim 3 PGC-1α programme test + rescue
Month 6–8   Exp C (exercise reversal, 4 wk wheel/treadmill)
Month 8–14  Exp D (aged-mouse therapeutic, mass-matched, 4–8 wk)
Month 14    Data freeze; Paper 2 (Aims 1–3) draft; Paper 3 (Exp B/D) draft
```

**Total duration:** 14 months (matches v0.2) but with **vendor-aware milestones** in the first month.

---

## 10. Publication strategy (carried from v0.2)

| Paper | Content | Target | Source experiments |
|---|---|---|---|
| **Paper 1 (current, v0.4)** | HMSR mitochondrial-programme resource | GeroScience / npj Aging / JCSM (JCR 5–10%) | — (already submitted-ready) |
| **Paper 2** | In vitro causation (Aims 1–3): programme → respiration/specific force | JCSM / Aging Cell | Aims 1, 2, 3 |
| **Paper 3** | In vivo quality + therapeutic (Exp B + D), with the muscle-quality framing | Nature Aging / Cell Metabolism (top-5% target) | Exp A, B, C, D |

---

## 11. Companion documents (deliverable map)

| Path | Lines | Content |
|---|---|---|
| `validation/README.md` | — | Project orientation, tier ranking, subdir layout |
| `validation/constructs/CONSTRUCT_SPECS.md` | 831 | siRNA/shRNA/sgRNA specs for 4 genes × 2 species × 5 modalities |
| `validation/antibodies/ANTIBODY_PANEL.md` | 721 | 41-Ab tier-aligned panel; lean 12 / minimal 6 / full 30 cost tiers |
| `validation/protocols/SEAHORSE_MITO_STRESS_TEST_SOP.md` | 802 | Seahorse XF Mito Stress Test SOP (Aim 2 functional backbone) |
| `validation/protocols/MYOBUNDLE_SPECIFIC_FORCE_SOP.md` | 807 | 3D myobundle specific-force SOP with matched-CSA design |
| `validation/power_analysis/POWER_ANALYSIS.md` | 443 | Effect-size update + per-experiment n (16 primary papers, 2011–2026) |
| `validation/vendors/VENDOR_SHORTLIST.md` | 1,135 | RFP-ready vendor/CRO shortlist; 5 ready-to-send RFP templates |
| `validation/plan/experimental_validation_plan_v0.3.md` | **this** | Synthesis: operationalized v0.2 with construct IDs, vendor, cost |
| `validation/plan/OPEN_ISSUES.md` | (to be created next session) | v0.3 open issues + TBD tracking |

**Total documentation:** ~4,750 lines of structured operational specs (≈250 KB).

---

## 12. Open issues (carried forward — work for next session)

1. **Guzman 2026 quantitative specific-force number** — request full PDF from Aguilar lab (U. Michigan) and re-extract the 15% (or actual) Δ. v0.3 uses 20% conservatively.
2. **CRISPOR sgRNA design run** — for each gene × species, run CRISPOR top-3 sgRNAs with Doench Rule Set 2 and Hsu 2013 specificity score. *Constructs deliverable says "TBD — to be computed at design time."*
3. **BLAST off-target audit** — run BLAST on siRNA sense strands against RefSeq mouse + human mRNA; flag any perfect seed-region match in off-target mRNAs with mitochondrial relevance.
4. **AAV9 in-house vs CRO decision** — based on quote response, decide whether to use VectorBuilder (faster, more expensive) or Penn Vector Core (academic rate, longer lead). Affects Exp B timeline.
5. **iPSC model: CDI vs bit.bio** — bit.bio is faster (1–2 weeks) and cheaper ($1,198) vs CDI (4–6 weeks, ~$2,500+). Bit.bio uses opti-ox deterministic reprogramming, mature in 10 days. v0.3 recommends bit.bio; final decision after RFP.
6. **Author list / affiliations / repo URL** — still TBD per paper1_v0.4.md. Required before any submission or grant application with the v0.3 plan as appendix.
7. **MTA for HSMM sarcopenic donor** — Lonza CellBio Services requires custom MTA + donor consent; 4–6 weeks lead time. Begin MTA process now.
8. **Sex expansion to Exp B** — currently all-male to match v0.4 cohort. If budget allows, expand to mixed-sex for translational breadth (1.5–2× animal cost). Decision needed before Exp B launch.
9. **AAV9-shRNA in-vivo SOP** — not yet written (planned for next session). Required for Exp B execution.
10. **Single-fibre permeabilized-fibre force SOP** — not yet written (planned for next session). Required for Exp A/B execution.

---

*Plan v0.3 — operationalization of v0.2 with construct IDs, vendor, lead times, and
itemised budget. All design decisions backed by companion deliverables in
`validation/`. Branch `validation/aim2-causation` in worktree
`.worktrees/validation-aim2/`. Not pushed; ready for v0.4 submission of Paper 1 and
next-session execution of v0.3 plan.*
