# In Vitro / In Vivo Validation Plan v0.2
## From a mitochondrial-programme discovery to a function-level proof in sarcopenia

**Supersedes** `experimental_validation_plan_v0.1.md`, which predated the v0.2–v0.4
corrections. This version is aligned to the corrected science and is designed as the
**path from a JCR 5–10% resource paper to a top-tier discovery paper**.

**Version:** v0.2 — 2026-06-12

---

## 0. What changed from v0.1 (read first)

| v0.1 framing (wrong) | v0.4 corrected framing (this plan) |
|---|---|
| "7 replicated OXPHOS genes" | **Pathway-level** finding: the whole mitochondrial **biogenesis programme** is coordinately down (permutation p=2.0×10⁻³, all 6 sub-modules; robust to 3 confound controls). Only **NDUFB4 + ATP5F1B are true OXPHOS subunits**. |
| CLTB treated as mitochondrial | **CLTB is NOT mitochondrial** (clathrin light chain B). Tested separately, not in the mito arm. |
| Gene-centric validation | Validate the **programme** and the **strongest causal nodes**, with **function (specific force, respiration)** — not mass — as the primary readout. |

**The honest gap the discovery leaves open** (and what this plan must close):
the human result is (i) correlational, (ii) cross-sectional, (iii) transcript-level
(does not measure respiration/content/flux), (iv) underpowered per gene. Validation
must show the programme down-regulation **causes loss of mitochondrial function and
muscle quality**, and is **reversible**.

---

## 1. Central hypothesis and the design principle that makes it top-tier

**H0 (discovery):** In sarcopenic human muscle, the nuclear-encoded mitochondrial
biogenesis programme (translation, import, cristae, respiratory chain) is coordinately
down-regulated.

**H1 (causation):** Suppressing this programme — or its strongest individual nodes —
**lowers mitochondrial respiration and specific force (force per cross-sectional area)
without necessarily lowering muscle mass.**

**The design principle (borrowed from the companion muscle-quality Perspective):**
the decisive readout is **muscle quality = function per unit size**, not bulk. A
manipulation that reduces specific force / respiration while CSA is held constant
proves the programme is a *quality* driver. This dissociation is what separates a
confirmatory mitochondrial study from a mechanistic one, and is the reason to measure
single-fibre/myotube specific force and Seahorse respiration as **primary** endpoints.

**Gene tiers (by the corrected stats):**
- **Tier 1 — lead node:** *CHCHD10* (β=−0.16, p=7.5×10⁻⁶, **I²=0%**, MICOS/cristae). Strongest, zero heterogeneity; external support: muscle-specific CRISPR-KO of CHCHD10 recapitulates aged-muscle phenotypes incl. reduced ATP and NMJ fragmentation (Guzman 2026).
- **Tier 2 — true OXPHOS subunits:** *NDUFB4* (Complex I), *ATP5F1B* (Complex V) — direct respiratory-chain test.
- **Tier 3 — biogenesis/translation:** *MRPL34*, *MRPL33* (mitoribosome), *APOO* (MICOS).
- **Programme master switch:** *PPARGC1A* (PGC-1α) — manipulate to test whether the *whole programme* is reproducible from one node.
- **Separate track (non-mito):** *CLTB* — is it a real hit (clathrin-mediated mitophagy?) or a passenger? Low-priority, hypothesis-generating only.

---

## 2. In Vitro Program

### Models
- **C2C12** myotubes — primary screen (siRNA, fast).
- **Primary human skeletal-muscle myotubes (HSMM)** from sarcopenic vs control donors — human relevance + the discovery-confirmation arm.
- **iPSC-derived myocytes** with isogenic CRISPR KO of *CHCHD10* and *ATP5F1B* — clean causal human model.

### Aim 1 — Confirm the discovery beyond transcript (closes gap iii)
Independent sarcopenic vs control human myotubes/biopsies (n≥10/group):
- Mitochondrial **protein** panel (immunoblot/targeted proteomics) for the programme — does the down-regulation hold at protein, not just mRNA?
- **Respiration** (Seahorse), mtDNA copy number, PGC-1α/TFAM.
- **Primary endpoint:** is the mitochondrial programme down at the protein/function level, and does it correlate with donor grip strength / fibre specific force?

### Aim 2 — Causation: does losing the programme impair *function*? (closes gaps i, iii)
siRNA/CRISPR knockdown of Tier 1–2 genes (CHCHD10, NDUFB4, ATP5F1B) and PGC-1α in myotubes.

**Primary (quality) endpoints:**
- **Mitochondrial respiration** — Seahorse Mito Stress Test (basal, ATP-linked, maximal OCR, spare capacity).
- **Specific force proxy** — engineered myobundle / electrically-paced force normalized to myotube CSA (the in vitro "force per size" readout).

**Secondary:** ΔΨm (TMRE), mt-ROS (MitoSOX), ATP rate, mitochondrial morphology (TEM/confocal), myotube diameter & fusion index (to show **CSA can be held while function drops**).

**Decisive contrast (the quality test):** a knockdown that reduces OCR/specific force at **matched myotube diameter** supports H1; if force only falls in proportion to diameter loss, the gene acts via mass, not quality.

### Aim 3 — Is it a coordinated *programme*? (tests the pathway-level claim)
- Knock down **PGC-1α** → does it reproduce the *whole* mitochondrial-programme signature (RNA-seq) seen in human sarcopenia? (tests whether one master node explains the coordinated pattern).
- **Rescue:** Ad-PGC-1α overexpression in CHCHD10/NDUFB4-KD myotubes → does restoring biogenesis recover respiration/force?
- **Exercise-mimetic:** AICAR / electrical pulse stimulation on KD myotubes → does an exercise signal compensate? (in vitro preview of the in vivo reversal arm).

### Aim 4 — CLTB (separate, low priority)
Test whether CLTB couples to mitophagy (CHCHD10/CLTB co-IP; mt-Keima flux). Purpose:
decide whether CLTB belongs in the mitochondrial story at all. Hypothesis-generating.

---

## 3. In Vivo Program

### Exp A — Observational (does the programme track function with age?)
Young (3-mo) vs aged (24-mo) C57BL/6J, n=8/group, TA/gastrocnemius/soleus.
- Mito programme (qPCR + protein), permeabilized-fibre respiration (Oroboros), **single-fibre specific force**, fibre CSA, grip strength.
- **Endpoint:** does the programme decline **track specific force more tightly than it tracks mass/CSA**? (the quality-vs-mass correlation in vivo).

### Exp B — Causal sufficiency (the key quality experiment)
AAV9-shRNA knockdown of **CHCHD10** and **ATP5F1B** in TA of young mice (contralateral scramble control; n=10; 8 wk).
- **Primary:** in vivo specific force / tetanic force normalized to CSA; permeabilized-fibre respiration.
- **Secondary:** muscle mass, fibre CSA, fibre-type, TEM, mtDNA, grip/rotarod, RNA-seq.
- **Decisive result:** loss of specific force / respiration **with mass and CSA relatively preserved** = the programme is a *quality* driver (the top-tier result). If mass falls proportionally, it is a mass effect.
- Power: 0.80, α=0.05, expected 15% specific-force reduction (CHCHD10-KO precedent), SD 10% → n≈9; use 10.

### Exp C — Reversibility / exercise (closes the WP5 gap)
3-mo mice: sedentary vs voluntary wheel vs treadmill (4 wk; n=12).
- Does training **up-regulate the mitochondrial programme** and raise specific force/respiration? (the 7 candidates are absent from the rat exercise epigenetic ladder — this directly fills that gap).

### Exp D — Therapeutic proof-of-concept (the muscle-quality tie-in; top-5% lever)
Aged mice, mass-matched design echoing the companion Perspective:
- Arm 1: biogenesis-restoring intervention (PGC-1α induction, or a clinical-grade
  15-PGDH inhibitor as the Perspective nominates) vs Arm 2: an anabolic comparator
  matched for mass gain vs Arm 3: vehicle.
- **Primary:** specific force / respiration at **equal or lesser mass gain** — does
  restoring the mitochondrial programme buy *function* the anabolic agent does not?
- This is the experiment that, if positive, supports both papers at once and is the
  natural Nature-Aging-tier result.

---

## 4. Decision gates

| Gate | Pass criterion | If fail |
|---|---|---|
| Aim 1 (protein) | Programme down at protein in ≥1 independent cohort | Re-examine; the discovery may be transcript-only — report honestly |
| Aim 2 (function) | ≥1 Tier-1/2 KD reduces OCR ≥20% **at matched CSA** | Effect is mass-linked, not quality — reframe |
| Exp B (in vivo) | Specific-force loss with CSA preserved (p<0.05) | Programme is a passenger, not a driver |
| Exp D (therapeutic) | Quality arm > anabolic arm on function at ≤ mass | Mitochondrial restoration insufficient alone |

---

## 5. What each result would (and would not) prove

- **Aim 1 positive** → the human signature is real at protein/function level (not a normalization artifact). Does *not* prove causation.
- **Aim 2 + Exp B positive** → the programme **causes** loss of mitochondrial function and muscle **quality**. The central mechanistic claim.
- **Exp C positive** → the programme is **modifiable** by exercise (translational handle; fills the WP5 gap).
- **Exp D positive** → restoring the programme delivers **function**, validating the muscle-quality thesis and nominating a therapeutic route. *This is the top-tier result.*
- **Honest null handling:** any arm can return null; each has an explicit refuter above, and a null on Exp B (force loss tracks mass, not quality) would be a publishable, hypothesis-correcting result.

---

## 6. Timeline & budget (indicative)

```
M1–4   In vitro Aims 1–2 (C2C12 + HSMM, Seahorse, force)
M3–6   Aim 3 (PGC-1α programme test + rescue); iPSC-CRISPR KO underway
M4–6   Exp A (aged-mouse observational)
M4–8   Exp B (AAV-shRNA, the quality experiment)
M5–8   Exp C (exercise reversal)
M8–14  Exp D (aged-mouse therapeutic mass-matched)
```
Estimated ~$120–160k over 14 months (siRNA/CRISPR, Seahorse, AAV production,
aged-mouse colony, single-fibre force rig time, RNA-seq, iPSC core, histology/TEM).

---

## 7. Statistics & rigor
- Biological n ≥ 3 independent differentiations (in vitro); blinded force/histology scoring.
- Seahorse normalized to protein; QC-gated wells.
- In vivo: mixed ANOVA (gene × treatment), effect sizes (Cohen's d), pre-registered SAP.
- RNA-seq: DESeq2, genome-wide BH-FDR.
- **Specific force (force/CSA) is the primary endpoint throughout** — the mass-vs-quality dissociation is the scientific spine, not an afterthought.
- All numbers from committed analysis scripts; no hand-computed values.

---

## 8. Publication strategy
| Paper | Content | Target |
|---|---|---|
| **Paper 1 (current, v0.4)** | HMSR mitochondrial-programme resource | GeroScience / npj Aging / JCSM (JCR 5–10%) |
| **Paper 2** | In vitro causation (Aims 1–3): programme → respiration/specific force | JCSM / Aging Cell |
| **Paper 3** | In vivo quality + therapeutic (Exp B+D), with the muscle-quality framing | Nature Aging / Cell Metabolism (top-5% target) |

*Plan v0.2 — basis: HMSR WP3/3b/3c/3d/3e outputs + the companion muscle-quality Perspective. The discovery paper supports candidate selection; only the experiments above can establish causation and function.*
