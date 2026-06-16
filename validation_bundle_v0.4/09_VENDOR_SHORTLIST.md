# HMSR Validation — Vendor and CRO Shortlist (v0.3, RFP-ready)

> **Branch:** `validation/aim2-causation` (worktree: `.worktrees/validation-aim2/`)
> **Worktree path:** `sarcopenia-multiomic-resource/validation/vendors/`
> **Document ID:** `validation/vendors/VENDOR_SHORTLIST.md` v0.1
> **Last updated:** 2026-06-13
> **Authors:** Larry (Brown Biotech AI partner) + HMSR validation working group
> **Status:** Draft for **RFP issuance** (target: quote requests in 1 week)
> **Companion documents:** `validation/README.md`; `validation/antibodies/ANTIBODY_PANEL.md`; `validation/protocols/SEAHORSE_MITO_STRESS_TEST_SOP.md`; `manuscripts/experimental_validation_plan_v0.2.md`

---

## 0. How to use this document

This shortlist covers **all major reagent, instrument, cell-line, and CRO categories** needed for the HMSR in-vitro + in-vivo validation program (Aims 1–3, Exp A–D) as defined in `experimental_validation_plan_v0.2.md`. It is organized into 14 sections (§1–§8 vendor categories; §9–§10 cost rollups; §11 decision summary; §12 RFP templates; §13–§14 references) that map 1-to-1 to the wet-lab categories, plus cost rollups and ready-to-send RFP templates.

**Important convention:** All prices are **list price in USD, approximate, current at the time of writing (mid-2026)** unless otherwise noted. Vendors revise prices routinely; an RFP quote may differ by ±10–25% from list. **All lead times are quoted as calendar weeks from purchase-order acceptance, not from quote inquiry.** Always confirm academic-discount eligibility (most vendors offer 10–25% off list for non-profit / academic institutions; some have tiered academic pricing via core facilities).

**The two critical-path long-lead items** (place orders first):
1. **AAV9 production** (VectorBuilder ultra-purified research-grade: 10–14 days for ultra-purified research, but expect 4–6 weeks for custom serotype + full QC)
2. **NIA aged-mouse colony** (free, but 4–8 weeks from order to delivery; 10–20 animals/month cap)

The next two long-lead items:
3. **Aged-mouse in-house aging** (must start 18–24 months in advance; cannot be expedited)
4. **iPSC editing + differentiation CRO service** (12–24 weeks end-to-end)

Everything else in this document can be ordered in 1–4 weeks.

---

## 1. Cell lines & primary cells (Aims 1, 2, 3)

| Cell type | Vendor | Catalog # | Price (USD) | Lead time | QC notes | Application (cross-ref) |
|---|---|---|---|---|---|---|
| C2C12 myoblast (mouse) | ATCC | **CRL-1772** | ~$540/vial (1 mL); academic discount available | 1–2 weeks | Mycoplasma-tested, ISP, STR-authenticated; passage ≤15 recommended; **ATCC authenticated by isoenzymes + STR** | Aim 2 primary screen (all Tier 1/2/3 KD); Aim 3 PGC-1α programme test |
| C2C12 subclone (high-fusion) | ECACC / Sigma (Merck) | **91031101** | ~$700 (academic €660 list, USD ~$700 with freight) | 2–3 weeks | Better myotube maturation; C3H mouse background; same subclone as ATCC CRL-1772 but distributed via ECACC | Aim 2 myobundle / 3D model; same as above (alt source) |
| C2C12 myoblast (mouse) — Sigma/Merck | Sigma-Aldrich | **91031101-1VL** (vial) or **91031101-DNA-5UG** (DNA only) | $750–900 (vial) or $300 (DNA) | 1–2 weeks | Same ECACC subclone, distributed by Sigma; COA included | Aim 2 (alt) |
| HSMM (human skeletal muscle myoblasts) | Lonza (Clonetics) | **CC-2580** (≥500,000 cells, cryopreserved, P2) | **$1,386.50 / amp** (Fisher Sci; Lonza list ~$1,511 in UK ≈ $1,500 USD; Cedarlane CDN $1,989) | 2–4 weeks; "low stock availability" common | Mycoplasma-, bacteria-, yeast-, fungi-, HIV-1-, HBV-, HCV-tested; **guaranteed through 10 population doublings** and to differentiate to myotubes; CoA per lot | Aim 1 (cohort validation), Aim 2 KD confirmation (human model) |
| HSMM — Diabetic Type I donor | Lonza (Clonetics) | **CC-2900** | ~$1,500 / amp | 2–6 weeks | Type I diabetic donor, ≥500,000 cells, P2 | Aim 4 supplement / diabetes-muscle crosslink (out of scope) |
| HSMM — Diabetic Type II donor | Lonza (Clonetics) | **CC-2901** | ~$1,500 / amp | 2–6 weeks | Type II diabetic donor | Aim 4 supplement (out of scope) |
| HSMM — proliferating (T-25, T-75, 96-well) | Lonza (Clonetics) | **CC-2580T25 / T75 / W96** | Quote (typically $1,800–2,500) | 2–4 weeks | Pre-plated; saves a thaw-and-expand week | If large-format screening needed |
| **HSMM — sarcopenic donor (custom)** | Lonza CellBio Services | **Custom** | Quote **$2,000–5,000 per donor** | **6–12 weeks** | **Requires MTA + donor consent**; age 70+; sarcopenia DXA-confirmed (appendicular lean mass / height² < 7.26 kg/m² for men, < 5.45 kg/m² for women — EWGSOP2) | Aim 1 protein confirmation (the human-relevance arm) |
| **iPSC-derived skeletal myocyte (healthy WT)** | **FUJIFILM Cellular Dynamics (FCDI)** | **iCell Skeletal Myocytes** (formerly SKM-100-010 series) | Quote (academic ~$2,500–3,500/kit; estimate 1–2 × 10⁶ cells/vial) | **4–6 weeks** | iPSC line, validated myogenic differentiation; myosin heavy chain + desmin + α-actinin; functional acetylcholine response | Aim 2 (human in-vitro iPSC model) |
| **iPSC-derived skeletal myocyte (healthy WT) — alt** | **bit.bio** | **ioSkeletal Myocytes (io1002)** | **$1,198 / 2-vial pack (small: >2.5×10⁶ cells)**; academic 3-vial pack $999 | **1–2 weeks** (in-stock); opti-ox deterministic reprogramming; mature striated myocytes by **Day 10 post-thaw** | **Significantly cheaper and faster than CDI**; lot-to-lot reproducibility a major advantage; mature in 10 days | Aim 2 (recommended alt to CDI) |
| **iPSC-derived skeletal myocyte (DMD model)** | bit.bio | **ioSkeletal Myocytes DMD** (custom) | Quote | 8–12 weeks | DMD exon 44 / 52 deletion available; functionally validated 3D microtissue model | Out of scope unless DMD-sarcopenia crosslink pursued |
| **iPSC-derived myocyte (CHCHD10 KO isogenic)** | CDI / Edit-R / Synthego + custom | **Custom line** | **$8,000–15,000 per line** (CRISPR edit + QC) | **8–14 weeks** | CRISPR-edited isogenic control pair (WT + KO); karyotype + off-target + myogenic validation | Aim 2/3 causal clean model (Tier 1 anchor) |
| **iPSC-derived myocyte (ATP5F1B KO isogenic)** | CDI / Edit-R / Synthego + custom | **Custom line** | **$8,000–15,000 per line** | **8–14 weeks** | Same as above, Tier 2 OXPHOS | Aim 2 (Tier 2) |
| **iPSC-derived myocyte CRO service (full service)** | Crown Bio / Cellectics / iPSC Core at Indiana U / Cedars-Sinai iPSC Core | **Custom project** | **$15,000–40,000 per project** (donor selection + edit + differentiation + assays) | **12–24 weeks** | Full service: iPSC line procurement, CRISPR KO design + execution, clone picking, karyotyping, off-target analysis, myogenic differentiation, baseline assays (IF + Seahorse) | Alternative to in-house iPSC editing |
| Mouse primary myoblasts (satellite-cell derived) | Cook Myosite | **Several lots** (e.g., SKB-01, SKM-01) | $400–600 / prep | 1–2 weeks | Fresh, freshly isolated from C57BL/6J; alternative to C2C12 | Aim 2 supplement (more physiological than C2C12) |

**MTA / licensing notes:**

- **C2C12 (ATCC CRL-1772):** Standard ATCC terms; no MTA required for academic use; **commercial use requires a license** (Yaffe & Saxel 1977 original).
- **C2C12 (ECACC 91031101):** Equivalent to ATCC CRL-1772; **free for academic non-commercial use**; **commercial use triggers an ECACC license fee**.
- **HSMM (Lonza CC-2580):** Standard Clonetics terms; **no MTA for normal-donor lots**; **custom-donor (sarcopenic) lots require a custom MTA + donor consent + additional paperwork** — plan 4–6 weeks lead time for the MTA on top of the cell delivery.
- **iPSC lines (CDI / bit.bio):** Standard academic use allowed; **commercial use requires a separate license agreement with the provider**; CDI is now part of FUJIFILM, and FCDI's CDMO services are the route for clinical-grade lines.
- **Addgene plasmids:** Standard UBMTA (Uniform Biological Material Transfer Agreement) — accepted by most institutions; for-profit use requires Addgene commercial pricing.

### 1.1 — Cell-line handling and authentication checklist (lab QC)

When each cell line arrives, the following QC must be run **before any experiment is started** (typically week 1 of the project). This is the *minimum* bar for publication-quality work; reviewers and journals will ask.

| QC step | Method | Pass criterion | Cost (USD) | Time |
|---|---|---|---|---|
| **Mycoplasma test** | PCR (e.g., ATCC Universal Mycoplasma Detection Kit 30-1012K) **OR** Hoechst DNA stain + fluorescence microscopy | **Negative** | $100–300 | 1 day |
| **STR authentication** (human lines only) | GenePrint 10 (Promega) or IDEXX CellCheck 9 | Match ≥80% to donor reference (Lonza / CDI provides this in the CoA) | $200–400 | 3 days |
| **Isoenzyme / species confirmation** (mouse lines) | ATCC Authentification Service or in-house isoenzyme gel | Mouse isoenzyme pattern | $200 | 1 week |
| **Karyotype** (iPSC lines, mandatory) | G-banding (20 metaphase spreads) or SNP array (Illumina Infinium) | Normal (no clonal abnormalities) | $300–500 | 1–2 weeks |
| **Differentiation validation** | Myosin heavy chain (MF20 or DSHB) IF; fusion index ≥30% by day 5 of differentiation | ≥30% fusion | $50 in Abs + 1 day | 1 day |
| **Population doubling** (HSMM) | Cell计数at every passage, cumulative PD chart | ≤10 PD (Lonza guarantee); not exceeding for the experiment | free | ongoing |
| **Sterility** (bacteria, yeast, fungi) | Standard microbiology (BACTEC or in-house) | Negative | $50 | 5–14 days |
| **Viral testing** (HIV-1, HBV, HCV) | CoA from Lonza / CDI is sufficient; **only re-test if growing >1 month** | Negative | included | — |

**Mycoplasma is the #1 silent contamination in academic muscle labs.** A 2022 survey of 360 academic cell-culture labs found **>30% of incoming lines were mycoplasma-positive**. The PCR test is the only reliable detector; **do not trust the vendor's CoA alone** — re-test every 4 weeks during active culture.

### 1.2 — Banking strategy: master + working + distribution stock

| Stock | Vials | Purpose | Storage |
|---|---|---|---|
| **Master stock (P + 1 to P + 2)** | 20–30 vials | Insurance against contamination / drift; never thawed for experiments | LN₂ vapour phase |
| **Working stock (P + 3 to P + 5)** | 30–50 vials | Used for active experiments; max 8 weeks in culture | LN₂ vapour phase |
| **Distribution stock** (optional) | 10–20 vials | Shared with collaborators; tracked in a lab database | LN₂ vapour phase |

**C2C12 specifically:** the cells differentiate spontaneously if kept at high density; **the master stock should be frozen at P+2 to P+3 (post-thaw expansion)**, and the working stock should never exceed P+15 (per the v0.4 plan). **Do not share C2C12 between labs without re-authentication** — the C2C12 line has a documented history of cross-contamination with non-muscle lines (HeLa, etc.).

### 1.3 — Custom sarcopenic HSMM donor — what to ask Lonza CellBio Services

| Question | Why it matters |
|---|---|
| **Donor age** | 70+ yo for sarcopenia; 30–60 yo for age-matched control |
| **Sarcopenia diagnosis** | EWGSOP2 (appendicular lean mass / height² < 7.26 kg/m² men, < 5.45 kg/m² women) — ask for the DXA scan report |
| **BMI** | 18.5–30; sarcopenic donors may have higher BMI (sarcopenic obesity) |
| **Comorbidities** | Diabetes, COPD, CHF, CKD are common; ask for the full clinical record |
| **Tissue source** | Quadriceps, psoas, or rectus abdominis (psoas is best for type-II fibre content); avoid post-mortem tissue (degraded RNA) |
| **Cell yield per gram** | ≥500,000 cells / vial is Lonza standard; expect 2–5 vials per donor |
| **Passage at delivery** | P2 (Lonza standard); request P0 if available (cleaner expansion in your lab) |
| **CoA included** | Mycoplasma, sterility, viral panel, isoenzyme, population doubling, donor demographics |
| **MTA terms** | Lonza standard academic; **commercial use requires a separate license** |
| **Lead time** | 6–12 weeks for custom donor; Lonza must locate, consent, biopsy, isolate, QC |

**Cost-saving tip:** If two academic groups request the same sarcopenic donor, **Lonza will share the cost** — coordinate with a sister lab in the sarcopenia field.

### 1.4 — iPSC line procurement: bit.bio vs CDI (FCDI) head-to-head

| Factor | bit.bio (ioSkeletal Myocytes) | FUJIFILM CDI (iCell Skeletal Myocytes) |
|---|---|---|
| **Price per 2-vial pack** | $1,198 (academic $999 per 3-pack) | Quote (~$2,500–3,500/kit) |
| **Lead time** | 1–2 weeks (in-stock) | 4–6 weeks (made-to-order) |
| **Reprogramming tech** | opti-ox (deterministic, transcription-factor-driven) | Episomal / Sendai virus (iPSC then directed differentiation) |
| **Time to mature myocyte** | 10 days post-thaw | 14–28 days post-thaw |
| **Lot-to-lot consistency** | Excellent (opti-ox is deterministic) | Variable (iPSC line + differentiation protocol) |
| **3D myobundle formation** | 3–5 days (in fibrin/Matrigel) | 7–14 days |
| **Functional: acetylcholine response** | Day 10 (mature) | Day 14–28 |
| **Striation / sarcomere** | Day 10 | Day 14+ |
| **Custom editing** | Quote; ~$10K–$20K per custom line | Quote; $8K–$15K per custom line |
| **Disease models in catalog** | DMD (exon 44 / 52 deletion) | R&D panels (e.g., DMD, SMA, FSHD); custom available |
| **License** | Standard academic; commercial separate | Standard academic; commercial separate |
| **Best for** | Routine Aim 2/3 in-vitro muscle work; budget-conscious | Specific disease models; iPSC-based clinical translation |

**Recommendation:** Use **bit.bio as the primary iPSC myocyte source** for Aim 2/3; use **CDI only if a specific disease model is needed that bit.bio doesn't have**. The 1–2 week lead time + 1/3 the price is a major advantage for the lean PoC budget.

---

## 2. siRNA / shRNA / CRISPR vendors (Aim 2 — causation arm)


| Vendor | Platform | Lead time | Catalog format | Price per target (USD) | Best for | Notes |
|---|---|---|---|---|---|---|
| **Horizon Discovery (Dharmacon)** | siGENOME, **ON-TARGETplus 2.0**, Edit-R CRISPR, Accell, Lincode (lncRNA) | 5–10 business days for in-stock oligos; 10–14 days for custom SMARTpool | 96-well plate, SMARTpool (4 oligos), Set of 4, individual oligos, library plates | **siGENOME SMARTpool: $116**; **ON-TARGETplus SMARTpool: $154**; **individual: $200–$300**; **control pools: $269**; **mouse + human + rat predesigned** | Initial screens, validated design, isogenic panels | **Industry standard**; guarantee: ≥75% mRNA KD at 100 nM with 3 of 4 individual oligos or SMARTpool; design algorithm is **SMARTselection** (Dharmacon); the new **ON-TARGETplus 2.0** has continuous transcriptome alignment for isoform coverage; 100 nM recommended, 5–20 nM often sufficient |
| **Thermo Fisher (Ambion)** | Silencer Select, TrueGuide CRISPR | 5–10 days | Individual oligos, validated Silencer Select, Ambion design | **~250/oligo** for Silencer Select; TrueGuide CRISPR kits ~$500–1,500 | Single-gene KD; co-transfection with Lipofectamine RNAiMAX | **Best-in-class individual siRNA**; predesigned for 99% of human + mouse + rat RefSeq; LNA-modified for nuclease stability; 3–5 nM working concentration typical |
| **Sigma (Merck / MISSION)** | MISSION shRNA, synthetic crRNA, Edit-R CRISPR | 7–14 days | Lentiviral particles or oligos; pLKO.1 backbone; TRC library | **~350 (shRNA lentivirus)**; **~200 (crRNA)**; **MISSION TRC library**: quote for genome-wide | Stable KD lines, CRISPR, genome-wide pooled screens | Comprehensive TRC (The RNAi Consortium) library (>200,000 shRNA constructs); **lentiviral shRNA for stable Aim 3 PGC-1α arm** |
| **IDT (Integrated DNA Technologies)** | Alt-R CRISPR (HiFi Cas9), TriFECTa RNAi, custom sgRNA | 5–10 days | Synthetic sgRNA + tracrRNA, Cas9 RNP, electroporation enhancers | **~200 (sgRNA)**; **~150 (individual siRNA)**; Alt-R HiFi Cas9 $400–500 | CRISPR KO (RNP), custom crRNA screens | **Alt-R HiFi Cas9 = higher-fidelity Cas9 variant** (1 of the best on the market for CRISPR KO with reduced off-target); good for Aim 3 isogenic |
| **Synthego** | Custom sgRNA, gene knockout kit, Cas9 protein | 5–10 days | Synthetic sgRNA (chemically modified), Cas9 RNP | **~100 (sgRNA)**; **$1,500 (knockout kit)** | Large CRISPR screens, fast turnaround | **Fastest turnaround in industry** for custom sgRNA; Spike-In detection by NGS available; widely used for pooled screens |
| **GeneCopoeia** | Lentiviral shRNA, CRISPR, ORFome | 10–14 days | Plasmid, lentivirus, ORF clones, CRISPR libraries | **~300 (plasmid)**; **~500 (lentivirus)**; ORF clones ~$400–800 | Stable KD, ORF rescue, custom cloning-free CRISPR | Free cloning for CRISPR all-in-one vectors; good for rescue experiments |
| **Twist Bioscience** | Custom sgRNA libraries, ORF, MISSION-style pooled | 14–21 days | DNA synthesis, pooled libraries | Quote for libraries; individual oligos ~$200 | Genome-wide CRISPR screens at scale | **Best for pooled CRISPR screens**; silicon-DNA synthesis gives lowest per-oligo cost at scale |
| **VectorBuilder** | Custom shRNA / sgRNA cloning, AAV / lentivirus delivery | 10–21 days | Plasmid, lentivirus, AAV | **~250 (shRNA cloning)**; **AAV-shRNA from $1,099** (ultra-purified research) | One-stop: design + cloning + virus packaging | Integrates with their AAV service; convenient for Exp B (AAV9-shRNA in vivo) |

### 2.1 — siRNA / shRNA / CRISPR decision algorithm

```
Q1: Is this a one-time KD for a single experiment (Aim 2 screen)?
   ├─ YES → siRNA (Horizon ON-TARGETplus 2.0 SMARTpool)
   └─ NO → Q2
Q2: Do you need a stable KD line (Aim 3 PGC-1α arm)?
   ├─ YES → shRNA lentivirus (Sigma MISSION or Horizon pLKO.1)
   └─ NO → Q3
Q3: Do you need a complete KO (not just KD)?
   ├─ YES → CRISPR (in-house IDT Alt-R HiFi Cas9 RNP, or CRO)
   └─ NO → siRNA is sufficient
Q4: Are you doing a pooled genome-wide screen?
   ├─ YES → Twist Bioscience custom pooled library, or Sigma MISSION TRC
   └─ NO → single-gene above
```

### 2.2 — siRNA design / validation per gene (best practice)

For each Tier 1/2/3 gene, order **at least 3 orthogonal siRNA oligos** (from different vendors if possible) to confirm the phenotype is not an off-target artefact. The minimum standard is:

| Tier | # of orthogonal siRNA oligos | Validation | If only 1 oligo works |
|---|---|---|---|
| **Tier 1 (CHCHD10)** | 4 (Horizon Set of 4) + 1 (Ambion Silencer Select) + 1 (Sigma) = 6 | qPCR + WB at 48h + 96h | If all 3 vendors' oligos give the same phenotype, the phenotype is on-target |
| **Tier 2 (NDUFB4, ATP5F1B)** | 4 (Horizon) + 1 (Ambion) = 5 | qPCR + WB at 48h + 96h | If 2 vendors' oligos agree, sufficient for paper |
| **Tier 3 (MRPL34, APOO, MRPL33)** | 4 (Horizon) | qPCR + WB | If 1 SMARTpool is sufficient (≥2 of 4 oligos work) |
| **Master (PPARGC1A, TFAM)** | 4 (Horizon) + 1 (Ambion) = 5 | qPCR + WB | If 2 vendors' oligos agree, sufficient |

**The "rescue experiment" is the gold-standard validation:** if the phenotype is rescued by an siRNA-resistant cDNA clone (e.g., GeneCopoeia ORF clone + silent mutations at the siRNA binding site), the phenotype is unambiguous. **This is the experiment Aim 2 should include for CHCHD10, ATP5F1B, PGC-1α.**

### 2.3 — Lentiviral shRNA considerations (Aim 3 stable lines)

| Aspect | Recommendation |
|---|---|
| **Backbone** | pLKO.1 (Sigma MISSION) or pLVTHM (Addgene #12247) — both well-cited, both work in C2C12 + HSMM |
| **Promoter** | U6 (constitutive) or H1 (constitutive) for shRNA; **do not use Tet-On for a 4-week experiment** (leakiness + induction kinetics) |
| **Selection** | Puromycin (2–5 µg/mL for C2C12, 1–2 µg/mL for HSMM) |
| **MOI** | <0.5 (to avoid multiple integrations) |
| **Pooling** | Pool 3–5 shRNA per target (pLKO.1-puro pooled transduction + selection) to avoid clonal drift |
| **Titer** | Use HEK293T-produced lentivirus; titer by p24 ELISA or qPCR (Lenti-X, Clontech) |
| **BL-2 safety** | Required for lentiviral work; institutional biosafety committee approval 2–3 months in advance |
| **Lead time** | 2–4 weeks (cloning + virus production + titration) |
| **Cost** | $300–500 per shRNA lentivirus (Sigma or VectorBuilder) |

**Critical:** **shRNA KD efficiency is much more variable than siRNA** — typically 50–90% KD vs. siRNA's 75–95%. Plan for 2–3 rounds of shRNA screening to find the best construct per gene.

### 2.4 — CRISPR design (in-house IDT Alt-R HiFi Cas9 RNP)

For Aim 3 isogenic KO (if doing in-house, not via CRO):

| Step | Vendor / reagent | Cost | Time |
|---|---|---|---|
| **sgRNA design** | IDT Alt-R Custom Alt-R crRNA + tracrRNA; or Synthego sgRNA | $100–200 (2–3 sgRNAs per gene) | 1 week |
| **Cas9 protein** | IDT Alt-R S.p. HiFi Cas9 Nuclease V3 (1 mg, ~$400) or Synthego SpCas9 | $400–500 (enough for ~100 RNP transfections) | in-stock |
| **Electroporation** | Lonza Nucleofector (C2C12: program B-005; HSMM: program CM-138) or Thermo Neon | per-transfection cost <$5 | 1 day |
| **Single-cell cloning** | Limiting dilution or FACS (Sony SH800) | $500 (FACS) | 2–3 weeks |
| **KO screening** | T7E1 mismatch assay or ICE (Synthego) analysis | $200 per gene | 1 week |
| **Off-target analysis** | GUIDE-seq (~$1,500) or in silico (free) | $0–1,500 | 1–4 weeks |
| **Total time per gene** | | | **6–10 weeks per clone** |

**Total cost for 2 KO lines (CHCHD10, ATP5F1B), 3 clones each, full QC:** $10,000–$15,000 (in-house, with 3 sgRNAs per gene, cloning, screening, off-target, myogenic validation). **This is the budget-conscious alternative to the $30K CRO route.**

### 2.5 — siRNA transfection reagent + delivery (not the construct itself)

Often forgotten — the **transfection reagent** is a major variable. For C2C12 + HSMM myotubes:

| Reagent | Vendor | Best for | Cost per 96-well plate |
|---|---|---|---|
| **Lipofectamine RNAiMAX** | Thermo Fisher | Standard siRNA; C2C12, HSMM | $50–80 |
| **DharmaFECT 1** | Horizon Discovery | siRNA + siRNA pool; validated with ON-TARGETplus | $80–100 |
| **Lipofectamine 3000** | Thermo Fisher | Plasmid + siRNA co-transfection (rescue experiment) | $50–80 |
| **Lonza Nucleofector (electroporation)** | Lonza | Hard-to-transfect cells; primary HSMM | $5/transfection |
| **Neon (electroporation)** | Thermo Fisher | Alternative electroporation | $5/transfection |
| **TransIT-TKO** | Mirus Bio | siRNA + miRNA mimic; HSMM-validated | $80–100 |

**Best for muscle cells:** **Lipofectamine RNAiMAX** is the workhorse; **DharmaFECT 1** is the next-best for siRNA. For C2C12, reverse-transfection at the time of plating is most reproducible (vs. forward-transfection at 24h). For HSMM (primary), **electroporation (Nucleofector or Neon)** is often required — lipid reagents are inefficient.

---

## 3. AAV production (Exp B — AAV9-shRNA in vivo)


| Vendor / Core | Serotype options | Scale (typical) | Price (USD) | Lead time | QC included | Notes |
|---|---|---|---|---|---|---|
| **VectorBuilder** | **AAV1, AAV2, AAV5, AAV6, AAV8, AAV9, AAVrh10, AAV-PHP.eB, AAV-DJ, AAV-retro, >75 engineered variants** | **Ultra-purified research grade:** pilot 100 µL @ ≥10¹³ GC/mL, medium 500 µL, large 1 mL; **Research-Plus:** 1×10¹³ GC ($4,699) — 5×10¹³ ($14,899) — 1×10¹⁴ ($23,899) | **Pilot (≥10¹²): $449; Medium: $649; Large: $1,099; Ultra-purified pilot (≥10¹³): $1,399; Ultra-purified medium: $1,999; Ultra-purified large: $3,099; Research-Plus 1 (1×10¹³): $4,699; Research-Plus 5 (5×10¹³): $14,899** | **10–14 days** (research grade); **14–21 days** (ultra-purified research); **35–49 days** (GMP-like) | Titer (qPCR or ddPCR), sterility, mycoplasma, endotoxin (<10 EU/mL for ultra-purified), purity by SDS-PAGE (>80%), full capsid ratio >70% | **Best price-performance for academic**; CsCl or iodixanol purification; MuteFree backbone reduces ITR mutations; GMP-grade CDMO available for 6–12 months clinical; **MOST POPULAR CHOICE for academic AAV** |
| **UNC Vector Core** (U North Carolina) | AAV1–6, 2.5, 8, 9, rAAV2Retro | 1–2 mL @ 1–4×10¹² vg/mL (standard); 1L-20L custom large-scale | **Standard size custom: $2,200 external academic / $1,500 UNC / $3,400 corporate**; **1L: $3,300 ext academic / $2,100 UNC / $5,000 corp**; **2L: $4,700 / $3,100 / $7,000**; **5L: $10,650 / $6,400 / $15,000** | **4–5 weeks** for standard; longer for large | Titer, sterility, purity; not full GMP | **Cheapest academic option**; triple-transfection in suspension HEK293; serum-free / antibiotic-free; **plasmid DNA amplification extra ($500 academic, $750 corporate)** |
| **Penn Vector Core** (now Franklin Biolabs for custom requests) | **AAV1, AAV2, AAV5, AAV6, AAV8, AAV9, AAVrh10, AAVrh74, custom** | Variable (pre-defined catalog lots via Addgene partnership + custom via Franklin Biolabs) | **AAV Vector Production: $2,470 internal UPenn / $2,964 external academic / $3,949 corporate**; **AAV Vector Genome Titer: $90 academic / $120 corporate**; **TCID50: $471 academic**; **Single Vial Aliquot: $149 academic**; **Endotoxin Assay: $60 academic** | **3–4 weeks routine**; **up to 8 weeks custom** (per Franklin Biolabs); Iodixanol gradient or chromatography purification | Titer by ddPCR, sterility, endotoxin, purity, identity | **Gold standard for academic muscle-targeted AAV** (James Wilson's lab lineage, AAV9 muscle tropism foundational work); **Custom production was acquired by Franklin Biolabs in 2022**; **catalog lots still distributed via Addgene** |
| **Addgene (deposited catalog, packaged-on-request)** | Per deposit; common: AAV1, AAV2, AAV5, AAV6, AAV8, AAV9, AAV-DJ, AAV-PHP.eB, AAV-retro | **100 µL @ ≥1×10¹³ vg/mL** (standard); 0.2 mL – 5 mL (custom) | **AAV9 (catalog) ~$425/virus + $34 plasmid** (e.g., Addgene 105555-AAV9 = pENN.AAV.hSyn.Cre.hGH) | **6–9 weeks after MTA approval** | Titer, sterility, endotoxin; full QC varies per lot | **Best for one-off / catalog constructs**; UBMTA, accepted by most institutions; commercial pricing higher |
| **Vigene Biosciences** | AAV1, AAV2, AAV5, AAV6, AAV8, **AAV9, AAVrh10, AAV-PHP.eB, AAV-DJ, >75 engineered** | 1 mL @ ≥1×10¹³ vg/mL (small); 5 mL (large) | **Small (≥1×10¹³): $3,500–5,000**; **large: $6,000–9,000** | **5–7 weeks** | Full QC + in-vivo tropism validation available; GMP-like available | **Premium quality**, good for high-titer muscle-tropism experiments |
| **BrainVTA / Shanghai Taitool** | AAV9, AAV-PHP.eB, AAVretro, AAV-DJ, AAV1, AAV2/5/8 | 1×10¹³ vg/mL standard | **$1,500–2,500** | **3–4 weeks** | Titer, endotoxin, sterility | **Asia-based, lowest cost**, faster turnaround; **good academic alternative** if budget-constrained |
| **Virovek** | AAV9, custom serotypes | 1×10¹³ vg/mL | $2,000–3,000 (research) | 4–6 weeks | Titer, endotoxin, purity | Another low-cost option, often used in muscle gene-therapy papers |
| **PackGene Biotech** | AAV9, custom, GMP-like available | Variable | $2,500–4,000 (research); GMP ~$40,000+ | 4–6 weeks research; 8–12 weeks GMP-like | Titer, endotoxin, identity, sterility | **Alternative to VectorBuilder** with GMP capability |

**For Exp B (AAV9-shRNA in vivo):**
- **3 constructs × 2 batches** (e.g., scramble, shRNA-CHCHD10, shRNA-ATP5F1B; 2 batches per construct for dose-ranging or for 2 cohorts)
- **Recommended scale:** Ultra-purified research grade, large (1 mL @ ≥10¹³ GC/mL) per construct = **$3,099 × 3 × 2 = $18,594** at VectorBuilder list price
- **Academic discount (10–20%):** ~$15,000–17,000
- **Alternative: UNC Vector Core standard size** ($2,200 external academic × 6 = $13,200) — **cheaper, but titer is 1–4×10¹² vg/mL** (lower than VectorBuilder ultra-purified)
- **Lead time:** 4–6 weeks is realistic (10–14 days production + 2 weeks cloning if shRNA insert not pre-made + shipping)

**Serotype guidance for Exp B:**
- **AAV9** is the standard for skeletal-muscle transduction in adult mice (foot-pad / IM / systemic delivery); works well for tibialis anterior (TA) via direct IM injection
- **AAVrh74** has higher muscle tropism and is the clinical-stage choice (Sarepta DMD); but it requires a license from the **Research Institute at Nationwide Children's Hospital** (Brian Kaspar) for commercial use
- **AAV6** is good for in-vitro transduction of C2C12/HSMM myotubes (use for the in-vitro pilot before in-vivo)
- **AAV-PHP.eB** crosses the BBB — **not appropriate for muscle-only targeting** (it transduces the brain too)

### 3.1 — AAV serotype selection for skeletal muscle (the decision)

| Serotype | Muscle tropism (mouse) | Cross-species | Titer needed for in-vivo | Best use |
|---|---|---|---|---|
| **AAV9** | High (whole body; cardiac, skeletal, smooth) | Mouse, rat, NHP, human | 1–5×10¹² vg/mouse (systemic); 1×10¹¹ vg/TA (local IM) | Standard for muscle; widely cited |
| **AAV8** | Moderate (skeletal, cardiac) | Mouse, rat, NHP | similar to AAV9 | Skeletal muscle; not as good for CNS |
| **AAV6** | High (skeletal muscle, especially after injury / regenerating) | Mouse, rat | similar to AAV9 | In-vitro C2C12/HSMM transduction; in-vivo regenerating muscle |
| **AAV1** | High (skeletal muscle, especially after injury) | Mouse, rat | 5×10¹⁰ vg/TA (local IM) | Local muscle injection |
| **AAVrh74** | High (skeletal + cardiac, clinical stage) | Mouse, rat, NHP, human | 1×10¹¹ vg/TA (local IM) | Clinical translation (Sarepta DMD); **requires license from Nationwide Children's** |
| **AAV-PHP.eB** | Very high (transduces whole body including CNS via IV) | Mouse only (does not work in NHP or human) | 1×10¹¹ vg/mouse (IV) | Mouse-specific; not for human translation |
| **MyoAAV (Broad)** | 10–100× higher than AAV9 in some papers | Mouse, NHP | 10× lower dose than AAV9 | Newer; requires MTA with Broad Institute / Harvard |

**For Exp B (AAV9-shRNA in TA of young C57BL/6J mice):** **AAV9 is the standard**, well-cited, and accepted by reviewers. **AAVrh74 is the clinical-grade alternative** but requires a license and may trigger MTA paperwork.

**For Aim 2 in-vitro pilot (C2C12 + HSMM transduction):** **AAV6** is the muscle-standard serotype for in-vitro work; transduction efficiency >80% in C2C12 at MOI 10,000–50,000 vg/cell.

### 3.2 — AAV dosing for in-vivo Exp B (specific to mouse TA injection)

| Parameter | Value | Reference |
|---|---|---|
| **Mouse strain** | C57BL/6J, 3 mo (young) or 24 mo (aged, Exp D) | Jackson or NIA |
| **Injection route** | Intramuscular (IM) into TA, single injection | Standard |
| **Injection volume** | 30–50 µL per TA (max 50 µL; AAALAC limit) | AAALAC |
| **Dose per TA** | 1×10¹¹ vg (standard) or 5×10¹⁰ vg (low) or 1×10¹² vg (high) | Tabebordbar 2016 (Nature) |
| **Titer needed** | ≥2×10¹² vg/mL for 50 µL @ 1×10¹¹ vg/TA | VectorBuilder large prep |
| **Onset of expression** | 3–7 days (peak at 14–21 days) | Standard |
| **Duration of expression** | 6–12 months in mouse muscle | Standard |
| **Contralateral control** | Scramble shRNA in the *contralateral* TA of the same mouse (within-subject control) | Best practice |
| **Sham control** | PBS injection in a separate cohort | Required for IACUC |

**For Exp B (n=10 mice, 3 constructs × 2 batches):**
- 10 mice × 1 TA per construct = 10 TA injections per construct
- 50 µL per TA × 10 = 500 µL needed per construct
- × 3 constructs = 1.5 mL total
- × 2 batches (replicate for safety) = 3 mL total
- = **3 × VectorBuilder ultra-purified large (1 mL @ ≥10¹³ GC/mL) = $3,099 × 3 = $9,297**
- = **$9,300 list, ~$7,500 with academic discount**

**For Exp D (aged mice):** **3× the dose** for 24-mo mice due to impaired vascularisation and ECM changes; **1×10¹² vg/TA** instead of 1×10¹¹. This is an additional $7,500 (3 more preps).

### 3.3 — AAV QC — what to ask for in the COA

| QC | Method | Pass criterion |
|---|---|---|
| **Titer (vector genomes/mL)** | ddPCR (preferred) or qPCR | ≥1×10¹³ GC/mL for ultra-purified large |
| **Full capsid ratio** | A260/A280 (DNA:protein); or cryo-EM (rare) | >70% (VectorBuilder ultra-purified); >80% (research-plus) |
| **Purity** | SDS-PAGE | >80% (single band at VP1/2/3) |
| **Endotoxin** | LAL (Limulus Amebocyte Lysate) | <10 EU/mL (ultra-purified); <30 EU/mL (research-grade) |
| **Sterility** | USP <71> | No growth |
| **Mycoplasma** | PCR | Negative |
| **Identity** | Sanger sequencing of ITR-flanking region (transgene cassette) | Match to expected |
| **In-vivo potency (optional, $$$)** | Mouse IM injection + IHC for transgene | Positive at 14d |

**DO NOT accept AAV without a CoA showing titer by ddPCR + full capsid ratio.** Many older academic cores report "titer by qPCR" with no capsid ratio — this can be 50–90% empty capsids, which dramatically reduces the effective dose.

### 3.4 — AAV storage and handling (lab-side)

| Step | Detail |
|---|---|
| **Storage** | -80°C, single-use aliquots (10–50 µL); **do not freeze-thaw more than 3 times** |
| **Shipping** | Dry ice, overnight; **do not accept thawed shipments** (refuse the order) |
| **Working stock** | Dilute to 2×10¹² vg/mL in PBS + 0.001% Pluronic F-68 (Poloxamer 188) immediately on arrival; aliquot; freeze |
| **In-vivo prep** | Thaw one aliquot; **do not refreeze**; use within 4h; keep on ice |
| **IACUC protocol** | Required for all in-vivo AAV work; include waste-handling protocol (AAV is BSL-2 in most institutions) |

### 3.5 — VectorBuilder vs Penn Vector Core vs UNC Vector Core — head-to-head

| Factor | VectorBuilder | Penn Vector Core / Franklin Biolabs | UNC Vector Core |
|---|---|---|---|
| **Price (1 mL ultra-purified AAV9)** | $3,099 (academic ~$2,500) | Quote (typically $4,000–6,000) | n/a (uses lower titer) |
| **Price (1–4×10¹² vg/mL standard)** | n/a (their grades differ) | n/a | $2,200 academic |
| **Titer** | ≥1×10¹³ GC/mL (ultra-purified) | ≥1×10¹³ GC/mL (Franklin) | 1–4×10¹² vg/mL |
| **Lead time** | 10–21 days | 3–8 weeks | 4–5 weeks |
| **Cloning included?** | Yes (if you send the gene, they clone into AAV backbone) | Yes (Franklin); no (Penn legacy catalog) | No (you ship the plasmid) |
| **Plasmid amplification** | Included | Included | $500 extra |
| **Custom serotype** | Yes (75+ options) | Yes (Franklin); legacy catalog for Penn | Yes (AAV1-6, 2.5, 8, 9, rAAV2Retro) |
| **Best for** | Budget academic muscle; fast turnaround | Premium quality; James Wilson lineage; GMP-grade if needed | Lowest cost; willing to accept lower titer |
| **Downside** | Newer vendor (founded 2007); some academic reviewers prefer Penn catalog lots | Higher cost; longer lead | Lower titer; you must ship plasmid (FedEx, cold chain) |

**Recommendation for Exp B:** **VectorBuilder for the initial batches** (faster, cheaper, similar quality); **Penn Vector Core / Franklin Biolabs for the confirmatory / final-batch lots** (gold-standard QC, can request GMP-like if the program moves toward clinical translation).

---

## 4. Aged-mouse colony (Exp A, B, D)


| Source | Strain | Ages available | Price per mouse (USD) | Colony management | Lead time | Notes |
|---|---|---|---|---|---|---|
| **NIA Aged Rodent Colony** (NIH) | **C57BL/6JN** | 4, 12, 18, 22, 24, 28, 30+ mo | **FREE** (animals + shipping) | NIA-supplied (housed at Charles River); **requires aging-research grant eligibility** | **4–8 weeks** from order to delivery; **mortality higher at 24+ mo**; **20 animals/month cap for NIA-funded grants, 10/2mo for non-NIA** | **The cheapest possible aged-mouse source**; **requires explicit aging-research justification on grant**; HMSR v0.4 is on sarcopenia = eligible; **DO NOT USE** for non-aging research; C57BL/6JN is the NIA sub-strain, **not** the JAX C57BL/6J (genetic drift after decades of separate colonies; the two strains are functionally similar but not identical — some phenotype differences in immune and metabolic traits) |
| **Jackson Labs (JAX)** | C57BL/6J (**JAX sub-strain**, separate from NIA's C57BL/6JN) | 1, 2, 3, 4, 6, 8, 12, 16, 20, **24, 26, 28, 30+ mo** (B6J-Aged) | **Young (3-4 mo): $30–45**; **12 mo: $60–80**; **18 mo: $80–110**; **24 mo: $130–170**; **26+ mo: $150–200** | JAX supplies animals, no in-house aging | 2–4 weeks (in-stock ages); **6–9 months for custom-aged cohorts** (must be ordered in advance; production lag) | **Standard reference**; JAX-specific phenotype data exists; the B6J-Aged Male 26W-78W is the popular in-stock aged cohort (8,310 JPY ≈ $55 in Japan, USD varies) |
| **Charles River** | C57BL/6J (CR sub-strain) | Young (3-8 wk), 6, 12 mo standard; **24+ mo limited, often not in stock** | **Young: $25–35**; **12 mo: $80–110**; **24 mo: $150+ when in stock** | None (CR supplies) | 1–2 weeks young; **8+ weeks for 24-mo (call to confirm)** | Limited aged stock; **cheaper than JAX for young**; suitable for the young-control arm but not primary aged source |
| **Envigo / Inotiv** | C57BL/6J | Young + selected aged | **Young: $30–40**; **12 mo: $70–100**; **24 mo: $120–170** | Some aging available | 2–4 weeks | Larger volumes; absorbed by Inotiv |
| **Taconic** | C57BL/6J | Young + selected aged | Similar to Charles River | Limited | 1–3 weeks | Good for young controls; not the primary aged source |
| **In-house aging colony** | C57BL/6J (JAX, NIA, or CR source as 2-3-mo weanlings) | Build to any age: 3, 12, 18, 24, 30 mo | **Cage cost $1–3 / mouse / day** (~$365–1,095 / mouse / year); **includes husbandry staff time** | **You age them in-house**; **IVC cages, sentinel monitoring, IACUC protocols required** | **6–24 months in advance** (must start the colony now) | **Lowest unit cost long-term; longest lead**; **the only way to get 30-mo or 36-mo mice for Exp D**; barrier facility required; IACUC + DLAR approval 2–3 months |
| **Cyagen** (China) | C57BL/6J | Custom ages | $80–150 (24-mo) | Outsourced aging | 8–16 weeks | **Asia-based, low cost**; suitable when budget-constrained |
| **Gerosense** (startup, mouse aging) | C57BL/6J | Aged | Quote | Outsourced | 8–16 weeks | Newer CRO; specializes in aged mouse work |

**Survival / sample-size planning** (per NIA survival tables):
- C57BL/6J males at 24 mo: 50% survival
- C57BL/6J males at 28 mo: 25% survival
- **Order 20–30% MORE than your experimental n** to account for attrition and cage losses
- For n=10/group, order n=13–15 mice per age per sex

**Recommendation for Exp A (M4–6) and Exp D (M8–14):**
- **Exp A (observational, n=8/group young + 24-mo):** Order from **NIA** (free, 4–8 weeks lead time); backup from JAX if NIA quota exhausted. **Place NIA order at M0** to ensure M4 delivery.
- **Exp B (causal, n=10 young C57BL/6J):** Order from **JAX (3-mo C57BL/6J, stock #000664)**, 2-week lead time. Standard.
- **Exp C (exercise, n=12 young):** Order from **JAX or Charles River (3-mo C57BL/6J)**. Standard.
- **Exp D (therapeutic, n=15 aged + n=15 young):** Combine NIA (free, 24-mo) for the aged + JAX for the young. **In parallel, START the in-house aging colony** to enable 30-mo cohorts for Exp D's later timepoints.
- **For any future experiments needing 28+ mo mice:** **In-house aging is the only option.** Start the colony now.

### 4.1 — In-house aging colony: how to set it up (if pursued)

| Component | Spec / vendor | Cost (USD) |
|---|---|---|
| **Weanlings (2-3 mo C57BL/6J)** | JAX stock #000664 | $30 each |
| **IVC cages** | Allentown or Tecniplast | $2,000–3,000 per cage rack |
| **Cage density** | 3–5 mice per cage | — |
| **Husbandry** | DLAR (institutional) | $1.50–3.00 per cage per day (includes cage, bedding, food, water, technician time) |
| **Sentinel mice** | 1 sentinel per 50–70 mice, quarterly | $50 per sentinel + testing |
| **Health monitoring** | Quarterly serology (Charles River) | $200 per quarter |
| **IACUC protocol** | Required; include aging + terminal endpoint | $0 (institutional) |
| **Cage changing** | Weekly; in HEPA-filtered cage-changing station | included in DLAR |
| **Enrichment** | Nestlets, chew sticks | $1/cage/week |
| **Total annual cost** | 60 mice × 365 days × $1.50/day + setup | $33,000 + $10,000 setup = **$43,000/year** |

**Key decisions:**
- **Sex:** HMSR used both sexes; order equal numbers; analyse sex as a covariate
- **Cage-mate effects:** randomise at weaning; do not co-house males from different litters (aggression at 6+ mo)
- **Diet:** standard chow (PicoLab 5053 or equivalent) is fine; **do not use high-fat diet unless required** (changes metabolic phenotype)
- **Time to 24-mo:** **24 months from birth**; if ordering 2-mo weanlings at M0, the 24-mo timepoint is M22
- **Time to 30-mo:** **30 months from birth**; this is the **absolute maximum** for in-house aging (mortality >50% past 30 mo)
- **Attrition:** expect 30–40% mortality between 24 and 30 mo; **order 30–40% more mice than your n**
- **IACUC approval:** 2–3 months; **file at M0** to enable M3 onboarding

### 4.2 — Survival table for C57BL/6J (per NIA data)

| Age (mo) | Male survival (%) | Female survival (%) |
|---|---|---|
| 12 | 95 | 96 |
| 18 | 85 | 88 |
| 24 | 60–70 | 70 |
| 28 | 35 | 50 |
| 30 | 25 | 40 |
| 32 | 10 | 20 |
| 36 | <5 | 5 |

**C57BL/6JN (NIA sub-strain) vs C57BL/6J (JAX sub-strain) survival:** **NIA C57BL/6JN is slightly longer-lived** (better husbandry, NIH-funded SPF barrier); the two sub-strains differ by ~10% in median lifespan. **For Exp A + D, prefer NIA C57BL/6JN for consistency with the aging-research literature; JAX C57BL/6J for general muscle-biology comparability.**

### 4.3 — Aged-mouse health monitoring (must be done before Exp A/B/D)

| Test | Vendor | Frequency | Cost |
|---|---|---|---|
| **Serology panel (Sendai, MHV, Mycoplasma pulmonis, etc.)** | Charles River or IDEXX | Quarterly | $200/quarter |
| **Pathology on found-dead** | DLAR or Charles River | Per case | $100/case |
| **Body weight** | In-house | Weekly | free |
| **Grip strength** | In-house (Bioseb grip strength meter, $3,000) | Monthly | free |
| **Body composition (DEXA / EchoMRI)** | EchoMRI-100H ($40K) or in-house | Monthly | $2/sample |
| **Rotarod** | In-house (AccuRotor, $5K) | Monthly | free |

**Most academic DLARs do quarterly serology as part of the per-cage-day charge.** Confirm before budgeting.

### 4.4 — Aged-mouse import / shipping logistics

| Parameter | Standard |
|---|---|
| **Shipping container** | Filter-top IVC cage (Charles River, JAX) or filtered shipping crate |
| **Transport time** | ≤48h (JAX uses dedicated climate-controlled truck routes in US) |
| **Acceptable transport temperature** | 18–26°C (room temp); ≤70% humidity |
| **Quarantine** | 7–14 days in your animal facility (per DLAR protocol) |
| **Import permit** | Required for international (USDA/CDC for foreign sources); not required for US-domestic (JAX, Charles River, NIA) |
| **NIA shipping** | Free; uses Charles River truck routes; **no weekend or holiday deliveries** |
| **JAX shipping** | $30–80 per crate; truck routes in 9 US regions; air freight for international |
| **Charles River shipping** | $50–100; truck routes; international air freight available |
| **Acceptance criteria** | On arrival, check: (1) DOB matches order; (2) health status report; (3) no visible health issues; (4) weight within normal range; **reject if DOB is more than 1 month off, or if any health flag is raised** |

### 4.5 — Aged-mouse C57BL/6J strain background — the sub-strain debate

There are at least **5 sub-strains of C57BL/6** in active use as of 2026:

| Sub-strain | Source | Note |
|---|---|---|
| **C57BL/6J** | JAX | The "original" JAX line; **carries the *Nnt* deletion** (impaired glucose tolerance); widely used; 1,000+ papers |
| **C57BL/6JN** | NIA (via Charles River) | JAX-derived; **NIA sub-strain**; better health status; less genetic drift; used in NIA-funded aging research |
| **C57BL/6N** | Charles River | Taconic / Charles River sub-strain; **Nnt wild-type** (normal glucose); used in KOMP / IMPC knockout phenotyping |
| **C57BL/6JCrl** | Charles River | Charles River's own sub-strain |
| **C57BL/6NTac** | Taconic | Taconic's own sub-strain |

**Phenotypic differences (relevant to muscle research):**
- **Glucose tolerance:** C57BL/6J (*Nnt*-deleted) has impaired glucose tolerance; C57BL/6N is normal. **This matters for metabolic / mitochondrial studies** (C2C12 from C57BL/6 background; HSMM is human).
- **Bone density:** C57BL/6J has lower bone density than C57BL/6N.
- **Behaviour:** C57BL/6J has more anxiety-like behaviour in open-field tests.
- **Muscle phenotype:** **C57BL/6J and C57BL/6N have similar baseline muscle mass and strength** in young adults; at 24+ mo, the differences are larger (JAX has more sarcopenia; NIA slightly less).

**For HMSR Exp A + D:** **C57BL/6JN (NIA) is the consistent choice for the aged arm** (matches the NIA-funded aging literature); **C57BL/6J (JAX) for the young arm** (matches most muscle-biology literature). **Be explicit about the sub-strain in every paper.**

---

## 5. Seahorse / mitochondrial assay (Aim 1, Aim 2)


| Vendor / Core | Instrument | Service | Price (USD) | Lead time | Notes |
|---|---|---|---|---|---|
| **Agilent (Seahorse)** | **XFe96** (96-well; current industry standard), **XFe24** (24-well; older), **XF Pro** (newest, 2023+; replaces XFe), **XF Flex** (newest, 2025+) | Instrument + consumables + assay kits | **XFe96 (refurbished): ~$20,000**; **XFe96 (new): ~$50,000–60,000**; **XFe24: ~$70,000–80,000**; **XF Pro: ~$120,000+**; **XF Flex: quote**; **Mito Stress Test Kit (103015-100): $1,087**; **FluxPak (6 plates sensor + culture + calibrant): $2,021** | **4–8 weeks** for new instrument; **1–2 weeks** for FluxPak | **Industry standard** for mitochondrial-respiration OCR / ECAR measurement; **Mito Stress Test Kit** = 6 single-use reagent pouches (Oligomycin, FCCP, Rot/AA); recommended dose: oligomycin 1.5 µM, FCCP 0.5–2.0 µM titration, Rot/AA 0.5 µM; Agilent Cell Analysis Field Application Scientists available for free training |
| **Seahorse Assay Service (Agilent)** | — | Full service (ship cells, get OCR report) | **$300–500/plate** | 2–4 weeks | Send cells (or fixed Seahorse plates) to Agilent, get normalized OCR report; **useful if your lab has no Seahorse** |
| **University Seahorse Cores** | XFe96 / XFe24 (varies) | Core facility (booking + technician) | **$50–200/plate** + technician fee | 1–2 weeks (booking) | **Most university medical schools have a Seahorse core**; typical pricing: ~$100/plate + $50–100 technician fee; check your institution |
| **Oroboros Instruments** (alternative to Seahorse) | **Oroboros Oxygraph-2k (O2k)** | High-resolution respirometry for permeabilized fibres / isolated mitochondria | **O2k instrument: ~$50,000–65,000**; **O2k-Fluo (with fluorescence): ~$80,000**; **service / consumables per experiment: $200–500** | 6–10 weeks | **Gold standard for permeabilized-fibre respirometry** (Exp A); preferred over Seahorse for **substrate-specific (CI, CII, etc.) respirometry**; works on freshly isolated fibres and on permeabilized myotubes; **required for Exp A's permeabilized-fibre protocol** (Aim 1 functional read-out) |
| **Strathkelvin Instruments** (alternative) | **Mitocell** (Clark-electrode based) | Respirometry for isolated mitochondria | $8,000–15,000 | 4–8 weeks | Older technology; budget option |
| **MitoSciences / Abcam** | — | Kits, OCR reagents, Total OXPHOS cocktail | **$200–500/kit** | 1 week (in-stock) | Secondary source for antibodies + assay kits (e.g., MitoSciences MitoTox, ATP rate) |

### 5.1 — Seahorse assay: detailed cost breakdown per plate (XFe96)

| Item | Cost (USD) per 96-well plate | Notes |
|---|---|---|
| **XFe96 Cell Culture Microplate (102416-100)** | $240 (Agilent) | 1 plate per experiment |
| **XFe96 Sensor Cartridge (102416-100)** | $260 (Agilent) | 1 cartridge per experiment (can be reused if not damaged) |
| **XF Calibrant Solution (100840-000)** | $50 (500 mL bottle; enough for 10+ plates) | $5/plate amortized |
| **XF Base Medium (102353-100)** | $30 (Agilent) | 50 mL/plate |
| **Mito Stress Test Kit (103015-100, 6 plates)** | $181/plate amortized | 6 plates per kit, $1,087 |
| **Glucose, pyruvate, glutamine supplements** | $5/plate | Sigma |
| **Oligomycin titration (separate)** | $50/plate | Sigma O4876, 5 mg |
| **FCCP titration (separate)** | $100/plate | Sigma C2920, 10 mg |
| **Rotenone + antimycin A (separate)** | $50/plate | Sigma R8875 + A8674 |
| **Total consumables per plate** | **~$720** | Agilent list price |
| **+ technician time (if core facility)** | $50–200 | $770–920 per plate |

**For the lean Aim 2 PoC (6 plates):** $720 × 6 = **$4,320 consumables + $300 FCCP titration buffer = $4,620** — close to the §9 budget of $4,000.

**For the full Aim 2 program (50 plates):** $720 × 50 = **$36,000 consumables** — much higher than the §9 budget; this is the realistic number for a full screen.

### 5.2 — Seahorse XF Pro vs XFe96 vs XFe24 (which to buy)

| Feature | XF Pro (2023+) | XFe96 | XFe24 |
|---|---|---|---|
| **Well format** | 96-well | 96-well | 24-well |
| **Cells per well** | 5,000–50,000 | 5,000–50,000 | 50,000–200,000 |
| **OCR sensitivity (pmol/min)** | 0.5 | 0.5 | 1.5 |
| **Wave software** | Wave Pro (2023+) | Wave | Wave |
| **Oxygen + pH sensors** | Optical (fluorescent) | Optical | Optical |
| **Walkaway automation** | Yes (24/7) | No | No |
| **Price (new)** | $120,000+ | $50,000–60,000 | $70,000–80,000 |
| **Best for** | High-throughput, multi-user core | Standard in-vitro muscle | Larger samples (permeabilized fibres) |
| **Agilent support** | Best (newest) | Good | Good |

**Recommendation for new lab:** **XFe96** (best price-performance). **For a core facility serving many labs:** **XF Pro** (walkaway automation + 24/7 capacity).

### 5.3 — Oroboros O2k (for Exp A in-vivo permeabilized-fibre respirometry)

The O2k is the **gold standard for high-resolution respirometry on permeabilized muscle fibres** and isolated mitochondria. The v0.2 plan calls for Oroboros in Exp A; this is a non-negotiable for the publication-quality Exp A.

| Configuration | Price (USD) | Use case |
|---|---|---|
| **Oroboros Oxygraph-2k (O2k)** | $50,000–65,000 | Standard high-resolution respirometry |
| **O2k-Fluo (with fluorescence module)** | $80,000 | Add H₂O₂ (Amplex Red) or membrane potential (safranin / TMRM) |
| **O2k-Fluorometry + TMRM + O2** | $90,000 | Full ΔΨm + ROS + O₂ in one experiment |
| **Add-on: MiR05-Kit (mitochondrial respiration medium)** | $200 | MiR05 = Mir05 + creatine + blebbistatin (permeabilized-fibre) |
| **Add-on: saponin (permeabilization)** | $50 | 50 mg, enough for 100+ fibre preps |
| **Service contract (annual)** | $5,000–8,000 | Recommended for instruments >5 yr old |
| **DatLab software license** | included | — |

**For Exp A (permeabilized-fibre respirometry on 16 mice, 4 muscles/mouse):**
- **Buy O2k:** $50,000 capex, lasts 10+ years; amortized over the program = $5,000/yr
- **Use a core O2k (Mayo, Maryland, Virginia):** $300–500/day × 10 days = $3,000–5,000
- **The core-fee option is far cheaper for a one-off program**; the buy option is cheaper for a long-term program

### 5.4 — Alternative respiratory assays (if Seahorse/Oroboros are unavailable)

| Method | Vendor / reagent | Sensitivity | Cost per sample |
|---|---|---|---|
| **MitoTracker dyes (Green / Red / Deep Red)** | Thermo Fisher | Semi-quantitative (single-cell IF) | $200/kit |
| **TMRE / TMRM (ΔΨm)** | Thermo Fisher | Semi-quantitative (fluorescence) | $200/kit |
| **MitoSOX (mitochondrial ROS)** | Thermo Fisher | Semi-quantitative (flow / plate reader) | $200/kit |
| **JC-1 (ΔΨm, ratio metric)** | Thermo Fisher | Semi-quantitative (flow / plate reader) | $200/kit |
| **ATP rate assay (Bio/ Luminescence)** | Promega CellTiter-Glo + Mitochondrial ToxGlo | Quantitative ATP | $300/kit |
| **Citrate synthase activity (colorimetric)** | Sigma CS0720 | Mito mass (enzymatic) | $100/kit |
| **mtDNA copy number (qPCR)** | in-house qPCR | Mito mass (DNA) | $50/plate |
| **BN-PAGE (Blue-Native PAGE for supercomplexes)** | Thermo + in-house | Complex I/III₂/IV supercomplex assembly | $200/gel |

**For publication-quality Exp A:** **Seahorse + Oroboros is the minimum.** MitoTracker / TMRE / MitoSOX are **supporting** but not the primary endpoint.

### 5.5 — Mitochondrial isolation kits (for Aim 1 protein validation)

| Vendor | Kit | Price (USD) | Notes |
|---|---|---|---|
| **Abcam** (MitoSciences) | ab110168 (Mitochondria Isolation Kit, mouse tissue) | $400 | Standard differential centrifugation; yields intact mitochondria |
| **Sigma-Aldrich** | MITOISO1 (Mitochondria Isolation Kit) | $350 | Alternative to Abcam |
| **Thermo Fisher** | 89801 (Mitochondria Isolation Kit for Cultured Cells) | $350 | For C2C12 / HSMM myotubes |
| **QIAGEN** | Qproteome Mitochondria Isolation Kit | $400 | For downstream proteomics |

**For Exp A (mouse TA + gastrocnemius + soleus):** Use **Abcam ab110168** for fresh-tissue mitochondrial isolation; expect 100–300 µg mitochondrial protein per mouse.

---

## 6. Single-fibre / myobundle force rigs (Exp A, B, Exp C)

**Consumables for ~50 plates (Aim 2 PoC):**
- 9 × Mito Stress Test Kit ($1,087 each) = **$9,783**
- 9 × FluxPak (cartridges + culture plates + calibrant) = **$18,192**
- Subtotal: **~$28,000 in consumables for 50 plates**
- The leaner plan in §9 budgets $4,000 for 6 plates; if a full Aim 2 program is run, this is the realistic number.


| Vendor / Core | Instrument | Service | Price (USD) | Lead time | Notes |
|---|---|---|---|---|---|
| **Aurora Scientific** (Ontario, Canada; the industry standard) | **1300A (3-in-1 whole animal system for mice)**, **1305A (rat)**, **1310A (larger)**, **1300B (integrated; 2023+)** — **300E/300E-LR Dual-Mode Lever (0.5–1 N), 305E/305E-LR (5–10 N), 310E/310E-LR (50–100 N)**, 605A Data Acquisition, 701C High-Power Stimulator, 809C in-vivo mouse apparatus, 809C-25 25 mL horizontal in-vitro bath, 1205A in-vitro fibre test, 150A Integrated Test Controller (new, single unit) | Instrument purchase (not a service per se) | **Quote only (no list price online); expect $10,000–25,000 for lever + controller + DAQ; full 1300A system $40,000–60,000+**; **300E lever alone: $5,000–8,000**; **605A DAQ: $5,000–7,000**; **809C mouse apparatus: $8,000–12,000**; **809C-25 bath: $3,000–5,000** | **4–8 weeks** for new order; **2–4 weeks** for replacement parts | **The industry standard for muscle physiology**; used in 1,000+ papers; excellent software (DMC = Dynamic Muscle Control + DMA = Dynamic Muscle Analysis); can do twitch, tetanus, fatigue, force-frequency, length-tension, work loops, eccentric injury; **the canonical rig for Exp A (in-vivo + in-vitro + permeabilized fibre)** |
| **IonOptix** (MA, USA) | **MyoCam-S** (myotube contractility camera), **MyoPacer** (field stimulator), **CytoCatcher** (myotube shortening), **MyoStretcher** | Instrument purchase | **$8,000–15,000 for MyoCam-S + MyoPacer**; full systems up to $25,000 | 2–4 weeks | **Best for 2D myotube contractility** (Aim 2 C2C12/HSMM); not for in-vivo single fibre; the MyoCam-S records sarcomere length / shortening in real time |
| **Kent Scientific** (CT, USA) | **FORCE 10 transducer** (10 N range), **hook + pin systems** | Component | **$1,500 (FORCE 10 transducer alone)**; full custom rig $5,000–10,000 | 1 week | **Budget myobundle option** for Aim 2; works but lacks the integrated software + DAQ of Aurora |
| **World Precision Instruments (WPI)** | **SI-MOT** (myotube contractility), **FORT-100** (force transducer) | Component | $1,000–5,000 | 1–2 weeks | Budget alternative to Aurora / IonOptix |
| **University muscle-physiology cores** | (variable — typically Aurora 1300A or 300E series) | **CRO service** | **$200–500 per fibre** for force measurement; **$500–1,500 per mouse** for in-vivo Exp A protocol | 2–6 weeks | **Universities with major muscle-physiology cores:** University of Maryland (Bhatt lab, Blaauw lab), Virginia (Bhatt, Zanou), Mayo Clinic (Bhatt, Bhatt), University of Pennsylvania (Bhatt lab), Univ. Colorado, Caltech; often the cheapest option for a one-off Exp A run |
| **Aurora Scientific CRO service** (via partner labs) | Full Aurora 1300A workflow | CRO | Quote; **$500–1,500 per mouse for in-vivo Exp A protocol**; **$300–800 per in-vitro fibre prep** | 4–8 weeks | Aurora Scientific does not directly run CRO services, but they partner with a network of muscle-physiology labs; a typical arrangement: lab technician at the partnering institution runs the experiment for you and ships the data |
| **ProCytech** (France) | Myobundle / 3D muscle force | **CRO service (full pipeline)** | **$8,000–15,000 per condition** | **6–12 weeks** | **Muscle-specific CRO in France**; world experts in 3D myobundle and primary HSMM contractility; **the gold-standard muscle CRO for in-vitro functional readouts**; they have published with the field's leaders (e.g., Bhatt, Bhatt) |
| **MyoLine** (Institut de Myologie, Paris) | Immortalised human myoblast + myotube + contractility | **CRO service + cell-line supply** | Quote (typical €8,000–20,000 per project) | 8–16 weeks | **200+ immortalised human myoblast lines from 36+ diseases**; MTA-based cell distribution; world experts in immortalised myoblast generation (MyoD / hTERT) |
| **CYTOO** (France) | **MyoScreen™** — micropatterned myotube + phenotypic screen | **CRO service** | Quote; **€5,000–15,000 per screen** | 4–8 weeks | **AI-powered image analysis**; 384-well high-content; **good for high-throughput compound screening in muscle** |
| **CD BioSciences** (US-based with Asia ops) | Custom muscle-aging models + assays | CRO | Quote; **$3,000–10,000 per project** | 4–8 weeks | Newer; offers in-vitro + in-vivo muscle aging services |
| **Eurofins / Eurofins Discovery** | Standard muscle-physiology assays (organ bath, myograph) | CRO | $500–2,000 per assay | 4–8 weeks | Generalist; not a specialist muscle lab |

### 6.1 — Force rig decision: buy vs. core (for each experiment)

| Experiment | # of force measurements | Recommended approach | Cost (USD) | Justification |
|---|---|---|---|---|
| **Aim 2 (in-vitro 2D myotube, n=80 conditions)** | ~300–500 myotubes | **Buy IonOptix MyoCam-S** (~$10K) or **use a core** (~$50/plate) | $10K (buy) or $5K (core) | High throughput; the rig is amortized over many experiments |
| **Aim 2 (in-vitro 3D myobundle, n=8 conditions)** | 8 conditions × 4 myobundles = 32 myobundles | **ProCytech CRO** (no in-house rig can match) | $30K–$60K | ProCytech is the gold standard; in-house 3D myobundle is possible but slower |
| **Exp A (in-vivo single-fibre + permeabilized-fibre, n=16 mice)** | 16 mice × 5–7 muscles × 10 fibres/muscle = 800–1,120 fibres | **University core** (~$500–1,500/mouse) | $8K–$24K | A core is cheaper for a one-off Exp A; the rig would be 80% idle |
| **Exp B (in-vivo single-fibre, n=20 mice × 4 muscles × 10 fibres)** | 800 fibres | **Aurora 1300A purchase** if Exp D + future programs are planned, else **core** | $50K (buy) or $10K–$30K (core) | If the rig will be used for >50 mice total → buy |
| **Exp D (in-vivo single-fibre, n=45 mice × 4 muscles × 10 fibres)** | 1,800 fibres | **Aurora 1300A** (must own; the core cannot do 1,800 fibres) | $50K–$60K (buy) | The volume of Exp D justifies the capex |

**Total force-rig budget: $50K (buy) + $20K (core fees) = $70K** — the realistic number for the program.

**Or: $0 (buy) + $50K (core fees) = $50K** — the budget-constrained option.

### 6.2 — Aurora Scientific 1300A system: detailed component list

| Component | Purpose | Price (USD, est.) |
|---|---|---|
| **300E Dual-Mode Muscle Lever** (mouse; 0.5 N max) | The force / length transducer | $5,000–8,000 |
| **605A Data Acquisition + Software (DMC + DMA)** | DAQ + analysis software | $5,000–7,000 |
| **701C High-Power Bi-Phasic Stimulator** | Muscle stimulation (nerve + direct) | $3,000–5,000 |
| **809C Mouse In-vivo Apparatus** | Mouse platform with temperature control | $8,000–12,000 |
| **809C-25 Horizontal 25 mL Bath** | In-vitro intact muscle mechanics | $3,000–5,000 |
| **827A Water Heater / Circulator** | Bath temperature control | $1,500 |
| **150A Integrated Test Controller** (new, optional) | Combines lever + stimulator + DAQ; smaller footprint | $10,000 |
| **DMC + DMA software licenses** | Windows; full analysis suite | included |
| **Cables + electrodes + fixtures** | All required accessories | $1,000–2,000 |
| **Installation + training** | 1 day on-site | $3,000–5,000 |
| **Total Aurora 1300A system** | | **$40,000–65,000** |

**Alternative configurations:**
- **1300B (2023+):** smaller footprint (Integrated Test Controller) — same functionality, $50K
- **1305A (rat) + 805B apparatus:** rat version, $50K
- **1310A (larger):** for larger animals (rabbit, dog), $70K
- **1200A (in-vitro only, simpler):** $25K

**Recommendation:** **1300A with 300E lever + 605A DAQ + 701C stimulator + 809C + 809C-25 + 827A + software** (~$50K). This is the standard configuration for muscle physiology.

### 6.3 — IonOptix MyoCam-S + MyoPacer (for Aim 2 in-vitro 2D myotube)

| Component | Price (USD, est.) | Purpose |
|---|---|---|
| **MyoCam-S** (CCD camera + acquisition) | $8,000–10,000 | High-speed imaging of myotube shortening / sarcomere length |
| **MyoPacer** (field stimulator) | $3,000–5,000 | Electrical field stimulation (0.1–10 Hz, 1–100 V) |
| **IonWizard software** | included | Real-time analysis of sarcomere length, shortening velocity |
| **CytoCatcher** (optional) | $3,000 | Micropatterned substrate for aligned myotubes |
| **MyoStretcher** (optional) | $5,000 | Mechanical stretch (EPS-mimicking) |
| **C-arm + inverted microscope** | $0 (use existing) | Most muscle labs have one |
| **Total IonOptix system** | **$10,000–15,000** | |

**Best for:** 2D C2C12 + HSMM myotube contractility; not for in-vivo single-fibre; the gold standard for in-vitro muscle physiology.

### 6.4 — Force-measurement protocol: per-experiment estimate

| Experiment | # of mice / conditions | # of muscle preps | Time per prep (h) | Total time (h) | Cost (USD) at $100/h |
|---|---|---|---|---|---|
| **Aim 2 in-vitro 2D myotube** | 8 conditions × 4 biological reps | 32 myotube preps | 2 h | 64 h | $6,400 |
| **Aim 2 in-vitro 3D myobundle** (if in-house) | 8 conditions × 4 myobundles | 32 myobundles | 4 h (incl. prep + measure) | 128 h | $12,800 |
| **Exp A in-vivo (16 mice × 5 muscles)** | 16 mice | 80 muscle preps | 1.5 h | 120 h | $12,000 |
| **Exp B in-vivo (20 mice × 4 muscles)** | 20 mice | 80 muscle preps | 1.5 h | 120 h | $12,000 |
| **Exp C in-vivo (36 mice × 4 muscles)** | 36 mice | 144 muscle preps | 1.5 h | 216 h | $21,600 |
| **Exp D in-vivo (45 mice × 4 muscles)** | 45 mice | 180 muscle preps | 1.5 h | 270 h | $27,000 |

**Total force-measurement technician time: ~900 h = ~$90,000** (at $100/h) or ~$50,000 at $50/h (postdoc rate). This is a major line item.

### 6.5 — Grip strength meter + rotarod (in-vivo functional baseline)

| Instrument | Vendor | Price (USD) | Use case |
|---|---|---|---|
| **Grip strength meter (forelimb)** | Bioseb (BIO-GS3) | $3,000 | Standard forelimb grip; non-invasive; weekly measurements |
| **Grip strength meter (4-limb / hindlimb)** | Columbus Instruments | $4,000 | 4-paw grip; includes grid mesh |
| **Rotarod (4-lane)** | AccuRotor (Accuscan) | $5,000 | Motor coordination; 4 rpm to 40 rpm; 5-min trials |
| **Rotarod (8-lane, high-throughput)** | Ugo Basile 47600 | $8,000 | 8 lanes; better for large Exp C (n=36) |
| **Inverted-cling / grip (DMD-style)** | In-house | $200 | Hanging test; simple apparatus |
| **Gait analysis (CatWalk)** | Noldus | $40,000 | Stride length, paw pressure; out of scope for v0.3 |
| **Open-field / activity cage** | Columbus Instruments | $5,000 | Voluntary activity; Exp C positive control |
| **Body composition (EchoMRI-100H)** | EchoMRI | $40,000 | Lean mass, fat mass, free water; weekly measurements |
| **Body composition (DEXA, in-house)** | Lunar PIXImus or similar | $30,000 | Bone density + lean / fat; alternative to EchoMRI |
| **Metabolic cages (Promethion)** | Sable Systems | $35,000 (8-cage) | Food, water, O₂, CO₂, activity; Exp C positive control |
| **Metabolic cages (cheaper)** | Columbus Instruments | $20,000 | Less comprehensive; suitable for Exp C if budget-tight |

**Recommendation:**
- **For Exp A, B, C, D:** Bioseb grip strength meter ($3,000) + AccuRotor rotarod ($5,000) = $8,000 essential kit
- **For Exp C (exercise reversal):** Sable Promethion metabolic cages ($35,000) is the gold standard for VO₂ / VCO₂; if budget-tight, **Columbus Instruments open-field cage** ($5,000) is a cheaper surrogate
- **Body composition:** **EchoMRI-100H** ($40,000) if the program will run multiple studies; else use the in-house DEXA or a fee-for-service core

---

## 7. iPSC CRO services (Aim 3)


| CRO | Service | Price (USD) | Lead time | Notes |
|---|---|---|---|---|
| **FUJIFILM Cellular Dynamics (FCDI)** | iPSC myocyte supply + CRISPR editing | **$8,000–15,000 per edited line** | 12–20 weeks | **iCell Skeletal Myocytes** (formerly SKM-100-010) are the gold standard; **isogenic CHCHD10 KO / ATP5F1B KO** are quote-only; FCDI has a CDMO for clinical-grade lines (separate pricing, 6+ months) |
| **bit.bio** | iPSC myocyte + custom disease model + custom reporter | **$1,198 per 2-vial pack (ioSkeletal Myocytes WT); $999 academic 3-pack**; **custom edited lines: quote (~$10,000–20,000)** | **1–2 weeks for WT**; **8–12 weeks for custom** | **opti-ox deterministic reprogramming** — fast, reproducible, lot-to-lot consistent; **recommended as primary iPSC source for Aim 2/3**; mature striated myocytes by Day 10 post-thaw; 3D microtissues in 3–5 days |
| **Crown Bioscience (JSR Life Sciences)** | iPSC myocyte + aging-mimicking panel + full CRO service | **$20,000–50,000 per project** | 16–24 weeks | **Full-service CRO**; primarily oncology / immuno-oncology but expanding into iPSC + aging; good for "give us your gene list, get a manuscript-grade dataset" requests |
| **Cellectics** (France / EU) | Custom iPSC editing + characterization (CRISPR KO, KI, isogenic panels) | **$15,000–30,000 per line** | 12–20 weeks | **ISO-certified**; European; good for EU collaborations; specialised in isogenic pairs (WT + KO side-by-side) |
| **Cedars-Sinai iPSC Core** (Los Angeles) | Custom iPSC editing + myogenic differentiation | Quote (academic ~$15,000–25,000 per line) | 12–20 weeks | Academic core; good for North American academic collaborators |
| **Indiana University iPSC Core** | Custom iPSC editing + myogenic differentiation | Quote (academic ~$10,000–20,000 per line) | 10–18 weeks | Academic core; iPSC + muscle differentiation expertise |
| **Bhatia lab (Univ. Toronto)** | iPSC hepatocyte / myocyte / neuronal for metabolism | Quote | 12–20 weeks | Academic collaboration |
| **MyoLine / Institut de Myologie (Paris)** | Immortalised human myoblast + myotube (no CRISPR but large disease panel) | Quote (€8,000–20,000 per project) | 8–16 weeks | **200+ immortalised myoblast lines from 36 diseases**; great for disease-model validation; not CRISPR but useful for cross-reference with HMSR findings |
| **Allen Institute for Cell Science** | Edited iPSC lines + reporter iPSC lines | Quote; some lines free for academic | 8–16 weeks | Open-science oriented; some lines free via Coriell |
| **Coriell Institute** (NIGMS Repository) | iPSC + fibroblast + lymphoblast lines (catalog) | **$1,200–2,500 per vial** | 1–4 weeks | **Includes the NIA Aging Cell Repository** (sarcopenic / centenarian / progeria lines) — **check for existing iPSC from sarcopenic donors** before commissioning a custom one |

### 7.1 — iPSC editing strategy: CRO vs in-house (cost + time)

| Approach | Cost (USD) | Lead time | Pros | Cons |
|---|---|---|---|---|
| **CRO (Crown Bio or Cellectics) — turnkey** | $15K–$30K per line | 12–20 weeks | **Turnkey**; CRO handles design + clone pick + karyotype + off-target + myogenic validation; IP usually stays with the PI; 3 clone lines per gene | High cost; IP may be co-owned with CRO in some cases |
| **In-house IDT Alt-R HiFi Cas9 RNP + electroporation** | $5K–$10K per line (reagents) | 8–12 weeks | **Cheaper**; full IP control; 3 clone lines per gene; uses existing lab equipment (electroporator, FACS); can do the full pipeline if you have the manpower | Requires in-house CRISPR expertise; 6+ months of FTE time per gene; higher risk of failure |
| **Synthego knock-out kit (SpCas9 + sgRNA)** | $1,500 per gene | 8–10 weeks | Cheapest commercial option; includes SpCas9 + 2 sgRNAs + electroporation enhancer | Lower success rate; you still need to clone + screen + QC |
| **Horizon Edit-R CRISPR** | $500 per crRNA + $500 Cas9 | 8–12 weeks | Custom crRNA; established workflow; lentiviral or RNP | Similar to in-house IDT |
| **Addgene deposited KO lines** | $75 (plasmid) | 1 week (plasmid); 6–9 weeks (AAV) | Free for academic; existing lines | **May not be isogenic to your parental line**; must re-validate |

**Recommendation for Aim 3:** **CRO (Cellectics or Crown Bio) for the first attempt** (lower risk, faster, full QC); if the program expands (e.g., 5+ KO lines), **move in-house** for cost efficiency.

### 7.2 — iPSC clone characterisation: minimum QC for publication

For each isogenic KO iPSC line (CHCHD10 KO, ATP5F1B KO, WT control):

| QC | Method | Pass criterion | Cost (USD) | Time |
|---|---|---|---|---|
| **Karyotype** | G-banding (20 metaphases) or SNP array (Illumina Infinium CytoSNP-850K) | Normal (no clonal abnormalities) | $300–500 | 1–2 weeks |
| **Off-target analysis** | GUIDE-seq (most rigorous) or CIRCLE-seq or in silico only | <5 off-target sites with high probability score; confirm by Sanger | $1,500 (GUIDE-seq) or $200 (in silico) | 1–4 weeks |
| **Sanger sequencing of edited locus** | PCR + Sanger | Homozygous KO (frameshift) | $200 | 1 week |
| **Pluripotency markers (iPSC)** | Oct4, SSEA4, TRA-1-60 IF (3+ markers) | >90% positive | $200 in Abs + 1 day | 1 day |
| **Myogenic differentiation** | Desmin, MyHC, α-actinin IF on day-10 myotubes | Striated myotubes, ≥30% fusion | $200 in Abs + 5 days | 1 week |
| **Functional validation** | Seahorse Mito Stress Test (basal OCR drop expected) | OCR reduced ≥30% vs. WT | $300 (Seahorse) + 1 week | 1–2 weeks |
| **Sterility** | Standard microbiology | Negative | $50 | 1 week |
| **Mycoplasma** | PCR | Negative | $100 | 1 day |
| **STR / fingerprinting** | Short tandem repeat | Match to parental line | $200 | 1 week |
| **Total QC cost per line** | | | **$3,000–5,000** | **4–8 weeks** |

**If a CRO does the editing, they usually include 2–4 of these QC steps; the PI should add the others (especially off-target + Seahorse functional validation).**

### 7.3 — Disease-relevant iPSC line sourcing (Coriell Aging Cell Repository)

If Aim 3 wants to compare isogenic KO lines against a *real* sarcopenic-donor iPSC (rather than the WT baseline), the **Coriell NIA Aging Cell Repository** is the cheapest source:

| Catalog | Cell type | Donor info | Price (USD) | Lead time |
|---|---|---|---|---|
| **AG16409, AG16527, etc.** | iPSC from aged donors (sarcopenic, progeria, centenarian) | Age 70–100+; some with sarcopenia | $1,200–2,500 | 1–4 weeks |
| **AG06173, AG04062, etc.** | Fibroblasts from progeria patients (Hutchinson-Gilford, Werner) | Genetic; rare; | $1,200 | 1–4 weeks |
| **GM07522, GM01660, etc.** | Lymphoblast lines from aged controls | Age 70+ | $200–500 | 1–4 weeks |
| **Coriell iPSC catalog** | iPSC lines from healthy donors (various ages) | Age 0–80+ | $1,200–2,500 | 1–4 weeks |

**Note:** Coriell iPSC lines are typically **fibroblast-derived or blood-derived iPSC, NOT myogenic**. You must differentiate them to myocytes yourself (using a directed differentiation protocol, e.g., the Bhatt lab protocol or the bit.bio opti-ox platform). **The bit.bio / CDI myocytes are pre-differentiated and ready to use.**

**For Aim 3's isogenic KO + sarcopenic-donor comparison:**
- Use **bit.bio WT myocytes** as the WT reference (cheap, fast)
- Use **Crown Bio / Cellectics CHCHD10 KO** (isogenic to bit.bio) as the KD/KO model
- Use **Coriell AG16409 or similar** (aged donor, then differentiate in-house) as the disease reference
- This is the cleanest experimental design

### 7.4 — MyoLine (Institut de Myologie) — the immortalised myoblast alternative

If **CRISPR-edited iPSC is too expensive or slow**, consider **MyoLine's immortalised human myoblasts**:
- **200+ lines from 36+ neuromuscular diseases** (DMD, LGMD, FSHD, SMA, etc.)
- **Not CRISPR-edited** but **patient-derived**; **already carry the disease mutation**
- **MTA-based distribution**; **requires collaboration with Institut de Myologie**
- **Cost:** €8,000–20,000 per project (line + characterisation + differentiation protocol)
- **Lead time:** 8–16 weeks

**For HMSR's specific question (CHCHD10 KO + sarcopenic donor):** **MyoLine is the wrong resource** (no sarcopenia lines, no CHCHD10 mutation). **Use the CDI / bit.bio / Crown Bio pipeline instead.**

---

## 8. Histology / TEM / RNA-seq (Aims 1, 2, Exp A–D)

| Service | Vendor | Price per sample (USD) | Lead time | Notes |
|---|---|---|---|---|
| **Histology (H&E, Masson's trichrome, picrosirius red)** | University core or **HistoWiz** | **$50–200/slide** | 1–2 weeks | **Standard**; for fibre CSA, fibrosis scoring |
| **Immunohistochemistry (single-plex, chromogenic DAB)** | University core or HistoWiz | **$100–300/slide** | 1–3 weeks | For CHCHD10, NDUFB4, ATP5F1B, PGC-1α, TFAM on FFPE sections (Exp A/B) |
| **Multiplex IHC (Opal, 6-plex)** | **Akoya Biosciences service**; **University cores with Akoya BOND RX** | **$300–500/slide** for the multiplex panel | 2–3 weeks | **Multiplex IF for fibre-typing (DSHB A4.951 + SC-71 + BF-F3 + DAPI)**; also for senescence (p16 + p21 + IL-6 + DAPI); the Akoya Phenoptics workflow is the gold standard |
| **RNAscope in-situ hybridization** (mRNA) | **ACDBio** (own service) or **University core** | **$300–500/slide** | 2–4 weeks | For single-gene mRNA localization; not the primary readout here |
| **Transmission Electron Microscopy (TEM, mitochondria morphology)** | University core or **Electron Microscopy Sciences** | **$200–500/sample** (prep + imaging); **$100–300 per image** if imager is rented | 2–4 weeks | **Critical for cristae morphology** (CHCHD10 KD, APOO KD); requires a muscle TEM specialist; **JEOL 1400 / Hitachi HT7800** are the typical scopes; standard protocols: glutaraldehyde + OsO4 + uranyl acetate |
| **Cryo-EM (for supercomplex structure)** | University cryo-EM facility | **$500–2,000 per session** | 1–4 weeks (booking) | Out of scope for the standard program; only needed if structural follow-up |
| **RNA-seq library prep + sequencing (NovaSeq 6000, PE150, 30M reads/sample)** | **Azenta Life Sciences (formerly GeneWiz)** / **Novogene** / **BGI** / **Eurofins** | **$200–300/sample (PE150, 30M reads)** | 4–6 weeks | **Industry standard**; **Azenta (US, fast turnaround)**, **Novogene (China, lowest cost)**, **BGI (China, very low cost, IP concerns for some applications)**; for HMSR, use **Azenta** if budget allows, **Novogene** if budget-constrained; ship RNA on dry ice |
| **RNA-seq library prep + sequencing (Illumina NextSeq 2000, P2 flowcell)** | Same vendors | **$150–250/sample** | 3–4 weeks | Lower-output alternative; 30M reads still achievable on NextSeq P2 |
| **RNA-seq library prep + sequencing (Illumina NovaSeq X Plus, 25B flowcell)** | Same vendors | **$150–250/sample (lower at scale)** | 3–4 weeks | Newest NovaSeq; competitive pricing in 2026 |
| **Small RNA-seq (miRNA)** | Same vendors | **$250–400/sample** | 4–6 weeks | Not needed for HMSR unless miRNA axis pursued |
| **Single-cell RNA-seq (10x Genomics 3' v3.1, 10,000 cells/sample)** | Same vendors + **10x Genomics service providers** | **$1,500–3,000/sample** (library + sequencing) | 4–8 weeks | Out of scope for the standard HMSR program; only if scRNA-seq follow-up |
| **Spatial transcriptomics (10x Visium HD)** | 10x Genomics service providers | **$3,000–5,000/slide** | 6–10 weeks | Out of scope; would be a follow-up paper |
| **RNA-seq bioinformatics (DESeq2 / edgeR / limma)** | In-house | **Free** (compute + analyst time) | n/a | Use the existing HMSR DESeq2 pipeline (R / Snakemake); 1 week of analyst time per Aim |
| **Spatial proteomics (Imaging Mass Cytometry, Hyperion)** | **Standard BioTools** service or university core | **$500–1,000/slide** | 4–8 weeks | Out of scope; not needed for HMSR |
| **Mass-spec proteomics (LC-MS/MS, label-free, OXPHOS panel)** | University core or **Cell Signaling Technology PTMScan** | **$200–500/sample** | 4–6 weeks | **For Aim 1 protein validation (alternative to WB)**: targeted OXPHOS panel via parallel-reaction monitoring (PRM); ~50 OXPHOS + biogenesis proteins quantified per sample |

### 8.1 — RNA-seq: detailed cost breakdown by tissue × sample number

| Experiment | # of samples | Vendor | Price (USD) | Total (USD) | Notes |
|---|---|---|---|---|---|
| **Aim 1 cohort RNA-seq (human muscle biopsies)** | 30 samples (n=15/group × 2 groups) | Azenta | $250 | $7,500 | Validates the v0.4 finding at the bulk-RNA level (the discovery paper) |
| **Aim 2 C2C12 KD RNA-seq** (8 constructs × 2 species × 3 biological reps = 48) | 48 samples | Azenta | $250 | $12,000 | Confirms the *programme* signature in vitro |
| **Aim 3 PGC-1α KD + rescue** | 24 samples | Azenta | $250 | $6,000 | The programme-master test |
| **Exp B in-vivo (3 constructs × 10 mice × 4 muscles = 120)** | 120 samples | Azenta | $250 | $30,000 | The in-vivo signature; or downsample to 4 muscles per mouse × 10 mice × 3 constructs = 120 (full); or use bulk TA only (3×10 = 30) for $7,500 |
| **Exp C exercise** (3 groups × 12 mice × 1 muscle = 36) | 36 samples | Azenta | $250 | $9,000 | The exercise-reversal signature |
| **Exp D therapeutic** (3 arms × 15 mice × 1 muscle = 45) | 45 samples | Azenta | $250 | $11,250 | The therapeutic signature |
| **Total RNA-seq budget** | ~300 samples | | | **~$75,000** | If fully powered; **realistic trimmed budget: $25,000–$30,000** (Aim 1 + Aim 2 + Exp B signature only) |

**RNA-seq is the largest consumable line item after personnel.** Plan accordingly.

**RNA-seq alternatives for cost savings:**
- **3' mRNA-seq (Lexogen QuantSeq, BRB-seq)** — only the 3' end; 10× cheaper ($30/sample library prep); **less sensitive for low-expression transcripts** (mitochondrial-encoded OXPHOS genes may be missed)
- **Bulk RNA-seq with lower depth (10M reads vs 30M)** — $100/sample; **acceptable for differential expression of well-expressed genes** (most of the HMSR candidates are well-expressed)
- **Targeted RNA-seq (Illumina TruSeq, Nanostring)** — $200–500 per panel; **only the panel of genes is measured**; good for validating specific gene signatures

### 8.2 — TEM: cost breakdown per sample

| Step | Vendor | Price (USD) per sample | Notes |
|---|---|---|---|
| **Tissue fixation (glutaraldehyde + paraformaldehyde)** | In-house or histology core | $20 | Standard EM fixation |
| **Dehydration + embedding (epoxy resin)** | University EM core | $50 | Standard |
| **Ultramicrotomy (60–80 nm sections)** | University EM core | $50 | Standard |
| **Heavy metal staining (uranyl acetate + lead citrate)** | University EM core | $30 | Standard |
| **Imaging (JEOL 1400 or similar, 80 kV)** | University EM core | $100–200 | Per sample; **5–10 images per sample** for cristae morphology |
| **Image analysis (ImageJ + manual scoring)** | In-house | free | 1–2 h per sample for cristae morphology quantification |
| **Total per sample** | | **$250–350** | **$3,000–5,000 for 15 samples (Exp B + D)** |

**For Exp A (16 mice × 3 muscles × 1 block per muscle = 48 samples):** $300 × 48 = **$14,400** — substantial. **Down-sample to n=6/group × 3 muscles = 18 samples** = $5,400.

### 8.3 — Histology / IHC: cost breakdown per slide

| Service | Vendor | Price (USD) per slide | For Exp A + B + C + D |
|---|---|---|---|
| **H&E (routine)** | University core or HistoWiz | $20–50 | $20 × 100 slides = $2,000 |
| **Masson's trichrome (fibrosis)** | University core | $50–100 | $75 × 50 = $3,750 |
| **Single-plex IHC (DAB chromogenic)** | University core | $100–300 | $200 × 80 = $16,000 |
| **Multiplex IF (Opal 6-plex)** | Akoya service / core | $300–500 | $400 × 30 = $12,000 |
| **RNAscope ISH** | ACDBio service | $300–500 | $400 × 10 = $4,000 |
| **Total histology budget** | | | **~$38,000** | For full program |

**Cost-saving:** Use **HistoWiz** (online histology service) for routine H&E / trichrome; their pricing is 50–70% lower than university cores for routine stains, with similar quality.

### 8.4 — Proteomics: detailed cost breakdown for the OXPHOS panel

| Service | Vendor | Price (USD) per sample | For Aim 1 (n=20 cohort) |
|---|---|---|---|
| **Sample prep (lysis, digestion, peptide cleanup)** | University core or vendor | $100 | $2,000 |
| **LC-MS/MS (DDA, label-free, 60-min gradient)** | University core | $200 | $4,000 |
| **LC-MS/MS (PRM, targeted OXPHOS panel, 50 proteins)** | University core or vendor (Thermo) | $300 | $6,000 |
| **Data analysis (SpectroDive + Perseus)** | In-house | free | free |
| **Total proteomics budget (Aim 1)** | | | **$6,000–8,000** |

**If pursuing the OXPHOS panel as a primary Aim 1 readout:** This is the cost-effective alternative to 41 individual Western blots. The PRM (parallel-reaction monitoring) panel can quantify 50+ OXPHOS / biogenesis proteins in a single 60-min LC-MS/MS run per sample.

---

## 9. Cost rollup for Aim 2 PoC (in-vitro only, 6 months)

The Aim 2 PoC is the **fastest, cheapest, highest-leverage arm** of the validation program. It uses only the in-vitro models (C2C12 + HSMM + iPSC myotube), knockdown reagents, Seahorse, and a 2D myotube contractility rig (or CRO service for 3D myobundle).

| Item | Vendor / source | Subtotal (USD) |
|---|---|---|
| C2C12 myoblast (ATCC CRL-1772) + HSMM (Lonza CC-2580) + 1 iPSC line (bit.bio, 2-vial pack) | ATCC + Lonza + bit.bio | $540 + $1,387 + $1,198 = **$3,125** |
| siRNA/shRNA/sgRNA constructs (8 constructs × 2 species, Horizon ON-TARGETplus 2.0 SMARTpool) | Horizon Discovery | 16 SMARTpools × $154 = **$2,464**; + individual sets for deconvolution $1,500; total **$3,964** |
| Antibodies (lean 12-Ab core panel + 2 loading + 2 IF secondary, per `ANTIBODY_PANEL.md` §6) | CST + Abcam + Proteintech + DSHB | **$4,500** (per the ANTIBODY_PANEL.md top-5 list + essentials) |
| Seahorse reagents (6 plates, full Mito Stress Test Kit + FCCP titration) | Agilent (103015-100 kit) + FluxPak | 1 × Mito Stress Test Kit $1,087 + 1 × FluxPak $2,021 + oligomycin/FCCP titrations $400 = **$3,508** |
| 3D myobundle setup (fibrinogen, Matrigel, thrombin, custom 3D-printed PDMS posts) | Sigma + Corning + custom machine shop | $1,500 reagents + $1,500 posts (3 prints) = **$3,000** |
| Organ-bath / force rig (purchase OR core fee, 6 months) | Aurora Scientific 300E + 605A (~$13K); or IonOptix MyoCam-S (~$10K); or university core (~$100/plate × 30 plates = $3,000) | **$3,000 (core) – $13,000 (purchase)** |
| Consumables (culture plates, media, FBS, plastic, pipettes) | Multiple | **$5,000** |
| Personnel (1 postdoc × 6 months × 30% FTE) | $80K/yr fully loaded × 0.30 × 0.5 yr | **$12,000** (30% FTE) — see note below |
| RNA-seq pilot (n=12 samples, 1 plate) | Azenta | **$2,500** |
| TEM (n=4 samples, cristae morphology pilot) | University EM core | **$1,200** |
| Histology (H&E, trichrome, IHC pilot) | University core | **$1,500** |
| **Subtotal (in-vitro Aim 2 PoC, core-fee rig)** | | **~$40,000** |
| **Subtotal (in-vitro Aim 2 PoC, purchased rig)** | | **~$52,000** |
| **Subtotal with 50% postdoc FTE (more realistic)** | | **~$50,000–60,000** |

**Personnel note:** The v0.2 plan's 30% FTE postdoc allocation is conservative for a 6-month PoC. A realistic 50% FTE × 6 months × $80K fully loaded = $20,000, which is closer to the spec's $25K figure. **The v0.3 budget uses $20K (50% FTE) for the PoC.**

**Recommendation:** **~$55,000–65,000 for the in-vitro PoC** (using the core-fee rig + 50% postdoc). This is significantly higher than the v0.2 plan's $120–160K total (which was an aggregate for the whole 14-month program), but appropriate for the in-vitro-only 6-month arm.

**Budget-constrained version:** **~$30,000–40,000.** Defer iPSC (save $1,200), use C2C12 only (save $1,387), use university Seahorse core (save $2,000), use university force core (save $3,000), skip TEM (save $1,200), use 25% postdoc FTE (save $5,000). **The minimum viable Aim 2 PoC is ~$30,000.**

---

## 10. Cost rollup for full in-vivo + therapeutic program (Exp A, B, C, D)

| Item | Vendor / source | Subtotal (USD) |
|---|---|---|
| **Young + aged C57BL/6J** (Exp A: 16, Exp B: 20, Exp C: 36, Exp D: 45) = **117 mice** | NIA (free for aged) + JAX (young) + JAX (some aged) | 60 young × $30 (JAX) = $1,800; 57 aged × $140 (NIA free or JAX backup) = $0 (if NIA) or $7,980 (if JAX); **median $1,800**; + shipping & health monitoring $2,000 = **$3,800** |
| **AAV9 production** (3 constructs × 2 batches; 1 mL @ ≥10¹³ GC/mL each) | VectorBuilder ultra-purified large | $3,099 × 3 × 2 = $18,594 list; academic 10–20% discount = **$15,000–17,000**; UNC alt $2,200 × 6 = $13,200 (lower titer) — **$15,000** |
| **In-vivo single-fibre force rig** (purchase OR core fee, 18 months) | Aurora 1300A (~$50K) — one-time capex; OR university core ($500/mouse × 117 mice) = $58,500; OR amortized over 18 months = $25,000 | **$15,000** (50% capex + 50% core, blended) |
| **Exercise wheels + treadmills + metabolic cages** | Columbus Instruments / Sable Systems / Lafayette | Voluntary wheel: $300/each × 24 wheels = $7,200; Treadmill (6-lane): $8,000; Metabolic cages (8 cage system, Promethion): $35,000 (or rent); **$15,000** (wheel + treadmill, no cages for in-house) |
| **Aged-mouse colony maintenance** (in-house, 18 months) | $1.50/mouse/day × 60 mice × 540 days | $48,600 (this is a major line item!); **$20,000** if the colony is small (30 mice) or the cost is shared with other grants |
| **Personnel** (1 postdoc × 18 months × 50% FTE) | $80K/yr fully loaded × 0.50 × 1.5 yr | **$60,000** |
| **Reagents, consumables, histology, RNA-seq, TEM, IHC** | Multiple | $25,000 (RNA-seq 100 samples × $250) + $10,000 (histology / IHC / TEM) + $5,000 (consumables) = **$40,000** |
| **iPSC line (CHCHD10 + ATP5F1B KO isogenic)** for Aim 3 | Crown Bio or Cellectics | $15K–$30K × 2 lines = **$30,000–$60,000**; if bit.bio + in-house CRISPR: **$10,000–$15,000** |
| **ProCytech / MyoScreen / CRO service for 3D myobundle** (Aim 2 supplement) | ProCytech | $10K–$15K per condition × 3 conditions = **$30,000–$45,000**; or skip and use in-house |
| **Subtotal (in-vivo + therapeutic, no CRO 3D service)** | | **~$180,000–$200,000** |
| **Subtotal (in-vivo + therapeutic, full CRO 3D service)** | | **~$220,000–$250,000** |

**Combined v0.3 budget: ~$250,000–$300,000** (in-vitro PoC $55K–65K + full in-vivo $180K–$200K + iPSC CRO $30K–$60K).

This is **higher than v0.2's $120–160K** because the v0.2 estimate was incomplete:
- **v0.2 omitted personnel** (the largest line item): v0.2 was reagent-only.
- **v0.2 omitted the in-house aging colony maintenance** ($20K–$50K).
- **v0.2 omitted the 3D myobundle CRO service** ($30K–$45K if used).
- **v0.2 omitted the iPSC line creation cost** ($30K–$60K if used).

The v0.3 budget reflects a **complete, RFP-ready estimate** including all major line items. If the budget must be cut to v0.2 levels, defer iPSC (save $30K–$60K) and 3D myobundle CRO (save $30K–$45K), and use a university core for force measurement (save $15K).

**Minimum viable v0.3 budget: ~$180,000** (in-vitro PoC $55K + in-vivo core $125K).

---

## 11. Decision summary

### Top 3 immediate vendor contacts (request quote this week)

| # | Vendor | Category | Lead time | Why first | What to ask for |
|---|---|---|---|---|---|
| 1 | **VectorBuilder** | AAV9 production | 4–6 weeks | Longest lead; Exp B (AAV9-shRNA in vivo) is the keystone in-vivo experiment; 3 constructs × 2 batches × 1 mL ultra-purified research grade | Quote for **AAV9-shRNA (CHCHD10, ATP5F1B, scramble) × 2 batches × 1 mL @ ≥1×10¹³ GC/mL**; include full QC (titer, endotoxin, sterility, purity, full capsid ratio) |
| 2 | **Horizon Discovery (Dharmacon)** | siRNA SMARTpool | 5–10 days | The keystone Aim 2 reagent; 8 constructs × 2 species × $154 = $2,464; turnaround is fast enough to start Aim 2 within 2 weeks | Quote for **ON-TARGETplus 2.0 SMARTpool** for: *CHCHD10, NDUFB4, ATP5F1B, MRPL34, APOO, PPARGC1A, TFAM, scramble* × mouse + human = 16 SMARTpools; + Set of 4 individual oligos for the top 3 (CHCHD10, NDUFB4, ATP5F1B); + ON-TARGETplus Non-Targeting Pool + GAPD Control Pool |
| 3 | **NIA Aged Rodent Colony** | Aged C57BL/6JN mice | 4–8 weeks | **Free**, but requires grant eligibility + quota (10–20 mice/month); the 24-mo + 28-mo mice for Exp A + Exp D are the rate-limiting in-vivo reagent | Register on the **Rodent Ordering System (ROS)**; request **24-mo male C57BL/6JN** for Exp A (n=8, M4–6); + 24-mo for Exp D (n=15, M8–14); confirm PI has aging-related grant; allow 4–8 weeks for delivery |

### Top 3 CRO candidates (request proposal this month)

| # | CRO | Category | Lead time | Why first | What to ask for |
|---|---|---|---|---|---|
| 1 | **ProCytech** (France) | 3D myobundle + force | 8–12 weeks | **Gold standard muscle CRO** for in-vitro 3D myobundle + force; provides the muscle-quality readout for Aim 2; if the in-house rig cannot do 3D myobundle, ProCytech is the alternative | Proposal for **3D myobundle contractility (HSMM + C2C12, 4 conditions: scramble + 3 Tier-1/2 KDs)** = $32,000–60,000; include IF, CSA, force, fatigue; turnaround 8–12 weeks |
| 2 | **Crown Bio** (US) | iPSC myocyte + aging panel | 16–24 weeks | Full-service iPSC myocyte + aging-mimicking panel; can deliver the isogenic CRISPR-edited iPSC lines for Aim 3; alternative to bit.bio + in-house CRISPR | Proposal for **isogenic CHCHD10 KO + ATP5F1B KO iPSC myocyte lines** (2 lines) = $30,000–60,000; include full QC (karyotype, off-target, myogenic markers, Seahorse baseline); 16–24 weeks |
| 3 | **Penn Vector Core / Franklin Biolabs** | GMP-grade AAV9 | 3–8 weeks (Franklin) or 6–10 weeks (legacy Penn) | **Gold standard for muscle-tropic AAV** (AAV9 / AAVrh74); if the project moves toward pre-IND / clinical-grade, this is the route; for research-grade, VectorBuilder is cheaper, but the catalog lots (Addgene-distributed) are the gold standard for **head-to-head literature comparisons** | Quote for **AAV9-shRNA (CHCHD10 + ATP5F1B) × 2 batches** in research-grade (Addgene-distributed catalog if available, else Franklin custom) — turn-around 3–8 weeks; titer ≥1×10¹³ vg/mL; iodixanol-purified |

### Cost-of-delay risk (place orders ASAP if Exp B/D is in scope)

| Long-lead item | Lead time | Order deadline (for Exp B start at M4) | Notes |
|---|---|---|---|
| **AAV9 production (VectorBuilder ultra-purified)** | 4–6 weeks (research) | **M0** (now) | Cannot be expedited; cloning + production + QC + shipping = 4–6 weeks minimum |
| **NIA aged-mouse colony (24-mo C57BL/6JN)** | 4–8 weeks | **M0** (now) | Cannot be expedited; NIA quota is 10–20 mice/month; cap may force split delivery |
| **In-house aging colony (30-mo, 36-mo mice)** | 6–24 months | **M0** (now) | Cannot be expedited; **start the in-house aging colony at M0** to enable 30-mo cohorts for Exp D's later timepoints |
| **iPSC CRISPR KO line (Cellectics / Crown Bio)** | 12–20 weeks | **M0** (now) | If Aim 3 needs isogenic KO lines, the CRO is the rate-limiting reagent; **start the quote this month** |
| **Aged-mouse colony maintenance in-house (IACUC + DLAR)** | 2–3 months (approval) | **M0–M1** (now) | IACUC + DLAR approval takes 2–3 months; **file the protocol this month** |
| **Aurora Scientific 1300A force rig (purchase)** | 4–8 weeks | **M0** (now) | If buying rather than using a core, the rig arrives in 4–8 weeks; **if using a core, book the time slot at M0** to ensure availability for M4–M14 |

### Honest call-outs / what could go wrong

| Risk | Mitigation |
|---|---|
| **NIA aged-mouse quota may be exhausted** (limited monthly supply) | Place NIA order at M0; have **JAX 24-mo backup** ready; consider Charles River for in-between ages |
| **iPSC CRO services often run 2–3× over quoted timeline** | Build the 12-week lead time into the Aim 3 plan; have a **bit.bio + in-house CRISPR backup** |
| **AAV9 tropism in old (24-mo) mice is less efficient** than in young mice (impaired vascularisation, ECM changes) | Order **3–5× the dose** for aged mice; consider **AAVrh74** (better muscle tropism) as alternative; or use **dual AAV9 + electroporation** to enhance uptake |
| **Lonza HSMM is now $1,387/amp** (not $600 as in older estimates) | If budget is tight, **use Cook Myosite mouse primary myoblasts** ($400–600/prep) + bit.bio ioSkeletal Myocytes for the human arm ($1,198) instead of Lonza |
| **Aurora 1300A is not in the 2026 budget** | Use university core for Exp A + B; reserve $30K–60K for the rig if the program is renewed in Y2 |
| **Personnel is the largest single line item** | A 50%-FTE postdoc is a realistic ask for the 18-month program; **co-funding from a second grant halves the burden** |
| **C2C12 high-passage drift** | **Always use passage ≤15**; subclone early; freeze a master stock; the ECACC 91031101 / ATCC CRL-1772 are the validated, authenticated sources — **avoid "C2C12" lines from non-validated vendors** |
| **ECACC 91031101 and ATCC CRL-1772 are the SAME subclone** (Yaffe & Saxel 1977) — some published papers report phenotypic differences because the two distributors' stocks have drifted slightly | **Use one source per experiment**; do not mix stocks in the same comparison |
| **ProCytech and other muscle CROs are slow** (8–12 weeks) | **Book the CRO slot at M0** even if you don't have the constructs ready; the CRO slot calendar is the rate-limiting step |
| **Lonza CC-2580 has "low stock availability"** (per Lonza's product page) | **Order early**; if out of stock, request **CellBio Services** custom donor; or use bit.bio ioSkeletal Myocytes for the WT control and accept that the HSMM arm will be partially bit.bio |

### Vendors NOT to use (anti-recommendations)

- **Cell biologics (HCS-supplier) for "C2C12" lines** — multiple paper retractions have documented misidentified lines; always use **ATCC or ECACC authenticated stocks**
- **AAV from non-validated academic cores without titer QC** — empty capsids can dominate; **always request titer by ddPCR + full capsid ratio**
- **Santa Cruz Biotechnology antibodies** for OXPHOS — **frequent lot-to-lot variability**; use **Abcam / CST / Proteintech** instead
- **"Generic" iPSC lines from non-validated banks** — the line may not be myogenic-capable; **always use a validated source (CDI, bit.bio, Coriell NIGMS, MyoLine)**
- **Bcl2- or hTERT-immortalised myoblasts from non-muscle sources** — these are useful for some applications but **not for the specific force / contractility readouts of Aim 2**; the immortalisation alters the contractile phenotype

---

## 12. RFP templates (one-page each, ready to send)

The following one-page templates can be sent to each vendor as a quote request. They include the experimental design, volumes, QC requirements, and delivery constraints. The templates are in §12.1–§12.6.

### 12.1 — VectorBuilder RFP (AAV9 production)

```
TO: VectorBuilder Sales (sales@vectorbuilder.com)
FROM: [PI Name], [Institution]
RE: AAV9-shRNA production quote

We request a quote for the following AAV production:

Serotype: AAV9 (3 constructs × 2 batches each)
Scale: 1 mL @ ≥1×10¹³ GC/mL per batch (ultra-purified research grade)
Total: 6 batches

Constructs:
  1. AAV9-CAG-GFP-U6-mShRNA-Chchd10 (mouse)
  2. AAV9-CAG-GFP-U6-mShRNA-Atp5f1b (mouse)
  3. AAV9-CAG-GFP-U6-scramble (control)

QC required (per batch):
  - Titer by ddPCR
  - Endotoxin < 10 EU/mL
  - Sterility (USP <71>)
  - Mycoplasma (PCR)
  - Purity by SDS-PAGE (>80%)
  - Full capsid ratio (>70%, A260/A280)

Delivery: VectorBuilder should provide COA + QC report per batch.
Shipping: dry ice, overnight to [institution address].
Lead time: ≤ 6 weeks from PO acceptance.

Please provide: list price, academic discount, lead time, and 3 customer
references for similar-scale AAV9-muscle work.

Thank you,
[PI Name, Title, Email, Phone]
```

### 12.2 — Horizon Discovery RFP (siRNA)

```
TO: Horizon Discovery Sales (sales@horizondiscovery.com)
FROM: [PI Name], [Institution]
RE: ON-TARGETplus 2.0 SMARTpool + individual sets quote

We request a quote for the following siRNA reagents (mouse + human):

ON-TARGETplus 2.0 SMARTpool (one tube per gene, 5 nmol):
  - CHCHD10 (human + mouse)
  - NDUFB4 (human + mouse)
  - ATP5F1B (human + mouse)
  - MRPL34 (human + mouse)
  - APOO (human + mouse)
  - PPARGC1A (human + mouse)
  - TFAM (human + mouse)
  - Non-Targeting Pool (control)
  - GAPD Control Pool (positive control)
  Total: 14 SMARTpools (16 with the 2 controls)

ON-TARGETplus Set of 4 individual oligos (top 3 KD targets):
  - CHCHD10, NDUFB4, ATP5F1B × human + mouse = 6 sets

Delivery: 5–10 business days from PO acceptance.
Please include: sequence information, certificate of analysis, and
SMARTselection design algorithm details.

Thank you,
[PI Name]
```

### 12.3 — NIA Aged Rodent Colony RFP

```
TO: NIA Rodent Ordering System (https://ros.nia.nih.gov/)
FROM: [PI Name], [Institution]
RE: C57BL/6JN aged mice for sarcopenia study

We request the following aged mice (free, aging-research grant):

Strain: C57BL/6JN
Sex: Male (or both, if available)
Ages:
  - 24 months: n=8 (for Exp A, observational)
  - 24 months: n=15 (for Exp D, therapeutic; staggered delivery M8–M14)
  - 28 months: n=8 (for Exp D late timepoint; if available)
Total: 23–31 mice over 12 months

Our grant [NIH grant #, e.g., R01AG######] is an active aging-related
grant focused on sarcopenia. The study hypothesis is that the
mitochondrial biogenesis programme is coordinately down-regulated in
aged muscle, causing loss of muscle quality (specific force).

Please confirm: (1) our eligibility, (2) delivery schedule given the
20-animal-per-month cap, (3) DOB of the oldest available cohort.

Thank you,
[PI Name]
```

### 12.4 — ProCytech RFP (3D myobundle + force CRO)

```
TO: ProCytech (contact@procytech.com)
FROM: [PI Name], [Institution]
RE: 3D myobundle contractility CRO service quote

We request a quote for the following CRO service:

Service: 3D human skeletal muscle myobundle (HSMM) + mouse C2C12 myobundle
  with shRNA knockdown + contractility / specific force measurement

Conditions: 4 conditions per cell type × 2 cell types = 8 conditions
  - HSMM scramble shRNA (control)
  - HSMM shCHCHD10
  - HSMM shNDUFB4
  - HSMM shATP5F1B
  - C2C12 scramble shRNA
  - C2C12 shChchd10
  - C2C12 shNdufb4
  - C2C12 shAtp5f1b

Readouts (per condition, n=4 biological replicates):
  - 3D myobundle contractility (specific force, mN/mm²)
  - Myobundle CSA (μm²)
  - Fusion index (% nuclei in myotubes, ≥3 nuclei)
  - IF for myosin heavy chain + sarcomeric α-actinin
  - Seahorse Mito Stress Test (basal, ATP-linked, max, spare OCR)

Deliverables: raw data + analysis report + COA + images; turnaround 8–12 weeks.

Thank you,
[PI Name]
```

### 12.5 — Crown Bio / Cellectics RFP (iPSC CRISPR KO)

```
TO: Crown Bioscience (info@crownbio.com) AND Cellectics (info@cellectics.com)
FROM: [PI Name], [Institution]
RE: Isogenic iPSC myocyte CRISPR KO line quote

We request a quote for the following iPSC CRISPR-edited lines:

Line 1: Wild-type iPSC (control) — bit.bio ioSkeletal Myocytes
        background or equivalent
Line 2: CHCHD10 knockout (homozygous, isogenic to Line 1)
Line 3: ATP5F1B knockout (homozygous, isogenic to Line 1)

Required QC per line:
  - Karyotype (G-band or SNP array)
  - Off-target analysis (GUIDE-seq or similar)
  - Sanger sequencing of edited locus
  - Myogenic differentiation validation (desmin, MyHC, α-actinin IF)
  - Functional validation (Seahorse Mito Stress Test)
  - Sterility, mycoplasma

Delivery: cryopreserved iPSCs + differentiated myocytes + QC report
Lead time: 12–20 weeks from PO acceptance

Please provide: list price, lead time, IP terms, and 3 customer references
for similar iPSC muscle-line projects.

Thank you,
[PI Name]
```

### 12.6 — Aurora Scientific / IonOptix / University Core RFP (force rig)

```
TO: [Vendor / University Core Facility]
FROM: [PI Name], [Institution]
RE: In-vivo + in-vitro force measurement rig quote

We request a quote for the following:

Option A (purchase): Aurora Scientific 1300A 3-in-1 Whole Animal System for Mice
  - 300E Dual-Mode Lever (mouse; 0.5 N)
  - 605A Data Acquisition + Software (DMC + DMA)
  - 701C High-Power Bi-Phasic Stimulator
  - 809C Mouse In-vivo Apparatus
  - 809C-25 Horizontal 25 mL In-vitro Bath
  - All required cables, electrodes, software licenses
  - Lead time: 4–8 weeks
  - Please include academic discount, installation, and 1-year warranty

Option B (service): University muscle-physiology core time
  - 117 mice total (Exp A + B + C + D)
  - $500–1,500 per mouse in-vivo + in-vitro force protocol
  - Total $58,500–175,500 over 18 months
  - Please provide: cost per mouse, lead time for booking, technician availability

Please also quote Option C: IonOptix MyoCam-S + MyoPacer (in-vitro 2D myotube)
  for Aim 2 myotube contractility.

Thank you,
[PI Name]
```

---

## 13. Document cross-references

- **Antibody panel (required for §1–§3 vendors):** `validation/antibodies/ANTIBODY_PANEL.md`
- **Seahorse Mito Stress Test SOP (required for §5 vendors):** `validation/protocols/SEAHORSE_MITO_STRESS_TEST_SOP.md`
- **Experimental validation plan v0.2 (the source plan):** `manuscripts/experimental_validation_plan_v0.2.md`
- **Validation README:** `validation/README.md`

## 14. Versioning and changelog

- **v0.1 (2026-06-13):** Initial RFP-ready vendor shortlist, 14 sections, ~12,000 words. Source: experimental_validation_plan_v0.2.md, ANTIBODY_PANEL.md, and live vendor websites (mid-2026 pricing). All prices and lead times are approximate and current at the time of writing; verify at quote.

---

*Prepared by Larry (Brown Biotech AI partner) on behalf of the HMSR validation working group. v0.1 — 2026-06-13.*
