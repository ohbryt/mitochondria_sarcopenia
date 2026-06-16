# SOP — Specific Force at Matched CSA in C2C12 and HSMM Myobundles (HMSR Aim 2 Quality Readout)

> **Document ID:** `MYOBUNDLE_SPECIFIC_FORCE_SOP.md`
> **Version:** 0.1 (initial issue; Aim 2 v0.2-aligned)
> **Branch:** `validation/aim2-causation`
> **Worktree:** `.worktrees/validation-aim2/`
> **Owner:** HMSR Aim 2 working group (in-vitro causation arm)
> **Pair with:** `protocols/SEAHORSE_MITO_STRESS_TEST_SOP.md` (respiration endpoint)
> **Source plan:** `manuscripts/experimental_validation_plan_v0.2.md` (Aim 2)
> **CRO-executable:** yes — designed for handoff to a muscle-physiology CRO (Muscle Forum Labs, ProCytech, Charité Berlin muscle physiology core) with on-site vendor verification of all catalog numbers before quote.

---

## Table of contents

1. [Scope and rationale](#1-scope-and-rationale)
2. [2D single-myotube force (Aurora Scientific 1300A / IonOptix MyoCam)](#2-2d-single-myotube-force-aurora-scientific-1300a--ionoptix-myocam)
3. [3D engineered myobundle (fibrin / Matrigel hydrogel)](#3-3d-engineered-myobundle-fibrin--matrigel-hydrogel)
4. [Matched-CSA design (the critical Aim 2 endpoint)](#4-matched-csa-design-the-critical-aim-2-endpoint)
5. [Pre-registered analysis plan](#5-pre-registered-analysis-plan)
6. [QC gates and acceptance criteria](#6-qc-gates-and-acceptance-criteria)
7. [Common pitfalls](#7-common-pitfalls)
8. [Cross-reference to in-vivo single-fibre force (Exp A / B)](#8-cross-reference-to-in-vivo-single-fibre-force-exp-a--b)
9. [Cost & timeline](#9-cost--timeline)
10. [References](#10-references)
11. [Day-of-Experiment Checklist](#11-day-of-experiment-checklist)

---

## 1. Scope and rationale

### 1.1 What is specific force?

**Specific force (sF)** = peak tetanic force ÷ muscle cross-sectional area (CSA).
Units are typically reported as **kN/m²** or equivalently **mN/mm²** (1 kN/m² = 1 mN/mm²).

$$\mathrm{sF}\;\;[\mathrm{kN/m^2}] = \frac{F_\text{tetanus}\;[\mathrm{mN}]}{\mathrm{CSA}\;[\mathrm{mm^2}]}$$

CSA for a single myotube is computed assuming a circular cross-section:

$$\mathrm{CSA} = \pi \times (d/2)^2 \;\;[d\;\text{in mm}]$$

For a 3D myobundle, the same formula is used with the bundle's mean outer diameter at the point of force measurement (most labs assume circular; some use histology cross-section — see §3.5).

### 1.2 Why this is the primary Aim 2 endpoint

**The scientific problem.** Sarcopenia is currently dominated by "**mass** drugs" — myostatin antagonists, testosterone, growth hormone — and they have under-delivered. The companion muscle-quality Perspective (HMSR) argues this is because **mass without quality is not function**. The HMSR discovery (v0.4) shows the entire nuclear-encoded mitochondrial biogenesis programme is coordinately down-regulated in sarcopenic muscle. The next question is: **does that down-regulation cause loss of *quality* (force at preserved size), or just loss of *quantity* (mass)?** That is the Aim 2 v0.2 decisive contrast:

> *"A knockdown that reduces OCR / specific force at matched myotube diameter supports H1; if force only falls in proportion to diameter loss, the gene acts via mass, not quality."* — `experimental_validation_plan_v0.2.md:76`

This is why **specific force at matched CSA is the primary quality readout** of Aim 2, and why every analysis (§4) is designed around the matched-CSA contrast, not around raw force or raw CSA.

### 1.3 Cell models and their role

| Model | Role in Aim 2 | Strength | Limitation |
|---|---|---|---|
| **C2C12 myotubes (2D)** | Pilot / acute KD screen; biochemistry cross-check | Fast, cheap, scalable; canonical in the field | Sarcomere disarray; 2D maturation ceiling; CSA measurement sensitive to substrate |
| **C2C12 myobundle (3D)** | Primary in-vitro quality screen for CHCHD10, NDUFB4, ATP5F1B, PGC-1α KD | Long-term maturation (≥14 d), better sarcomeres, more reproducible CSA, electrically-paceable | Setup overhead; lower absolute specific force than single-fibre in-vivo |
| **HSMM myobundle (3D)** | Human-relevance confirmation; sarcopenic-donor HSMM | Human, supports Aim 1 donor link | Donor variability, slow maturation (d21–28), expensive |

### 1.4 How in-vitro myobundle connects to the in-vivo single-fibre force assay (Exp A/B)

The in-vivo programme (Exp A — observational young vs aged C57BL/6J; Exp B — AAV9-shRNA CHCHD10 / ATP5F1B) uses a different rig (Aurora Scientific 300C-LR dual-mode lever with permeabilized single-fibre protocol; Brotto / Ahn / Frangini references; see §8). The in-vitro myobundle is the **in-vitro match to the in-vivo single-fibre force assay**:

- In-vivo single fibre: ~250 kN/m² (EDL); skinned fibres, Ca²⁺-activated.
- In-vitro myobundle: ~5–15 kN/m² (C2C12 mature); intact bundles, electrically stimulated.

The absolute numbers differ by ~20×, but the **proportional effect of a gene KD on specific force should agree** within ~2× between the two systems. A divergence in which the in-vitro model shows no effect while the in-vivo shows a strong effect is diagnostic: the in-vitro model is missing an aging context (denervation, inflammation, fibrosis). Convergence across both systems is the strongest possible support for the muscle-quality thesis.

### 1.5 What this SOP covers

- **2D single-myotube force** (§2) — Aurora Scientific 1300A or 1600A Permeabilized Myocyte System, or equivalent (IonOptix MyoCam-S + C-Pace EP). Faster, lower-cost, complementary to 3D.
- **3D engineered myobundle** (§3) — fibrin / Matrigel / PDMS-post system. **Primary in-vitro model for Aim 2.**
- **The matched-CSA analysis design** (§4) — three statistical approaches (regression, stratification, matched-pairs) with sample-size requirements.
- **Pre-registered analysis plan, QC gates, pitfalls, cross-references, cost, and a day-of-experiment checklist** (§5–11).

---

## 2. 2D single-myotube force (Aurora Scientific 1300A / IonOptix MyoCam)

### 2.1 Equipment options and what to use them for

| System | Vendor | Catalog | Best use | Notes |
|---|---|---|---|---|
| **Aurora Scientific 1300A** 3-in-1 Whole Animal System (300E lever + 605A data acquisition + 701C stimulator + 809C apparatus) | Aurora Scientific | **1300A** (mouse) / 1305A (rat) | Whole-muscle / engineered tissue bath. Used for 2D myotubes mounted on a custom glass-bottom chamber attached to the 809C-25 horizontal muscle bath. | The 1300A is a versatile rig but is *not* the only option. |
| **Aurora Scientific 1600A** Permeabilized Myocyte System | Aurora Scientific | **1600A** | **Best choice for 2D single-myotube force** — 8-well temperature-controlled bath, motorized XYZ stages, 400C force transducer (resolution 0.3 mN). | Includes HVSL (901D) for sarcomere length. |
| **Aurora Scientific 1400A** Permeabilized Fiber System | Aurora Scientific | **1400A** | Skinned (permeabilized) single fibres, including from biopsies | Auto-indexing bath; throughput 6–12 fibres / day |
| **IonOptix MyoCam-S** + C-Pace EP culture pacer | IonOptix | MyoCam-S (TBD per config) / C-Pace EP | Field-stimulation contractility on 2D myotubes (calcium-transient + edge-detection shortening) | C-Pace EP: ±40 V, 0.4–24 ms pulse, 1 channel per C-Dish |
| **CellScale MechanoCulture J1 / T6** | CellScale | MCJ1, MCT6 | Engineered tissue / bundle; high-throughput uniaxial stimulation | Force capacity 10–100 N; not single-myotube |

**Note for the CRO:** the prompt mentions "Aurora Scientific 1300A or equivalent" for single myotube work. The 1300A is technically a whole-animal rig that *can* be configured for in-vitro work (with the 809C-25 bath), but for true **single-myotube** contractility at the scale and resolution needed here, the **1600A Permeabilized Myocyte System is the better match**. Confirm with the CRO which rig they have on hand; the SOP is portable across the two.

### 2.2 Cell preparation for 2D force

- **Cell line:** C2C12 (ATCC **CRL-1772**, low-passage, p < 12). For HSMM (Lonza **CC-2580** / CC-2561 or equivalent), adapt the same protocol with longer differentiation (d7–10).
- **Plate substrate:**
  - **Glass-bottom 35 mm dish** (MatTek **P35G-1.5-14-C** or equivalent) coated with **Matrigel GFR (Corning 354230)** at 1:100 in DMEM/F-12, 1 h at 37 °C.
  - **OR Cell-Tak** (Corning **354240**) at 3.5 µg/cm² in 0.1 M NaHCO₃, 20 min RT, for stiffer attachment.
  - **Sylgard 184** (Dow **4019862**) bottom for compliance-matched reference — coat a 22 × 22 mm #1.5 coverslip with Sylgard mixed 1:10 (base:curing agent), cure 4 h at 60 °C, then Matrigel-coat as above.
- **Seeding density:** 1.5 × 10⁵ cells / 35 mm dish (sub-confluent at d0; myotubes visible by d3, robust by d5–7).
- **Differentiation:** switch to DM (DMEM + 2% horse serum + 1× ITS + 1 µM insulin) at ~90% confluence (d0). Replace every 48 h. Use by d5–7 for C2C12, d7–10 for HSMM.

### 2.3 Tyrode's solution (recipe for the rig bath)

| Component | mM |
|---|---|
| NaCl | 121 |
| KCl | 5 |
| CaCl₂ | 1.8 |
| MgCl₂ | 0.5 |
| NaH₂PO₄ | 0.4 |
| NaHCO₃ | 24 |
| glucose | 5.5 |
| HEPES | 10 |
| pH | 7.4 (with NaOH) |
| Osmolarity | 290 ± 5 mOsm (verify with osmometer) |

Pre-warm to 30 °C in a water bath; bubble with 95% O₂ / 5% CO₂ for at least 15 min before use. For the 2D rig, also include 0.2 mM L-ascorbic acid-2-phosphate to reduce oxidative damage during the 30–60 min experiment.

### 2.4 Stimulation protocol (field stimulation)

| Parameter | Value | Notes |
|---|---|---|
| Pulse width | 0.5 ms | Biphasic |
| Frequencies tested | 1, 10, 20, 40, 80 Hz | Full force-frequency curve; 1 Hz = twitch |
| Train duration | 350 ms | Long enough for tetanic fusion at 80 Hz |
| Inter-train interval | 60 s | Prevents fatigue |
| Voltage | 12–20 V (field) | Adjust to ~1.5× threshold per dish |
| Bath temperature | 30 °C | Standard for in-vitro skeletal muscle |

**Stimulation pattern for one bundle / dish:** twitch (1 Hz × 1 pulse) → wait 60 s → force-frequency (1, 10, 20, 40, 80 Hz trains in ascending order, 60 s rest between) → wait 120 s → final 80 Hz tetanus for CSA measurement.

### 2.5 Force readout (2D)

- **Twitch force (F_t):** peak force of the 1 Hz single pulse, in µN (typically 1–10 µN for a single C2C12 myotube).
- **Tetanic force (F_tet):** peak force during the 80 Hz train, in µN.
- **Twitch:tetanus ratio:** F_t / F_tet (0.2–0.4 is mature for C2C12; <0.1 indicates immature or sick).
- **Time-to-peak tension (TPT):** time from first stimulus to peak force, <100 ms for C2C12 myotubes at 30 °C.
- **Half-relaxation time (RT50):** time from peak to 50% force decay, <150 ms.

### 2.6 CSA measurement (2D myotube)

- After force measurement, capture **phase-contrast images at 20×** at 5–10 points along the myotube length.
- **Measure diameter (d)** at each point with ImageJ (straight-line tool, perpendicular to the myotube long axis), excluding regions of branch points or nuclei.
- **Mean diameter** across the 5–10 points is the value used.
- **CSA (mm²)** = π × (d_mean / 2)².
- **Specific force (kN/m²)** = F_tet (mN) / CSA (mm²).
- **Caveat:** assuming circular cross-section underestimates CSA by ~10–20% for non-circular myotubes. This is a systematic error; preserve the assumption across all conditions (do not switch to ellipse-fitting for one group) so the comparison remains unbiased.

### 2.7 Critical QC for 2D

- **Include only myotubes that produce BOTH a twitch AND a tetanic force** (exclude non-contracting, spontaneous-only, or twitching-but-non-tetanic).
- **Discard myotubes with visible detachment, hypercontraction, or sarcomere disarray** (visualize α-actinin by IF on a parallel dish; the 901D HVSL camera can do this in real time).
- **Track myotube age rigorously.** d5 vs d7 vs d10 differ markedly in force kinetics and specific force; report d.p.c. (days post-confluence) in every figure.
- **Plate-level controls:** every KD and every condition is paired with a scramble / non-targeting siRNA control on the same day, same plate lot, same Matrigel lot. Plate effects are larger than genotype effects in 2D — randomize well positions.

### 2.8 Limitations of 2D (and why 3D is recommended for Aim 2)

- Sarcomere disarray is common; HVSL sarcomere-length confirmation is not always available.
- Substrate compliance distorts force measurement (force is small — 1–10 µN; substrate bend artifact can rival the signal).
- Long-term culture (the maturation that drives specific force up) is harder in 2D.
- The 2D model is therefore a **screen**, not the primary readout. The 3D myobundle (§3) is the primary Aim 2 quality readout.

---

## 3. 3D engineered myobundle (fibrin / Matrigel hydrogel)

> **This is the recommended in-vitro model for HMSR Aim 2.** It supports the matched-CSA design (§4), is electrically-paceable for chronic maturation, and bridges to the in-vivo single-fibre force assay (Exp A / B; §8).

### 3.1 Why 3D for Aim 2

- **Long-term culture (14–28 d)** with chronic electrical stimulation → better sarcomere assembly and maturation.
- **Standard organ-bath rigs** (Aurora 1300A, 1600A with 809C-25 bath; CellScale MCJ1) are drop-in compatible.
- **Matched-CSA design** (§4) requires a population of bundles with a range of CSAs. The 3D system produces a wider, more controllable CSA distribution than 2D.
- **Sarcopenia-mimic interventions** (TNF-α, IL-6, dexamethasone, H₂O₂; see §3.7) can be applied chronically with a defined time course and recovered for force measurement.

### 3.2 Materials and vendors

| Item | Vendor | Catalog # | Pack | Indicative price (USD) | Notes |
|---|---|---|---|---|---|
| Fibrinogen from human plasma (50–70% protein, ≥80% clottable) | Sigma-Aldrich | **F3879** | 1 g | ~$456 | 50 mg-pack also available (F3879-50MG). Lyophilized; store –20 °C. |
| Thrombin from human plasma (≥2,000 NIH U/mg) | Sigma-Aldrich | **T6884** | 100 U or 1 kU | ~$95–$540 | Lyophilized; reconstitute 50 U/mL stock in 0.1% BSA in PBS |
| Matrigel® Growth Factor Reduced (GFR), LDEV-free | Corning | **354230** | 10 mL | ~$400 | Store –20 °C; avoid repeated freeze-thaw. Phenol-red-free variant: **356231** if fluorescence is needed. |
| Pluronic® F-127 (powder, BioReagent) | Sigma-Aldrich | **P2443** | 100 g / 1 kg | ~$95 / ~$640 | 0.2% w/v in water to coat PDMS molds (anti-adhesion) |
| Aprotinin from bovine lung (1.5 mg/mL stock) | Sigma-Aldrich | **A6106** | 5 mg | ~$110 | 1 mg/mL final; prevents fibrinolysis |
| 6-Aminocaproic acid (ACA) | Sigma-Aldrich | **A2504** | 100 g | ~$50 | 1.5–2 mg/mL in growth media |
| Sylgard 184 silicone elastomer kit (PDMS) | Dow / Ellsworth | **4019862** (kit) | 1.1 kg | ~$250 | Posts: 1:10 base:curing agent; 50 durometer |
| DMEM, high glucose, pyruvate | Gibco | **11995065** | 500 mL | ~$60 | |
| DMEM, low glucose | Gibco | **11885084** | 500 mL | ~$60 | Differentiation base |
| Horse serum (heat-inactivated) | Gibco / Hyclone | **26050088** / SH30074.03 | 500 mL | ~$300–$500 | Batch-test (see §3.6) |
| Fetal bovine serum (heat-inactivated) | Gibco | **10438026** | 500 mL | ~$500 | |
| Penicillin–streptomycin (10,000 U/mL) | Gibco | **15140122** | 100 mL | ~$25 | |
| Insulin-transferrin-selenium (ITS-G) | Gibco | **41400045** | 10 mL | ~$45 | |
| L-carnitine | Sigma | **C0283** | 10 g | ~$30 | 100 µM in DM |
| Palmitic acid | Sigma | **P0500** | 1 g | ~$50 | 5 µM; pre-conjugate to BSA |
| Sodium oleate | Sigma | **O7501** | 1 g | ~$50 | 5 µM; pre-conjugate to BSA |
| 6-well / 12-well non-tissue-culture-treated plates | Corning | **3737** (6 well) / **3738** (12 well) | case | ~$300 | For free-floating culture after compaction |
| Stainless steel minutien pins (0.1 mm) | Fine Science Tools | **26002-10** | pack | ~$30 | For frame anchoring |
| C-Pace EP chronic culture pacer (8-channel) | IonOptix | **C-Pace EP** (with C-Dish 6-well electrode assembly) | system | ~$10K–$15K | Multi-channel chronic pacing |
| C-Dish 6-well electrode assembly | IonOptix | **C-Dish** (6-well) | set | ~$600 | For 35 mm dishes |
| 3D-printed or PDMS-cast silicone-post molds | Custom (in-house or e.g. **Protolabs**, **Sculpteo**) | TBD per geometry | per lot | $200–$500 (in-house 3D print) | Frame-and-post geometry per Khodabukus 2014 |
| Aurora Scientific 300C-LR dual-mode lever | Aurora Scientific | **300C-LR** (1.0 N max, 0.5 mN resolution) | system | ~$8K–$12K | Force transducer; CROs typically have it |
| Aurora Scientific 1300A whole-animal system (alt) | Aurora Scientific | **1300A** | system | ~$45K–$60K | Includes 300E lever + 605A DAQ + 701C stim + 809C apparatus |
| CellScale MechanoCulture J1 (alt; high-throughput) | CellScale | **MCJ1** | system | ~$25K | 6 independent chambers; 10–100 N load cell |
| Kent Scientific FORCE 10 force sensor (alt; low-cost) | Kent Scientific | **FORCE 10** | unit | ~$1.5K | Single-channel; suitable for bundle force if calibrated |

**Vendor verification (confirmed at SOP issue):** Sigma F3879, T6884, P2443, Corning 354230, IonOptix C-Pace EP and C-Dish, Aurora 300C-LR / 1300A, CellScale MCJ1 — all confirmed by current vendor pages. The CRO should re-verify catalog numbers at quote time; the SOP and CRO RFP will note "catalog verified YYYY-MM-DD."

### 3.3 Cell seeding (per bundle)

**Recipe per 100 µL of bundle hydrogel** (final gel composition):

- 5 mg/mL fibrinogen (final)
- 2 U/mL thrombin (final)
- ~30% v/v Matrigel GFR
- Cells: 1 × 10⁶ C2C12 myoblasts per bundle (5 × 10⁵ for HSMM — fewer, slower maturation)
- 1 mg/mL final aprotinin (10 µL of 10 mg/mL stock per 100 µL gel)
- DMEM or differentiation media to volume

**Working stock recipes** (sufficient for ~50 bundles):

- **Fibrinogen stock:** 20 mg/mL in DMEM, sterile-filtered. Add 25 µL per 100 µL gel. (Note: warming at 37 °C for 15 min before use improves solubility.)
- **Thrombin stock:** 50 U/mL in 0.1% BSA in PBS. Add 4 µL per 100 µL gel. (Stock stable 1 month at 4 °C.)
- **Matrigel:** thawed on ice, used undiluted. Add 30 µL per 100 µL gel.
- **Aprotinin stock:** 10 mg/mL in PBS. Add 10 µL per 100 µL gel.

**PDMS mold and post geometry** (per Khodabukus & Baar 2014, PMID 25233218; Madden 2015 eLife):

- Mold: 17 × 8 mm PDMS well, 2 mm deep, cast from a Teflon master.
- Two semi-cylindrical PDMS posts (Ø 0.8 mm, 7 mm tall) anchored at the ends, separated by 7 mm working length.
- Frame (laser-cut Cerex, 9 × 9 mm, 1 mm rim) around the well to anchor bundle ends.
- Posts: 50 durometer PDMS (Sylgard 184 mixed 1:10 base:curing agent), 4 h cure at 60 °C. **Stiffness calibration:** see §3.4.
- Mold pre-treatment: 0.2% Pluronic F-127 in PBS, 1 h at RT, then air-dry, then UV-sterilize 20 min.

**Seeding procedure (timed, 4 h bench):**

1. Trypsinize myoblasts (0.05% Trypsin-EDTA, 5 min, 37 °C), neutralize 1:1 with growth media, count, spin 200 g × 5 min.
2. Resuspend at 1 × 10⁷ cells/mL in DMEM (10× stock for 1 × 10⁶ per 100 µL).
3. Prepare **cell solution** on ice: for n bundles, combine 10 × n µL cell suspension + 10 × n µL aprotinin stock + 4 × n µL thrombin stock.
4. Prepare **gelling solution** on ice: 25 × n µL fibrinogen stock + 30 × n µL Matrigel + (31 × n) µL DMEM.
5. Mix cell solution and gelling solution 1:1 (final volume 100 × n µL); keep on ice.
6. Pipette 100 µL of cell/hydrogel mix per PDMS well (avoid bubbles); ensure the bundle spans the two posts.
7. Polymerize 30 min at 37 °C, 5% CO₂ (no media on top yet).
8. Add 2 mL growth media + 1.5 mg/mL ACA. **Do not add aprotinin to media after d0; it is in the gel.**
9. Day 3: replace media with **DM** (differentiation): low-glucose DMEM + 2% horse serum + 100 µM L-carnitine + 5 µM palmitic acid–BSA + 5 µM sodium oleate–BSA + 1× ITS-G + 2 mg/mL ACA + 1% P/S.
10. **Begin chronic electrical stimulation at d3** (see §3.6). Do *not* start before d3 — early stimulation prevents gel compaction and contractile tissue formation.

### 3.4 Post stiffness calibration (critical — force = post deflection × k)

The relationship between post deflection and bundle force is:

$$F = k \cdot \delta$$

where **k** is the post bending stiffness (N/m). Calibrate per lot of PDMS.

**Calibration procedure:**

1. Cast 10 PDMS posts in the same batch as the experimental posts.
2. For each post, apply known weights (1, 2, 5, 10, 20, 50 mg; hang on the post tip with a fine wire hook) and measure tip displacement under a stereomicroscope.
3. Plot F (mN) vs displacement (µm); linear regression gives k in mN/µm = N/m.
4. **Acceptable range:** k between **0.5 and 5 mN/µm**. Posts stiffer than this give unmeasurable deflection; posts softer than this detach under tetanic load.

**Live bundle measurement (post-deflection method):**

1. Acquire phase-contrast image of the bundle + posts at 10× every 100 ms during the stimulation train.
2. Track post tip position with ImageJ (manual or automated with TrackMate).
3. δ(t) = post tip position at time t minus position at rest.
4. F(t) = k × δ(t).
5. Peak tetanic force = max(F(t)) during the 350 ms train.

**Alternative method (CRO-preferred):** mount the bundle between the 300C-LR lever and a fixed post, with the lever arm in **isometric mode** (length-clamped). This eliminates the post-deflection math but requires that the bundle be mounted on the lever (more complex holder; higher-throughput on a 300C).

### 3.5 Force measurement protocol (d14 for C2C12; d21–28 for HSMM)

**Day-of:** 30 °C Tyrode's bath, 95% O₂ / 5% CO₂ bubbling.

1. **Transfer bundle to bath** (5 min) — use a stainless steel minutien-pin handle or a 3D-printed transfer tool; never grasp the bundle.
2. **Mount between custom holders** (post-deflection method) or **between 300C-LR lever and fixed post** (isometric method).
3. **Equilibrate 15 min** at 30 °C in Tyrode's.
4. **Set optimal length (L_o).** Apply a 5% stretch ramp over 30 s, hold 1 min, measure passive force. Repeat in 2.5% increments until passive force rises sharply. The L at the foot of the rise is L_o. **Most bundles plateau in passive force at 110–130% of the slack length; L_o is typically at ~115% of slack.**
5. **Stimulation protocol (identical to 2D):**
   - Single twitch (1 Hz × 1 pulse), 60 s rest.
   - Force-frequency: 1, 10, 20, 40, 80 Hz trains (350 ms each), 60 s rest between, ascending order.
   - Wait 120 s; final 80 Hz tetanus.
6. **Capture peak tetanic force** at 80 Hz (primary endpoint).
7. **Capture twitch kinetics:** TPT, RT50, twitch:tetanus ratio.
8. **Capture passive tension at L_o.**
9. **CSA measurement (post-force):** acquire phase-contrast image at 3 points along the bundle (typically at 25%, 50%, 75% of working length). Measure outer diameter at each point with ImageJ. Mean diameter → CSA = π × (d/2)². (Some labs fix the bundle in 4% PFA and section for histology cross-section — preferred for publication figures but not strictly required for the matched-CSA design.)
10. **Compute specific force:** sF = F_tet (mN) / CSA (mm²).

### 3.6 Chronic electrical stimulation (during differentiation, d3 onward)

Use the **IonOptix C-Pace EP** with **C-Dish 6-well electrode assemblies**, in the incubator at 37 °C, 5% CO₂.

**Stimulation parameters (maturation protocol; per Khodabukus 2019, PMID 30973827):**

| Parameter | Value | Notes |
|---|---|---|
| Pulse duration | 10 ms | Biphasic |
| Frequency | 1 Hz | Continuous |
| Voltage | 2 V/cm (field) | Verified with a field probe at the start of each run |
| Duration | 30 min/day, every day d3 → d14 (C2C12) or d3 → d28 (HSMM) | Or 1-h on / 7-h rest cycle for higher maturation |
| C-Pace EP setup | 6-well C-Dish; 8-channel pacer | Use the 4-well C-Dish for higher-voltage protocols |

**Critical:** voltage > 2 V/cm → electrolysis, pH drift, cell death. Voltage < 1 V/cm → no capture, no maturation benefit. Verify field strength with a cathode-ray oscilloscope or field probe monthly.

### 3.7 Sarcopenia-mimicking interventions to test

| Intervention | Vendor / catalog | Dose | Duration | Mechanism |
|---|---|---|---|---|
| TNF-α (recombinant mouse) | Peprotech **315-01A** or Sigma **H8916** | 5–10 ng/mL | 48–96 h | NF-κB activation, SASP mimic |
| IL-6 (recombinant mouse) | Peprotech **216-16** | 5–20 ng/mL | 48–96 h | STAT3, JAK/STAT, atrogene induction |
| Dexamethasone | Sigma **D4902** | 1 µM | 48 h | Glucocorticoid atrophy model; ↓myogenin, ↓MyoD, MuRF1/MAFbx up |
| H₂O₂ | Sigma **216763** | 50–100 µM | 24 h | Oxidative stress; mimics aging mt-ROS burden |
| siRNA KD of CHCHD10 | Dharmacon siGENOME SMARTpool M-032322-01 (mouse) | 50 nM | Knockdown d–2 (transient) or d–7 (lentiviral); measure d14 | Tier 1 lead node; MICOS / cristae |
| siRNA KD of NDUFB4 | Dharmacon M-058960-01 (mouse) | 50 nM | as above | Tier 2; Complex I |
| siRNA KD of ATP5F1B | Dharmacon M-008484-01 (mouse) | 50 nM | as above | Tier 2; Complex V |
| siRNA KD of PGC-1α (PPARGC1A) | Dharmacon M-040445-01 (mouse) | 50 nM | as above | Master regulator; tests the whole-programme hypothesis |
| Scramble / non-targeting control | Dharmacon D-001206-13 (mouse) | 50 nM | as above | Negative control |

**Application for chronic treatment (TNF-α, IL-6, dex, H₂O₂):** add to DM at the indicated time, replace media + treatment every 48 h. **Do not** combine with chronic electrical stimulation > 1 Hz — already-stressed bundles will not survive. For combined treatment + EPS, use 0.5 Hz or skip EPS during treatment window.

**Application for siRNA KD (acute):** transduce bundles at d7 (lentiviral shRNA, MOI 5–10) or at d10 (siRNA via lipofectamine RNAiMAX, reverse transfection) and force-measure at d14 (C2C12) or d28 (HSMM). Verify knockdown by parallel qPCR / WB (≥ 70% mRNA reduction, ≥ 50% protein reduction is the acceptance threshold for the force measurement to be interpretable).

### 3.8 Knockdown verification (parallel plate)

- **qPCR:** 4–6 parallel bundles per condition pooled for RNA (RNeasy Mini **74104**), reverse-transcribe (SuperScript IV **18091200**), qPCR with gene-specific primers (TaqMan or SYBR; Thermo Fisher). Accept KD if mean mRNA < 30% of scramble.
- **WB:** 4–6 parallel bundles pooled, lyse in RIPA + protease inhibitors, run 20 µg/lane, probe with the matched antibody from `validation/antibodies/MITOPROGRAM_PANEL.md`. Accept KD if mean band intensity < 50% of scramble.
- **Seahorse Mito Stress Test (paired, on the same batch):** see `protocols/SEAHORSE_MITO_STRESS_TEST_SOP.md` for the parallel respiration readout on sister bundles. **Both the respiration and the force endpoints must point the same direction in the matched-CSA design** for the result to count as a "quality driver."

### 3.9 When to do Aim 1 vs Aim 2 vs Aim 3

This SOP is for **Aim 2 (causation, KD intervention).** For Aim 1 (donor / sarcopenic vs control HSMM), the only difference is the cells: use HSMM from a young, healthy donor (Lonza **CC-2580**, donor age 20–35) vs a sarcopenic donor (commercial source TBD; alternative is HSMM from a biopsy cohort; contract with the muscle biopsy CRO). All other steps identical. For Aim 3 (programme rescue), the addition is the rescue arm (e.g., Ad-PGC-1α overexpression in CHCHD10 KD; AICAR 1 mM; chronic EPS at 1 Hz in rescue). See the v0.2 plan and `validation/plan/experimental_validation_plan_v0.3.md` for the full arm structure.

---

## 4. Matched-CSA design (the critical Aim 2 endpoint)

> **This section is the scientific spine of Aim 2.** Read it carefully and pre-register the chosen statistical approach *before* starting the experiment.

### 4.1 The decisive contrast (verbatim from v0.2 plan)

> *"A knockdown that reduces OCR/specific force at matched myotube diameter supports H1; if force only falls in proportion to diameter loss, the gene acts via mass, not quality."* — `experimental_validation_plan_v0.2.md:76`

A raw force comparison (e.g., scramble 0.45 mN vs CHCHD10 KD 0.30 mN, p < 0.05) is **not sufficient**. The knockdown might also have reduced CSA, in which case the force loss is just a mass effect. The matched-CSA design forces a causal interpretation by removing the size confound.

### 4.2 Why a *population* matched-CSA design is more powerful than fixed-diameter exclusion

A common but weaker approach is to *exclude* any bundle with CSA < some threshold (e.g., < 300 µm). This throws away data and biases the population. The three approaches below all retain the full population and extract the CSA-independent effect statistically.

### 4.3 The three statistical approaches

#### 4.3.1 Approach 1 — Regression (recommended primary; most statistically powerful)

**Model:**

$$\log(F_\text{tetanus}) = \beta_0 + \beta_1 \cdot \log(\mathrm{CSA}) + \beta_2 \cdot \mathrm{Genotype} + \beta_3 \cdot \log(\mathrm{CSA}) \times \mathrm{Genotype} + \varepsilon$$

Run as a linear mixed model (LMM) with random effect `(1 | DifferentiationBatch)`:

$$\log(F) \sim \log(\mathrm{CSA}) \times \mathrm{Genotype} + (1 | \text{Differentiation})$$

- **β₂** (Genotype main effect) = force change at the average CSA (the *quality* effect, if positive).
- **β₃** (CSA × Genotype interaction) = does the slope of the force–CSA relationship differ? Usually near zero; a non-zero interaction suggests the KD changes how CSA translates to force (atypical but worth flagging).
- **β₁** (CSA main effect) = the expected force scales with CSA — usually ~0.7 to 1.0 (force ∝ CSA^β₁).
- The test of H1 is on **β₂** (log scale): a significantly negative β₂ with preserved β₁ and β₃ ≈ 0 = quality driver.

**Reporting:** back-transform β₂ to fold-change: 100 × (e^β₂ – 1)%.

**Sample size:** n ≥ 12 bundles per condition (per genotype, per differentiation batch, across ≥ 2 differentiations). Approach 1 needs the largest n because it estimates a regression coefficient; power is driven by the spread of CSA in the sample.

**R code (sketch):**

```r
library(lme4); library(lmerTest)
m <- lmer(log(F) ~ log(CSA) * Genotype + (1 | Differentiation), data = df)
summary(m)
emmeans::emtrends(m, ~ Genotype, var = "log(CSA)")  # for interaction check
emmeans::emmip(m, ~ Genotype | CSA)                  # visualization
```

#### 4.3.2 Approach 2 — Stratification (defensible and intuitive)

**Procedure:**

1. Pool all bundles across all conditions (scramble + all KDs).
2. Compute CSA quartiles (Q1, Q2, Q3, Q4) from the pooled distribution.
3. Within each quartile, compare specific force between KD and scramble.
4. A KD that reduces specific force within *every* quartile = quality driver (not driven by a single CSA subpopulation).

**Sample size:** n ≥ 8 per condition per quartile means n ≥ 32 per genotype total (8 × 4 quartiles). Often unrealistic; Approach 2 is most useful as a sensitivity check on Approach 1, not as the primary.

#### 4.3.3 Approach 3 — Matched-pairs (most defensible to reviewers; smallest n)

**Procedure:**

1. For each KD bundle, find a scramble bundle with CSA within ±10%.
2. Pair them (1 KD : 1 control); each pair is a matched observation.
3. Compute ΔsF = sF_KD − sF_Scramble per pair.
4. **Paired t-test** (or Wilcoxon signed-rank if non-normal) on ΔsF across pairs.
5. If mean ΔsF < 0 and p < 0.05 → quality driver. If p > 0.05 → refuter.

**Sample size:** n = 6–8 pairs is the minimum for 80% power at α = 0.05 to detect a 15% sF reduction (SD 10%). v0.2 plan targets n = 10 per arm for the in-vivo experiment; the same n is sufficient for the in-vitro.

**R code (sketch):**

```r
pair_df <- df %>%
  group_by(KD_id) %>%
  mutate(scramble_match = CSA[which.min(abs(CSA - CSA_value) & Genotype == "Scramble")])
# Or: do a pre-computed nearest-neighbor pairing (MatchIt or designmatch)
t.test(Pair(sF_KD, sF_Scramble) ~ 1, data = pair_df)  # paired t-test
cohens_d <- mean(pair_df$delta_sF) / sd(pair_df$delta_sF)
```

#### 4.3.4 Recommendation: Approach 1 (regression) primary, Approach 3 (matched-pairs) as reviewer-defensible secondary

- Approach 1 is the most statistically powerful and the standard in the Khodabukus / Madden / Baar literature.
- Approach 3 is the easiest to explain to a Reviewer 2 who is unfamiliar with LMM. Pre-register both; report both; if they agree, the result is robust.
- Approach 2 is rarely the primary, but is a useful sensitivity check.

### 4.4 Pre-registration of the matched-CSA design

Pre-register the analysis plan *before* opening the data file. The pre-registration is in `power_analysis/POWER_ANALYSIS.md` and is summarized in §5. The matched-CSA design must be locked in (statistical approach, n, exclusion criteria, multiple-testing correction) before the force measurement, not after.

### 4.5 Anticipated outcomes and their interpretation

| Outcome | Interpretation | Action |
|---|---|---|
| β₂ < 0 (Approach 1) **and** mean ΔsF < 0 (Approach 3), p < 0.05 | **Quality driver** — H1 supported. The KD reduces force independent of CSA. | This is the top-tier result. Move to next tier; if CHCHD10, NDUFB4, ATP5F1B all positive, the programme is a coordinated quality driver. |
| β₂ ≈ 0, β₁ reduced (slope is shallower) | Mass effect — force loss is proportional to CSA loss. | Refuter. The gene is a *mass* driver, not a quality driver. Re-frame: test if a combined mitochondrial + mass intervention recovers function better than either alone. |
| β₂ < 0 but β₁ reduced **and** CSA not reduced in KD | Mixed: KD reduces both force and the slope of force-on-CSA, suggesting both quality and architecture. | Investigate CSA distribution; if KD bundles cluster at low CSA, mass is the driver. If not, quality. |
| β₂ > 0 (KD **increases** sF) | Unusual. Possibly a compensatory up-regulation of remaining mitochondria, or an off-target effect. | Do not claim. Verify with a second siRNA pool and orthogonally with shRNA. |

---

## 5. Pre-registered analysis plan

### 5.1 Sample size (see `power_analysis/POWER_ANALYSIS.md` for full derivation)

| Approach | n per condition (KD or scramble) | n total per experiment | Justification |
|---|---|---|---|
| Approach 1 (regression) | ≥ 12 | ≥ 24 | 80% power to detect β₂ = –0.15 (15% sF drop) at α = 0.05 with SD(residual) = 0.10 and CSA range spanning 0.5× – 2× median |
| Approach 2 (stratification) | ≥ 8 per quartile per condition | ≥ 64 | Quartile-based; rarely primary |
| Approach 3 (matched-pairs) | ≥ 8 pairs | ≥ 16 (8 KD + 8 scramble) | 80% power to detect ΔsF = 15% with SD = 10% in paired t-test |

**Standard experimental unit:** one bundle from one differentiation batch. **Differentiation batch** is a random effect in all LMMs. **Recommended:** ≥ 3 independent differentiations per condition (so 36 bundles per genotype for Approach 1, pooled across 3 differentiations).

### 5.2 Primary statistical analysis

- **Approach 1:** LMM, `log(F_tet) ~ log(CSA) × Genotype + (1 | Differentiation)`, BH-FDR across the 4 KD targets. Test: β₂ (Genotype main effect) is significantly negative.
- **Approach 3:** Paired t-test on ΔsF (KD − matched scramble), per KD target. BH-FDR across the 4 KD targets.
- **Effect size:** Cohen's d (Approach 3) and standardized β₂ (Approach 1); both reported with 95% CI (bootstrap, 10,000 resamples).
- **Multiple testing correction:** Benjamini–Hochberg FDR at q = 0.05 across the 4 Tier-1/2 KDs (CHCHD10, NDUFB4, ATP5F1B, PGC-1α). If a 5th gene is added (MRPL34 or APOO), include it in the BH set.

### 5.3 Secondary analyses (supporting, not pre-registered)

- Force-frequency curve (specific force at each of 1, 10, 20, 40, 80 Hz).
- Twitch kinetics (TPT, RT50, twitch:tetanus ratio).
- Fatigue (1 Hz × 5 min continuous, decay time constant).
- Correlation between sF and matched Seahorse OCR (paired sister bundles; Pearson r with bootstrap CI).
- Correlation between sF and matched TMRE / MitoSOX (paired sister bundles).

### 5.4 Blinding

**All force measurements and all CSA measurements are performed blinded to genotype.** This is non-negotiable. The blinding key is held by a single designated lab member (the "unblinded PI") and is not opened until the analysis file is locked. Bracket the genotype labels with a scramble-vs-KD ordering unknown to the measurer.

### 5.5 Pre-registration timeline

- **2 weeks before first force measurement:** pre-registration document posted to OSF (or institutional equivalent) with: statistical approach, n, exclusion criteria, primary and secondary endpoints, blinding plan, multiple-testing correction.
- **Day of measurement:** raw force traces + raw CSA measurements stored; measurer remains blinded.
- **After data collection complete:** unblinding, locked analysis dataset, analysis script run, results reported against the pre-registered plan.

### 5.6 Deviations from the pre-registered plan

Any deviation (additional analysis, exclusion of a bundle not in the pre-registered exclusion list, change in n) is documented in a "Deviations" appendix to the analysis report, with rationale. Pre-registration is for transparency, not for rigidity in the face of unexpected biology — but the deviation log is the audit trail.

---

## 6. QC gates and acceptance criteria

### 6.1 Bundle health QC (before force measurement)

A bundle is **discarded** (and the exclusion logged) if any of the following:

- Spontaneous contractions under chronic stimulation (irregular, unrelated to stimulus — indicates hyperexcitability or dying cells).
- Visible gel detachment from the posts or the frame.
- Bundle diameter < 100 µm (too thin, no contractile tissue) or > 600 µm (necrotic core, central cells are nutrient-deprived).
- Macroscopic contamination (yeast, mold, mycoplasma-positive by routine test).
- Bundle detached from the post during transfer to the rig.

### 6.2 Force QC (during measurement)

A bundle is **discarded** (and the exclusion logged) if any of the following:

- Twitch:tetanus ratio < 0.10 (immature) or > 0.6 (atypical, possible spontaneous activity masking the twitch).
- TPT > 150 ms or < 20 ms (atypical, possibly dead or Ca²⁺-overloaded).
- RT50 > 300 ms (very slow, sick) or < 30 ms (unusually fast, possibly not a true tetanus).
- Passive tension at L_o > 10% of peak tetanic force (excessive baseline stiffness; bundle is fibrotic or compressed).
- Force trace shows clear rundown (> 30% drop) over three consecutive tetani at 80 Hz, 60 s apart (bundle is fatiguing faster than expected — sick or undersized).
- Force-frequency curve is non-monotonic (decreases between 40 Hz and 80 Hz) — indicates measurement error or electrode issue.

### 6.3 Specific force reference ranges (literature; do **not** use as a single target value)

| Preparation | Mature specific force range | Source |
|---|---|---|
| C2C12 myobundle (3D, fibrin/Matrigel, d14) | 5–15 kN/m² | Khodabukus & Baar 2014 (PMID 25233218); Madden 2015 eLife (PMID 26153763) |
| HSMM myobundle (3D, d21–28) | 3–10 kN/m² | Madden 2015 (PMID 26153763); Khodabukus 2019 (PMID 30973827) |
| Mouse single fibre EDL (in-vivo, permeabilized) | 250–350 kN/m² | Brotto 2012 (PMID 22987565); Lynch 2011 (PMID 21879801) |
| Mouse single fibre soleus (in-vivo, permeabilized) | 200–280 kN/m² | Brotto 2012; Lynch 2011 |
| Rat single fibre (in-vivo, permeabilized) | 200–300 kN/m² | |

**Interpretation of the ~20× in-vivo vs in-vitro gap:** the in-vitro myobundle is a *partial* model. It has well-organized sarcomeres, a defined force-frequency relationship, and a reproducible CSA — but it lacks the in-vivo context (denervation/inflammation/fibrosis/aging systemic milieu) and is generally cultured for ≤ 4 weeks vs the months-to-years of development in vivo. The aim is **proportional** effect-size agreement between in-vitro and in-vivo, not absolute agreement.

### 6.4 Pre-registered decision gates (from v0.2 plan)

| Gate | Decision criterion | Refuter |
|---|---|---|
| Aim 2 (function) | ≥ 1 Tier-1/2 KD reduces OCR ≥ 20% **at matched CSA** | Effect is mass-linked, not quality — reframe |
| Exp B (in-vivo) | Specific-force loss with CSA preserved (p < 0.05) | Programme is a passenger, not a driver |
| Exp D (therapeutic) | Quality arm > anabolic arm on function at ≤ mass | Mitochondrial restoration insufficient alone |

The matched-CSA design in this SOP operationalizes the Aim 2 decision gate. A positive result (sF drop with CSA preserved, p < 0.05) is the top-tier outcome; a refuter (sF tracks CSA) is publishable and hypothesis-correcting.

---

## 7. Common pitfalls

A list of failure modes that have killed Aim 2-style experiments in the literature. Each pitfall has a "how to avoid" in **bold**.

### 7.1 PDMS / post issues

- **Posts too stiff (high-durometer silicone, e.g., 70A or harder):** bundles don't deflect enough to resolve force. **Use 50-durometer PDMS (Sylgard 184 mixed 1:10 base:curing agent) or custom 40–60A silicone.** Verify with a known-weight calibration.
- **Posts too soft (low-durometer, < 30A):** bundles detach or rupture under tetanic load. **Calibrate each post lot; reject lots with k < 0.5 mN/µm.**
- **Post-mold release contamination:** residual curing agent or mold-release spray on posts prevents cell attachment. **Wash molds 3× with 70% EtOH and 3× with PBS after demolding; UV-sterilize.**
- **Post geometry drift during cure:** posts cure unevenly if mold is not level. **Cure on a leveled vibration-isolated table at 60 °C for 4 h.**

### 7.2 Cell seeding issues

- **Cell density too low (C2C12 < 5 × 10⁵/bundle):** bundles don't form contractile tissue; specific force < 2 kN/m². **Use 1 × 10⁶ / bundle for C2C12, 5 × 10⁵ for HSMM.**
- **Cell density too high (C2C12 > 2 × 10⁶/bundle):** necrotic core, poor survival, low specific force. **Verify survival at center of bundle by histology on a parallel bundle.**
- **Myoblast passage number too high (C2C12 p > 15):** reduced fusion and contractility. **Use p < 12.**
- **Cells not synchronized at differentiation:** replace media on a tight schedule (every 48 h) so all bundles are at the same d.p.c. ± 0.5 d. **Stagger the start of each differentiation batch by 1 d to allow force measurements on d14 to spread over d13–15.**

### 7.3 Hydrogel / matrix issues

- **Fibrinogen lot variability:** each Sigma F3879 lot has different clottability (50–70% protein, ≥80% clottable). **Test a new lot with a control bundle before running experiments; reject lots that give sF < 5 kN/m² on scramble.**
- **Matrigel lot variability:** growth factor content (even in GFR) varies; matrix stiffness varies. **Batch-test Matrigel lots; reserve one lot for the entire experiment if possible (Corning allows lot reservation; order early).**
- **Pluronic F-127 not fully dissolved:** 0.2% w/v in PBS requires slow mixing and 30 min at 4 °C. **Filter sterilize after full dissolution; do not autoclave (it degrades).**

### 7.4 Stimulation issues

- **Chronic stimulation too aggressive (> 2 V/cm field):** electrolysis, pH drift, cell death. **Measure field strength with a probe at the start of each run; cap at 2 V/cm.**
- **Stimulation at d0–2:** prevents gel compaction, no contractile tissue forms. **Start at d3 minimum.**
- **Single-pulse twitch with too short a wait (e.g., 5 s instead of 60 s):** twitch kinetics are confounded by post-tetanic potentiation. **60 s between stimuli; 120 s between tetani.**
- **Biphasic vs monophasic pulse:** monophasic pulses cause electrolysis at the cathode within minutes. **Always use biphasic (the C-Pace EP default is biphasic; verify).**

### 7.5 Length / CSA issues

- **Measuring force at sub-optimal length (L_o):** underestimates force. **Do the L_o ramp; record L_o; report the stretch ratio.**
- **CSA measurement at a single point (vs ≥ 3 points averaged):** introduces noise. **Always measure at ≥ 3 points along the bundle length; report mean ± SD.**
- **CSA measurement biased by the measurer (who is not blinded):** introduces systematic error. **Blind the measurer; if possible, have a second measurer re-score a random 20% of bundles; check inter-rater ICC > 0.8.**

### 7.6 KD / pharmacology issues

- **siRNA off-target effects:** a single siRNA oligo can have non-target knockdowns. **Use SMARTpool (4 oligos per target) for the primary experiment; if a single pool is positive, validate with a second independent pool (orthogonal).**
- **siRNA KD too short (24–48 h):** protein may not be fully depleted. **For CHCHD10 and ATP5F1B, the protein half-life is ≥ 72 h; use lentiviral shRNA for sustained KD or siRNA with a 96 h pre-incubation before force measurement.**
- **Lentiviral shRNA toxicity:** MOI > 10 kills cells. **Titrate MOI on a 2D pilot; use MOI 5–10.**
- **TNF-α / dexamethasone toxicity at high dose:** 20 ng/mL TNF or 10 µM dex kills bundles. **Titrate the dose on a parallel 2D viability assay first.**

### 7.7 Analysis / interpretation issues

- **Forgetting to log-transform force and CSA before regression:** the relationship is power-law, not linear. **Log-log regression is the standard; report the back-transformed fold-change.**
- **Forgetting to include the differentiation batch as a random effect:** pseudoreplication inflates n and underestimates SE. **Always include `(1 | Differentiation)` in the LMM.**
- **Reporting only p-values, not effect sizes with CI:** reviewers will ask. **Always report Cohen's d, Hedges' g, or standardized β with 95% CI (bootstrap).**
- **Claiming "no effect" from a non-significant p-value with low n:** underpowered. **Pre-register n; if n is not reached, report the result as inconclusive, not negative.**

---

## 8. Cross-reference to in-vivo single-fibre force (Exp A / B)

### 8.1 The in-vivo rigs (Exp A — observational; Exp B — AAV9-shRNA)

| System | Vendor | Catalog | Best for | Cost |
|---|---|---|---|---|
| **Aurora Scientific 300C-LR** dual-mode lever | Aurora Scientific | **300C-LR** (1.0 N max, 0.5 mN resolution) | Permeabilized single-fibre force (the in-vivo gold standard) | ~$8K–$12K (lever only; full 1400A system $30K–$45K) |
| Aurora Scientific 1400A Permeabilized Fiber System | Aurora Scientific | **1400A** | Full permeabilized-fibre workflow with auto-indexing bath | ~$30K–$45K |
| Aurora Scientific 901D HVSL (High-Speed Video Sarcomere Length) | Aurora Scientific | **901D** | Sarcomere length measurement by laser diffraction or video | ~$10K–$15K |
| 400C series force transducer | Aurora Scientific | **400C** (multiple force ranges) | Direct-mount force transducer for skinned fibres | ~$5K–$8K |

### 8.2 Key differences between in-vivo single-fibre and in-vitro myobundle

| Parameter | In-vivo single fibre | In-vitro myobundle |
|---|---|---|
| Specific force (mouse, mature) | 250–350 kN/m² (EDL); 200–280 kN/m² (soleus) | 5–15 kN/m² (C2C12 d14) |
| Activation | Ca²⁺-activated skinned fibre; pCa 4.5–8.0 | Electrically stimulated intact bundle |
| Sarcomere length set by | Laser diffraction (HVSL) or video | Bundle length clamped at L_o; sarcomere length inferred |
| CSA measurement | Fibre diameter at 3 points (circular assumption) — or elliptical from histology | Bundle diameter at 3 points (circular assumption) — or histology cross-section |
| Biological n | 10–20 fibres per mouse, 5–10 mice per group | 6–12 bundles per condition per differentiation, 3+ differentiations |
| Variability source | Mouse-to-mouse, fibre-to-fibre (Type I vs II), batch of permeabilization | Differentiation-to-differentiation, gel batch, Matrigel lot |
| Time to mature | Native | 14 d (C2C12) or 21–28 d (HSMM) |
| Aging context | Native (young vs aged) or AAV9-shRNA 8 wk post-injection | Sarcopenia-mimic intervention (TNF, IL-6, dex, H₂O₂) for 48–96 h |

### 8.3 The convergence test

**If a gene KD reduces in-vivo specific force by 15% (Exp B, AAV9-shRNA CHCHD10 in TA), the in-vitro myobundle should also reduce sF by 10–30% (within 2×) for the in-vitro model to be considered validated.**

- If in-vitro and in-vivo agree (both reduce sF at matched CSA): the in-vitro model is validated for that gene; the programme is a *quality* driver in vivo.
- If in-vitro shows no effect and in-vivo shows 15% sF loss: the in-vitro model is missing a critical aging context. Investigate: combine KD with TNF-α or IL-6 to mimic the aging milieu; verify that the in-vitro effect emerges.
- If in-vitro shows a stronger effect than in-vivo: the in-vitro model is more sensitive; in-vivo may be buffered by systemic factors (e.g., compensatory up-regulation in contralateral muscle). This is informative, not a refuter.

---

## 9. Cost & timeline

### 9.1 Setup costs (one-time)

| Item | Cost (USD) | Lead time |
|---|---|---|
| PDMS mold tooling (in-house 3D print, Teflon master, Cerex frames) | $500–$2,000 | 2–4 weeks |
| Aurora 300C-LR lever (if not already owned) | $8K–$12K | 4–6 weeks |
| Or Aurora 1300A whole-animal rig (3-in-1) | $45K–$60K | 6–10 weeks |
| CellScale MechanoCulture J1 (alternative, 6-chamber) | ~$25K | 4–6 weeks |
| IonOptix C-Pace EP chronic pacer + 6-well C-Dish | $11K–$16K | 3–6 weeks |
| Kent Scientific FORCE 10 sensor (low-cost bundle force option) | ~$1.5K | 1–2 weeks |
| ImageJ + force transducer DAQ setup | $0 (ImageJ open source) + $500 DAQ | 1 week |
| Custom software for post-deflection tracking (Python / MATLAB) | in-house | 2 weeks |

### 9.2 Per-experiment cost

| Item | Cost (USD) per experiment (assume 1 condition, 3 differentiations, 12 bundles per differentiation) |
|---|---|
| C2C12 cells (ATCC CRL-1772) | $300 (expansion) |
| HSMM cells (Lonza CC-2580, 1 donor) | $1,200 |
| Fibrinogen (Sigma F3879, 1 g) | $456 |
| Thrombin (Sigma T6884, 1 kU) | $540 |
| Matrigel GFR (Corning 354230, 10 mL) | $400 |
| Pluronic F-127 (Sigma P2443, 100 g — sufficient for many experiments) | $95 |
| Aprotinin, ACA, media, horse serum (one round) | $400–$600 |
| siRNA / shRNA constructs (Dharmacon, 4 targets + scramble) | $1,200 |
| qPCR + WB verification (parallel plates) | $500 |
| Seahorse Mito Stress Test on sister bundles (paired) | $2,000 (cartridges + media) |
| **Total per experiment (C2C12, 4 KDs + scramble, 3 differentiations, 36 bundles/condition)** | **~$7K–$9K** |
| **Total per experiment (HSMM, 4 KDs + scramble, 3 differentiations, 36 bundles/condition)** | **~$12K–$15K** |

### 9.3 CRO outsource cost (recommend for the in-vivo single-fibre portion; in-house for the 3D myobundle)

| CRO | Specialty | Indicative cost per condition (10–15 bundles) | Indicative lead time |
|---|---|---|---|
| **Muscle Forum Labs** (UK) | 3D myobundle force + histology | $5K–$8K | 8–12 weeks |
| **ProCytech** (FR) | Skinned single-fibre force, Oroboros | $5K–$10K | 8–16 weeks |
| **Charité Berlin Muscle Physiology Core** (DE) | Permeabilized fibre + intact bundle | $4K–$8K | 8–12 weeks |
| **Crown Bioscience** (US/EU/CN) | iPSC-derived myocyte myobundle | $5K–$8K per donor | 12–16 weeks |
| **iPSC Core** (academic; varies) | Custom iPSC myogenic differentiation + CRISPR | $5K–$8K per donor line | 12–24 weeks |

### 9.4 Timeline for the full Aim 2 (in-house)

| Month | Milestone |
|---|---|
| M1 | Vendor orders, mold fabrication, cell-line acquisition, C-Pace EP install |
| M2 | C2C12 pilot bundles (3 differentiations, 12 bundles each); establish scramble baseline sF |
| M3 | First 3 KDs (CHCHD10, NDUFB4, ATP5F1B) + scramble in C2C12; matched-CSA pre-registration locked |
| M4 | PGC-1α KD + rescue (Ad-PGC-1α); tier-1 confirmation |
| M5 | HSMM pilot (1 donor, 3 differentiations); establish scramble baseline sF for HSMM |
| M6 | HSMM KDs; Aim 1 cross-reference (sarcopenic vs control donor if available) |

---

## 10. References

### 10.1 Primary protocol papers

1. **Khodabukus A, Baar K.** "Regulating fibrinolysis to engineer skeletal muscle from the C2C12 cell line." *Tissue Eng Part C Methods* 15(3):501–511, 2009. (Foundational fibrin + C2C12 + aprotinin protocol.) DOI: 10.1089/ten.tec.2008.0286
2. **Khodabukus A, Baar K.** "Defined electrical stimulation emphasizes ex vivo tissue development." *Tissue Eng Part C Methods* 18(3):249–257, 2012. (Electrical pacing protocol.)
3. **Khodabukus A, Baar K.** "Optimizing a fibrin + Matrigel + C2C12 myobundle for contractile force." PMID 25233218, 2014. (Protocol refined for reproducible specific force.)
4. **Madden L, Juhas M, Kraus WE, Truskey GA, Bursac N.** "Bioengineered human myobundles mimic clinical responses of skeletal muscle to drugs." *eLife* 4:e04885, 2015. PMID 26153763. (HSMM myobundle drug-response benchmark.)
5. **Khodabukus A, Madden L, Prabhu NK, Koves TR, Jackman CP, Muoio DM, Bursac N.** "Electrical stimulation increases hypertrophy and metabolic flux in tissue-engineered human skeletal muscle." *Biomaterials* 198:259–269, 2019. PMID 30973827. (Maturation + chronic pacing.)
6. **Dennis RG, Dow DE.** "Excitability of skeletal muscle during development, disease, and adaptation." *Can J Appl Physiol* 32(5):553–570, 2007. PMID 17992290. (Aurora Scientific in-vitro muscle test system overview.)
7. **Cheng CS, Davis BN, Madden L, Bursac N, Truskey GA.** "Challenges and strategies for engineering a functional tissue-engineered skeletal muscle." *Tissue Eng Part B Rev* 20(6):687–698, 2014. PMID 24401938. (Review of engineered muscle design choices.)
8. **Brotto M, Abreu E.** "Sarcopenia and the muscle-bone interaction in aging." *Curr Osteoporos Rep* 10(3):204–210, 2012. PMID 22987565. (Single-fibre force protocols in aging context.)
9. **Lynch GS.** "Update on emerging drugs for sarcopenia — age-related muscle loss." *Expert Opin Emerg Drugs* 16(4):735–752, 2011. PMID 21879801. (Permeabilized-fibre techniques and aging applications.)
10. **Juhas M, Engelmayr GC, Fontanella AN, Palmer GM, Bursac N.** "Bioreactor-induced self-assembly of elongated muscle fibers in fibrin gel." *Tissue Eng Part A* 20(5–6):1010–1021, 2014. (Fibrin compaction and alignment.)
11. **Hinds S, Tyhovych N, Bursac N.** "A protocol for rapid scaffold-free engineering of functional skeletal muscle tissues." *J Tissue Eng Regen Med* 5(8):622–632, 2011. (Scaffold-free alternative.)
12. **Guzman SD, et al.** (Preprint / recent publication; 2026) — muscle-specific CHCHD10 CRISPR-KO recapitulates aged-muscle phenotypes. (Cited in v0.2 plan as the precedent for the 15% sF reduction power assumption.) [Note: full citation to be confirmed at SOP issue; see `manuscripts/experimental_validation_plan_v0.2.md:46`]

### 10.2 Companion HMSR documents

- `manuscripts/experimental_validation_plan_v0.2.md` — Aim 2 v0.2 plan; the source of the matched-CSA decision gate
- `validation/README.md` — operationalization of Aim 2 into wet-lab specifications
- `validation/protocols/SEAHORSE_MITO_STRESS_TEST_SOP.md` — paired respiration SOP (sister endpoint)
- `validation/power_analysis/POWER_ANALYSIS.md` — full n derivation (paired with this SOP)
- `validation/plan/experimental_validation_plan_v0.3.md` — v0.3 plan with construct IDs, vendor, cost line items
- `validation/constructs/` — siRNA / shRNA / gRNA sequences (mouse + human); vendor-mapped
- `validation/antibodies/MITOPROGRAM_PANEL.md` — mitochondrial programme protein panel for KD verification
- `validation/vendors/` — vendor shortlist (cell lines, reagents, kits, CROs)

### 10.3 Vendor documentation (URLs confirmed at SOP issue; verify at quote time)

- Aurora Scientific 1300A: <https://aurorascientific.com/products/muscle-physiology/systems/1300a-whole-animal-system-mice/>
- Aurora Scientific 1600A Permeabilized Myocyte System: <https://aurorascientific.com/products/muscle-physiology/systems/1600a-permeabilized-myocyte-system-microscope-mountable/>
- Aurora Scientific 300C-LR dual-mode lever: <https://aurorascientific.com/products/muscle-physiology/controllers-levers-transducers/300c-dual-mode-muscle-levers/>
- IonOptix C-Pace EP Culture Pacing System: <https://www.ionoptix.com/products/systems/cell-culture-pacing/>
- Sigma F3879 Fibrinogen from human plasma: <https://www.sigmaaldrich.com/US/en/product/sigma/f3879>
- Sigma T6884 Thrombin from human plasma: <https://www.sigmaaldrich.com/US/en/product/sigma/t6884>
- Sigma P2443 Pluronic F-127: <https://www.sigmaaldrich.com/US/en/product/sigma/p2443>
- Corning 354230 Matrigel GFR: <https://ecatalog.corning.com/life-sciences/b2b/CALAOther/en/Surfaces/Extracellular-Matrices-ECMs/Corning%C2%AE-Matrigel%C2%AE-Matrix/p/354230>
- CellScale MechanoCulture J1: <https://www.cellscale.com/products-cellscale-biomaterials-testing/mcj1-4/>

---

## 11. Day-of-Experiment Checklist

> **Print and bring to the rig.** A copy lives in `validation/protocols/CHECKLISTS/`.

### 11.1 Two days before the experiment

- [ ] Verify all reagents within expiry; thaw Matrigel on ice overnight at 4 °C.
- [ ] Prepare fresh Tyrode's (1 L); verify pH 7.4 and osmolarity 290 ± 5 mOsm.
- [ ] Verify C-Pace EP is functional; test field strength with a probe in a mock 6-well dish.
- [ ] Check the incubator (37 °C, 5% CO₂); clean and re-fill water tray.
- [ ] Confirm the assigned measurer is blinded to the genotype key.
- [ ] Pre-registration of the matched-CSA statistical approach is locked in OSF (or equivalent).

### 11.2 Day before the experiment

- [ ] Differentiate fresh media: DM (low-glucose DMEM + 2% horse serum + 100 µM L-carnitine + 5 µM palmitic acid–BSA + 5 µM sodium oleate–BSA + 1× ITS-G + 2 mg/mL ACA + 1% P/S); warm to 37 °C; ~50 mL per 6-well.
- [ ] Prepare fresh fibrinogen stock (20 mg/mL in DMEM) — filter-sterilize, 37 °C 15 min to dissolve, then keep at 4 °C.
- [ ] Prepare fresh thrombin stock (50 U/mL in 0.1% BSA in PBS) — aliquot and keep at 4 °C; stable 1 month.
- [ ] Prepare fresh 0.2% Pluronic F-127 in PBS (sterile-filtered); keep at 4 °C.
- [ ] Set up the force rig: Tyrode's bath at 30 °C, O₂/CO₂ bubble on, stimulator tested with a mock load.
- [ ] Stage the bundles in 6-well plates with fresh DM; check each bundle under the stereomicroscope for detachment, contamination, or visible damage.
- [ ] Pre-heat the imaging station (microscope, camera, ImageJ with calibration slide).
- [ ] Run the post-stiffness calibration *if posts are a new lot* (see §3.4).
- [ ] Confirm the post-stiffness k is in the 0.5–5 mN/µm range; if not, replace the post lot.

### 11.3 Morning of the experiment

- [ ] Replace bundle media with pre-warmed Tyrode's 30 min before measurement.
- [ ] Set up the imaging station: phase-contrast, 10× and 20× objectives calibrated.
- [ ] Verify the ImageJ post-tip tracking macro / script is loaded and the calibration is current.
- [ ] Verify the force transducer DAQ is recording at ≥ 1 kHz.
- [ ] Verify the stimulator is set to the protocol (twitch → force-frequency 1, 10, 20, 40, 80 Hz → final 80 Hz tetanus; 350 ms train, 60 s rest).
- [ ] Prepare a labelled force-measurement data sheet (paper or electronic) with: bundle ID, genotype (scramble / KD-1 / KD-2 / KD-3 / KD-PGC1a, blinded to the measurer), differentiation batch, d.p.c., post-stiffness k value.

### 11.4 At the rig — per bundle

- [ ] Photograph the bundle at the stereomicroscope before mounting (record any visible defects; mark "discard" if needed).
- [ ] Mount the bundle in the bath; equilibrate 15 min at 30 °C.
- [ ] Set L_o (5% stretch ramp; 2.5% increments; identify the L at the foot of the passive-tension rise).
- [ ] Run the twitch (1 Hz, single pulse). Check that the force is a clean monophasic twitch.
- [ ] Run the force-frequency protocol. Plot peak force vs frequency in real time; verify monotonic increase to 80 Hz.
- [ ] Capture the final 80 Hz tetanus (peak force, TPT, RT50, twitch:tetanus ratio, passive tension).
- [ ] Photograph the bundle after force measurement (3 CSA points: 25%, 50%, 75% of working length).
- [ ] Measure CSA at all 3 points in ImageJ; record mean ± SD.
- [ ] Compute sF = F_tet (mN) / CSA (mm²).
- [ ] Apply QC gates (§6.2); if a bundle fails, log the reason and discard.
- [ ] Save raw data, processed data, and the bundle's image stack. The measurer remains blinded.
- [ ] After all bundles are done for the day, transfer bundles to Trizol / RIPA (parallel) for qPCR / WB verification.

### 11.5 End of day

- [ ] Lock the day's data file (read-only); back up to the lab server.
- [ ] Update the pre-registration deviation log if any bundles were excluded for non-pre-registered reasons.
- [ ] Verify the next day's bundles are in the incubator with chronic EPS running (C-Pace EP on, 1 Hz, 2 V/cm, 30 min on / 90 min rest, 4–6 cycles per day).
- [ ] Clean the rig: flush Tyrode's bath with 70% EtOH, then dH₂O; refill with fresh Tyrode's; cover for the night.
- [ ] Recharge / replace the C-Pace EP high-voltage board if voltage output is < 90% of set value.

### 11.6 At the analysis step (post-experiment)

- [ ] Unblind the genotype key (only after all data is locked).
- [ ] Run the pre-registered analysis script (Approach 1 LMM, Approach 3 paired t-test).
- [ ] Verify the BH-FDR correction is applied across the 4 KD targets.
- [ ] Generate the figures: force-frequency curve, sF at 80 Hz vs CSA scatter with regression line (Approach 1), sF in CSA quartiles (Approach 2), ΔsF in matched pairs (Approach 3).
- [ ] Generate the QC figure: twitch kinetics, passive tension, bundle CSA distribution per condition.
- [ ] Cross-reference with the parallel Seahorse OCR data (sister bundles); report sF–OCR correlation with 95% CI.
- [ ] Write up against the pre-registered plan; log any deviations in the analysis appendix.

### 11.7 Quick-reference numbers (laminate and stick to the rig)

| Parameter | Value |
|---|---|
| Bath temperature | 30 °C |
| Tyrode's pH | 7.4 |
| Tyrode's osmolarity | 290 ± 5 mOsm |
| Pulse width | 0.5 ms (biphasic) |
| Force-frequency frequencies (Hz) | 1, 10, 20, 40, 80 |
| Train duration | 350 ms |
| Inter-train rest | 60 s |
| Twitch: tetanus ratio (mature) | 0.2–0.4 |
| TPT (mature) | < 100 ms |
| RT50 (mature) | < 150 ms |
| Passive tension at L_o | < 10% of F_tet |
| C2C12 bundle sF (mature) | 5–15 kN/m² |
| HSMM bundle sF (mature) | 3–10 kN/m² |
| Post-stiffness k (acceptable) | 0.5–5 mN/µm |
| C2C12 bundle diameter (acceptable) | 100–600 µm |
| Chronic EPS voltage field | ≤ 2 V/cm |
| Chronic EPS frequency | 1 Hz |
| Chronic EPS start day | d3 (never before) |
| KD verification threshold (mRNA) | < 30% of scramble |
| KD verification threshold (protein) | < 50% of scramble |

---

> **End of SOP v0.1 — `MYOBUNDLE_SPECIFIC_FORCE_SOP.md`**
> **Next review:** upon completion of M2 (C2C12 pilot), or earlier if vendor catalog numbers shift.
> **Sign-off:** Aim 2 working group lead; wet-lab collaborator / CRO RFP issuer; Larry (Brown Biotech AI / validation-aim2 owner).
