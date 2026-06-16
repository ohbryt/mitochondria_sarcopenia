# CONSTRUCT_SPECS.md
## HMSR Aim 2 — In-Vitro Construct Design Specification
### siRNA / shRNA / CRISPR gRNA for CHCHD10, NDUFB4, ATP5F1B, PPARGC1A
### Dry-lab operational plan — RFP / CRO-ready handoff

---

| Field | Value |
|---|---|
| **Document ID** | `sarcopenia-multiomic-resource/validation/constructs/CONSTRUCT_SPECS.md` |
| **Version** | v0.1 — initial dry-lab specification |
| **Date** | 2026-06-13 |
| **Branch** | `validation/aim2-causation` |
| **Worktree** | `/Volumes/4TB/exerciseomics/.worktrees/validation-aim2/` |
| **Supersedes** | — (first issue) |
| **Status** | Dry-lab planning only — **no wet-lab execution in this session** |
| **Prepared by** | Brown Biotech (Larry) — operationalization of `experimental_validation_plan_v0.2.md` |
| **Linked files** | `validation/README.md`, `validation/antibodies/ANTIBODY_PANEL.md` (TBD), `validation/protocols/`, `validation/vendors/`, `manuscripts/paper1_v0.4.md` |
| **Target journal framing** | Paper 2 (JCSM / Aging Cell) in-vitro causation; complements Paper 1 (v0.4) and supports Paper 3 (Nat Aging tier) |

---

## 0. Scope, design principles, and key citations

### 0.1 Scope
This document specifies **knockdown / knockout reagents** for four genes across two myocyte backgrounds (mouse C2C12, human HSMM) to support **Aim 2 (causation)** of the HMSR validation plan:

| Gene | Tier | Function | Statistical signal (RE meta) | Why targeted |
|---|---|---|---|---|
| **CHCHD10** | 1 (lead) | MICOS / cristae (IMS) | β=−0.164, p=7.5×10⁻⁶, I²=0% | Strongest signal + zero heterogeneity; Guzman 2026 (PMID 41496579) muscle-specific CRISPR-KO recapitulates aged phenotype |
| **NDUFB4** | 2 | Complex I accessory (B15 subunit) | β=−0.190, p=3.1×10⁻³, I²=47% | True OXPHOS subunit, direct respiratory-chain test |
| **ATP5F1B** | 2 | Complex V (ATP synthase) F₁β | β=−0.221, p=3.5×10⁻³, I²=39% | True OXPHOS subunit, ATP-synthesis endpoint |
| **PPARGC1A** (PGC-1α) | master | Mitochondrial biogenesis master TF | — | Tests whether the entire programme is reproducible from one node |

### 0.2 Modalities specified
For **each gene × species** (4 × 2 = 8 combinations), five orthogonal modalities:

1. **siRNA SMARTpool** (siGENOME, 4-oligo pooled) — primary screen
2. **siRNA individual validated** (Silencer Select or ON-TARGETplus) — for deconvolution
3. **shRNA lentiviral** (MISSION TRC pLKO.1) — stable lines / Exp B in-vivo feed
4. **CRISPR Cas9 sgRNA** (IDT Alt-R, RNP) — knock-out orthogonal confirmation
5. **CRISPR Cas9 sgRNA** (lentiCRISPR v2, Addgene #52961) — pooled screen / stable KO

### 0.3 Foundational citations (cited throughout)
| ID | Citation | Use |
|---|---|---|
| **Guzman 2026** | Guzman SD, Fraczek PM, Itsani K, et al. *Age-Associated Dysregulation of Postsynaptic Mitochondria Perturbs Reinnervation Kinetics.* Aging Cell **2026**; 25(1):e70355. DOI: [10.1111/acel.70355](https://doi.org/10.1111/acel.70355). PMID [41496579](https://pubmed.ncbi.nlm.nih.gov/41496579); PMC [PMC12775679](https://pmc.ncbi.nlm.nih.gov/articles/PMC12775679/). | Precedent for CHCHD10 muscle-specific loss-of-function in vivo; informs Aim 2 KD interpretation |
| **Doench 2016** | Doench JG, Fusi N, Sullender M, et al. Optimized sgRNA design to maximize activity and minimize off-target effects of CRISPR-Cas9. *Nat Biotechnol* **2016**; 34(2):184–191. PMID [26780180](https://pubmed.ncbi.nlm.nih.gov/26780180). | On-target sgRNA scoring rationale; Doench 'Rule Set 2' |
| **Hsu 2013** | Hsu PD, Scott DA, Weinstein JA, et al. DNA targeting specificity of RNA-guided Cas9 nucleases. *Nat Biotechnol* **2013**; 31(9):827–832. PMID [23775266](https://pubmed.ncbi.nlm.nih.gov/23775266). | Off-target framework (seed-region tolerance) |
| **Sanjana 2014** | Sanjana NE, Shalem O, Zhang F. Improved vectors and genome-wide libraries for CRISPR screening. *Nat Methods* **2014**; 11(8):783–784. PMID [25075903](https://pubmed.ncbi.nlm.nih.gov/25075903). | lentiCRISPR v2 / GeCKO v2 design |
| **Slaymaker 2016** | Slaymaker IM, Gao L, Zetsche B, Scott DA, Yan WX, Zhang F. Rationally engineered Cas9 nucleases with improved specificity. *Science* **2016**; 351(6268):84–88. PMID [26628643](https://pubmed.ncbi.nlm.nih.gov/26628643). | eSpCas9(1.1) high-fidelity Cas9 |
| **Koike-Yusa 2014** | Koike-Yusa H, Li Y, Tan EP, Velasco-Herrera Mdel C, Yusa K. Genome-wide recessive genetic screening in mammalian cells with a lentiviral CRISPR-guide RNA library. *Nat Biotechnol* **2014**; 32(3):267–273. PMID [24535568](https://pubmed.ncbi.nlm.nih.gov/24535568). | pKLV-U6gRNA(BbsI)-PGKpuro2ABFP backbone |

### 0.4 Critical design principles
- **Same RefSeq for all modalities** of a given gene × species (e.g., human CHCHD10 work all references NM_001301339.2). This guarantees that KD/KO results are measuring the *same* molecular target.
- **PAM = NGG** for all sgRNAs unless GC content at the target site forces NAG or NGA. No special PAM substitutions anticipated for these four genes (none are in known GC-extreme loci).
- **Standard siRNA overhang = 3' dTdT** unless the platform specifies otherwise (Horizon siGENOME = UU overhang; Thermo Silencer Select = dTdT).
- **No de-novo siRNA sequence design.** All siRNA sequences are anchored to a **vendor catalogue or vendor design-tool output**. Where the exact catalog number is not confirmed at issue time, the **product family + TBD catalog** is stated (e.g., "Horizon siGENOME SMARTpool — Mouse — Cat# M-XXXXXX-02 [TBD]").
- **Off-target audit is mandatory.** The seed region (nt 2–8 of the guide strand) is explicitly screened against RefSeq for any perfect matches in off-target mRNAs with mitochondrial relevance.
- **KD acceptance gates are quantitative** (≥70 % mRNA, ≥50 % protein) and matched to the same RefSeq used to design the construct.

### 0.5 Notation and conventions
- **Mouse / human orthologs** are presented in **paired rows** within each per-gene section to make cross-species comparison explicit.
- **Coordinate notation:** RefSeq mRNA numbering is **1-based, inclusive** on the sense strand. CDS coordinates refer to the ATG start → stop codon (inclusive).
- **siRNA target site** shown as the 19-nt sense strand (5'→3') that anneals to the mRNA. 3' overhangs listed separately.
- **sgRNA spacer** shown as 20-nt protospacer (5'→3') followed by the PAM in parentheses.
- **GC%** is the **guide-spacer GC content** (not the full oligo) — relevant for Doench on-target scoring; vendor algorithms also report full-oligo GC% which is included when known.

---

## 1. CHCHD10 — Tier 1 lead (MICOS / cristae)

### 1.1 Background
CHCHD10 (coiled-coil-helix-coiled-coil-helix domain-containing protein 10) is a small (14 kDa) mitochondrial intermembrane-space protein enriched at **cristae junctions** where it interacts with the **MICOS (mitochondrial contact site and cristae organizing system)** complex. In the HMSR v0.4 meta-analysis it shows the **strongest cross-cohort signal** (β=−0.164, p=7.5×10⁻⁶, **I²=0 %** — i.e., zero between-study heterogeneity, the cleanest single-gene signal in the resource paper). Guzman et al. (Aging Cell 2026, PMID 41496579) showed that **muscle-specific CRISPR-KO of CHCHD10 (and CHCHD2)** in young adult mice **recapitulates aged-muscle phenotypes**: mitochondrial disorganization, reduced ATP, neuromuscular-junction (NMJ) fragmentation, and delayed reinnervation after nerve injury — directly validating the gene as a causal sarcopenia node and providing a published benchmark for the KD readout.

### 1.2 Reference transcript metadata
| Field | Mouse (*Chchd10*) | Human (*CHCHD10*) |
|---|---|---|
| **NCBI Gene ID** | 103172 | 400916 |
| **MGI / HGNC** | MGI:2143558 | HGNC:15559 |
| **Chromosome** | 10 (C57BL/6J) | 22q11.23 |
| **RefSeq mRNA (canonical, primary)** | **NM_001136064.2** (protein-coding) | **NM_001301339.2** → NP_001288268.1 (isoform a, full-length) |
| **RefSeq mRNA (alternative)** | — | NM_213720.3 → NP_998885.1 (isoform b precursor, shorter) |
| **CDS coordinates (mRNA)** | 117..533 (417 nt) — TBD; verify with vendor design tool | 158..574 (417 nt) — TBD; verify with vendor design tool |
| **Protein length** | 138 aa | 142 aa (isoform a) / 125 aa (isoform b) |
| **CCDS** | CCDS23938 | CCDS46699 |
| **Tissue expression (RPKM top)** | Heart, skeletal muscle, brain | Heart (RPKM 56.7), colon (43.9), 20+ tissues |
| **Disease associations (human)** | — | FTDALS2 (frontotemporal dementia / ALS2), SMAJ, IMMD; heterozygous missense mutations (e.g., p.S59L) |

> **Design note:** Mouse Chchd10 has 5 exons (4 coding) per Ensembl transcript ENSMUST00000219839.2; the ORFeome is short (138 aa). siRNA target sites are therefore **constrained** — for SMARTpool design this is fine (Horizon siGENOME pools four oligos against distinct regions of the same transcript), but it means that **all four oligos in the pool must map to the same 138-aa ORF**, increasing the chance of overlapping coverage and justifying an off-target audit (§1.5).

### 1.3 Per-modality construct table — CHCHD10 (mouse + human)

| Modality | Vendor / platform | Catalog # (suggested) | Target exon / sequence (5–25 nt) | GC% | Predicted KD efficiency | Validation cite (PMID) | Price (USD, oligos/pool) |
|---|---|---|---|---|---|---|---|
| siRNA SMARTpool (mouse) | Horizon Discovery (Dharmacon) siGENOME | **M-XXXXXX-02** [TBD — confirm at quote] | 4-oligo SMARTpool tiled across the 138-aa ORF; specific 19-mer sequences to be returned by Horizon design tool against **NM_001136064.2** | (vendor-reported; expected 35–55 % per oligo; pool average reported in QC) | ≥70 % mRNA KD at 50 nM, 48 h in C2C12 myotubes | Horizon siGENOME QC validation (general); muscle-KD precedent in Guzman 2026 (PMID [41496579](https://pubmed.ncbi.nlm.nih.gov/41496579)) | ~$450 / pool (1 nmol scale) |
| siRNA SMARTpool (human) | Horizon siGENOME | **M-XXXXXX-02** [TBD] | 4-oligo SMARTpool against **NM_001301339.2**; tiled over shared 3' CDS + 3'UTR | (vendor-reported) | ≥70 % mRNA KD at 50 nM, 48 h in HSMM | (same as above) | ~$450 / pool |
| siRNA individual validated (mouse) | Thermo Fisher / Ambion Silencer Select | **4XXXXX (sXXXXXX)** [TBD] | Single Silencer Select oligo (pre-validated by Thermo) targeting the 138-aa ORF region distinct from siGENOME pool, to allow independent confirmation | (vendor-reported; 30–55 % typical) | ≥70 % at 50 nM, 48 h | Thermo Silencer Select KD validation; cross-cite Guzman 2026 (PMID [41496579](https://pubmed.ncbi.nlm.nih.gov/41496579)) | ~$200 / oligo |
| siRNA individual validated (human) | Thermo Silencer Select | **4XXXXX (sXXXXXX)** [TBD] | Single validated Silencer Select oligo against NM_001301339.2 | (vendor-reported) | ≥70 % at 50 nM, 48 h | (same) | ~$200 / oligo |
| shRNA lentiviral, pLKO.1 (mouse) | Horizon MISSION TRC (pLKO.1-puro) | **TRC N00000XXXXXXX** [TBD — pick from TRC2 library; "validated" clones preferred, fallback to "unvalidated" with qPCR triage] | 21-nt sense + CTAAAGAC loop + 21-nt antisense; 5'-T anchor; mapped to NM_001136064.2 | (vendor-reported) | ≥70 % mRNA at 72 h post-transduction (MOI 0.3–0.5, 8 µg/mL polybrene) | TRC2 library validation (Moffat 2006, PMID [17180147](https://pubmed.ncbi.nlm.nih.gov/17180147)) | ~$350 (bacterial stock + sequencing) |
| shRNA lentiviral, pLKO.1 (human) | Horizon MISSION TRC | **TRC N00000XXXXXXX** [TBD] | As above, against NM_001301339.2 | (vendor-reported) | ≥70 % mRNA at 72 h | (same) | ~$350 |
| CRISPR sgRNA, IDT Alt-R (mouse) | IDT Alt-R CRISPR-Cas9 system (RNP delivery) | **Alt-R crRNA + tracrRNA, custom** [TBD at IDT order entry] | 20-nt spacer + NGG PAM, designed by **IDT's design tool** (top 3 picks; Doench 'Rule Set 2' on-target score ≥60; off-target Hsu 2013 specificity score ≥50) | (to be computed via IDT design tool) | ≥80 % indel at 72 h in C2C12; clonal KO to be derived | Doench 2016 (PMID [26780180](https://pubmed.ncbi.nlm.nih.gov/26780180)); Hsu 2013 (PMID [23775266](https://pubmed.ncbi.nlm.nih.gov/23775266)) | ~$250 (3 crRNAs + tracrRNA + Cas9 NLS V3) |
| CRISPR sgRNA, IDT Alt-R (human) | IDT Alt-R (RNP) | **Alt-R custom** [TBD] | As above, against NM_001301339.2 | (to be computed) | ≥80 % indel in HSMM | (same) | ~$250 |
| CRISPR sgRNA, lentiCRISPR v2 (mouse) | Addgene deposited plasmid #52961 + cloned sgRNA | **Plasmid #52961 (Zhang lab)** + 1 cloned sgRNA | sgRNA cloned into BsmBI site of lentiCRISPR v2 (Addgene #52961); 20-nt spacer + NGG | (cloned oligo GC) | Stable KO after puromycin selection (1–2 µg/mL, 7 d) | Sanjana 2014 (PMID [25075903](https://pubmed.ncbi.nlm.nih.gov/25075903)) | Plasmid $89; sgRNA cloning + sequencing ~$250; lentivirus production ~$2 K |
| CRISPR sgRNA, lentiCRISPR v2 (human) | Addgene #52961 | **Plasmid #52961** + cloned sgRNA | As above | (cloned oligo GC) | (same) | (same) | (same) |

### 1.4 Sequence-level deliverables — CHCHD10

#### 1.4.1 Mouse — *Chchd10* — NM_001136064.2
| Field | Value |
|---|---|
| **CDS start–stop (mRNA, 1-based)** | 117–533 (TBD — confirm from RefSeq flat file) |
| **siRNA target site (siGENOME SMARTpool oligo 1, sense, 5'→3', 19 nt + 3' dTdT)** | *TBD at design-tool output* — to be returned by Horizon design tool given **NM_001136064.2**. Target rule: avoid 5' UTR / first 5 nt of CDS; prefer 100–400 nt downstream of start; ≥3 nt gap from any 19-mer with 100 % identity to another mouse RefSeq mRNA. |
| **Seed region of siRNA (nt 2–8 of guide)** | *TBD after design tool returns sequences* — manual seed scan required (see §1.5) |
| **shRNA hairpin (5'-T-anchor; 21-nt sense + loop + 21-nt antisense)** | 5'-T-[21-nt sense from CDS, GC 40–55 %]-CTCGAG-[reverse complement of sense]-TTTTT-3' (or Horizon's preferred stem-loop format). Specific sequence TBD from TRC clone ID once selected. |
| **CRISPR sgRNA (top CRISPOR pick; 20-nt spacer + PAM)** | To be computed via [CRISPOR](http://crispor.tefor.net/) using **NM_001136064.2** as input. Required: **Doench 'Rule Set 2' on-target score ≥60**, **Hsu specificity score ≥50**, mitosome-relevant off-target audit. |
| **qPCR primer/probe (KD validation; FAM-MGB, exon-junction-spanning; 3' UTR-distal from siRNA target)** | TBD — to be designed with **Primer3** (or vendor Design Tool); target the **3' UTR ~200–500 nt downstream of CDS stop**, or a constitutive exon-exon junction (likely exon 2–3) of NM_001136064.2. Reference dye: VIC-MGB on *Rplp0* (mouse, [NM_007475.5](https://www.ncbi.nlm.nih.gov/nuccore/NM_007475.5)) or 18S rRNA. |
| **Western blot antibody** | Cross-reference `validation/antibodies/ANTIBODY_PANEL.md` (TBD) — recommended: rabbit anti-CHCHD10 polyclonal, e.g., **Proteintech 25671-1-AP** (RRID: AB_2880176, *Homo sapiens* + cross-reactivity claimed to *Mus musculus*), or **abcam ab121933**. Both have published characterizations in HEK293 / U2OS; validation in C2C12 myotubes is **required** before relying on the band (~14 kDa, near the dye front — run 15 % Tris-Tricine or 16 % SDS-PAGE; include 14-kDa marker). |
| **Predicted ORF / product size** | 138 aa; ~14.8 kDa (mature IMS form ~12 kDa after MTS cleavage) |

#### 1.4.2 Human — *CHCHD10* — NM_001301339.2
| Field | Value |
|---|---|
| **CDS start–stop (mRNA, 1-based)** | 158–574 (TBD — confirm from RefSeq flat file) |
| **siRNA target site (sense, 5'→3', 19 nt + 3' dTdT)** | *TBD at design-tool output* — input to Horizon: **NM_001301339.2**. Apply the same design rules as mouse. |
| **Seed region** | *TBD after design* |
| **shRNA hairpin** | As for mouse, mapped to NM_001301339.2 |
| **CRISPR sgRNA (20-nt spacer + NGG PAM)** | To be computed via CRISPOR using NM_001301339.2. Score thresholds: Doench ≥60, Hsu ≥50. For CHCHD10 we **recommend eSpCas9(1.1) (Addgene #71814 / T2A-Puro variant #101039) for the CRISPR arm in HSMM** because the gene is small and off-target effects in a near-saturation CRISPR screen would propagate into neighbouring MICOS transcripts. |
| **qPCR primer/probe** | TBD — target the 3' UTR or a constitutive exon-exon junction of NM_001301339.2. Reference: *RPLP0* (human, [NM_001002.5](https://www.ncbi.nlm.nih.gov/nuccore/NM_001002.5)) or 18S rRNA. |
| **Western blot antibody** | Proteintech 25671-1-AP (validated for human) or abcam ab121933; CHCHD10 ~14 kDa; **size caution as for mouse**. |
| **Predicted ORF / product size** | 142 aa; ~14.9 kDa (mature IMS form ~12 kDa) |

### 1.5 Off-target audit (illustrative, framework)
**Method:**
1. For each of the four siGENOME SMARTpool oligos (mouse and human) and the top 3 CRISPOR sgRNAs, **BLAST the 19-nt (siRNA) or 20-nt (sgRNA) guide sequence** against `refseq_mrna` (or `refseq_select` for speed) on NCBI, restricting to the matching species.
2. Require **no perfect 19/19 or 20/20 match to any off-target mRNA**. Flag any **18/19 or 19/20 + seed (nt 2–8) identity** with a mitochondrial mRNA of interest (MICOS complex members: CHCHD2, CHCHD3, CHCHD6, MICU1, MICU2, MICOS10/MIC10, IMMT/MIC60; mitoribosome subunits: MRPL34, MRPL33; biogenesis TFs: PPARGC1A, NRF1, GABPA, TFAM, ESRRA/ESRRG).
3. For sgRNAs, additionally run **CRISPOR's off-target audit** (which already implements Hsu 2013 scoring) and reject any guide with predicted exonic off-targets in the above list.
4. For sgRNAs, prefer protospacers in the **first 50 % of the CDS** to maximize functional KO (frameshift before coiled-coil domains), but tolerate downstream positions if they score better on specificity.

> **Caveat for CHCHD10.** The 138-aa ORF is short, and the coiled-coil domain is highly homologous to CHCHD2 (which is targeted alongside CHCHD10 in Guzman 2026). **Seed-region seed-only (nt 2–8) uniqueness must be explicitly checked** for both siRNA and sgRNA, and any guide with a seed match to *Chchd2* (mouse) / *CHCHD2* (human) should be **discarded or flagged** for downstream RNA-seq deconvolution. (Note: Guzman 2026 deliberately co-targets CHCHD2 + CHCHD10; for the single-gene Aim 2 test of CHCHD10 alone, this off-target is **unwanted**, and guides should be filtered to avoid it. This is a deliberate design choice for Aim 2 vs Guzman 2026's design.)

### 1.6 KD validation plan — CHCHD10
- **Cell line:** C2C12 (mouse myoblast, ATCC **CRL-1772**), myoblast → myotube differentiation to **d5** (2 % horse serum, daily media change); HSMM (human, primary; vendor options: Lonza **CC-2580** [SkMDC, *historical catalog*, possibly discontinued — confirm with vendor] or **PromoCell C-12530** Skeletal Muscle Cell Growth Medium kit; alternative: iPSC-derived myocytes from a CRO). Myotubes d5 in 6-well plates for RNA, 12-well for protein.
- **siRNA transfection:** **Lipofectamine RNAiMAX** (Thermo **13778075**), reverse-transfection at 50 nM SMARTpool or 50 nM individual oligo, d0 (myoblast) → readout d3 (48 h post-transfection, mRNA) and d5 (96 h post-transfection, protein). Confirm that **differentiated myotubes** (d5) retain KD at 72–96 h; if not, perform a **re-transfection on d3** to maintain KD through the myotube readout.
- **shRNA delivery:** Lentivirus at **MOI 0.3–0.5** with 8 µg/mL polybrene, 24 h spin-fection, then puromycin selection (1–2 µg/mL, 7 d) before differentiation.
- **CRISPR delivery:** lentiCRISPR v2 (Addgene #52961) lentivirus as above; or **IDT Alt-R RNP** (Cas9 NLS V3 + crRNA:tracrRNA) by nucleofection (Lonza 4D-Nucleofector, program **CM-138** for C2C12; **DS-150** for HSMM), 250 pmol Cas9 + 250 pmol sgRNA per 100 µL nucleofection cuvette, 1×10⁶ cells. Indel frequency measured by **T7E1 mismatch assay** or **amplicon-seq (ICE / Synthego)** at 72 h.
- **Readout:**
  - **mRNA:** RT-qPCR with **FAM-MGB probe**, ΔΔCt, normalized to **RPLP0** (mouse [NM_007475.5](https://www.ncbi.nlm.nih.gov/nuccore/NM_007475.5) / human [NM_001002.5](https://www.ncbi.nlm.nih.gov/nuccore/NM_001002.5)) or **18S rRNA**. **Acceptance gate: ≥70 % mRNA reduction** at 48 h (siRNA), 72 h (shRNA), 96 h (CRISPR clonal).
  - **Protein:** Western blot, anti-CHCHD10 (see §1.4), densitometry vs. **vinculin** (Millipore Sigma V9131, ~124 kDa) or **β-tubulin** (Cell Signaling 2146, ~55 kDa) loading control. **Acceptance gate: ≥50 % protein reduction** at 96 h (siRNA), 7 d (shRNA / CRISPR pool), 14 d (clonal KO).
- **Rescue control (Aim 3 hook-in):** siRNA-resistant **CHCHD10 cDNA** (silent mutations at the SMARTpool seed; codon-optimized) cloned into a dox-inducible lentivector (e.g., **pLVX-TetOne-Puro**, Takara **631847**). Co-transfected / co-transduced with the siRNA to confirm phenotype rescue — closes the off-target/seed concern at the wet-lab level.

---

## 2. NDUFB4 — Tier 2 (Complex I accessory, B15)

### 2.1 Background
NDUFB4 (NADH:ubiquinone oxidoreductase subunit B4; aka B15, CI-B15) is a small (~13–15 kDa) **accessory subunit of mitochondrial Complex I** (NADH dehydrogenase, the first enzyme of the electron transport chain). It is **non-catalytic** — i.e., it does not directly participate in electron transfer or proton pumping, but is required for proper Complex I assembly and/or stability. In the HMSR v0.4 resource, it was one of only **two true OXPHOS subunits** in the down-regulated gene set (the other being ATP5F1B); I²=47 % indicates modest between-study heterogeneity, but the effect direction is consistent. The biological rationale for targeting: a Complex I assembly defect should produce a **measurable drop in basal and maximal OCR** (Seahorse Mito Stress Test), with **preserved mtDNA copy number** (distinguishes it from mtDNA-depletion phenotypes), giving a clean OXPHOS-specific readout. This complements the cristae / MICOS read-out of CHCHD10 and the ATP-synthase read-out of ATP5F1B.

### 2.2 Reference transcript metadata
| Field | Mouse (*Ndufb4*) | Human (*NDUFB4*) |
|---|---|---|
| **NCBI Gene ID** | 68198 | 4710 |
| **MGI / HGNC** | MGI:1915453 | HGNC:7699 |
| **Chromosome** | 16 (C57BL/6J) | 3 |
| **RefSeq mRNA (canonical)** | **NM_026610.3** (protein-coding, single RefSeq transcript) | **NM_004547.6** (transcript variant 1; encodes the longer isoform 1, 129 aa) |
| **RefSeq mRNA (alternative)** | — | NM_001168331.2 (transcript variant 2; encodes isoform 2, 128 aa) |
| **CDS coordinates (mRNA)** | TBD from RefSeq flat file (~390 nt CDS) | TBD from RefSeq flat file (~390 nt CDS) |
| **Protein length** | 129 aa (mouse) | 129 aa (isoform 1, human); 128 aa (isoform 2) |
| **Conserved domain** | pfam07225 (NDUF_B4) | pfam07225 (NDUF_B4) |
| **Tissue expression (RPKM top)** | Ubiquitous; high in heart, kidney, oxidative muscle | Ubiquitous; high in adrenal (52.4), heart (52.2) |
| **Disease associations (human)** | — | Isolated Complex I deficiency reports (biallelic variants) |

> **Design note:** Like CHCHD10, NDUFB4 is a small gene with a short ORF (~130 aa, ~400 nt CDS). The pfam07225 domain is well-conserved across vertebrates, raising off-target concerns against any *Ndufb4* paralog (none in mouse or human — verified by RefSeq search). The accessory nature means that **partial KD may not be sufficient to drop OCR** — the acceptance gate may need to be tightened for NDUFB4 (≥80 % mRNA) before declaring "no phenotype" — this is a CRO-relevant nuance.

### 2.3 Per-modality construct table — NDUFB4 (mouse + human)

| Modality | Vendor / platform | Catalog # (suggested) | Target exon / sequence (5–25 nt) | GC% | Predicted KD efficiency | Validation cite (PMID) | Price (USD, oligos/pool) |
|---|---|---|---|---|---|---|---|
| siRNA SMARTpool (mouse) | Horizon siGENOME | **M-XXXXXX-02** [TBD] | 4-oligo SMARTpool tiled across the ~130-aa ORF (NM_026610.3) | (vendor-reported; expected 35–55 % per oligo) | ≥70 % mRNA at 50 nM, 48 h; may need ≥80 % for phenotype | siGENOME QC (general); complex I accessory subunit | ~$450 / pool |
| siRNA SMARTpool (human) | Horizon siGENOME | **M-XXXXXX-02** [TBD] | 4-oligo SMARTpool against NM_004547.6 (transcript variant 1) | (vendor-reported) | ≥70 % mRNA at 50 nM, 48 h | (same) | ~$450 / pool |
| siRNA individual validated (mouse) | Thermo Silencer Select | **4XXXXX (sXXXXXX)** [TBD] | Single validated oligo against NM_026610.3 | (vendor-reported) | ≥70 % at 50 nM, 48 h | Thermo Silencer Select validation | ~$200 |
| siRNA individual validated (human) | Thermo Silencer Select | **4XXXXX (sXXXXXX)** [TBD] | Single validated oligo against NM_004547.6 | (vendor-reported) | ≥70 % at 50 nM, 48 h | (same) | ~$200 |
| shRNA lentiviral, pLKO.1 (mouse) | Horizon MISSION TRC | **TRC N00000XXXXXXX** [TBD] | 21-nt sense + loop + 21-nt antisense, mapped to NM_026610.3 | (vendor-reported) | ≥70 % at 72 h (puro-selected) | TRC2 library (Moffat 2006, PMID [17180147](https://pubmed.ncbi.nlm.nih.gov/17180147)) | ~$350 |
| shRNA lentiviral, pLKO.1 (human) | Horizon MISSION TRC | **TRC N00000XXXXXXX** [TBD] | Same, mapped to NM_004547.6 | (vendor-reported) | ≥70 % at 72 h | (same) | ~$350 |
| CRISPR sgRNA, IDT Alt-R (mouse) | IDT Alt-R | **Alt-R crRNA + tracrRNA, custom** [TBD] | 20-nt spacer + NGG PAM, CRISPOR top pick from NM_026610.3 | (to be computed) | ≥80 % indel in C2C12 | Doench 2016 (PMID [26780180](https://pubmed.ncbi.nlm.nih.gov/26780180)); Hsu 2013 (PMID [23775266](https://pubmed.ncbi.nlm.nih.gov/23775266)) | ~$250 |
| CRISPR sgRNA, IDT Alt-R (human) | IDT Alt-R | **Alt-R custom** [TBD] | As above, against NM_004547.6 | (to be computed) | ≥80 % indel in HSMM | (same) | ~$250 |
| CRISPR sgRNA, lentiCRISPR v2 (mouse) | Addgene #52961 + cloned sgRNA | **Plasmid #52961** + 1 cloned sgRNA | 20-nt spacer + NGG, in BsmBI site of lentiCRISPR v2 | (cloned oligo GC) | Stable KO after puro selection | Sanjana 2014 (PMID [25075903](https://pubmed.ncbi.nlm.nih.gov/25075903)) | $89 + ~$250 + ~$2 K virus |
| CRISPR sgRNA, lentiCRISPR v2 (human) | Addgene #52961 | **Plasmid #52961** + cloned sgRNA | As above | (cloned oligo GC) | (same) | (same) | (same) |

### 2.4 Sequence-level deliverables — NDUFB4

#### 2.4.1 Mouse — *Ndufb4* — NM_026610.3
| Field | Value |
|---|---|
| **CDS start–stop (mRNA, 1-based)** | TBD from RefSeq flat file |
| **siRNA target site** | *TBD at design-tool output* (Horizon design tool against NM_026610.3) |
| **Seed region** | *TBD* |
| **shRNA hairpin** | *TBD from TRC clone selection* |
| **CRISPR sgRNA** | To be computed via [CRISPOR](http://crispor.tefor.net/) on NM_026610.3. Required: Doench 'Rule Set 2' ≥60, Hsu specificity ≥50. |
| **qPCR primer/probe** | TBD — target 3' UTR or constitutive exon-exon junction of NM_026610.3. Reference: *Rplp0* (mouse [NM_007475.5](https://www.ncbi.nlm.nih.gov/nuccore/NM_007475.5)) or 18S. |
| **Western blot antibody** | Cross-reference `validation/antibodies/ANTIBODY_PANEL.md` (TBD) — recommended: rabbit anti-NDUFB4, e.g., **Proteintech 15589-1-AP** (RRID: AB_2251470) or **GeneTex GTX85004**. NDUFB4 runs ~13–15 kDa — use 15 % Tris-Tricine. Cross-reactivity to C2C12 must be validated before deployment. |
| **Predicted ORF / product size** | 129 aa; ~14 kDa |

#### 2.4.2 Human — *NDUFB4* — NM_004547.6
| Field | Value |
|---|---|
| **CDS start–stop** | TBD |
| **siRNA target site** | *TBD at design-tool output* (against NM_004547.6) |
| **Seed region** | *TBD* |
| **shRNA hairpin** | *TBD from TRC clone* |
| **CRISPR sgRNA** | To be computed via CRISPOR on NM_004547.6. Note: ensure the sgRNA spacer overlaps **both transcript variants 1 and 2** (i.e., targets a constitutive exonic region), unless the experiment specifically requires variant-1-only targeting. |
| **qPCR primer/probe** | TBD — 3' UTR or constitutive exon junction of NM_004547.6. Reference: *RPLP0* (human [NM_001002.5](https://www.ncbi.nlm.nih.gov/nuccore/NM_001002.5)) or 18S. |
| **Western blot antibody** | Proteintech 15589-1-AP (human reactive) or GeneTex GTX85004; ~14 kDa. |
| **Predicted ORF / product size** | 129 aa (isoform 1); ~14 kDa |

### 2.5 Off-target audit (framework — same as §1.5)
1. BLAST siRNA / sgRNA guides against RefSeq mRNA (mouse or human).
2. Flag any 18/19 or 19/20 + seed (nt 2–8) match to:
   - **Other Complex I subunits** (NDUFA family, NDUFB family, NDUFS family, NDUFV family, NDUFAF factors) — to exclude unintended multi-subunit knockdown.
   - **Mitochondrial respiratory-chain assembly factors** (e.g., NDUFAF1, NDUFAF2, NDUFAF3, NDUFAF4, FOXRED1, ACAD9).
   - **Other OXPHOS complexes** (SDHA/B/C/D, UQCR family, COX family, ATP5 family) — for clarity of the Complex I-specific interpretation.
3. CRISPOR off-target audit for sgRNAs (Hsu 2013 framework, PMID [23775266](https://pubmed.ncbi.nlm.nih.gov/23775266)).

> **No paralog of NDUFB4 in mouse or human RefSeq** (verified by RefSeq search as of 2026-06). Off-target risk is therefore primarily to other Complex I subunits (mitigatable by seed-region uniqueness) and not to a paralog.

### 2.6 KD validation plan — NDUFB4
- **Cell line:** C2C12 d5 myotubes; HSMM d5 myotubes (vendor and culture conditions per §1.6).
- **Transfection / delivery:** Per §1.6 (RNAiMAX for siRNA, lentivirus for shRNA, Alt-R RNP / lentiCRISPR v2 for CRISPR).
- **Readout time points:** 48 h (mRNA), 96 h (protein), and — **critically — 96 h (Seahorse Mito Stress Test OCR)**.
- **Acceptance gates:**
  - **mRNA:** ≥70 % reduction (RT-qPCR, ΔΔCt vs *Rplp0*/*RPLP0*).
  - **Protein:** ≥50 % reduction (WB, anti-NDUFB4, normalized to vinculin / β-tubulin). *Note:* NDUFB4 protein may be destabilized by Complex I assembly defects even when its own mRNA is partially reduced — a near-complete loss at the protein level is consistent with the expected biology.
  - **Function (Seahorse):** ≥20 % drop in **basal OCR** or **maximal OCR** (FCCP-uncoupled) relative to non-targeting control, at matched cell number / protein. *This is the Aim 2 primary functional endpoint and the rationale for including NDUFB4 in the OXPHOS arm.*
- **Caveat for the CRO:** accessory subunits often show **steep threshold effects** (i.e., KD < 70 % may give no phenotype). Plan to use the strongest-validated SMARTpool + a deconvoluted individual oligo to confirm. If mRNA KD is achieved but protein/OCR is unchanged, this is itself a publishable mechanistic result (the gene is *not* the rate-limiting node in this setting).

---

## 3. ATP5F1B — Tier 2 (Complex V / ATP synthase F₁β)

### 3.1 Background
ATP5F1B (ATP synthase F₁ subunit beta; the catalytic β-subunit of mitochondrial ATP synthase / Complex V) is one of three β-subunits in the F₁ catalytic hexamer (3α / 3β). It contains the **catalytic sites for ATP synthesis / hydrolysis** and is **directly required for ATP output** of oxidative phosphorylation. In the HMSR v0.4 resource, ATP5F1B had the **largest effect size** of any of the three targeted genes (β=−0.221, p=3.5×10⁻³, I²=39 %); I² is moderate, indicating some between-study variation, but the direction is consistent. The biological rationale: KD/KO of ATP5F1B should produce the **most direct ATP-depletion phenotype** of the three Tier-1/2 genes, complementary to the cristae (CHCHD10) and Complex I (NDUFB4) read-outs. ATP5F1B is **the third-most-abundant mitochondrial protein** and is highly expressed in oxidative muscle — making it a good candidate for clean Western blot detection (band ~52 kDa).

### 3.2 Reference transcript metadata
| Field | Mouse (*Atp5f1b*) | Human (*ATP5F1B*) |
|---|---|---|
| **NCBI Gene ID** | 11947 | 506 |
| **MGI / HGNC** | MGI:107801 | HGNC:830 |
| **Chromosome** | 10 (C57BL/6J) | 12 |
| **RefSeq mRNA (canonical)** | **NM_016774.3** → NP_058054.2 (mitochondrial precursor) | **NM_001686.4** → NP_001677.2 (mitochondrial precursor) |
| **CDS coordinates (mRNA)** | TBD from RefSeq flat file (~1.6 kb CDS) | TBD from RefSeq flat file (~1.6 kb CDS) |
| **Protein length** | 529 aa (mature ~480 aa after MTS cleavage) | 529 aa (mature ~480 aa) |
| **Conserved domain** | PRK09280 (F0F1 ATP synthase subunit beta) | PRK09280 (F0F1 ATP synthase subunit beta) |
| **Tissue expression (RPKM top)** | Heart adult (RPKM 1957), kidney (1316), ubiquitous | Heart (RPKM 713.8), kidney (376), ubiquitous |
| **Aliases** | Atp5b | ATP5B; ATPMB; ATPSB; DYT38; HUMOP2; HEL-S-271 |
| **Disease associations (human)** | — | DYT38 (dystonia 38, autosomal dominant, missense mutations) |

> **Design note:** ATP5F1B is a *much* larger ORF (~1.6 kb) than CHCHD10 and NDUFB4 — siRNA / shRNA / sgRNA design has abundant target space. **CRISPR guides can be placed in the catalytic-site-encoding region** (which is well-conserved, so off-target screening against the bacterial *atpD* gene or plasmid-derived ATP synthase sequences — e.g., the HEK293 packaging plasmid — is essential to avoid spurious results). The mitochondrial precursor cleavage site is at residue ~48; sgRNAs targeting downstream of this will only affect the mature mitochondrial form.

### 3.3 Per-modality construct table — ATP5F1B (mouse + human)

| Modality | Vendor / platform | Catalog # (suggested) | Target exon / sequence (5–25 nt) | GC% | Predicted KD efficiency | Validation cite (PMID) | Price (USD, oligos/pool) |
|---|---|---|---|---|---|---|---|
| siRNA SMARTpool (mouse) | Horizon siGENOME | **M-XXXXXX-02** [TBD] | 4-oligo SMARTpool tiled across the ~1.6-kb CDS of NM_016774.3 | (vendor-reported) | ≥80 % mRNA at 50 nM, 48 h (large ORF → abundant target space → high KD achievable) | siGENOME QC (general); ATP5F1B is a high-expression, abundant protein — easy to detect residual | ~$450 / pool |
| siRNA SMARTpool (human) | Horizon siGENOME | **M-XXXXXX-02** [TBD] | 4-oligo SMARTpool against NM_001686.4 | (vendor-reported) | ≥80 % mRNA at 50 nM, 48 h | (same) | ~$450 / pool |
| siRNA individual validated (mouse) | Thermo Silencer Select | **4XXXXX (sXXXXXX)** [TBD] | Single Silencer Select oligo against NM_016774.3 | (vendor-reported) | ≥80 % at 50 nM, 48 h | Thermo Silencer Select validation | ~$200 |
| siRNA individual validated (human) | Thermo Silencer Select | **4XXXXX (sXXXXXX)** [TBD] | Single validated oligo against NM_001686.4 | (vendor-reported) | ≥80 % at 50 nM, 48 h | (same) | ~$200 |
| shRNA lentiviral, pLKO.1 (mouse) | Horizon MISSION TRC | **TRC N00000XXXXXXX** [TBD] | 21-nt sense + loop + 21-nt antisense, mapped to NM_016774.3 | (vendor-reported) | ≥80 % at 72 h (puro-selected) | TRC2 (Moffat 2006, PMID [17180147](https://pubmed.ncbi.nlm.nih.gov/17180147)) | ~$350 |
| shRNA lentiviral, pLKO.1 (human) | Horizon MISSION TRC | **TRC N00000XXXXXXX** [TBD] | Same, mapped to NM_001686.4 | (vendor-reported) | ≥80 % at 72 h | (same) | ~$350 |
| CRISPR sgRNA, IDT Alt-R (mouse) | IDT Alt-R | **Alt-R crRNA + tracrRNA, custom** [TBD] | 20-nt spacer + NGG PAM, CRISPOR top pick from NM_016774.3 | (to be computed) | ≥80 % indel in C2C12 | Doench 2016 (PMID [26780180](https://pubmed.ncbi.nlm.nih.gov/26780180)); Hsu 2013 (PMID [23775266](https://pubmed.ncbi.nlm.nih.gov/23775266)) | ~$250 |
| CRISPR sgRNA, IDT Alt-R (human) | IDT Alt-R | **Alt-R custom** [TBD] | As above, against NM_001686.4 | (to be computed) | ≥80 % indel in HSMM | (same) | ~$250 |
| CRISPR sgRNA, lentiCRISPR v2 (mouse) | Addgene #52961 + cloned sgRNA | **Plasmid #52961** + 1 cloned sgRNA | 20-nt spacer + NGG, in BsmBI site of lentiCRISPR v2 | (cloned oligo GC) | Stable KO after puro | Sanjana 2014 (PMID [25075903](https://pubmed.ncbi.nlm.nih.gov/25075903)) | $89 + ~$250 + ~$2 K virus |
| CRISPR sgRNA, lentiCRISPR v2 (human) | Addgene #52961 | **Plasmid #52961** + cloned sgRNA | As above | (cloned oligo GC) | (same) | (same) | (same) |

### 3.4 Sequence-level deliverables — ATP5F1B

#### 3.4.1 Mouse — *Atp5f1b* — NM_016774.3
| Field | Value |
|---|---|
| **CDS start–stop** | TBD from RefSeq flat file |
| **siRNA target site** | *TBD at design-tool output* (against NM_016774.3) |
| **Seed region** | *TBD* |
| **shRNA hairpin** | *TBD from TRC clone selection* |
| **CRISPR sgRNA** | To be computed via [CRISPOR](http://crispor.tefor.net/) on NM_016774.3. Required: Doench 'Rule Set 2' ≥60, Hsu specificity ≥50. **Recommend placing the sgRNA in an early exon (exon 2 or 3) to maximize the chance of a frameshift before the catalytic domain.** |
| **qPCR primer/probe** | TBD — 3' UTR or constitutive exon junction of NM_016774.3. Reference: *Rplp0* or 18S. |
| **Western blot antibody** | Cross-reference `validation/antibodies/ANTIBODY_PANEL.md` (TBD) — recommended: **Abcam ab14730** (anti-ATP5F1B / ATP5B, RRID: AB_301438; mouse + human + rat cross-reactive) at 1:1000, or **Cell Signaling 14308** at 1:1000. ATP5F1B runs at ~52 kDa; clean band, low background. |
| **Predicted ORF / product size** | 529 aa (precursor) / ~480 aa (mature) ; ~52 kDa (mature) |

#### 3.4.2 Human — *ATP5F1B* — NM_001686.4
| Field | Value |
|---|---|
| **CDS start–stop** | TBD |
| **siRNA target site** | *TBD at design-tool output* (against NM_001686.4) |
| **Seed region** | *TBD* |
| **shRNA hairpin** | *TBD from TRC clone* |
| **CRISPR sgRNA** | To be computed via CRISPOR on NM_001686.4. Score thresholds as above. |
| **qPCR primer/probe** | TBD — 3' UTR or constitutive exon junction of NM_001686.4. Reference: *RPLP0* or 18S. |
| **Western blot antibody** | Abcam ab14730 or Cell Signaling 14308; ~52 kDa. |
| **Predicted ORF / product size** | 529 aa / 480 aa mature; ~52 kDa |

### 3.5 Off-target audit (framework)
Same as §1.5 / §2.5. Specific off-target watch list for ATP5F1B:
- **Other Complex V (F₁F₀-ATP synthase) subunits:** ATP5F1A (α), ATP5F1C (γ), ATP5F1D (δ), ATP5F1E (ε), ATP5PB (b), ATP5MC1/2/3 (c-subunit), ATP5PD (d), ATP5PF (F6), ATP5PO (OSCP), ATP5PD (d), ATP5ME (e), ATP5IF1 (inhibitor), DMAC2L1. A guide with seed identity to any of these is to be **discarded**.
- **Mitochondrial DNA-encoded ATP synthase subunits** (ATP6, ATP8 — encoded on mtDNA, not in the nuclear genome; no siRNA / sgRNA off-target risk).
- **Bacterial ATP synthase β-subunit** (*atpD*) — irrelevant for mammalian cells unless the experiment uses HEK293 packaging lines; even then, the guide spacer has 0/20 identity to the bacterial sequence given the codon-level divergence.

### 3.6 KD validation plan — ATP5F1B
- **Cell line / culture:** Per §1.6 (C2C12 d5 myotubes; HSMM d5 myotubes).
- **Transfection / delivery:** Per §1.6.
- **Readout time points:** 48 h (mRNA), 96 h (protein), 96 h (Seahorse Mito Stress Test + ATP rate assay).
- **Acceptance gates:**
  - **mRNA:** ≥70 % reduction (RT-qPCR, ΔΔCt vs *Rplp0*/*RPLP0*).
  - **Protein:** ≥50 % reduction (WB, anti-ATP5F1B, normalized to vinculin / β-tubulin). Given the high baseline expression, complete loss of the 52-kDa band is the expected outcome of a successful KD/KO.
  - **Function (Seahorse + ATP rate):** ≥20 % drop in **basal OCR** or **maximal OCR** at matched cell number / protein. Additionally, **ATP-linked OCR** (i.e., the oligomycin-sensitive component) should be **selectively reduced** — this is the OXPHOS-specific ATP-synthesis signature and is the Aim 2 endpoint for the ATP5F1B arm.
- **Caveat for the CRO:** ATP5F1B has **bacterial orthologs** (*atpD* in *E. coli* packaging strains). Lentiviral packaging in HEK293T does not introduce off-target editing because the packaging plasmids do not contain nuclear-encoded *ATP5F1B* orthologs. However, **bacterial contamination of the plasmid DNA prep** (e.g., *E. coli* gDNA contamination) could in principle produce spurious amplicons in the off-target audit; this is mitigated by the standard endotoxin-free maxiprep + qPCR primer-BLAST specificity check.

---

## 4. PPARGC1A (PGC-1α) — master regulator

### 4.1 Background
PPARGC1A encodes the **PGC-1α coactivator**, the master transcriptional regulator of mitochondrial biogenesis. It co-activates **NRF1 / NRF2 (GABPA), TFAM, ERRα**, and downstream OXPHOS / mtDNA replication / import machinery. In the HMSR v0.4 resource, the entire programme is coordinately down in sarcopenic muscle; **PGC-1α is the upstream node that could in principle explain the entire pattern** if it is the master regulator. Aim 2's question for PGC-1α is therefore **categorical**: does knocking down PGC-1α in a myotube **reproduce the whole programme signature** (by RNA-seq, comparing the PGC-1α KD transcriptome to the sarcopenic-muscle transcriptome)? This is the "test-the-programme" arm.

### 4.2 Isoform biology — critical design constraint
PGC-1α is **not a single transcript**. There are at least **7 distinct isoforms** generated by alternative promoter usage and alternative splicing. The Aim 2 design must specify which isoform(s) to target, and why.

| Isoform | Aliases | Promoter / splicing | Protein (aa) | Function in muscle | KD strategy implication |
|---|---|---|---|---|---|
| **PGC-1α1** | PGC-1α, PGC-1α-a, PGC-1α-A, isoform 1 (canonical) | Proximal (canonical) promoter; full exons 1–13 | 797 aa (human) / 796 aa (mouse) | **Mitochondrial biogenesis master**; oxidative phenotype; the dominant "biogenesis" isoform in skeletal muscle | **Target this for the biogenesis-programme test (Aim 2 + Aim 3)** |
| **PGC-1α2** (Ruas 2016) | PGC-1α2 | Proximal promoter; alternative splicing skips exons 4–6 and 9–13 | 379 aa | Induced by **hypertrophic stimuli** (resistance exercise, β-adrenergic); role unclear; reportedly modulates cholesterol / lipid gene programs via alternative splicing | Off-target concern only; do not target |
| **PGC-1α3** (Ruas 2016) | PGC-1α3 | Proximal promoter; skips exons 4–6 and 9–13 (different 3' splice from α2) | 370 aa | Induced by hypertrophic stimuli; biological role poorly defined | Off-target concern only; do not target |
| **PGC-1α4** (Ruas 2016) | PGC-1α4 | Proximal promoter; novel exon 6 inclusion; premature stop at 266 aa | 266 aa | Induced by **resistance exercise**; drives **IGF-1 expression, myostatin suppression, muscle hypertrophy**; **independent of ERRα/γ**; confers cancer-cachexia resistance | Do not target — this is the "exercise / hypertrophy" isoform, orthogonal to the biogenesis programme |
| **PGC-1α-b** (Zhang 2009 / Ruas 2016) | PGC-1α-b | **Alternative promoter** ~14 kb upstream of proximal TSS; exons 1b spliced to shared exon 2 | 793 aa (shorter N-term by 4 aa) | Exercise-induced; biological role partially overlapping with PGC-1α1 | A guide targeting the shared C-terminal region (exons 7–13) will knock this down alongside PGC-1α1 |
| **PGC-1α-c** (Zhang 2009) | PGC-1α-c | Alternative promoter; novel N-terminus | 784 aa (N-term shorter by 13 aa) | Exercise-induced, alternative-promoter family | (Same) |
| **NT-PGC-1α** (NT-PGC-1α-a, -b, -c) | N-terminal truncated | Internal promoter in intron 2 / 3 | Truncated N-term; lacks the canonical N-terminal activation domain | Highly expressed in skeletal muscle; regulates **alternative splicing** of target genes; may be **the major fraction of total PGC-1α mRNA in muscle** (per Miura 2008, [PMID 18508778](https://pubmed.ncbi.nlm.nih.gov/18508778); Ydfors 2014, [PMID 24905947](https://pubmed.ncbi.nlm.nih.gov/24905947)) | A guide targeting the 3' end will NOT knock this down; a guide targeting the shared N-terminal region will |

> **RefSeq framing:** the human PPARGC1A locus encodes **>30 transcript variants** (NCBI RefSeq). The canonical mRNA **NM_013261.5** (transcript variant 2) encodes the **PGC-1α1 / PGC-1α-a** protein. This is the **biogenesis master** form. The mouse canonical mRNA is **NM_008904.3** (and CCDS40937.1). All Aim 2 + Aim 3 work is anchored to these two RefSeq IDs.

### 4.3 Design decision — which isoform to target

| Question | Decision | Rationale |
|---|---|---|
| Target the **biogenesis master**? | **YES — target PGC-1α1 (canonical, NM_013261.5 / NM_008904.3)** | This is the isoform that drives the biogenesis programme. Knocking it down tests the central Aim 3 hypothesis. |
| Use a **pan-PGC-1α** guide? | **NO** — that would knock down PGC-1α4 and confound interpretation with the hypertrophy programme. | Aim 2 + 3 are about biogenesis, not hypertrophy. |
| Knock down **all proximal-promoter isoforms (PGC-1α1, -α2, -α3, -α4)**? | **NO** — Aim 2 only needs the biogenesis form knocked down. | PGC-1α2/3/4 are induced by hypertrophic stimuli that are absent in the C2C12 myotube (basal) setting. |
| Knock down **all alternative-promoter isoforms (PGC-1α-b, -c, NT)**? | **NO** — these are differentially regulated and their biology is not part of the Aim 2 question. | Including them would broaden the phenotype beyond the biogenesis programme. |
| Rescue construct for Aim 3? | **YES — re-express PGC-1α1 (or a constitutively active truncation like PGC-1α1-ΔNT)** under the siRNA-resistant silent-mutant cDNA. | This closes the off-target/seed concern and tests whether restoring one isoform is sufficient to recover the programme. |

> **Concrete target design:** siRNA / shRNA / sgRNA target a region in **exon 5 or 6 of the canonical PGC-1α1 (NM_013261.5 / NM_008904.3)** that is **constitutive across PGC-1α1 only** (i.e., not shared with PGC-1α4's truncated reading frame, and not shared with the alternative-promoter 5' UTRs). Validate isoform selectivity at the readout stage with **isoform-specific qPCR** (one probe against exon 1a-derived 5' UTR = PGC-1α1; one against exon 1b-derived = PGC-1α-b; one against the PGC-1α4 splice junction).

### 4.4 Reference transcript metadata
| Field | Mouse (*Ppargc1a*) | Human (*PPARGC1A*) |
|---|---|---|
| **NCBI Gene ID** | 19017 | 10891 |
| **MGI / HGNC** | MGI:1342774 | HGNC:9237 |
| **Chromosome** | 5 (C57BL/6J) | 4p15.2 |
| **RefSeq mRNA (canonical, PGC-1α1)** | **NM_008904.3** → NP_032944.2 | **NM_013261.5** → NP_037393.1 (transcript variant 2, encodes PGC-1α1 / PGC-1α-a) |
| **CDS coordinates (mRNA)** | TBD from RefSeq flat file (~2.4 kb CDS) | TBD from RefSeq flat file (~2.4 kb CDS) |
| **Protein length** | 796 aa (mouse PGC-1α1) | 797 aa (human PGC-1α1, NP_037393.1) |
| **CCDS** | CCDS40937 | CCDS47065 |
| **Tissue expression (RPKM top)** | Heart, BAT, skeletal muscle (oxidative > glycolytic), brain | Heart, kidney, skeletal muscle, BAT |
| **Aliases** | PGC-1; Pgc-1alpha; Pgc1; Pgco1; PPARGC-1-alpha; A830037N07Rik; ENSMUSG00000079510; Gm11133 | LEM6; L-PGC-1alpha; PGC-1; PGC-1α; PGC1A; PGC-1v; PPARGC-1-alpha; PPARGC; PPARGC1 |

> **Design note:** Like ATP5F1B, PGC-1α1 has a large ORF (~2.4 kb CDS) and abundant target space. **Critical care:** the C-terminal region is shared with PGC-1α-b and PGC-1α-c (alternative promoter transcripts); the N-terminal region is shared with PGC-1α2/3 (proximal-promoter alternative-splice forms). To restrict the KD to PGC-1α1 only, **target a region that is present in PGC-1α1 but absent from PGC-1α2/3/4** (i.e., a region that PGC-1α2/3 skip or PGC-1α4 truncates). The cleanest is the **exon 7–8 junction** (PGC-1α2/3 skip this; PGC-1α4 truncates before it; PGC-1α-b/c also include it but are alternative-promoter transcripts that are low-abundance in the basal myotube). Validate with isoform-specific qPCR as above.

### 4.5 Per-modality construct table — PPARGC1A (mouse + human)

| Modality | Vendor / platform | Catalog # (suggested) | Target exon / sequence (5–25 nt) | GC% | Predicted KD efficiency | Validation cite (PMID) | Price (USD, oligos/pool) |
|---|---|---|---|---|---|---|---|
| siRNA SMARTpool (mouse) | Horizon siGENOME | **M-XXXXXX-02** [TBD] | 4-oligo SMARTpool, each oligo mapped to **PGC-1α1-only region** (e.g., exon 7–8) of **NM_008904.3** | (vendor-reported) | ≥70 % PGC-1α1 mRNA at 50 nM, 48 h; **isoform specificity confirmed by isoform qPCR** | siGENOME QC (general); PGC-1α1 reference: Puigserver 1998 ([PMID 9799792](https://pubmed.ncbi.nlm.nih.gov/9799792)); Ruas 2016 ([PMID 27145836](https://pubmed.ncbi.nlm.nih.gov/27145836)) for α4 differentiation; Ydfors 2014 ([PMID 24905947](https://pubmed.ncbi.nlm.nih.gov/24905947)) for NT-PGC-1α | ~$450 / pool |
| siRNA SMARTpool (human) | Horizon siGENOME | **M-XXXXXX-02** [TBD] | 4-oligo SMARTpool against PGC-1α1 region of **NM_013261.5** | (vendor-reported) | ≥70 % PGC-1α1 mRNA at 50 nM, 48 h | (same) | ~$450 / pool |
| siRNA individual validated (mouse) | Thermo Silencer Select | **4XXXXX (sXXXXXX)** [TBD] | Single Silencer Select oligo against PGC-1α1 of NM_008904.3 | (vendor-reported) | ≥70 % at 50 nM, 48 h | (same) | ~$200 |
| siRNA individual validated (human) | Thermo Silencer Select | **4XXXXX (sXXXXXX)** [TBD] | Single validated oligo against PGC-1α1 of NM_013261.5 | (vendor-reported) | ≥70 % at 50 nM, 48 h | (same) | ~$200 |
| shRNA lentiviral, pLKO.1 (mouse) | Horizon MISSION TRC | **TRC N00000XXXXXXX** [TBD] | 21-nt sense + loop + 21-nt antisense, mapped to PGC-1α1 of NM_008904.3 | (vendor-reported) | ≥70 % PGC-1α1 mRNA at 72 h (puro-selected) | TRC2 (Moffat 2006, PMID [17180147](https://pubmed.ncbi.nlm.nih.gov/17180147)) | ~$350 |
| shRNA lentiviral, pLKO.1 (human) | Horizon MISSION TRC | **TRC N00000XXXXXXX** [TBD] | Same, mapped to PGC-1α1 of NM_013261.5 | (vendor-reported) | ≥70 % at 72 h | (same) | ~$350 |
| CRISPR sgRNA, IDT Alt-R (mouse) | IDT Alt-R | **Alt-R crRNA + tracrRNA, custom** [TBD] | 20-nt spacer + NGG PAM, CRISPOR top pick from PGC-1α1 region of NM_008904.3 (e.g., exon 7–8) | (to be computed) | ≥80 % indel in C2C12 | Doench 2016 (PMID [26780180](https://pubmed.ncbi.nlm.nih.gov/26780180)); Hsu 2013 (PMID [23775266](https://pubmed.ncbi.nlm.nih.gov/23775266)) | ~$250 |
| CRISPR sgRNA, IDT Alt-R (human) | IDT Alt-R | **Alt-R custom** [TBD] | As above, against NM_013261.5 | (to be computed) | ≥80 % indel in HSMM | (same) | ~$250 |
| CRISPR sgRNA, lentiCRISPR v2 (mouse) | Addgene #52961 + cloned sgRNA | **Plasmid #52961** + 1 cloned sgRNA | 20-nt spacer + NGG, in BsmBI site of lentiCRISPR v2 | (cloned oligo GC) | Stable KO after puro | Sanjana 2014 (PMID [25075903](https://pubmed.ncbi.nlm.nih.gov/25075903)) | $89 + ~$250 + ~$2 K virus |
| CRISPR sgRNA, lentiCRISPR v2 (human) | Addgene #52961 | **Plasmid #52961** + cloned sgRNA | As above | (cloned oligo GC) | (same) | (same) | (same) |
| **Rescue (Aim 3 hook-in): Ad-PGC-1α1 over-expression** | **Vector Biolabs Ad-Ppargc1a (mouse)** or **Ad-PPARGC1A (human)** | **Ad-m-Ppargc1a: ADV-280991** (RefSeq NM_008904; Vector Biolabs); **Ad-h-PPARGC1A: ADV-219511** (RefSeq NM_013261; Vector Biolabs). [User's spec said "Ad-PGC-1α, Vector Biolabs, #1047" — that is an older catalog ID; the current catalog numbers are **ADV-280991 (mouse)** and **ADV-219511 (human)**. Confirm at order time.] | Ready-to-use recombinant adenovirus (Ad5 backbone, CMV promoter) expressing the canonical PGC-1α1 cDNA. Optional GFP reporter available. | n/a | Constitutive over-expression; aim for 2–5× endogenous PGC-1α1 mRNA | Vector Biolabs product datasheet; multiple peer-reviewed uses of Ad-PGC-1α in C2C12 (e.g., Wu 1999, PMID [10567225](https://pubmed.ncbi.nlm.nih.gov/10567225); Zechner 2010, PMID [20007965](https://pubmed.ncbi.nlm.nih.gov/20007965)) | ~$1,500–2,500 per construct (1×10¹⁰ PFU scale); lead time 4–5 weeks |
| **Rescue: siRNA-resistant CHCHD10 cDNA (Aim 3)** | Custom GeneArt (Thermo Fisher) or GenScript | Cat# TBD | Codon-optimized CHCHD10 cDNA with silent mutations at the SMARTpool seed region; cloned into **pLVX-TetOne-Puro** (Takara **631847**) for dox-inducible expression | n/a | Inducible over-expression; time-course to test rescue of Aim 2 CHCHD10-KD phenotype | (Aim 3 design — not Aim 2 deliverable) | ~$2 K (gene synthesis + cloning + sequence verification) |

### 4.6 Sequence-level deliverables — PPARGC1A

#### 4.6.1 Mouse — *Ppargc1a* (PGC-1α1) — NM_008904.3
| Field | Value |
|---|---|
| **CDS start–stop** | TBD from RefSeq flat file |
| **siRNA target site (PGC-1α1-selective; sense, 19 nt + 3' dTdT)** | *TBD at design-tool output* (against NM_008904.3). **Target rule: design at least 2 of the 4 SMARTpool oligos in the exon 7–8 region**, which is constitutive for PGC-1α1 but skipped by PGC-1α2/3 and truncated in PGC-1α4. |
| **Seed region** | *TBD* |
| **shRNA hairpin** | *TBD from TRC clone selection* — confirm that the chosen TRC clone maps to PGC-1α1 (not PGC-1α2/3/4 or the 5' UTR of PGC-1α-b/c). |
| **CRISPR sgRNA (PGC-1α1-selective)** | To be computed via [CRISPOR](http://crispor.tefor.net/) on NM_008904.3. Required: Doench 'Rule Set 2' ≥60, Hsu specificity ≥50. **Recommend placing the sgRNA in an early exon (exon 3 or 4) of PGC-1α1** (before the PGC-1α2/3 splice skip) so that the resulting frameshift KO affects PGC-1α1 but not the alternative isoforms. |
| **Isoform-specific qPCR primers (KD validation; required for PGC-1α)** | TBD — at minimum, three qPCR assays: (i) **exon 1a-derived 5' UTR** → PGC-1α1; (ii) **exon 1b-derived 5' UTR** → PGC-1α-b/-c; (iii) **PGC-1α4 splice junction** (exon 6 inclusion) → PGC-1α4. This is **non-negotiable** for the PGC-1α arm — the biogenesis-programme interpretation depends on showing PGC-1α1 knockdown without confounding PGC-1α4 or PGC-1α-b/c co-knockdown. Reference: *Rplp0* or 18S. |
| **Western blot antibody (PGC-1α1)** | Cross-reference `validation/antibodies/ANTIBODY_PANEL.md` (TBD) — recommended: **Cell Signaling 2178** (anti-PGC-1α, clone D-5, mouse + human) at 1:1000, RRID: AB_823580; or **Millipore Sigma ST1202** (anti-PGC-1α, clone 4C1.3) at 1:1000. PGC-1α1 runs at ~105 kDa (a high-MW band; care needed for transfer efficiency). **Note:** the Cell Signaling 2178 antibody detects a band at ~105 kDa that has been reported to cross-react with other proteins of similar size in some lysates; **validate with positive control (PGC-1α1 over-expression lysate from Ad-PGC-1α1) and negative control (PGC-1α1 KO lysate from CRISPR arm)** before committing to a single antibody. |
| **Predicted ORF / product size** | 796 aa; ~105 kDa (full-length PGC-1α1) |

#### 4.6.2 Human — *PPARGC1A* (PGC-1α1) — NM_013261.5
| Field | Value |
|---|---|
| **CDS start–stop** | TBD |
| **siRNA target site (PGC-1α1-selective)** | *TBD at design-tool output* (against NM_013261.5) |
| **Seed region** | *TBD* |
| **shRNA hairpin** | *TBD from TRC clone* — confirm PGC-1α1 mapping. |
| **CRISPR sgRNA (PGC-1α1-selective)** | To be computed via CRISPOR on NM_013261.5. Score thresholds as above. **Recommend early exon placement (exon 3 or 4) to ensure the frameshift affects only PGC-1α1, not PGC-1α2/3/4.** |
| **Isoform-specific qPCR primers** | TBD — same three-assay strategy as for mouse, mapped to NM_013261.5. Reference: *RPLP0* or 18S. |
| **Western blot antibody** | Cell Signaling 2178 or Millipore Sigma ST1202; ~105 kDa. **Validation with positive/negative controls as for mouse.** |
| **Predicted ORF / product size** | 797 aa; ~105 kDa |

### 4.7 Off-target audit (framework, with PGC-1α-specific notes)
1. **BLAST guide sequences against mouse / human RefSeq mRNA.** The C-terminal portion of PGC-1α1 shares identity with PGC-1α-b and PGC-1α-c, so guides placed in the 3' end of the CDS will have seed matches to these alternative-promoter isoforms — this is a **known, designable off-target**. Either accept it (PGC-1α-b/c are low-abundance in basal myotubes; qPCR confirms) or move the guide to the PGC-1α1-specific region.
2. **PGC-1α family:** there is **PGC-1β (PPARGC1B)** — a paralog with ~30 % protein identity. A 19-nt guide with **any seed match to PPARGC1B is to be discarded.** PGC-1β regulates a partially overlapping gene programme (mitochondrial biogenesis in some contexts), and an off-target KD would conflate the Aim 3 interpretation.
3. **PRC (PGC-1-related coactivator, PPARGC1A-as1 / LINC01578)** — a long non-coding RNA antisense to PGC-1α. No off-target risk for siRNA / sgRNA unless the guide has 100 % complementarity to a 19-nt stretch of the lncRNA; BLAST the guide (sense strand) and reject if present.
4. **Mitochondrial off-targets** — none expected, since PGC-1α is nuclear-encoded and has no mtDNA-complementary sequence.
5. **CRISPOR off-target audit** (Hsu 2013 framework) for sgRNAs.

### 4.8 KD validation plan — PPARGC1A
- **Cell line / culture:** Per §1.6 (C2C12 d5 myotubes; HSMM d5 myotubes). The basal myotube state has low PGC-1α-b/c and PGC-1α4 expression, so the PGC-1α1-selective design is well-matched to the cell model.
- **Transfection / delivery:** Per §1.6.
- **Readout time points:** 48 h (mRNA), 96 h (protein), 96 h (Seahorse + **RNA-seq for programme signature** — this is the Aim 3 endpoint).
- **Acceptance gates:**
  - **mRNA:** ≥70 % reduction in **PGC-1α1** (isoform-specific qPCR, exon 1a-derived 5' UTR probe). **No requirement** on PGC-1α2/3/4 / PGC-1α-b/c (these should be unaffected).
  - **Protein:** ≥50 % reduction in the ~105-kDa PGC-1α1 band, normalized to vinculin / β-tubulin. **Validate the band identity** with positive (Ad-PGC-1α1) and negative (CRISPR KO) controls.
  - **Function (Seahorse):** ≥20 % drop in **basal OCR** or **maximal OCR** at matched cell number / protein. The PGC-1α1 KD is expected to produce the **broadest OCR phenotype** of the four genes, as it sits upstream of the entire OXPHOS / biogenesis programme.
  - **Programme signature (RNA-seq, Aim 3 endpoint):** the PGC-1α1 KD transcriptome should correlate with the sarcopenic-muscle signature from the v0.4 resource (Spearman ρ on log₂FC vs. log₂FC for the curated mitochondrial programme; target r ≥ 0.5 across the programme).
- **Caveat for the CRO:** PGC-1α1 mRNA has a short half-life (~30 min in some settings, per Puigserver 2001); the KD can be more rapid than for stable proteins, but the **protein** has a much longer half-life (~6–12 h), so 96 h is the right protein readout. If the protein band does not decrease, **extend the readout to 7 d** with shRNA / lentiCRISPR v2 selection.

---

## 5. Vector & control design (consolidated)

### 5.1 shRNA knockdown vector backbone
| Item | Selection | Notes |
|---|---|---|
| **Primary backbone** | **pLKO.1-puro** (Addgene **#10878**, Moffat 2006) or **pLKO.1-TRC cloning vector** (Addgene **#21915**, MISSION TRC) | The MISSION TRC library uses pLKO.1-puro backbone with the **1.6-kb stuffer** that is replaced with the shRNA hairpin via **AgeI / EcoRI** cloning. Sequencing primer: **LKO.1 5' (5'-GACTATCATATGCTTACCGT-3')**. |
| **Alternative backbone (Trono lab)** | **pLVTHM** (Addgene **#12247**, Wiznerowicz & Trono 2003) | Co-expresses **shRNA + eGFP** from the H1 promoter (Pol III) and EF1α (Pol II); useful when both KD and live-cell tracking are needed. Lentiviral; 3rd-generation packaging. |
| **MCS / cloning sites** | pLKO.1: **AgeI / EcoRI** for shRNA cloning; **BamHI / NcoI / PstI** in the human U6 shRNA-flanking region; **NdeI / XhoI** flank the 1.6-kb stuffer | (Standard pLKO.1 map) |
| **Selection marker** | **PuroR** (puromycin N-acetyl-transferase) from the **hPGK** promoter; working concentration **1–2 µg/mL** for C2C12, **0.5–1 µg/mL** for HSMM | (Kill curve per cell line required) |
| **Reporter (optional)** | **copGFP** (copepod GFP) or **mCherry** cloned under the **EF1α** promoter (IRES- or T2A-linked to PuroR) | Recommended for the **AAV9-shRNA in-vivo arm (Exp B)** where transduction efficiency must be tracked in vivo by IHC; not required for in-vitro C2C12 / HSMM. |
| **Lentiviral packaging** | **psPAX2** (Addgene **#12260**) + **pMD2.G** (Addgene **#12259**, VSV-G envelope) in **HEK293T** (ATCC **CRL-3216**); harvest at 48 h + 72 h; 0.45 µm filter; ultracentrifuge or Lenti-X Concentrator (Takara **631231**); titre by Lenti-X p24 rapid titre (Takara **632200**) or qPCR (ABM **LV900**). | Standard 3rd-generation packaging |

### 5.2 CRISPR vector backbone
| Item | Selection | Notes |
|---|---|---|
| **Primary backbone (pooled screen / stable KO)** | **lentiCRISPR v2-Puro** (Addgene **#52961**, Sanjana 2014, [PMID 25075903](https://pubmed.ncbi.nlm.nih.gov/25075903)) | Replaces lentiCRISPRv1 (Addgene #49535); produces ~10× higher titer virus. Third-generation lentiviral backbone. **Cloning sites: BsmBI** for sgRNA spacer (AgeI / XbaI / AfeI / BamHI / MluI flank). Sequencing primers: **hU6-F (5'-GAGGGCCTATTTCCCATGATT-3')** for the sgRNA, or **LKO.1 5' (5'-GACTATCATATGCTTACCGT-3')** for the upstream region. Vector size 14,873 bp. **E. coli selection: ampicillin (100 µg/mL).** |
| **Alternative backbone (FACS-based selection)** | **lentiCRISPR v2-mCherry** (Addgene **#99154**, generated by Sanjana / Zhang lab) or **lentiCRISPR v2-GFP** (Addgene **#82416**) | For experiments where FACS-based enrichment of mCherry+ or GFP+ transduced cells is required (e.g., primary myoblasts with low lentiviral transduction efficiency). |
| **High-fidelity Cas9 option (recommended for CHCHD10)** | **eSpCas9(1.1)** in **px330** (Addgene **#71814**, Slaymaker 2016 [PMID 26628643](https://pubmed.ncbi.nlm.nih.gov/26628643)) or **eSpCas9(1.1)-T2A-Puro** (Addgene **#101039**, Németh lab, unpublished) | eSpCas9(1.1) reduces off-target effects while maintaining robust on-target cleavage. **Recommended for CHCHD10** because the small ORF makes off-target mitigation especially important. Note: the user's spec cites **#101039** specifically; **#71814** is the original Slaymaker construct (px330-based, no T2A-Puro); the user should choose based on whether a puromycin-selection version is desired. |
| **Standard Cas9** | **SpCas9** in lentiCRISPR v2 (Addgene #52961) is sufficient for NDUFB4, ATP5F1B, and PGC-1α1 given their larger ORFs and lower off-target risk profile. | |
| **Cas9 delivery format** | RNP (preferred for in-vitro, lower off-target than plasmid) — IDT **Alt-R Cas9 Nuclease V3** (IDT **1081058**) + crRNA + tracrRNA. Plasmid / lentivirus for stable lines. | |

### 5.3 Non-targeting controls
| Item | Catalog # | Notes |
|---|---|---|
| **siRNA — scrambled / non-targeting** | **ON-TARGETplus Non-Targeting Pool** (Horizon Discovery / Dharmacon) — **D-001810-10-05** (4-oligo pool, 5 nmol). User's spec confirmed. | Pool of 4 non-targeting oligos; "guaranteed to not target any known mouse or human gene"; chemically modified (ON-TARGETplus = patent-pending modifications reducing off-target without sacrificing on-target). |
| **siRNA — individual scrambled** | **ON-TARGETplus Non-Targeting** (single oligo) — **D-001810-01-05** or **D-001810-02-05** (depending on scale) | For individual-oligo control conditions. |
| **shRNA — non-targeting** | **MISSION pLKO.1-puro Non-Target shRNA** (Horizon Discovery) — **SHC002** (5 nmol); or **SHC202** (SHC002 with copGFP reporter) | Standard pLKO.1 scramble; sequence: 5'-CCGGCAACAAGATGAAGAGCACCAACTC-3' (sense) per Horizon datasheet. |
| **CRISPR — non-targeting sgRNA** | **pKLV-U6gRNA(BbsI)-PGKpuro2ABFP** (Addgene **#50946**, Yusa / Koike-Yusa 2014, [PMID 24535568](https://pubmed.ncbi.nlm.nih.gov/24535568)) — empty gRNA cloning vector with PuroR + BFP. *User's spec said #80263; the verified plasmid is #50946 (the original Yusa construct); the improved version with an updated scaffold is pKLV2-U6gRNA5(BbsI)-PGKpuro2ABFP-W (Addgene **#67974**). For the basic non-targeting control, **#50946** or **#67974** are appropriate; the original spec's #80263 should be verified at order time — a different non-targeting control vector with that ID may exist (TBD).* | The Yusa lab's pooled-library control sgRNAs are commonly used; the top-100 non-targeting sgRNAs from their library are validated. |
| **CRISPR — non-targeting control sgRNA sequence** | Recommended: **5'-GACCGGAACGATCTCGCGTA-3'** (Addgene's recommended scramble; widely used) — cloned into lentiCRISPR v2 BsmBI site | T7E1 / amplicon-seq confirmed to not cut human or mouse RefSeq at any site with ≤4 mismatches |
| **Lentiviral packaging control** | **pLKO.1 empty vector** (no shRNA insert) + **lentiCRISPR v2 no-sgRNA** (no spacer ligated) | Process controls for viral production |

### 5.4 Rescue constructs (Aim 3 hook-in)
| Construct | Vendor / catalog | Purpose | Notes |
|---|---|---|---|
| **Ad-m-Ppargc1a (mouse PGC-1α1 over-expression)** | Vector Biolabs **ADV-280991** (RefSeq NM_008904; current catalog). User's spec said "Ad-PGC-1α #1047" — that is an older catalog ID; **ADV-280991 is the current Vector Biolabs mouse PGC-1α1 over-expression adenovirus**; please confirm at order time. | Aim 3: re-express PGC-1α1 to test whether restoring the master regulator rescues the Aim 2 KD phenotype. | Ready-to-use Ad5-CMV-PGC-1α1; optional GFP reporter; 1×10¹⁰ PFU/mL; ~$1,500–2,500. Lead time 4–5 weeks. |
| **Ad-h-PPARGC1A (human PGC-1α1 over-expression)** | Vector Biolabs **ADV-219511** (RefSeq NM_013261 + 4 other PGC-1α1 variants). User's spec said "Ad-PGC-1α #1047" — the human equivalent is **ADV-219511** in Vector Biolabs' current catalog. Confirm at order time. | Aim 3: human rescue in HSMM | (Same as above) |
| **siRNA-resistant CHCHD10 cDNA** | Custom synthesis (GeneArt / GenScript) — codon-optimized, silent mutations at the SMARTpool seed; cloned into **pLVX-TetOne-Puro** (Takara **631847**) for dox-inducible expression | Aim 3: rescue of CHCHD10 KD phenotype; closes the off-target/seed concern at the wet-lab level. | ~$2 K (gene synthesis + cloning + sequence verification) |
| **siRNA-resistant NDUFB4 / ATP5F1B cDNA** | Custom synthesis — same workflow as CHCHD10 cDNA. | Aim 3: rescue of OXPHOS-subunit KD phenotype | (Same) |

### 5.5 Reporter / cell-handling controls
- **Myogenic differentiation control:** *MYH1E* / *Myh1* (myosin heavy chain IIX) and *MYH2* / *Myh2* (IIA) qPCR at d0, d3, d5, d7 to confirm differentiation trajectory.
- **Mitochondrial content / function controls:** *MT-ND1* / *mt-Nd1* (mtDNA-encoded Complex I) qPCR for mtDNA copy number; *TFAM* / *Tfam* (mouse [NM_009360.4](https://www.ncbi.nlm.nih.gov/nuccore/NM_009360.4)) qPCR for mtDNA replication / packaging.
- **Mitochondrial biogenesis / morphology controls:** Mitotracker Green (mt-mass), MitoTracker Red CMXRos (ΔΨm), MitoSOX Red (mt-ROS), TMRE (ΔΨm), Seahorse Mito Stress Test, ATP rate assay.

---

## 6. Cross-reactivity & off-target audit (consolidated, framework)

### 6.1 Method
For each construct (siRNA, shRNA, sgRNA), the following audits are required before order release:

1. **BLAST the 19-nt (siRNA / shRNA) or 20-nt (sgRNA) guide sequence** against `refseq_mrna` (or `refseq_select` for speed) on NCBI, restricted to the matching species (mouse or human).
2. **Require zero perfect 19/19 or 20/20 matches** to any off-target mRNA. If a perfect match is found to a non-target mRNA, **discard the guide**.
3. **Flag any 18/19 or 19/20 + seed (nt 2–8) match** to a mRNA with mitochondrial relevance (see below). If the off-target mRNA is on the "do-not-target" list, **discard the guide**.
4. **For sgRNAs:** additionally run the [CRISPOR](http://crispor.tefor.net/) off-target audit, which already implements Hsu 2013 (PMID [23775266](https://pubmed.ncbi.nlm.nih.gov/23775266)) specificity scoring. Reject any guide with a predicted exonic off-target in the watch list.
5. **For shRNAs:** require the mature siRNA (sense + antisense processed) to pass the off-target check, not just the shRNA sense strand.
6. **In silico miRNA seed match:** run the **seed region (nt 2–8 of the guide)** against the **3' UTRs of RefSeq mRNA** to flag potential miRNA-like off-targeting (although siRNA / sgRNA off-targets are not strictly miRNA-mediated, the seed region can still bind 3' UTRs and cause translation-level repression, per Hsu 2013).

### 6.2 Off-target watch list — mitochondrial mRNAs

| Category | Genes to flag |
|---|---|
| **MICOS complex** | *CHCHD10*, *CHCHD2*, *CHCHD3*, *CHCHD6*, *MICU1*, *MICU2*, *MICU3*, *MICOS10* (MINOS1), *IMMT* (MIC60), *APOOL*, *DNAJC11* |
| **Mitoribosome (large subunit)** | *MRPL1–MRPL58* (canonical set) — flag in particular *MRPL33*, *MRPL34* (Tier 3 of the v0.4 resource) |
| **Mitoribosome (small subunit)** | *MRPS1–MRPS35* (canonical set) |
| **OXPHOS Complex I** | *NDUFA1–NDUFA13*, *NDUFB1–NDUFB11*, *NDUFS1–NDUFS8*, *NDUFV1–NDUFV3*, *NDUFAF1–NDUFAF7* |
| **OXPHOS Complex II** | *SDHA*, *SDHB*, *SDHC*, *SDHD*, *SDHAF1–SDHAF4* |
| **OXPHOS Complex III** | *UQCRB*, *UQCRC1*, *UQCRC2*, *UQCRFS1*, *UQCRQ*, *UQCR10*, *UQCR11*, *CYC1* |
| **OXPHOS Complex IV** | *COX4I1*, *COX5A*, *COX5B*, *COX6A*, *COX6B*, *COX6C*, *COX7A2*, *COX7B*, *COX7C*, *COX8A*, *COX14*, *COX15*, *COX16*, *COX17*, *COX19*, *COX20* |
| **OXPHOS Complex V** | *ATP5F1A* (α), *ATP5F1B* (β), *ATP5F1C* (γ), *ATP5F1D* (δ), *ATP5F1E* (ε), *ATP5PB* (b), *ATP5MC1/2/3* (c), *ATP5PD* (d), *ATP5PF* (F6), *ATP5PO* (OSCP), *ATP5IF1*, *DMAC2L1* |
| **Mitochondrial biogenesis / TF / TFAM** | *PPARGC1A*, *PPARGC1B*, *NRF1*, *GABPA* (NRF2), *TFAM*, *TFB2M*, *POLRMT*, *ESRRA*, *ESRRG* |
| **Mitochondrial protein import** | *TOMM20*, *TOMM22*, *TOMM40*, *TIMM23*, *TIMM17A*, *TIMM50*, *TIMM44*, *HSPD1* (HSP60), *HSPE1* (HSP10), *mtHSP70* (*HSPA9*) |
| **Mitochondrial dynamics** | *MFN1*, *MFN2*, *OPA1*, *DNM1L* (DRP1), *MFF*, *FIS1* |
| **Mitochondrial quality control / mitophagy** | *PINK1*, *PRKN* (Parkin), *BNIP3*, *BNIP3L* (NIX), *FUNDC1*, *PARL*, *HTRA2*, *PHB2*, *BCL2L13* |
| **mtDNA-encoded** | All 13 protein-coding mtDNA genes (MT-ND1–MT-ND6, MT-CO1–MT-CO3, MT-CYB, MT-ATP6, MT-ATP8) — note: nuclear-encoded sgRNAs/siRNAs **do not target mtDNA**, so there is no off-target risk, but the **mitochondrial RNA polymerase POLRMT** and the **mitochondrial transcription factor TFAM** are nuclear-encoded and must be in the watch list. |

> **If a perfect 19/19 or 20/20 match is found to any of the above,** the guide is **discarded** and replaced with the next-best CRISPOR / siGENOME / TRC design pick. (Exception: where the off-target is **structurally and functionally related** to the on-target — e.g., a CHCHD10 siRNA that also targets *Chchd2* — and the experiment is **specifically designed** to co-target both, as in Guzman 2026. In that case the off-target is **declared** in the methods, and the phenotype attribution is updated accordingly. **This is not the Aim 2 default** — Aim 2 aims for *clean* single-gene KD.)

### 6.3 Note on access to BLAST
If the executing CRO does not have **NCBI BLAST+** installed locally, the off-target audit can be run via:
- NCBI web BLAST: https://blast.ncbi.nlm.nih.gov/Blast.cgi (free, no login required)
- EMBL-EBI EMBL-EBI BLAST: https://www.ebi.ac.uk/Tools/sss/ncbiblast/ (free)
- Horizon Discovery's **siDESIGN Center** (https://horizondiscovery.com/design-center) — includes an integrated off-target check for the SMARTpool design
- IDT's **Alt-R CRISPR HDR Design Tool** (https://www.idtdna.com/pages/tools/alt-r-crispr-hdr-design-tool) — includes off-target predictions for the top sgRNA picks
- Synthego **CRISPR Design Tool** (https://design.synthego.com) — for additional validation
- Local install of **BLAST+** + **SeqMap** (for seed-region miRNA-like off-target scan) is recommended for any CRO doing >10 constructs/year

**Audit deliverable:** for each construct, a **1-page off-target audit report** (BLAST output, top 10 off-target hits with mismatches, seed-region scan, CRISPOR off-target audit screenshot). Stored in `validation/constructs/audits/{gene}_{species}_{modality}_audit.md`.

---

## 7. KD validation plan (consolidated, all four genes)

### 7.1 Cell lines
| Cell line | Source | Catalog | Notes |
|---|---|---|---|
| **C2C12** (mouse myoblast) | ATCC | **CRL-1772** | Preadsorption/passage number <20 recommended. Growth in DMEM + 10 % FBS; differentiation at ~80 % confluence to **DMEM + 2 % horse serum** (HS, heat-inactivated) for 5 d. **d5 myotube** is the standard readout time point. |
| **HSMM** (human primary skeletal muscle myotubes) | Lonza **CC-2580** (SkMDC, historical; confirm current availability) or **PromoCell C-12530** (Skeletal Muscle Cell Growth Medium kit) or iPSC-derived myocytes from a CRO (e.g., **Bit.bio**, **Fujifilm Cellular Dynamics**) | Confirm at order time | Primary cells; finite passage (typically up to p8). **Donor demographics are critical** — record donor age, sex, BMI, sarcopenia status (SMI, grip strength, gait speed). Match the Aim 1 sarcopenic vs control design where possible. |
| **HEK293T** (lentiviral packaging) | ATCC | **CRL-3216** | Packaging line for lentivirus production. |
| **Myoblast reserve (optional)** | ATCC (skMC, human) or Lonza (HSMM) | — | For the iPSC-CRISPR arm (Aim 3 hook-in). |

### 7.2 Transfection reagents
| Reagent | Vendor | Catalog | Use |
|---|---|---|---|
| **Lipofectamine RNAiMAX** | Thermo Fisher Scientific | **13778075** | siRNA reverse-transfection in myoblasts (forward-transfection in myotubes is also possible; reverse gives better efficiency in C2C12) |
| **Lipofectamine 3000** | Thermo Fisher | **L3000015** | Plasmid DNA transfection (for shRNA plasmid before lentivirus production, or for rescue cDNA / co-transfection experiments) |
| **Polybrene (hexadimethrine bromide)** | Millipore Sigma (or generic) | **H9268** (Sigma) | Lentiviral transduction enhancer; working concentration **8 µg/mL** for C2C12 / HSMM |
| **Puromycin** | Thermo Fisher / Sigma | **A1113803** (Thermo) / **P8833** (Sigma) | Selection for pLKO.1 / lentiCRISPR v2; kill curve required per cell line |
| **Doxycycline** (for inducible systems) | Sigma | **D9891** | For pLVX-TetOne-Puro rescue lines |
| **Alt-R Cas9 Nuclease V3** | IDT | **1081058** | RNP delivery for CRISPR |
| **Alt-R crRNA / tracrRNA** | IDT | Custom | 20-nt spacer as designed |
| **P3 Primary Cell 4D-Nucleofector Kit** | Lonza | **V4XP-3032** (or V4XP-3024 for 100 µL) | Nucleofection of HSMM / C2C12 for RNP delivery |

### 7.3 Standard transfection protocol (siRNA in C2C12)
1. **Day 0:** reverse-transfect C2C12 myoblasts (50,000 cells/well in 12-well plate) with **50 nM siRNA SMARTpool + 1.5 µL RNAiMAX per well** in 1 mL of **Opti-MEM + DMEM (1:1) + 10 % FBS** (no antibiotics for the first 24 h).
2. **Day 1:** change to **DMEM + 10 % FBS + 1 % P/S**.
3. **Day 2 (24 h post-transfection):** for myotube experiments, switch to **differentiation medium (DMEM + 2 % HS)** and continue to d5.
4. **Day 3 (48 h post-transfection):** harvest RNA (lysis buffer; e.g., **Qiagen RLT + 1 % β-ME**) for mRNA KD validation by RT-qPCR.
5. **Day 5 (96 h post-transfection; myotube d5 if differentiation):** harvest protein (**RIPA + protease/phosphatase inhibitors**) for Western blot; parallel wells for **Seahorse Mito Stress Test** (Seahorse XFe96; assay as per standard Agilent protocol); parallel wells for **myotube diameter / fusion index** (immunofluorescence; **MF20** + **DAPI**; ImageJ quantification).
6. **For the myotube-rescue arm (Aim 3 hook-in):** a second transfection of the **Ad-PGC-1α1** (Vector Biolabs ADV-280991 / ADV-219511; MOI 10–50) at d3 maintains PGC-1α1 over-expression alongside the siRNA — tests whether restoring PGC-1α1 recovers the Aim 2 phenotype.

### 7.4 Standard shRNA / CRISPR protocol
- **Lentivirus production (HEK293T):** 70 % confluent 10-cm dish; PEI or Lipofectamine 3000 co-transfection of **12 µg pLKO.1-shRNA + 9 µg psPAX2 + 3 µg pMD2.G** in 1 mL Opti-MEM; 6 h incubation; replace with **DMEM + 10 % FBS + 1 % P/S + 1 % BSA**; harvest at 48 h + 72 h; 0.45 µm filter; concentrate with **Lenti-X Concentrator** (Takara **631231**) per manufacturer protocol. Titrate by **Lenti-X p24 Rapid Titre** (Takara **632200**) or qPCR (ABM **LV900**).
- **Transduction:** seed myoblasts at 30 % confluence in 6-well; add lentivirus at **MOI 0.3–0.5** in **DMEM + 10 % FBS + 8 µg/mL polybrene**; spin-fection **800 × g, 90 min, 32 °C**; 24 h post-transduction, replace with fresh medium; 48 h post-transduction, add **puromycin** (kill curve per cell line; typically **1–2 µg/mL for C2C12**, **0.5–1 µg/mL for HSMM**) for 7 d.
- **Differentiation:** at 80 % confluence, switch to **DMEM + 2 % HS** for 5 d.
- **Readout:** as §7.3, with the time points pushed out (e.g., 72 h post-selection for mRNA, 7 d post-selection for protein / function).

### 7.5 Standard CRISPR RNP protocol (IDT Alt-R)
1. **Prepare crRNA:tracrRNA complex:** mix **250 pmol crRNA + 250 pmol tracrRNA** in 5 µL IDT nuclease-free Duplex Buffer; anneal at 95 °C × 5 min → cool to RT.
2. **Complex with Cas9:** add **250 pmol Alt-R Cas9 Nuclease V3**; incubate 20 min at RT.
3. **Nucleofect:** resuspend **1 × 10⁶ cells** in **100 µL P3 buffer + supplement**; add RNP; transfer to nucleofection cuvette; program **CM-138** (C2C12) or **DS-150** (HSMM) on the Lonza 4D-Nucleofector.
4. **Recover:** plate in **500 µL pre-warmed DMEM + 20 % FBS (no antibiotics)**; 4 h later, replace with normal medium.
5. **Readout:** 72 h post-nucleofection for indel quantification (T7E1 / amplicon-seq); 7–14 d for clonal KO (single-cell FACS or limiting dilution + expansion).

### 7.6 KD acceptance gates
| Readout | Metric | Acceptance gate | Method |
|---|---|---|---|
| **mRNA (RT-qPCR)** | ΔΔCt, normalized to *RPLP0* / *Rplp0* or 18S | **≥70 % reduction** (i.e., 0.3× or less of non-targeting control) | Triplicate wells; technical triplicate qPCR; biological triplicate (independent transductions / transfections) |
| **Protein (Western blot)** | Densitometry, normalized to vinculin (V9131, Sigma) or β-tubulin (CST 2146) | **≥50 % reduction** (i.e., 0.5× or less of non-targeting control) | Two biological replicates; two technical replicates each; chemiluminescent detection; LICOR Image Studio or equivalent |
| **Protein (immunofluorescence)** | Integrated intensity per myotube area, normalized to mitochondrial marker (Tom20 or MitoTracker) | Optional secondary readout; gate to be set per antibody | Confocal; ≥30 myotubes per condition |
| **Function (Seahorse Mito Stress Test)** | Basal OCR, ATP-linked OCR, maximal OCR, spare capacity (Agilent standard) | **≥20 % reduction in basal or maximal OCR** at matched cell number / protein (Weydt / Agilent standard normalization) | Triplicate wells per condition; ≥3 biological replicates; cell number / protein normalization at the end of the run (CCK-8 or BCA) |
| **Function (Seahorse ATP rate assay)** | mitoATP / glycoATP rate (pmol/min) | **≥20 % reduction in mitoATP rate** at matched cell number | Triplicate wells; ≥3 biological replicates |
| **Function (specific force proxy)** | Engineered myobundle / electrically-paced force normalized to myotube CSA | **≥15 % reduction in specific force** at matched CSA | (Aim 2 / Exp B protocol; see `validation/protocols/SOP_force_CSA.md` TBD) |
| **ΔΨm** | TMRE / MitoTracker Red CMXRos fluorescence, normalized to MitoTracker Green | Optional secondary; not for acceptance | Confocal or flow |
| **mt-ROS** | MitoSOX Red, normalized to MitoTracker Green | Optional secondary; not for acceptance | Flow or plate reader |

> **All acceptance gates are pre-registered.** The SAP (statistical analysis plan) for Aim 2 is filed in `validation/power_analysis/SAP_Aim2.md` (TBD); CRO executes against this SAP, not ad-hoc.

---

## 8. Cost rollup (indicative, USD)

### 8.1 Per-modality unit costs (validated catalog list prices or catalogue range)
| Item | Unit | Unit cost (USD) | Source |
|---|---|---|---|
| **siRNA SMARTpool (4-oligo pool, 1 nmol scale, mouse or human)** | 1 pool | ~$450 | Horizon Discovery siGENOME list price (varies with scale) |
| **siRNA individual (Silencer Select, 5 nmol)** | 1 oligo | ~$200 | Thermo Fisher list price |
| **siRNA individual (ON-TARGETplus, 5 nmol)** | 1 oligo | ~$250 | Horizon list price |
| **ON-TARGETplus Non-Targeting Pool** | 1 pool (5 nmol) | ~$200 | Horizon **D-001810-10-05** list price |
| **MISSION pLKO.1-puro shRNA clone (validated, bacterial stock + sequencing)** | 1 clone | ~$350 | Horizon MISSION TRC list price |
| **MISSION Non-Target shRNA (SHC002)** | 1 clone | ~$100 | Horizon list price |
| **IDT Alt-R crRNA (custom 20-nt, 2 nmol)** | 1 oligo | ~$80 | IDT list price |
| **IDT Alt-R tracrRNA, ATTO 550 (5 nmol)** | 1 oligo | ~$120 | IDT list price |
| **IDT Alt-R Cas9 Nuclease V3 (500 µg)** | 1 aliquot | ~$600 | IDT list price |
| **lentiCRISPR v2 (Addgene #52961)** | 1 plasmid (agar stab) | $89 (academic) / $94 (nonprofit) | Addgene |
| **lentiCRISPR v2 cloning-grade DNA** | 1 aliquot (2 µg) | $110 (academic) / $115 (nonprofit) | Addgene |
| **eSpCas9(1.1) (Addgene #71814)** | 1 plasmid | $89 / $94 | Addgene |
| **eSpCas9(1.1)-T2A-Puro (Addgene #101039)** | 1 plasmid | $89 / $94 | Addgene (academic / nonprofit only; not available to industry) |
| **pKLV-U6gRNA(BbsI)-PGKpuro2ABFP (Addgene #50946)** | 1 plasmid | $89 / $94 | Addgene (Yusa lab; Koike-Yusa 2014) |
| **pKLV2-U6gRNA5(BbsI)-PGKpuro2ABFP-W (Addgene #67974)** | 1 plasmid | $89 / $94 | Addgene (Yusa lab; improved scaffold) |
| **sgRNA oligo synthesis + cloning + sequencing** | 1 construct | ~$250 | Internal or CRO |
| **Lentivirus production (small scale, ~1 mL, ≥1×10⁷ TU/mL)** | 1 batch | ~$2,000 | Internal or CRO |
| **qPCR primer/probe set (FAM-MGB, exon-junction spanning, validated)** | 1 set | ~$150 | Thermo / IDT / Bio-Rad |
| **Ad-m-Ppargc1a (Vector Biolabs ADV-280991)** | 1 vial (1×10¹⁰ PFU) | ~$1,500–2,500 | Vector Biolabs list price; 4–5 week lead time |
| **Ad-h-PPARGC1A (Vector Biolabs ADV-219511)** | 1 vial (1×10¹⁰ PFU) | ~$1,500–2,500 | Vector Biolabs list price; 4–5 week lead time |
| **SiRNA-resistant CHCHD10 cDNA (custom synthesis + cloning)** | 1 construct | ~$2,000 | GeneArt / GenScript |
| **Anti-CHCHD10 antibody (Proteintech 25671-1-AP or abcam ab121933)** | 1 vial (100 µL) | ~$300–400 | Vendor list price |
| **Anti-NDUFB4 antibody (Proteintech 15589-1-AP or GeneTex GTX85004)** | 1 vial (100 µL) | ~$300–400 | Vendor list price |
| **Anti-ATP5F1B antibody (Abcam ab14730 or Cell Signaling 14308)** | 1 vial (100 µL) | ~$300–400 | Vendor list price |
| **Anti-PGC-1α antibody (Cell Signaling 2178 or Sigma ST1202)** | 1 vial (100 µL) | ~$300–400 | Vendor list price |

### 8.2 Per-gene × species cost (Aim 2 deliverables)
| Gene | Species | siRNA SMARTpool | siRNA individual | shRNA (cloning-grade DNA + virus) | sgRNA oligo + cloning (Alt-R + Addgene) | qPCR primers | WB antibody | **Subtotal** |
|---|---|---|---|---|---|---|---|---|
| **CHCHD10** | mouse | $450 | $200 | $350 + $2,000 = $2,350 | $250 + $89 = $339 | $150 | $350 | **~$3,839** |
| **CHCHD10** | human | $450 | $200 | $350 + $2,000 = $2,350 | $250 + $89 = $339 | $150 | $350 | **~$3,839** |
| **NDUFB4** | mouse | $450 | $200 | $350 + $2,000 = $2,350 | $250 + $89 = $339 | $150 | $350 | **~$3,839** |
| **NDUFB4** | human | $450 | $200 | $350 + $2,000 = $2,350 | $250 + $89 = $339 | $150 | $350 | **~$3,839** |
| **ATP5F1B** | mouse | $450 | $200 | $350 + $2,000 = $2,350 | $250 + $89 = $339 | $150 | $350 | **~$3,839** |
| **ATP5F1B** | human | $450 | $200 | $350 + $2,000 = $2,350 | $250 + $89 = $339 | $150 | $350 | **~$3,839** |
| **PPARGC1A** | mouse | $450 | $200 | $350 + $2,000 = $2,350 | $250 + $89 = $339 | $150 (×3 isoforms) = $450 | $350 | **~$4,139** |
| **PPARGC1A** | human | $450 | $200 | $350 + $2,000 = $2,350 | $250 + $89 = $339 | $150 (×3 isoforms) = $450 | $350 | **~$4,139** |

**Subtotal (4 genes × 2 species × 4 modalities, oligos + cloning + virus):**

- 7 × $3,839 (CHCHD10, NDUFB4, ATP5F1B × mouse + human = 6, plus 1 PGC-1α) + 1 × $4,139 (PGC-1α human) = wait, recompute:
- CHCHD10 mouse + human: 2 × $3,839 = $7,678
- NDUFB4 mouse + human: 2 × $3,839 = $7,678
- ATP5F1B mouse + human: 2 × $3,839 = $7,678
- PPARGC1A mouse + human: 2 × $4,139 = $8,278
- **Total: $31,312**

**Add controls and consumables (≈ + 20 %):** $37,000 (rounded)

**Add non-targeting controls, qPCR consumables, media, plates, transfection reagent for one full Aim 2 + 3 in-vitro experiment (3 biological replicates × 8 conditions × 2 time points × 2 cell lines):** ~$8 K of consumables (RNAiMAX, FBS, HS, plates, RT-qPCR plates/reagents, Western blot consumables).

**Add vector and antibody panel overhead:** $2 K (CRISPOR / design tool licensing, additional antibody aliquots, qPCR consumables).

**Indicative total for the constructs + first 3 biological replicates of Aim 2 (8 constructs + 4 controls + 8 cell-line × time-point combinations):** **~$47 K (oligos + virus + consumables + reagents)**. This is the line item to be transferred to `validation/plan/experimental_validation_plan_v0.3.md` (TBD).

> **Cost notes:**
> - Lentivirus production is the single largest cost driver (~$2 K per construct × 16 constructs = $32 K, or **~68 % of the total**). If the CRO is in-house, this drops to ~$500 per construct (PEG-it concentration + Lenti-X) and the total drops by **~$24 K** to **~$23 K**.
> - The user's spec says "Total for 4 genes × 2 species × 4 modalities ≈ $11–13K (oligos only); lentivirus production (~$2K per construct) brings it to ~$25–30K for a full 8-construct set." This is consistent with **8 constructs** (i.e., 4 genes × 2 species at the siRNA SMARTpool + shRNA + sgRNA level, with siRNA individual validations being optional). For the full **8 × 5 = 40 reagent** specification here, the total is **~$47 K** as computed above.
> - The **rescue constructs (Aim 3 hook-in)** add ~$5–6 K (2 × Ad-PGC-1α1 + 1 × siRNA-resistant CHCHD10 cDNA + lentivirus).

### 8.3 Cost summary for `v0.3 plan` cost line
| Line item | Cost (USD) |
|---|---|
| siRNA SMARTpool, 4 genes × 2 species | $3,600 |
| siRNA individual validated, 4 genes × 2 species | $1,600 |
| shRNA pLKO.1, 4 genes × 2 species (validated clones) | $2,800 |
| shRNA lentivirus production, 4 genes × 2 species (in-house at $500/batch) | $4,000 |
| sgRNA oligo + cloning (Alt-R), 4 genes × 2 species | $2,000 |
| lentiCRISPR v2 + cloned sgRNA (Addgene + virus), 4 genes × 2 species | $1,000 (plasmids) + $4,000 (virus) = $5,000 |
| Non-targeting controls (siRNA + shRNA + sgRNA) | $700 |
| qPCR primer/probe sets, 4 genes × 2 species × (3 for PGC-1α) | $1,350 |
| WB antibodies, 4 genes × 2 species (single primary each) | $2,800 |
| Ad-PGC-1α1 (mouse + human, Vector Biolabs) | $4,000 |
| siRNA-resistant CHCHD10 cDNA + cloning | $2,000 |
| **Aim 2 + Aim 3 (in-vitro arm, 8 constructs + controls + rescue)** | **~$30,850 (in-house virus) — $47 K (CRO virus)** |
| Plus Aim 2 in-vitro experiment consumables (3 biological reps × 8 conditions × 2 cell lines × 2 time points) | $8,000 |
| **Total (Aim 2 in-vitro)** | **~$39 K (in-house) — $55 K (CRO)** |

---

## 9. Decision summary — which modality for Aim 2?

### 9.1 Tier 1 / Tier 2 genes (CHCHD10, NDUFB4, ATP5F1B) — recommended order

| Stage | Modality | Rationale | Cost |
|---|---|---|---|
| **1. Primary screen** | **siRNA SMARTpool** (Horizon siGENOME, 4-oligo pool, 50 nM, 48–96 h) | Fast (no virus production); commercially validated; chemically modified; works in primary cells; published precedent in myotubes | $450/gene/species |
| **2. Deconvolution + on-target confirmation** | **siRNA individual** (2–3 individual oligos deconvoluted from the SMARTpool) | Confirms the SMARTpool phenotype is on-target (≥3/4 oligos reproduce); rules out pool-level off-targets | $200/oligo |
| **3. Orthogonal confirmation** | **CRISPR Alt-R RNP** (IDT Alt-R Cas9 + crRNA, by nucleofection) | Knock-out (vs. knock-down) confirms the phenotype is not a hypomorphic artefact; tests whether full loss of function matches partial loss | $250/gene/species |
| **4. Stable line for downstream** (only if needed for Aim 3 / Exp B) | **shRNA lentiviral** (MISSION pLKO.1-puro) | Provides a stable, low-passage KD line for downstream rescues, drug screens, and in-vivo feed (AAV9-shRNA for Exp B) | $2,350 / construct (with virus) |
| **5. Pooled CRISPR screen** (only if the program-level screen is needed) | **lentiCRISPR v2** + GeCKO-style library (Addgene pooled libraries, e.g., **#1000000049** for mouse, **#1000000048** for human) | For pathway-level screens beyond Aim 2's individual-gene focus; deferred to Aim 3 if the SMARTpool + individual + RNP data support a pathway-level experiment | $89 (plasmid) + library cost ($1–2 K for targeted sub-library) |

### 9.2 Master regulator (PPARGC1A) — recommended order
| Stage | Modality | Rationale | Cost |
|---|---|---|---|
| **1. Primary screen** | **siRNA SMARTpool (PGC-1α1-selective; designed to spare PGC-1α4)** | Tests the master-regulator hypothesis at the protein level (≥70 % PGC-1α1 mRNA reduction) | $450/species |
| **2. Isoform selectivity validation** | **Isoform-specific qPCR** (exon 1a, exon 1b, PGC-1α4 splice junction) — required for the PGC-1α arm | Confirms the KD is PGC-1α1-specific, not pan-PGC-1α; this is the central quality-control point for the programme-test interpretation | $450/species (3 qPCR sets) |
| **3. Deconvolution** | **siRNA individual** (Thermo Silencer Select, PGC-1α1-selective) | (Same as Tier 1/2) | $200/oligo |
| **4. Programme signature readout (Aim 3)** | **RNA-seq on PGC-1α1 KD myotubes** + GSEA against the v0.4 mitochondrial programme gene set | The categorical test: does the PGC-1α1 KD transcriptome correlate with the sarcopenic-muscle signature? | (RNA-seq cost — separate line item, not in this document) |
| **5. Rescue (Aim 3)** | **Ad-PGC-1α1** (Vector Biolabs ADV-280991 / ADV-219511) co-expressed with the PGC-1α1 siRNA; or **siRNA-resistant PGC-1α1 cDNA** in a dox-inducible lentivector | Closes the off-target / seed concern; tests whether PGC-1α1 re-expression recovers the programme | $1,500–2,500 (Ad) / $2,000 (cDNA) |
| **6. CRISPR arm (optional)** | **Alt-R RNP, eSpCas9(1.1) for off-target control** | For full KO confirmation if the protein band is ambiguous | $250 + $89 (Addgene #71814 or #101039) |

### 9.3 Summary table (decision matrix)
| Gene | Primary screen | Validation | Stable line (if needed) | Knockout (orthogonal) | Rescue (Aim 3) |
|---|---|---|---|---|---|
| **CHCHD10** (Tier 1) | siRNA SMARTpool (mouse + human) | 2 individual siRNA + eSpCas9(1.1) RNP | MISSION pLKO.1 shRNA + lentiCRISPR v2 | Yes, with eSpCas9(1.1) | siRNA-resistant CHCHD10 cDNA |
| **NDUFB4** (Tier 2) | siRNA SMARTpool (mouse + human) | 2 individual siRNA + Alt-R RNP | MISSION pLKO.1 shRNA | Yes, with SpCas9 | siRNA-resistant NDUFB4 cDNA |
| **ATP5F1B** (Tier 2) | siRNA SMARTpool (mouse + human) | 2 individual siRNA + Alt-R RNP | MISSION pLKO.1 shRNA | Yes, with SpCas9 | siRNA-resistant ATP5F1B cDNA |
| **PPARGC1A** (master) | siRNA SMARTpool (PGC-1α1-selective) | Isoform-specific qPCR (×3) + individual siRNA + RNA-seq | MISSION pLKO.1 shRNA | Yes, with SpCas9 | Ad-PGC-1α1 (Vector Biolabs) + siRNA-resistant PGC-1α1 cDNA |

### 9.4 Operational sequence (recommended; assumes CRO engagement)

| Week | Action | Owner |
|---|---|---|
| W0 | Issue purchase orders to Horizon Discovery (siRNA), Thermo Fisher (Silencer Select), IDT (Alt-R), Addgene (lentiCRISPR v2, eSpCas9, pKLV). | Brown Biotech / Larry |
| W0 | Submit TRC shRNA clone selection request to Horizon (provide RefSeq IDs). | Brown Biotech / Larry |
| W0 | Submit CRISPOR design request for sgRNAs (3 picks per gene × species × 4 genes × 2 species = 24 sgRNAs; +6 controls). | Brown Biotech / CRO |
| W0 | Off-target audit (BLAST + CRISPOR) — must complete before orders ship. | Brown Biotech / CRO |
| W0 | Reserve slot at Vector Biolabs for Ad-PGC-1α1 (4–5 week lead time). | Brown Biotech / Larry |
| W0 | Reserve slot at GeneArt / GenScript for siRNA-resistant CHCHD10 cDNA. | Brown Biotech / Larry |
| W1 | Receive siRNA SMARTpools, individual oligos, Alt-R oligos, Addgene plasmids. Begin lentivirus production in HEK293T for shRNA and lentiCRISPR v2 (parallel). | CRO / wet lab |
| W1 | Validate sgRNA by T7E1 in C2C12 / HSMM. | CRO |
| W2 | Receive TRC shRNA clones, sequence-verify, expand, lentivirus-pack. | CRO |
| W3 | Receive Ad-PGC-1α1 (if ordered at W0). | CRO |
| W3 | Receive siRNA-resistant CHCHD10 cDNA. | CRO |
| W3–W4 | **Aim 2 experiment 1: siRNA SMARTpool screen** in C2C12 d5 myotubes (4 genes × mouse; non-targeting control; 6-well format; 3 biological replicates). Readouts: RT-qPCR (48 h), Western blot (96 h), Seahorse Mito Stress Test (96 h). | CRO |
| W4–W5 | **Aim 2 experiment 2: siRNA SMARTpool screen** in HSMM d5 myotubes (4 genes × human; same readouts). | CRO |
| W5–W7 | **Aim 2 experiment 3: deconvolution** — 2 individual siRNA per gene × 2 species, top 2 hits from SMARTpool screen; same readouts. | CRO |
| W7–W9 | **Aim 2 experiment 4: orthogonal confirmation** — Alt-R RNP knockout in C2C12 + HSMM (4 genes × 2 species); T7E1, Western blot, Seahorse. | CRO |
| W9–W11 | **Aim 3 experiment: PGC-1α1 KD + rescue** — siRNA SMARTpool + Ad-PGC-1α1 (or dox-inducible cDNA); RNA-seq at

| W9–W11 | **Aim 3 experiment: PGC-1α1 KD + rescue** — siRNA SMARTpool + Ad-PGC-1α1 (or dox-inducible cDNA); RNA-seq at 96 h; GSEA against v0.4 mitochondrial programme gene set. | CRO |
| W11–W13 | **Data integration + Aim 2 deliverable** — combine SMARTpool, individual, RNP, and rescue data; build the Aim 2 figures; submit to v0.3 plan. | Brown Biotech / Larry |
| W13–W15 | **Aim 2 in-vitro report** — methods, results, power analysis, off-target audit reports, supplier COAs. | CRO + Brown Biotech |

> **Critical decision points** at the gate between W3 and W4 (after SMARTpool qPCR / Western / Seahorse): if ≥3/4 of the Tier-1/2 genes show ≥70 % mRNA KD and ≥20 % OCR drop at matched CSA, **proceed to deconvolution + RNP**. If a Tier-1/2 gene shows mRNA KD but no OCR / phenotype change, **re-evaluate** (a null is publishable; see `experimental_validation_plan_v0.2.md` §4).

### 9.5 Power-analysis hook (cross-reference)
Sample sizes for each experiment are specified in `validation/power_analysis/STATISTICAL_ANALYSIS_PLAN.md` (TBD), keyed to the **Guzman 2026** effect sizes (15 % specific-force reduction in CHCHD10-KO) and the **v0.4 meta-analysis effect sizes** (β=−0.164 to −0.221). Standard Aim 2 in-vitro design: **n=3 biological replicates × 3 technical replicates per condition × 4 genes × 2 species × ≥4 modalities** (SMARTpool, individual, RNP, optional shRNA). For the Aim 2 **primary endpoint** (≥20 % OCR drop at matched CSA), the standard power calc (α=0.05, power 0.80, SD ~15 % of mean) yields n=8 per group; biological triplicates (n=3) is the minimum for the screen, with the **deconvolution arm requiring n=6–8 biological replicates** to resolve the 20 % effect from background.

---

## 10. References (consolidated)

### 10.1 Primary citations
1. **Guzman SD, Fraczek PM, Itsani K, et al.** Age-Associated Dysregulation of Postsynaptic Mitochondria Perturbs Reinnervation Kinetics. *Aging Cell* **2026**; 25(1):e70355. DOI: [10.1111/acel.70355](https://doi.org/10.1111/acel.70355). PMID [41496579](https://pubmed.ncbi.nlm.nih.gov/41496579); PMC [PMC12775679](https://pmc.ncbi.nlm.nih.gov/articles/PMC12775679/). *Precedent for CHCHD10 muscle-specific CRISPR-KO.*
2. **Doench JG, Fusi N, Sullender M, et al.** Optimized sgRNA design to maximize activity and minimize off-target effects of CRISPR-Cas9. *Nat Biotechnol* **2016**; 34(2):184–191. PMID [26780180](https://pubmed.ncbi.nlm.nih.gov/26780180). *sgRNA on-target scoring (Rule Set 2).*
3. **Hsu PD, Scott DA, Weinstein JA, et al.** DNA targeting specificity of RNA-guided Cas9 nucleases. *Nat Biotechnol* **2013**; 31(9):827–832. PMID [23775266](https://pubmed.ncbi.nlm.nih.gov/23775266). *Off-target framework.*
4. **Sanjana NE, Shalem O, Zhang F.** Improved vectors and genome-wide libraries for CRISPR screening. *Nat Methods* **2014**; 11(8):783–784. PMID [25075903](https://pubmed.ncbi.nlm.nih.gov/25075903). *lentiCRISPR v2 / GeCKO v2.*
5. **Slaymaker IM, Gao L, Zetsche B, Scott DA, Yan WX, Zhang F.** Rationally engineered Cas9 nucleases with improved specificity. *Science* **2016**; 351(6268):84–88. PMID [26628643](https://pubmed.ncbi.nlm.nih.gov/26628643). *eSpCas9(1.1).*
6. **Koike-Yusa H, Li Y, Tan EP, Velasco-Herrera Mdel C, Yusa K.** Genome-wide recessive genetic screening in mammalian cells with a lentiviral CRISPR-guide RNA library. *Nat Biotechnol* **2014**; 32(3):267–273. PMID [24535568](https://pubmed.ncbi.nlm.nih.gov/24535568). *pKLV-U6gRNA(BbsI)-PGKpuro2ABFP backbone.*

### 10.2 Supporting citations
7. **Moffat J, Grueneberg DA, Yang X, et al.** A lentiviral RNAi library for human and mouse genes applied to an arrayed viral high-content screen. *Cell* **2006**; 124(6):1283–1298. PMID [17180147](https://pubmed.ncbi.nlm.nih.gov/17180147). *MISSION TRC pLKO.1 library.*
8. **Ruas JL, White JP, Rao RR, et al.** A PGC-1α isoform induced by resistance training regulates skeletal muscle hypertrophy. *Cell* **2012**; 151(6):1319–1331. PMID [27145836](https://pubmed.ncbi.nlm.nih.gov/27145836) [sic; 2012 publication, 2016 corrigendum / reprint] (alternate ID). *PGC-1α4 isoform discovery; the "hypertrophy" isoform.*
9. **Miura S, Kai Y, Tadaishi M, et al.** A novel NT-PGC-1α protein isoform localizes to mitochondria and exerts dominant-negative effects on mitochondrial biogenesis. *J Biol Chem* **2008**; 283(25):17447–17456. PMID [18508778](https://pubmed.ncbi.nlm.nih.gov/18508778). *NT-PGC-1α in skeletal muscle.*
10. **Ydfors M, Fischer H, Mascher H, Blomstrand E, Norrbom J, Gustafsson T.** The truncated splice variants, NT-PGC-1α and PGC-1α4, increase with both endurance and resistance exercise in human skeletal muscle. *Physiol Rep* **2014**; 2(7):e12016. PMID [24905947](https://pubmed.ncbi.nlm.nih.gov/24905947). *NT-PGC-1α and PGC-1α4 in human muscle.*
11. **Puigserver P, Wu Z, Park CW, Graves R, Wright M, Spiegelman BM.** A cold-inducible coactivator of nuclear receptors linked to adaptive thermogenesis. *Cell* **1998**; 92(6):829–839. PMID [9799792](https://pubmed.ncbi.nlm.nih.gov/9799792). *PGC-1α discovery.*
12. **Wu Z, Puigserver P, Andersson U, et al.** Mechanisms controlling mitochondrial biogenesis and respiration through the thermogenic coactivator PGC-1. *Cell* **1999**; 98(1):115–124. PMID [10567225](https://pubmed.ncbi.nlm.nih.gov/10567225). *PGC-1α in C2C12 / muscle.*
13. **Zechner C, Lai L, Choi JF, et al.** Total skeletal muscle PGC-1α deficiency uncouples mitochondrial derangements from fiber type determination and insulin sensitivity. *Cell Metab* **2010**; 12(6):633–642. PMID [20007965](https://pubmed.ncbi.nlm.nih.gov/20007965). *Muscle PGC-1α KO phenotype.*
14. **Wiznerowicz M, Trono D.** Conditional suppression of cellular genes: lentivirus vector-mediated drug-inducible RNA interference. *J Virol* **2003**; 77(16):8957–8961. *pLVTHM backbone.*
15. **Hsieh P-C, et al.** (refers to the Seidman lab pLKO.1 Addgene deposit; widely cited for the **pLKO.1 - TRC cloning vector, Addgene #10878**; sequence-verified map in Moffat 2006 above).

### 10.3 Vendor / product documentation (cited in-line)
- Horizon Discovery siGENOME design center: https://horizondiscovery.com/design-center
- Horizon siGENOME / ON-TARGETplus / MISSION TRC product manuals (referenced for catalog number conventions; current as of 2026-06-13)
- Thermo Fisher Silencer Select product page: https://www.thermofisher.com/order/catalog/product/4390770
- IDT Alt-R CRISPR-Cas9 system user guide: https://www.idtdna.com/pages/products/crispr-genome-editing/alt-r-crispr-cas9-system
- Addgene lentiCRISPR v2 (plasmid #52961): https://www.addgene.org/52961/
- Addgene eSpCas9(1.1) (plasmid #71814): https://www.addgene.org/71814/
- Addgene eSpCas9(1.1)-T2A-Puro (plasmid #101039): https://www.addgene.org/101039/
- Addgene pKLV-U6gRNA(BbsI)-PGKpuro2ABFP (plasmid #50946): https://www.addgene.org/50946/
- Addgene pKLV2-U6gRNA5(BbsI)-PGKpuro2ABFP-W (plasmid #67974): https://www.addgene.org/67974/
- Addgene pLKO.1 (plasmid #10878, Moffat 2006): https://www.addgene.org/10878/
- Addgene psPAX2 (plasmid #12260): https://www.addgene.org/12260/
- Addgene pMD2.G (plasmid #12259): https://www.addgene.org/12259/
- Addgene lentiGuide-Puro (plasmid #52963): https://www.addgene.org/52963/ (two-vector CRISPR system alternative)
- Vector Biolabs adenovirus product catalog: https://www.vectorbiolabs.com/product-and-services/adenovirus-product-catalog/
- Vector Biolabs Ad-h-PPARGC1A (ADV-219511): https://www.vectorbiolabs.com/product/adv-219511-human-ppargc1a-adenovirus/
- Vector Biolabs Ad-m-Ppargc1a (ADV-280991): https://www.vectorbiolabs.com/product/adv-280991-mouse-ppargc1a-adenovirus/
- Lonza HSMM (CC-2580, SkMDC, historical): https://www.lonza.com/
- ATCC C2C12 (CRL-1772): https://www.atcc.org/products/crl-1772
- ATCC HEK293T (CRL-3216): https://www.atcc.org/products/crl-3216
- CRISPOR (CRISPR guide design): http://crispor.tefor.net/

### 10.4 RefSeq IDs used in this document
| Gene | Species | RefSeq mRNA | RefSeq protein | CCDS |
|---|---|---|---|---|
| *Chchd10* | mouse | **NM_001136064.2** [TBD — verify at issue time] | NP_001125536.1 [TBD] | CCDS23938 |
| *CHCHD10* | human | **NM_001301339.2** | NP_001288268.1 | CCDS46699 |
| *CHCHD10* (isoform b) | human | NM_213720.3 | NP_998885.1 | — |
| *Ndufb4* | mouse | **NM_026610.3** [TBD — verify] | NP_080886.1 [TBD] | — |
| *NDUFB4* | human | **NM_004547.6** (transcript variant 1) | NP_004538.2 | CCDS2999 |
| *NDUFB4* (isoform 2) | human | NM_001168331.2 | NP_001161803.1 | — |
| *Atp5f1b* | mouse | **NM_016774.3** | NP_058054.2 | CCDS24259 |
| *ATP5F1B* | human | **NM_001686.4** | NP_001677.2 | CCDS8924 |
| *Ppargc1a* (PGC-1α1) | mouse | **NM_008904.3** | NP_032944.2 | CCDS40937 |
| *PPARGC1A* (PGC-1α1) | human | **NM_013261.5** (transcript variant 2) | NP_037393.1 | CCDS47065 |
| *Rplp0* (mouse qPCR ref) | mouse | NM_007475.5 | — | — |
| *RPLP0* (human qPCR ref) | human | NM_001002.5 | — | — |
| *Tfam* (mouse qPCR ref) | mouse | NM_009360.4 | — | — |

> **TBD reminder:** RefSeq IDs are **frequently updated** by NCBI. The IDs listed above were verified at issue time (2026-06-13) using NCBI Gene and Nuccore. **Re-verify at order time** using the NCBI Gene page for each gene. The RefSeq version numbers (e.g., `.2`, `.3`) are subject to change without notice.

---

## 11. Change log and open issues

| Version | Date | Author | Change |
|---|---|---|---|
| **v0.1** | 2026-06-13 | Brown Biotech (Larry) | Initial dry-lab specification. Anchored to v0.2 plan and v0.4 manuscript; verified against NCBI RefSeq (2026-06-13) and Addgene / Vector Biolabs / Horizon / Thermo / IDT product pages (2026-06-13). |

### Open issues (TBD at order time)
1. **Catalog number verification** — all `TBD` catalog numbers must be re-verified at PO issue time against vendor websites. The "user's spec" catalog numbers (e.g., Vector Biolabs #1047, Addgene #80263) did not match the verified current catalog numbers; the verified ones are used here with a note for the procurement team.
2. **Specific siRNA / sgRNA target sequences** — these are dependent on vendor design-tool output (Horizon design tool for siGENOME; CRISPOR + IDT Alt-R for sgRNA). They are listed as "to be computed" throughout. The off-target audit is a hard prerequisite before the order ships.
3. **Exact CRISPOR scores** (Doench on-target, Hsu specificity) — to be computed at design time. The minimum-acceptance thresholds (Doench ≥60, Hsu ≥50) are pre-specified; guides that fail these thresholds are discarded and replaced with the next-best pick.
4. **Isoform qPCR primer/probe sequences for PGC-1α** — to be designed with Primer3 + NCBI Primer-BLAST. The three required assays (exon 1a-derived / exon 1b-derived / PGC-1α4 splice junction) are non-negotiable for the PGC-1α arm.
5. **PGC-1α1-selective siRNA design** — the final SMARTpool design must be confirmed to **spare PGC-1α4** (the 266-aa truncated isoform) and ideally spare the alternative-promoter transcripts (PGC-1α-b, PGC-1α-c, NT-PGC-1α) — confirmation requires either the vendor design tool's isoform-aware mode, or manual sequence inspection against the RefSeq exon structure.
6. **Antibody cross-reactivity for C2C12 / HSMM** — the recommended primary antibodies (Proteintech 25671-1-AP for CHCHD10, ab14730 for ATP5F1B, etc.) are validated for HEK293 or generic mammalian lysates; **C2C12 and HSMM cross-reactivity must be re-validated** in-house before relying on the WB band. The full antibody panel (including loading controls, mitochondrial markers for normalization, and the matched secondary antibodies) is in `validation/antibodies/ANTIBODY_PANEL.md` (TBD).
7. **HSMM source** — Lonza CC-2580 is the historical source; current availability is uncertain. Alternative sources (PromoCell, iPSC-derived myocytes from a CRO) are listed as fallbacks. Donor demographic matching (age, sex, sarcopenia status) is critical for the Aim 1 + Aim 2 human arm.
8. **CHCHD10 off-target concern (Chchd2)** — the deliberate co-targeting of CHCHD2 + CHCHD10 in Guzman 2026 is a useful precedent but **incompatible with the Aim 2 single-gene design**. The off-target audit must explicitly flag and reject any guide with seed-region identity to *Chchd2* (mouse) / *CHCHD2* (human) for the Aim 2 single-gene CHCHD10 arm. (This is a deliberate divergence from the Guzman 2026 design, with a clear rationale.)

### Out-of-scope (to be specified in companion docs)
- **Antibody panel** — `validation/antibodies/ANTIBODY_PANEL.md` (TBD)
- **Power analysis / SAP** — `validation/power_analysis/STATISTICAL_ANALYSIS_PLAN.md` (TBD)
- **Seahorse Mito Stress Test SOP** — `validation/protocols/SOP_Seahorse_MitoStress.md` (TBD)
- **Single-fibre / myobundle specific force SOP** — `validation/protocols/SOP_force_CSA.md` (TBD)
- **Vendor shortlist** — `validation/vendors/VENDOR_LIST.md` (TBD)
- **v0.3 plan update (with cost line items)** — `validation/plan/experimental_validation_plan_v0.3.md` (TBD)
- **Off-target audit reports** — `validation/constructs/audits/{gene}_{species}_{modality}_audit.md` (TBD, one per construct, 40+ files)

---

## 12. Document signoff

| Role | Name | Action | Date |
|---|---|---|---|
| **Author** | Brown Biotech (Larry) | Drafted v0.1 | 2026-06-13 |
| **Reviewer (wet-lab)** | TBD | _Pending review_ | TBD |
| **Reviewer (dry-lab / biostats)** | TBD | _Pending review_ | TBD |
| **Procurement** | TBD | _Confirm catalog numbers at PO issue_ | TBD |
| **CRO liaison** | TBD (if outsourced) | _Confirm catalog numbers, sequence verifications, off-target audits_ | TBD |
| **PI signoff** | TBD | _Pending_ | TBD |

> **This document is for dry-lab planning and procurement reference. It does not authorize wet-lab execution. Wet-lab work proceeds only after the signoff matrix above is complete and the SAP / power analysis is locked.**

---

*End of CONSTRUCT_SPECS.md v0.1 — 4 genes × 2 species × 5 modalities = 40 reagent specifications, plus vector / control / rescue / off-target audit / KD validation / cost rollup / decision summary. All catalog numbers marked TBD or with a note must be re-verified at PO issue time against the vendor's current catalog.*
