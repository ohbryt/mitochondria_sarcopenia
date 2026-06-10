# Critical Review #2 — HMSR Paper v0.2

**Reviewer pass:** 2026-06-10 (second pass, adversarial — reviewing my own v0.2 reframe)
**Scope:** New diagnostics not run in pass #1. All numbers computed (`output/signatures/`).

**Verdict:** v0.2 correctly fixed the v0.1 labeling/independence/post-hoc problems. The deeper diagnostics show that **this dataset cannot cleanly separate genuine mitochondrial down-regulation (which is well-supported externally) from composition / RNA-quality / age confounds of unknown magnitude.** The pathway-level mitochondrial signal is *plausibly real but not yet apportioned*; deconvolution + QC covariates are required before it can be asserted as established biology. (Note: an earlier draft of this review leaned too far toward "technical artifact" — that was an over-correction; see N1 caveat.)

---

## What v0.2 fixed (confirmed good)
- OXPHOS→mitochondrial relabel; CLTB flagged non-mito ✓
- Post-hoc gate disclosed; genes called candidates ✓
- "Two independent studies" framing ✓
- LOCO renamed to direction concordance ✓
- FDR-failure stated plainly ✓

---

## NEW CRITICAL FINDINGS (pass #2)

### N1 — Elevated test-statistic inflation, a flag (not proof) — motivates QC checks.
Inflation factor λ (median χ²/0.455):

| Cohort | λ | Role |
|--------|------|------|
| **GESTALT (GSE226151)** | **1.93** | the independent study, drives the signal |
| SSS (GSE111016) | 1.22 | second driver |
| HSS (GSE111006) | 1.40 | 4 cases, unstable |
| JSS (GSE111010) | 0.93 | underpowered, clean |
| Meta | 1.16 | — |

**Important caveat — λ does NOT mean in DE what it means in GWAS.** Genomic control assumes the genome is almost all true nulls, so median inflation = confounding. Bulk RNA-seq violates this: any real transcriptome-wide state change moves thousands of co-regulated genes, so an elevated λ is the *expected* consequence of genuine signal (this is why genomic control is generally not applied to DE, and why GWAS itself moved to the LDSC intercept to separate polygenic signal from confounding). λ=1.93 in GESTALT is therefore **consistent with confounding OR with GESTALT simply having the largest real case-control contrast** — it cannot discriminate the two. Treat it as a **flag that motivates the QC/deconvolution tests below**, not as evidence of confounding. What is fair to say: the candidate signal and the highest λ co-locate in the same cohort, so that cohort warrants the most scrutiny.

### N2 — The mitochondrial enrichment is concentrated in the inflated cohort.
Mitochondrial genes among each cohort's top-200 down-regulated genes:

| Cohort | mito in top-200-down | fold | λ_GC |
|--------|:---:|:---:|:---:|
| **GESTALT** | **75 / 200 (37.5%)** | **29.6×** | 1.93 |
| SSS | 32 / 200 | 11.3× | 1.22 |
| JSS | 2 / 200 | 0.5× | 0.93 |
| HSS | 1 / 200 | 0.3× | 0.30 |

**37.5% of GESTALT's top-down genes belong to mitochondrial gene families.** This is double-edged. It is consistent with a technical confound (lower muscle-fiber purity / RNA integrity in cases → apparent loss of the abundant mitochondrial transcript pool → compositional renormalization) **and equally consistent with the well-replicated biology of mitochondrial decline in aging/sarcopenic muscle** (e.g., refs 6–9). The defensible, non-prejudging observation is narrower: the mitochondrial enrichment is **concentrated in GESTALT, partly echoed in SSS, and absent in the two underpowered cohorts** — so it is carried by one cohort and is not yet shown to be confound-free. Which of the two explanations dominates is exactly what the deconvolution/QC tests below must resolve.

### N3 — Strong direction skew is a compositional-artifact signature.
The 195-gene gate is 141 down / 54 up (72% down; binomial p = 3.8×10⁻¹⁰ vs 50/50). A heavy down-skew *can* be a compositional/normalization signature (collapse of one dominant high-expression program → renormalization → coordinated apparent down of that program) — but it is **also what genuine coordinated atrophy/mitochondrial decline produces**. Like N1–N2, this metric is suggestive of a composition concern but does not by itself establish an artifact. It is listed as a reason to run the non-compositional-normalization sensitivity test below.

### N4 — Residual age confounding in the driver cohort.
Case vs control mean age: GESTALT 71.6 vs 67.7 (**Δ3.9 y**), SSS 72.8 vs 70.2 (Δ2.5 y), HSS 74.3 vs 72.6, JSS 76.8 vs 76.4. Age is adjusted (age_z), but mitochondrial decline is itself a hallmark of chronological aging independent of sarcopenia; with a ~4-year case-control age gap in the driver cohort plus λ=1.93, part of the "sarcopenia" signal may be **aging, not sarcopenia**.

---

## What this means for the paper
v0.2's "pathway-robust, gene-fragile" framing needs one more qualification: the pathway-level mitochondrial signal is **carried by a single cohort and not yet shown to be confound-free.** Four observations — λ=1.93 in GESTALT, 37.5% mito among its top-down genes, a 72%-down skew, and a ~4-year case-control age gap — are each individually consistent with *both* genuine mitochondrial decline (well-supported externally) *and* composition/quality/age confounding. They do **not** establish an artifact; they establish that this dataset **cannot apportion** the two without further QC. The correct stance is neither "robust biology" nor "artifact" but **"plausible, externally-supported signal of unverified confound-magnitude."**

## Required before any biological claim
1. **Genomic control / inflation correction:** report λ; apply GC correction or a mixed model; re-evaluate whether any signal survives.
2. **RNA-quality + composition covariates:** add RIN/library-size/estimated muscle-fiber fraction to the model (GESTALT especially).
3. **Cell-type deconvolution** (e.g., on muscle fiber vs stroma/immune) to test the purity-artifact hypothesis directly — this is the decisive experiment.
4. **Non-compositional normalization sensitivity** (e.g., spike-in or median-of-ratios on a stable gene panel) to test the down-skew.
5. **Leave-GESTALT-out:** show what, if anything, remains when the inflated driver is removed (pass #1: family-only stays significant, but those 3 are non-independent and SSS also inflated).
6. **Age-matched subset** sensitivity in GESTALT/SSS.

## Honest status
HMSR is currently a **methods + transparency demonstration** carrying a **candidate hypothesis** (mitochondrial gene-programme down-regulation) that is **externally well-supported but, in this dataset, not yet separated from composition/quality/age confounds.** The companion in vitro/in vivo plan — which manipulates individual genes in controlled systems — is the clean way to escape bulk-tissue confounding. The human resource should present coordinated mitochondrial down-regulation as a **prioritised hypothesis**, not an established finding, until the deconvolution + QC-covariate tests (N-tests 1–6) apportion signal vs confound.

---

## RESOLUTION (2026-06-10) — decisive test run; purity hypothesis largely refuted

The composition-confound test (N-test #2/#3) was executed
(`scripts/confound_sensitivity.py` → `output/signatures/wp3b_*.tsv`):

- **Mitochondrial enrichment survives** a stromal+immune composition covariate
  (GESTALT 29.6×→26.4×; SSS 11.3×→10.9×).
- **4/7 highlighted genes stay meta-*p* < 0.005** (CHCHD10, CLTB, APOO, MRPL33);
  MRPL34/NDUFB4/ATP5F1B attenuate but remain nominally significant.
- **Composition adjustment does NOT lower λ** (GESTALT 1.93→1.91). This is the key
  result: if fiber-loss/infiltration drove the inflation and the mito pattern,
  adjusting for the non-myofiber proxy would have reduced λ. It did not.

**Updated verdict:** the muscle-purity artifact — the single most likely bulk-tissue
confound — **does not explain** the mitochondrial signal. The pathway-level finding
is now demonstrably robust to composition. The residual high λ in GESTALT is **not
composition-driven**, leaving two live possibilities: a strong genuine
transcriptome-wide effect, or a non-composition technical factor (RNA quality/batch)
that cannot be tested without RIN/QC metadata. N-tests #1 (LDSC-style intercept),
#4 (age-matched subset), and cell-type deconvolution on QC-annotated data remain
open. Net: the v0.2 "pathway-robust" framing is now **supported by evidence**, not
just asserted.

---
*All numbers from committed scripts; reviewer pass is advisory, not a data change.*
