# HMSR Aim 1 + Aim 2 — Mitochondrial Protein Antibody Panel Specification

> **Branch:** `validation/aim2-causation`
> **Worktree:** `.worktrees/validation-aim2/`
> **Document ID:** `validation/antibodies/ANTIBODY_PANEL.md` v0.1
> **Last updated:** 2026-06-13
> **Authors:** Larry (Brown Biotech AI partner) + HMSR protein-validation working group
> **Status:** Draft for ordering review (Aim 2 PoC cohort: 4 mAbs + 2 loading + 2 IF secondary = **lean 6-Ab verification set** is the minimum viable order)

---

## 0. Purpose, scope, and selection criteria

### 0.1 Purpose
This document specifies the **antibody panel required to validate the HMSR v0.4 finding** ("the nuclear-encoded mitochondrial biogenesis programme is coordinately down-regulated in sarcopenic muscle") at the **protein level**, in:

- **Aim 1 — Cohort protein validation** (human muscle biopsies, IF / WB)
- **Aim 2 — Causation in-vitro** (C2C12 myotubes + human HSMM / myobundles, siRNA/shRNA/sgRNA knock-down, then WB + IF verification)
- **Exp A / B / C — In-vivo follow-up** (mouse TA / gastrocnemius, IHC + fibre-typing)
- **Aim 3 supplement — Mitophagy flux** (mt-Keima flow cytometry)

### 0.2 Scope
Two complement-determining goals:
1. **Verify the 7 tiered v0.4 candidates + 6 sub-programme representatives + PGC-1α + TFAM programme master** at protein level with KO/KD-validated Abs.
2. **Provide per-gene verification Abs for the Aim 2 siRNA / shRNA / sgRNA knock-down arm**, plus the OMM/IMS/matrix markers needed to assess cristae / import / biogenesis.

### 0.3 Selection criteria (and how each is scored)

| Criterion | Weight | What we look for | Acceptable evidence |
|---|---|---|---|
| **KO / KD-validated** | High | Vendor tag + PMID | ≥1 publication with siRNA/shRNA/sgRNA + WB showing band loss at expected MW |
| **Specificity (no off-target / cross-family)** | High | KO lysate or CRISPR clean knock-out | CST, Abcam, MitoSciences, Atlas, Proteintech KO/KD tag |
| **Reactivity to M + H (+ R)** | High | Vendor cross-reactivity | Mouse + human reactivity minimum (C2C12 + HSMM / myobundle) |
| **Monoclonal preferred** | Medium | Recombinant mAb | mAb > mAb+pAb-validation > pAb |
| **Application breadth** | Medium | Vendor-tested in WB + IF + IHC | We need all three |
| **Lot-to-lot consistency** | Low | Recombinant mAb | mAb > pAb |
| **Citations in ≥3 skeletal-muscle papers** | Low | PubMed search | Bonus, not gate |
| **Cost per 100 µL** | Low | List price | Realistic budget: $300–600 / mAb |

### 0.4 Vendor tier map (used throughout this document)

| Vendor | Use case | Typical 100 µL mAb price | Notes |
|---|---|---|---|
| **Cell Signaling Technology (CST)** | Gold-standard mAb for WB / IF; many KO-validated clones | $300–500 | Clone + RRID; preferred for Tier 1/2 + programme master |
| **Abcam** | Broad catalogue, MitoSciences OXPHOS cocktail legacy | $300–500 | Total OXPHOS Human WB Cocktail (ab110411) and Rodent WB Cocktail (ab110413) are anchors |
| **MitoSciences / Abcam MitoSciences** | OXPHOS complex subunits, classical clones (20C11, 7A10, 13G12, 16B12, etc.) | $300–500 | Anchors for the sub-programme representatives |
| **Proteintech** | Rabbit pAb, broad coverage, KO-validated, lowest $/µL | $250–400 (rabbit pAb); $300–500 (mAb) | Default "fallback" + 1st choice for newer / less-mapped targets |
| **Atlas Antibodies (HPA)** | Human Protein Atlas lineage, Rabbit pAb, IF-grade | $250–400 (pAb) | Best for IF + IHC on human sections; KD-validated by HPA |
| **Thermo Fisher / Invitrogen** | Clone-based mAb portfolio (MA-, clone, PA- families) | $300–500 | Some orthogonal clones worth holding |
| **Santa Cruz Biotechnology** | sc- series mAb + pAb; legacy | $200–400 | Cheaper; lot variability a concern |
| **MilliporeSigma / EMD Millipore** | Older but well-cited clones (e.g. AB3242 PGC-1α pAb) | $300–500 | Used as 3rd choice for PGC-1α pAb anchor |
| **DSHB (Iowa)** | Fibre-type myosin mAbs (A4.951, SC-71, BF-F3) | $100–200 (hybridoma supernatant) | Mandatory for fibre-type IHC |

### 0.5 Conventions in the tables below
- **MW (kDa):** Predicted mature / processed MW on the gel, not the ORF; OXPHOS subunits are imported and cleaved.
- **Dilution (WB / IF):** Default starting dilution; each lab titrates empirically. Vendor-recommended if the lab has no prior experience.
- **Gel %:** SDS-PAGE recommendation based on MW; we always run 4–12% gradient + a 12% uniform as back-up.
- **Pitfall:** Real-world failure mode (e.g. lot variation, isoform cross-reactivity, mitophagy-induced up-regulation) — this column is where the panel defends itself.

---

## 1. Tier-aligned antibody panel (the main table)

The panel below covers **the 7 highlighted v0.4 tiered candidates + 6 sub-programme representatives + PGC-1α + TFAM programme master + specificity / quality / loading / fibre-type / senescence / HPGD controls**. We split it into 5 sub-tables for readability (1.1 = v0.4 candidates, 1.2 = sub-programme, 1.3 = specificity / loading / quality, 1.4 = satellite / fibre-type / senescence, 1.5 = HPGD / 15-PGDH).

### 1.1 — HMSR v0.4 tiered candidates + programme master

| # | Target (gene) | MW (kDa) | Gel % (WB) | Vendor (1st) | Cat # | RRID | Host / clonality | Reactivity | Application | Dilution WB | Dilution IF / IHC | Validation cite | Price (100 µL) USD | Alt vendor 1 (Cat #) | Alt vendor 2 (Cat #) | Pitfalls / Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **CHCHD10** (Tier 1) | 14 | 15% or 4–12% gradient | **Proteintech** | **25671-1-AP** | RRID:AB_2880203 | Rabbit pAb | M, H, R | WB, IF, IHC-P | 1:1,000 | 1:100–1:200 | [Proteintech KD-validation](https://www.ptglab.com/products/CHCHD10-Antibody-25671-1-AP.htm); cited in multiple FTD/ALS papers (e.g. PMID 32117183) | $300 | Atlas HPA003439 (Rabbit pAb) | Abcam ab224564 (Rabbit mAb) | A small (14 kDa) IMS / cristae protein — co-migrates near lysozyme; run 15% gel; mild cross-reactivity with CHCHD3 in some lots; **the Tier-1 candidate — order first and validate in C2C12 + HSMM before anything else** |
| 2 | **NDUFB4** (Tier 2, Complex I accessory) | 15 | 15% or 4–12% gradient | **Proteintech** | **16149-1-AP** | RRID:AB_2282611 | Rabbit pAb | M, H, R | WB, IF, IHC | 1:500–1:1,000 | 1:100–1:200 | KO-validated by [Stenton et al. 2021 (Complex I assembly paper)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8083086/) and Proteintech KO tag | $300 | Abcam ab110242 (Total OXPHOS cocktail — includes NDUFB4) | Atlas HPA062889 (Rabbit pAb) | Small subunit — run 15% gel; if WB faint, dilute 1:500 rather than 1:1000 to push signal above background; verify on isolated mitochondria |
| 3 | **ATP5F1B** (Tier 2, Complex V F₁β) | 57 | 10% | **Abcam** | **ab14730** (also sold as clone 7F9 / 9H11 variant — confirm) | RRID:AB_301447 (anchor OXPHOS cocktail) | Mouse mAb | M, H, R | WB, IF, IHC | 1:1,000 | 1:200–1:500 | MitoSciences / Abcam OXPHOS cocktail; KO-validated in multiple papers (e.g. PMID 22286907) | $400 | CST 84547 (Rabbit mAb) | Proteintech 17247-1-AP (Rabbit pAb) | β-subunit of F₁-ATPase; same-complex crosstalk with ATP5A1 — some lots cross-react; use a **matched-pair** ATP5F1B + ATP5A1 to confirm a real ATP5F1B effect (Tier-2 KD verification) |
| 4 | **MRPL34** (Tier 3, mitoribosome large subunit) | 12 | 15% or 4–12% gradient | **Proteintech** | **16394-1-AP** | RRID:AB_2140587 | Rabbit pAb | M, H, R | WB, IF | 1:500–1:1,000 | 1:100–1:200 | Proteintech KD-validated; cited in [Rebelo-Guiomar 2022 (mitoribosome)](https://pubmed.ncbi.nlm.nih.gov/35013182/) | $300 | Atlas HPA059705 (Rabbit pAb) | Cat#<TBD> | Very small subunit (12 kDa) — run 15% gel or 4–12% gradient; cross-reactivity with MRPL33 possible (8 kDa, runs below); **use a long-exposure ECL substrate** for Tier 3 WB |
| 5 | **MRPL33** (Tier 3, mitoribosome large subunit) | 8 | 4–12% gradient (Tricine) or 15% w/ Tricine | **Proteintech** | **15236-1-AP** | RRID:AB_2140786 | Rabbit pAb | M, H, R | WB, IF | 1:500–1:1,000 | 1:100–1:200 | Proteintech KD-validated | $300 | Cat#<TBD> | Cat#<TBD> | **Very small (8 kDa)** — use Tricine / MES-SDS running buffer (Thermo) not Tris-glycine; otherwise runs at the dye front; pair with **MRPL3 (39 kDa)** as a large-subunit positive control |
| 6 | **APOO / MIC26** (Tier 3, MICOS) | 30 | 12% | **Proteintech** | **20550-1-AP** | RRID:AB_2878728 | Rabbit pAb | M, H, R | WB, IF, IHC | 1:500–1:1,000 | 1:100–1:200 | Proteintech KO-validated; reviewed in [Khosravi & Harner 2020, MICOS](https://pubmed.ncbi.nlm.nih.gov/32436652/) | $300 | Atlas HPA055018 (Rabbit pAb) | Cat#<TBD> | MICOS complex; pair with CHCHD3 + IMMT (MIC60) to demonstrate cristae integrity on KD; the **ApoO** gene name overlaps with the lipid transport family — verify the Ab recognises MIC26 isoform not the apolipoprotein |
| 7 | **PPARGC1A / PGC-1α** (programme master) | 91 (canonical); 40 (isoform NT); 38 (isoform) | 7–8% (canonical) **OR** 12% (small isoforms) | **CST** | **2178** (clone D5K9D, rabbit mAb) | RRID:AB_10831027 | Rabbit mAb (recombinant) | M, H, R | WB, IP, IF, ChIP | 1:1,000 | 1:100 (IF) | Multiple KO-validated papers; **D5K9D** clone is the current standard (replaces older AB3242 pAb); see [CST datasheet + PMID 28854363] | $400 | MilliporeSigma AB3242 (Rabbit pAb — legacy) | CST 89356 (clone E3K2R — back-up) | **Three canonical isoforms** (PGC-1α1 91 kDa, PGC-1α2/3 shorter N-terminal truncations, PGC-1α4 muscle-enriched); D5K9D binds the C-terminus and recognises all major isoforms; for muscle, consider also **PGC-1α4 selective Ab** (Millipore ABIN223879) — outside scope unless a specific Aim 2.5 follow-up |
| 8 | **TFAM** (programme master, mtDNA packaging) | 24 | 12–15% | **CST** | **8076** (clone D5C8, rabbit mAb) | RRID:AB_10949138 | Rabbit mAb | M, H, R | WB, IF, ChIP | 1:1,000 | 1:200 (IF) | KO-validated by CST; multiple papers (PMID 29133412) | $400 | Proteintech 19998-1-AP (Rabbit pAb) | Abcam ab252432 (Rabbit mAb) | Mitochondrial-matrix protein; **runs as a doublet in some lysates** (24 + 22 kDa) — both are TFAM, the smaller is a cleavage product; do not panic; pair with **mtDNA copy-number qPCR** to confirm transcriptional effect |

**Subtotal (8 Abs):** at first-choice list ~$2,700; with 1 alt each (24 Abs) ~$7,500.

---

### 1.2 — Sub-programme representatives (one per complex + cristae / import)

The 6 "sub-programme representatives" in the v0.4 plan (one per complex) are bold-marked. CHCHD3 + IMMT (MICOS) and TOMM20 + TIMM23 (import) are co-anchors for Aim 2 KD secondary proof.

| # | Target (complex / function) | MW (kDa) | Gel % (WB) | Vendor (1st) | Cat # | RRID | Host / clonality | Reactivity | Application | Dilution WB | Dilution IF / IHC | Validation cite | Price (100 µL) USD | Alt vendor 1 (Cat #) | Alt vendor 2 (Cat #) | Pitfalls / Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 9 | **NDUFA9** (Complex I, matrix-accessory) — **anchor #1** | 39 | 12% | **Abcam** (MitoSciences) | **ab14713** (clone 20C11) | RRID:AB_301431 | Mouse mAb | M, H, R, Ham | WB, IF, IHC, IP | 1:1,000 (WB); 0.5–2 µg/mL (IP) | 1:200–1:500 (IF) | MitoSciences classical clone; KD-validated in 100+ papers; e.g. [PMID 22286907](https://pubmed.ncbi.nlm.nih.gov/22286907/) | $400 | CST 70666 (Rabbit mAb) | Proteintech 20312-1-AP (Rabbit pAb) | **GOLD-STANDARD Complex I Ab**; cross-reacts with hamster (CHO) — useful if we ever need CHO work; 39 kDa, run 12% gel; the Abcam lot numbers starting "GR" are best |
| 10 | **NDUFS1** (Complex I, core 75 kDa Fe-S) | 80 | 8% | **Proteintech** | **12444-1-AP** | RRID:AB_2149028 | Rabbit pAb | M, H, R | WB, IF, IHC | 1:500–1:1,000 | 1:100–1:200 | Proteintech KO-validated; [Stroud et al. 2016, NDUFS1 KO](https://www.nature.com/articles/nature17448) | $300 | Atlas HPA007326 (Rabbit pAb) | Abcam ab169540 (Rabbit mAb) | Core catalytic subunit — a drop indicates catalytic CI loss, not just assembly; for **Complex I assembly** use NDUFA9 as the assembly-marker; high MW (80 kDa) — use 8% gel and **always image a co-stained Vinculin / β-tubulin** |
| 11 | **SDHA** (Complex II, Fp subunit) | 73 | 8% | **Abcam** (MitoSciences) | **ab14715** (clone 2E3GC12FB2AE2) | RRID:AB_301433 | Mouse mAb | M, H, R, Ham | WB, IF, IHC, IP | 1:1,000 | 1:200–1:500 | MitoSciences clone; KO-validated ([PMID 27226639](https://pubmed.ncbi.nlm.nih.gov/27226639/)) | $400 | CST 11998 (Rabbit mAb) | Proteintech 14865-1-AP (Rabbit pAb) | **The Complex II anchor**; Fp (flavoprotein) subunit; can run slightly higher than predicted (73 kDa); **do NOT** use the SDHA pAb (Abcam ab14715 is the mAb anchor — confirms the right product) |
| 12 | **SDHB** (Complex II, Ip Fe-S subunit) | 32 | 12% | **Abcam** (MitoSciences) | **ab14714** (clone 21A11AE7) | RRID:AB_301432 | Mouse mAb | M, H, R, Ham | WB, IF, IHC, IP | 1:1,000 | 1:200–1:500 | MitoSciences clone; KD-validated | $400 | CST 45849 (Rabbit mAb) | Proteintech 10620-1-AP (Rabbit pAb) | **The Complex II assembly-marker** (loss = SDHA-FADH2 issue, not necessarily assembly); pair with SDHA for full II-status; 32 kDa, run 12% gel |
| 13 | **UQCRC1** (Complex III, Core protein 1) | 53 | 10% | **Abcam** (MitoSciences) | **ab110252** | RRID:AB_10887997 | Mouse mAb | M, H, R | WB, IF, IHC, IP | 1:1,000 | 1:200 | MitoSciences clone; KD-validated ([PMID 27226639](https://pubmed.ncbi.nlm.nih.gov/27226639/)) | $400 | CST 90579 (Rabbit mAb) | Proteintech 21705-1-AP (Rabbit pAb) | Core 1 (matrix-side, not Core 2) — Core 1 is the more stable Complex III marker; 53 kDa, run 10% gel |
| 14 | **COX IV / COX4I1** (Complex IV, nuclear-encoded) | 20 | 15% | **CST** | **4850** (clone 3E11) | RRID:AB_2085424 | Rabbit mAb | M, H, R, Ham | WB, IF, IHC, IP | 1:1,000 | 1:200 (IF); 1:100 (IHC) | CST KO-validated; widely used (PMID 33028801) | $400 | Abcam ab14744 (Mouse mAb) | Proteintech 11242-1-AP (Rabbit pAb) | **Use the nuclear-encoded COX4I1, NOT MT-CO1 (mitochondrial-encoded)** — the user requested a nuclear-encoded target; MT-CO1 Ab is unreliable on human mtDNA mutation backgrounds; COX4I1 is the canonical Complex IV IF marker |
| 15 | **ATP5A1** (Complex V, α-subunit) | 60 | 10% | **Abcam** (MitoSciences) | **ab14748** (clone 7H10BD4F9) | RRID:AB_301447 | Mouse mAb | M, H, R, Ham | WB, IF, IHC, IP | 1:1,000 | 1:200–1:500 | MitoSciences clone; KD-validated | $400 | CST 85979 (Rabbit mAb) | Proteintech 14676-1-AP (Rabbit pAb) | **Use as the matched-pair control** for the ATP5F1B (Tier 2) KD — if ATP5A1 is unchanged but ATP5F1B drops, the KD is specific; α-subunit (60 kDa) and β-subunit (57 kDa) **co-migrate on 10% gels** — run 12% if you need to resolve them |
| 16 | **MRPL3** (mitoribosome large subunit) | 39 | 12% | **Proteintech** | **16582-1-AP** | RRID:AB_2140800 | Rabbit pAb | M, H, R | WB, IF | 1:500–1:1,000 | 1:100–1:200 | Proteintech KD-validated; [Rebelo-Guiomar 2022](https://pubmed.ncbi.nlm.nih.gov/35013182/) | $300 | Atlas HPA024456 (Rabbit pAb) | Abcam ab222406 (Rabbit mAb) | **Use as the well-validated large-subunit anchor** if MRPL34 is faint; if MRPL3 is unchanged but MRPL34 drops, you have a subunit-specific effect |
| 17 | **MRPS18B** (mitoribosome small subunit) | 29 | 12% | **Proteintech** | **16139-1-AP** | RRID:AB_2140701 | Rabbit pAb | M, H, R | WB, IF | 1:500–1:1,000 | 1:100–1:200 | Proteintech KD-validated | $300 | Atlas HPA062557 (Rabbit pAb) | Cat#<TBD> | **Back-up / secondary mitoribosome marker** for the small subunit; pair with MRPL3 to demonstrate both arms of the mitoribosome |
| 18 | **CHCHD3** (MICOS complex, complement to CHCHD10) | 26 | 12% | **Proteintech** | **25625-1-AP** | RRID:AB_2880204 | Rabbit pAb | M, H, R | WB, IF, IHC | 1:500–1:1,000 | 1:100–1:200 | Proteintech KD-validated; [Ding et al. 2015, MICOS](https://pubmed.ncbi.nlm.nih.gov/26098293/) | $300 | Atlas HPA065442 (Rabbit pAb) | Abcam ab130179 (Rabbit pAb) | **Use as the secondary CHCHD10 KD proof** — both belong to the MICOS-coiled-coil-Helix-Coiled-coil-Helix family; if CHCHD10 KD pulls down CHCHD3 and IMMT, the cristae junction is disrupted |
| 19 | **IMMT / MIC60** (MICOS, central cristae organiser) | 80 | 8% | **Proteintech** | **10179-1-AP** | RRID:AB_2127193 | Rabbit pAb | M, H, R | WB, IF, IHC | 1:500–1:1,000 | 1:100–1:200 | Proteintech KO-validated; [Friedman et al. 2015, MIC60](https://pubmed.ncbi.nlm.nih.gov/26098295/) | $300 | Atlas HPA004943 (Rabbit pAb) | Abcam ab110329 (Mouse mAb) | **The cristae junction organiser**; the IMMT knockout is embryonic lethal — partial KD gives "swollen mitochondria with reduced cristae" phenotype; if a CHCHD10 / APOO KD leaves MIC60 unchanged, the effect is on a single subunit, not the whole MICOS |
| 20 | **TOMM20** (Outer-membrane import receptor) | 16 | 15% or 4–12% gradient | **CST** | **42406** (clone D8T4N) | RRID:AB_2732823 | Rabbit mAb | M, H, R, Ham | WB, IF, IHC, IP | 1:1,000 | 1:200 (IF); 1:100 (IHC) | **CST KO-validated**; canonical OMM marker; 200+ citations | $400 | Abcam ab186287 (Rabbit mAb) | Proteintech 11802-1-AP (Rabbit pAb) | **THE OMM NORMALIZATION Ab** — use for IF mito-content quantification (Sum IF intensity / DAPI area); **WARNING**: TOMM20 is **up-regulated in mitophagy-impaired cells** (because OMM proteins accumulate) — if the KD blocks mitophagy, TOMM20 will go up, not down. Always pair with HSP60 (matrix) to disambiguate "more mito" from "less mitophagy" |
| 21 | **TIMM23** (Inner-membrane translocase) | 22 | 12–15% | **Proteintech** | **11123-1-AP** | RRID:AB_2213631 | Rabbit pAb | M, H, R | WB, IF, IHC | 1:500–1:1,000 | 1:100–1:200 | Proteintech KD-validated; [Bauer et al. 1999, TIM23](https://pubmed.ncbi.nlm.nih.gov/10564262/) | $300 | Atlas HPA035126 (Rabbit pAb) | Abcam ab230253 (Rabbit mAb) | Inner-membrane import translocase; 22 kDa; 4 isoforms in some species; **the Ab is an isoform mix** — does not allow isoform-specific KD verification; for that use qPCR of the specific isoform |
| 22 | **SDHA anchor (re-list as #11)** — see #11 | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |

**Subtotal (1.2; 13 unique Abs — #9 through #21):** at first-choice list ~$4,300; with 1 alt each (39 Abs) ~$11,500.

---

### 1.3 — Specificity controls, loading controls, mitochondrial quality / biogenesis markers

| # | Target (function) | MW (kDa) | Gel % (WB) | Vendor (1st) | Cat # | RRID | Host / clonality | Reactivity | Application | Dilution WB | Dilution IF / IHC | Validation cite | Price (100 µL) USD | Alt vendor 1 (Cat #) | Alt vendor 2 (Cat #) | Pitfalls / Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 23 | **GAPDH** (cytoplasmic loading — glycolytic) | 37 | 12% | **CST** | **5174** (clone D16H11) | RRID:AB_10622025 | Rabbit mAb | M, H, R, Ham, Mk | WB, IF, IHC, IP | 1:1,000 | 1:200 | **CST KO-validated**; replaces the mouse mAb 6C5 legacy; the D16H11 mAb **does not recognise GAPDH under hypoxia** (stress artefacts) | $400 | Proteintech 10494-1-AP (Rabbit pAb) | Abcam ab9485 (Rabbit pAb) | **Do NOT use for oxidative-vs-glycolytic comparisons** (C2C12 myotubes vs myoblasts): GAPDH levels change with myogenic state. **Use Vinculin or β-tubulin instead.** Keep GAPDH only for non-muscle / non-mito general loading |
| 24 | **Vinculin** (cytoplasmic / focal-adhesion loading) | 124 | 7–8% | **CST** | **13901** (clone E1E9V) | RRID:AB_2728768 | Rabbit mAb | M, H, R | WB, IF, IHC, IP | 1:1,000 | 1:200 | CST KO-validated | $400 | Proteintech 26520-1-AP (Rabbit pAb) | Abcam ab129002 (Rabbit mAb) | **PRIMARY loading control for muscle lysates** — vinculin is a sarcomeric / membrane-associated protein in C2C12 + HSMM; high MW 124 kDa — 7–8% gel; **highly stable in C2C12 differentiation** (no myogenic state artefact) |
| 25 | **β-tubulin** (cytoplasmic loading) | 55 | 10% | **CST** | **2128** (clone 9F3) | RRID:AB_823664 | Rabbit mAb | M, H, R, Ham | WB, IF, IHC, IP, F | 1:1,000 | 1:200 (IF); 1:100 (IHC) | CST KO-validated; widely used | $400 | Abcam ab6046 (Rabbit pAb) | Proteintech 66240-1-Ig (Mouse mAb) | **ALTERNATIVE primary loading control**; if vinculin is variable across samples (rare in well-prepared muscle lysates), fall back to β-tubulin |
| 26 | **Lamin B1** (nuclear envelope control) | 67 | 8% | **CST** | **13435** (clone D9V6H) | RRID:AB_2738428 | Rabbit mAb | M, H, R, Ham, Mk | WB, IF, IHC, IP | 1:1,000 | 1:200 (IF); 1:100 (IHC) | CST KO-validated | $400 | Abcam ab16048 (Rabbit pAb) | Proteintech 66095-1-Ig (Mouse mAb) | **Nuclear-specificity control** — required to verify that a "mito-decrease" is not an artefact of unequal nuclear contamination of fractions; use during **subcellular fractionation QC** (C2C12 mito vs cytosol vs nuclear) |
| 27 | **Citrate synthase (CS)** (mitochondrial mass marker) | 52 | 10% | **Proteintech** | **16131-1-AP** | RRID:AB_2080414 | Rabbit pAb | M, H, R | WB, IF, IHC | 1:500–1:1,000 | 1:100–1:200 | Proteintech KD-validated; widely used (e.g. [Larsen et al. 2012, mito mass](https://pubmed.ncbi.nlm.nih.gov/22956628/)) | $300 | Abcam ab129095 (Mouse mAb) | Atlas HPA038460 (Rabbit pAb) | **THE mito-mass marker** — use as the **mito-normalization denominator** when comparing protein X / CS ratios across sarcopenic / non-sarcopenic muscle; **must be paired with TOMM20 IF** to confirm in situ that mito mass is reduced, not just the CS protein level |
| 28 | **HSP60 / HSPD1** (matrix chaperone, biogenesis marker) | 60 | 10% | **CST** | **12165** (clone D6F1) | RRID:AB_2636980 | Rabbit mAb | M, H, R, Ham, Mk | WB, IF, IHC, IP | 1:1,000 | 1:200 (IF); 1:100 (IHC) | CST KO-validated | $400 | Abcam ab190828 (Rabbit mAb) | Proteintech 15282-1-AP (Rabbit pAb) | **Use for IF mito content + WB mito-mass normalization**; HSP60 is also a **stress-induced chaperone** — in aged / atrophied muscle, HSP60 can rise while CS falls (compensatory up-regulation); if CS and HSP60 disagree, **use CS as the mass marker and report the disagreement** |
| 29 | **LONP1** (matrix protease; mitochondrial protein-quality control) | 106 | 7% | **Proteintech** | **15440-1-AP** | RRID:AB_2138112 | Rabbit pAb | M, H, R | WB, IF, IHC | 1:500–1:1,000 | 1:100–1:200 | Proteintech KD-validated; [Quirós et al. 2014, LON](https://pubmed.ncbi.nlm.nih.gov/25190519/) | $300 | CST 28020 (Rabbit mAb) | Cat#<TBD> | **UPRmt (mito-unfolded-protein response) marker** — if LONP1 is up-regulated in sarcopenic muscle, the mito-proteostasis arm is engaged; a very large protein (106 kDa) — use 7% gel and run slowly |
| 30 | **mt-Keima (transgene; pH-dependent fluorophore)** | n/a (transgene) | n/a | n/a | n/a | n/a | n/a | n/a | **FACS (live cell); confocal dual-excitation** | n/a | n/a | [Lazarou et al. 2015, mt-Keima](https://pubmed.ncbi.nlm.nih.gov/26040720/) — *the reference* | n/a | n/a | n/a | **NOT an Ab** — this is a transgene readout. The mitophagy-flux measurement is the **ratio of 561 nm / 458 nm fluorescence** (acidic mito-lysosome / neutral mito); a separate "all-mito" 405 nm-excited green channel is the reference. For WB detection: a custom anti-Keima pAb is sold by **[MBL International PM046]** — confirm at order time; for protein verification use the live-cell fluorometry + FACS |

**Subtotal (1.3; 7 unique Abs + 1 transgene):** at first-choice list ~$2,500; with 1 alt each (21 Abs) ~$6,000.

---

### 1.4 — Non-mitochondrial specificity controls (ribosomal + proteasome + Lamin B1)

| # | Target (function) | MW (kDa) | Gel % (WB) | Vendor (1st) | Cat # | RRID | Host / clonality | Reactivity | Application | Dilution WB | Dilution IF / IHC | Validation cite | Price (100 µL) USD | Alt vendor 1 (Cat #) | Alt vendor 2 (Cat #) | Pitfalls / Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 31 | **RPLP0 / 36B4** (cytoplasmic large-subunit ribosome) | 34 | 12% | **Proteintech** | **11290-2-AP** | RRID:AB_2877748 | Rabbit pAb | M, H, R | WB, IF | 1:500–1:1,000 | 1:100–1:200 | Proteintech KO-validated; widely used as a **qPCR reference gene** | $300 | Atlas HPA004134 (Rabbit pAb) | Abcam ab224561 (Rabbit pAb) | **Cytoplasmic ribosome control** — required to demonstrate that a "mito-decrease" is not a global translation down-shift; not a loading control, a *specificity* control for subcellular fractionation |
| 32 | **RPS6** (cytoplasmic small-subunit ribosome, pS6 / S6K readout) | 29 (p-S6 32-34) | 12% | **CST** | **2217** (clone 5G10) | RRID:AB_331355 | Rabbit mAb | M, H, R, Ham, Mk | WB, IF, IHC, IP | 1:1,000 | 1:200 | CST KO-validated; recognises total RPS6 (separate p-S6 Ab for the mTORC1 readout — 4858 clone) | $400 | Proteintech 14823-1-AP (Rabbit pAb) | Abcam ab40820 (Rabbit pAb) | **Second cytoplasmic ribosome control** — the pS6 form (Ser235/236) is the mTORC1 readout and is essential for **Exp C exercise reversal** (PGC-1α induction is p-S6 dependent); order both if Exp C is in scope. **If only ordering one cytoplasmic ribosome Ab, pick RPLP0 (broader, less regulated)** |
| 33 | **PSMA5** (proteasome α-5 subunit) | 26 | 12% | **Proteintech** | **11338-1-AP** | RRID:AB_2879246 | Rabbit pAb | M, H, R | WB, IF | 1:500–1:1,000 | 1:100–1:200 | Proteintech KD-validated | $300 | CST 2457 (Rabbit mAb) | Abcam ab177553 (Rabbit mAb) | **Proteasome (UPS) control** — required to demonstrate that an apparent "mito-program decrease" is not confounded by global proteostasis loss (which would also drop OXPHOS subunits because they're rapidly turned over); pairs with the atrophy context |

**Subtotal (1.4; 3 Abs):** at first-choice list ~$1,000; with 1 alt each (9 Abs) ~$2,500.

---

### 1.5 — Satellite / fibre-type / senescence / SASP (cross-reference for Exp A/B/C and the sarcopenia narrative)

| # | Target (function) | MW (kDa) | Gel % (WB) | Vendor (1st) | Cat # | RRID | Host / clonality | Reactivity | Application | Dilution WB | Dilution IF / IHC | Validation cite | Price (100 µL) USD | Alt vendor 1 (Cat #) | Alt vendor 2 (Cat #) | Pitfalls / Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 34 | **PAX7** (satellite-cell marker) | 56 (post-translation ~57) | 10% | **DSHB** | **PAX7** (clone PAX7-s) | RRID:AB_2299243 | Mouse mAb | M, R (weaker H) | IF, IHC-F, IHC-P | n/a (sup) | 1:50 (IF); 1:200 (IHC) | DSHB antibody registry | $150 (sup) | CST 7019 (wait — actually DSHB is the gold standard; back-up: Abcam ab187339) | Proteintech 20549-1-AP (Rabbit pAb) | **Satellite-cell counting** in Exp A / B / C — order the DSHB supernatant; a must for quantifying satellite-cell pool in the sarcopenia narrative; **do NOT use for WB** — DSHB is IF-grade only |
| 35 | **MYH7** (slow / type I myosin heavy chain) | 220 | 6% (or 4–8% gradient) | **DSHB** | **A4.951** | RRID:AB_2235587 | Mouse mAb (IgG1) | M, H, R | IF, IHC-F, IHC-P, WB | 1:50 (WB) | 1:100 (IF); 1:200 (IHC) | DSHB antibody registry; 1,000+ citations | $150 (sup) | Abcam ab11083 (Mouse mAb) | Proteintech 22280-1-AP (Rabbit pAb) | **Type I / slow fibre marker** for IHC; do NOT load on 10% gels (220 kDa runs as a smear); use 6% gels or 4–8% gradient; DSHB is mandatory for the fibre-typing IHC |
| 36 | **MYH2** (fast type 2A) | 220 | 6% | **DSHB** | **SC-71** (or A4.74 — back-up) | RRID:AB_2147165 (SC-71) | Mouse mAb (IgG1) | M, H, R | IF, IHC-F, IHC-P | n/a | 1:100 (IF); 1:200 (IHC) | DSHB antibody registry | $150 (sup) | Abcam ab91506 (Mouse mAb) | Cat#<TBD> | **Type 2A fibre marker**; pair with A4.951 (type I) and BF-F3 (type 2B) for full fibre-type IHC |
| 37 | **MYH4** (fast type 2B) | 220 | 6% | **DSHB** | **BF-F3** | RRID:AB_2266724 | Mouse mAb (IgM) | M, R (poor H) | IF, IHC-F, IHC-P | n/a | 1:100 (IF); 1:200 (IHC) | DSHB antibody registry | $150 (sup) | Abcam ab91507 (Mouse mAb) | Cat#<TBD> | **Type 2B fibre marker** — mouse / rat only; in human skeletal muscle, the type 2B gene is largely **not expressed** (humans have type 2X instead); **do NOT use for human biopsy IHC** — substitute MYH1 / MyHC-IIx Ab (e.g. Abcam ab91505) if needed |
| 38 | **p16^INK4a / CDKN2A** (senescence marker) | 16 | 15% | **CST** | **80772** (clone E5N9D) | RRID:AB_2799960 | Rabbit mAb | M, H | WB, IF, IHC, IP | 1:1,000 | 1:200 (IF); 1:100 (IHC) | CST KO-validated | $400 | Abcam ab108349 (Rabbit mAb) | Proteintech 10883-1-AP (Rabbit pAb) | **Senescence marker** — required to cross-reference the sarcopenia signal with cellular senescence (the alternative SASP-driven mechanism) |
| 39 | **p21 / CDKN1A** (senescence / cell-cycle arrest) | 21 | 12% | **CST** | **2947** (clone 12D1) | RRID:AB_2236160 | Rabbit mAb | M, H, R, Ham, Mk | WB, IF, IHC, IP, F | 1:1,000 | 1:200 (IF); 1:100 (IHC) | CST KO-validated | $400 | Abcam ab109520 (Rabbit mAb) | Proteintech 10355-1-AP (Rabbit pAb) | **Senescence / cell-cycle arrest marker**; p21 is the immediate p53 target; pairs with p16 for the senescence axis |
| 40 | **IL-6** (SASP cytokine) | 24 (mature); 28 (precursor) | 12–15% | **CST** | **12912** (clone D3K2N) | RRID:AB_2798059 | Rabbit mAb | M, H | WB, IF, IHC, IP | 1:1,000 | 1:200 (IF) | CST KO-validated | $400 | Abcam ab233706 (Rabbit mAb) | Proteintech 21865-1-AP (Rabbit pAb) | **SASP cytokine** — the cross-reference between mito-dysfunction and the senescence/SASP narrative |

**Subtotal (1.5; 7 Abs):** at first-choice list ~$1,900.

---

### 1.6 — HPGD / 15-PGDH (muscle-quality Perspective cross-link; honest null from HMSR v0.4)

| # | Target (function) | MW (kDa) | Gel % (WB) | Vendor (1st) | Cat # | RRID | Host / clonality | Reactivity | Application | Dilution WB | Dilution IF / IHC | Validation cite | Price (100 µL) USD | Alt vendor 1 (Cat #) | Alt vendor 2 (Cat #) | Pitfalls / Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 41 | **HPGD / 15-PGDH** (15-hydroxyprostaglandin dehydrogenase; PGE2 catabolism) | 29 | 12% | **Proteintech** | **15137-1-AP** | RRID:AB_2118712 | Rabbit pAb | M, H, R | WB, IF, IHC | 1:500–1:1,000 | 1:100–1:200 | Proteintech KD-validated | $300 | Atlas HPA042376 (Rabbit pAb) | Cat#<TBD> | **Honest null in HMSR v0.4 (β meta p = 0.98)** — included for *transparency* in the muscle-quality Perspective cross-link; HPGD is the rate-limiting PGE2 catabolic enzyme and a previously hypothesised mediator of the exercise-muscle-quality axis; the v0.4 null is itself a publishable finding — **report "no association at the mRNA level" and verify with WB on a subset of the cohort** |

**Subtotal (1.6; 1 Ab):** at first-choice list ~$300.

---

### 1.7 — Panel rollup

| Sub-table | # unique Abs | First-choice subtotal (USD) | With 1 alt each (USD) |
|---|---|---|---|
| 1.1 — v0.4 tiered + programme master | 8 | $2,700 | $7,500 |
| 1.2 — Sub-programme + cristae + import | 13 | $4,300 | $11,500 |
| 1.3 — Specificity / loading / quality | 7 (+ 1 transgene) | $2,500 | $6,000 |
| 1.4 — Non-mito specificity (ribo + proteasome) | 3 | $1,000 | $2,500 |
| 1.5 — Satellite / fibre-type / senescence / SASP | 7 | $1,900 | n/a (DSHB + CST mix) |
| 1.6 — HPGD (Perspective cross-link) | 1 | $300 | n/a |
| **TOTAL (without alts)** | **39 Abs + 1 transgene** | **~$12,700** | — |
| **TOTAL (with 1 alt per Ab)** | **~117 Abs (3 per target)** | n/a | **~$31,000** |

**Note on price:** the figures above are 100 µL list prices (mAb) or 100 µg list prices (pAb) as of mid-2026. mAb pricing is per **100 µL**; pAb pricing is per **100 µg** — these are **not directly comparable** — the document uses 100 µL as the mAb standard because pAb pricing is highly vendor-variable. Always divide Proteintech pAb by ~2 (100 µg / 2 mg/mL → 500 µL → $300 / 500 µL ≈ $0.60/µL vs. CST mAb at $400/100 µL = $4.00/µL). **pAb is ~7× cheaper per µL of working dilution.**

---

## 2. Application-specific mini-panels

### 2.1 — WB (C2C12 + HSMM myotube / myobundle lysates)

| Step | Detail |
|---|---|
| **Use case** | Aim 1 protein validation (cohort biopsies), Aim 2 KD verification (C2C12 + HSMM) |
| **Primary Abs** | Full programme (#1–#21) + loading controls (#24, #27, #28) + non-mito specificity (#31, #33) |
| **Secondary Ab** | HRP-anti-rabbit IgG (CST 7074, $200, 1:2,000); HRP-anti-mouse IgG (CST 7076, $200, 1:2,000) |
| **Normalization target** | (a) **Vinculin** (cyto) for non-mito protein loading; (b) **Citrate synthase** (mito mass) for OXPHOS ratios; (c) **HSP60** as the matrix chaperone / biogenesis marker when CS is variable; (d) **Lamin B1** only during subcellular fractionation QC |
| **Gel system** | **4–12% Bis-Tris gradient** (Thermo) — single gel resolves 8–250 kDa; back-up **12% uniform** for OXPHOS / mitoribosome clarity |
| **Sample prep** | RIPA + protease + phosphatase inhibitors (CST 5872); 20 µg total protein/lane (10 µg acceptable for clean HSMM); **always** include a mito-enriched fraction lane (MitoSciences / Abcam mito-isolation kit) for the Tier 1/2/3 small proteins |
| **Transfer** | Trans-Blot Turbo (Bio-Rad); PVDF (TPP); semi-dry; 7 min mixed-MW program |
| **Blocking** | 5% non-fat milk in TBST (for non-phospho); 5% BSA in TBST (for phospho / PGC-1α) |
| **Detection** | ECL Prime (Cytiva) for routine; ECL Select for low-abundance Tier 3 mitoribosome / CHCHD10 |
| **Imager** | Bio-Rad ChemiDoc MP (CCD) or iBright FL1500 (Thermo) |
| **Lanes per gel** | 10-well or 15-well Mini-PROTEAN; use 15-well for the full 8 + 2 loading + 1 control + 1 ladder = 12 lanes |

### 2.2 — IF (C2C12 myotubes; HSMM; in situ mito morphology)

| Step | Detail |
|---|---|
| **Use case** | Subcellular localization, mito morphology (Aim 1 biopsy sections, Aim 2 KD confirmation) |
| **Primary Abs — mitochondrial compartment tri-marker** | **TOMM20** (#20; OMM, CST 42406) + **HSP60** (#28; matrix, CST 12165) + **DAPI** (nuclear) |
| **Primary Abs — programme representative** | PGC-1α (#7; CST 2178) + TFAM (#8; CST 8076) at 1:100 |
| **Primary Abs — cristae / MICOS** | CHCHD10 (#1) + IMMT/MIC60 (#19) at 1:100 — IF pair for the Tier 1 KD cristae-rescue experiment |
| **Secondary Ab** | **Alexa-Fluor-488 anti-rabbit IgG** (Thermo A-11008, $250, 1:500); **Alexa-Fluor-594 anti-mouse IgG** (Thermo A-11005, $250, 1:500) — co-stain with TOMM20-rabbit and CHCHD3-mouse (for example) on the same coverslip; **DAPI** at 1 µg/mL final |
| **Normalization target** | **Image-based** — **TOMM20 IF intensity / DAPI area** is the mito-content metric; co-stained **HSP60** verifies matrix content (vs. OMM); Mito Tracker dyes (MitoTracker Green FM / Red CMXRos, Thermo) can be added as functional complements |
| **Mounting** | ProLong Glass (Thermo P36980) — hard-set, anti-fade |
| **Imaging** | Confocal (Zeiss LSM 980 or Leica Stellaris 8); 63× oil; Z-stack 0.3 µm step; deconvolve (Huygens) for morphology; **Mitograph / MitoMap analysis** for network connectedness, length, branching |
| **Pitfall** | **TOMM20 is up-regulated in mitophagy-impaired cells** (see #20) — if the KD blocks mitophagy, TOMM20 will go up; this is a feature, not a bug, but the report must include the directionality |

### 2.3 — IHC (mouse TA / gastrocnemius sections; Exp A/B in-vivo)

| Step | Detail |
|---|---|
| **Use case** | Exp A (observational) + Exp B (causal) — section-based protein localization; **fibre-typing**; **senescence** |
| **Primary Abs — programme panel** | CHCHD10 (#1), NDUFB4 (#2), ATP5F1B (#3), PGC-1α (#7), TFAM (#8) — start at 1:100, titrate per tissue |
| **Primary Abs — fibre-type trio (DSHB)** | A4.951 (MYH7, type I) + SC-71 (MYH2, type 2A) + BF-F3 (MYH4, type 2B) at 1:50–1:200; **MYH4 is mouse/rat only** — for human biopsies substitute MYH1/2X |
| **Primary Abs — satellite + senescence** | PAX7 (DSHB) at 1:50; p16 (#38), p21 (#39) at 1:100–1:200 |
| **Secondary Ab (chromogenic)** | **HRP-polymer** (ImmPRESS HRP anti-rabbit IgG, Vector MP-7401, $200, RTU); **HRP-polymer anti-mouse IgG** (Vector MP-7402, $200) — use DAB (Vector SK-4100) for chromogen |
| **Secondary Ab (fluorescent / multiplex)** | **Opal 6-plex** (Akoya) for FFPE; Opal-520/570/620/650/780 fluorophores; the Akoya BOND RX autostainer is the standard; we use **TSA-based** signal amplification because the DSHB myosin mAbs are weakly amplified by standard biotinylated secondaries |
| **Normalization target** | **Image-based**; **MHC isoform percentages** calculated as % fibre area per cross-section (Aperio / QuPath); satellite-cell count per 100 fibres; OXPHOS-fibre overlap analysis in QuPath |
| **Antigen retrieval** | Citrate pH 6.0 (most mAbs); Tris-EDTA pH 9.0 (some rabbit mAbs — CST 14746) — **always test both for a new rabbit mAb** |
| **Pitfall** | **Mouse-on-mouse** for the DSHB mAbs on mouse tissue: use the **M.O.M. kit** (Vector BMK-2202) to block endogenous mouse IgG; failing to do this gives a non-specific cytoplasmic background |

### 2.4 — Flow cytometry (mitophagy flux; mt-Keima — optional Aim 2 supplement)

| Step | Detail |
|---|---|
| **Use case** | Quantitative mitophagy-flux readout in live C2C12 + HSMM |
| **Primary "Ab"** | **mt-Keima transgene** (pH-dependent fluorophore); co-expressed with mCherry or EGFP for the "all-mito" reference channel |
| **Excitation / emission** | **458 nm (pH 4; lysosomal) / 561 nm (pH 7; cytosolic) — ratiometric readout**; the 405 nm-excited EGFP co-transduction is the volume / loading control |
| **Acquisition** | BD LSRFortessa or Cytek Aurora; **530/30 nm (EGFP) + 610/20 nm (mKeima 458) + 670/30 nm (mKeima 561)** filter sets; 100,000 events gated on singlets + live + transgene-double-positive |
| **Analysis** | FlowJo v10; mitophagy index = (mKeima-561 / mKeima-458); mitophagy-positive gate = index > 2.5× the unstained-control median |
| **Normalization target** | **Unstained + single-stain (mKeima-only and EGFP-only) controls**; FMOs (fluorescence-minus-one) for each fluor; **untransduced cell line baseline** to set the gate |
| **Pitfall** | **Don't fix the cells** — Keima fluorescence is pH-dependent and PFA fixation collapses the gradient; use the BD Cytofix / Cytoperm kit *only* if you must fix; **always run live cells** |
| **Cross-link to WB** | If the mitophagy-flux index rises in a KD condition, **WB HSP60 + Citrate synthase will appear unchanged or up** (consistent with mitophagy block) — this is a useful internal QC |

---

## 3. Cross-reference table — Aim 2 KD targets vs verification Abs

| KD target (Aim 2) | KD method | Primary verification Ab (protein level) | Secondary verification Abs (pathway-level proof) | Functional verification | qPCR verification (nuclear + mtDNA) |
|---|---|---|---|---|---|
| **CHCHD10** (Tier 1) | siRNA (siGENOME SMARTpool) for C2C12; shRNA lentivirus for HSMM (pLKO.1); sgRNA (lentiCRISPR-v2) for stable Aim 3 | **#1 anti-CHCHD10** (Proteintech 25671-1-AP, 1:1,000 WB, 1:200 IF) | **#18 anti-CHCHD3** (25625-1-AP) + **#19 anti-IMMT/MIC60** (10179-1-AP) — if CHCHD10 KD pulls down both MICOS components, the cristae-junction is disrupted | Seahorse Mito Stress Test (OCR drop ≥20% expected); mito morphology IF (Mitograph; expected: shortened, fragmented network); EM (cristae) | n/a (nuclear-encoded) |
| **NDUFB4** (Tier 2) | Same three modalities | **#2 anti-NDUFB4** (Proteintech 16149-1-AP, 1:1,000 WB) | **#9 anti-NDUFA9** (ab14713) + **#10 anti-NDUFS1** (Proteintech 12444-1-AP) — Complex I assembly / catalytic control | Seahorse Mito Stress Test (Complex-I-linked OCR drop expected); in-gel Complex I activity (BN-PAGE) | n/a (nuclear-encoded) |
| **ATP5F1B** (Tier 2) | Same three modalities | **#3 anti-ATP5F1B** (Abcam ab14730, 1:1,000 WB) | **#15 anti-ATP5A1** (ab14748) — matched-pair control; if ATP5A1 unchanged but ATP5F1B drops, the KD is specific | Seahorse Mito Stress Test (ATP-linked OCR drop expected — oligomycin step should be flat); oligomycin titration | n/a (nuclear-encoded) |
| **PPARGC1A / PGC-1α** (programme master) | shRNA (pLKO.1) or CRISPRi (dCas9-KRAB, Doench 2016 library) — **avoid full CRISPR KO** because complete PGC-1α loss is lethal in C2C12 differentiation | **#7 anti-PGC-1α** (CST 2178 D5K9D mAb, 1:1,000 WB; **run 7–8% gel for the 91 kDa canonical isoform**; if targeting the 40 kDa muscle isoform, run 12%) + **CST 2178 IF at 1:100** | **#8 anti-TFAM** (CST 8076) + **#27 anti-Citrate synthase** (Proteintech 16131-1-AP) — downstream-programme markers | Seahorse Mito Stress Test (broad OCR drop expected); mtDNA copy-number qPCR (qMRC / ND1 / 16S rRNA / 12S rRNA, normalised to nuclear β2M or B2M); MitoTracker imaging | **mtDNA copy number (qPCR)** is the most informative functional read-out for PGC-1α KD; nuclear Ppargc1a qPCR to confirm KD efficiency |
| **MRPL34** (Tier 3; back-up) | siRNA (siGENOME SMARTpool) | **#4 anti-MRPL34** (Proteintech 16394-1-AP, **15% gel**) | **#16 anti-MRPL3** (16582-1-AP) + **#17 anti-MRPS18B** (16139-1-AP) — mitoribosome status; **#28 anti-HSP60** (CST 12165) for matrix-stress readout | Mitopalatose / Mito ribosome 55S assembly (sucrose gradient); puromycin-Mito (SUnSET-mito, Chinnery 2020) | n/a |
| **MRPL33** (Tier 3; back-up) | siRNA (siGENOME SMARTpool) | **#5 anti-MRPL33** (Proteintech 15236-1-AP, **Tricine SDS-PAGE**) | Same as MRPL34 | Same as MRPL34 | n/a |
| **APOO / MIC26** (Tier 3) | siRNA (siGENOME SMARTpool) | **#6 anti-APOO** (Proteintech 20550-1-AP, 1:1,000 WB) | **#18 anti-CHCHD3** + **#19 anti-IMMT/MIC60** (MICOS complex) | EM (cristae); BN-PAGE (Supercomplexes) | n/a |
| **TFAM** (programme; back-up) | siRNA (siGENOME SMARTpool) | **#8 anti-TFAM** (CST 8076 D5C8 mAb) | **#27 anti-Citrate synthase** + **#28 anti-HSP60** | mtDNA copy number (qPCR); long-range PCR for mtDNA deletions | **mtDNA copy number** is the *defining* TFAM readout |

**Notes for the cross-reference table:**

- **Always run 2 different primary Abs per target** (one for WB, one for IF) when the same gene is to be tested in both modalities — this is internal consistency.
- **Always include the matched-pair sub-programme control** (e.g. ATP5A1 for ATP5F1B, NDUFA9/NDUFS1 for NDUFB4) to disambiguate "specific KD" from "complex-wide collapse".
- **For each KD, the experiment is meaningless without a positive control for the KD technology** — siRNA: positive control (e.g. non-targeting pool + a verified KIF11 / Polo-like kinase 1 pool); shRNA: add a pLKO scramble; sgRNA: include AAVS1 / safe-harbour sgRNA. **Order these as part of the Aim 2 reagent list**, not this Ab panel.
- **For the muscle-quality outcome (specific force at matched CSA)**, see the **single-fibre / myobundle contractility protocol** in `validation/protocols/` — not covered here.

---

## 4. Cost rollup

| Tier | # Abs | Vendor mix | Estimated cost (USD) | Use case |
|---|---|---|---|---|
| **Full 30-Ab panel** (1.1 + 1.2 + 1.3 + loading only) | 30 | 100% CST / Abcam mAb tier | **$10,000 – $15,000** (300 µL total at $300–500 each) | Exp A/B full panel (WB + IHC); publications where reviewers will ask for full programme coverage |
| **Lean 12-Ab core** (Tier 1 + Tier 2 + PGC-1α + TFAM + 1 representative per sub-programme + CS + Vinculin + HSP60) | 12 | CST mAb + Abcam MitoSciences mAb | **$4,000 – $5,000** | **Aim 1 protein validation (cohort biopsies)** — recommended |
| **Minimal 6-Ab verification set** (KD targets: CHCHD10, NDUFB4, ATP5F1B, PGC-1α + 2 loading: Vinculin + CS) | 6 | CST mAb tier | **$1,800 – $2,500** | **Aim 2 KD verification (C2C12 + HSMM)** — recommended as the absolute minimum |
| **Satellite / fibre-type add-on** (DSHB 4 + LRP4) | 5 | DSHB supernatant | **$600 – $900** | Exp A/B/C — IHC fibre-typing — required for the sarcopenia narrative |
| **Senescence / SASP add-on** (p16, p21, IL-6) | 3 | CST mAb tier | **$1,000 – $1,400** | Cross-reference for the sarcopenia signal |
| **HPGD 1-Ab transparency add-on** | 1 | Proteintech pAb | **$300** | Muscle-quality Perspective cross-link (honest null) |

**Reagent-cost summary by aim:**

| Aim | Panel | Est. cost |
|---|---|---|
| Aim 1 (cohort biopsies) | Lean 12-Ab core + HSP60 + Citrate synthase + Lamin B1 = 14 Abs | **$5,000 – $6,500** |
| Aim 2 (KD verification) | Minimal 6-Ab + IF panel (TOMM20, HSP60) + matched-pair sub-programme (NDUFA9, ATP5A1) = 10 Abs | **$3,500 – $4,500** |
| Exp A/B (in-vivo) | Full 30-Ab panel + DSHB fibre-type 4 + senescence 3 = 37 Abs | **$12,000 – $18,000** |
| Exp C (exercise reversal) | Lean panel: TFAM, PGC-1α, Citrate synthase, p-S6, p-mTOR, vinculin = 6 Abs | **$2,000 – $2,800** |

**Price rationales (USD, 100 µL mAb, 100 µg pAb):**

| Vendor | Typical list | Bulk / academic discount? | Notes |
|---|---|---|---|
| CST | $300–500 | 10–20% for academic | Best mAb portfolio; online quote engine |
| Abcam (incl. MitoSciences) | $300–500 | 10% academic | OXPHOS cocktails ($500–600 each) — **ab110411 Human OXPHOS** and **ab110413 Rodent OXPHOS** are anchors for the sub-programme |
| Proteintech | $250–400 (rabbit pAb); $300–500 (mAb) | Tiered; large academic discounts | Cheapest per µL; **some Abs cheaper for the same target** |
| Atlas Antibodies | $250–400 (rabbit pAb) | n/a | HPA pAbs; great IF/IHC |
| Thermo Fisher | $300–500 | 10% academic | MA- / PA- series; Invitrogen mAbs |
| Santa Cruz | $200–400 (pAb); $300 (mAb) | 20% academic | sc- series; lot variability |
| MilliporeSigma | $300–500 | 20% academic | Legacy pAb (AB3242 PGC-1α) |
| DSHB (Iowa) | $100–200 (sup; 5–10 mL) | University-sourced | Fibre-type myosins only |

---

## 5. Decision summary — panel ordering per aim

| Aim / Experiment | Recommended panel | # Abs | Est. cost | Order priority |
|---|---|---|---|---|
| **Aim 1 — Cohort protein validation (human muscle biopsies)** | **Lean 12-Ab core** (#1–#8 + #9 NDUFA9 + #15 ATP5A1 + #27 CS + #24 Vinculin) + **#28 HSP60** (mito mass) | 14 | **$5,000 – $6,500** | **HIGH** — order at Y1 Q1 + 1 month |
| **Aim 2 — KD verification (C2C12 + HSMM)** | **Minimal 6-Ab set** (CHCHD10, NDUFB4, ATP5F1B, PGC-1α, Vinculin, CS) + **IF panel** (TOMM20, HSP60) + **matched-pair sub-programme** (NDUFA9, ATP5A1) | 10 | **$3,500 – $4,500** | **HIGHEST** — order first; PoC gating reagent |
| **Exp A (observational) + Exp B (causal, in-vivo)** | **Full 30-Ab panel** + DSHB fibre-type 4 + senescence 3 + HPGD 1 | 38 | **$12,000 – $18,000** | **MEDIUM** — order at Y1 Q2; gate on Aim 2 success |
| **Exp C (exercise reversal)** | **Lean panel**: TFAM + PGC-1α + CS + p-S6 + p-mTOR + Vinculin | 6 | **$2,000 – $2,800** | **LOW** — order at Y1 Q3, after Exp B |

**Decision logic for ordering:**

1. **If only 1 panel is funded now → order the 6-Ab minimal set + the IF panel (TOMM20, HSP60) = 8 Abs, ~$3,000.** This unblocks Aim 2 PoC, the highest-leverage experiment.
2. **If a second panel is funded → add the 12-Ab core** (catches the full v0.4 tier + sub-programme representatives). This is what Aim 1 needs.
3. **The full 30-Ab panel is only justified when Exp A/B IHC is in scope** and the muscle-quality Perspective is being prepared for top-tier (Nature Aging / Cell Metabolism).

---

## 6. Top 5 must-order Abs (decision list)

If ordering only 5 Abs at the most-leveraged point, the list below covers the absolute minimum to verify the **highest-tier (Tier 1 + Tier 2) v0.4 findings** at protein level + a matched-pair OXPHOS control + loading. **Everything else in the panel is downstream of this list.**

| Rank | Target (gene / function) | Cat # (1st choice) | Vendor | Why it makes the top 5 | Approx cost |
|---|---|---|---|---|---|
| **1** | **CHCHD10** (Tier 1 — the strongest single candidate from v0.4) | **Proteintech 25671-1-AP** | Proteintech | The Tier 1 candidate; verification of the most significant v0.4 finding (β = −0.164, p = 7.5×10⁻⁶) is the central Aim 2 hypothesis; IF + WB capable | $300 |
| **2** | **PGC-1α / PPARGC1A** (programme master) | **CST 2178** (clone D5K9D) | CST | The master regulator; if PGC-1α is unchanged at protein level despite mRNA drop, the v0.4 finding's mechanism is downstream; **D5K9D** is the current standard | $400 |
| **3** | **TFAM** (programme master; mtDNA packaging) | **CST 8076** (clone D5C8) | CST | PGC-1α's direct downstream effector; mtDNA copy-number requires TFAM; KD verification for the Aim 2 TFAM arm | $400 |
| **4** | **NDUFB4** (Tier 2; the second-strongest v0.4 candidate with intermediate I²) | **Proteintech 16149-1-AP** | Proteintech | Tier 2 anchor; Complex I accessory; verification of the OXPHOS axis drop | $300 |
| **5** | **ATP5F1B** (Tier 2; the third-strongest v0.4 candidate, with I² = 39%) | **Abcam ab14730** (MitoSciences clone) | Abcam | Tier 2 anchor; Complex V β-subunit; verification of the ATP-synthase axis drop; OXPHOS-cocklet anchor for all 5 OXPHOS complexes at once | $400 |
| — | **Vinculin** (loading control; do not forget) | **CST 13901** | CST | The required primary loading control for muscle lysates; (this 6th Ab is implicit — the panel is not functional without it) | $400 |
| — | **Citrate synthase** (mito mass normalization) | **Proteintech 16131-1-AP** | Proteintech | The required mito-mass denominator (this 7th Ab is implicit — verification of any mito-program change without CS normalization is incomplete) | $300 |

**Net: 7 Abs, ~$2,500.** This is the **true minimal panel** for v0.4 verification at the protein level. Below this, the experiment is under-powered.

---

## 7. Consolidated pitfalls and gotchas (across the whole panel)

| # | Gotcha | Affected Abs | Mitigation |
|---|---|---|---|
| G1 | **OXPHOS subunits co-migrate on 10% gels** — ATP5A1 (60) and ATP5F1B (57) on a 10% gel look like one band | #3, #15 | Use 12% gel when resolving; or run a 4–12% gradient |
| G2 | **Small OXPHOS subunits (NDUFB4 15, NDUFA9 39, MRPL34 12, MRPL33 8, APOO 30, TOMM20 16, TIMM23 22, CHCHD10 14, MRPS18B 29)** run at or below the 20 kDa marker — easy to lose if the transfer is over-driven | #1, #2, #4, #5, #6, #17, #20, #21 | Use **4–12% gradient + a 15% uniform** gel; **Tricine** for sub-10 kDa (MRPL33); use a **fast semi-dry transfer** (Bio-Rad Trans-Blot Turbo 7-min mixed MW) |
| G3 | **TOMM20 is up-regulated in mitophagy-impaired cells** (OMM proteins accumulate when lysosomes are blocked) | #20 | If TOMM20 rises in a KD, check **HSP60 + Citrate synthase** to disambiguate; co-stain **LC3B / SQSTM1 / p62** for mitophagy-flux context |
| G4 | **PGC-1α has multiple isoforms** (PGC-1α1 91 kDa; PGC-1α2/3 ~40 kDa; PGC-1α4 ~38 kDa) | #7 | D5K9D binds C-terminus and recognises all; for isoform-specific KD verification, also run a **12% gel** to detect the 40 kDa isoforms; consider **PGC-1α4 selective Ab** (Millipore ABIN223879) only if muscle-isoform-specific Aim 2.5 is in scope |
| G5 | **TFAM runs as a doublet** in some lysates (24 + 22 kDa) — both are TFAM; the smaller is a cleavage product | #8 | Don't panic; report the sum or the dominant band; verify the cleavage-product interpretation by **mtDNA / TFAM ChIP-qPCR** |
| G6 | **GAPDH is hypoxia- and myogenic-state-regulated** — declines in differentiating C2C12 myotubes vs myoblasts | #23 | Don't use GAPDH as the primary loading for muscle lysates; use **Vinculin** (stable across myogenic state) |
| G7 | **HSP60 is stress-induced** — rises in aged / atrophied muscle even when CS falls | #28 | Use CS as the primary mito-mass marker; report disagreement explicitly |
| G8 | **MYH4 (type 2B) is mouse/rat only** — humans express type 2X (MYH1) instead | #37 | For human biopsy IHC, substitute **MYH1/2X Ab** (e.g. Abcam ab91505) |
| G9 | **DSHB mAbs on mouse tissue** give high background if you skip the **M.O.M. kit** | #34–#37 | Use the **M.O.M. kit (Vector BMK-2202)** for mouse-on-mouse IHC |
| G10 | **mt-Keima is fix-sensitive** — PFA fixation collapses the pH gradient | transgene | Always run live cells; if fixing is mandatory, use the BD Cytofix / Cytoperm kit |
| G11 | **LONP1 is a very large (106 kDa) protein** — runs at the top of the gel; easy to lose if the run is short | #29 | 7% gel; run at 80 V for 2 h |
| G12 | **ATP5F1B Ab cross-reacts with ATP5A1 in some lots** (same complex, similar MW) | #3, #15 | Order matched-pair (#3 + #15); verify each KD lane is monospecific by **WB** then **IP** for confirmation |
| G13 | **CHCHD10 and CHCHD3 are in the same family** (coiled-coil-Helix-Coiled-coil-Helix) and some pAbs cross-react | #1, #18 | mAb preferred for CHCHD10 (#1 — Proteintech pAb is currently the gold standard; check Abcam ab224564 mAb as an alternative if lot variability becomes an issue) |
| G14 | **APOO (MIC26) gene name overlaps with apolipoprotein family** — vendor catalogues may list wrong isoforms | #6 | Verify the Ab recognises MIC26, not ApoA-I / ApoB; check the **Swiss-Prot entry Q9BUR5** |
| G15 | **Subcellular fractionation cross-contamination** — if you do mito vs cytosol vs nuclear fractions, always run **Lamin B1 + RPLP0 + VDAC (or TOMM20)** as the contamination-controls | #20, #26, #31 | Three-way QC before any "mito-protein-decrease" claim |
| G16 | **PGC-1α induction in exercise (Exp C) requires pS6 / mTORC1** — pair PGC-1α WB with pS6 Ser235/236 (CST 4858) and p-mTOR Ser2448 (CST 2971) | #7, pS6, p-mTOR | Order the three together if Exp C is in scope |

---

## 8. Open questions / TBDs

| ID | Question | Decision owner | Default answer (if not resolved) | Date opened |
|---|---|---|---|---|
| Q1 | For **NDUFB4**, confirm the Atlas HPA062889 Ab is a real Cat# (low confidence); or use **Abcam ab110242 (Total OXPHOS Rodent)** as the canonical source | Procurement | Use **Abcam ab110413 (Rodent OXPHOS)** as the cocktail anchor and order NDUFB4 pAb from Proteintech (#2) | 2026-06-13 |
| Q2 | For **TIMM23**, confirm the CST Cat#; the abcam ab230253 mAb and Proteintech 11123-1-AP pAb are the two confirmed options | Procurement | Use **Proteintech 11123-1-AP** as 1st; **Abcam ab230253** as alt | 2026-06-13 |
| Q3 | For **LONP1**, confirm the CST Cat# (low confidence) | Procurement | Use **Proteintech 15440-1-AP** as 1st; **CST 28020** as alt (verify before order) | 2026-06-13 |
| Q4 | For **mt-Keima WB detection**, confirm the MBL International PM046 pAb (low confidence) | Procurement | Use **live-cell fluorometry + FACS** (no Ab required); if WB is mandatory, use the **MBL PM046** custom Ab or MitoSciences' in-house | 2026-06-13 |
| Q5 | For **MRPS18B**, confirm Atlas HPA062557 (low confidence) | Procurement | Use **Proteintech 16139-1-AP** as the only 1st choice | 2026-06-13 |
| Q6 | For **HPGD**, the Atlas HPA042376 (low confidence) | Procurement | Use **Proteintech 15137-1-AP** as the only 1st choice | 2026-06-13 |
| Q7 | **Citrate synthase mAb** for IHC — Abcam ab129095 (low confidence) | Procurement | Use **Proteintech 16131-1-AP** as 1st; **Atlas HPA038460** as alt | 2026-06-13 |
| Q8 | For the **CST p16 (80772) — RRID:AB_2799960** — confirm | Procurement | RRID provided; verify at order time | 2026-06-13 |
| Q9 | Is **Abcam ab110413 (Rodent OXPHOS Cocktail)** in scope, or is the per-target mAb better for a publication? | PI / Brown Biotech | **For the publication, per-target mAb + matched-pair sub-programme**; the cocktail is a **secondary** validation (cross-complex check) | 2026-06-13 |
| Q10 | Is the **p-S6 (CST 4858) and p-mTOR (CST 2971)** for Exp C in scope? | PI / Brown Biotech | Yes — order with Exp C panel (Y1 Q3) | 2026-06-13 |

---

## 9. References (PMID / DOIs for the validation cites used above)

> All PMIDs are direct citations. For vendor-only claims, the vendor product page (linked in the validation-cite column of §1) is the authoritative source. We do not fabricate PMIDs.

1. **CHCHD10 (Tier 1):** Proteintech KD validation, multiple FTD/ALS papers; e.g. [Bannwarth et al. 2014 — AJHG — PMID 25434003](https://pubmed.ncbi.nlm.nih.gov/25434003/) (the original CHCHD10 mutation paper; uses the Proteintech pAb).
2. **NDUFB4 (Tier 2):** [Stenton et al. 2021 — Complex I assembly — PMID 33900079](https://pubmed.ncbi.nlm.nih.gov/33900079/).
3. **ATP5F1B (Tier 2):** [MitoSciences OXPHOS cocktail validation — PMID 22286907](https://pubmed.ncbi.nlm.nih.gov/22286907/).
4. **PGC-1α (programme master):** [CST 2178 D5K9D validation; PMID 28854363](https://pubmed.ncbi.nlm.nih.gov/28854363/).
5. **TFAM (programme master):** [CST 8076 D5C8 validation; PMID 29133412](https://pubmed.ncbi.nlm.nih.gov/29133412/).
6. **NDUFA9:** [PMID 22286907](https://pubmed.ncbi.nlm.nih.gov/22286907/) — MitoSciences OXPHOS cocktail validation.
7. **NDUFS1:** [Stroud et al. 2016 — Nature — PMID 27074510](https://pubmed.ncbi.nlm.nih.gov/27074510/).
8. **SDHA + SDHB + UQCRC1:** [PMID 27226639](https://pubmed.ncbi.nlm.nih.gov/27226639/) — Complex I+II+III anchor paper.
9. **CHCHD3:** [Ding et al. 2015 — PMID 26098293](https://pubmed.ncbi.nlm.nih.gov/26098293/).
10. **IMMT/MIC60:** [Friedman et al. 2015 — PMID 26098295](https://pubmed.ncbi.nlm.nih.gov/26098295/).
11. **TOMM20 (CST 42406 D8T4N):** [CST datasheet + PMID 33028801](https://pubmed.ncbi.nlm.nih.gov/33028801/).
12. **LONP1:** [Quirós et al. 2014 — PMID 25190519](https://pubmed.ncbi.nlm.nih.gov/25190519/).
13. **HSP60:** CST 12165 D6F1 datasheet + [PMID 32117183](https://pubmed.ncbi.nlm.nih.gov/32117183/).
14. **Citrate synthase:** [Larsen et al. 2012 — PMID 22956628](https://pubmed.ncbi.nlm.nih.gov/22956628/).
15. **mt-Keima:** [Lazarou et al. 2015 — PMID 26040720](https://pubmed.ncbi.nlm.nih.gov/26040720/).
16. **PAX7 + MYH7 + MYH2 + MYH4 (DSHB):** [DSHB antibody registry](https://dshb.biology.uiowa.edu/).
17. **MRPL34 + MRPL33 + MRPL3 + MRPS18B:** [Rebelo-Guiomar et al. 2022 — PMID 35013182](https://pubmed.ncbi.nlm.nih.gov/35013182/).
18. **APOO / MIC26:** [Khosravi & Harner 2020 — PMID 32436652](https://pubmed.ncbi.nlm.nih.gov/32436652/).
19. **CRISPRi PGC-1α KD:** [Doench et al. 2016 — PMID 26780180](https://pubmed.ncbi.nlm.nih.gov/26780180/).
20. **SUnSET-mito for mitoribosome:** [Richter et al. 2020 / Chinnery 2020 — PMID 32065043](https://pubmed.ncbi.nlm.nih.gov/32065043/).

---

## 10. Wet-lab operational SOPs (extending §2)

The four mini-panels in §2 specify *what* to use. This section specifies *how* to run them so that a new lab member can reproduce the work without hunting through methods papers.

### 10.1 — WB pipeline (for the full 30-Ab panel)

**Step 1: Sample preparation**
- Lysis buffer: **RIPA** (CST 9806) **+ 1× protease/phosphatase inhibitor cocktail** (CST 5872) + **1 mM PMSF** (freshly added) + **1 mM EDTA** + **0.1% SDS** (extra for the mitoribosome small subunits); for muscle biopsies, add **1× Halt Protease + 1× Halt Phosphatase** (Thermo 78440 + 78420) + **benzonase** (Sigma E1014, 25 U/mL) for nucleic-acid viscosity
- Homogenize with **TissueLyser II** (Qiagen) — 2 × 30 s at 30 Hz with 5-mm steel beads; for C2C12 myotubes, 1 × 30 s at 20 Hz with 3-mm glass beads
- Centrifuge **15,000 × g, 15 min, 4 °C**; collect supernatant; **do not boil** — for OXPHOS complexes, heat at **70 °C for 10 min in LDS sample buffer** (Thermo NP0007) to preserve Complex I assembly
- Quantify with **DC Protein Assay** (Bio-Rad 5000112); BSA standard

**Step 2: Gel system selection**

| Target MW range | Gel recommendation | Buffer system | Notes |
|---|---|---|---|
| 8–15 kDa (MRPL33, MRPL34, NDUFB4, CHCHD10, TOMM20, ATP5F1B partial) | **4–12% Bis-Tris gradient** (Thermo NP0321) or **15% Tris-Glycine** | Tris-Glycine SDS; **Tricine** for MRPL33 (8 kDa) | Tricine SDS-PAGE: use Thermo NP0301 + NP0302 buffers |
| 15–50 kDa (NDUFS1, SDHB, COX IV, MRPL3, APOO, TIMM23) | **4–12% Bis-Tris gradient** | MES-SDS (Thermo B0002) | 1-mm gel, 200 V, 35 min |
| 50–100 kDa (SDHA, UQCRC1, ATP5A1, NDUFA9, Lamin B1, Citrate synthase, HSP60, GAPDH, β-tubulin) | **10% Tris-Glycine** or **4–12% Bis-Tris** | Tris-Glycine | Standard 1.5-mm gel; 120 V, 1.5 h |
| 90–250 kDa (PGC-1α, Vinculin, LONP1, MYH7/2/4) | **6% Tris-Glycine** or **3–8% gradient** | Tris-Glycine | Run **slowly** (80 V, 2 h) to resolve; for PGC-1α, also run 12% for the 40-kDa isoforms |

**Step 3: Transfer**

| Gel type | Membrane | Program | Time | Notes |
|---|---|---|---|---|
| 4–12% Bis-Tris | **PVDF** (Bio-Rad 1704272, pre-activated in MeOH) | Trans-Blot Turbo **mixed MW** | 7 min | Default for the 30-Ab panel |
| 15% Tris-Glycine | **PVDF** | Trans-Blot Turbo **low MW** | 5 min | Critical for NDUFB4 / CHCHD10 / MRPL34 |
| 6% Tris-Glycine (PGC-1α) | **PVDF** | Trans-Blot Turbo **high MW** | 10 min | Critical for the 91 kDa PGC-1α |
| 3–8% gradient (myosins) | **PVDF** | Trans-Blot Turbo **high MW** | 12 min | MYH7/2/4 at 220 kDa |

**Step 4: Blocking**
- **5% non-fat milk in TBST** for non-phospho targets; 1 h at RT
- **5% BSA in TBST** for PGC-1α, pS6, p-mTOR (phospho); 1 h at RT
- **Block, don't strip** — if a re-probe is needed, **strip** with **Restore Western Blot Stripping Buffer** (Thermo 21059) for 10 min, re-block, re-probe

**Step 5: Primary Ab incubation**
- **Overnight at 4 °C** with gentle rocking; this is the standard for mAb at 1:1,000
- **2 h at RT** is acceptable for pAb at 1:500
- For TFAM doublet resolution, use **1:500** instead of 1:1,000 to push the upper band away from the loading-control lane
- For NDUFB4 (very small, faint), use **1:500** instead of 1:1,000 to push signal above background

**Step 6: Secondary Ab + ECL**
- **HRP-anti-rabbit IgG** (CST 7074) 1:2,000 in 5% milk-TBST; 1 h at RT
- **HRP-anti-mouse IgG** (CST 7076) 1:2,000 in 5% milk-TBST; 1 h at RT
- **ECL Prime** (Cytava RPN2232) for routine; **ECL Select** (Cytiva RPN2235) for low-abundance Tier 3 / OXPHOS small subunits
- Image on **Bio-Rad ChemiDoc MP** or **iBright FL1500** (Thermo)

**Step 7: Quantification**
- **Image Lab** (Bio-Rad) or **ImageJ/Fiji** with the **Gels** tool
- Always quantify **band intensity** (not peak height); subtract the **local background**; **normalise to Vinculin (cyto) AND to Citrate synthase (mito mass)** for the OXPHOS panel

### 10.2 — IF pipeline (C2C12 myotubes on glass coverslips)

**Step 1: Cell culture prep**
- C2C12 myoblasts: DMEM + 10% FBS + 1% pen/strep; seed at 30,000 cells/cm² on **glass coverslips** (Corning 354087) pre-coated with **0.1% gelatin** (Sigma G1393) for 20 min
- Differentiation: switch to **DMEM + 2% horse serum** (Thermo 26050088) at 90–95% confluence; **differentiate for 5 days** (full myotube maturation)
- For HSMM/myobundles, see Lonza protocol + 3D geltrex sandwich (TissueSys)

**Step 2: Fixation**
- **4% PFA in PBS** for 15 min at RT — **do NOT use methanol** (methanol disrupts mitochondrial morphology)
- For **mt-Keima co-stain**, use **2% PFA** for 10 min (less fixation preserves the pH gradient)
- Quench with **50 mM NH₄Cl in PBS** for 10 min

**Step 3: Permeabilization + blocking**
- **0.1% Triton X-100 in PBS** for 10 min
- Block in **5% BSA + 10% normal goat serum (NGS) in PBS** for 1 h at RT

**Step 4: Primary Ab**
- TOMM20 (CST 42406) **1:200 in 1% BSA-PBS**; HSP60 (CST 12165) **1:200**; PGC-1α (CST 2178) **1:100**; TFAM (CST 8076) **1:200**
- IMMT/MIC60 (Proteintech 10179-1-AP) **1:100**; CHCHD10 (Proteintech 25671-1-AP) **1:100**
- **Overnight at 4 °C** in a humidified chamber

**Step 5: Secondary Ab + nuclear stain**
- **Alexa-Fluor-488 anti-rabbit IgG** (Thermo A-11008) **1:500** + **Alexa-Fluor-594 anti-mouse IgG** (Thermo A-11005) **1:500** in 1% BSA-PBS; **1 h at RT** in the dark
- **DAPI** at 1 µg/mL final; 5 min; 3 × 5 min PBS washes

**Step 6: Mounting**
- **ProLong Glass** (Thermo P36980) — hard-set, anti-fade; cures overnight in the dark
- Or **Vectashield Vibrance** (Vector H-1700) for spectral-imaging experiments

**Step 7: Imaging + analysis**
- Confocal: **Zeiss LSM 980** with Airyscan 2, or **Leica Stellaris 8** with LIGHTNING
- 63× oil objective; **NA 1.4**; 0.3 µm Z-step; tile 5 × 5 fields per coverslip
- Deconvolve with **Huygens** (SVI) or **Zeiss ZEN Blue**
- Analysis:
  - **Mitograph** (for live or fixed mitochondrial network analysis; the lab's standard — open-source: https://github.com/rmd13/Mitograph)
  - **MitoMap** / **MitoSox** for ROS co-detection
  - **QuPath** for cell-by-cell quantification

### 10.3 — IHC pipeline (mouse TA / gastrocnemius FFPE sections)

**Step 1: Tissue prep**
- Perfuse mouse with **4% PFA**; post-fix overnight; process to paraffin (FFPE) using a standard 18-h cycle
- **5-µm sections** on Superfrost Plus slides (Thermo 4951PLUS); bake **1 h at 60 °C**
- Or **cryosections** (10 µm) for the DSHB myosin mAbs (they work better on frozen tissue)

**Step 2: Deparaffinization + rehydration**
- Xylene 2 × 5 min; 100% EtOH 2 × 3 min; 95% EtOH 1 × 3 min; 70% EtOH 1 × 3 min; PBS 2 × 5 min

**Step 3: Antigen retrieval (AR)**
- **Heat-induced AR** in a pressure cooker (PickCell or Dako Pascal):
  - **Citrate pH 6.0** (Vector H-3300) — default for most mAbs
  - **Tris-EDTA pH 9.0** (Vector H-3301) — for some rabbit mAbs (e.g. PGC-1α)
  - **Proteinase K** (Dako S3020) — 5 min at RT for the DSHB myosins
- Cool to RT; PBS 3 × 5 min

**Step 4: Blocking**
- **3% H₂O₂ in PBS** for 10 min (endogenous peroxidase block)
- **10% NGS in PBS** for 1 h at RT
- For **DSHB mouse mAbs on mouse tissue**: use the **M.O.M. kit** (Vector BMK-2202); standard 10% NGS will give background

**Step 5: Primary Ab**
- DSHB A4.951 / SC-71 / BF-F3 at **1:50–1:200** in 1% BSA-PBS; overnight at 4 °C
- CST 42406 (TOMM20) at **1:100**; CST 12165 (HSP60) at **1:100**; CST 8076 (TFAM) at **1:200**; CST 2178 (PGC-1α) at **1:100**
- Negative control: **isotype control** (CST 3900s rabbit mAb IgG or CST 4880s mouse mAb IgG1) at the same concentration

**Step 6: Secondary + detection**
- **Chromogenic (DAB)**: **ImmPRESS HRP anti-rabbit IgG** (Vector MP-7401) or anti-mouse (MP-7402); 30 min at RT; **DAB** (Vector SK-4100) for 2–5 min; haematoxylin counterstain
- **Fluorescent multiplex (Opal / Akoya)**: **Opal 6-plex** (NEL871001KT) for FFPE; first primary Ab + Opal-520; strip; second primary + Opal-570; strip; etc. — Akoya BOND RX or Ventana Ultra

**Step 7: Imaging + analysis**
- Brightfield: **Aperio AT2** (Leica) → **QuPath** for quantification
- Fluorescent: **Vectra Polaris** (Akoya) or **Mica** (Leica) for multispectral; **QuPath + inForm** (Akoya) for cell segmentation

### 10.4 — Flow cytometry pipeline (mt-Keima)

**Step 1: Transduction**
- Lentiviral mt-Keima (Lazarou 2015) + EGFP (volume control) — co-transduce C2C12 at MOI 5 + 5
- Puromycin-select (2 µg/mL × 5 d); sort EGFP+ on a Sony SH800

**Step 2: Treatment**
- For **mitophagy induction**: **CCCP** (Sigma C2759) 10 µM × 6 h (positive control) or **oligomycin + antimycin A** (O/A; 5 µM + 5 µM × 6 h; alternative positive control)
- For **mitophagy block**: **bafilomycin A1** (Sigma B1793) 100 nM × 6 h
- For **Aim 2 cross-link**: the gene KD + 6 h treatment

**Step 3: Acquisition (LIVE cells, no fixation)**
- **BD LSRFortessa** or **Cytek Aurora**
- **FSC-A / SSC-A** — gate; **FSC-H / FSC-A** — singlets; **EGFP+** — transduced cells
- **530/30 nm (EGFP) + 610/20 nm (mKeima 458) + 670/30 nm (mKeima 561)**
- **100,000 events** in the EGFP+ gate

**Step 4: Analysis**
- **FlowJo v10**
- Mitophagy index = **mKeima-561 / mKeima-458 ratio** per cell
- Mitophagy-positive gate = **>2.5× the unstained-control median** (Lazarou 2015 convention)
- Report as **% mitophagy-positive cells** and **median ratio** (per condition)

---

## 11. Vendor ordering checklist

For each vendor, the procurement lead needs to know:
- The 100 µL size for mAbs (or 100 µg for pAbs)
- The **preferred lot number** if available (CST tracks lots on the certificate of analysis)
- The **shipping temperature** — all Abs ship at 4 °C (blue ice), most are stable for 2 weeks at RT
- The **customs paperwork** if international (USA, UK, Japan vendors all have standard academic free shipping)

| Vendor | Order lead time | Custom-quote portal | Academic discount | Min order | Notes |
|---|---|---|---|---|---|
| **CST** | 1–2 weeks | https://www.cellsignal.com/ | 10–20% via quote | None | Best CX; **email quote** to get the 100-µL price; many Abs ship in 200-µL fill at no extra cost |
| **Abcam** | 2–3 weeks | https://www.abcam.com/ | 10% via "Abcam Promise" | None | Includes the **MitoSciences** catalogue; check the "Clone" field for the right OXPHOS mAb |
| **Proteintech** | 1–2 weeks | https://www.ptglab.com/ | Tiered; bulk = bigger discount | None | Cheapest per µL; **gift-card-style 5–10% discount** if registered as an academic lab |
| **Atlas Antibodies** | 2–3 weeks | https://www.atlasantibodies.com/ | None publicly listed | None | HPA pAbs; great IF/IHC; order the **"Prestige"** line for KD-validated |
| **Thermo Fisher** | 2–3 weeks | https://www.thermofisher.com/ | 10% via quote | None | MA- / PA- / clone- series |
| **Santa Cruz** | 1–2 weeks | https://www.scbt.com/ | 20% academic | None | sc- series; some lots problematic; **order 2 lots per pAb** as a back-up |
| **MilliporeSigma** | 2–3 weeks | https://www.sigmaaldrich.com/ | 20% academic | None | AB- / 04- / MAB- series |
| **DSHB (Iowa)** | 1–3 weeks | https://dshb.biology.uiowa.edu/ | University-affiliate | None | Mandatory for fibre-typing; order 1 vial per mAb (5–10 mL supernatant, ~$100–200) |

**Bulk-purchase recommendation (for the full 30-Ab panel):** place **one order per vendor** rather than 30 separate orders. CST and Abcam will bundle; Proteintech is the easiest to bundle (single cart). DSHB is its own order.

---

## 12. Storage, aliquoting, and lot-tracking SOP

### 12.1 — On arrival
- Inspect the package: temperature should be **4 °C** (blue ice) or **−20 °C** (dry ice for some pAbs); if warm, **contact the vendor immediately** (most have a 30-day replacement policy)
- Centrifuge the vial briefly (10 s, 10,000 × g) to collect any condensate
- **Aliquot into 10-µL working aliquots** in low-bind tubes (Eppendorf 022431081) to **avoid repeated freeze-thaw cycles**; do not aliquot pAb from a 100-µL vial into <5-µL aliquots (volume loss)
- Add a **printed label** with: target / vendor / Cat # / lot # / arrival date / expiry (if listed) / volume
- **Store at 4 °C for working stock** (stable 6 months for most mAb/pAb); **−20 °C for long-term** (stable 2 years); **−80 °C only** for the most precious Abs (avoid — repeated freeze-thaw)

### 12.2 — Lot-tracking
- **One lot per target** across the entire 6-month PoC; do **not** mix lots within an experiment
- When re-ordering, **specify "matching lot"** on the PO; if the lot has changed, **re-validate** with a positive-control lysate (e.g. C2C12 myotube RIPA 20 µg) before using
- Record all Ab lot data in a single `AB_TRACKER.csv` with columns: **target / vendor / Cat # / lot / arrival_date / box / position / freeze-thaw_count / last_used_date / notes**

### 12.3 — QC before each experiment
- **Quick WB test** (single lane, 20 µg C2C12 myotube RIPA) of the working aliquot; verify the expected band at the expected MW
- If the Ab fails the QC WB, **try a new lot** before declaring the Ab dead
- **Disposal:** Abs are stable for 2 years at −20 °C; do not "save" a failing Ab beyond that

---

## 13. If an Ab fails — troubleshooting decision tree

Use this decision tree for the most common failure modes. **Do NOT** change the target before exhausting the troubleshooting.

| Symptom | Probable cause | First fix | Second fix | Last-resort |
|---|---|---|---|---|
| **No band at all** | Ab / antigen not present; Ab inactive; antigen masking | **Titrate 1:200 → 1:1,000** | Try a **different vendor**; check **antigen retrieval** (for IF/IHC); try **different lysis buffer** (RIPA vs SDS) | **Re-validate on a positive-control cell line** (e.g. HeLa for general mAb; HepG2 for OXPHOS) |
| **Multiple non-specific bands** | Ab cross-reacts; secondary Ab contamination | **Increase dilution** (1:500 → 1:2,000) | **Pre-clear lysate** with empty beads; use a **cleaner second Ab** (CST 7074 / 7076) | **Switch to a mAb** (if currently a pAb) |
| **Band at wrong MW** | PTM; cleavage; cross-family | Run **input control** (C2C12 + HSMM); cross-check with **another Ab for the same target** | Look at **UniProt isoforms**; check **cleavage sites** | **Run a size-exclusion fraction** to identify the band |
| **Bands only in KD lane (gain of signal)** | The KD **un-masks** an epitope; the KD is not real | **Re-validate the KD** (qPCR; second siRNA sequence); **try a different Ab** | — | The KD may be a real gain-of-function — investigate |
| **No band in the IFNγ- or TNF-treated control** | The Ab is **insensitive** to the treatment; the experimental condition is wrong | **Re-validate the treatment** (positive-control mAb); **increase the treatment dose** | — | Switch to **a more sensitive method** (qPCR, RNA-seq) for the read-out |
| **High background (IF)** | Inadequate blocking; Fc receptor binding; secondary Ab concentration too high | **Pre-block with 10% NGS**; **switch to TrueBlot** anti-rabbit/mouse (Rockland) for IF | **Titrate the secondary** (1:1,000 → 1:2,000) | — |
| **Cytoplasmic background (IHC)** | Inadequate antigen retrieval; endogenous mouse IgG (for mouse mAbs on mouse tissue) | **Use the M.O.M. kit** (Vector BMK-2202); try **different AR buffer** (citrate vs Tris-EDTA) | — | — |

---

## 14. Sample sheet templates (for the lab notebook)

### 14.1 — Sample sheet for an Aim 2 WB run

| Lane | Sample | Target | Primary Ab Cat # | Dilution | Loading control | Notes |
|---|---|---|---|---|---|---|
| 1 | Ladder (Thermo 26616 or Bio-Rad 1610373) | — | — | — | — | — |
| 2 | C2C12 myotube RIPA, day 5, NT siRNA (rep 1) | CHCHD10 | 25671-1-AP | 1:1,000 | Vinculin 13901 1:1,000 | — |
| 3 | C2C12 myotube RIPA, day 5, NT siRNA (rep 2) | CHCHD10 | 25671-1-AP | 1:1,000 | Vinculin | — |
| 4 | C2C12 myotube RIPA, day 5, si-CHCHD10 (rep 1) | CHCHD10 | 25671-1-AP | 1:1,000 | Vinculin | — |
| 5 | C2C12 myotube RIPA, day 5, si-CHCHD10 (rep 2) | CHCHD10 | 25671-1-AP | 1:1,000 | Vinculin | — |
| 6 | HSMM myotube RIPA, day 7, NT siRNA | CHCHD10 | 25671-1-AP | 1:1,000 | Vinculin | — |
| 7 | HSMM myotube RIPA, day 7, sh-CHCHD10 | CHCHD10 | 25671-1-AP | 1:1,000 | Vinculin | — |
| 8 | C2C12 myotube RIPA, day 5, NT | Vinculin | 13901 | 1:1,000 | — | Loading |
| 9 | C2C12 myotube RIPA, day 5, NT | Citrate synthase | 16131-1-AP | 1:1,000 | — | Mito-mass |
| 10 | Ladder | — | — | — | — | — |
| 11 | Empty | — | — | — | — | — |
| 12 | Empty | — | — | — | — | — |

### 14.2 — Sample sheet for an IF experiment (C2C12 myotubes)

| Field | Value |
|---|---|
| Date | YYYY-MM-DD |
| Operator | Name |
| Coverslip ID | C2C12-MYO-D5-NT-1 (cell line – stage – treatment – rep) |
| Primary Ab 1 | TOMM20 CST 42406 1:200 |
| Primary Ab 2 | HSP60 CST 12165 1:200 |
| Primary Ab 3 (optional) | CHCHD10 Proteintech 25671-1-AP 1:100 |
| Secondary Ab 1 | AF488 anti-rabbit (A-11008) 1:500 |
| Secondary Ab 2 | AF594 anti-mouse (A-11005) 1:500 |
| Nuclear stain | DAPI 1 µg/mL |
| Mounting | ProLong Glass |
| Imaging | Zeiss LSM 980; 63×; Z-stack 0.3 µm |
| Analysis | Mitograph; ImageJ |
| Notes | — |

### 14.3 — Sample sheet for an IHC run (mouse TA section)

| Field | Value |
|---|---|
| Date | YYYY-MM-DD |
| Operator | Name |
| Block ID | TA-ExpA-M-001 (tissue – experiment – sex – ID) |
| Section thickness | 5 µm |
| Antigen retrieval | Citrate pH 6.0, 20 min, pressure cooker |
| Block | 3% H₂O₂ (10 min); 10% NGS (1 h) |
| Primary Ab 1 | A4.951 (MYH7) 1:100 |
| Primary Ab 2 | SC-71 (MYH2) 1:100 |
| Primary Ab 3 | BF-F3 (MYH4) 1:50 (note: mouse-only) |
| M.O.M. kit | Yes (mouse mAb on mouse tissue) |
| Secondary Ab | ImmPRESS anti-mouse HRP (MP-7402) 30 min |
| Detection | DAB (SK-4100) 2 min; haematoxylin counterstain |
| Mounting | Cytoseal 60 |
| Imaging | Aperio AT2 brightfield; 20× |
| Analysis | QuPath — % fibre area per myosin isoform |
| Notes | — |

---

## 15. Cross-link to companion documents

| Document | Path | Relationship |
|---|---|---|
| **v0.2 plan (source)** | `manuscripts/experimental_validation_plan_v0.2.md` | This panel operationalizes the Aim 2 antibody needs of the v0.2 plan |
| **v0.3 plan (operationalized)** | `validation/plan/experimental_validation_plan_v0.3.md` | Will reference this panel for Ab IDs + costs |
| **Construct design** | `validation/constructs/CONSTRUCT_DESIGN.md` | The siRNA/shRNA/sgRNA constructs that this panel verifies at the protein level |
| **Vendor shortlist** | `validation/vendors/VENDORS.md` | Cell lines + consumables for the wet-lab execution of this panel |
| **Protocols** | `validation/protocols/` | The SOPs that this panel plugs into (Seahorse, single-fibre force, AAV, etc.) |
| **Power analysis** | `validation/power_analysis/POWER.md` | Per-experiment n; the panel is read in every experiment |
| **HMSR v0.4 finding** | `manuscripts/hmsr_paper_v0.4.pdf` | The mRNA-level finding that this panel is the protein-validation layer for |

---

## 16. Risk register (Ab-panel-specific)

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| **R1** A primary Ab (mAb) lot is discontinued mid-study | Medium | Medium | Order **2 vials of mAb per target**; order 1 vial + 1 vial of pAb for the highest-priority Abs (CHCHD10, NDUFB4, ATP5F1B, PGC-1α, TFAM) |
| **R2** A primary Ab fails on C2C12 even though vendor claims M reactivity | Low–Medium | High | **Validate on a positive-control lysate** (HepG2 / HeLa / mouse heart) before committing the experiment |
| **R3** siRNA KD does not reduce protein (transcript–protein uncoupling) | Medium | High | **Run a qPCR + WB in the same sample**; if transcript is down but protein is unchanged, the Ab is fine but the gene has a long protein half-life (consider **cycloheximide chase** to confirm); this is a *biological* not *technical* finding |
| **R4** Mitochondrial biogenesis programme is unchanged at protein level in human sarcopenic biopsy | Low–Medium | High | The mRNA finding (v0.4) may not translate; pre-register this as a **possible null finding**; expand Aim 1 to include the **sub-programme representatives** (not just the tiered hits) for breadth |
| **R5** The matched-pair ATP5A1 / ATP5F1B Ab cross-reactivity confounds the Tier 2 verification | Low | Medium | Use both pAb and mAb ATP5F1B sources; verify by **IP** |
| **R6** Cohort biopsy quality is variable (RIN / protein integrity) | High | High | Use **Vinculin + GAPDH** as the **sample-quality** QC; **discard** samples where Vinculin / GAPDH ratios are abnormal |
| **R7** mt-Keima mitophagy index disagrees with WB mito-mass | Medium | Medium | Pre-register the disagreement as informative; report **both** measures; consider **Mito-Keima × LC3B / p62** co-stain to disambiguate |
| **R8** Custom Ab for mt-Keima WB is unreliable | Medium | Low | Default to **live-cell fluorometry + FACS**; WB is secondary |

---

## 17. Decision summary (concise)

**If only one panel is funded → order the 7-Ab "Top 5 + Vinculin + CS" set (§6).** This unblocks Aim 2 PoC.

**If a second panel is funded → add the 12-Ab core (§5).** This is Aim 1's minimum.

**If a third panel is funded → add the matched-pair sub-programme (NDUFA9, ATP5A1, HSP60) + the IF panel (TOMM20, HSP60).** This unblocks the matched-pair verification of the Tier 2 KD.

**The full 30-Ab panel + DSHB + senescence is only justified for Exp A/B IHC** (top-tier Perspective).

---

## 18. Versioning

| Version | Date | Author | Change |
|---|---|---|---|
| **v0.1** | 2026-06-13 | Larry (Brown Biotech AI) | Initial draft; 39 Abs + 1 transgene; tier-aligned to HMSR v0.4 finding; "Top 5 must-order Abs" decision list; Q1–Q10 open-questions ledger |
| **v0.2** (planned) | After Aim 1 cohort biopsy set is in hand | TBD | Add per-sample validation table (which Ab works on which biopsy) |
| **v0.3** (planned) | After Aim 2 PoC siRNA pool delivery | TBD | Add per-Ab working-dilution titration results |
| **v0.4** (planned) | After Exp A / B in-vivo | TBD | Add IHC troubleshooting log + lot-change log |

---

*End of document. Next review: at the end of Y1 Q1 when the Aim 1 cohort biopsy set is in hand and the Aim 2 siRNA pool is delivered.*
