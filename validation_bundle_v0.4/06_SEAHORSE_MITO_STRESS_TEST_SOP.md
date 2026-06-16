# Seahorse XF Mito Stress Test — Standard Operating Procedure

**Project:** HMSR — Human Muscle Sarcopenia multiomic Resource (v0.2 validation plan)
**Aim:** 2 — Causation (in-vitro functional validation)
**Document ID:** SOP-VAL-AIM2-SEAHORSE-001
**Version:** 1.0
**Effective date:** 2026-06-13
**Authoritative for:** All in-vitro Aim 2 OCR / spare capacity / coupling experiments
**Worktree:** `validation/aim2-causation` (path: `.worktrees/validation-aim2/sarcopenia-multiomic-resource/`)

> **Audience.** A wet-lab scientist with prior Seahorse XF experience but no prior HMSR context must be able to execute this SOP end-to-end against C2C12 or HSMM myotubes, including FCCP titration, normalization, QC gating, and CSA-matched myotube flagging, without consulting any other HMSR document.
>
> **Pairing.** This SOP is the in-vitro functional backbone. It is paired with `myobundle_specific_force_SOP.md` (3D myobundle contractile read-out, separate file) for the matched-CSA force interpretation. Cross-references are noted in §6.4.

---

## Table of contents

1. [Scope and assay overview](#1-scope-and-assay-overview)
2. [Reagents, consumables, instruments — bill of materials](#2-reagents-consumables-instruments--bill-of-materials)
3. [Plate preparation](#3-plate-preparation)
4. [Drug port loading and FCCP titration](#4-drug-port-loading-and-fccp-titration)
5. [Assay protocol — Wave software settings](#5-assay-protocol--wave-software-settings)
6. [Normalization — protein, DNA, and CSA-matched myotube](#6-normalization--protein-dna-and-csa-matched-myotube)
7. [QC gates and acceptance criteria](#7-qc-gates-and-acceptance-criteria)
8. [Data analysis pipeline](#8-data-analysis-pipeline)
9. [Common pitfalls](#9-common-pitfalls)
10. [References](#10-references)
11. [Day-of-Run Checklist (printable)](#11-day-of-run-checklist-printable)

---

## 1. Scope and assay overview

### 1.1 Assay principle

The Seahorse XF Mito Stress Test is a real-time, plate-based, live-cell assay of mitochondrial respiration. The instrument (XFe96 or XFe24) measures dissolved O₂ and free H⁺ in a small transient chamber above adherent cells, computing:

- **OCR** — oxygen consumption rate (pmol O₂ · min⁻¹), a proxy for mitochondrial respiration.
- **ECAR** — extracellular acidification rate (mpH · min⁻¹), driven by glycolytic lactate export and CO₂ hydration.

Three sequential pharmacologic perturbations isolate discrete components of the respiratory chain:

1. **Oligomycin (Port A).** Inhibit the F₁F₀-ATP synthase (complex V). The drop in OCR after oligomycin equals the OCR coupled to ATP synthesis ("ATP-linked OCR"). Residual OCR is the sum of proton leak and non-mitochondrial consumption.
2. **FCCP (Port B).** A protonophore / uncoupler that collapses the inner-membrane ΔpH and ΔΨ, forcing the electron transport chain to operate at maximum electron flux. The peak OCR after FCCP = **maximal OCR**. **Spare (reserve) respiratory capacity = maximal − basal.** Identifying the optimal FCCP concentration requires a separate, mandatory titration step (see §4.3). Skipping the titration is the single most common reason maximal OCR is reported incorrectly.
3. **Rotenone + Antimycin A (Port C).** Rotenone inhibits complex I (NADH:ubiquinone oxidoreductase); antimycin A inhibits complex III (cytochrome bc₁). Together they abolish electron transport through the respiratory chain, leaving only non-mitochondrial O₂ consumption. The post-Rot/AA OCR is subtracted from all other measurements.

### 1.2 Cell models

| Model | Vendor / Catalog | Species | Differentiation | Assay day |
|---|---|---|---|---|
| C2C12 | ATCC CRL-1772 | *Mus musculus* (mouse) myoblast | DM (DMEM + 2% horse serum), 5–7 days | **d5–d7** |
| HSMM (primary) | Lonza CC-2580 | *Homo sapiens* (adult skeletal muscle) | Lonza SkGM-2 → SkMDM, 7–10 days | **d7–d10** |

> HSMM lot-to-lot variability is substantial — Lonza quotes ≤15% CV on donor age, sex, and biopsy site. Track lot number and donor metadata end-to-end (see §6.6).

### 1.3 Plate format

| Format | Instrument | Use case | Wells/genotype per plate (recommended) |
|---|---|---|---|
| **96-well (preferred for screening)** | Seahorse XFe96 | RNAi screen, dose-response, ≥3 genotypes | 6–10 wells/genotype |
| **24-well (confirmation)** | Seahorse XFe24 | Validation, paired with myobundle force | 2–4 wells/genotype |

Default protocol below is written for 96-well; 24-well volumes and any instrument-specific deviations are called out explicitly. **Do not run 96- and 24-well plates in the same Wave session.**

### 1.4 Primary readouts

| Readout | Definition | Units (preferred) | Units (secondary) |
|---|---|---|---|
| Basal OCR | Average of 3 baseline cycles (Rot/AA-subtracted) | pmol O₂ · min⁻¹ · µg protein⁻¹ | pmol O₂ · min⁻¹ · 10⁴ cells⁻¹ |
| ATP-linked OCR | Basal − post-Oligo | same | same |
| Maximal OCR | Peak post-FCCP cycle (Rot/AA-subtracted) | same | same |
| Spare respiratory capacity | Maximal − Basal | same | same |
| Non-mito OCR | Average of last Rot/AA cycle | pmol O₂ · min⁻¹ · well⁻¹ | n/a |
| Coupling efficiency | ATP-linked / Basal | dimensionless | n/a |
| ECAR (auxiliary) | glycolytic flux proxy | mpH · min⁻¹ · µg protein⁻¹ | n/a |

### 1.5 Normalization strategy (top-level)

1. **Primary:** protein content (BCA), reported as OCR · min⁻¹ · µg protein⁻¹.
2. **Secondary:** DNA content (Hoechst 33342), reported as OCR · min⁻¹ · 10⁴ cells⁻¹.
3. **CSA cross-check:** myotube diameter measured in 5–10 random fields per well; any well with mean diameter >15% from plate control mean is flagged and excluded from the "matched-CSA" interpretation (§6.4).

### 1.6 Out of scope

- Live-cell ATP quantification (use a parallel luminescence assay if needed).
- Substrate-specific respiration (pyruvate, fatty acid, glutamine) — for that, see Agilent Substrate Oxidation Stress Tests.
- Electron flow assay (rotenone + succinate). See Agilent Kit 103720-100 if needed.
- Isolated mitochondria. This SOP is intact-cell only.

---

## 2. Reagents, consumables, instruments — bill of materials

### 2.1 Cell culture and differentiation

| Item | Vendor | Catalog # | Qty / 96-well plate | Price (USD, est.) | Storage |
|---|---|---|---|---|---|
| C2C12 (mouse myoblast) | ATCC | CRL-1772 | 1 vial (≥1×10⁶ cells) | ~$520 | LN₂ |
| HSMM (human primary skeletal muscle myoblasts) | Lonza | CC-2580 | 1 donor vial (≥5×10⁵ cells) | ~$800 (lot-dependent) | LN₂ |
| SkGM-2 BulletKit (HSMM growth) | Lonza | CC-3245 | 1 kit (per 2–3 plates) | ~$700 | -20°C / 4°C |
| SkMDM (HSMM differentiation) | Lonza | CC-3245 + CC-4441 (insulin) | 250 mL | ~$350 | -20°C |
| DMEM, high glucose, GlutaMAX | Thermo / Gibco | 10566-016 | 500 mL | ~$30 | 4°C |
| FBS (USDA-tested, for C2C12 growth) | Thermo / Gibco | 10437-028 | 500 mL | ~$280 | -20°C |
| Horse serum, heat-inactivated (C2C12 DM) | Thermo / Gibco | 26050-088 | 500 mL | ~$370 | -20°C |
| Penicillin–streptomycin (10,000 U/mL) | Thermo / Gibco | 15140-122 | 100 mL | ~$15 | -20°C |
| PBS, pH 7.4 (Ca²⁺/Mg²⁺-free) | Thermo / Gibco | 10010-023 | 500 mL | ~$30 | RT |
| TrypLE Express (no phenol red) | Thermo | 12605010 | 100 mL | ~$30 | RT |
| Dimethyl sulfoxide (DMSO) | Sigma | D2650 | 100 mL | ~$40 | RT |
| Insulin (recombinant human, for HSMM DM) | Sigma | I9278 | 100 mg | ~$70 | 4°C |

### 2.2 Seahorse XF consumables

| Item | Vendor | Catalog # | Qty / 96-well plate | Price (USD, est.) | Storage |
|---|---|---|---|---|---|
| **Seahorse XFe96 FluxPak** (10 plates + 10 cartridges + calibrant) | Agilent | **102601-100** | 1 box (10 plates + 10 cartridges) | ~$2,300 | RT |
| **Seahorse XF Mito Stress Test Kit** (Oligo 1 µmol + FCCP 1 µmol + Rot/AA 1 µmol each) | Agilent | **103015-100** | 1 kit (≈6 plates) | ~$750 | -20°C |
| XF DMEM medium, pH 7.4 (no bicarbonate) | Agilent | **103575-100** | 50 mL · plate⁻¹ | ~$50 / 500 mL bottle | 4°C |
| XF 1 M glucose | Agilent | **103577-100** | 5 mL · plate⁻¹ | included w/ kit supplements | 4°C |
| XF 100 mM pyruvate | Agilent | **103578-100** | 5 mL · plate⁻¹ | included w/ kit supplements | 4°C |
| XF 200 mM L-glutamine | Agilent | **103579-100** | 5 mL · plate⁻¹ | included w/ kit supplements | 4°C |
| Hoechst 33342 DNA normalization kit (optional) | Agilent | **102701** | 1 kit (≥10 plates) | ~$120 | 4°C |
| Seahorse XFe96 Spare Cartridge (replacement) | Agilent | 102601-100 (sub) | 1 / run | (incl. w/ FluxPak) | RT |

For **24-well (XFe24)** runs:

| Item | Vendor | Catalog # | Notes |
|---|---|---|---|
| XFe24 FluxPak | Agilent | **102340-100** | Includes 24-well cell plates, 24-well cartridges, calibrant. Verify current at order. |
| XF Mito Stress Test Kit (24-well compatible) | Agilent | **103015-100** | Same kit, different port volumes (see §4.2). |

> **Catalog-number note.** Agilent periodically updates FluxPak kit numbers when bundling/contents change. Always confirm current catalog against the Agilent online store at order time. The numbers above are valid as of 2026-06 and are the canonical references used in the v0.2 plan.

### 2.3 Normalization reagents

| Item | Vendor | Catalog # | Qty / plate | Price (USD) | Storage |
|---|---|---|---|---|---|
| Pierce BCA Protein Assay Kit | Thermo | **23225** | 1 kit (≥20 plates) | ~$150 | RT |
| BSA protein standard, 2 mg/mL | Thermo | 23210 | 10 × 1 mL | ~$60 | -20°C |
| RIPA lysis buffer | Thermo | 89900 | 100 mL | ~$40 | 4°C |
| Protease / phosphatase inhibitor cocktail (100×) | Thermo | 78440 | 5 mL | ~$80 | 4°C |
| Hoechst 33342, 10 mg/mL stock | Thermo | H3570 | 10 mL | ~$85 | 4°C |
| Cell-Tak (Corning) for non-TC plate coating | Corning | **354240** | 1 mg | ~$200 | 4°C |
| Matrigel (Corning), LDEV-free, for myogenic plates | Corning | **354234** | 10 mL | ~$350 | -20°C |
| Paraformaldehyde, 4% (PFA, for CSA fixation) | Thermo | J19943-K2 | 100 mL | ~$25 | 4°C |

### 2.4 Instruments

| Instrument | Vendor / Model | Required accessories | Calibration cadence |
|---|---|---|---|
| Seahorse XFe96 Analyzer (or XFe24) | Agilent | 96-well cartridge holder; CO₂-free incubator | Vendor PM every 6 mo |
| Multi-mode plate reader (Hoechst + optional Hoechst pre-read) | Tecan Spark / BioTek Cytation 5 | Ex 350 / Em 461 filter or monochromator | Quarterly |
| Plate fluorometer for Hoechst QC (optional) | Molecular Devices SpectraMax | n/a | Annual |
| Tissue culture hood (BSL-2) | n/a | Class II Type A2 | Annual cert |
| Cell culture incubator, 37°C, 5% CO₂ | n/a | n/a | Quarterly |
| Inverted phase-contrast microscope (CSA imaging) | Olympus IX73 / Nikon Eclipse | 10× phase objective; calibrated reticle | Annual |
| Vortex, benchtop centrifuge, dry bath | n/a | n/a | n/a |
| ImageJ/Fiji (Fiji Is Just ImageJ) | open source | n/a | n/a |

### 2.5 Software

- **Wave** (Agilent) — v2.6 or later, instrument controller and assay template.
- **Agilent Report Generator** (bundled with Wave) — for plate map export.
- **R** ≥4.3.0 (`tidyverse`, `lme4`, `emmeans`, `multcomp`, `readxl`).
- **Python** ≥3.10 (`pandas`, `numpy`, `seaborn`, `pingouin`).
- **Fiji** (ImageJ2) for myotube diameter measurement (§6.4).

---

## 3. Plate preparation

### 3.1 Cell density optimization (mandatory pilot)

Before any experimental run, perform a **density pilot** for each cell model. Seed cells at a 6-point dose range:

| Density (cells/well, 96-well) | C2C12 | HSMM |
|---|---|---|
| 1,000 | ✅ test | ✅ test |
| 2,500 | ✅ test | ✅ test |
| 5,000 | ✅ test | ✅ test |
| 8,000 | ✅ test | ✅ test |
| 12,000 | ✅ test | ✅ test |
| 20,000 | ✅ test (only if low signal at 8K) | ✅ test |

**Acceptance criteria for density selection (basal OCR at d6 C2C12 / d9 HSMM):**

- **Basal OCR in 50–250 pmol O₂ · min⁻¹ · 10⁴ cells⁻¹** range (or 0.5–5 pmol · min⁻¹ · µg protein⁻¹ for C2C12).
- **O₂ partial pressure in well > 80 mmHg at start of measurement** (instrument reports this as "O₂ level"; if < 80, reduce density or reduce mix duty cycle).
- **Oligomycin response produces a clear drop (≥20% of basal).**

**Default starting density** (apply if no prior pilot exists):

- C2C12: **6,000 cells/well** (96-well), **20,000 cells/well** (24-well).
- HSMM: **10,000 cells/well** (96-well), **35,000 cells/well** (24-well).

Record the density used per experiment in the LIMS sample manifest.

### 3.2 Plate coating

**Option A — Cell-Tak** (preferred for non-TC-treated Seahorse plates; rare for fully differentiated myotubes since the plate is already pre-TC-treated):

1. Dilute Cell-Tak to **22.4 µg/mL** in **0.1 M NaHCO₃, pH 8.0**.
2. Add 25 µL/well (96-well) or 100 µL/well (24-well) to the Seahorse cell plate.
3. Incubate **30 min at RT** in hood.
4. Aspirate, wash 2× with sterile PBS.
5. Use plate within 2 hr or seal and store at 4°C for ≤24 hr.

**Option B — Matrigel** (preferred for HSMM and for 3D myobundle cross-protocols):

1. Thaw Matrigel on ice (slow, 4°C overnight, or in cold block).
2. Dilute to **1:100 in cold DMEM** (final ≈ 80–100 µg/mL protein).
3. Add 50 µL/well (96-well) and incubate **1 hr at 37°C** or **2 hr at RT**.
4. Aspirate coating solution; do **not** let wells dry.
5. Seed cells immediately.

> If wells dry after aspiration, re-coat — myotubes will not attach uniformly to a dried Matrigel film.

### 3.3 Seeding (Day 0)

1. Dissociate cells with TrypLE Express, 4 min at 37°C.
2. Resuspend in growth medium (C2C12: DMEM + 10% FBS + 1% P/S; HSMM: SkGM-2).
3. Count and adjust to seeding density (see §3.1).
4. Seed **100 µL/well** (96-well) or **500 µL/well** (24-well).
5. Allow cells to settle ≥4 hr in incubator before moving plate.
6. Change medium at 24 hr to remove dead cells and DMSO traces.

### 3.4 Differentiation

| Model | Day 0 | Day 1 | Day 2 | Day 3 | Day 4 | Day 5 | Day 6 | Day 7 | Day 8 | Day 9 | Day 10 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| C2C12 (mouse) | Seed (growth) | Growth | **DM** | DM | DM | **DM** | **DM (assay window)** | **DM (assay window)** | n/a | n/a | n/a |
| HSMM (human) | Seed (SkGM-2) | SkGM-2 | SkGM-2 | **SkMDM** | SkMDM | SkMDM | SkMDM | SkMDM | SkMDM | **SkMDM (assay window)** | **SkMDM (assay window)** |

Bold = assay-eligible day. **For C2C12, run assay on d5, d6, or d7 of DM. For HSMM, run on d7, d8, d9, or d10 of DM.** Outside this window, myotubes begin to contract and detach.

> **RNAi timing for the Mito Stress Test.** Transfect siRNA (e.g., CHCHD10, NDUFB4, ATP5F1B, PGC-1α, scrambled control) at the **start of differentiation (C2C12 d0 DM; HSMM d0 SkMDM)** using reverse transfection in Matrigel-coated plates. Validate knockdown by parallel qPCR and Western on sister wells at assay day. **If KD efficiency < 70% at mRNA, do not run the Seahorse assay** — the OCR effect will be below the detection limit. Reserve fresh siRNA aliquots at -20°C; avoid freeze-thaw.

### 3.5 Day-of-assay medium switch

**T = -60 min** (relative to instrument start):

1. Pre-warm XF DMEM, glucose, pyruvate, glutamine in a 37°C water bath.
2. Prepare **XF assay medium**: XF DMEM + **10 mM glucose** + **1 mM pyruvate** + **2 mM L-glutamine**, pH 7.4 (verify with a pH meter; do not adjust with HCl/NaOH unless drift > 0.1 pH).
3. Aspirate growth/differentiation medium from the cell plate.
4. **Wash once** with 200 µL/well (96-well) of assay medium to remove residual HEPES / bicarbonate from culture medium (HEPES carryover distorts ECAR).
5. Add **180 µL/well** (96-well) or **500 µL/well** (24-well) of fresh assay medium.
6. Place plate in a **37°C, CO₂-free incubator** for **45 min** before the run. This is the standard 30–60 min equilibration window; do not extend past 90 min (cells begin to drift).

> **Critical:** the 45 min equilibration must be in a **non-CO₂** environment (a standard CO₂ incubator will re-buffer the medium and the FCCP titration will be miscalibrated). If a CO₂-free incubator is unavailable, place the plate in the instrument's built-in 37°C / ambient-CO₂ chamber 60 min before the run.

### 3.6 Cartridge hydration (overnight, T = -12 to -18 hr)

1. Open XFe96 cartridge.
2. Add **200 µL/well** of XF calibrant (supplied with FluxPak) to the utility plate.
3. Lower the cartridge onto the utility plate.
4. Place in a **37°C, non-CO₂ incubator** overnight (≥12 hr, ≤18 hr).
5. If overnight is impossible, a 4-hr hydration is acceptable for screening but **never for confirmation runs.**

---

## 4. Drug port loading and FCCP titration

### 4.1 Master stock preparation (10× for ports)

The XF Mito Stress Test Kit (103015-100) provides lyophilized vials of Oligomycin, FCCP, and Rotenone + Antimycin A. Reconstitute per the kit insert:

| Compound | Solvent | Stock conc. | Storage after reconstitution |
|---|---|---|---|
| Oligomycin | DMSO (kit vial) | 100 µM | -20°C, ≤ 1 month |
| FCCP | DMSO (kit vial) | 100 µM | -20°C, ≤ 1 month (protect from light) |
| Rotenone | DMSO (kit vial) | 100 µM | -20°C, ≤ 1 month |
| Antimycin A | DMSO (kit vial) | 100 µM | -20°C, ≤ 1 month |

For working 10× stocks for the standard run, prepare in assay medium so that 1:10 dilution into the well yields the final target concentration.

| Port | 10× stock in assay medium (96-well prep) | Volume loaded in port | Final in well (180 µL well volume) |
|---|---|---|---|
| A — Oligo | 10 µM | 20 µL | 1 µM (final well concentration) |
| B — FCCP | 10 µM (or per titration) | 22 µL | 1 µM (default; override per §4.3) |
| C — Rot + AA | 10 µM + 10 µM | 25 µL | 1 µM each |

**Final well concentrations of 1 µM for all three compounds are the Agilent-default target for adherent cell lines, including C2C12 myotubes and HSMM.** If the cell line responds to a different optima, override with the FCCP titration result (§4.3). Do not change oligomycin or Rot/AA concentrations without explicit justification.

### 4.2 24-well port volumes

| Port | 10× stock | Volume loaded | Final in well (500 µL well volume) |
|---|---|---|---|
| A — Oligo | 10 µM | 56 µL | 1 µM |
| B — FCCP | 10 µM | 62 µL | 1 µM |
| C — Rot + AA | 10 µM + 10 µM | 69 µL | 1 µM each |

### 4.3 FCCP titration (mandatory; do not skip)

> **Failure mode warning.** A single-point 1 µM FCCP injection frequently **underestimates** maximal OCR, because the optimum varies by cell type, density, mitochondrial content, and FCCP lot. The first 5 publications you read will report a different "optimal" FCCP concentration. **You must titrate on your cells in your lab, with your lot, with your density, before any experimental run.** This is not optional.

#### 4.3.1 Plate setup for FCCP titration

Use a **dedicated titration plate** (not an experimental plate). Layout: 8 columns × 6 FCCP concentrations × ≥ 6 wells per concentration.

| Column | FCCP final in well |
|---|---|
| 1 | 0 (vehicle) — basal reference |
| 2 | 0.125 µM |
| 3 | 0.25 µM |
| 4 | 0.5 µM |
| 5 | 1.0 µM |
| 6 | 2.0 µM |
| 7 | 4.0 µM |
| 8 | baseline repeat (vehicle) |

1. Seed C2C12 (or HSMM) at the chosen experimental density.
2. Differentiate normally to the assay day (d5–7 C2C12; d7–10 HSMM).
3. Medium switch as in §3.5.
4. **Skip Port A and Port C.** Load only Port B with the titration series. Inject each concentration on **independent wells** (the instrument cannot dose-response through a single well; each well gets one FCCP concentration).
5. Run 3 cycles of mix/wait/measure post-FCCP.
6. Plot OCR vs. FCCP concentration.

#### 4.3.2 Selecting the optimum

- **Optimal FCCP = lowest concentration that gives the highest mean OCR.**
- A **bell-shaped** curve is normal: at high FCCP the inner membrane becomes too leaky and respiration collapses.
- **Reject any titration where 4.0 µM is still increasing** (suggests FCCP stock is degraded or density is too high) — re-run with fresh FCCP or lower density.
- For C2C12 myotubes at 6,000 cells/well: typical optimum is **1.0–2.0 µM**.
- For HSMM at 10,000 cells/well: typical optimum is **1.0–2.0 µM**.
- Record the chosen FCCP concentration in the LIMS and update the Wave assay template.

#### 4.3.3 Re-titration triggers

Re-run the FCCP titration if any of the following change:

- New cell line / new donor lot
- New FCCP kit lot
- New cell density (>2× change)
- New cell culture substrate (TC plate brand change)
- New lot of Matrigel or Cell-Tak

---

## 5. Assay protocol — Wave software settings

### 5.1 Protocol template

Apply the following protocol in Wave for each plate. Total run time ≈ 100 min (calibration + equilibration adds ~25 min before the first measurement).

| Step | Port | Cycles | Mix (min) | Wait (min) | Measure (min) |
|---|---|---|---|---|---|
| **Baseline (basal)** | n/a | 3 | 3 | 2 | 3 |
| Inject Port A (Oligo 1 µM final) | A | 3 | 3 | 2 | 3 |
| Inject Port B (FCCP @ titration optimum) | B | 3 | 3 | 2 | 3 |
| Inject Port C (Rot 1 µM + AA 1 µM) | C | 3 | 3 | 2 | 3 |

This gives **12 measurement points** per well (3 per step × 4 steps).

### 5.2 Wave group definitions

For an RNAi experiment with CHCHD10, NDUFB4, ATP5F1B, PGC-1α knockdown, set up these groups:

| Group | Wells (96-well) | Notes |
|---|---|---|
| **Background (cell-free)** | 4 wells (corners A1, A12, H1, H12) | Coat, treat identically, but seed with medium only. Used for non-cell-derived O₂ consumption. |
| **Scrambled siRNA (negative control)** | 12 wells | Spread across plate to control for edge effects. |
| **siRNA CHCHD10** | 10 wells | |
| **siRNA NDUFB4** | 10 wells | |
| **siRNA ATP5F1B** | 10 wells | |
| **siRNA PGC-1α (positive control for OXPHOS defect)** | 10 wells | |
| **Positive control: FCCP max (1 µM) on scrambled wells** | 6 wells | Reserved within scrambled; used to verify FCCP response on every plate. |
| **Positive control: Rot/AA min (1 µM each) on scrambled wells** | 6 wells | Reserved within scrambled; used to verify non-mito floor on every plate. |

> **Edge-effect note.** Seahorse XFe96 wells on column 1 and column 12 are most prone to evaporation and temperature drift. **Do not place critical samples there.** Reserve columns 1 and 12 for background wells.

### 5.3 Wave measurement parameters

| Setting | Value | Notes |
|---|---|---|
| Temperature | **37°C** (assay) | Calibrant hydration also at 37°C. |
| O₂ range | **ambient** (default) | If using "Seahorse XF Plasma Membrane Permeabilizer" override — not used in this SOP. |
| Mix | 3 min, default speed (6–8 of 10) | No bubbles — visually inspect port injection. |
| Wait | 2 min | Lets the medium re-equilibrate after mix. |
| Measure | 3 min | Default 3 min for XFe96. |
| Total cycles / step | 3 | Yields stable mean per step. |
| Data averaging | mean of 3 cycles per step | Outlier cycles flag in §7. |

### 5.4 Pre-run quality checks

Before pressing **Start**:

- [ ] Cartridge ports loaded with correct volume (20 / 22 / 25 µL for 96-well).
- [ ] No air bubbles in cartridge ports (tap cartridge on bench to settle; use a pipette to dislodge).
- [ ] Cell plate medium pH 7.4 ± 0.1 (pH strip on aspirated supernatant).
- [ ] Cell plate pre-equilibrated 45 min in non-CO₂ incubator.
- [ ] Plate map uploaded to Wave and group definitions correct.
- [ ] LIMS sample manifest updated with plate ID, cell model, donor/differentiation ID, and siRNA treatment.

### 5.5 During the run

- Watch the first basal cycle on the Wave live display. If a well's OCR is **negative** or **> 1000 pmol/min**, pause, inspect for bubbles, and re-fill that well with fresh assay medium if needed.
- If the instrument logs an error (e.g., temperature, O₂ drift), abort and re-start with a fresh cartridge.

### 5.6 Run completion

1. Wave auto-saves data to `C:\Agilent\Wave\…\<filename>.xlsx` (or Mac equivalent). Backup immediately to the LIMS or a network share — do not trust a local drive.
2. Remove cartridge, rinse with ddH₂O, dry, archive.
3. **Do not discard the cell plate.** Proceed directly to normalization (§6).

---

## 6. Normalization — protein, DNA, and CSA-matched myotube

### 6.1 Primary: BCA protein

#### 6.1.1 Lysis

**RIPA + 1× protease/phosphatase inhibitor cocktail** (cold).

1. Aspirate assay medium from the cell plate.
2. Add **50 µL/well (96-well)** of cold RIPA + inhibitors.
3. Pipette up-and-down 5× and scrape the well with a P200 tip.
4. Transfer lysate to a fresh 96-well V-bottom plate.
5. Incubate **15 min on ice**.
6. Centrifuge **10 min at 14,000 × g, 4°C**.
7. Supernatant → BCA. Store at -80°C if not running BCA same day.

#### 6.1.2 BCA assay

Per Pierce BCA Kit 23225 (microplate protocol):

| Step | Detail |
|---|---|
| Standard curve | 9 points, 0–2000 µg/mL BSA, in RIPA buffer. |
| Sample | 25 µL lysate + 200 µL working reagent (A:B = 50:1). |
| Blank | 25 µL RIPA + 200 µL working reagent. |
| Incubate | **30 min at 37°C**. |
| Read | **562 nm**, plate reader. |
| Acceptance | Standard curve R² > 0.99. |
| Report | µg protein / well. |

**Normalize OCR:** pmol O₂ · min⁻¹ · well⁻¹ ÷ µg protein · well⁻¹ = **pmol O₂ · min⁻¹ · µg protein⁻¹**.

### 6.2 Secondary: Hoechst DNA

1. Add **10 µL/well (96-well)** of 10 µg/mL Hoechst 33342 in PBS to each well (final 1 µg/mL).
2. Incubate **30 min at 37°C, 5% CO₂** (with CO₂ this time — plate is being terminated).
3. Read fluorescence: **Ex 350 nm, Em 461 nm**.
4. Generate a **standard curve** per plate by seeding a parallel set of wells with known cell numbers (e.g., 0; 2,500; 5,000; 10,000; 20,000; 40,000) and Hoechst-treating identically.
5. Convert RFU to cell number.
6. Report OCR · 10⁴ cells⁻¹.

> **Note.** Hoechst and BCA together in the same well is not possible. If both are needed, run a parallel set of sister wells (e.g., seed 110 wells for 100 assay wells to get both measurements on matched wells). For RNAi screens, **BCA is sufficient** unless ECAR/calcium data is also being interpreted.

### 6.3 Cross-check: protein vs. DNA

After OCR normalization:

- For each well, compute **µg protein / 10⁴ cells** (a proxy for protein content per cell).
- **Flag** any well where this ratio deviates > 2× from the plate median. This catches:
  - Cell clumping (high protein/cell)
  - Cell death / detachment between seeding and assay (low protein/cell)

### 6.4 CSA-matched myotube normalization

The HMSR Aim 2 plan requires that the OCR differences between genotypes be interpretable as **bioenergetic** differences, not as **myotube size** differences. A knockdown (or compound) that causes myotube atrophy will spuriously raise OCR · µg protein⁻¹ (because there's less contractile apparatus per mitochondrion), and will also reduce the "force at matched CSA" interpretation. We therefore **measure myotube diameter in the same well** that was used for OCR.

#### 6.4.1 Fixation

1. After BCA/Hoechst lysate removal, add **100 µL/well of 4% PFA** to the cell plate.
2. Incubate **15 min at RT**.
3. Wash 3× with PBS.
4. Store sealed at **4°C, light-protected, ≤ 2 weeks** before imaging.

#### 6.4.2 Imaging

1. Acquire **5–10 random fields per well at 10× phase**, automated stage.
2. Save as `.tif` with the LIMS plate ID encoded in the filename.

#### 6.4.3 Diameter measurement (Fiji / ImageJ)

1. Open a representative field.
2. Set scale: µm/pixel based on objective calibration.
3. For each well, measure **≥ 30 myotubes**:
   - Draw a line perpendicular to the long axis, mid-tube.
   - Measure the Feret diameter (line tool → Measure → ` Feret`).
4. Compute **mean diameter per well ± SD**.

#### 6.4.4 CSA-matched flagging

- Compute the **plate-wide mean diameter** of the scrambled (control) group.
- **Flag** any well (any genotype) where mean diameter differs from the control mean by **>15%**.
  - **If >15% smaller:** the OCR · µg protein⁻¹ result for that well is reported but is **excluded** from the "matched-CSA" comparison; report alongside a footnote.
  - **If >15% larger:** same action; suggests hyperfusion / swelling artefact.
- These flagged wells are **not** silently dropped — they are reported in the supplementary table with the flag and a reason.

#### 6.4.5 Link to myobundle specific force

For the Aim 2 plan, every Seahorse genotype must be paired with a sister myobundle preparation (3D fibrin-Matrigel construct) run on the same differentiation. Force · CSA⁻¹ from the parallel `myobundle_specific_force_SOP.md` provides the gold-standard matched-CSA comparator. Cross-reference the two files at analysis time.

### 6.5 Other CSA proxies (acceptable alternatives)

If high-content imaging is unavailable, fallback CSA proxies include:

- **Myosin heavy chain (MyHC) ELISA on lysate** (R&D Systems, e.g., MAB4470 for capture / BAF4470 for detection; or Thermo MYH1E-MA1-25909).
- **Total protein per myotube nucleus** (low-coverage proxy).

### 6.6 Sample metadata to record (LIMS)

| Field | Example |
|---|---|
| Plate ID | HMSR-SH-2026-06-13-A |
| Cell model | C2C12 (ATCC CRL-1772), p8 |
| Donor / differentiation | C2C12 d6 DM, replicate 3 |
| Seeding density | 6,000 cells/well (96-well) |
| Coating | Matrigel 1:100 |
| siRNA | siRNA CHCHD10 (Dharmacon L-051518-01-0005, lot X) |
| Transfection reagent | Lipofectamine RNAiMAX, 0.3 µL/well |
| KD efficiency (qPCR, parallel well) | 87% mRNA knockdown |
| FCCP concentration used | 1.5 µM (per titration) |
| Medium batch | XF DMEM lot Y |
| Operator | JS |
| Instrument | XFe96, S/N Z |
| Run date / time | 2026-06-13 14:30 |
| Notes | baseline drift in row 7 — flagged |

---

## 7. QC gates and acceptance criteria

### 7.1 Plate-level gates

A plate **passes** only if all of the following hold:

| Gate | Criterion | Action if fail |
|---|---|---|
| Background wells (cell-free) | OCR < 5 pmol · min⁻¹ in baseline cycles | Re-run; check coating artifacts. |
| Scrambled basal OCR | Within 50–250 pmol · min⁻¹ · 10⁴ cells⁻¹ (cell-type-dependent; track over time) | Re-run; check density, media, lot. |
| FCCP response | ≥ 1.5× scrambled basal, peaks at expected concentration | Re-titrate FCCP; verify lot. |
| Rot/AA response | < 10% of scrambled basal | If not, retest Rot/AA stocks (they can degrade). |
| pH of assay medium | 7.4 ± 0.1 | Adjust with 1 N NaOH / HCl; do not rely on "default". |
| O₂ in well at start of basal | > 80 mmHg (instrument logs this) | Reduce density; wells were oxygen-depleted. |
| Plate-edge baseline drift | < 15% CV across plate | Re-run with humidified chamber. |
| KD efficiency (sister well) | ≥ 70% mRNA KD | Do not interpret OCR data; re-transfect. |

### 7.2 Well-level gates

A well **passes** only if:

| Gate | Criterion | Action if fail |
|---|---|---|
| Basal OCR | < 3 SD from plate mean (per genotype group) | Exclude from analysis, flag in supp. |
| Oligo response | ≥ 20% drop from basal | Re-inspect; may indicate dead/dying well. |
| FCCP response | ≥ 1.2× basal (for live cells) | Re-inspect; non-mito may dominate. |
| Technical CV (triplicate) | < 15% per genotype per plate | Re-run with fresh transfections. |
| Myotube diameter | within ± 15% of scrambled mean (or flagged) | Flag and report separately (§6.4.4). |
| Cell detachment / morphology | Confluent monolayer / fused myotubes | Exclude (cell quality event). |

### 7.3 Biological replicate gates

A genotype effect is **reportable** only if:

- ≥ 3 independent differentiations (C2C12) or ≥ 3 donors (HSMM).
- Sign of effect (KD vs scrambled) **consistent** across all 3 replicates.
- **Magnitude** of effect (Cohen's d) within **2× of the median** across replicates (otherwise flag as high-variance donor / differentiation).
- Mixed-model ANOVA F-test for genotype effect: p < 0.05 (uncorrected, with Tukey HSD post-hoc, BH-FDR < 0.1 for the 5–6 endpoints).

### 7.4 Out-of-spec run (master reset)

If a plate fails ≥ 2 plate-level gates, treat the run as failed. Re-run from a new vial / new differentiation. **Do not patch a failed run with reanalysis.**

---

## 8. Data analysis pipeline

### 8.1 Data extraction (Wave → Excel)

1. In Wave, go to **Export → Data** for each plate. Save `.xlsx` to the LIMS analysis folder.
2. Confirm the plate map (group × well) is preserved in the export.
3. The export contains one row per well per cycle, with columns: `Well`, `Group`, `Time`, `OCR (pmol/min)`, `ECAR (mpH/min)`, `Cycle`, `Step`.

### 8.2 Computation of mitochondrial parameters

Using the formulas below. Implement in a **single committed R or Python script** (e.g., `analysis/seahorse_compute_params.R` in the LIMS). Re-run on every batch; do not paste values into spreadsheets by hand.

Let:
- `B` = mean OCR of the 3 baseline cycles (Rot/AA-subtracted)
- `O` = mean OCR of the 3 post-Oligo cycles (Rot/AA-subtracted)
- `F` = mean OCR of the 3 post-FCCP cycles (Rot/AA-subtracted) — or use the **peak** cycle (max) if FCCP-induced OCR spikes transiently
- `R` = mean OCR of the 3 post-Rot/AA cycles (non-mito floor)

Then:

| Parameter | Formula |
|---|---|
| Non-mito OCR | `R` |
| Basal OCR | `B - R` (or `B` if already non-mito-subtracted in Wave) |
| ATP-linked OCR | `B - O` |
| Maximal OCR | `F` |
| Spare respiratory capacity | `F - B` |
| Coupling efficiency | `(B - O) / B` |
| Proton leak (residual) | `O - R` |

> **Sign convention.** All values should be ≥ 0 in a healthy preparation. If a calculated parameter is negative, it indicates a problem (incorrect Rot/AA subtraction, sample mix-up, or genuine cell death). Investigate before reporting.

### 8.3 Statistical analysis

- **Model:** linear mixed model (`lme4::lmer` in R or `statsmodels.formula.api.mixedlm` in Python).
  - Fixed effect: **genotype** (scrambled, CHCHD10, NDUFB4, ATP5F1B, PGC-1α).
  - Random effect: **differentiation / donor ID** (random intercept).
  - Response: each OCR parameter (basal, ATP-linked, maximal, spare, coupling).
  - Cycle-level: response is the **mean of the 3 cycles per step** per well.
- **Post-hoc:** Tukey HSD on genotype pairwise contrasts (`emmeans` in R, `pingouin` in Python).
- **Multiple endpoint correction:** BH-FDR (5 endpoints per genotype comparison).
- **Effect size:** Cohen's d (per pairwise contrast).
- **Significance:** BH-FDR < 0.1 (≥ 90% confidence) is the reportable threshold. P < 0.05 is informational.

### 8.4 Plotting

Mandatory figures per replicate / donor / genotype:

1. **Kinetic traces.** OCR vs. time per well, colored by genotype. Include all wells, with mean line per group. Annotate Port A / B / C injection times.
2. **Bar plot of mitochondrial parameters.** Per genotype: basal, ATP-linked, maximal, spare. Bar = mean ± SE; overlay individual data points (one per well). Color by genotype.
3. **CSA overlay.** Same x-axis as bar plot, secondary y-axis: mean myotube diameter per well. Use this to visually flag diameter-confounded results.
4. **Representative myotube images** (CSA matched): per genotype, 1 representative 10× phase field with mean diameter within ±5% of group median.

### 8.5 Output files

| File | Format | Required |
|---|---|---|
| Per-plate raw data | `.xlsx` from Wave | ✅ |
| `seahorse_normalized.csv` | per-well OCR parameters + protein + DNA + diameter | ✅ |
| `seahorse_summary_stats.csv` | per-genotype per-donor mean ± SE for each parameter | ✅ |
| `seahorse_model_results.csv` | mixed-model coefficients, p, FDR, Cohen's d per contrast | ✅ |
| `figures/kinetics_*.pdf` | per plate | ✅ |
| `figures/parameters_*.pdf` | per donor / differentiation / pooled | ✅ |
| `qc_report.md` | gates passed/failed, exclusions | ✅ |
| `run_manifest.yaml` | plate ID, lot numbers, operator, date, all input files with SHA-256 | ✅ |

### 8.6 Code review and reproducibility

All R/Python scripts in the analysis pipeline are version-controlled in the LIMS. Each commit is **the** analysis — no manual paste. The script takes one CLI argument: the LIMS analysis folder for one plate, and emits all the output files above. A reviewer must be able to run the same script on the same input and get bit-identical output.

---

## 9. Common pitfalls

A ranked list of the failures that have most commonly compromised in-vitro Seahorse runs in our hands. Each item links to the section that addresses it.

| # | Pitfall | Symptom | Fix / Section |
|---|---|---|---|
| 1 | **FCCP titration skipped** | Maximal OCR reported is too low; spare capacity compressed. | §4.3 — mandatory titration. |
| 2 | **Cell density too high** | O₂ in well drops below 80 mmHg mid-run; kinetics become non-linear; FCCP looks higher than it is. | §3.1 — density pilot required. |
| 3 | **Cell density too low** | Noisy baseline; high CV across replicates; Rot/AA subtraction eats the signal. | §3.1 — same pilot. |
| 4 | **Plate not pre-equilibrated in non-CO₂ incubator** | Baseline drift; first cycles trending downward; OCR appears to be falling even before Oligo. | §3.5 — 45 min in CO₂-free. |
| 5 | **Myotube detachment during medium switch** | Variable cell numbers per well; high CV; out-of-spec basal. | §3.2 — Matrigel or Cell-Tak coat; aspirate gently. |
| 6 | **HEPES / bicarbonate carryover from culture medium** | Distorted ECAR; sometimes variable OCR baseline. | §3.5 — wash once with assay medium. |
| 7 | **KD not validated before assay** | OCR unchanged despite "successful" siRNA; data non-informative. | §3.4 + §7 — qPCR + WB on sister wells. |
| 8 | **FCCP kit lot not re-titrated** | Maximal OCR off by 30–50% between experiments. | §4.3.3 — re-titration triggers. |
| 9 | **Plate-edge effects** (columns 1, 12) | Higher CV; wells in those columns deviate from interior wells. | §5.2 — reserve columns 1/12 for background. |
| 10 | **Rot/AA not mixing well before addition** | Non-mito floor higher than expected; spare capacity underestimated. | Tap cartridge on bench before injection. |
| 11 | **Sodium bicarbonate in "XF DMEM" misread** | Some lots have it; verify on the bottle. Use **XF DMEM 103575-100** (bicarb-free) only. | §2.2. |
| 12 | **OCR unit conversion error** | Reporting pmol/min instead of pmol/min/well normalized. | §8.5 — report both pmol/min/µg protein and /10⁴ cells. |
| 13 | **Wave "Background correction" mis-set** | Background subtracted twice or not at all. | §5.2 — cell-free wells in columns 1/12. |
| 14 | **Reanalysis after the fact** | Re-derived numbers don't match archived Excel. | §8.6 — script-driven, deterministic. |
| 15 | **Single-donor HSMM "validation"** | n=1 cannot validate; not a biological replicate. | §7.3 — ≥ 3 donors. |

---

## 10. References

> PMIDs cited below are checked against the v0.2 plan and the most-cited Seahorse methodology literature. Verify current DOIs at the time of writing any manuscript section that uses this SOP.

1. **Agilent Seahorse XF Mito Stress Test Kit User Guide** (kit insert, current version). Agilent Technologies, Santa Clara, CA. Kit 103015-100.
2. **Agilent Application Note: "Mitochondrial respiration in C2C12 myotubes"** (current version). Search the Agilent Literature Library with query `C2C12 myotube Mito Stress Test`.
3. **Agilent Seahorse XF Prep Station and Instrument User Guide** (current version).
4. Divakaruni AS, Wiley SE, Rogers GW, et al. (2014). Analysis of FCCP-mediated mitochondrial uncoupling and electron transport chain in vitro. *Method Enzymol.* (PMID **24828385** — verify at time of writing).
5. Brand MD, Nicholls DG (2011). Assessing mitochondrial dysfunction in cells. *Biochem J* 435(2): 297–312. (PMID **21433285**.)
6. Mookerjee SA, Gerencser AA, Nicholls DG, Brand MD (2020). Interpreting in vitro OCR data: from mechanism to diagnosis. (PMID **33127978** — verify at time of writing.)
7. An Y, et al. (2023). A Seahorse-based protocol for assessing C2C12 myotube mitochondrial function. (Verify citation at time of writing; preprint or published version per the v0.2 plan literature set.)
8. **C2C12 differentiation & contractile apparatus baseline.** Blau HM, Pavlath GK, Hardeman EC, Chiu CP, Silberstein L, Webster SG, Miller SC, Webster C (1985). Plasticity of the differentiated state. *Science* 230(4727): 758–766. (PMID **3861843**.)
9. **HSMM donor and differentiation baseline.** Bonavaud S, Agbulut O, Nizard R, D'Hont G, Mouly V, Butler-Browne G (2001). A confocal and electron microscopy study of the human skeletal muscle cell in culture. (Verify in v0.2 plan literature set.)
10. **MyHC and CSA imaging standard.** ImageJ documentation: https://imagej.net/ (current version).

> **Verification step (required before any manuscript use of this SOP).** Run a PubMed search with the exact PMID + "Seahorse" + "myotube" + current year. If the PMID does not resolve to a paper with that title/abstract, update the citation. Treat any unresolved reference as a placeholder.

---

## 11. Day-of-Run Checklist (printable)

Print this page and complete each row. The plate ID, operator, and time stamps are **the** record of the run.

### 11.1 Pre-run (T = -12 to -18 hr)

- [ ] Date: __________
- [ ] Operator: __________
- [ ] Plate ID: __________ (LIMS)
- [ ] Cell model: ☐ C2C12 (d__ DM) ☐ HSMM (d__ SkMDM, donor ID __________)
- [ ] Differentiation replicate: __ of __ (≥3 required)
- [ ] Cell density used: _______ cells/well (96-well) or _______ (24-well)
- [ ] Coating: ☐ Matrigel 1:100 ☐ Cell-Tak 22.4 µg/mL ☐ TC plate only
- [ ] siRNA / treatment / control layout: ☐ uploaded to Wave ☐ recorded in LIMS
- [ ] KD efficiency on sister well (mRNA): ____% (≥70% required)
- [ ] KD efficiency on sister well (protein, optional): ____%
- [ ] FCCP titration completed? ☐ yes (this cell line + density + lot, ≤30 days ago) ☐ N/A (re-titrate)
- [ ] Optimal FCCP from titration: _______ µM
- [ ] Seahorse XFe96 cartridge hydrated: 200 µL/well XF calibrant, 37°C, non-CO₂, ≥12 hr
- [ ] XF DMEM, glucose, pyruvate, glutamine warmed to 37°C
- [ ] XF assay medium prepared (DMEM + 10 mM glucose + 1 mM pyruvate + 2 mM L-glut), pH 7.4 ± 0.1

### 11.2 Port loading (T = -30 min)

- [ ] Oligomycin working stock: 10 µM in assay medium, 20 µL loaded in Port A (96-well) or 56 µL (24-well)
- [ ] FCCP working stock: 10 µM in assay medium (or per titration), 22 µL in Port B (96-well) or 62 µL (24-well)
- [ ] Rot/AA working stock: 10 µM + 10 µM in assay medium, 25 µL in Port C (96-well) or 69 µL (24-well)
- [ ] No air bubbles in any port (tapped, pipetted to settle)
- [ ] Cartridge visually inspected: each port has the correct volume

### 11.3 Plate prep (T = -60 min)

- [ ] Cell plate aspirated of growth/differentiation medium
- [ ] Washed 1× with 200 µL/well assay medium (96-well) — HEPES removed
- [ ] Fresh assay medium added: 180 µL/well (96-well) or 500 µL/well (24-well)
- [ ] Plate transferred to 37°C, non-CO₂ incubator; 45-min timer started
- [ ] Cell plate pH check: 7.4 ± 0.1 (pH strip on aspirated well)

### 11.4 Pre-start (T = 0)

- [ ] Plate map uploaded to Wave
- [ ] Group definitions: scrambled, CHCHD10, NDUFB4, ATP5F1B, PGC-1α, FCCP max, Rot/AA min, background (cell-free)
- [ ] FCCP concentration in template matches the titration result
- [ ] All four steps configured: 3 cycles × (mix 3 + wait 2 + measure 3) min
- [ ] Temperature 37°C
- [ ] Background wells in columns 1 and 12 (corners preferred: A1, A12, H1, H12)
- [ ] Run started

### 11.5 Post-run (T = +100 min)

- [ ] Wave data exported to `.xlsx`, saved to LIMS with plate ID
- [ ] Cell plate removed; treated as a PFA-pending sample, not discarded
- [ ] Cartridge rinsed with ddH₂O, dried, archived
- [ ] Lysis for BCA: 50 µL/well cold RIPA + 1× inhibitors, 15 min on ice, -80°C if not run same day
- [ ] Hoechst DNA (if running secondary): 10 µL/well of 10 µg/mL, 30 min at 37°C + 5% CO₂
- [ ] PFA fixation: 100 µL/well 4% PFA, 15 min RT, then PBS, 4°C store
- [ ] Run-end time: __________
- [ ] Any anomalies noted in LIMS (bubble in well X, slow inject, edge drift in row Y): __________

### 11.6 QC sign-off (within 24 hr of run)

- [ ] Background wells OCR < 5 pmol/min? ☐ yes ☐ no (action: __________)
- [ ] Scrambled basal in 50–250 pmol/min/10⁴ cells? ☐ yes ☐ no
- [ ] FCCP peak ≥ 1.5× basal? ☐ yes ☐ no
- [ ] Rot/AA < 10% basal? ☐ yes ☐ no
- [ ] O₂ in well > 80 mmHg at basal? ☐ yes ☐ no
- [ ] Edge-drift < 15% CV? ☐ yes ☐ no
- [ ] BCA standard curve R² > 0.99? ☐ yes ☐ no
- [ ] All myotube diameter measurements completed (≥ 30 per well)? ☐ yes ☐ no
- [ ] Any well flagged for diameter > ±15% from scrambled mean? ☐ no ☐ yes — list: __________
- [ ] QC report saved as `qc_report_<plate_ID>.md` in LIMS

### 11.7 Pass / fail decision

- [ ] **PASS** — all plate-level and well-level gates met. Proceed to analysis pipeline (§8).
- [ ] **FAIL** — re-run with new plate / new differentiation. Record failure reason in LIMS. Do not report.

### 11.8 Sign-off

- Operator signature: __________ Date: __________
- PI or co-PI signature: __________ Date: __________ (required for any FAIL→PIPELINE, or for any Flagged-Well inclusion in the main report)

---

## Appendix A — Quick reference: C2C12 vs HSMM parameter table

| Parameter | C2C12 (d6) | HSMM (d9) |
|---|---|---|
| Seed density (96-well) | 6,000 | 10,000 |
| Differentiation start | day 0 (DM at 80–90% confluence) | day 3 of culture (SkMDM at 90% confluence) |
| Assay window (DM days) | 5–7 | 7–10 |
| Coating preferred | Matrigel 1:100 | Matrigel 1:100 |
| Typical basal OCR (pmol/min/10⁴ cells) | 100–200 | 60–150 (donor-variable) |
| Typical FCCP optimum | 1.0–2.0 µM | 1.0–2.0 µM |
| KD reagent (siRNA) | Lipofectamine RNAiMAX 0.3 µL/well | Lipofectamine RNAiMAX 0.3 µL/well |
| KD validation (qPCR primers, mRNA) | Assay ID ________________ | Assay ID ________________ |
| Notes | P0-P12 max; passage >P12 = use fresh vial | Donor age, sex, biopsy site recorded |

## Appendix B — 24-well conversion table (XFe24)

| Item | 96-well | 24-well |
|---|---|---|
| Cell plate well area | 0.32 cm² | 0.95 cm² |
| Medium switch volume | 180 µL | 500 µL |
| Port A volume (Oligo) | 20 µL | 56 µL |
| Port B volume (FCCP) | 22 µL | 62 µL |
| Port C volume (Rot/AA) | 25 µL | 69 µL |
| Cartridge hydration volume | 200 µL/well | 1 mL/well |
| RIPA for lysis | 50 µL/well | 150 µL/well |
| Background wells (recommended) | 4 corners | 4 corners |
| Group definition upload | Wave template `XFe96_Mito_Stress_v2.6` | Wave template `XFe24_Mito_Stress_v2.6` |

## Appendix C — Cross-references

- Pair protocol: `myobundle_specific_force_SOP.md` (3D myobundle contractile read-out, same worktree).
- Gene panel: `../aim2_gene_panel.md` (CHCHD10, NDUFB4, ATP5F1B, PGC-1α, scrambled control).
- Analysis pipeline: `analysis/seahorse_compute_params.R` (or `.py`) in LIMS.
- LIMS sample manifest: `lims/aim2/manifest_<plate_ID>.csv`.
- v0.2 plan reference: `../../../plan/hmsr_v0_2_experimental_validation_plan.md` (this worktree, in the parent module's `plan/` directory).
