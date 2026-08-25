# A reproducible skeletal-muscle resource reveals coordinated down-regulation of mitochondrial genes in sarcopenia

**Authors:** Larry Oh

**Affiliations:** Brown Biotech, Seoul, South Korea

**Correspondence:** Larry Oh, Brown Biotech, Seoul, South Korea. Email: `ohbryt@gmail.com`

**ORCID:** [TBD — register at https://orcid.org and update before submission]

**Keywords:** sarcopenia, skeletal muscle, transcriptomics, random-effects meta-analysis, mitochondria, mitochondrial translation, mitoribosome, aging

> **Version note (v0.4):** Corrects the Table 1 cohort demographics (which were
> wrongly inferred from acronyms) using the actual GEO metadata, relabels GSE226151
> as "MOS" (it is not the GESTALT dataset), and adds a bounded translational-context
> link to the muscle-quality reframe. Builds on v0.3, which added the rigorous,
> correlation-aware **label-permutation
> gene-set test** (replacing the inflated hypergeometric of v0.2) and the
> sub-programme decomposition (Figure 5), establishing that the *entire* mitochondrial
> biogenesis programme — not just respiratory subunits — is coordinately and
> specifically down-regulated. Carries forward the v0.2 corrections: gene set is
> *mitochondrial* not "OXPHOS" (CLTB is non-mitochondrial); the gate is *exploratory
> and post-hoc* (genes are **candidates**); the data are **two independent studies**,
> not four; and the pathway signal is robust to muscle-composition adjustment. The
> defensible result is **pathway-level coordinated mitochondrial-programme
> down-regulation**, robust collectively but fragile gene-by-gene. Honest ceilings
> remain: no gene survives genome-wide FDR, and the finding confirms (with new rigor)
> the established biology of mitochondrial decline in muscle aging.

---

## Abstract

Sarcopenia — the age-related loss of skeletal muscle mass and function — lacks a
consensus molecular signature. Here we present the **Human skeletal Muscle
Sarcopenia Resource (HMSR)**, a reproducible transcriptomic meta-analysis of
skeletal muscle across **two independent case-control studies** comprising four
sample sets (HSS, JSS, SSS — three demographic strata of one multi-site study,
GSE111017; and MOS/GSE226151, an independent study; n = 135 strict
case/control samples, 53 cases, 82 controls). Using cohort-stratified ordinary
least squares differential expression and DerSimonian-Laird random-effects
meta-analysis across 37,469 genes, we found that **no gene survives genome-wide
Benjamini-Hochberg FDR**; the genome-wide signal is weak (1.75× enrichment over
chance at meta-*p* < 0.005). We therefore applied an **exploratory, post-hoc
multi-criteria gate** (meta-*p* < 0.005, unanimous effect direction, no
heterogeneity flag) that yields **195 candidate genes** (141 down, 54 up). These
candidates are **significantly enriched for mitochondrial genes** (26/195 vs ~2.7
expected). A **correlation-aware label-permutation test** on the full ranked
genome (gate-independent) shows the entire 539-gene nuclear-encoded mitochondrial
programme is coordinately down-regulated (permutation *p* = 2.0×10⁻³), with **all
six sub-programmes** — Complex I/II-III-IV/V, mitoribosome, cristae/MICOS, and
import — concordantly down (*p* ≤ 6×10⁻³), whereas non-mitochondrial control
gene-sets are not (cytoplasmic ribosome *p* = 0.28; proteasome *p* = 0.12). This
is the transcriptomic signature of coordinated down-regulation of the mitochondrial **biogenesis**
programme, not isolated respiratory-chain loss. Gene-level signal is concentrated in the two
balanced, adequately-powered sample sets (SSS and MOS); per-gene effects are
directionally consistent but individually non-significant in the two small,
underpowered sets. Importantly, the mitochondrial enrichment **survives adjustment
for a muscle-composition (stromal/immune purity) proxy** (enrichment 26× retained;
4/7 highlighted genes remain meta-*p* < 0.005), arguing against a simple
fiber-loss/infiltration artifact, though residual test-statistic inflation in one
cohort and the absence of RNA-quality metadata leave a non-composition technical
factor incompletely excluded. We present HMSR as a **discovery resource**: the
pathway-level mitochondrial finding is robust to the most likely bulk-tissue
confound, whereas individual candidate genes require prospective validation (a
companion in vitro/in vivo plan is provided).

---

## Introduction

Sarcopenia, defined by the concurrent loss of skeletal muscle mass and physical
performance with aging, affects an estimated 10–29% of adults aged 60 and older
worldwide and is associated with falls, frailty, disability, and increased
all-cause mortality [1,2]. Despite decades of research, no single molecular
signature has gained broad acceptance, in part because most transcriptomic studies
of human skeletal muscle in sarcopenia are single-cohort and underpowered to
distinguish genuine disease signals from cohort-specific noise.

The heterogeneity problem is compounded by technical variation across studies:
different platforms, tissue-collection procedures, diagnostic criteria (EWGSOP1,
EWGSOP2, AWGS), and demographic imbalances. Vote-counting approaches — tallying how
many studies report a gene as differentially expressed — are prone to false
positives because they ignore effect-size heterogeneity and within-study
correlation [3,10].

Here we build HMSR, a reproducible meta-analytic resource. We assemble skeletal
muscle case-control data (Work Package 2, WP2), apply cohort-stratified
differential expression with standardized covariate handling (WP3), and combine
effect sizes using DerSimonian-Laird (DL) random-effects meta-analysis that
explicitly models between-cohort heterogeneity (τ²). Because genome-wide FDR
significance is **not** achieved, we treat downstream gene lists as exploratory
candidates and emphasize **pathway-level** structure, which is more robust to the
modest per-gene power than individual gene claims.

---

## Results

### Cohort assembly and the independence structure of the data

We assembled four skeletal muscle sample sets (Table 1). Critically, three of them
(GSE111006, GSE111010, GSE111016; HSS, JSS, SSS) are **demographic strata of a
single multi-site study** (superseries GSE111017; same laboratory, protocol, and
processing pipeline): the Hertfordshire (UK, Caucasian descent), Jamaica
(Afro-Caribbean descent), and Singapore (Chinese descent) Sarcopenia Studies — **all
male**. The fourth (GSE226151; here "MOS", an independent multi-omics sarcopenia
cohort, mixed-sex) is a separate study. The data therefore represent **two
independent studies**, one with three single-sex ancestry strata — not four
independent replications; their shared ancestry breadth (Caucasian, Afro-Caribbean,
Chinese) is a strength, but they are not independent replications. After restricting
to strict binary case/control samples, 135 samples remained (53 cases, 82 controls).
Phenotype assignment used structured GEO metadata fields only (`sarcopenia_status`,
`disease_state`, `low_muscle_mass`, `low_strength_or_function`), without manual
abstract inspection.

**Table 1. Sample-set characteristics.** (Demographics from each series' GEO metadata; MOS = GSE226151, an independent cohort — not the GESTALT/GSE164471 dataset, which was excluded.)

| Set | GEO | Study | Ancestry / origin | Sex | n (strict) | Cases | Controls | Genes tested |
|:----|:----|:------|:------------------|:----|:----------:|:-----:|:--------:|:------------:|
| HSS | GSE111006 | Hertfordshire Sarcopenia Study (UK) | Caucasian descent | Male | 32 | 4 | 28 | 15,362 |
| JSS | GSE111010 | Jamaica Sarcopenia Study | Afro-Caribbean descent | Male | 23 | 9 | 14 | 14,914 |
| SSS | GSE111016 | Singapore Sarcopenia Study | Chinese descent | Male | 40 | 20 | 20 | 37,073 |
| MOS | GSE226151 | Independent multi-omics sarcopenia cohort | Not stated in metadata | Both (20F/20M) | 40 | 20 | 20 | 17,988 |

Note that HSS contains only **4 cases**; its per-gene OLS estimates are unstable and
we report sensitivity analyses excluding it (below).

### No gene survives genome-wide FDR; the genome-wide signal is weak

We fitted per-gene OLS models independently in each set (formula
`expression ~ sarcopenia + estimable_covariates`; age z-scored in all sets, sex in
MOS), then combined sarcopenia effect sizes with DL random-effects
meta-analysis (Methods). **Across 37,469 genes, no gene passes genome-wide
Benjamini-Hochberg FDR ≤ 0.10.** The genome-wide signal is modest: 328 genes reach
meta-*p* < 0.005 versus 187 expected by chance (1.75× enrichment; implied
false-discovery proportion ≈ 57%), and 99 reach meta-*p* < 0.001 versus 37 expected
(2.6×). There is real but weak excess signal over the null.

Because no gene meets the pre-specified FDR threshold, we defined an **exploratory,
post-hoc multi-criteria gate** to prioritise candidates for follow-up:
(1) meta-*p* < 0.005; (2) unanimous effect direction across sets; (3) no
heterogeneity flag (I² < 50%, no sign mixing). We emphasise that this gate was
chosen **after** observing the FDR outcome and is **not** a confirmatory threshold;
genes passing it are **candidates**, not validated findings. Under the gate, **195
genes** pass (141 down-regulated, 54 up-regulated; Figure 3; mean I² = 1.9%).

### The entire mitochondrial gene programme is coordinately and specifically down-regulated

The central biological result is at the **pathway level** and does **not** depend on
the exploratory gate. Across the full transcriptome, the nuclear-encoded
mitochondrial gene programme (539 genes) is shifted strongly toward down-regulation:
the competitive statistic — in-set minus out-set mean per-gene meta-z — is **−1.14**
(Figure 5). For both the descriptive shift and the inferential test below we use a
fast Stouffer per-gene meta-z (combining the per-cohort OLS z-scores), which is the
statistic the permutation null is built on; the manuscript's DerSimonian-Laird
random-effects estimates (used for individual-gene reporting) give a concordant
competitive shift of −0.91 for the same gene set (descriptive companion;
`wp3c_pathway_enrichment.tsv`). The two meta flavours agree on direction and
magnitude; we report the Stouffer value because the significance test is calibrated
to it.

Because mitochondrial genes are co-regulated (PGC-1α biogenesis axis) and therefore
violate the gene-independence assumption of hypergeometric or rank-sum tests, we
assess significance with a **label-permutation null** that preserves the gene–gene
correlation structure: we permute the case/control label within each cohort, recompute
the entire per-gene (Stouffer) meta statistic, and rebuild the gene-set statistic
2,000 times (`scripts/pathway_permutation.py`). Because every gene is recomputed under
the same permuted labels, the gene–gene correlation structure is preserved in the
null, making this a correlation-aware test (the permutation analogue of CAMERA's
variance inflation). One caveat: labels are permuted while the age/sex covariates are
held fixed, so this null is not fully covariate-exchangeable. We therefore repeated the
test with a **Freedman–Lane residual permutation** (regress expression on the covariates,
permute the reduced-model residuals, refit the full model; N = 2,000), which respects
the covariate structure. The result is essentially unchanged: the mitochondrial programme
remains down at *p* = 1.0×10⁻³, all six sub-programmes at *p* ≤ 5.5×10⁻³, and the
non-mitochondrial controls remain non-significant (Table S7;
`scripts/sensitivity_freedman_libsize.py`).

Under this null, the mitochondrial programme is significantly down-regulated
(permutation *p* = 2.0×10⁻³; 3.2 SD below the permutation-null mean), and — notably —
**all six mitochondrial sub-programmes move together**: Complex I (*p* = 1.0×10⁻³),
Complex II/III/IV (1.0×10⁻³), Complex V (3.5×10⁻³), mitoribosome (6.0×10⁻³),
cristae/MICOS (5.0×10⁻⁴), and protein import (3.0×10⁻³). This is the transcriptomic
signature of coordinated down-regulation of the mitochondrial **biogenesis** programme
(translation, import, cristae assembly, and the respiratory chain) rather than isolated
loss of respiratory-subunit transcripts.

The shift is **mitochondria-specific**, not a global down-shift: non-mitochondrial
control gene sets are not significant under the same test (cytoplasmic ribosome
*p* = 0.28; proteasome *p* = 0.12), and the collagen/ECM set shifts *up* (consistent
with relative fibrosis). The descriptive effect-size separation is large — mitochondrial
sub-programmes sit at competitive AUC 0.25–0.33 (strongly down) versus controls at
0.40–0.47 (`output/signatures/wp3c_pathway_enrichment.tsv`).

**Table 2. Seven highlighted mitochondrial candidates — corrected functional classes.**

| Gene | True function | OXPHOS subunit? | β (RE meta) | p (meta) | FDR (BH) | I² (%) |
|:-----|:--------------|:---------------:|:-----------:|:--------:|:--------:|:------:|
| NDUFB4 | Complex I accessory subunit | **Yes** | −0.190 | 3.1×10⁻³ | 0.534 | 47 |
| ATP5F1B | Complex V (ATP synthase) F₁β | **Yes** | −0.221 | 3.5×10⁻³ | 0.544 | 39 |
| CHCHD10 | MICOS / cristae (IMS) | No | −0.164 | 7.5×10⁻⁶ | 0.255 | 0 |
| APOO | MICOS (MIC26) / cristae | No | −0.236 | 4.9×10⁻⁴ | 0.339 | 36 |
| MRPL33 | Mitoribosome large subunit | No | −0.212 | 1.3×10⁻³ | 0.424 | 48 |
| MRPL34 | Mitoribosome large subunit | No | −0.282 | 3.6×10⁻⁴ | 0.303 | 35 |
| ~~CLTB~~ | **Clathrin light chain B — NOT mitochondrial** | No | −0.145 | 1.6×10⁻⁵ | 0.255 | 0 |

**CLTB is not a mitochondrial protein** (cytosolic clathrin vesicle coat). It is the
second-strongest single signal but does not belong to the mitochondrial cluster; it
is retained here only for transparency and should be interpreted separately. Only
**NDUFB4 and ATP5F1B are true OXPHOS subunits**; the remainder are mitochondrial
translation (mitoribosome) and cristae-organising (MICOS) genes. The v0.1 label
"OXPHOS signature" was therefore inaccurate and is corrected to "mitochondrial."

### Gene-level signal is concentrated in the two balanced, well-powered sets

Per-set significance reveals that individual-gene replication is limited (Table 3).
For the six mitochondrial candidates above, individual significance (p < 0.05)
occurs in only **1–2 of 4 sets**, always SSS (GSE111016) and/or MOS
(GSE226151) — the two balanced 20/20 designs. The two small sets (HSS, 4 cases;
JSS, 9 cases) are never individually significant, with effects ranging from
consistent-but-underpowered (HSS) to near-zero (JSS). Excluding the two well-powered
sets leaves no significant signal (HSS+JSS-only meta p = 0.09–0.45).

**Table 3. Per-set effects (β; * p<0.05) for six mitochondrial candidates.**

| Gene | HSS (n=32) | JSS (n=23) | SSS (n=40) | MOS (n=40) | Sets sig. |
|:-----|:----------:|:----------:|:----------:|:--------------:|:---------:|
| CHCHD10 | −0.190 | −0.152 | −0.158\* | −0.324 | 1/4 |
| MRPL34 | −0.188 | −0.032 | −0.299\* | −0.463\* | 2/4 |
| APOO | −0.214 | −0.064 | −0.241\* | −0.415\* | 2/4 |
| MRPL33 | −0.177 | −0.050 | −0.202\* | −0.406\* | 2/4 |
| NDUFB4 | −0.053 | −0.083 | −0.196\* | −0.334\* | 2/4 |
| ATP5F1B | −0.120 | −0.011 | −0.230\* | −0.384\* | 2/4 |

This is consistent with a real but small effect that is detectable only in
adequately-powered designs: the directionally-consistent βs in HSS argue the effect
is present but undetectable per-set, whereas the meta-analysis aggregates the
evidence. The honest interpretation is **effective independent replication ≈ 1**
(MOS confirms the GSE111017-family signal). The signal is **robust at the
pathway level, fragile at the gene level**.

**Sensitivity (excluding the 4-case HSS set):** the six mitochondrial candidates
remain meta-*p* < 0.015 (CHCHD10 2.0×10⁻⁵; NDUFB4 2.9×10⁻⁴; MRPL34 3.2×10⁻³; APOO
7.5×10⁻³; ATP5F1B 7.7×10⁻³; MRPL33 1.3×10⁻²), so the unstable small set does not
drive the result.

### The mitochondrial signal is robust to muscle-composition confounding

A central concern for any bulk-muscle case/control comparison is that apparent
"down-regulation" of an abundant transcript program (such as the mitochondrial
program) may reflect **reduced muscle-fiber purity** — more stromal/immune
infiltration or fibrosis in cases — rather than per-cell transcriptional change. We
tested this directly (WP3b; `scripts/confound_sensitivity.py`) by (i) deriving a
per-sample non-myofiber composition proxy from stromal (collagens, *DCN*, *LUM*,
*PDGFRA*) and immune (*PTPRC*, *CD68*, *LYZ*, …) marker genes, (ii) re-fitting every
gene with this proxy as an added covariate, and (iii) recomputing the
meta-statistics and mitochondrial enrichment.

The signal **survives composition adjustment**:
- Mitochondrial enrichment among top down-regulated genes persists almost unchanged
  (MOS 26.4× vs 29.6× unadjusted; SSS 10.9× vs 11.3×).
- 4 of 7 highlighted genes remain meta-*p* < 0.005 after adjustment — **CHCHD10**
  (1.8×10⁻⁵), **CLTB** (3.1×10⁻⁵), **APOO** (1.9×10⁻³), **MRPL33** (4.3×10⁻³); the
  other three attenuate but stay nominally significant (MRPL34 0.034, NDUFB4 0.022,
  ATP5F1B 0.057).
- Critically, the composition proxy **does not reduce the test-statistic inflation**
  (MOS λ 1.93→1.91; SSS 1.22→1.32). If the inflation and the mitochondrial
  pattern were caused by fiber-loss/infiltration, adjusting for the non-myofiber
  proxy would have lowered both. It did not.

This argues **against** the simplest purity-artifact explanation: the coordinated
mitochondrial down-regulation is not merely a consequence of stromal/immune
contamination.

We further controlled for **sequencing depth**, because cases had ~7–9% lower library
size than controls in three of four cohorts (JSS 0.93, SSS 0.93, MOS 0.91; a potential
compositional confound). Re-fitting every gene with per-sample log₁₀(library size) as
an added covariate (WP3e; from `raw_counts.tsv`) left the highlighted genes essentially
unchanged — the same 4 of 7 remain meta-*p* < 0.005 (CHCHD10 8.6×10⁻⁶, CLTB 1.5×10⁻⁵,
MRPL33 2.5×10⁻³, MRPL34 2.5×10⁻³; APOO/NDUFB4/ATP5F1B attenuate to 0.0076–0.050) and the
mitochondrial enrichment persists (Table S8).

Two caveats remain: (i) we lack per-sample RNA-integrity (RIN) measurements, so a
non-composition technical factor in the high-λ MOS cohort cannot be fully excluded; (ii)
the residual inflation in MOS is consistent with either a strong genuine transcriptome-wide
effect or an unmeasured batch/quality factor. The decisive resolution is cell-type
deconvolution on data with QC metadata, and ultimately the controlled-perturbation
experiments in the companion plan.

### Exercise epigenetic evidence: a gap, not a link

Integration of the candidate set with the HMSR exercise epigenetic evidence ladder
(WP5; rat MoTrPAC DMR data) identified 37 exercise-epigenetic and 90 human
multilayer evidence rows. **None of the mitochondrial candidates overlap the rat
exercise epigenetic ladder.** Whether exercise epigenetically remodels these genes
is therefore unestablished from available rodent data — an explicit gap that
motivates the prospective in vitro and in vivo validation in the companion plan.

---

## Discussion

We present HMSR, a reproducible two-study skeletal-muscle meta-analysis. Our honest
findings are: (i) **no gene reaches genome-wide FDR significance**, and the
genome-wide signal is weak (1.75× at p<0.005); (ii) at the **pathway level**, a
correlation-aware permutation test shows the **entire mitochondrial gene programme
is coordinately and specifically down-regulated** (*p* = 2.0×10⁻³), with all six
sub-programmes — respiratory Complexes I/II-III-IV/V, mitoribosome, cristae/MICOS,
and import — moving together while non-mitochondrial controls do not; and (iii) this
pathway signal is **robust to muscle-composition adjustment** but, at the individual
gene level, is driven by the two balanced cohorts and contains no FDR-significant
member. The coordinated movement of translation, import, cristae, and respiratory
modules together is the signature of coordinated **mitochondrial biogenesis-programme down-regulation**,
a more complete and specific statement than "respiratory-chain decline."

**Pathway-level mitochondrial down-regulation is the defensible result.** The
convergence of mitoribosome subunits (*MRPL33/34*, *MRPS15*, *MRPL15/27*),
respiratory subunits (*NDUFB4*, *ATP5F1B*, *SDHD*), import machinery (*TIMM17A*),
and cristae genes (*CHCHD10*, *APOO*) is consistent with reduced mitochondrial
content and respiratory capacity reported in aged/sarcopenic muscle [6,7,9] and in
rodent models [8]. We deliberately frame this as a coordinated programme rather
than a panel of independent biomarkers, because per-gene power is limited.

**Individual candidates require validation; the labels matter.** Only *NDUFB4* and
*ATP5F1B* are OXPHOS subunits; *MRPL33/34* are translational and *CHCHD10/APOO* are
structural (MICOS). *CHCHD10* remains biologically compelling: CRISPR knockout in
young mouse muscle recapitulates aged-muscle phenotypes including reduced ATP
production and NMJ fragmentation [6], and dominant *CHCHD10* mutations cause
neuromuscular disease [4,5]. *CLTB*, although statistically prominent, is not
mitochondrial and should not be grouped with this cluster.

**Translational context: the "metabolic-competence" axis of muscle quality.** A
parallel line of argument holds that sarcopenia pharmacology has failed because it
targeted muscle *mass* — a poor surrogate for the innervated, metabolically competent,
force-producing fraction of muscle — and that future therapeutics should instead
target muscle *quality*, of which mitochondrial/metabolic competence is one of three
named pillars [11; metabolic-competence pillar consistent with 6,7]. Our pathway-level result provides
independent **human transcriptomic** support for that specific pillar: the
mitochondrial gene programme is coordinately down-regulated in sarcopenic muscle. We
make this point at the level of the **conceptual reframe** (a degraded metabolic-
competence axis), not at the level of any specific drug. For transparency we note
that the prostaglandin-degrading enzyme transcript *HPGD* (15-PGDH), nominated as a
druggable handle in that Perspective on the basis of a murine enzyme-activity result,
is not differentially expressed at the mRNA level in this human sarcopenia contrast
(Supplementary Table S6); a bulk-transcriptomic resource **cannot test an
enzyme-activity hypothesis** (transcript abundance need not track enzyme activity, and
the murine claim is young-vs-aged rather than sarcopenic-vs-control), so we draw no
inference about that target from this null.

**Limitations.** (1) The four sample sets are **two independent studies**; effective
independent replication is ≈1. (2) **No gene survives genome-wide FDR**; all gene
lists are exploratory candidates from a **post-hoc** gate, and require prospective
replication. (3) Gene-level signal depends on two balanced cohorts; the small sets
are underpowered (HSS has 4 cases). (4) Cross-sectional expression cannot establish
causation, and "biogenesis-programme down-regulation" is a transcript-level
statement — it does not directly measure mitochondrial content, respiration, or flux.
(5) The exercise epigenetic integration crosses species and shows no overlap with the
candidate genes. (6) The label-permutation null holds age/sex fixed; a covariate-
exchangeable **Freedman–Lane permutation gives the same result** (Table S7), and the
mitochondrial signal also survives a **library-size (sequencing-depth) covariate**
(Table S8) — but a formal age-matched subset and cell-type deconvolution on QC-annotated
data remain outstanding. (7) RNA-integrity/batch metadata are unavailable, and the
residual test-statistic inflation in MOS (λ = 1.93, not lowered by composition or
library-size adjustment) leaves a non-composition technical factor incompletely excluded.

**Implications.** HMSR is best used as a **pathway-level discovery resource**
pointing to mitochondrial gene-programme down-regulation — human transcriptomic
evidence for the metabolic-competence axis of muscle quality — plus a transparent
candidate list for prospective validation. The full replication matrix (37,469
genes) is released for re-analysis with correlation-aware gene-set methods.

---

## Methods

### Cohort assembly (WP2)
Automated query of GEO structured metadata. Inclusion: skeletal muscle; Homo
sapiens; sarcopenia-relevant binary phenotype in structured fields. Exclusion:
proxies/mixed phenotypes; non-human; no gene-level matrix. Final sets in Table 1.

### Differential expression (WP3)
Per-gene OLS (statsmodels) on TMM-normalized log2 CPM, formula
`expression ~ sarcopenia + estimable_covariates`. **Method note:** the field default
is DESeq2/edgeR/limma-voom on raw counts; OLS is used because inputs are
pre-normalized log-CPM (equivalent to limma-trend practice; documented in
`config.yaml`). Genome-wide BH-FDR per set.

### DerSimonian-Laird meta-analysis
Effect sizes combined with the DL random-effects estimator;
τ² = max(0, (Q − (k−1))/C), weights wᵢ* = 1/(σᵢ²+τ²), β_RE = Σ(wᵢ*βᵢ)/Σwᵢ*,
SE_RE = 1/√(Σwᵢ*). Genome-wide BH-FDR over all 37,469 meta-p values. We report that
**zero genes** reach FDR ≤ 0.10.

### Exploratory candidate gate (post-hoc)
After observing no FDR-significant genes, we defined an exploratory gate:
meta-*p* < 0.005; unanimous direction; no heterogeneity flag (I² < 50%, no sign
mixing). The "leave-one-cohort-out" field records **direction concordance** (sign
agreement between each held-out set and the mean of the rest), **not** a
significance-based replication test; it is reported for transparency and is not
used as evidence of statistical replication. Genes passing the gate are candidates.

### Gene-set enrichment (correlation-aware)
Gene sets were defined by curated symbol patterns (mitochondrial sub-programmes and
non-mitochondrial controls). Because nuclear-encoded mitochondrial genes are
co-regulated, gene-independence tests (hypergeometric, rank-sum) are inflated; we
therefore assess significance with a **label-permutation null** (`scripts/pathway_permutation.py`):
the case/control label is permuted within each cohort, the full per-gene meta
statistic (Stouffer combine of per-cohort OLS z) is recomputed, and the competitive
set statistic (in-set minus out-set mean meta-z) is rebuilt for N = 2,000 permutations
(seed 42). Because all genes are recomputed under the same permuted labels, the
gene–gene correlation structure is preserved in the null, making the empirical p-value
correlation-aware (the permutation analogue of CAMERA's variance inflation). One-sided
empirical and parametric (Gaussian-null) p-values are reported. Descriptive AUC and
mean-z effect sizes (`scripts/pathway_enrichment.py`) are valid point estimates;
their accompanying Mann-Whitney p-values are not correlation-aware and are used only
for ranking. Sensitivity meta-analyses excluding the 4-case HSS set are reported for
the highlighted candidates.

### Reproducibility
Code in the HMSR repository; environment pinned in `environment.yml` /
`environment.lock.yml`; `config.yaml` records gates and seeds; `scripts/verify.py`
asserts universal + bulk-transcriptomics gates (STATUS=PASS); output
checksums in `data/CHECKSUMS.txt`.

---

## Data availability
NCBI GEO: GSE111006, GSE111010, GSE111016, GSE226151. Full replication matrix and
candidate lists in Supplementary Tables S1–S3.

## Code availability
HMSR analysis code is publicly available at `https://github.com/ohbryt/mitochondria_sarcopenia`
(release tag `v0.4-paper1`; archival DOI pending) under the **MIT License**
(`LICENSE` file at repository root).
A one-command re-run and a terminal verifier (`scripts/verify.py`, STATUS=PASS)
reproduce all reported numbers. Output provenance hashes are in `data/CHECKSUMS.txt`.
Companion in-vitro / in-vivo validation plan (v0.2, v0.3) is included in the
`validation/` subdirectory of the repository.

## Competing interests
The author declares no competing interests. Brown Biotech (the author's
affiliation) had no role in study design, data analysis, interpretation, or
the decision to submit the work for publication.

## Funding
This work was supported by Brown Biotech (internal funding). No external
funding was received.

## Acknowledgments
We thank the HMSR validation working group and the Brown Biotech scientific
advisory board for helpful discussions; the contributors to the HMSR public
cohorts (GEO accessions GSE111006, GSE111010, GSE111016, GSE226151); and the
developers of open-source tools used in this work (statsmodels, scipy, pandas,
matplotlib, Snakemake, Nextflow). Codex (GPT) provided critical adversarial
review (see Supplementary Codex adversarial review v0.3).

---

## Figure legends

**Figure 1. Study overview.** Two independent studies (GSE111017 family with three
strata + MOS), 135 strict samples; WP3 OLS + DL random-effects meta across
37,469 genes; no FDR-significant gene; exploratory post-hoc gate → 195 candidates;
mitochondrial enrichment; WP5 exercise-epigenetic gap.

**Figure 2. Forest plots for highlighted mitochondrial candidates.** Per-set OLS β
(95% CI) and DL random-effects estimate (diamond). Note per-set non-significance in
the small sets (HSS, JSS) and that CLTB is shown separately as a non-mitochondrial
outlier.

**Figure 3. Meta-analysis volcano plot.** −log₁₀(meta-p) vs RE meta-β for 37,469
genes; candidate down (blue, n=141) / up (red, n=54); dashed line meta-p = 0.005.
No gene reaches genome-wide FDR.

**Figure 4. Heatmap of top candidates.** Per-set β; mitochondrial gene names
highlighted; CLTB annotated as non-mitochondrial.

**Figure 5. Coordinated, specific down-regulation of the mitochondrial gene programme.**
Competitive shift in meta-z (in-set minus out-set) for the aggregate mitochondrial
programme, its six sub-programmes (red), and non-mitochondrial control sets (grey),
from a label-permutation competitive test (N = 2,000; error bars = permutation-null
SD). All mitochondrial sub-programmes shift down (permutation *p* ≤ 6×10⁻³);
cytoplasmic-ribosome and proteasome controls are non-significant; collagen/ECM shifts
up. Source: `output/signatures/wp3c_permutation.tsv`.

---

## Supplementary Tables
**Table S1.** All 195 candidate genes with full meta-statistics.
**Table S2.** Full replication matrix (37,469 genes).
**Table S3.** Per-set significance and functional classification of highlighted candidates.
**Table S5.** Gene-set permutation enrichment (`wp3c_permutation.tsv`) and descriptive AUC (`wp3c_pathway_enrichment.tsv`).
**Table S6.** Therapeutic-axis transparency projection (`wp6_therapeutic_axis.tsv`): 15-PGDH/*HPGD*, PGE₂-axis, atrogene, myostatin-axis, and biogenesis genes in HMSR — none reach FDR<0.10; provided so readers can see the muscle-quality-pathway genes directly. Transcript-level, not an enzyme-activity test.
**Table S7.** Freedman–Lane covariate-exchangeable permutation enrichment (`wp3d_freedman_lane.tsv`): mitochondrial sub-programmes vs controls under a covariate-respecting null.
**Table S8.** Library-size (sequencing-depth) covariate sensitivity for the highlighted genes (`wp3e_libsize_sensitivity.tsv`).

---

## References

*(Based on articles retrieved from PubMed)*

1. Laskou F, Patel HP, Cooper C, Dennison E. A pas de deux of osteoporosis and sarcopenia: osteosarcopenia. *Climacteric* 2021;**25**(1):88–95. [https://doi.org/10.1080/13697137.2021.1951204](https://doi.org/10.1080/13697137.2021.1951204) (PMID: 34308725)
2. Widajanti N, *et al.* Sarcopenia and Frailty Profile in the Elderly Community of Surabaya. *Acta Med Indones* 2020;**52**(1):5–13. (PMID: 32291366)
3. Silva NI, *et al.* Host Transcriptional Meta-signatures Reveal Diagnostic Biomarkers for *Plasmodium falciparum* Malaria. *J Infect Dis* 2024;**230**(2):e474–e485. [https://doi.org/10.1093/infdis/jiae041](https://doi.org/10.1093/infdis/jiae041) (PMID: 38271704)
4. Shammas MK, Huang TH, Narendra DP. CHCHD2 and CHCHD10-related neurodegeneration. *Biochem Soc Trans* 2023;**51**(2):797–809. [https://doi.org/10.1042/BST20221365](https://doi.org/10.1042/BST20221365) (PMID: 37021679)
5. Genin EC, *et al.* Loss of MICOS complex integrity and mitochondrial damage in CHCHD10-related diseases. *Neurobiol Dis* 2018;**119**:159–171. [https://doi.org/10.1016/j.nbd.2018.07.027](https://doi.org/10.1016/j.nbd.2018.07.027) (PMID: 30092269)
6. Guzman SD, *et al.* Age-Associated Dysregulation of Postsynaptic Mitochondria Perturbs Reinnervation Kinetics. *Aging Cell* 2026;**25**(1):e70355. [https://doi.org/10.1111/acel.70355](https://doi.org/10.1111/acel.70355) (PMID: 41496579)
7. Kawaida MY, *et al.* Elevating Circulating L-Kynurenine Promotes Frailty in Aging Mice. *J Cachexia Sarcopenia Muscle* 2026;**17**(1):e70214. [https://doi.org/10.1002/jcsm.70214](https://doi.org/10.1002/jcsm.70214) (PMID: 41622921)
8. Mo X, *et al.* Faecal microbiota transplantation from young rats attenuates age-related sarcopenia. *J Cachexia Sarcopenia Muscle* 2023;**14**(5):2168–2183. [https://doi.org/10.1002/jcsm.13294](https://doi.org/10.1002/jcsm.13294) (PMID: 37439281)
9. Flaherty SE, *et al.* GDF15 Neutralization Ameliorates Muscle Atrophy in a Mouse Model of Mitochondrial Myopathy. *J Cachexia Sarcopenia Muscle* 2025;**16**(1):e13715. [https://doi.org/10.1002/jcsm.13715](https://doi.org/10.1002/jcsm.13715) (PMID: 39976232)
10. Harbert DH. ALDH1A1-dopaminergic gene co-expression in human substantia nigra: meta-analysis across seven Parkinson's disease datasets. *Front Aging Neurosci* 2026;**18**:1806505. [https://doi.org/10.3389/fnagi.2026.1806505](https://doi.org/10.3389/fnagi.2026.1806505) (PMID: 42239820)
11. [Companion Perspective] "Sarcopenia drug development has optimized the wrong variable: the case for targeting muscle quality." Manuscript in preparation (the muscle-quality reframe and 15-PGDH/PGE₂ nomination cited here as conceptual context). *Cited as an unpublished companion manuscript; not used as empirical support.*

---
*Manuscript version: v0.4 — 2026-06-12. Response to Codex adversarial review (`CODEX_REVIEW_v0.3.md`): **corrected Table 1 demographics from the actual GEO metadata** (HSS = Hertfordshire/UK/Caucasian/male; JSS = Jamaica/Afro-Caribbean/male; SSS = Singapore/Chinese/male; GSE226151 relabelled "MOS", an independent cohort — NOT GESTALT/GSE164471) and propagated the fix through all prose; clarified the Stouffer-vs-DL meta statistic for the enrichment headline; purged "replicated" from figures (now "candidate"/"gate-pass"); softened "collapse" to transcript-level down-regulation; **ran the two remaining methodological sensitivities — Freedman–Lane covariate-exchangeable permutation (Table S7) and library-size/sequencing-depth covariate (Table S8) — both confirm the mitochondrial result.** Adds a bounded **translational-context** paragraph linking the mitochondrial finding to the muscle-quality (metabolic-competence) reframe of the companion therapeutics Perspective, with an HPGD transparency note (Table S6). Carries forward v0.2/v0.3 rigor (correlation-aware permutation, composition-robustness, two-study framing, OXPHOS→mitochondrial). See `CRITICAL_REVIEW_v0.1.md` / `CRITICAL_REVIEW_v0.2.md` / `CODEX_REVIEW_v0.3.md`.*
*All statistics computed by committed pipeline code; no hand-computed values.*
