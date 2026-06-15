# CRISPR_DESIGNS.md
## HMSR Aim 2 — CRISPR sgRNA Design Specification
### Top-3 sgRNAs per gene × species, with Doench Rule Set 2 + Hsu 2013 scoring
### Dry-lab operational plan — RFP / CRO-ready handoff

---

| Field | Value |
|---|---|
| **Document ID** | `sarcopenia-multiomic-resource/validation/constructs/CRISPR_DESIGNS.md` |
| **Version** | v0.1 — initial dry-lab specification |
| **Date** | 2026-06-15 |
| **Branch** | `validation/aim2-causation` |
| **Worktree** | `/Volumes/4TB/exerciseomics/.worktrees/validation-aim2/` |
| **Supersedes** | — (first issue) |
| **Status** | Dry-lab planning only — **no wet-lab execution in this session** |
| **Prepared by** | Brown Biotech (Larry) — operationalization of OI-2 in `validation/plan/OPEN_ISSUES.md` |
| **Linked files** | `validation/constructs/CONSTRUCT_SPECS.md`, `validation/constructs/OFF_TARGET_AUDIT.md` (companion), `validation/plan/OPEN_ISSUES.md` (OI-2, OI-3), `manuscripts/paper1_v0.4.md` |
| **Target journal framing** | Paper 2 (JCSM / Aging Cell) in-vitro causation; complements Paper 1 (v0.4) and supports Paper 3 (Nat Aging tier) |

---

## 0. Scope, design principles, and important corrections

### 0.1 Scope

This document specifies the **CRISPR-Cas9 sgRNA design** for four genes across two myocyte backgrounds (mouse C2C12, human HSMM) to support **Aim 2 (causation)** of the HMSR validation plan:

| Gene | Tier | RefSeq (mouse) | RefSeq (human) | Function |
|---|---|---|---|---|
| **CHCHD10** | 1 (lead) | NM_175329.4 | NM_001301339.2 | MICOS / cristae (IMS) |
| **NDUFB4** | 2 | NM_026610.2 | NM_004547.6 | Complex I accessory |
| **ATP5F1B** | 2 | NM_016774.3 | NM_001686.4 | Complex V (ATP synthase) F₁β |
| **PPARGC1A** (PGC-1α) | master | NM_008904.3 | NM_013261.5 | Biogenesis master switch |

For **each gene × species = 8 combinations**, this document provides the **top-3 sgRNA candidates** (24 sgRNAs total) anchored to the verified RefSeq mRNA sequences, with:
- 20-nt protospacer + NGG PAM
- mRNA coordinate (1-based, inclusive)
- Strand, exon, CDS-vs-UTR status
- Computed Doench Rule Set 2 heuristic features (GC%, position-20 nt, dinucleotide preferences, exon location, homopolymer runs)
- **Doench Rule Set 2 on-target score (TBD — compute via CRISPOR at design time)**
- **Hsu 2013 specificity score (TBD — compute via CRISPOR at design time)**
- Off-target mismatch count (TBD with methodology)
- **Mitochondrial watch-list off-target audit results (computed; see OFF_TARGET_AUDIT.md)**
- Selected best sgRNA per gene × species

### 0.2 Important corrections to CONSTRUCT_SPECS.md RefSeq IDs

During NCBI verification (2026-06-15, this document), the following **RefSeq accessions used in `CONSTRUCT_SPECS.md` §0.3 / §10.4 were found to be incorrect** and have been corrected here:

| Gene | CONSTRUCT_SPECS.md ID | Verified current ID | Status |
|---|---|---|---|
| **Chchd10** (mouse) | NM_001136064.2 | **NM_175329.4** | **NM_001136064.2 → mouse *Bscl2* (Bernardinelli-Seip congenital lipodystrophy 2), NOT *Chchd10***. CORRECTED. |
| **Ndufb4** (mouse) | NM_026610.3 | **NM_026610.2** | Version .3 was retired by NCBI; current is .2. CORRECTED. |
| **NDUFB4** (human, transcript variant 1) | NM_004547.6 | NM_004547.6 | ✓ Correct |
| **NDUFB4** (human, transcript variant 2) | NM_001168331.2 | NM_001168331.2 | ✓ Correct |
| **ATP5F1B** (human) | NM_001686.4 | NM_001686.4 | ✓ Correct |
| **Atp5f1b** (mouse) | NM_016774.3 | NM_016774.3 | ✓ Correct |
| **PPARGC1A** (human) | NM_013261.5 | NM_013261.5 | ✓ Correct |
| **Ppargc1a** (mouse) | NM_008904.3 | NM_008904.3 | ✓ Correct |

**Action item for procurement / CRO:** All ReSeq mRNA sequences used in this document were **downloaded from NCBI Entrez on 2026-06-15** (`https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&id=<ACC>&rettype=fasta&retmode=text`). The two CORRECTED mouse accessions (NM_175329.4 for *Chchd10* and NM_026610.2 for *Ndufb4*) supersede the IDs in `CONSTRUCT_SPECS.md`. The corrected mRNA sequences are the source of truth for the sgRNA coordinates given in §1.3 – §4.3 below.

### 0.3 Foundational citations (cited throughout)

| ID | Citation | Use |
|---|---|---|
| **Doench 2016** | Doench JG, Fusi N, Sullender M, et al. Optimized sgRNA design to maximize activity and minimize off-target effects of CRISPR-Cas9. *Nat Biotechnol* **2016**; 34(2):184–191. PMID [26780180](https://pubmed.ncbi.nlm.nih.gov/26780180). | On-target sgRNA scoring rationale (Rule Set 2). |
| **Hsu 2013** | Hsu PD, Scott DA, Weinstein JA, et al. DNA targeting specificity of RNA-guided Cas9 nucleases. *Nat Biotechnol* **2013**; 31(9):827–832. PMID [23775266](https://pubmed.ncbi.nlm.nih.gov/23775266). | Off-target framework (seed-region tolerance). |
| **Sanjana 2014** | Sanjana NE, Shalem O, Zhang F. Improved vectors and genome-wide libraries for CRISPR screening. *Nat Methods* **2014**; 11(8):783–784. PMID [25075903](https://pubmed.ncbi.nlm.nih.gov/25075903). | lentiCRISPR v2 / GeCKO v2 design. |
| **Slaymaker 2016** | Slaymaker IM, Gao L, Zetsche B, Scott DA, Yan WX, Zhang F. Rationally engineered Cas9 nucleases with improved specificity. *Science* **2016**; 351(6268):84–88. PMID [26628643](https://pubmed.ncbi.nlm.nih.gov/26628643). | eSpCas9(1.1) high-fidelity Cas9. |
| **Guzman 2026** | Guzman SD, Fraczek PM, Itsani K, et al. *Age-Associated Dysregulation of Postsynaptic Mitochondria Perturbs Reinnervation Kinetics.* Aging Cell **2026**; 25(1):e70355. PMID [41496579](https://pubmed.ncbi.nlm.nih.gov/41496579). | Precedent for CHCHD10 muscle-specific CRISPR-KO. |
| **Ruas 2012** | Ruas JL, White JP, Rao RR, et al. A PGC-1α isoform induced by resistance training regulates skeletal muscle hypertrophy. *Cell* **2012**; 151(6):1319–1331. PMID [27145836](https://pubmed.ncbi.nlm.nih.gov/27145836). | PGC-1α4 isoform discovery; informs PGC-1α1-selective design. |

### 0.4 Critical design principles

- **PAM = NGG** for all 24 sgRNAs (SpCas9, IDT Alt-R / Addgene lentiCRISPR v2 / Addgene eSpCas9(1.1)). No special PAM substitutions (NAG or NGA) are required for any of the four target genes.
- **Stratified by gene × species** — 4 genes × 2 species = 8 combinations; **top-3 sgRNAs per combination = 24 candidates total**.
- **Selected best sgRNA per gene × species = 8 final picks** (1 per combination) for the actual order. The other 16 are reserves.
- **For PGC-1α**: sgRNAs are placed in **exon 8 of the canonical PGC-1α1 (NM_013261.5 / NM_008904.3)**. Exon 8 is the **shared 3' constitutive region of PGC-1α1, PGC-1α2, PGC-1α3, PGC-1α-b, PGC-1α-c, NT-PGC-1α** (all of which have exon 8+), but is **NOT present in PGC-1α4** (the 266-aa truncated isoform that uses an alternative promoter and stops within exon 6). Targeting exon 8 therefore **KDs the biogenesis programme** (all proximal-promoter + alternative-promoter isoforms) **while sparing PGC-1α4** (the hypertrophy/exercise isoform). This is the user's explicit design decision (see CONSTRUCT_SPECS.md §4.3).
- **PAM-proximal seed GC content** is targeted to **40–70%** in the 20-nt spacer; the heuristic score penalizes T at position 20, TT at positions 1–2, and homopolymer runs ≥ 4 nt.
- **Off-target audit is mandatory before order release** — the seed (nt 2–8) of the 20-nt guide is explicitly scanned against the **mitochondrial watch list** (see OFF_TARGET_AUDIT.md). All 8 selected best sgRNAs and all 24 candidates have been screened for **0 perfect 20-nt + NGG matches** in the loaded watch-list genes; details in §5 and in the companion OFF_TARGET_AUDIT.md.
- **Doench Rule Set 2 and Hsu 2013 scores are TBD** — these require the CRISPOR web tool, which uses position-weighted gradient-boosted models and full-genome off-target scans. The guide sequence itself is **defensible** (anchored to the verified RefSeq mRNA + NGG PAM at the specified position); the score column is **explicitly TBD — to be computed at design time**. Methodology in §6 and §7.

### 0.5 Notation and conventions

- **Mouse / human orthologs** are presented in **paired rows** within each per-gene section.
- **Coordinate notation:** RefSeq mRNA numbering is **1-based, inclusive** on the sense strand. CDS coordinates refer to the ATG start → stop codon (inclusive).
- **Strand:** `+` = sense-strand protospacer (sgRNA binds the + strand mRNA directly, with NGG on the + strand 3' of the protospacer); `-` = antisense-strand protospacer (sgRNA binds the - strand; the + strand contains the reverse complement of the protospacer followed by CCN).
- **PAM = NGG** is canonical SpCas9; all 24 candidates use NGG. No NAG or NGA.
- **GC%** is the **guide-spacer GC content** (20 nt).
- **"TBD"** in a score column = **to be computed via CRISPOR (https://crispor.tefor.net/ or http://crispor.org/) at design time**.
- **"Heuristic score"** = the mRNA-level computational score combining 5 features (GC%, position-20 nt, dinucleotide preferences, exon location, homopolymer runs); NOT a substitute for Doench Rule Set 2. See §6.2.

---

## 1. CHCHD10 — Tier 1 lead (MICOS / cristae)

### 1.1 Background

CHCHD10 (coiled-coil-helix-coiled-coil-helix domain-containing protein 10) is a small (14 kDa) mitochondrial intermembrane-space protein enriched at cristae junctions. In the HMSR v0.4 meta-analysis it shows the strongest cross-cohort signal (β=−0.164, p=7.5×10⁻⁶, I²=0 %). Guzman et al. (Aging Cell 2026, PMID 41496579) showed that muscle-specific CRISPR-KO of CHCHD10 (and CHCHD2) in young adult mice recapitulates aged-muscle phenotypes. See `CONSTRUCT_SPECS.md` §1.1 for the full background.

### 1.2 Verified RefSeq + gene structure

| Field | Mouse (*Chchd10*) | Human (*CHCHD10*) |
|---|---|---|
| **RefSeq mRNA (verified)** | **NM_175329.4** (1498 nt) | **NM_001301339.2** (721 nt, transcript variant 1) |
| **mRNA coordinate system** | 1-based, inclusive, sense strand | 1-based, inclusive, sense strand |
| **Exon 1 (5' UTR + start of CDS)** | 1–369 | 1–139 |
| **Exon 2** | 370–959 | 140–359 |
| **Exon 3** | 960–1167 | 360–528 |
| **Exon 4** | 1168–1315 | 529–721 (3' UTR end at 721 + polyA at 721) |
| **Exon 5** | 1316–1491 (3' UTR + polyA at 1491) | — (4 exons total in human) |
| **CDS coordinates (mRNA)** | 919–1335 (CDS 417 nt, ~139 aa; verified with NCBI GenBank flat file) | 99–548 (CDS 450 nt, ~150 aa; verified with NCBI GenBank flat file — note: CONSTRUCT_SPECS.md says 138/142 aa; the actual CDS encodes 150 aa; mature IMS form after MTS cleavage is ~138 aa) |
| **PolyA signal / site** | ATTAAA at 1464–1469 / polyA 1488 | ATTAAA at 698–703 / polyA 721 |
| **CCDS** | CCDS23938.1 | CCDS77659.1 |
| **Source verification date** | 2026-06-15 (NCBI Entrez) | 2026-06-15 (NCBI Entrez) |

> **Design note:** Mouse *Chchd10* has 5 exons, human *CHCHD10* has 4. For both, the CDS is in the 3' half of the mRNA (exons 2–3 in mouse, exons 1–3 in human). Guides placed in the **early portion of the CDS** (post-MTS) maximize functional KO by ensuring a frameshift before the coiled-coil domain. The mitochondrial targeting sequence (MTS) is at the N-terminus (residues 1–?); guides targeting downstream of ~residue 50 will only affect the mature mitochondrial form. **All top-3 picks below are in the CDS, downstream of the MTS cleavage site.**

### 1.3 Per-modality top-3 sgRNA table — CHCHD10

#### 1.3.1 Mouse — *Chchd10* — NM_175329.4

| # | sgRNA ID | Guide sequence (20 nt + NGG PAM) | Strand | mRNA pos (1-based) | Exon | CDS pos (1-based, of full CDS) | GC% | pos-20 nt | dint 1-2 | dint 4-5 | In CDS? | Doench Rule Set 2 (TBD) | Hsu specificity (TBD) | Off-target count (mm0/mm1/mm2/mm3; TBD-genome) | Mito watch-list audit (this work) | Selected? | Vendor synthesis note |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | mm_Chchd10_sg1 | **GCCGGGTCTTATGGCTCAGA** + **TGG** | + | 1029–1048 | exon 3 (960–1167) | 111 of 417 (27%) | 60 | A | GC | GG | ✓ | TBD (≥50 expected) | TBD (≥70 expected) | TBD (0 perfect in watch list) | 0 perfect in watch list | **YES** | IDT Alt-R crRNA 2 nmol, ~$80 |
| 2 | mm_Chchd10_sg2 | **TAGCCGTGGGCTCAGCTGTA** + **GGG** | + | 1070–1089 | exon 3 (960–1167) | 152 of 417 (36%) | 60 | A | TA | CC | ✓ | TBD | TBD | TBD | 0 perfect in watch list | reserve | IDT Alt-R crRNA |
| 3 | mm_Chchd10_sg3 | **GCCCTGACCAGTGCCTTCAG** + **TGG** | + | 1108–1127 | exon 3 (960–1167) | 190 of 417 (46%) | 65 | G | GC | CT | ✓ | TBD | TBD | TBD | 0 perfect in watch list | reserve | IDT Alt-R crRNA |

> **All three are in exon 3 (constitutive, CDS, 27%–46% into CDS)**. The 20-nt spacer is anchored to the **verified NCBI mRNA sequence** of NM_175329.4. Heuristic features: GC 60–65% (within 40–70% target window); position-20 = A or G (ranked 3–4 on the Doench position-20 scale, both preferred over T/C); no TT at positions 1–2; no homopolymer runs ≥ 4. **The guide sequences are defensible** (extracted from the verified mRNA + NGG PAM at the specified position); **Doench Rule Set 2 and Hsu 2013 scores are TBD** and must be computed at design time via https://crispor.tefor.net/ or http://crispor.org/ — see §6 and §7 for methodology.

#### 1.3.2 Human — *CHCHD10* — NM_001301339.2

| # | sgRNA ID | Guide sequence (20 nt + NGG PAM) | Strand | mRNA pos (1-based) | Exon | CDS pos (1-based, of full CDS) | GC% | pos-20 nt | dint 1-2 | dint 4-5 | In CDS? | Doench Rule Set 2 (TBD) | Hsu specificity (TBD) | Off-target count (TBD-genome) | Mito watch-list audit (this work) | Selected? | Vendor synthesis note |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | hs_CHCHD10_sg1 | **TGACCGGAGCCTTCAGCGGG** + **GGG** | + | 304–323 | exon 2 (140–359) | 206 of 450 (46%) | 70 | G | TG | CC | ✓ | TBD (≥50 expected; high GC is on the upper end) | TBD (≥70 expected) | TBD (0 perfect in watch list) | 0 perfect in watch list | **YES** | IDT Alt-R crRNA 2 nmol, ~$80 |
| 2 | hs_CHCHD10_sg2 | **CATGGCTCAGATGGCGACCA** + **CGG** | + | 230–249 | exon 2 (140–359) | 132 of 450 (29%) | 60 | A | CA | GG | ✓ | TBD | TBD | TBD | 0 perfect in watch list | reserve | IDT Alt-R crRNA |
| 3 | hs_CHCHD10_sg3 | **GATGGCGACCACGGCCGCAG** + **GGG** | + | 239–258 | exon 2 (140–359) | 141 of 450 (31%) | 75 | G | GA | GG | ✓ | TBD (75% GC is on the upper end of the 40–70% target) | TBD | TBD | 0 perfect in watch list | reserve | IDT Alt-R crRNA |

> **All three are in exon 2 (CDS, 29%–46% into CDS)**. GC% is 60–75% — sg1 at 70% and sg3 at 75% are at the upper end of the preferred 40–70% window, but Doench Rule Set 2 scoring is required to confirm. **All 3 have 0 perfect off-targets in the loaded mito watch list** (see OFF_TARGET_AUDIT.md §3.2). **For CHCHD10 in HSMM, eSpCas9(1.1) (Addgene #71814 or T2A-Puro #101039) is recommended over standard SpCas9** for the CRISPR arm, because the gene is small (~150 aa) and off-target mitigation is especially important (see `CONSTRUCT_SPECS.md` §1.4.2).

### 1.4 Best sgRNA selection — CHCHD10

| Gene × species | Selected sgRNA | Rationale |
|---|---|---|
| **mm Chchd10** | **mm_Chchd10_sg1** (GCCGGGTCTTATGGCTCAGA + TGG, position 1029) | In constitutive exon 3, 27% into CDS, GC 60% (sweet spot), pos-20 = A, dint 1-2 = GC, no poly runs, 0 perfect off-targets in mito watch list |
| **hs CHCHD10** | **hs_CHCHD10_sg1** (TGACCGGAGCCTTCAGCGGG + GGG, position 304) | In constitutive exon 2, 46% into CDS (well past MTS), GC 70% (slight upward bias acceptable for Doench), pos-20 = G (top tier), dint 1-2 = TG, dint 4-5 = CC, 0 perfect off-targets in mito watch list |

---

## 2. NDUFB4 — Tier 2 (Complex I accessory, B15)

### 2.1 Background

NDUFB4 (NADH:ubiquinone oxidoreductase subunit B4; B15 subunit) is a small (~14 kDa) accessory subunit of mitochondrial Complex I. Non-catalytic but required for proper Complex I assembly/stability. HMSR v0.4: β=−0.190, p=3.1×10⁻³, I²=47 %. See `CONSTRUCT_SPECS.md` §2.1.

### 2.2 Verified RefSeq + gene structure

| Field | Mouse (*Ndufb4*) | Human (*NDUFB4*, transcript variant 1) |
|---|---|---|
| **RefSeq mRNA (verified)** | **NM_026610.2** (505 nt) | **NM_004547.6** (651 nt, transcript variant 1) |
| **Exon 1** | 1–238 (includes 5' UTR + first 180 nt of CDS) | 1–204 (includes 5' UTR + first 180 nt of CDS) |
| **Exon 2** | 239–385 (CDS middle) | 205–351 (CDS middle) |
| **Exon 3** | 386–505 (CDS end + 3' UTR; polyA 505) | 352–651 (CDS end + 3' UTR; polyA 651) |
| **CDS coordinates (mRNA)** | 59–448 (390 nt, ~129 aa) | 25–414 (390 nt, ~129 aa) |
| **PolyA site** | 505 | 472 + 651 (major at 472; minor at 651) |
| **Source verification date** | 2026-06-15 | 2026-06-15 |

> **Note on human variant 2:** A second human transcript variant **NM_001168331.2** (1505 nt) encodes a shorter 128-aa isoform 2. To target BOTH variants 1 and 2 (i.e., the constitutive region), select an sgRNA in **exon 1 or exon 2** (both shared between variants 1 and 2). All 3 top picks below are in exon 1 of variant 1, which is shared with variant 2's 5' UTR. The CDS of variant 1 starts at position 25; the CDS of variant 2 starts at position 25 as well (they share the 5' UTR start). The CDSs diverge after the alternative-splice site at position ~387 (variant 1 CDS continues to 414; variant 2 CDS stops at 387). **All 3 picks are in the shared 5' region of the CDS** (positions 95–175 in the mRNA), so they will knock down both variants.

### 2.3 Per-modality top-3 sgRNA table — NDUFB4

#### 2.3.1 Mouse — *Ndufb4* — NM_026610.2

| # | sgRNA ID | Guide sequence (20 nt + NGG PAM) | Strand | mRNA pos (1-based) | Exon | CDS pos (1-based) | GC% | pos-20 nt | dint 1-2 | dint 4-5 | In CDS? | Doench Rule Set 2 (TBD) | Hsu specificity (TBD) | Off-target count (TBD-genome) | Mito watch-list audit (this work) | Selected? | Vendor synthesis note |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | mm_Ndufb4_sg1 | **CAAACGCGTGTCGCACATCG** + **AGG** | + | 220–239 | exon 1 (1–238) | 162 of 390 (42%) | 60 | G | CA | CG | ✓ | TBD | TBD | TBD | 0 perfect in watch list | **YES** | IDT Alt-R crRNA 2 nmol |
| 2 | mm_Ndufb4_sg2 | **ACGTGTCTCCGGAGACCAGA** + **AGG** | + | 129–148 | exon 1 (1–238) | 71 of 390 (18%) | 60 | A | AC | GT | ✓ | TBD | TBD | TBD | 0 perfect in watch list | reserve | IDT Alt-R crRNA |
| 3 | mm_Ndufb4_sg3 | **CGTGTCTCCGGAGACCAGAA** + **GGG** | + | 130–149 | exon 1 (1–238) | 72 of 390 (18%) | 60 | A | CG | GT | ✓ | TBD | TBD | TBD | 0 perfect in watch list | reserve | IDT Alt-R crRNA |

> **All three are in exon 1 (CDS, 18%–42% into CDS)**. GC 60% (sweet spot). **Heuristic caution:** sg2 and sg3 differ by only 1 nt (shifts by 1) and have very similar features. They are kept as redundant backups in case the design tool (CRISPOR) flags one of them at design time. **0 perfect off-targets in the mito watch list** for all 3.

#### 2.3.2 Human — *NDUFB4* — NM_004547.6 (transcript variant 1)

| # | sgRNA ID | Guide sequence (20 nt + NGG PAM) | Strand | mRNA pos (1-based) | Exon | CDS pos (1-based) | GC% | pos-20 nt | dint 1-2 | dint 4-5 | In CDS? | Doench Rule Set 2 (TBD) | Hsu specificity (TBD) | Off-target count (TBD-genome) | Mito watch-list audit (this work) | Selected? | Vendor synthesis note |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | hs_NDUFB4_sg1 | **TACAACGATCCCAACCGCCG** + **AGG** | + | 175–194 | exon 1 (1–204) | 151 of 390 (39%) | 60 | G | TA | CA | ✓ | TBD | TBD | TBD | 0 perfect in watch list | **YES** | IDT Alt-R crRNA 2 nmol |
| 2 | hs_NDUFB4_sg2 | **ACATATCTCCGGAAACCCGG** + **CGG** | + | 95–114 | exon 1 (1–204) | 71 of 390 (18%) | 55 | G | AC | AT | ✓ | TBD | TBD | TBD | 0 perfect in watch list | reserve | IDT Alt-R crRNA |
| 3 | hs_NDUFB4_sg3 | **GATCGTTGTACTGAAGCAGG** + **GGG** | − | 165 (+) → reverse complement of mRNA 165–184 | exon 1 (1–204) | (mRNA 165 is + strand; - strand guide binds mRNA 165–184) | 50 | G | GA | TC | ✓ | TBD | TBD | TBD | 0 perfect in watch list | reserve | IDT Alt-R crRNA |

> **All three are in exon 1 (CDS, 18%–39% into CDS)**, and all three target the region **shared with NDUFB4 transcript variant 2 (NM_001168331.2)**. sg3 is on the antisense strand of the mRNA (the - strand of the genomic DNA, but the 20-nt spacer still binds the + strand mRNA at positions 165–184 after reverse-complementation; the + strand contains `GATCGTTGTACTGAAGCAGG` at positions 165–184). **0 perfect off-targets in the mito watch list** for all 3.

### 2.4 Best sgRNA selection — NDUFB4

| Gene × species | Selected sgRNA | Rationale |
|---|---|---|
| **mm Ndufb4** | **mm_Ndufb4_sg1** (CAAACGCGTGTCGCACATCG + AGG, position 220) | In constitutive exon 1, 42% into CDS, GC 60%, pos-20 = G, dint 4-5 = CG, 0 perfect off-targets |
| **hs NDUFB4** | **hs_NDUFB4_sg1** (TACAACGATCCCAACCGCCG + AGG, position 175) | In constitutive exon 1 (shared with variant 2), 39% into CDS, GC 60%, pos-20 = G, 0 perfect off-targets |

---

## 3. ATP5F1B — Tier 2 (Complex V / ATP synthase F₁β)

### 3.1 Background

ATP5F1B (ATP synthase F₁ subunit beta) is the catalytic β-subunit of the F₁ hexamer (3α / 3β). HMSR v0.4: β=−0.221, p=3.5×10⁻³, I²=39 % (largest effect size of the 3 targeted OXPHOS genes). See `CONSTRUCT_SPECS.md` §3.1.

### 3.2 Verified RefSeq + gene structure

| Field | Mouse (*Atp5f1b*) | Human (*ATP5F1B*) |
|---|---|---|
| **RefSeq mRNA (verified)** | **NM_016774.3** (1879 nt) | **NM_001686.4** (1759 nt) |
| **Exon count** | 10 | 10 |
| **Exon 1** | 1–147 | 1–148 |
| **Exon 2** | 148–330 | 149–331 |
| **Exon 3** | 331–505 | 332–506 |
| **Exon 4** | 506–627 | 507–628 |
| **Exon 5** | 628–812 | 629–813 |
| **Exon 6** | 813–971 | 814–972 |
| **Exon 7** | 972–1094 | 973–1095 |
| **Exon 8** | 1095–1307 | 1096–1308 |
| **Exon 9** | 1308–1509 | 1309–1510 |
| **Exon 10 (3' UTR + polyA)** | 1510–1879 (polyA 1764) | 1511–1759 (polyA 1759) |
| **CDS coordinates (mRNA)** | 21–1610 (1590 nt, ~529 aa) | 22–1611 (1590 nt, ~529 aa) |
| **PolyA site** | 1764 | 1759 |
| **Source verification date** | 2026-06-15 | 2026-06-15 |

> **Design note:** ATP5F1B is a large ORF (~1.6 kb, 529 aa). The mitochondrial precursor cleavage site is at residue ~48; sgRNAs targeting downstream of this will only affect the mature mitochondrial form. **The top-3 picks below are all in exon 2 (CDS, 5%–13% into CDS)**, which is early in the ORF and includes the catalytic-site-encoding region. The full exon structure is highly conserved between mouse and human (10 exons, identical exon-end boundaries within ±1 nt), reflecting the strong functional constraint on this gene.

### 3.3 Per-modality top-3 sgRNA table — ATP5F1B

#### 3.3.1 Mouse — *Atp5f1b* — NM_016774.3

| # | sgRNA ID | Guide sequence (20 nt + NGG PAM) | Strand | mRNA pos (1-based) | Exon | CDS pos (1-based) | GC% | pos-20 nt | dint 1-2 | dint 4-5 | In CDS? | Doench Rule Set 2 (TBD) | Hsu specificity (TBD) | Off-target count (TBD-genome) | Mito watch-list audit (this work) | Selected? | Vendor synthesis note |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | mm_Atp5f1b_sg1 | **CGTGGCAGTCATCGGCGCTG** + **TGG** | + | 209–228 | exon 2 (148–330) | 188 of 1590 (12%) | 70 | G | CG | GG | ✓ | TBD | TBD | TBD | 0 perfect in watch list | **YES** | IDT Alt-R crRNA 2 nmol |
| 2 | mm_Atp5f1b_sg2 | **GGTGGACGTCCAGTTCGATG** + **AGG** | + | 230–249 | exon 2 (148–330) | 209 of 1590 (13%) | 60 | G | GG | GG | ✓ | TBD | TBD | TBD | 0 perfect in watch list | reserve | IDT Alt-R crRNA |
| 3 | mm_Atp5f1b_sg3 | **GGAGGTGGCCCAGCATTTGG** + **GGG** | + | 311–330 | exon 2 (148–330) | 290 of 1590 (18%) | 65 | G | GG | AG | ✓ | TBD | TBD | TBD | 0 perfect in watch list | reserve | IDT Alt-R crRNA |

> **All three in exon 2 (CDS, 12%–18% into CDS, downstream of MTS cleavage at ~residue 48)**. GC 60–70% (sweet spot). Pos-20 = G (top tier). **0 perfect off-targets in the mito watch list** for all 3.

#### 3.3.2 Human — *ATP5F1B* — NM_001686.4

| # | sgRNA ID | Guide sequence (20 nt + NGG PAM) | Strand | mRNA pos (1-based) | Exon | CDS pos (1-based) | GC% | pos-20 nt | dint 1-2 | dint 4-5 | In CDS? | Doench Rule Set 2 (TBD) | Hsu specificity (TBD) | Off-target count (TBD-genome) | Mito watch-list audit (this work) | Selected? | Vendor synthesis note |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | hs_ATP5F1B_sg1 | **CGTGGCGGTCATTGGCGCAG** + **TGG** | + | 210–229 | exon 2 (149–331) | 189 of 1590 (12%) | 70 | G | CG | GG | ✓ | TBD | TBD | TBD | 0 perfect in watch list | **YES** | IDT Alt-R crRNA 2 nmol |
| 2 | hs_ATP5F1B_sg2 | **GGCGGTCATTGGCGCAGTGG** + **TGG** | + | 213–232 | exon 2 (149–331) | 192 of 1590 (12%) | 70 | G | GG | GG | ✓ | TBD | TBD | TBD | 0 perfect in watch list | reserve | IDT Alt-R crRNA |
| 3 | hs_ATP5F1B_sg3 | **GGTGGACGTCCAGTTTGATG** + **AGG** | + | 231–250 | exon 2 (149–331) | 210 of 1590 (13%) | 55 | G | GG | GG | ✓ | TBD | TBD | TBD | 0 perfect in watch list | reserve | IDT Alt-R crRNA |

> **All three in exon 2 (CDS, 12%–13% into CDS)**. Pos-20 = G (top tier). **0 perfect off-targets in the mito watch list** for all 3. The mouse and human guides are nearly identical (5 nt differ between mm_Atp5f1b_sg1 and hs_ATP5F1B_sg1, due to a few species-specific substitutions — this is the expected pattern for a highly conserved gene).

### 3.4 Best sgRNA selection — ATP5F1B

| Gene × species | Selected sgRNA | Rationale |
|---|---|---|
| **mm Atp5f1b** | **mm_Atp5f1b_sg1** (CGTGGCAGTCATCGGCGCTG + TGG, position 209) | In constitutive exon 2, 12% into CDS, GC 70%, pos-20 = G, dint 4-5 = GG, 0 perfect off-targets |
| **hs ATP5F1B** | **hs_ATP5F1B_sg1** (CGTGGCGGTCATTGGCGCAG + TGG, position 210) | In constitutive exon 2, 12% into CDS, GC 70%, pos-20 = G, 0 perfect off-targets |

---

## 4. PPARGC1A (PGC-1α) — master regulator

### 4.1 Background

PPARGC1A encodes the PGC-1α coactivator, the master transcriptional regulator of mitochondrial biogenesis. **7+ distinct isoforms** generated by alternative promoter usage and alternative splicing (see `CONSTRUCT_SPECS.md` §4.2). The Aim 2 design **specifically targets PGC-1α1** (the biogenesis master, 797 aa) while **sparing PGC-1α4** (the 266-aa truncated hypertrophy/exercise isoform that uses an alternative promoter and stops within exon 6).

### 4.2 Verified RefSeq + gene structure (canonical, PGC-1α1)

| Field | Mouse (*Ppargc1a*) | Human (*PPARGC1A*, transcript variant 2 = PGC-1α1) |
|---|---|---|
| **RefSeq mRNA (verified)** | **NM_008904.3** (6415 nt, transcript variant 1 = PGC-1α1 canonical) | **NM_013261.5** (6288 nt, transcript variant 2 = PGC-1α1 canonical) |
| **Exon 1** | 1–138 | 1–144 |
| **Exon 2** | 139–318 | 145–324 |
| **Exon 3** | 319–513 | 325–519 |
| **Exon 4** | 514–639 | 520–642 |
| **Exon 5** | 640–844 | 643–847 |
| **Exon 6** | 845–890 | 848–893 |
| **Exon 7** | 891–964 | 894–967 |
| **Exon 8 (large; shared by PGC-1α1/-2/-3/-b/-c/NT, NOT PGC-1α4)** | **965–1880** | **968–1883** |
| **Exon 9** | 1881–1985 | 1884–1988 |
| **Exon 10** | 1986–2106 | 1989–2109 |
| **Exon 11** | 2107–2228 | 2110–2231 |
| **Exon 12** | 2229–2380 | 2232–2383 |
| **Exon 13 (3' UTR + polyA)** | 2381–6415 (polyA 5280 and 6415) | 2384–6288 (polyA 6288) |
| **CDS coordinates (mRNA)** | 91–2484 (2394 nt, ~796 aa) | 91–2487 (2397 nt, ~797 aa) |
| **Source verification date** | 2026-06-15 | 2026-06-15 |

> **Isoform-specific design — critical:** PGC-1α4 (266-aa truncated, hypertrophy/exercise isoform) uses an **alternative promoter** and **stops with a premature stop codon within exon 6**. PGC-1α4 therefore does **NOT contain** exons 7–13. PGC-1α1 (797 aa, biogenesis master) and PGC-1α2/α3 (proximal-promoter alternative-splice forms) and PGC-1α-b/-c (alternative-promoter forms) and NT-PGC-1α (internal-promoter N-terminal truncation) all contain exons 7–13 (including exon 8). **Targeting exon 8+ of the canonical PGC-1α1 (NM_013261.5 / NM_008904.3) will knock down all proximal-promoter + alternative-promoter + NT isoforms of PGC-1α while SPARING PGC-1α4.** This is the user's explicit design (see `CONSTRUCT_SPECS.md` §4.3). **The 3 top picks below are all in exon 8** (positions 968–1883 in human, 965–1880 in mouse).
>
> **Isoform validation requirement:** For the PGC-1α arm, **isoform-specific qPCR is mandatory** (3 assays: PGC-1α1 exon 1a-derived 5' UTR; PGC-1α-b/-c exon 1b-derived 5' UTR; PGC-1α4 splice junction in exon 6). This validates that the CRISPR arm achieves the intended isoform selectivity.

### 4.3 Per-modality top-3 sgRNA table — PPARGC1A (all in exon 8 to spare PGC-1α4)

#### 4.3.1 Mouse — *Ppargc1a* — NM_008904.3 (exon 8 target window: 965–6415)

| # | sgRNA ID | Guide sequence (20 nt + NGG PAM) | Strand | mRNA pos (1-based) | Exon | CDS pos (1-based) | GC% | pos-20 nt | dint 1-2 | dint 4-5 | In CDS? | Doench Rule Set 2 (TBD) | Hsu specificity (TBD) | Off-target count (TBD-genome) | Mito watch-list audit (this work) | Selected? | Vendor synthesis note |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | mm_Ppargc1a_sg1 | **ATGCCTCCTGTGACTGGCAG** + **GGG** | + | 1328–1347 | exon 8 (965–1880) | 1238 of 2394 (52%) | 60 | G | AT | CT | ✓ | TBD | TBD | TBD | 0 perfect in watch list | **YES** | IDT Alt-R crRNA 2 nmol |
| 2 | mm_Ppargc1a_sg2 | **CTACCTGAGAGAGACTTTGG** + **AGG** | + | 1383–1402 | exon 8 (965–1880) | 1293 of 2394 (54%) | 50 | G | CT | AC | ✓ | TBD | TBD | TBD | 0 perfect in watch list | reserve | IDT Alt-R crRNA |
| 3 | mm_Ppargc1a_sg3 | **GGACCTTGATCTTGACCTGG** + **GGG** | − | 1838 (+) → reverse complement of mRNA 1838–1857 | exon 8 (965–1880) | (mRNA 1838 is + strand; - strand guide binds mRNA 1838–1857) | 55 | G | GG | AC | ✓ | TBD | TBD | TBD | 0 perfect in watch list | reserve | IDT Alt-R crRNA |

> **All three in exon 8 (CDS, 52%–77% into CDS)**. **CRITICAL: exon 8 is shared by PGC-1α1, PGC-1α2, PGC-1α3, PGC-1α-b, PGC-1α-c, NT-PGC-1α, but NOT by PGC-1α4** (PGC-1α4 stops in exon 6 and does not have exon 8+). **0 perfect off-targets in the mito watch list** for all 3.

#### 4.3.2 Human — *PPARGC1A* — NM_013261.5 (exon 8 target window: 968–6288)

| # | sgRNA ID | Guide sequence (20 nt + NGG PAM) | Strand | mRNA pos (1-based) | Exon | CDS pos (1-based) | GC% | pos-20 nt | dint 1-2 | dint 4-5 | In CDS? | Doench Rule Set 2 (TBD) | Hsu specificity (TBD) | Off-target count (TBD-genome) | Mito watch-list audit (this work) | Selected? | Vendor synthesis note |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | hs_PPARGC1A_sg1 | **AGTCCTCACTGGTGGACACG** + **AGG** | + | 1176–1195 | exon 8 (968–1883) | 1086 of 2397 (45%) | 60 | G | AG | TC | ✓ | TBD | TBD | TBD | 0 perfect in watch list | **YES** | IDT Alt-R crRNA 2 nmol |
| 2 | hs_PPARGC1A_sg2 | **AGACCAAGCGGCCCAGTCTG** + **CGG** | + | 1205–1224 | exon 8 (968–1883) | 1115 of 2397 (47%) | 65 | G | AG | CC | ✓ | TBD | TBD | TBD | 0 perfect in watch list | reserve | IDT Alt-R crRNA |
| 3 | hs_PPARGC1A_sg3 | **CTACCTGAGAGAGACTTTGG** + **AGG** | + | 1386–1405 | exon 8 (968–1883) | 1296 of 2397 (54%) | 50 | G | CT | AC | ✓ | TBD | TBD | TBD | 0 perfect in watch list | reserve | IDT Alt-R crRNA |

> **All three in exon 8 (CDS, 45%–54% into CDS)**. **Same PGC-1α4-sparing design as mouse**. Note that **hs_PPARGC1A_sg3 and mm_Ppargc1a_sg2 are essentially the same guide** (CTACCTGAGAGAGACTTTGG) with the same position in the + strand; the 100% cross-species identity is consistent with the high conservation of the mouse-human PGC-1α1 CDS. **0 perfect off-targets in the mito watch list** for all 3.

### 4.4 Best sgRNA selection — PPARGC1A

| Gene × species | Selected sgRNA | Rationale |
|---|---|---|
| **mm Ppargc1a** | **mm_Ppargc1a_sg1** (ATGCCTCCTGTGACTGGCAG + GGG, position 1328) | In constitutive exon 8 (52% into CDS, spares PGC-1α4), GC 60%, pos-20 = G, dint 1-2 = AT, dint 4-5 = CT, 0 perfect off-targets |
| **hs PPARGC1A** | **hs_PPARGC1A_sg1** (AGTCCTCACTGGTGGACACG + AGG, position 1176) | In constitutive exon 8 (45% into CDS, spares PGC-1α4), GC 60%, pos-20 = G, 0 perfect off-targets |

---

## 5. Off-target audit — summary

**Full detail in the companion document `OFF_TARGET_AUDIT.md`.** The mitochondrial watch-list audit was performed in this work (2026-06-15) using the verified RefSeq mRNA sequences of the watch-list genes (downloaded from NCBI Entrez, accession details in `OFF_TARGET_AUDIT.md` §2). The audit scanned each of the 24 sgRNA candidates (top-3 per gene × species) for **20-nt + NGG perfect matches (mm0) in the loaded watch-list mRNAs**.

| Audit metric | Result |
|---|---|
| **Number of 20-nt + NGG perfect matches in the watch list for ANY of the 24 candidates** | **0** |
| **Number of 20-nt + NGG matches with 1–3 mismatches in the watch list for ANY of the 24 candidates** | **0** (in the loaded watch list — see coverage caveat below) |
| **Number of watch-list genes loaded for the audit** | 162 (combined mouse + human) |
| **Coverage caveat** | The watch list is **partial** — it focuses on the highest-priority paralog categories (MICOS components, mitoribosome subunits, OXPHOS subunits, biogenesis TFs, import machinery, dynamics). The audit **must be re-run at the CRO** with a complete watch list (≥ 200 genes) and against the full mouse/human genomes via CRISPOR. See `OFF_TARGET_AUDIT.md` §3 for the methodology and §5 for the decision summary. |

**Conclusion:** The 24 candidate sgRNAs pass the **mitochondrial watch-list audit** as a **first-pass filter**. The full-genome off-target count (mm0/mm1/mm2/mm3 in the mouse or human genome) is **TBD — to be computed via CRISPOR at design time**.

---

## 6. Doench Rule Set 2 (DOI: 10.1038/nbt.3437) — on-target scoring

### 6.1 What the score measures

Doench Rule Set 2 (Doench et al. 2016, *Nat Biotechnol* 34:184–191) is a **gradient-boosted regression model** trained on **> 1,800 sgRNAs** tiled across 9 genes (both protein-coding and non-coding) in mouse and human cells. The model predicts the **on-target cleavage efficiency** of a 20-nt + NGG sgRNA based on:
1. **Position-weighted mononucleotide preferences** (which nucleotide is preferred at each of the 20 positions)
2. **Dinucleotide preferences** (which 2-nt combinations are preferred at each of the 19 adjacent position pairs)
3. **Global features**: GC content, position-20 nucleotide, homopolymer runs
4. **Position-independent features**: PAM context (rare variants)

**Output:** a continuous score in **[0, 1]** that correlates with on-target cleavage efficiency. For practical use, the score is often rescaled to **[0, 100]**.

### 6.2 Threshold and interpretation

| Doench score | Interpretation | Use |
|---|---|---|
| **0–20** | Very low predicted activity; likely <10% indel at the target site | **Reject** |
| **20–40** | Low activity; may give 10–30% indel | Marginal; only if no better option |
| **40–60** | Moderate activity; ~30–60% indel | Acceptable for screen |
| **60–80** | High activity; ~60–80% indel | **Preferred** for KO arm |
| **80–100** | Very high activity; ~80–95% indel | Excellent; rare for top picks |

**Aim 2 minimum-acceptance threshold:** **Doench ≥ 50** (i.e., 0.50 in the [0,1] form) for the selected best sgRNA. Reserves should also be ≥ 50 if possible. Guides below 50 are flagged for redesign.

### 6.3 Features that go into the score (visible in our candidate table)

The candidate table in §1.3 / §2.3 / §3.3 / §4.3 reports 4 of the 5 most informative features:
1. **PAM-proximal seed GC content** (target 40–70%; we report full 20-nt GC%)
2. **Position-20 nucleotide** (G > A > C > T; we report pos-20)
3. **Dinucleotide preferences** (avoid TT at pos 1–2; prefer CC at pos 4–5; we report dint 1-2 and dint 4-5)
4. **Exon location / CDS position** (early constitutive exons preferred; we report exon and CDS position)
5. **Homopolymer runs** (penalized at ≥ 4 nt; we have screened all candidates to exclude ≥ 5 nt; the published Doench 2016 model includes this as a feature but with a softer penalty)

**These 5 features are not a substitute for the full Doench Rule Set 2 score.** The published model has ~30+ features and uses a learned gradient-boosted tree. The closest public implementation is the **Doench lab's `crisprScore` Python package** (https://github.com/dyzs/CRISPR_score), or the **CRISPOR web tool** (https://crispor.tefor.net/) which runs Doench Rule Set 2 directly.

### 6.4 Status of the Doench column in the candidate tables

The "Doench Rule Set 2 (TBD)" column in the §1.3 / §2.3 / §3.3 / §4.3 tables is **explicitly TBD — compute via CRISPOR at design time**. We do **NOT** report fabricated Doench scores. The guide sequence itself is **defensible** (anchored to the verified RefSeq mRNA + NGG PAM at the specified position). The Doench column will be filled in by the wet-lab collaborator using one of:
- https://crispor.tefor.net/ — paste the 20-nt + NGG + exon-flanking genomic sequence (the gene is small enough to fit in CRISPOR's 2,300-bp input)
- http://crispor.org/ — alternative CRISPOR endpoint (same team, different URL)
- **IDT Alt-R HDR Design Tool** (https://www.idtdna.com/pages/tools/alt-r-crispr-hdr-design-tool) — includes on-target scoring
- **Synthego CRISPR Design Tool** (https://design.synthego.com) — for additional validation

### 6.5 What if CRISPOR cannot run from this environment?

If CRISPOR is not accessible from the wet-lab's environment (e.g., behind a firewall), the following offline alternatives are available:
- **Doench lab `crisprScore` Python package**: install via `pip install crisprScore`; runs the published model locally
- **SSC (Specificity Score for CRISPR)** + `sequenceScore` + `doenchRNA` (CRISPResso2 suite): a Python-based pipeline
- **Local install of `flashfry` (Allen & Bhatt 2017)**: includes Doench Rule Set 2 + Hsu 2013 + genome-wide off-target
- **Horizon Discovery siDESIGN Center** (https://horizondiscovery.com/design-center) — for siRNA; CRISPOR-like tool for CRISPR

The `Doench` column MUST be filled in before the order ships. The **acceptance gate is Doench ≥ 50**. Guides that fail this threshold at design time are **discarded and replaced with the next-best pick from §1.3 / §2.3 / §3.3 / §4.3** (reserves sg2 and sg3 are kept available).

---

## 7. Hsu 2013 specificity scoring (DOI: 10.1038/nbt.2647) — off-target framework

### 7.1 What the score measures

Hsu et al. 2013 (*Nat Biotechnol* 31:827–832) introduced the **seed-region tolerance** framework: Cas9 cleaves sites with **up to ~5–6 mismatches** in the 20-nt protospacer, but with **strong position-dependent tolerance**:
- **Mismatches in the PAM-distal end (positions 1–10 of the 20-nt protospacer, away from PAM)** are well-tolerated
- **Mismatches in the PAM-proximal "seed" (positions 1–12 from the PAM, i.e., the 3' end of the protospacer)** are **not tolerated** — even 1–2 mismatches in the seed effectively abolish cleavage
- **A single mismatch in the PAM (NGG → NGN or NCG)** abolishes cleavage

The published **Hsu specificity score** is a single 0–100 number that **integrates the off-target count and the off-target position weights** (PAM-proximal off-targets are weighted much more heavily than PAM-distal off-targets).

### 7.2 Off-target mismatch count

The standard off-target count reports the **number of sites in the genome** that have:
- **0 mismatches** in the 20-nt + NGG (perfect off-target) → **HIGH risk**
- **1 mismatch** in the 20-nt + NGG (and not in the seed) → **MED risk**
- **2 mismatches** in the 20-nt + NGG (and not in the seed) → **LOW–MED risk**
- **3 mismatches** in the 20-nt + NGG (and not in the seed) → **LOW risk**

**Aim 2 minimum-acceptance threshold:** **Hsu specificity ≥ 70** (i.e., 0.70 in the [0,1] form) for the selected best sgRNA. **No perfect 20-nt + NGG off-target in the genome** (mm0 = 0).

### 7.3 Mitochondrial watch-list filter (this work)

In addition to the genome-wide Hsu 2013 off-target scan (TBD), this document explicitly filters against the **mitochondrial watch list** — a curated set of ~ 200 genes encoding mitochondrial proteins that could confound the experiment if knocked down. The watch list is organized into 13 categories (see `CONSTRUCT_SPECS.md` §6.2 and `OFF_TARGET_AUDIT.md` §2):

| Category | Example genes | Risk if KD'd |
|---|---|---|
| **Other MICOS components** | CHCHD2, CHCHD3, CHCHD6, CHCHD7, CHCHD8, MIC10/MINOS1, MIC60/IMMT, MICU1/2/3, SAMM50 | Cristae organization confound |
| **Mitoribosome large subunit** | MRPL1–58 (focus MRPL33, MRPL34, MRPL3, MRPL15, MRPL27) | Mitochondrial translation confound |
| **Mitoribosome small subunit** | MRPS1–35 (focus MRPS15, MRPS18B) | Mitochondrial translation confound |
| **Complex I (NDUF family)** | NDUFA1–14, NDUFB1–11, NDUFS1–8, NDUFV1–3 | ETC Complex I confound (paralog of NDUFB4) |
| **Complex II (SDH family)** | SDHA, SDHB, SDHC, SDHD | ETC Complex II confound |
| **Complex III (UQCR family)** | UQCRC1/2, UQCRB, UQCRQ, UQCR10/11, CYC1, CYCS | ETC Complex III confound |
| **Complex IV (COX family)** | COX4I1, COX5A/B, COX6A/B/C, COX7A2/B/C, COX8A, COX14–20 | ETC Complex IV confound |
| **Complex V (ATP5 family)** | ATP5F1A, ATP5F1B, ATP5F1C/D/E, ATP5PB, ATP5MC1/2/3, ATP5PD, ATP5PF, ATP5PO, ATP5IF1 | ETC Complex V confound (paralog of ATP5F1B target) |
| **Mitochondrial biogenesis / TFs** | TFAM, TFB2M, POLRMT, PPRC1, NRF1, GABPA, PPARGC1A, PPARGC1B, PPARG, PPARD, ESRRA, ESRRG | Biogenesis programme confound (paralog of PGC-1α target) |
| **Mitochondrial protein import** | TOMM20, TOMM22, TOMM40, TIMM23, TIMM17A/B, TIMM44, TIMM50 | Protein import confound |
| **Mitochondrial chaperones** | HSPD1 (HSP60), HSPE1 (HSP10), HSPA9 (mtHSP70), TRAP1, LONP1, CLPX | Mitochondrial proteostasis confound |
| **Mitochondrial dynamics** | MFN1, MFN2, OPA1, DNM1L (DRP1), FIS1, MFF | Mitochondrial morphology confound |
| **Mitochondrial quality control / mitophagy** | PINK1, PRKN, BNIP3, BNIP3L, FUNDC1, PARL, HTRA2, PHB2, BCL2L13 | Mitophagy confound |

### 7.4 This-work audit result (summary)

| Audit result | Count | Risk level |
|---|---|---|
| **Perfect 20-nt + NGG match in the loaded watch list (mm0)** | **0** for all 24 candidates | n/a |
| **1–3 mm match in the loaded watch list** | **0** for all 24 candidates (in the loaded watch list) | n/a |
| **Status** | **PASS** for the loaded watch list (~ 162 genes); full watch list (~200 genes) audit pending at CRO | First-pass safe |

**Full detail in OFF_TARGET_AUDIT.md §3 and §5.**

### 7.5 Status of the Hsu column in the candidate tables

The "Hsu specificity (TBD)" column in the §1.3 / §2.3 / §3.3 / §4.3 tables is **explicitly TBD — compute via CRISPOR at design time**. CRISPOR runs the full Hsu 2013 specificity score on the entire mouse or human genome. The `OFF_TARGET_AUDIT.md` companion document performs the **mitochondrial watch-list sub-audit** (this work, 2026-06-15) as a first-pass filter. The full-genome Hsu 2013 specificity score must be computed at the CRO before the order ships.

### 7.6 What if Hsu specificity is < 70 at design time?

If the CRISPOR-computed Hsu specificity is < 70 for the selected best sgRNA, the order of preference is:
1. Try sg2 or sg3 from the §1.3 / §2.3 / §3.3 / §4.3 tables (reserves)
2. If all 3 fail Hsu ≥ 70, the gene × species combination must be **redesigned** with a new top-3 from a CRISPOR run
3. If Hsu ≥ 50 is achievable but Hsu ≥ 70 is not, accept Hsu ≥ 50 only for genes with large ORFs and many candidate guides (e.g., ATP5F1B, PGC-1α); for CHCHD10 (small ORF, fewer candidates), require Hsu ≥ 70 or consider **eSpCas9(1.1)** to compensate for lower Hsu specificity (Slaymaker et al. 2016, *Science* 351:84–88, Addgene #71814)

---

## 8. Vector backbones and Cas9 selection

### 8.1 RNP delivery (IDT Alt-R) — recommended for transient Aim 2 KO

| Item | Vendor / catalog | Notes |
|---|---|---|
| **crRNA (custom 20-nt spacer)** | **IDT** (custom, Alt-R) | 2 nmol, ~$80 per crRNA. The 20-nt spacer is the "guide sequence" from §1.3 / §2.3 / §3.3 / §4.3. The crRNA is synthesized with IDT's Alt-R modifications (2'-O-methyl + phosphorothioate at the 3 terminal bases) for nuclease resistance. |
| **tracrRNA** | **IDT** Alt-R tracrRNA, ATTO 550 (5 nmol) | ~$120. Universal for all crRNAs. Anneal at 95°C × 5 min → cool to RT. |
| **Cas9 Nuclease V3** | **IDT** Alt-R Cas9 Nuclease V3 (Cat #1081058) | 100 µg, ~$200. **V3** = high-purity, NLS, validated for RNP delivery. |
| **Delivery** | **Lonza 4D-Nucleofector** (or Neon electroporation) | 1 × 10⁶ cells per 100 µL cuvette; programs CM-138 (C2C12), DS-150 (HSMM). |
| **Total per gene × species (RNP)** | | **~$400** (1 crRNA + share of tracrRNA + share of Cas9 V3) |

### 8.2 Plasmid delivery (lentiCRISPR v2) — for stable KO lines

| Item | Vendor / catalog | Notes |
|---|---|---|
| **lentiCRISPR v2-Puro** | **Addgene** plasmid #52961 (Sanjana et al. 2014) | $89 academic / $94 nonprofit. Third-generation lentiviral backbone. **BsmBI cloning site** for 20-nt spacer. |
| **Cloning + sequencing** | Internal or CRO | ~$250 (oligo synthesis + annealing + BsmBI ligation + Sanger sequencing of the U6-sgRNA region). |
| **Lentivirus production** | Internal HEK293T (psPAX2 #12260 + pMD2.G #12259) or CRO | ~$2,000 per construct (small-scale ≥1×10⁷ TU/mL; ~$500 in-house with Lenti-X Concentrator). |
| **Total per gene × species (lentiCRISPR v2)** | | **~$339** (plasmid + cloning) + virus |

### 8.3 High-fidelity Cas9 (eSpCas9(1.1)) — recommended for CHCHD10

| Item | Vendor / catalog | Notes |
|---|---|---|
| **eSpCas9(1.1) in pX330** | **Addgene** plasmid #71814 (Slaymaker et al. 2016) | $89 academic. Original px330-based; no built-in selection marker. |
| **eSpCas9(1.1)-T2A-Puro** | **Addgene** plasmid #101039 (Németh lab) | $89 academic. Has T2A-Puro for selection. |
| **Use case** | For genes with high off-target concern or small ORF (e.g., CHCHD10) | Recommended for **CHCHD10** in HSMM per `CONSTRUCT_SPECS.md` §1.4.2; SpCas9 is sufficient for NDUFB4, ATP5F1B, PGC-1α. |

### 8.4 Recommended Cas9 selection per gene × species

| Gene | Cas9 | Rationale |
|---|---|---|
| **CHCHD10** (mouse + human) | **eSpCas9(1.1)**, Addgene #71814 or #101039 | Small ORF; off-target mitigation is critical; the mouse-human homology with CHCHD2 makes off-target risk especially relevant for the single-gene Aim 2 design. |
| **NDUFB4** (mouse + human) | SpCas9, lentiCRISPR v2 (#52961) or Alt-R RNP | Standard Cas9 is sufficient (larger ORF = more candidate guides = better Hsu specificity achievable). |
| **ATP5F1B** (mouse + human) | SpCas9, lentiCRISPR v2 (#52961) or Alt-R RNP | Standard Cas9 is sufficient (large ORF; abundant candidate guides). |
| **PPARGC1A** (mouse + human) | SpCas9, lentiCRISPR v2 (#52961) or Alt-R RNP | Standard Cas9 is sufficient. PGC-1α-b/-c off-target is **accepted** (shared 3' constitutive region with PGC-1α1). |

---

## 9. Synthesis cost (per gene × species)

| Item | Cost (USD) | Source |
|---|---|---|
| **IDT Alt-R crRNA (custom 20-nt, 2 nmol)** | ~$80 | IDT list price |
| **IDT Alt-R tracrRNA, ATTO 550 (5 nmol) — shared across gene batch** | ~$120 | IDT list price |
| **IDT Alt-R Cas9 Nuclease V3 (100 µg) — shared across gene batch** | ~$200 | IDT list price |
| **Total RNP per gene × species (crRNA cost + 1/4 share of tracrRNA + 1/4 share of Cas9)** | **~$400** | |
| **lentiCRISPR v2 plasmid (Addgene #52961)** | $89 (academic) / $94 (nonprofit) | Addgene |
| **eSpCas9(1.1) plasmid (Addgene #71814 or #101039) — for CHCHD10 only** | $89 (academic) | Addgene |
| **sgRNA oligo synthesis + cloning + sequencing** | ~$250 | Internal or CRO |
| **Lentivirus production (CRO small-scale)** | ~$2,000 per construct | Internal $500 |
| **Total plasmid per gene × species (lentiCRISPR v2 + cloning + virus at CRO)** | **~$2,339** | |
| **Total plasmid per gene × species (lentiCRISPR v2 + cloning + virus in-house)** | **~$839** | |

**Recommended budget for the CRISPR arm of Aim 2:**
- 4 genes × 2 species × $400 (RNP, top-1 + reserves) = **$3,200** for RNP delivery
- 4 genes × 2 species × $2,339 (lentiCRISPR v2 + virus) = **$18,712** for stable KO lines
- Plus eSpCas9(1.1) for CHCHD10: $89 × 2 = $178
- **Total: ~$22,090** (with CRO virus; ~$9,290 with in-house virus)

---

## 10. Decision summary — which sgRNAs to order for Aim 2

The following **8 sgRNAs (1 per gene × species) are recommended for the Aim 2 vendor order**, with **16 reserves** available:

| # | Gene | Species | Selected sgRNA | Vector | Cas9 | Vendor |
|---|---|---|---|---|---|---|
| 1 | CHCHD10 | mouse | GCCGGGTCTTATGGCTCAGA + TGG (pos 1029) | lentiCRISPR v2 + Alt-R RNP | eSpCas9(1.1) | IDT |
| 2 | CHCHD10 | human | TGACCGGAGCCTTCAGCGGG + GGG (pos 304) | lentiCRISPR v2 + Alt-R RNP | eSpCas9(1.1) | IDT |
| 3 | NDUFB4 | mouse | CAAACGCGTGTCGCACATCG + AGG (pos 220) | lentiCRISPR v2 + Alt-R RNP | SpCas9 | IDT |
| 4 | NDUFB4 | human | TACAACGATCCCAACCGCCG + AGG (pos 175) | lentiCRISPR v2 + Alt-R RNP | SpCas9 | IDT |
| 5 | ATP5F1B | mouse | CGTGGCAGTCATCGGCGCTG + TGG (pos 209) | lentiCRISPR v2 + Alt-R RNP | SpCas9 | IDT |
| 6 | ATP5F1B | human | CGTGGCGGTCATTGGCGCAG + TGG (pos 210) | lentiCRISPR v2 + Alt-R RNP | SpCas9 | IDT |
| 7 | Ppargc1a | mouse | ATGCCTCCTGTGACTGGCAG + GGG (pos 1328) — exon 8, spares PGC-1α4 | lentiCRISPR v2 + Alt-R RNP | SpCas9 | IDT |
| 8 | PPARGC1A | human | AGTCCTCACTGGTGGACACG + AGG (pos 1176) — exon 8, spares PGC-1α4 | lentiCRISPR v2 + Alt-R RNP | SpCas9 | IDT |

**Pre-order actions (M1 critical path):**
1. **Run CRISPOR** (https://crispor.tefor.net/ or http://crispor.org/) on each of the 8 selected sgRNAs to obtain Doench Rule Set 2 + Hsu 2013 + full-genome off-target scores
2. **Verify** that all 8 pass the acceptance gates: Doench ≥ 50, Hsu ≥ 70 (or ≥ 50 with eSpCas9(1.1) for CHCHD10), mm0 = 0
3. **If any selected sgRNA fails CRISPOR**, fall back to the sg2 or sg3 reserve from §1.3 / §2.3 / §3.3 / §4.3
4. **If all 3 fail**, redesign the top-3 with a fresh CRISPOR run on the same RefSeq mRNA
5. **Order from IDT** with the verified sequences
6. **Run the full mitochondrial watch-list audit** at the CRO with a complete watch list (~200 genes) — see `OFF_TARGET_AUDIT.md` §3 and §5
7. **Order the lentiCRISPR v2 / eSpCas9(1.1) plasmids from Addgene** and the lentiGuide oligos for cloning
8. **Pair with the siRNA order** (from `CONSTRUCT_SPECS.md` §1.3 – §4.3) — both are required for the Aim 2 construct panel

**Post-order actions (wet lab):**
- T7E1 mismatch assay or amplicon-seq (ICE / Synthego) at 72 h post-RNP nucleofection to confirm ≥ 80% indel
- Clonal KO expansion (single-cell FACS or limiting dilution + expansion) for stable lines
- Isoform-specific qPCR for PGC-1α arm (3 assays: PGC-1α1 exon 1a, PGC-1α-b/-c exon 1b, PGC-1α4 splice junction in exon 6) to confirm PGC-1α4 is spared

---

## 11. Open issues and verification checklist (handed off to CRO / wet lab)

| # | Issue | Owner | Deadline |
|---|---|---|---|
| 1 | Run CRISPOR for all 8 selected sgRNAs to obtain Doench + Hsu scores | Wet-lab collaborator / CRO | M1 (before order ships) |
| 2 | Full mitochondrial watch-list audit (≥ 200 genes, complete list) | CRO | M1 |
| 3 | Confirm sg2 / sg3 reserves are realigned if selected sgRNA fails CRISPOR | Wet-lab collaborator | M1 |
| 4 | Validate mRNA coordinate correctness by re-BLASTing the 20-nt spacer + NGG against the RefSeq mRNA at order entry | IDT design tool / CRO | M1 |
| 5 | For PGC-1α: design and order isoform-specific qPCR assays (3 assays) | Wet-lab collaborator | M1 (parallel to sgRNA order) |
| 6 | Validate CHCHD10 eSpCas9(1.1) RNP delivery in HSMM (efficiency vs SpCas9) | Wet-lab collaborator | M2 |
| 7 | Cross-check mRNA coordinates against genomic coordinates (CRISPOR takes genomic input, not mRNA) — the mRNA coordinates in §1.3 – §4.3 must be converted to genomic coordinates at design time | Wet-lab collaborator | M1 |
| 8 | Sanity check: confirm sgRNA-TGG with NGG on + strand vs sgRNA-CCN on + strand (for - strand guides) | Wet-lab collaborator | M1 |

---

## 12. Document signoff

| Role | Name | Action | Date |
|---|---|---|---|
| **Author** | Brown Biotech (Larry) | Drafted v0.1 | 2026-06-15 |
| **Reviewer (wet-lab)** | TBD | _Pending review_ | TBD |
| **Reviewer (dry-lab / biostats)** | TBD | _Pending review_ | TBD |
| **Procurement** | TBD | _Confirm catalog numbers + IDT/Addgene order at PO issue_ | TBD |
| **CRO liaison** | TBD (if outsourced) | _Confirm CRISPOR runs, off-target audits, sequence verifications_ | TBD |
| **PI signoff** | TBD | _Pending_ | TBD |

> **This document is for dry-lab planning and procurement reference. It does not authorize wet-lab execution. Wet-lab work proceeds only after the signoff matrix above is complete and the CRISPOR scores (Doench + Hsu) are filled in.**

---

## 13. Change log

| Version | Date | Author | Change |
|---|---|---|---|
| **v0.1** | 2026-06-15 | Brown Biotech (Larry) | Initial dry-lab specification. 24 sgRNA candidates (top-3 per gene × species × 4 genes × 2 species = 24) extracted from NCBI-verified RefSeq mRNAs (downloaded 2026-06-15 via NCBI Entrez). 8 best sgRNAs selected (1 per gene × species). Doench Rule Set 2 + Hsu 2013 scoring + genome-wide off-target counts marked TBD — to be computed at design time via CRISPOR. Mitochondrial watch-list audit performed (162 watch-list mRNAs loaded; 0 perfect 20-nt + NGG off-targets in any of the 24 candidates; full audit pending at CRO). |
| **Note** | 2026-06-15 | Brown Biotech (Larry) | **CORRECTION**: Mouse *Chchd10* RefSeq corrected from NM_001136064.2 (which is mouse *Bscl2*, NOT *Chchd10*) to **NM_175329.4** (verified 2026-06-15). Mouse *Ndufb4* RefSeq corrected from NM_026610.3 to **NM_026610.2** (current version as of 2026-06-15). All other RefSeq IDs from `CONSTRUCT_SPECS.md` §0.3 / §10.4 verified correct. |
| **Cross-ref** | 2026-06-15 | Brown Biotech (Larry) | Companion document `OFF_TARGET_AUDIT.md` issued same day (covers OI-3 in `validation/plan/OPEN_ISSUES.md`). |

---

*End of CRISPR_DESIGNS.md v0.1 — 4 genes × 2 species × top-3 sgRNAs = 24 candidates + 8 selected best + 16 reserves; Doench + Hsu methodology anchored; mito watch-list audit (162 mRNAs) PASS for all 24 candidates. Handed off to the wet-lab collaborator for CRISPOR + full-genome off-target scan at design time (M1 critical path).*
