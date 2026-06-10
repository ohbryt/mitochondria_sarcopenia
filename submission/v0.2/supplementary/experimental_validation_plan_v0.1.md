# In Vitro / In Vivo Experimental Validation Plan
## 7 WP3-Replicated Mitochondrial OXPHOS Genes in Sarcopenia

**Genes:** CHCHD10, CLTB, MRPL34, APOO, MRPL33, NDUFB4, ATP5F1B  
**Evidence basis:** DerSimonian-Laird random-effects meta-analysis across 4 independent cohorts  
(meta-p = 7.5×10⁻⁶ – 3.5×10⁻³; direction consistency = 1.0; LOCO = 100%; I² = 0–48%)  
**Version:** v0.1 — 2026-06-10  

---

## 1. Rationale and Prioritization

The 7 genes form two evidence tiers based on signal strength and heterogeneity:

### Tier 1 — High confidence, low heterogeneity (I² = 0)
| Gene | meta-p | Function |
|------|--------|----------|
| **CHCHD10** | 7.5×10⁻⁶ | Mitochondrial cristae integrity, respiratory supercomplex stability |
| **CLTB** | 1.6×10⁻⁵ | Clathrin light chain B; emerging mitochondrial trafficking role |

### Tier 2 — Moderate confidence, moderate heterogeneity (I² = 34–48%)
| Gene | meta-p | Function |
|------|--------|----------|
| **MRPL34** | 3.6×10⁻⁴ | Mitoribosome large subunit 34 — mt-protein translation |
| **APOO** | 4.9×10⁻⁴ | ATP synthase-associated, F₁Fₒ complex assembly |
| **MRPL33** | 1.3×10⁻³ | Mitoribosome large subunit 33 — mt-protein translation |
| **NDUFB4** | 3.1×10⁻³ | NADH:ubiquinone oxidoreductase subunit B4 — Complex I |
| **ATP5F1B** | 3.5×10⁻³ | ATP synthase F₁ β-subunit — catalytic core of OXPHOS |

**Critical evidence gap:** None of the 7 genes appear in the WP5 exercise
epigenetic ladder (MoTrPAC rat skeletal muscle). Establishing whether endurance
exercise up-regulates these genes in skeletal muscle is a primary experimental objective.

**Experimental priority order:** CHCHD10 → ATP5F1B → NDUFB4 → MRPL33/MRPL34 → APOO → CLTB

---

## 2. In Vitro Experimental Plan

### 2.1 Cell Models

| Model | Use case | Rationale |
|-------|----------|-----------|
| **C2C12 mouse myoblasts** (differentiated to myotubes) | Primary screen, knockdown/KO | Fast, tractable, well-validated differentiation |
| **Primary human skeletal muscle myoblasts (HSMMs)** | Human relevance confirmation | Patient-derived; differentiate to myotubes day 7 |
| **iPSC-derived skeletal myocytes** | Disease-relevant human model | Isogenic KO via CRISPR-Cas9 |

**Differentiation protocol (C2C12):** 70% confluence → switch to 2% horse serum DMEM for 7 days; confirm MHC+ multinucleation by Day 7.

---

### 2.2 Gene Knockdown Screen (Tier 1 + 2)

**Approach:** siRNA-mediated transient knockdown in C2C12 myotubes  
**Timeline:** 72 h post-transfection readout

| Step | Detail |
|------|--------|
| siRNA design | 3 independent siRNAs per gene (Silencer Select or Dharmacon SMARTpool); scramble control |
| Transfection | Lipofectamine RNAiMAX; optimise in myotubes (Day 4 post-diff) |
| Knockdown confirmation | RT-qPCR (ΔΔCt, normalise to RPLP0/GAPDH) + immunoblot at 72 h |
| KD efficiency target | ≥ 70% mRNA reduction; ≥ 60% protein reduction |

---

### 2.3 Primary Readouts — Mitochondrial Function

#### 2.3.1 Mitochondrial Respiration (Seahorse XF)
**Assay:** Mito Stress Test on C2C12 myotubes in XF96 plate

| Parameter | Interpretation |
|-----------|---------------|
| Basal OCR | Baseline mitochondrial respiration |
| ATP-linked OCR (oligomycin) | ATP synthase-coupled respiration |
| Maximal OCR (FCCP) | Respiratory capacity |
| Proton leak | Membrane uncoupling |
| Non-mitochondrial OCR | Non-mt oxygen consumption |
| Spare respiratory capacity | Bioenergetic reserve |

**Expected:** CHCHD10, ATP5F1B, NDUFB4 KD → reduced maximal OCR and ATP-linked OCR. MRPL33/MRPL34 KD → secondary reduction via impaired mt-protein synthesis (slower effect, measure at 96 h).

#### 2.3.2 ATP Production Rate
**Assay:** Seahorse ATP Rate Assay — simultaneously quantifies mitochondrial and glycolytic ATP

**Expected:** KD → shift from mitochondrial to glycolytic ATP (compensation), overall energy deficit in high-demand myotubes.

#### 2.3.3 Mitochondrial Membrane Potential (ΔΨm)
**Assay:** JC-1 or TMRE fluorescence (flow cytometry or plate reader)  
**Expected:** CHCHD10, ATP5F1B KD → reduced ΔΨm (collapse of proton gradient)

#### 2.3.4 ROS Production
**Assay:** MitoSOX Red (mitochondrial superoxide) + CellROX (total ROS), flow cytometry  
**Expected:** Complex I subunit loss (NDUFB4) → elevated mt-ROS

---

### 2.4 Secondary Readouts — Myotube Biology

| Readout | Assay | Rationale |
|---------|-------|-----------|
| Myotube diameter & fusion index | Phase contrast + MHC immunofluorescence | Atrophy-like phenotype |
| Protein synthesis | AHA (O-propargyl-puromycin) labelling | Anabolic capacity |
| Mitochondrial morphology | MitoTracker CMXRos + confocal imaging (aspect ratio, branching) | Fragmentation expected |
| mtDNA copy number | qPCR (mtDNA/nDNA ratio: ND1/B2M) | Mitochondrial biogenesis proxy |
| Mitochondrial mass | MitoTracker Green (ΔΨm-independent), flow cytometry | Content vs. function |
| Myofibrillar protein levels | Immunoblot: MHC, Troponin I, Actin | Structural protein loss |

---

### 2.5 Rescue Experiments

For genes showing the strongest functional phenotype (expected: CHCHD10, ATP5F1B, NDUFB4):

1. **cDNA rescue:** Co-transfect siRNA-resistant cDNA (ORFeome/Addgene) with siRNA; confirm restoration of OCR
2. **Exercise-mimetic rescue:** Treat KD myotubes with AICAR (AMPK activator, 500 µM, 24 h) or electrical pulse stimulation (EPS, 1 Hz, 2 ms, 24 h) to simulate exercise; ask whether exercise signalling can compensate for OXPHOS gene loss
3. **PGC-1α overexpression rescue:** Adenoviral Ad-PGC1α (10 MOI); test if mitobiogenesis induction compensates for individual subunit KD

---

### 2.6 CRISPR-Cas9 Stable KO (iPSC-derived myocytes)

**Purpose:** Isogenic human validation for Tier 1 genes (CHCHD10, ATP5F1B)  
**Approach:**
- SpCas9 + sgRNA pairs targeting exon 2–3 of each gene in H9 iPSCs
- Myogenic differentiation via Pax7-inducible system (doxycycline 7 d)
- Full Seahorse panel + transcriptome (RNA-seq) at myocyte stage
- Compare KO vs. isogenic WT; confirm no off-target effects (whole-genome sequencing)

**Timeline:** ~6 months (KO generation + validation + differentiation + assays)

---

## 3. In Vivo Experimental Plan

### 3.1 Animal Models

| Model | Age | Use case |
|-------|-----|----------|
| **C57BL/6J aged mice** (24 months) | Old | Naturally sarcopenic; test if target genes are down in aged TA/gastrocnemius |
| **C57BL/6J young mice** (3–4 months) + AAV-shRNA | Young | Acute knockdown; phenocopy sarcopenia in young healthy muscle |
| **C57BL/6J young mice + exercise training** | Young | Test exercise regulation of target genes (gap filling WP5) |

---

### 3.2 Experiment A — Expression Validation in Aged Mice (Observational)

**Goal:** Confirm WP3 human transcriptomic findings translate to rodent ageing.

**Design:**
- n = 8 young (3 m) vs. n = 8 old (24 m) male C57BL/6J per group
- Muscles: tibialis anterior (TA), gastrocnemius, soleus
- Readouts: RT-qPCR + immunoblot for all 7 genes; correlate protein levels with grip strength and fibre cross-sectional area (CSA)

**Primary endpoint:** Significant down-regulation of ≥ 4/7 genes in aged vs. young muscle (aligns with human meta-β < 0)

---

### 3.3 Experiment B — AAV-shRNA Knockdown in Young Mice

**Goal:** Determine whether loss of individual OXPHOS genes is sufficient to cause muscle atrophy.

**Priority targets:** CHCHD10 (I²=0, strongest signal), ATP5F1B (catalytic OXPHOS), NDUFB4 (Complex I)

**Design:**
- AAV9-U6-shRNA-mCherry (muscle tropism) injected intramuscularly (TA, 10¹¹ vg/leg)
- Contra-lateral leg: AAV9-scramble-mCherry control
- n = 10 per gene (paired design; each animal is its own control)
- Sacrifice at 8 weeks post-injection

**Functional readouts (in vivo, weekly):**
| Test | Measure |
|------|---------|
| Grip strength (BioSeb) | Fore/hindlimb peak force |
| Wire hang / inverted grid | Endurance proxy |
| Rotarod (15–40 rpm ramp) | Motor coordination/fatigue |
| Body composition (EchoMRI) | Fat mass, lean mass |

**Post-sacrifice readouts:**
| Readout | Method |
|---------|--------|
| Muscle mass (wet weight) | Analytical balance |
| Fibre CSA | H&E + laminin immunofluorescence; 200 fibres/section |
| Fibre type composition | ATPase staining / MHC I, IIa, IIx immunofluorescence |
| Mitochondrial morphology | TEM (transmission electron microscopy) |
| OCR ex vivo | Permeabilized fibre bundles (Oroboros O2k) |
| Complex I/IV activity | Spectrophotometric enzyme assay |
| mtDNA copy number | qPCR |
| Transcriptome | RNA-seq (TA, n=5/group) |

**Sample size justification:** Power = 0.80, α = 0.05, expected effect on CSA = 15% (based on published CHCHD10 mouse data), SD = 10%; n = 9 per group → round to 10.

---

### 3.4 Experiment C — Exercise Training Intervention (Gap Filling)

**Goal:** Determine whether aerobic exercise up-regulates the 7 OXPHOS genes in rodent skeletal muscle — closing the WP5 evidence gap.

**Design:**
- 3-month-old C57BL/6J male mice, n = 12/group
- **Sedentary (SED):** standard cage, ad libitum
- **Voluntary wheel running (VWR):** running wheel access 4 weeks
- **Forced treadmill training (FTT):** 60 min/day, 5 d/week, 4 weeks (15 m/min, 5% grade)
- Sacrifice 48 h after last bout (to capture training adaptation, not acute response)

**Readouts:**
- RT-qPCR + immunoblot for all 7 genes in TA and gastrocnemius
- Seahorse OCR (permeabilized fibres, Oroboros)
- mtDNA copy number
- PGC-1α protein (positive control for exercise response)

**Analysis:** One-way ANOVA (SED vs. VWR vs. FTT) + Tukey HSD; report fold-change with 95% CI for each gene; define exercise-responsive as ≥ 1.5-fold up vs. SED, p < 0.05.

---

### 3.5 Experiment D — Aged Mice + Exercise Rescue

**Goal:** Test whether endurance exercise can partially restore OXPHOS gene expression and muscle function in naturally sarcopenic aged mice.

**Design:**
- 20-month-old C57BL/6J male mice (pre-sarcopenic/early sarcopenic)
- **Aged sedentary:** n = 10
- **Aged VWR (12 weeks):** n = 10
- **Young sedentary (3 m):** n = 8 (reference)

**Primary endpoint:** Change in TA grip strength-normalised CSA between aged SED and aged VWR  
**Secondary endpoints:** mRNA and protein levels of all 7 OXPHOS genes; mitochondrial respiration; fibre type shift

---

## 4. Experimental Timeline

```
Month 1–2:   In vitro siRNA screen (all 7 genes, C2C12, Seahorse)
Month 2–3:   In vitro primary + secondary readouts; rescue experiments
Month 3–4:   HSMM validation of top 3 hits
Month 4–6:   Exp A: aged mouse observational study
Month 4–8:   Exp B: AAV-shRNA KD (injection M4, weekly phenotyping M4–8, sacrifice M8)
Month 5–8:   Exp C: exercise training (gap fill)
Month 6–12:  iPSC-CRISPR KO (Tier 1 only)
Month 8–12:  Exp D: aged mice + exercise rescue
```

---

## 5. Key Decision Gates

| Gate | Criterion | If fail |
|------|-----------|---------|
| siRNA KD efficiency | ≥ 70% mRNA, ≥ 60% protein | Optimise; try alternative siRNA sequences |
| In vitro mitochondrial phenotype | ≥ 1 gene shows ≥ 20% OCR reduction (p < 0.05) | Re-evaluate cell model; switch to HSMMs |
| Aged mouse expression | ≥ 4/7 genes down (FC < 0.7, p < 0.05) | Expand cohort; check muscle sub-type specificity |
| AAV KD efficiency in vivo | ≥ 60% protein reduction at 4 weeks | Increase viral titer or switch to bilateral injection |
| Exercise response (Exp C) | ≥ 1 gene up-regulated ≥ 1.5-fold | Extend training to 8 weeks; try higher intensity |

---

## 6. Expected Outcomes and Publication Strategy

### Tier 1 expected outcomes
- **CHCHD10 KD** → severe mitochondrial fragmentation, cristae disorganisation (TEM), ≥ 30% maximal OCR reduction, myotube atrophy (reduced diameter, fusion index); phenotype rescuable by cDNA
- **ATP5F1B KD** → reduced ATP-linked OCR, compensatory glycolytic shift, ΔΨm reduction
- **NDUFB4 KD** → elevated mt-ROS (MitoSOX), reduced Complex I activity, secondary OCR reduction

### If CLTB KD phenotype is unexpected (I² = 0 but non-canonical OXPHOS gene)
- Explore clathrin-mediated mitophagy: CHCHD10 and CLTB co-IP; mitophagy flux assay (mt-Keima or mito-mRFP-GFP)

### Publication targets
| Paper | Content | Target journal |
|-------|---------|---------------|
| **Paper 1** (current) | HMSR resource + 7-gene discovery | Nature Aging / Aging Cell |
| **Paper 2** | In vitro functional screen (7 genes, C2C12 + HSMM) | J Cachexia Sarcopenia Muscle |
| **Paper 3** | In vivo CHCHD10 ± ATP5F1B (AAV KD + exercise rescue) | JCI / Cell Metabolism |

---

## 7. Resources Required

| Resource | Estimated cost (USD) | Timeline driver |
|----------|---------------------|-----------------|
| siRNA library (21 siRNAs + controls) | $3,000 | Month 1 |
| Seahorse XFe96 cartridges (8 runs) | $6,400 | Month 1–3 |
| C2C12 + HSMM culture consumables | $4,000 | Month 1–4 |
| AAV9 production (3 constructs × 10¹³ vg) | $15,000 | Month 3–4 |
| Aged mice (24 m C57BL/6J, NIA colony) | $12,000 | Month 4 order |
| Young mice (Exps B, C, D) | $8,000 | Month 4–8 |
| TEM sample prep + imaging | $3,500 | Month 7–8 |
| RNA-seq (10 libraries × 30M reads) | $5,000 | Month 8 |
| iPSC-CRISPR KO (core facility) | $20,000 | Month 4–10 |
| **Total estimated** | **~$77,000** | 12 months |

---

## 8. Statistical Analysis Plan

- All in vitro experiments: n ≥ 3 independent differentiations (biological replicates); within each: ≥ 3 technical replicates; report mean ± SEM
- Comparisons: unpaired t-test (2 groups) or one-way ANOVA + Tukey (> 2 groups)
- Seahorse: OCR normalised to total protein (BCA assay); exclude wells with <80% XF quality control
- In vivo: mixed ANOVA (gene × treatment); post-hoc Bonferroni; report effect size (Cohen's d)
- RNA-seq: DESeq2; genome-wide BH-FDR; pre-registered analysis plan before unblinding
- All n, p-values, and effect sizes computed by analysis scripts; no hand-computed values
- Sample blinding: all functional assays and histology scored blinded to treatment group

---

*Plan version v0.1 — 2026-06-10*  
*Basis: WP3 replication_matrix.tsv + wp3_gate_pass.tsv; all effect estimates from committed pipeline code.*
