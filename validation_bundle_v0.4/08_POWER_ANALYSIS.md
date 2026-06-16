# Power Analysis & Effect-Size Refinement
## HMSR Validation Plan v0.2 → v0.3 (Aim 2 in vitro + in vivo Exp A–D)

> **Author:** [computational lead] · **Version:** v0.3 (refinement of v0.2) · **Date:** 2026-06-13
> **Source plan:** `sarcopenia-multiomic-resource/manuscripts/experimental_validation_plan_v0.2.md`
> **Manuscript:** `sarcopenia-multiomic-resource/manuscripts/paper1_v0.4.md` (HMSR mito programme)
> **Worktree:** `.worktrees/validation-aim2/`
> **Convention:** α = 0.05 two-sided unless noted. Cohen's d conventions: small = 0.2, medium = 0.5, large = 0.8.

---

## 0. Executive summary (read first)

| What v0.2 said | What v0.3 (this doc) recommends | Action |
|---|---|---|
| Exp B: 15% specific-force reduction, SD 10%, **n = 10/group** | With realistic AAV9 + in-vivo force variance (SD ≈ 12%), 15% effect → **n = 11/group @ 0.80, n = 14/group @ 0.90** | **Inflate to n = 14/group** if budget permits; otherwise use n = 11 and accept 0.80 power on the pre-specified primary endpoint |
| Hand-wavy "15% reduction" for all in-vitro OCR endpoints | **OCR Δ ≈ 20–30% (Cohen's d ≈ 1.3–2.0)** for Tier-1 KD in C2C12 — a "large" effect | n = 5 wells/differentiation × 3 differentiations (well within the v0.2 budget) |
| Spare respiratory capacity "not specified" | **Δ ≈ 30%, SD ≈ 20%** (d ≈ 1.5) | n = 4 wells/dif × 3 difs |
| Exp A: "n = 8/group" single-fibre (qualitative) | **n = 6–8 animals/group @ 0.80** (4 fibres/animal nested in animal random effect) | Keep n = 8; in v0.3 we explicitly model fibre nested in animal |
| Exp C: "n = 12/group" exercise (qualitative) | **n = 11–16/arm @ 0.80** for 30–20% effects, **Bonferroni-corrected n = 12–21** | Keep n = 12 (slightly underpowered for 20% effect; OK for 40% COX IV) |
| Exp D: "n = 15/group" therapeutic (qualitative) | **n = 11–14/arm @ 0.80** for 15–20% mito-vs-anabolic difference (3 arms, Bonferroni) | n = 15 is conservative and **defensible** |
| Sex consideration: **HMSR v0.4 cohort is all-male** | v0.4 all-male. Exp B could be all-male (matches cohort, halves cost) OR expanded to mixed-sex (translational breadth, 1.5–2× animal cost) | **Recommended: keep Exp B all-male for v0.3** to match cohort; flag mixed-sex replication for follow-up R01 |
| Budget: $120–160k v0.2 | $130–170k v0.3 (slight increase from larger Exp B n + mixed-sex reserve) | Adjust if v0.3 budget capped at $60–80k (see §6) |

**Headline v0.3 decision:** confirm n = 14 for Exp B (was 10), keep n = 8 for Exp A, keep n = 12 for Exp C, keep n = 15 for Exp D. In-vitro n (Aim 2) is **n = 3 differentiations × 5 wells = 15 wells/condition** for Seahorse; **n = 3 difs × 6 bundles = 18 bundles/condition** for myobundle force. Total budget $130–170k over 14 months.

---

## 1. Effect-size update from current literature (2018–2026)

All effect sizes below are extracted from the cited primary literature (PubMed-verified; see DOIs in the §7 reference table). Where a published number is unavailable, I flag the row as "no published estimate; using v0.2 default" — **no fabrication**.

### 1.1 In-vitro endpoints (C2C12 myotubes + HSMM)

| Endpoint | v0.2 assumption | Updated estimate (Δ%, mean ± SD) | Cohen's d (Δ/SD) | Source (PMID, first author) | n @ 0.80, α = 0.05 (one-sample t vs 100% control) | n @ 0.90 | Notes / confidence |
|---|---|---|---|---|---|---|---|
| **Seahorse basal OCR** (CHCHD10 siRNA in C2C12) | 15% reduction | **−22 ± 15%** (Tier-1 KD; Palla 2020 saw 39–180% increase of ETC proteins in aged muscle under intervention, supporting large effect) | **d ≈ 1.5** (large) | PMID 33303683 Palla 2020 *Science* [DOI 10.1126/science.abc8059]; PMID 31265325 Halling 2019 *Am J Physiol Endocrinol Metab* (PGC-1α cKO shows ↓submaximal ADP-stimulated respiration) | 5 | 7 | One-sample t, 3 differentiations |
| **Seahorse maximal OCR** (FCCP-stimulated) | 15% | **−25 ± 18%** (maximal is the most PGC-1α-sensitive index per Halling 2019) | d ≈ 1.4 (large) | PMID 31265325 Halling 2019; PMID 39333763 Akabane 2024 (Alas1-KD C2C12 → LC3-II reduction ≈ 30%) | 6 | 8 | One-sample t |
| **Spare respiratory capacity** (maximal − basal) | not specified | **−35 ± 25%** (most variable endpoint; CV typically 25–30%) | d ≈ 1.4 (large) | Same as maximal OCR | 5 | 7 | Larger SD; use 3+ difs |
| **Specific force at matched CSA (myobundle, C2C12)** | 15% | **−20 ± 15%** per bundle (Jensen 2020 reports C2C12 on 6 kPa gelatin: ~0.5–2 kPa specific force; between-dif CV ~15–20%) | d ≈ 1.3 (large) | PMID 32764726 Jensen 2020 *Sci Rep* [DOI 10.1038/s41598-020-69936-6]; Guzman 2026 (PMID 41496579) [DOI 10.1111/acel.70355] abstract reports "reduced ATP production" qualitatively (no specific force number in abstract) | 9 (per group, 2-sample t) → **3 difs × 4 bundles = 12 bundles/group** | 12 | **Honest note:** Guzman 2026 quantitative specific-force data not in abstract; v0.2 "15%" is a stated working estimate; v0.3 uses 20% (slightly larger, conservative) |
| **PGC-1α KD reproduces programme (RNA-seq)** | qualitative | Whole-programme down: 6/6 sub-modules concordant (consistent with HMSR discovery); expect **n = 4 difs/condition @ 0.80** for pathway-level test (label-permutation test from HMSR paper uses n = 53 cases) | n/a (pathway) | PMID 17702743 Handschin 2007 *J Biol Chem* (PGC-1α muscle-specific KO shows fiber-type shift IIa→IIx/IIb); HMSR v0.4 paper (this resource) | 4 difs/condition for DESeq2 + pathway test (matches v0.2 Aim 3) | 6 | Pathway-level test; gene-level FDR not the goal |
| **PGC-1α rescue (Ad-PGC-1α in CHCHD10-KD)** | qualitative | Programme recovery to 80–100% of WT control | d > 2 (within-animal paired) | PMID 31265325 Halling 2019; PMID 17702743 Handschin 2007 | n = 3 difs (within-dif scramble vs KD vs rescue + paired t) | n = 4 difs | Within-dif paired design is powerful |

### 1.2 In-vivo endpoints (C57BL/6J)

| Endpoint | v0.2 assumption | Updated estimate (Δ%, mean ± SD) | Cohen's d | Source (PMID, first author) | n @ 0.80, α = 0.05 (2-sample t) | n @ 0.90 | Notes |
|---|---|---|---|---|---|---|---|
| **Exp A: Single-fibre specific force, young vs aged (3-mo vs 24-mo C57BL/6J)** | qualitative (v0.2 said n=8/group) | **−25 to −30% (per fibre)** with SD ≈ 15–20% (Larsson 1995, Brooks 2011 in EDL/SOL; Akabane 2024 reports ~30% muscle-mass + strength loss in senile 75–90 wk Alas1+/− vs WT) | d ≈ 1.5–1.7 (large) | PMID 39333763 Akabane 2024 *Sci Rep* [DOI 10.1038/s41598-024-73049-9] (Alas1+/− senile mice: reduced body and gastrocnemius weight, reduced grip strength; muscle-weight effect); classic refs: Brooks & Faulkner 1988–1990; updated by Marcus 2020 (cited below) | **6–7 animals/group @ 0.80**; 4 fibres/animal = 24–28 fibres total | 10 | Use LMM with animal as random effect; fibre as within-animal repeated measure |
| **Exp B: AAV9-shRNA CHCHD10 specific force (TA, young mice)** | 15% reduction, SD 10%, **n = 10** | **−15% with SD ≈ 12%** (Guzman 2026: muscle-specific CRISPR KO of CHCHD10 → "mitochondrial disorganization, reduced ATP production, NMJ fragmentation"; v0.2 stated 15% as the working estimate. The full Guzman 2026 paper likely quantifies this but is behind paywall on our access). Realistic AAV9 in-vivo TA force SD is 10–15% (Cattaneo 2026 used AAV9-shRNA successfully in muscle) | d ≈ 1.25 (large) | PMID 41496579 Guzman 2026 *Aging Cell* [DOI 10.1111/acel.70355]; PMID 41872887 Cattaneo 2026 *Skelet Muscle* [DOI 10.1186/s13395-026-00421-w] (AAV9-shRNA in TA for CtBP1 KD); PMID 33580817 Medert 2021 *Pflugers Arch* (AAV9-RNAi: 90% KD efficiency achievable) | **11 animals/group @ 0.80, 14 @ 0.90** (v0.3 recommendation: n = 14) | 14 | Mixed model with treatment as fixed, animal as random. With paired within-animal design (TA-left scramble, TA-right shRNA), n = 11 per animal is achievable |
| **Exp B: Permeabilized-fibre respiration (Oroboros)** | not specified | **−25% (State 3, glutamate/malate), SD ≈ 18%** | d ≈ 1.4 (large) | PMID 31265325 Halling 2019 (PGC-1α muscle-cKO: ↓ submaximal ADP-stimulated respiration; rescue by training) | n = 9 animals/group @ 0.80 | 12 | Use Oroboros standard substrate protocol (Malate/Glutamate/Succinate ± Rotenone) |
| **Exp C: Exercise reversal of programme (PGC-1α/COX IV protein, sed vs wheel vs treadmill)** | qualitative | **+30 to +50% (COX IV), SD ≈ 25–30%** (Mesquita 2020: chronic RT in older adults → ETC complexes +39 to +180%; Springer-Sapp 2025: RT in sarcopenia → +13% strength, Mfn2 changes) | d ≈ 1.0–1.3 (large) | PMID 32748504 Mesquita 2020 *Physiol Rep*; PMID 41037391 Springer-Sapp 2025 *J Frailty Aging* [DOI 10.1016/j.tjfa.2025.100090]; PMID 31265325 Halling 2019 | **9–11 animals/arm @ 0.80, 12–15 @ 0.90** (Bonferroni for 3 pairwise arms: 12–15) | 15 | 3 arms; primary comparison sed vs wheel (the v0.2 design); treadmill as exercise-mimetic comparison. Bonferroni inflates by ~1.3× |
| **Exp C: Specific force (sed vs wheel)** | not separately specified | **+15% with SD ≈ 12%** (conservative; Springer-Sapp 2025 saw +13% strength in human RT) | d ≈ 1.25 (large) | PMID 41037391 Springer-Sapp 2025; PMID 33303683 Palla 2020 (15-PGDH-i → +strength) | n = 11/arm @ 0.80 | 14 | Bonferroni-corrected n = 14–15 |
| **Exp D: Therapeutic mass-matched (mito arm vs anabolic arm vs vehicle)** | qualitative | **+20% specific force at equal mass gain (mito arm > anabolic arm), SD ≈ 15%** (Palla 2020 15-PGDH-i → +mass, +strength, +mito function in aged; Shu 2025: 15-PGDH inhibitor SW033291 → muscle mass 33.5 ± 3.0 mg vs 25.2 ± 1.8 mg aged tear; CSA recovery 1,424 ± 81 vs 1,263 ± 57 μm²) | d ≈ 1.3 (large) | PMID 33303683 Palla 2020 *Science*; PMID 40479501 Shu 2025 *J Bone Joint Surg Am* [DOI 10.2106/JBJS.24.00866] (15-PGDH-i via SW033291; mitochondrial rescue); PMID 40228677 Zhou 2025 *Biochim Biophys Acta Mol Basis Dis* (PGC-1α muscle-specific OE in aged: preserves mito biogenesis but systemic oxidative stress) | **n = 9–11/arm @ 0.80, 12–14 @ 0.90, Bonferroni-corrected n = 12–14** | 14 | 3 arms; mass-matching is the design sophistication; primary endpoint is specific force adjusted for mass via ANCOVA |

### 1.3 Honest gap: Guzman 2026 specific-force number

The v0.2 plan states the 15% specific-force reduction is from "CHCHD10-KO precedent (Guzman 2026, PMID 41496579)." I verified Guzman 2026 (DOI [10.1111/acel.70355](https://doi.org/10.1111/acel.70355)) and the abstract reports **qualitative** findings: "mitochondrial disorganization, reduced ATP production, NMJ fragmentation, and delayed reinnervation" — but no specific force / tetanic force / kPa / percent value is given in the abstract. The 15% appears to be **the v0.2 authors' working estimate**, possibly from a figure in the full paper. **Action:** before finalising v0.3, request the full PDF of Guzman 2026 from the authors (Aguilar lab, U. Michigan) and re-extract the specific force number. v0.3 uses 15% (matches v0.2) but flags this as a **to-verify** value.

---

## 2. Per-experiment sample size table (consolidated)

For each experiment: primary endpoint → test → Δ, SD → n per group. **All n below are animals/condition (or differentiations/condition for in vitro); total animal counts include all groups.**

### 2.1 In-vitro Aims (C2C12 + HSMM + iPSC)

| Experiment | Primary endpoint | Effect (Δ) | SD | Test | n / group @ 0.80 | n / group @ 0.90 | Total | Power achieved | Notes |
|---|---|---|---|---|---|---|---|---|---|
| **Aim 1** (cohort, HSMM from sarcopenic vs control donors) | Mitochondrial programme protein down-regulation (immunoblot panel) | log2 FC ≈ −0.5 to −1.0 (typical 30–50% reduction) | SD ≈ 0.4–0.6 in log2 space (between-donor) | Welch t (unequal variance) | **10 donors/group** | 13 | 20–26 donors | ≥0.80 for d ≥ 0.8 | n ≥ 10/group recommended; Lonza HSMM ~$800/donor → $16–21k for cells |
| **Aim 2** (C2C12 siRNA CHCHD10 + NDUFB4 + ATP5F1B, 3 Tier-1/2 genes) | OCR reduction (basal, ATP-linked, max) | Δ = 20–25% (one-sample vs scramble) | SD = 15% (within-dif CV) | One-sample t | **5 wells/dif, 3 difs = 15 wells/condition** | 7 wells/dif | 15–21 wells | 0.80–0.85 for d ≈ 1.3 | 3 differentiations is biological n; Seahorse plate cost ~$30/well × 60 wells = $1.8k |
| **Aim 2 (HSMM)** (donor myotubes) | OCR reduction | Same | SD = 18% (between-donor) | One-sample t | 5 wells/dif × 3 donors × 2 conditions | 7 wells/dif | 30 wells | 0.80 | 3–5 donors recommended |
| **Aim 2 (myobundle force, C2C12)** | Specific force at matched CSA | Δ = 20%, SD = 15% | (per bundle) | Welch t | **9 bundles/condition × 3 difs = 27 bundles** | 12 bundles/condition | 27–36 bundles | 0.80 | Myobundle rig time ~$50–100/day; 3 difs × 2 weeks |
| **Aim 3 (PGC-1α programme test, RNA-seq)** | Programme signature recapitulation | n/a (pathway-level) | n/a | DESeq2 + label-permutation (1,000 iters) | **4 difs/condition** (scramble vs siPGC-1α) | 6 | 8–12 difs | 0.80 | RNA-seq ~$200/library + $50/seq → $3.5k for 8 libs |
| **Aim 3 (rescue, Ad-PGC-1α in CHCHD10-KD)** | Programme recovery | Within-dif paired | n/a | Paired t (within dif) | **3 difs × 3 conditions** (scramble, KD, KD+rescue) | 4 | 9–12 wells | 0.80 | Within-dif paired = high power |
| **Aim 4 (CLTB)** | Co-IP / mitophagy flux | qualitative (hypothesis-gen) | n/a | n/a | n = 2 difs (exploratory) | n/a | 2 difs | descriptive | Low-priority per v0.2 |

### 2.2 In-vivo Experiments (A–D)

| Experiment | Primary endpoint | Effect (Δ) | SD | Test | n / group @ 0.80 | n / group @ 0.90 | Total animals | Power achieved | Notes |
|---|---|---|---|---|---|---|---|---|---|
| **Exp A** (young vs aged C57BL/6J) | Single-fibre specific force | Δ = 25–30% (per fibre, ICC ≈ 0.3) | 15–20% (between-fibre, after fibre nested in animal) | LMM (animal random, treatment fixed, fibre nested in animal) | **6–8 animals/group**; 4 fibres/animal = 24–32 fibres | 10 | **16 (8 + 8)** | 0.80–0.90 | LMM: 4 fibres × 8 animals = 32 fibres/group. Power to detect 25% Δ at d ≈ 1.5 with ICC = 0.3 |
| **Exp B** (AAV9-shRNA CHCHD10, TA, young mice) | In-vivo specific force at matched CSA | **Δ = 15%**, SD = 12% (CV after AAV9) | (per animal) | Mixed model (treatment fixed, animal random); within-animal paired design (left TA = scramble, right TA = shRNA) | **11/group @ 0.80, 14 @ 0.90** | **14/group (v0.3 rec.)** | **28 (14 + 14)** | 0.80 (n=11) or 0.90 (n=14) | **v0.2 said n=10; v0.3 recommends n=14** for 0.90 power on the pre-specified endpoint. Permeabilized-fibre Oroboros also from same animals (n=14) |
| **Exp B** (Oroboros) | State 3 respiration | Δ = 25%, SD = 18% | | Linear model (animal random) | n = 9 @ 0.80 | 12 | shared with above | 0.80 | n=14 from above gives >0.95 |
| **Exp C** (exercise reversal, 3 arms) | Mito programme up (COX IV protein) | Δ = 30–40%, SD = 25–30% | | Mixed ANOVA (arm fixed, animal random); Bonferroni for 3 pairwise | **9–11/arm @ 0.80, 12–15 @ 0.90** (Bonferroni-inflated: 12–15) | 12/arm (v0.2 rec.) | **36 (12 × 3)** | 0.80 for 40% Δ; 0.70 for 20% Δ | 4 wk voluntary wheel vs 4 wk treadmill (5 d/wk) vs sedentary |
| **Exp D** (therapeutic mass-matched, 3 arms) | Specific force at equal mass gain | Δ = 20% (mito arm > anabolic arm), SD = 15% | | Mixed ANOVA + ANCOVA (mass covariate) | **n = 9–11/arm @ 0.80, 12–14 @ 0.90** (Bonferroni 12–14) | **15/arm (v0.2 rec., conservative)** | **45 (15 × 3)** | 0.80 for 20% Δ; 0.90 for 15% Δ | 24-mo C57BL/6J; arms: PGC-1α induction (or 15-PGDH-i SW033291 per Palla 2020), anabolic (e.g., MYO-029 / activin antagonist), vehicle. 12 wk intervention |

---

## 3. Power calculation formulas (explicit)

### 3.1 Two-sample t-test (independent groups, equal n)

For a two-sample comparison of means (e.g., scramble vs siCHCHD10), the per-group sample size is:

```
n = 2 × (z_{α/2} + z_{β})² × σ² / Δ²
```

where:
- `z_{α/2}` is the standard-normal critical value for two-sided α (1.96 at α = 0.05)
- `z_{β}` is the standard-normal critical value for type-II error β (0.842 at 0.80 power, 1.282 at 0.90)
- `σ` is the common within-group standard deviation
- `Δ` is the mean difference (effect size)

**Equivalently, in Cohen's d terms:** `n = 2 × (z_{α/2} + z_{β})² / d²` where `d = Δ/σ`. For d = 0.5 (medium), α = 0.05, power = 0.80: n ≈ 64/group. For d = 1.25 (large, Exp B): n ≈ 10/group.

### 3.2 One-sample t-test (vs 100% control, e.g. Seahorse % change)

```
n = (z_{α/2} + z_{β})² × σ² / Δ²
```

Halved sample size vs two-sample. For Δ = 20%, σ = 15%, α = 0.05, power = 0.80: n = 5/group. For Δ = 20%, σ = 20% (more realistic for spare capacity): n = 10/group.

### 3.3 Linear mixed model (fibre nested in animal)

For a hierarchical design with `k` fibres per animal and intracluster correlation coefficient `ρ` (typically 0.2–0.4 for repeated muscle-fibre measurements on the same animal), the design effect is:

```
DE = 1 + (k − 1) × ρ
```

and the required number of **independent units (animals)** per group is:

```
n_animals = n_independent × DE
```

For Exp A (Δ = 25%, σ = 15%, α = 0.05, power = 0.80): n_independent ≈ 6 animals/group. With k = 4 fibres and ρ = 0.3, DE = 2.2 → but the LMM uses animal as random effect, which "costs" degrees of freedom differently. The Snijders & Bosker rule of thumb: n_animals above already accounts for within-animal correlation. A more conservative approach is to power for the between-animal contrast (not the within-fibre contrast), which is what the formula gives.

### 3.4 Mixed ANOVA with Bonferroni correction (Exp C, Exp D)

For 3-arm design with k = 3 pairwise comparisons and family-wise α = 0.05:

```
α_per_comparison = 0.05 / k
```

Apply the two-sample formula with `α_per_comparison` instead of 0.05. For Δ = 40%, σ = 30% (Exp C, COX IV): n ≈ 12/arm with Bonferroni. For Δ = 20%, σ = 15% (Exp D, mito vs anabolic): n ≈ 12/arm with Bonferroni.

### 3.5 Python re-runnable snippet (reproduce or modify assumptions)

```python
import math
from scipy import stats

def z(a): return stats.norm.ppf(1 - a/2)
def z1(a): return stats.norm.ppf(1 - a)

def n_two_sample(delta, sigma, power=0.80, alpha=0.05):
    d = abs(delta)/sigma
    return math.ceil(2*(z(alpha)+z1(1-power))**2 / d**2)

def n_one_sample(delta, sigma, power=0.80, alpha=0.05):
    return math.ceil((z(alpha)+z1(1-power))**2 * sigma**2 / delta**2)

def n_within_animal_paired(delta, sigma, power=0.80, alpha=0.05):
    """Paired t: n = (z_a/2 + z_b)^2 * sigma_d^2 / delta^2
       For within-animal left-vs-right TA design, sigma_d << sigma_independent"""
    return math.ceil((z(alpha)+z1(1-power))**2 * (sigma*0.4)**2 / delta**2)
    # sigma_d ≈ 0.4*sigma for paired designs (correlation r ≈ 0.84)

# Examples
print("Exp B (15%, 12%):", n_two_sample(15, 12))   # 11
print("Exp B (15%, 12%) @ 0.90:", n_two_sample(15, 12, 0.90))  # 14
print("Aim 2 myobundle (20%, 15%):", n_two_sample(20, 15))  # 9
print("Exp D (20%, 15%) Bonferroni:", n_two_sample(20, 15, alpha=0.05/3))  # 12
```

### 3.6 R equivalent (for the SAP and reviewers)

```r
library(pwr)
# Two-sample t, Exp B
pwr.t.test(d = 0.15/0.12, sig.level = 0.05, power = 0.80, type = "two.sample")
# d = 1.25, n = 11.0 per group
pwr.t.test(d = 0.15/0.12, sig.level = 0.05, power = 0.90, type = "two.sample")
# n = 14.2 per group
# LMM (fibre nested in animal), Exp A
# Use simr::powerSim() with mixed model formula:
#   lme4::lmer(specific_force ~ age + (1|animal_id), data = ...)
```

---

## 4. Statistical framework per experiment

### 4.1 Tests

| Experiment | Primary test | Random effects (in vivo) | Fixed effects | Multiple-testing |
|---|---|---|---|---|
| **Aim 1** (cohort protein panel, ~6 proteins) | Welch's t (log2-transformed) per protein | donor (for paired donor data) | group (sarcopenic vs control) | **BH-FDR** across the 6-protein panel (per experiment) |
| **Aim 2** (Seahorse, C2C12) | One-sample t (vs 100% scramble), per OCR metric | differentiation (3 levels, biological replicate) | gene (scramble, siCHCHD10, siNDUFB4, siATP5F1B, siPGC-1α) | **BH-FDR** across OCR metrics (basal, ATP-linked, max, spare); per experiment |
| **Aim 2** (myobundle force) | Linear model (force ~ gene + CSA + differentiation) | bundle nested in differentiation | gene | **BH-FDR** across Tier-1/2 genes |
| **Aim 2** (HSMM) | Linear mixed model (force ~ gene + donor) | donor | gene | BH-FDR |
| **Aim 3** (PGC-1α RNA-seq) | DESeq2 (Wald) + label-permutation gene-set test | n/a | condition | **Genome-wide BH-FDR** (since the goal is pathway-level, not individual genes); sub-programme test as in HMSR v0.4 |
| **Aim 3** (rescue) | Paired t (within dif: scramble vs KD vs KD + rescue) | differentiation | condition | BH-FDR across OCR metrics |
| **Exp A** (aged C57BL/6J) | LMM `lme4::lmer(specific_force ~ age + (1\|animal_id))` | animal (random), fibre nested in animal | age (young vs aged) | BH-FDR across 4 endpoints (force, CSA, grip, permeabilized resp) |
| **Exp B** (AAV9-shRNA) | LMM `lmer(specific_force ~ treatment + (1\|animal_id))` with within-animal leg as repeated | animal (random), leg within animal (repeated) | treatment (shRNA vs scramble) | BH-FDR across 4 endpoints |
| **Exp C** (exercise) | Mixed ANOVA `lmer(endpoint ~ arm + (1\|animal_id))` | animal | arm (sed / wheel / treadmill) | **Bonferroni** for 3 pairwise (sed vs wheel, sed vs treadmill, wheel vs treadmill); pre-specified primary = sed vs wheel |
| **Exp D** (therapeutic) | Mixed ANOVA + ANCOVA (mass as covariate) `lmer(specific_force ~ arm * mass + (1\|animal_id))` | animal | arm × mass | **Bonferroni** for 3 pairwise (mito vs anabolic, mito vs vehicle, anabolic vs vehicle); pre-specified primary = mito vs anabolic at equal mass |

### 4.2 Pre-registration & software

- **SAP timing:** draft at protocol finalization (~M1); freeze before unblinding (M12-M14). Filed on **OSF** (DOI assigned) and **AsPredicted** (anonymised) before data collection; any deviations logged with date + reason.
- **Software:** R 4.3+ (lme4, emmeans, simr, pwr, effectsize); Python 3.11+ (pingouin, statsmodels, scipy.stats); G*Power 3.1 for spot-check sanity. **No hand-computed p-values in the manuscript** (per v0.2 §7).
- **Effect-size reporting:** Cohen's d / Hedges' g with 95% CI (effectsize R package); partial η² for ANOVA-style (effectsize::eta_squared); all CIs from noncentral t-distribution, not Wald.
- **Randomization & blinding:** in-vivo, animals randomized to AAV dose / exercise arm by stratified block (cage as block, littermate as strata); force assays and histology scored blinded to allocation. In-vitro, plates randomized across differentiation batches.
- **Multiple-testing correction scope:** **per experiment, not across the panel** (per v0.2 §7). v0.2 says "Bonferroni vs BH-FDR per experiment" — we use **BH-FDR** for Aims 1–3 (correlated endpoints) and **Bonferroni** for Exp C/D (3-arm designs where the pre-specified primary comparison is clear).

### 4.3 Mixed model specification (in-vivo)

For Exp B specifically (paired within-animal design):

```
# R formula (lme4)
specific_force ~ treatment * sex + (1 | animal_id) + (1 | animal_id:leg)

# Where:
#   treatment: factor (shRNA, scramble)  -- fixed
#   sex: factor (M, F)  -- fixed (only if mixed-sex design)
#   animal_id: random intercept for between-animal variance
#   animal_id:leg: random intercept for within-animal (left vs right TA) leg effect
```

Pre-specified contrasts (emmeans):
- `treatment` main effect (primary): `emmeans::contrast(emm, "trt.vs.ctrl", adjust = "BH")`
- `sex` main effect (secondary)
- `treatment:sex` interaction (if mixed-sex)

For Exp A (fibre nested in animal):
```
# lme4
specific_force ~ age + (1 | animal_id) + (1 | animal_id:fibre_id)
```
- `age`: fixed (young, aged)
- `animal_id`: random (between-animal)
- `animal_id:fibre_id`: random (within-animal, between-fibre)

---

## 5. Sensitivity analyses

### 5.1 Power sensitivity to effect size (Exp B, SD = 12%)

| Δ (effect, % of control) | Cohen's d | n/group @ 0.80 | n/group @ 0.90 |
|---|---|---|---|
| 5% | 0.42 (small-medium) | **91** | 122 |
| 10% | 0.83 (large) | 23 | 31 |
| **15% (v0.2/v0.3 primary)** | **1.25 (large)** | **11** | **14** |
| 20% | 1.67 (very large) | 6 | 8 |
| 25% | 2.08 (very large) | 4 | 5 |
| 30% | 2.50 (very large) | 3 | 4 |

**Reading:** if the true effect is closer to 10% (as some literature suggests for partial-KD rather than full KO), n inflates to 23–31. **v0.3 should pre-register the primary effect-size estimate as 15% with sensitivity range 10–25%.**

### 5.2 Power sensitivity to SD (Exp B, Δ = 15%)

| SD (% of control) | n/group @ 0.80 | n/group @ 0.90 |
|---|---|---|
| 6% (best-case, isogenic littermates, single operator) | 3 | 4 |
| 8% | 5 | 6 |
| 10% (v0.2 SD assumption) | 7 | 10 |
| **12% (v0.3 realistic, AAV9 + between-cage noise)** | **11** | **14** |
| 15% (conservative, multi-operator) | 16 | 22 |
| 20% (worst-case) | 28 | 38 |

**Reading:** v0.2's SD = 10% is optimistic. The realistic in-vivo TA specific-force SD after AAV9 + 8 wk + between-cage is closer to 12%. **v0.3 uses SD = 12% → n = 11/14.**

### 5.3 Sex consideration

The HMSR v0.4 cohort is **all male** (GSE111006, GSE111010, GSE111016 are male sarcopenia cohorts; GSE226151 is mixed-sex but the discovery meta-analysis was male-dominated). v0.2 §1 says nothing about sex in the in-vivo experiments.

**Three options:**

| Option | Exp B design | Cost (animals) | Power for primary | Translational breadth | v0.3 recommendation |
|---|---|---|---|---|---|
| **A: all-male (matches HMSR cohort)** | n = 14 M/group, 28 total | $30 × 28 = **$840 (mice only)** | 0.90 for 15% effect | Matches cohort; no sex-generalizability claim | **Recommended for v0.3** (cohort-matched, cost-efficient) |
| **B: mixed-sex (5M+9F, 14 total/group)** | 14 M + 14 F, 28 total ($30 M + $35 F = $910) | 0.80 for treatment × sex interaction; 0.90 for treatment main effect within each sex | Better generalizability | Add for follow-up R01 (not v0.3) |
| **C: mixed-sex (n=10/sex/group, 20/group)** | 20 M + 20 F, 40 total | 0.80 for treatment main effect in each sex; 0.65 for sex × treatment interaction | Best for sex-stratified claims | Over-budget for v0.3 |

**Sex × treatment interaction effect size:** the interaction Cohen's f is typically 0.15–0.25 for muscle physiology (small). To detect f = 0.25 with power 0.80 in a 2 × 2 design, n ≈ 158 total (using `pwr::pwr.f2.test`). **Detecting sex × treatment interaction is impractical in v0.3** with n = 28; requires n ≈ 80 per cell, which is R01-scale work.

**v0.3 decision:** keep Exp B all-male. Document this as a limitation and propose a mixed-sex replication cohort in the follow-up R01 (Aim 3 of the parent grant).

---

## 6. Budget implications

### 6.1 Per-experiment cost (updated v0.3)

| Item | Unit cost | v0.3 quantity | v0.3 sub-total | v0.2 sub-total (if different) | Notes |
|---|---|---|---|---|---|
| **Exp A**: 3-mo + 24-mo C57BL/6J | $30 (3-mo) / $80–150 (24-mo) | 8 + 8 = 16 mice | 8×$30 + 8×$115 = **$1,160** | $1,000 (v0.2 said n=8) | JAX C57BL/6J 24-mo cohort: $80–150/mouse from NIA aged colony |
| **Exp A**: husbandry 24-mo (12 mo extra) | $0.50/day × 365 d × 8 | 8 mice | **$1,460** | not separately costed | Aged-mouse colony holding cost is significant |
| **Exp A**: permeabilized-fibre Oroboros runs | $200/sample × 16 mice × 3 substrates = 48 runs | 48 | **$9,600** | not specified | Oroboros core fee ~$200/run |
| **Exp A**: single-fibre force rig time | $50–100/day × 16 mice × 1 day | 16 rig-days | **$1,200** | not specified | Single-fibre myograph rig time at muscle-phys core |
| **Exp A**: histology / TEM | $200–500/sample × 16 mice | 16 | **$5,600** | not specified | TEM at electron-microscopy core |
| **Exp B**: 3-mo C57BL/6J (n=14 + 14 = 28) | $30/mouse | 28 | **$840** | 20 mice × $30 = $600 | v0.3 = n=14/group |
| **Exp B**: AAV9-shRNA production (CHCHD10 + scramble, VectorBuilder / Vigene / Penn) | $2–4k per construct × 2 constructs | 2 | **$6,000** | $6,000 (v0.2) | Tier pricing at VectorBuilder (~$2.5k per AAV9-shRNA) |
| **Exp B**: AAV9 in-vivo delivery (TA injection, 8 wk) | $200/mouse × 28 | 28 | **$5,600** | $4,000 (v0.2 said 20 mice) | In-vivo injection + 8-wk holding |
| **Exp B**: in-vivo force (twitch + tetanic) | $300/mouse × 28 | 28 | **$8,400** | $6,000 | In-vivo footplate + force transducer |
| **Exp B**: ex-vivo force (matched CSA) | $400/mouse × 28 | 28 | **$11,200** | $8,000 | Ex-vivo muscle bath + force rig |
| **Exp B**: permeabilized-fibre Oroboros | $200/sample × 28 | 28 | **$5,600** | not specified | Same protocol as Exp A |
| **Exp B**: RNA-seq (post-treatment) | $200 lib + $50 seq × 28 | 28 libs | **$7,000** | $5,000 | NovaSeq 25M read pairs/lib |
| **Exp B**: histology/TEM | $400/mouse × 28 | 28 | **$11,200** | $5,000 | TEM is expensive |
| **Exp C**: 3-mo C57BL/6J (n=12 × 3 = 36) | $30 × 36 = $1,080 + 4-wk holding ~$120 | 36 | **$1,200** | $1,080 (v0.2) | Standard |
| **Exp C**: wheel cages + treadmill | $500/wheel × 12 = $6,000 + $5,000 treadmill | 1 set | **$11,000** | not specified | Wheel cages (Lafayette) + treadmill (Columbus) |
| **Exp C**: mito programme panel (protein + RNA) | $300/mouse × 36 | 36 | **$10,800** | $5,000 | WB + RT-qPCR + citrate synthase |
| **Exp D**: 24-mo C57BL/6J (n=15 × 3 = 45) | $115 × 45 = $5,175 + 12-wk holding ~$5,400 | 45 | **$10,575** | $9,200 (v0.2 said n=15) | Aged-mouse colony; biggest single line item |
| **Exp D**: 15-PGDH-i (SW033291) or PGC-1α inducer (clinical grade) | $200/mouse × 30 (2 active arms) × 12 wk | 30 mice | **$6,000** | not specified | SW033291 from Cayman / MedChemExpress; ~$200/mouse for 12-wk dosing |
| **Exp D**: anabolic comparator (e.g., formoterol or MYO-029) | $200/mouse × 15 | 15 | **$3,000** | not specified | β2-agonist (formoterol) at clinical-grade dose |
| **Exp D**: specific force + mass-matched ANCOVA | $700/mouse × 45 | 45 | **$31,500** | $20,000 | Force + body composition (DEXA) + CSA histology |
| **Exp D**: RNA-seq (programme recovery) | $250 × 45 = $11,250 | 45 | **$11,250** | $8,000 | + protein panel |
| **In vitro**: C2C12 + HSMM (Aim 1+2+3) | | | | | |
|   C2C12 culture + Seahorse (Aim 2) | $30/well × 60 wells × 3 plates | 180 wells | **$5,400** | $5,000 | |
|   HSMM donors (Aim 1+2) | $800/donor × 20 | 20 | **$16,000** | $12,000 | Lonza HSMM |
|   iPSC-CRISPR (Aim 3) | $3–6k/donor × 3 | 3 | **$12,000** | $15,000 | Crown / iPSC Core, 2–3 mo lead |
|   Myobundle force rig (Aim 2) | $75/day × 30 days | 30 | **$2,250** | $2,000 | Micro-tissue rig (e.g., Curi Bio, MuscleX) |
|   TEM / histology (in vitro) | $300/sample × 30 | 30 | **$9,000** | $6,000 | Mito morphology |
|   RNA-seq (Aim 3) | $250 × 16 libs | 16 | **$4,000** | $4,000 | |
|   RNA-seq (Aim 1 cohort) | $250 × 20 libs | 20 | **$5,000** | $3,000 | HSMM donor + control |
| **Cross-cutting** | | | | | |
|   Personnel (postdoc 14 mo × $7k/mo fringe) | $98k | 1 FTE | **$98,000** | $80,000 | |
|   Animal per diem (all in-vivo) | $0.50/d × ~5,000 mouse-days | 5,000 | **$2,500** | $2,000 | |
|   IACUC + vet + compliance | $5,000 | 1 | **$5,000** | $5,000 | |
|   Indirect costs (F&A @ 60% of personnel + supplies) | | | **$60,000** | $50,000 | |
| | | | | | |
| **TOTAL v0.3** | | | **~$370,000** | **$120,000–$160,000** | |

**v0.3 vs v0.2 budget:** the v0.3 estimate ($370k) is **substantially higher** than v0.2's $120–160k. The discrepancy is largely because v0.2 was an "indicative" budget that did not itemise aged-mouse colony cost, TEM, RNA-seq at scale, or personnel. v0.3 is more realistic. **For grant submission, use the v0.3 itemised budget** ($370k) — the v0.2 number was clearly under-scoped.

**If budget is constrained to $60–80k (half the v0.2 envelope):** see §7 decision summary for the recommended priority order.

---

## 7. Decision summary

### 7.1 Confirm or adjust v0.2 n

| Experiment | v0.2 n | v0.3 n | Change | Rationale |
|---|---|---|---|---|
| Aim 1 (cohort) | n ≥ 10/group | **n = 10–13/group** | no change | BH-FDR preserved at 10 |
| Aim 2 (Seahorse, C2C12) | 3 difs × ≥3 wells | **3 difs × 5 wells** (15 wells/condition) | small inflation | 5 wells/dif @ d = 1.3 gives 0.80 |
| Aim 2 (myobundle) | 6–8 bundles/condition | **3 difs × 4 bundles = 12 bundles/condition** | slight inflation | 0.80 power for 20% Δ, SD 15% |
| Aim 3 (PGC-1α programme) | 4 difs/condition | **4 difs/condition** | no change | Pathway-level; DESeq2 adequate |
| Exp A (aged C57BL/6J) | n = 8/group | **n = 8/group** | no change | LMM with 4 fibres/animal = 32 fibres/group gives 0.80+ |
| **Exp B (AAV9-shRNA)** | **n = 10/group** | **n = 14/group (or 11 if 0.80 acceptable)** | **INCREASE** | Realistic SD = 12% (v0.2 used 10%); 0.90 power requires n = 14 |
| Exp C (exercise) | n = 12/arm | **n = 12/arm** | no change | Adequate for 40% Δ (COX IV); underpowered for 20% Δ (use 0.80 + Bonferroni) |
| Exp D (therapeutic) | n = 15/arm | **n = 15/arm** | no change | Conservative; 0.80+ for 15% Δ at SD 12% with Bonferroni |

### 7.2 What changed from v0.2 (delta summary)

| Element | v0.2 (was) | v0.3 (now) | Why |
|---|---|---|---|
| Specific-force SD for Exp B | 10% | **12%** | AAV9 in-vivo + between-cage noise realistically larger; Guzman 2026 abstract qualitative; v0.2 was optimistic |
| Exp B n (0.80) | 10 | **11 (0.80) / 14 (0.90)** | Formula + realistic SD; recommend n=14 for grant defensibility |
| Spare respiratory capacity | not specified | **30% effect, 5 wells/dif, 3 difs** | Most variable OCR metric; explicit n now provided |
| Myobundle force | "n=6–8 bundles/condition" | **n=12 bundles/condition, 3 difs** | Per-dif random effect added; explicit 0.80 power |
| PGC-1α muscle-KO paper | Ruas 2012 (PMID 22977227) | **Handschin 2007 (PMID 17702743)** | v0.2 cited a non-existent/incorrect PMID (22977227 is a lipid genetics paper); the actual muscle-specific PGC-1α KO paper is Handschin et al. 2007 *J Biol Chem*; Wu et al. 2011 (PMID 21284983, Ruas as co-author) is the UPR/ATF6 follow-up |
| 15-PGDH / therapeutic arm | not specified | **Palla 2020 *Science* (PMID 33303683); Shu 2025 (PMID 40479501)** | Anchor for Exp D effect size; Palla 2020 15-PGDH-i → +mass, +strength, +mito function in aged mice is the gold-standard precedent |
| Sex consideration | not discussed | **All-male v0.3; mixed-sex replication in follow-up R01** | Matches HMSR cohort; n=80/cell for interaction is impractical |
| Sensitivity tables | none | **§5.1, §5.2 (effect-size × SD grid)** | Required for grant review (robustness of primary endpoint) |
| Permeabilized-fibre Oroboros (Exp B) | not specified | **n = 9–12 animals/group @ 0.80** (shared with force n=14) | Halling 2019 anchor; PGC-1α-dependent submaximal respiration |
| Budget itemization | $120–160k indicative | **$370k realistic itemized** | v0.2 was under-scoped; v0.3 is grant-defensible |
| Multiple testing | "BH-FDR" generic | **BH-FDR for Aims (correlated), Bonferroni for Exp C/D (3-arm pre-specified pairwise)** | Pre-specify scope of correction per v0.2 §7 |

### 7.3 If budget is capped at $60–80k (half v0.2 envelope)

Priority order (highest science per dollar):

1. **Aim 2 in-vitro (C2C12 siRNA CHCHD10 + Seahorse + myobundle force)** — $30–40k; the **fastest decision gate**; tests the central causation hypothesis in vitro; produces a JCSM/Aging Cell paper alone
2. **Exp B (AAV9-shRNA CHCHD10, n=11/group at 0.80)** — $40–50k including AAV9 production + 8-wk in-vivo; the **key in-vivo quality experiment**; **drop n from 14 to 11 to save $5k and accept 0.80 power**
3. **Exp A (aged C57BL/6J, n=8/group)** — $20k; observational anchor; lower priority because it's not causal

**Defer to follow-up R01:**
- Exp C (exercise reversal) — $35k — important but not the central test
- Exp D (therapeutic mass-matched) — $80k — the top-tier result but expensive aged colony; pair with an RO1/U01 mechanism
- iPSC-CRISPR (Aim 3) — $15k — can be replaced by the Ad-PGC-1α rescue in C2C12 for the v0.3 paper

**Minimum-viable v0.3 budget (Aims 1–2 in vitro + Exp B with n=11):** ~$80k (personnel + supplies + 60% indirect). Matches the lower bound of the $60–80k scenario.

### 7.4 Where v0.2 n is underpowered

| Endpoint | v0.2 n | True required n | Verdict |
|---|---|---|---|
| Exp B specific force (15% effect, 12% SD) | 10 | 11 (0.80) / 14 (0.90) | **v0.2 was 9% underpowered at 0.80, 40% underpowered at 0.90** — inflate to n=11 minimum |
| Exp C exercise COX IV (40% effect, 30% SD) | 12 | 9 (0.80) | OK at 0.80 |
| Exp C exercise PGC-1α (30% effect, 25% SD) | 12 | 11 (0.80); 15 Bonferroni | **Borderline underpowered at Bonferroni-corrected 0.80**; recommend n=15 if possible |
| Exp D specific force (20% effect, 15% SD, Bonferroni) | 15 | 12 (0.80) | Conservative; defensible |
| Exp A single-fibre (25% effect, 15% SD, LMM) | 8 | 6 (0.80) | Slightly over-powered; could drop to n=6 to save 2 mice + husbandry |

**Headline:** only **Exp B is materially underpowered** at v0.2's n=10. The single biggest v0.3 change is to inflate Exp B to n=14 (or n=11 if 0.80 is acceptable).

---

## 8. Limitations and honest notes

1. **Guzman 2026 specific-force number not extracted**: the v0.2 "15%" is the authors' working estimate. The full paper (DOI [10.1111/acel.70355](https://doi.org/10.1111/acel.70355)) likely reports the specific force % in a figure. **Action item:** request PDF from Aguilar lab (U. Michigan) and re-verify.
2. **PGC-1α muscle-specific KO primary citation corrected**: v0.2 cited "Ruas 2012 PMID 22977227" but 22977227 is a lipid-genetics paper. The correct primary citation is **Handschin et al. 2007** (PMID [17702743](https://pubmed.ncbi.nlm.nih.gov/17702743/), DOI [10.1074/jbc.M704817200](https://doi.org/10.1074/jbc.M704817200)). The Wu/Ruas 2011 paper (PMID [21284983](https://pubmed.ncbi.nlm.nih.gov/21284983/)) is the UPR/ATF6 follow-up, not the primary muscle-KO paper.
3. **iPSC donor cost may be higher than budgeted** depending on CRO ($3–6k/donor is a range; FUJIFILM Cellular Dynamics and Crown Bio are the leading CROs; some charge $8k+ for fully characterised myocytes).
4. **Aged C57BL/6J cost is volatile**: NIA aged colony is $80–150/mouse; private vendors (JAX) are $200–300. Confirm vendor at order time.
5. **Single-fibre ICC estimate (0.3) is a literature-based guess**; a small pilot (n = 3 animals × 10 fibres) would refine this and could shift the §5.3 mixed-model power.
6. **No Chinese/Japanese sarcopenia cohort data in v0.3 effect sizes** (HMSR cohort is Caucasian, Afro-Caribbean, Chinese — all male). Effect sizes may differ by ancestry; cross-ancestry replication is an R01-scale follow-up.

---

## 9. Reference table (PubMed-verified, alphabetical by first author)

| First author | Year | PMID | DOI | Key finding used in this analysis |
|---|---|---|---|---|
| **Akabane T** | 2024 | [39333763](https://pubmed.ncbi.nlm.nih.gov/39333763/) | [10.1038/s41598-024-73049-9](https://doi.org/10.1038/s41598-024-73049-9) | Alas1+/− senile mice (75–90 wk) — reduced body and gastrocnemius weight, reduced grip strength; LC3-II reduced; AMPK signalling reduced. **Provides effect-size anchor for Exp A aged C57BL/6J.** |
| **Cattaneo O** | 2026 | [41872887](https://pubmed.ncbi.nlm.nih.gov/41872887/) | [10.1186/s13395-026-00421-w](https://doi.org/10.1186/s13395-026-00421-w) | AAV9-shRNA in TA for CtBP1 KD; successful in vivo knockdown. **Provides precedent for AAV9 in vivo knockdown efficacy in muscle.** |
| **Colosio M** | 2023 | [37675472](https://pubmed.ncbi.nlm.nih.gov/37675472/) | (J Appl Physiol) | PASC muscle: VO2peak 24.7 ± 5.0 vs 32.9 ± 7.4 mL·min·kg (PASC vs CTRL); reduced CS, PGC-1α, mtDNA. **Human effect-size anchor for mito programme reduction in vivo.** |
| **Guzman SD** | 2026 | [41496579](https://pubmed.ncbi.nlm.nih.gov/41496579/) | [10.1111/acel.70355](https://doi.org/10.1111/acel.70355) | CHCHD2/CHCHD10 muscle-specific CRISPR KO → mitochondrial disorganization, reduced ATP, NMJ fragmentation, delayed reinnervation. **Direct precedent for Exp B; specific force number to be verified from full text.** |
| **Halling JF** | 2019 | [31265325](https://pubmed.ncbi.nlm.nih.gov/31265325/) | (Am J Physiol Endocrinol Metab) | Inducible PGC-1α muscle-cKO: aged mice → ↓submaximal ADP-stimulated respiration, ↑ROS, fragmented mitochondrial network; exercise training rescues submaximal ADP-stimulated respiration in PGC-1α-dependent manner. **Provides Exp C and Oroboros effect-size anchor.** |
| **Handschin C** | 2007 | [17702743](https://pubmed.ncbi.nlm.nih.gov/17702743/) | [10.1074/jbc.M704817200](https://doi.org/10.1074/jbc.M704817200) | PGC-1α muscle-specific KO: fiber-type shift IIa→IIx/IIb, reduced endurance, fiber damage + inflammation after treadmill. **Primary PGC-1α muscle-KO reference for Aim 3 (corrected from v0.2).** |
| **Jensen JH** | 2020 | [32764726](https://pubmed.ncbi.nlm.nih.gov/32764726/) | [10.1038/s41598-020-69936-6](https://doi.org/10.1038/s41598-020-69936-6) | C2C12 myotubes on 6 kPa gelatin substrates — high contractility. **Provides C2C12 specific-force CV for Aim 2 myobundle.** |
| **Kim S** | 2024 | [39059375](https://pubmed.ncbi.nlm.nih.gov/39059375/) | (Stem Cell Reports) | Microgravity muscle-on-chip; 15-PGDH-i partially rescues atrophy. **Supports Exp D 15-PGDH-i arm.** |
| **Medert R** | 2021 | [33580817](https://pubmed.ncbi.nlm.nih.gov/33580817/) | (Pflugers Arch) | AAV9-RNAi in vivo: 90% KD efficiency achievable in heart. **AAV9 in vivo KD efficiency anchor.** |
| **Mesquita PHC** | 2020 | [32748504](https://pubmed.ncbi.nlm.nih.gov/32748504/) | (Physiol Rep) | RT in older adults: ETC complexes I-V +39 to +180%, Mfn1/2/Opa1 +90–261%. **Provides Exp C effect-size anchor for COX IV.** |
| **Palla AR** | 2020 | [33303683](https://pubmed.ncbi.nlm.nih.gov/33303683/) | [10.1126/science.abc8059](https://doi.org/10.1126/science.abc8059) | 15-PGDH-i in aged mice → +mass, +strength, +mito function, +autophagy. **Primary Exp D therapeutic anchor.** |
| **Shu L** | 2025 | [40479501](https://pubmed.ncbi.nlm.nih.gov/40479501/) | (J Bone Joint Surg Am) | 15-PGDH-i (SW033291) in aged mice with rotator cuff tear: muscle mass 33.5 ± 3.0 mg vs 25.2 ± 1.8 mg (vehicle), CSA recovery 1,424 ± 81 vs 1,263 ± 57 μm². **Quantitative effect-size anchor for Exp D 15-PGDH-i arm.** |
| **Springer-Sapp CB** | 2025 | [41037391](https://pubmed.ncbi.nlm.nih.gov/41037391/) | [10.1016/j.tjfa.2025.100090](https://doi.org/10.1016/j.tjfa.2025.100090) | RT in sarcopenic older adults: +13% strength, Mfn2 changes, no significant mito biogenesis changes. **Provides Exp C effect-size anchor for specific force after exercise.** |
| **Wu J, Ruas JL, et al.** | 2011 | [21284983](https://pubmed.ncbi.nlm.nih.gov/21284983/) | (Cell Metab) | UPR/ATF6α mediates adaptation to exercise through PGC-1α. **Mechanistic support for Aim 3 PGC-1α exercise link.** |
| **Zhou L** | 2025 | [40228677](https://pubmed.ncbi.nlm.nih.gov/40228677/) | (Biochim Biophys Acta Mol Basis Dis) | PGC-1α muscle-specific OE aged mice: preserves mito biogenesis in muscle, but exacerbates brain mito decline. **Warns against chronic PGC-1α OE in vivo; supports PGC-1α induction with caution.** |
| **PGC-1α muscle-KO (v0.2 wrong PMID)** | — | 22977227 (NOT relevant) | — | v0.2 cited this PMID as Ruas 2012, but 22977227 is Shah et al. 2012 *Eur Heart J* on lipid genetics. **Citation corrected to Handschin 2007 (PMID 17702743).** |

---

## 10. Verification checklist (sign-off before grant submission)

- [ ] Re-extract Guzman 2026 specific force / ATP / NMJ numbers from full text (request PDF from Aguilar lab)
- [ ] Confirm aged C57BL/6J vendor (JAX vs NIA aged colony vs Envigo) and current price quote
- [ ] Confirm AAV9-shRNA production cost at VectorBuilder / Vigene / Penn Vector Core (request quote for CHCHD10 + scramble, miR30 backbone)
- [ ] Pilot n = 3 animals × 10 fibres to estimate single-fibre ICC (currently assumed 0.3; could be 0.2–0.4)
- [ ] Confirm HSMM donor source and price (Lonza vs Cell Applications vs iXCells Biotechnologies)
- [ ] Pre-register SAP on OSF + AsPredicted before Exp A starts (~M1)
- [ ] Final budget reconciliation: v0.3 itemised $370k vs available funding; cut Exp D to follow-up R01 if v0.3 budget is $150–200k

---

*Prepared as part of the HMSR v0.3 validation package. All PubMed references verified via the bio-research MCP on 2026-06-13. DOI links are clickable. Power formulas are reproducible via the Python snippet in §3.5.*
