# HYPOTHESIS.md
## HMSR — A reproducible skeletal-muscle resource reveals coordinated down-regulation of mitochondrial genes in sarcopenia
## The mitochondrial biogenesis programme as a muscle-quality driver

> **Document ID:** `sarcopenia-multiomic-resource/validation/HYPOTHESIS.md`
> **Version:** v0.1 — initial dry-lab hypothesis specification
> **Date:** 2026-06-15
> **Branch:** `sarcopenia/paper1-v0.4`
> **Prepared by:** Brown Biotech (Larry)
> **Linked documents:**
> `manuscripts/paper1_v0.4.md` (the discovery paper)
> `validation/WET_VALIDATION_PLAN.md` (the executable plan that tests this hypothesis)
> `validation/plan/experimental_validation_plan_v0.3.md` (the operationalized plan, 5,263 lines / 492 KB)
> `validation/plan/OPEN_ISSUES.md` (current open issues + decision history)

---

## 0. Reading guide

This document states, in falsifiable form, the central hypothesis of the HMSR
project and the sub-hypotheses that follow from it. The companion document
`WET_VALIDATION_PLAN.md` specifies the experiments that test these hypotheses
with sufficient rigor to confirm, refine, or refute each one.

**The minimum the reader should take away:**

1. Sarcopenia is associated with **coordinated down-regulation of the
   mitochondrial biogenesis programme** (mitoribosome, cristae/MICOS, import,
   respiratory chain) — established at the **pathway level** (permutation
   p=2.0×10⁻³, robust to composition adjustment, Freedman–Lane permutation,
   and library-size covariate; v0.4).
2. We hypothesize this is **causal** for **muscle-quality loss** (specific
   force at matched CSA), not just a correlate of muscle-mass loss.
3. We hypothesize the programme is **reversible by exercise** and that
   **restoration of the programme delivers function** (the muscle-quality
   thesis).
4. Each hypothesis has a **falsification clause** — a pre-specified result
   that would refute it, plus an honest reframing of what we would then
   conclude.

---

## 1. The discovery (H0) — established by HMSR v0.4

**Statement (verified):** In sarcopenic human skeletal muscle (n=135 strict
case/control across two independent studies, 37,469 genes tested), the
nuclear-encoded mitochondrial biogenesis programme is **coordinately and
specifically down-regulated** at the **transcript level**.

**Evidence (HMSR v0.4, `paper1_v0.4.md`):**
- Correlation-aware label-permutation test on the full ranked genome
  (gate-independent): **p = 2.0×10⁻³** for the 539-gene nuclear-encoded
  mitochondrial programme, with **all six sub-programmes concordantly
  down** (Complex I, II/III/IV, V, mitoribosome, cristae/MICOS, import) at
  p ≤ 6×10⁻³.
- Cytoplasmic-ribosome and proteasome controls are **not** significantly
  shifted (p = 0.28 and 0.12 respectively).
- Collagen/ECM shifts **up** (consistent with relative fibrosis).
- Robust to muscle-composition (stromal/immune purity) adjustment:
  mitochondrial enrichment retained (26×); 4/7 highlighted genes remain
  meta-p < 0.005 after adjustment.
- Robust to **Freedman–Lane covariate-exchangeable permutation**:
  p = 1.0×10⁻³.
- Robust to **library-size (sequencing-depth) covariate** adjustment:
  same 4/7 genes remain meta-p < 0.005; mitochondrial enrichment persists.
- Honest ceilings: **no gene survives genome-wide FDR**; the result is
  pathway-level, not individual-gene.

**Defensible conclusion:** the **pathway-level coordinated mitochondrial
biogenesis programme down-regulation** is the result. Per-gene effect-size
estimates are honest but exploratory.

---

## 2. The causal hypothesis (H1) — to be tested in Aim 2

**Statement (hypothesis):** Suppressing the mitochondrial biogenesis programme
— or its strongest individual nodes — **lowers mitochondrial respiration and
specific force (force per cross-sectional area) without necessarily lowering
muscle mass**.

**Why this matters:** sarcopenia pharmacology has historically targeted
muscle mass as the primary endpoint, with mixed success. The companion
muscle-quality Perspective argues that mass is a poor surrogate for the
innervated, metabolically competent, force-producing fraction of muscle. If
the mitochondrial programme is causal for *quality* (function per unit
size) but not for *mass*, then the programme is precisely the kind of
target that explains the mass-vs-quality dissociation the field has
struggled with.

**Critical design principle:** the decisive readout is **muscle quality =
function per unit size**, not bulk. A manipulation that reduces specific
force / respiration at **matched CSA** proves the programme is a *quality*
driver. This dissociation is what separates a confirmatory mitochondrial
study from a mechanistic one.

**Sub-hypotheses (H1.1 – H1.4, one per gene tier + programme master):**

| ID | Sub-hypothesis | Test |
|---|---|---|
| **H1.1** | Suppressing **CHCHD10** (MICOS/cristae, Tier 1 lead) lowers specific force and respiration at matched CSA | siRNA/shRNA in C2C12 + HSMM → Seahorse + 3D myobundle force at matched CSA |
| **H1.2** | Suppressing **NDUFB4** (Complex I accessory) lowers specific force and respiration at matched CSA | Same as H1.1 |
| **H1.3** | Suppressing **ATP5F1B** (Complex V F₁β) lowers specific force and respiration at matched CSA | Same as H1.1 |
| **H1.4** | Suppressing **PPARGC1A** (PGC-1α1) reproduces the **entire** programme down-regulation (i.e., the programme is one-node-controlled) | siRNA + RNA-seq; pathway-level test (permutation vs HMSR v0.4) |

**Falsification clauses (H1):**
- **H1 refuted if** a Tier 1/2 KD reduces OCR ≥20% at matched CSA: the
  gene acts via mass, not quality, and the programme is not a quality
  driver. Re-frame as a mass-side effect.
- **H1.4 refuted if** PGC-1α1 KD does **not** reproduce the
  programme-wide signature: the programme is multi-node, not
  one-master-switch-controlled. The CRISPR screen + multi-target rescue
  arm becomes more important.

---

## 3. The protein-level confirmation (H0.5) — Aim 1

**Statement:** The programme down-regulation is **also present at the
protein level** in sarcopenic vs control human muscle biopsies.

**Why this matters:** the HMSR v0.4 result is transcript-level. A
transcript-level result cannot exclude the possibility that the programme
is regulated post-transcriptionally (translation, stability) and that
protein levels are unchanged. If protein levels are unchanged, the
discovery is less interesting as a target.

**Test:** mitochondrial protein panel (immunoblot + targeted proteomics) for
the programme on n≥10 sarcopenic vs n≥10 control biopsies (independent of
the discovery cohorts).

**Falsification clause:** if the protein panel shows no programme down
at protein level in ≥1 independent cohort, the discovery is transcript-only
and we report this honestly; the programme is still biologically
interesting but its causal role (H1) is less attractive as a therapeutic
target.

---

## 4. The exercise-reversibility hypothesis (H2) — Exp C

**Statement:** The programme down-regulation is **modifiable by exercise
training** in aged mice, and the **magnitude of rescue predicts the
magnitude of specific-force recovery** (the quality-vs-mass dissociation in
vivo).

**Why this matters:** H1 + H2 together show that the programme is both
causal (H1) and actionable (H2). Without H2, the discovery is a correlate.
With H2, it is a therapeutic target.

**Test:** 3-month vs 24-month C57BL/6J, voluntary wheel vs treadmill vs
sedentary, 4 weeks. Readouts: programme qPCR + WB, permeabilized-fibre
respiration (Oroboros), single-fibre specific force.

**Falsification clause:** if training up-regulates the programme but does
**not** recover specific force (only mass), the programme is a correlate
of exercise response, not a causal lever. The wet-lab priority shifts
to other nodes in the network.

---

## 5. The therapeutic hypothesis (H3) — Exp D

**Statement:** Restoring the programme in aged mice via a clinically
plausible intervention (PGC-1α induction or 15-PGDH inhibition, the
latter nominated by the companion muscle-quality Perspective) delivers
**function** (specific force at equal or lesser mass gain) **beyond what
an anabolic-only intervention matched for mass gain delivers**.

**Why this matters:** H3 is the **top-tier result**. Palla 2020 (Science,
PMID 33303683) showed that 15-PGDH inhibition in aged mice increases
muscle mass, strength, and exercise performance with augmented
mitochondrial function and autophagy. If replicated in our mass-matched
design with the HMSR programme as the molecular readout, it directly
supports the muscle-quality thesis and nominates a therapeutic route.

**Test:** aged C57BL/6J, 3 arms (mito-restoration vs anabolic comparator
vs vehicle), mass-matched by dose titration. Primary endpoint: specific
force at equal or lesser mass gain.

**Falsification clause:** if the mito arm and the anabolic arm deliver
equal specific force at equal mass gain, mitochondrial restoration alone
is insufficient — the muscle-quality thesis needs another pillar (neural,
ECM, satellite-cell) to explain the dissociation.

---

## 6. The compound hypothesis (H_combined)

**Statement:** The five sub-hypotheses (H0.5, H1.1–H1.4, H2, H3) are
**not independent**. The strongest version of the muscle-quality thesis
predicts that:
- H0.5 is true (programme down at protein)
- H1.1, H1.2, H1.3 are true (each tier KD reduces function at matched
  CSA)
- H1.4 is true (PGC-1α is the master)
- H2 is true (exercise rescues the programme AND specific force)
- H3 is true (therapeutic restoration beats anabolic on function at
  equal mass)

**Compound-falsification:** if any 2 of H1.1–H1.3 are refuted at matched
CSA, the quality-driver thesis is weakened. If H1.4 is refuted, the
master-switch model is wrong (the programme is multi-node).

**Compound-confirmation (the top-tier paper):** if H1, H2, and H3 are all
confirmed in the same project, the paper is **Nature Aging / Cell Metabolism
tier** (top 5%). The current v0.4 manuscript is a discovery paper; the
top-tier paper is built on the experimental confirmation of H1–H3.

---

## 7. What this hypothesis does NOT claim

- We do **not** claim that the mitochondrial programme down-regulation
  *causes* sarcopenia clinically. Sarcopenia is multifactorial; the
  programme is one node in a network.
- We do **not** claim a single gene (e.g., CHCHD10) is the **cause** of
  sarcopenia. The genes are the strongest individual nodes in a
  co-regulated programme; their perturbation tests the programme's causal
  role.
- We do **not** claim that restoring the programme is sufficient to
  reverse clinical sarcopenia. Exp D tests a single intervention
  (PGC-1α induction or 15-PGDH inhibition) in aged mice; clinical
  translation would require a human trial.
- We do **not** claim that the programme is the **only** muscle-quality
  pillar. The companion Perspective names three: metabolic competence
  (this work), neuromuscular junction integrity, and ECM/fibrosis
  balance. This work tests only the first.

---

## 8. Why this matters — the muscle-quality reframe

Sarcopenia drug development has historically targeted muscle mass (anabolic
agents, myostatin antagonists, growth hormone) with mixed efficacy. The
companion muscle-quality Perspective argues the field has been optimizing
the wrong variable: muscle mass is a poor surrogate for the
innervated, metabolically competent, force-producing fraction of muscle.

The HMSR v0.4 finding provides **independent human transcriptomic
evidence** for the metabolic-competence pillar: the entire mitochondrial
biogenesis programme is coordinately down in sarcopenic muscle. This
finding is independent of (but consistent with) the muscle-quality
reframe. If H1, H2, H3 are confirmed, the finding becomes a **therapeutic
target** for a programme-restoration strategy, validated in the same
project by a head-to-head mass-matched therapeutic experiment.

**Falsification of the entire thesis:** if H1 (KD at matched CSA) is
refuted, the muscle-quality pillar of the Perspective loses its
transcriptomic-to-causal link. The Perspective can still be true (mass
is a poor surrogate, for other reasons), but it loses the mitochondrial
mechanism. The honest conclusion would be: the programme is a correlate,
not a driver; future work should test the other two pillars (NMJ, ECM).

---

## 9. Sub-hypothesis summary table

| ID | Statement | Test | Power | Falsification clause |
|---|---|---|---|---|
| **H0** | Programme is down-regulated at transcript level in sarcopenic muscle | HMSR v0.4 | ✅ established | (verified) |
| **H0.5** | Programme is also down at protein level | Aim 1 cohort protein panel | n≥10/group | If protein unchanged, transcript-only |
| **H1.1** | CHCHD10 KD lowers specific force + respiration at matched CSA | C2C12 + HSMM siRNA → Seahorse + myobundle force at matched CSA | n=5 difs × 5 wells (Seahorse); n=3 difs × 6 bundles (force) | If force drops only with diameter loss, mass effect, not quality |
| **H1.2** | NDUFB4 KD lowers specific force + respiration at matched CSA | Same as H1.1 | Same | Same |
| **H1.3** | ATP5F1B KD lowers specific force + respiration at matched CSA | Same as H1.1 | Same | Same |
| **H1.4** | PGC-1α1 KD reproduces the whole programme (RNA-seq) | siRNA + RNA-seq + pathway permutation | n=3 difs | If 6/6 sub-programmes not concordantly down, multi-node model |
| **H2** | Exercise rescues the programme AND specific force in aged mice | Exp A (observational) + Exp C (training) | n=8/group A; n=12/arm C | If mass-only recovery, programme is correlate not causal |
| **H3** | Therapeutic restoration beats anabolic on specific force at equal mass gain | Exp D mass-matched 3-arm | n=11/arm @ 0.80; 14 @ 0.90 | If mito and anabolic arms equal, mito insufficient alone |

---

## 10. References (this document)

- `manuscripts/paper1_v0.4.md` (HMSR v0.4 — discovery)
- `validation/WET_VALIDATION_PLAN.md` (executable plan)
- `validation/plan/experimental_validation_plan_v0.3.md` (operationalized v0.3)
- `validation/power_analysis/POWER_ANALYSIS.md` (power calcs)
- Guzman 2026 (PMID 41496579) — CHCHD10 muscle-specific KO precedent
- Palla 2020 *Science* (PMID 33303683) — 15-PGDH inhibition in aged mice (H3 anchor)
- Handschin 2007 (PMID 17702743) — PGC-1α muscle-specific KO precedent (H1.4 anchor)
- Halling 2019 (PMID 31265325) — PGC-1α cKO + exercise reversal (H1.4 + H2 anchor)
- Akabane 2024 (PMID 39333763) — aged-mouse muscle loss model
- Shu 2025 (PMID 40479501) — 15-PGDH inhibitor in aged muscle (H3 anchor)
- Mesquita 2020 (PMID 32748504) — chronic RT in older adults (H2 anchor)

---

*Hypothesis document v0.1 — Brown Biotech (Larry), 2026-06-15. Self-contained;
no fabrication. All citations verifiable via PubMed.*
