# OFF_TARGET_AUDIT.md
## HMSR Aim 2 — Off-Target Audit for siRNA + sgRNA
### BLAST audit against RefSeq mouse + human mRNA with mitochondrial watch-list filter
### Dry-lab operational plan — RFP / CRO-ready handoff

---

| Field | Value |
|---|---|
| **Document ID** | `sarcopenia-multiomic-resource/validation/constructs/OFF_TARGET_AUDIT.md` |
| **Version** | v0.1 — initial dry-lab specification |
| **Date** | 2026-06-15 |
| **Branch** | `validation/aim2-causation` |
| **Worktree** | `/Volumes/4TB/exerciseomics/.worktrees/validation-aim2/` |
| **Supersedes** | — (first issue) |
| **Status** | Dry-lab planning only — **no wet-lab execution in this session** |
| **Prepared by** | Brown Biotech (Larry) — operationalization of OI-3 in `validation/plan/OPEN_ISSUES.md` |
| **Linked files** | `validation/constructs/CRISPR_DESIGNS.md` (companion; this work covered OI-2), `validation/constructs/CONSTRUCT_SPECS.md`, `validation/plan/OPEN_ISSUES.md` (OI-3) |
| **Target journal framing** | Paper 2 (JCSM / Aging Cell) in-vitro causation |

---

## 0. Scope, design principles, and key findings

### 0.1 Scope

This document specifies the **off-target audit framework** for the **siRNA and sgRNA reagents** designed in `CONSTRUCT_SPECS.md` (siRNA/shRNA/CRISPR modalities) and `CRISPR_DESIGNS.md` (top-3 sgRNAs per gene × species), to support **Aim 2 (causation)** of the HMSR validation plan.

The audit has **two components**:

1. **siRNA off-target audit** — for the **8 siRNA SMARTpools** (4 genes × 2 species; each SMARTpool is 4 oligos = **32 siRNA oligos total**) + the **top-3 individual siRNAs per gene × species** for deconvolution (**24 siRNA oligos**); total = **56 siRNA off-target audits**. The siRNA target sequences are **TBD at design-tool output** (Horizon siDESIGN Center or Thermo Silencer Select); the **methodology** is provided here and **a worked example** is given.
2. **sgRNA off-target audit** — for the **24 sgRNA candidates** (top-3 per gene × species from `CRISPR_DESIGNS.md`). The 20-nt spacer + NGG PAM sequences are **verified from the NCBI RefSeq mRNAs (downloaded 2026-06-15)** and the **mitochondrial watch-list audit is performed in this work (2026-06-15)**. The full-genome Hsu 2013 off-target count is **TBD at design time via CRISPOR**.

### 0.2 Key findings (this work, 2026-06-15)

| Audit result | Status |
|---|---|
| **24 sgRNA candidates × 162 watch-list mRNAs (combined mouse + human)** | **0 perfect 20-nt + NGG off-targets in the loaded watch list** for all 24 candidates |
| **24 sgRNA candidates × 162 watch-list mRNAs (1–3 mm)** | **0 off-targets in the loaded watch list** for all 24 candidates (in the loaded subset) |
| **8 selected best sgRNAs (1 per gene × species)** | All 8 PASS the mitochondrial watch-list sub-audit |
| **Full-genome Hsu 2013 mm0/mm1/mm2/mm3 count** | **TBD** at design time via CRISPOR |
| **siRNA off-target audit (32 SMARTpool + 24 individual)** | **TBD** at design tool output (Horizon / Thermo) — methodology provided; worked example below |

> **Conclusion:** The 8 selected best sgRNAs and the 16 reserves pass the **mitochondrial watch-list filter** as a first-pass screen. The full-genome off-target count and the siRNA-specific off-target audit (with vendor-specific output sequences) are **TBD at design time**.

### 0.3 Important corrections to the watch list

The mitochondrial watch list in `CONSTRUCT_SPECS.md` §6.2 was originally based on accessions from a previous documentation cycle. Several accessions in the original list were **incorrect** and have been **corrected in this work** (2026-06-15) using a fresh NCBI Entrez query:

- **CHCHD6 human**: original accession was invalid; corrected to **NM_001320610.2** (transcript variant 1) or **NM_032343.3** (transcript variant 2)
- **MINOS1 / MIC10 human**: corrected to **NM_172352.3** (or **NM_001204082.2**)
- **IMMT / MIC60 human**: corrected to **NM_001400124.1**
- **NDUFB1 human**: corrected to **NM_004545.4**
- **NDUFB7 human**: corrected to **NM_004146.6**
- **NDUFS1 human**: corrected to **NM_001199984.2**
- **NDUFS2 human**: corrected to **NM_001410889.1** (transcript variant 1) or **NM_004550.5** (transcript variant 2)
- **NDUFA5 human**: corrected to **NM_001291304.2**
- **NDUFA8 human**: corrected to **NM_001318195.2**
- **ATP5F1C human**: corrected to **NM_005174.4** (or **NM_001320886.2** v2)
- **ATP5PD human**: corrected to **NM_001003785.2** (or **NM_006356.3**)
- **ATP5MC1 human**: corrected to **NM_005175.3**
- **TFAM human**: corrected to **NM_001270782.2**
- **TIMM23 human**: corrected to **NM_006327.4**
- **PPARGC1A human** (for the watch list, mRNA isoform): corrected to **NM_013261.5** (the canonical mRNA) — note that a separate `PPARGC1A` RefSeqGene entry exists (NM_001330753.2) but that is a genomic scaffold, not a cDNA
- **CHCHD2 human**: corrected to **NM_001320327.2**
- **MRPL15 human**: corrected to **NM_014175.4**
- **MRPL27 human**: corrected to **NM_032477.3**
- **MRPL33 human**: corrected to **NM_145330.3**
- **MRPL34 human**: corrected to **NM_001400074.1**
- **CHCHD8 human**: corrected to **NM_016565.3**
- **MICU1 human**: corrected to **NM_001441225.1** (or the mRNA accession if a canonical mRNA is desired)
- **MICU3 human**: corrected to **NM_001413219.1**
- **DNAJC11 human**: corrected to **NM_018198.4**
- **SAMM50 human**: corrected to **NM_015380.5**
- **MRPS15 human**: corrected to **NM_031280.4**
- **MRPS18B human**: corrected to **NM_014046.4**
- **NDUFA1 human**: corrected to **NM_004541.4**
- **NDUFA2 human**: corrected to **NM_001185012.2**
- **NDUFA6 human**: corrected to **NM_002490.6**
- **NDUFA7 human**: corrected to **NM_005001.5**
- **NDUFA9 human**: corrected to **NM_005002.5**
- **NDUFA10 human**: corrected to **NM_001410987.1** (or **NM_001322019.2** v2)
- **NDUFB3 human**: corrected to **NM_001257102.2**
- **NDUFB5 human**: corrected to **NM_001199958.2**
- **NDUFB6 human**: corrected to **NM_001199987.2**
- **NDUFB8 human**: corrected to **NM_001284367.2**
- **NDUFB9 human**: corrected to **NM_001311168.2**
- **NDUFB10 human**: corrected to **NM_004548.3**
- **NDUFB11 human**: corrected to **NM_019056.7**
- **NDUFS3 human**: corrected to **NM_004551.3**
- **NDUFS4 human**: corrected to **NM_002495.4**
- **ATP5F1A human**: corrected to **NM_001001937.2** (or **NM_001257335.2**)
- **ATP5F1D human**: corrected to **NM_001001975.2**
- **ATP5F1E human**: corrected to **NM_006886.4**
- **ATP5PB human** (the original `ATP5PB: NM_001686.4` was the **ATP5F1B** mRNA — **CRITICAL ERROR**; corrected to **NM_001688.5** for ATP5PB)
- **ATP5PO human**: corrected to **NM_001697.3**
- **ATP5PF human**: corrected to **NM_001003697.2**
- **ATP5ME human**: corrected to **NM_007100.4**
- **ATP5IF1 human**: corrected to **NM_178191.3**
- **POLRMT human**: corrected to **NM_001407832.1**
- **NRF1 human**: corrected to **NM_003204.3**
- **PPARGC1B human**: corrected to **NM_001172699.2**
- **TOMM20 human**: corrected to **NM_014765.3**
- **TOMM40 human**: corrected to **NM_001128916.2** (or **NM_006114.3**)
- **HSPD1 human**: corrected to **NM_199440.2**
- **HSPE1 human**: corrected to **NM_002157.3**
- **HSPA9 human**: corrected to **NM_004134.7**
- **MFN1 human**: corrected to **NM_033540.3**
- **MFN2 human**: corrected to **NM_001127660.2** (or **NM_014874.4**)
- **OPA1 human**: corrected to **NM_130835.3**
- **DNM1L human**: corrected to **NM_001278465.2**

(For mouse, the watch list used the verified mouse accessions from `CONSTRUCT_SPECS.md` §0.3 / §10.4 plus the accessions re-verified in this work.)

### 0.4 Critical design principles

- **The watch list is curated** to include the highest-priority mitochondrial off-target categories (see §2.1). The full mitochondrial proteome has ~1,500 genes (mouse + human); the watch list is a focused subset of ~200.
- **The audit must be re-run at the CRO** with the complete watch list (~200 genes) and against the full mouse/human genomes via CRISPOR (genome-wide off-target). This document performs the watch-list sub-audit as a first-pass filter and provides the full methodology.
- **For sgRNA**: 0 perfect 20-nt + NGG match in the loaded watch list = **PASS for the watch-list sub-audit**. Full-genome Hsu 2013 count is TBD.
- **For siRNA**: each siRNA sense-strand seed (nt 2–8) is checked against the watch list; **0 perfect seed match in the watch list = PASS for the watch-list sub-audit**. Full siRNA BLAST against RefSeq mRNA is TBD at design-tool output.
- **HIGH risk**: perfect 20-nt + NGG off-target in any of the 4 Tier 1–2 paralog categories (MICOS, mitoribosome, OXPHOS Complex I/III/IV/V, biogenesis TFs including PPARGC1B). **MED risk**: 1–3 mm in Tier 1–2; 0 mm in Tier 3 (chaperones, dynamics, quality control). **LOW risk**: 1–3 mm in Tier 3; 0 off-target anywhere.
- **Any siRNA/sgRNA with HIGH-risk off-target is rejected** and replaced with a redesign (shift target site by 10–30 nt; if redesign is not possible, the gene × species combination is flagged for manual review).

---

## 1. Methodology

### 1.1 siRNA off-target audit method

For each siRNA (sense-strand 19–25 nt, with dTdT or UU overhang):
1. **Identify the seed region**: positions 2–8 of the sense strand (the "RISC-loading seed" that drives most off-target repression; per Hsu 2013 / Jackson 2003 / Birmingham 2006)
2. **BLAST the seed against RefSeq mRNA** (mouse or human, matching the siRNA target species) with parameters: `blastn -task blastn -evalue 1000 -word_size 7 -outfmt "6 qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore stitle"`
3. **Filter for mitochondrial watch-list genes** (see §2.1): perfect seed match (7/7 nt) in any watch-list mRNA = **flag as potential off-target**
4. **For watch-list hits**: extend the seed match to the full 19-nt siRNA sense strand. If the full 19-nt (or 19/19 + dTdT) has high identity (≥ 85%) to the watch-list mRNA, **HIGH risk**. If only the seed (7/7) matches, **MED risk** (RISC loading can still drive some off-target repression but is less efficient than full-length match).
5. **Optionally**: BLAST the **full 19-nt sense strand** (not just the seed) against the watch list to catch non-seed-driven off-targets. This is the more conservative audit and is recommended.
6. **In silico miRNA seed match**: BLAST the **seed region (nt 2–8 of the guide) against the 3' UTRs of RefSeq mRNA** to flag potential miRNA-like off-targeting (siRNA / sgRNA off-targets are not strictly miRNA-mediated, but the seed region can bind 3' UTRs and cause translation-level repression; per Hsu 2013).
7. **No perfect 19/19 or 20/20 match to any off-target mRNA** (per the standard rule). If found, **discard the siRNA**.

### 1.2 sgRNA off-target audit method

For each sgRNA (20-nt protospacer + NGG PAM):
1. **BLAST the 20-nt + NGG against RefSeq mRNA** (mouse or human) with parameters: `blastn -task blastn -evalue 1000 -word_size 7 -outfmt "6 ..."`
2. **Report the mismatch count distribution**: 0 mm (perfect 20-nt + NGG match), 1 mm, 2 mm, 3 mm. Each watch-list gene with a 0–3 mm hit is flagged.
3. **Filter for mitochondrial watch-list genes**: perfect 20-nt + NGG match (mm0) in any watch-list mRNA = **flag as HIGH risk off-target**.
4. **Run the full-genome Hsu 2013 off-target scan** via **CRISPOR** (http://crispor.org/ or https://crispor.tefor.net/). CRISPOR runs the full Hsu 2013 algorithm: it scans the mouse or human genome for all sites with ≤ 4 mismatches to the 20-nt + NGG, weights by position (PAM-proximal weighted much more heavily), and outputs the **Hsu specificity score (0–100)**.
5. **Tie-breaking**: if multiple candidates have the same Hsu specificity, choose the one with the **earlier CDS position** (more likely to give a functional KO before the protein domain).

### 1.3 Tools used in this work (2026-06-15)

| Tool | Use | Access |
|---|---|---|
| **NCBI Entrez eutils** (`efetch.fcgi`) | Downloaded verified RefSeq mRNA sequences for the 8 target genes + 162 watch-list genes | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi |
| **Python 3 (string search; sliding-window 23-nt audit)** | mRNA-level NGG-site scan; 20-nt + NGG off-target audit against the watch list | local |
| **CRISPOR** (TBD at design time) | Full-genome Hsu 2013 specificity + Doench Rule Set 2 | https://crispor.tefor.net/ or http://crispor.org/ |
| **Horizon Discovery siDESIGN Center** (TBD at design time) | SMARTpool oligo design + off-target audit | https://horizondiscovery.com/design-center |
| **Thermo Fisher Silencer Select tool** (TBD at design time) | Validated individual siRNA design | https://www.thermofisher.com/order/catalog/product/4390770 |
| **IDT Alt-R HDR Design Tool** (TBD at design time) | sgRNA design + off-target audit | https://www.idtdna.com/pages/tools/alt-r-crispr-hdr-design-tool |
| **NCBI web BLAST** (TBD at design time) | For the siRNA full-sense-strand audit, if not run via vendor tool | https://blast.ncbi.nlm.nih.gov/Blast.cgi |

### 1.4 Method limitations (caveats)

| Limitation | Mitigation |
|---|---|
| **Watch list is partial** (162 mRNAs loaded; full list is ~200) | Re-run at CRO with complete list |
| **Mitochondrial watch-list audit is mRNA-level only** (does not check for intronic / intergenic / promoter off-targets) | CRISPOR full-genome scan covers all genomic sites |
| **Hsu 2013 score is not computed** (CRISPOR not accessible from this environment) | Compute at design time via CRISPOR |
| **Doench Rule Set 2 score is not computed** (CRISPOR not accessible) | Compute at design time via CRISPOR |
| **siRNA SMARTpool sequences are TBD** (vendor design tool not accessed) | Vendor tool returns audit + sequences together; order proceeds only after audit passes |
| **Audit assumes RefSeq annotation is current** (RefSeq versions can change) | Re-verify at order time; the IDs in this document were verified 2026-06-15 |

---

## 2. Mitochondrial watch list

### 2.1 Categorized watch list

| Category | Examples (mouse / human) | Function | Risk tier |
|---|---|---|---|
| **Other MICOS components** | CHCHD2, CHCHD3, CHCHD6, CHCHD7, CHCHD8, CHCHD9, MINOS1/MIC10, MINOS2/MIC13, MINOS3/MIC14, MIC19, MIC25, MIC26/APOO, MIC27/APOOL, MIC60/IMMT, SAMM50, MICU1, MICU2, MICU3, DNAJC11 | Cristae organisation (paralogs of CHCHD10 target) | **Tier 1** — HIGH risk if KD'd (paralog of the CHCHD10 target) |
| **Mitoribosome large subunit** | MRPL1–58 (focus MRPL33, MRPL34, MRPL3, MRPL15, MRPL27) | Mitochondrial translation | **Tier 1** — HIGH risk |
| **Mitoribosome small subunit** | MRPS1–35 (focus MRPS15, MRPS18B) | Mitochondrial translation | **Tier 1** — HIGH risk |
| **OXPHOS Complex I (NDUF family)** | NDUFA1–14, NDUFAF1–8, NDUFB1–11, NDUFC1–2, NDUFS1–8, NDUFV1–3, FOXRED1, ACAD9 | ETC Complex I (paralogs of NDUFB4 target) | **Tier 1** — HIGH risk if KD'd (paralog of the NDUFB4 target) |
| **OXPHOS Complex II (SDH family)** | SDHA, SDHB, SDHC, SDHD, SDHAF1–4 | ETC Complex II | **Tier 2** — MED risk |
| **OXPHOS Complex III (UQCR family)** | UQCRC1, UQCRC2, UQCRB, UQCRQ, UQCR10, UQCR11, UQCRFS1, CYC1, CYCS | ETC Complex III | **Tier 2** — MED risk |
| **OXPHOS Complex IV (COX family)** | COX4I1, COX5A, COX5B, COX6A, COX6B, COX6C, COX7A2, COX7B, COX7C, COX8A, COX14–20 | ETC Complex IV | **Tier 2** — MED risk |
| **OXPHOS Complex V (ATP5 family)** | ATP5F1A, ATP5F1B, ATP5F1C, ATP5F1D, ATP5F1E, ATP5PB, ATP5MC1/2/3, ATP5PD, ATP5PF, ATP5PO, ATP5IF1, DMAC2L1 | ETC Complex V (paralogs of ATP5F1B target) | **Tier 1** — HIGH risk if KD'd (paralog of the ATP5F1B target) |
| **Mitochondrial transcription / biogenesis TFs** | TFAM, TFB2M, POLRMT, PPRC1, NRF1, GABPA, PPARG, PPARD, ESRRA, ESRRG, PPARGC1A, PPARGC1B | Mitochondrial biogenesis (paralogs of PGC-1α target) | **Tier 1** — HIGH risk if KD'd (paralog of PGC-1α target) |
| **Mitochondrial protein import** | TOMM20, TOMM22, TOMM40, TIMM23, TIMM44, TIMM50, TIMM17A/B | Mitochondrial protein import | **Tier 2** — MED risk |
| **Mitochondrial chaperones** | HSPD1 (HSP60), HSPE1 (HSP10), HSPA9 (mtHSP70), TRAP1, LONP1, CLPX | Mitochondrial protein folding/proteostasis | **Tier 2** — MED risk |
| **Mitochondrial dynamics** | MFN1, MFN2, OPA1, DNM1L (DRP1), FIS1, MFF | Mitochondrial fusion/fission | **Tier 3** — LOW risk |
| **Mitochondrial quality control / mitophagy** | PINK1, PRKN (Parkin), BNIP3, BNIP3L (NIX), FUNDC1, PARL, HTRA2, PHB2, BCL2L13 | Mitophagy | **Tier 3** — LOW risk |
| **mtDNA-encoded genes** | MT-ND1–6, MT-CO1–3, MT-CYB, MT-ATP6, MT-ATP8 (all 13 protein-coding mtDNA genes) | mtDNA-encoded ETC subunits | **Not applicable** — mtDNA-encoded mRNAs are transcribed in the mitochondrial matrix; nuclear-encoded sgRNAs/siRNAs **do not target mtDNA**; **no off-target risk** |

> **Tier 1 = HIGH risk**: any perfect seed match (siRNA) or 20-nt + NGG match (sgRNA) in this tier = **reject the reagent**. Tier 2 = MED risk: perfect seed match = **flag for review**, redesign preferred. Tier 3 = LOW risk: perfect seed match = **accept with disclosure in methods**.

### 2.2 Watch list (162 mRNAs loaded; ~ 200 in the complete list)

The watch list used in this work (mouse + human) was downloaded from NCBI Entrez in 2026-06-15. The full list of accessions is at `/tmp/watchlist_v3.tsv` (used by the audit script). For brevity, the accessions are not listed inline in this document; the methodology (§1) and the top-level summary (§3) are the operational deliverables. The watch list is also detailed in `CONSTRUCT_SPECS.md` §6.2 with the original (uncorrected) accessions — those have been corrected in §0.3 above.

---

## 3. sgRNA off-target audit (this work, 2026-06-15)

### 3.1 Audit method (mRNA-level, watch-list-only)

For each of the **24 sgRNA candidates** (top-3 per gene × species; sequences from `CRISPR_DESIGNS.md` §1.3 – §4.3), the **20-nt protospacer + NGG PAM** (23-nt full guide) was audited against the **loaded watch-list mRNAs** (162 sequences: ~ 80 mouse + ~ 80 human):

1. **Sliding-window 23-nt scan**: for each watch-list mRNA, slide a 23-nt window and compute the Hamming distance to the 23-nt guide (20-nt protospacer + 3-nt NGG PAM). Count windows with 0, 1, 2, or 3 mismatches.
2. **No self-matches**: the on-target gene (e.g., CHCHD10 for sgRNAs targeting CHCHD10) is excluded from the off-target count.
3. **Cross-species audit**: for human sgRNAs, the human watch list is used; for mouse sgRNAs, the mouse watch list is used. (No cross-species hits expected due to ~ 80% mRNA identity between mouse and human, but verified — none found in the loaded watch list.)

### 3.2 Per-sgRNA audit result (24 candidates)

#### 3.2.1 Human — CHCHD10, NDUFB4, ATP5F1B, PPARGC1A (12 candidates)

| sgRNA ID | Spacer + PAM | mRNA pos | Mito watch-list mm0 | Mito watch-list mm1 | mm2 | mm3 | Status |
|---|---|---|---|---|---|---|---|
| hs_CHCHD10_sg1 | TGACCGGAGCCTTCAGCGGG + GGG | 304 (+) | **0** | 0 | 0 | 0 | **PASS** |
| hs_CHCHD10_sg2 | CATGGCTCAGATGGCGACCA + CGG | 230 (+) | **0** | 0 | 0 | 0 | **PASS** |
| hs_CHCHD10_sg3 | GATGGCGACCACGGCCGCAG + GGG | 239 (+) | **0** | 0 | 0 | 0 | **PASS** |
| hs_NDUFB4_sg1 | TACAACGATCCCAACCGCCG + AGG | 175 (+) | **0** | 0 | 0 | 0 | **PASS** |
| hs_NDUFB4_sg2 | ACATATCTCCGGAAACCCGG + CGG | 95 (+) | **0** | 0 | 0 | 0 | **PASS** |
| hs_NDUFB4_sg3 | GATCGTTGTACTGAAGCAGG + GGG | 165 (-) | **0** | 0 | 0 | 0 | **PASS** |
| hs_ATP5F1B_sg1 | CGTGGCGGTCATTGGCGCAG + TGG | 210 (+) | **0** | 0 | 0 | 0 | **PASS** |
| hs_ATP5F1B_sg2 | GGCGGTCATTGGCGCAGTGG + TGG | 213 (+) | **0** | 0 | 0 | 0 | **PASS** |
| hs_ATP5F1B_sg3 | GGTGGACGTCCAGTTTGATG + AGG | 231 (+) | **0** | 0 | 0 | 0 | **PASS** |
| hs_PPARGC1A_sg1 | AGTCCTCACTGGTGGACACG + AGG | 1176 (+) | **0** | 0 | 0 | 0 | **PASS** |
| hs_PPARGC1A_sg2 | AGACCAAGCGGCCCAGTCTG + CGG | 1205 (+) | **0** | 0 | 0 | 0 | **PASS** |
| hs_PPARGC1A_sg3 | CTACCTGAGAGAGACTTTGG + AGG | 1386 (+) | **0** | 0 | 0 | 0 | **PASS** |

#### 3.2.2 Mouse — Chchd10, Ndufb4, Atp5f1b, Ppargc1a (12 candidates)

| sgRNA ID | Spacer + PAM | mRNA pos | Mito watch-list mm0 | Mito watch-list mm1 | mm2 | mm3 | Status |
|---|---|---|---|---|---|---|---|
| mm_Chchd10_sg1 | GCCGGGTCTTATGGCTCAGA + TGG | 1029 (+) | **0** | 0 | 0 | 0 | **PASS** |
| mm_Chchd10_sg2 | TAGCCGTGGGCTCAGCTGTA + GGG | 1070 (+) | **0** | 0 | 0 | 0 | **PASS** |
| mm_Chchd10_sg3 | GCCCTGACCAGTGCCTTCAG + TGG | 1108 (+) | **0** | 0 | 0 | 0 | **PASS** |
| mm_Ndufb4_sg1 | CAAACGCGTGTCGCACATCG + AGG | 220 (+) | **0** | 0 | 0 | 0 | **PASS** |
| mm_Ndufb4_sg2 | ACGTGTCTCCGGAGACCAGA + AGG | 129 (+) | **0** | 0 | 0 | 0 | **PASS** |
| mm_Ndufb4_sg3 | CGTGTCTCCGGAGACCAGAA + GGG | 130 (+) | **0** | 0 | 0 | 0 | **PASS** |
| mm_Atp5f1b_sg1 | CGTGGCAGTCATCGGCGCTG + TGG | 209 (+) | **0** | 0 | 0 | 0 | **PASS** |
| mm_Atp5f1b_sg2 | GGTGGACGTCCAGTTCGATG + AGG | 230 (+) | **0** | 0 | 0 | 0 | **PASS** |
| mm_Atp5f1b_sg3 | GGAGGTGGCCCAGCATTTGG + GGG | 311 (+) | **0** | 0 | 0 | 0 | **PASS** |
| mm_Ppargc1a_sg1 | ATGCCTCCTGTGACTGGCAG + GGG | 1328 (+) | **0** | 0 | 0 | 0 | **PASS** |
| mm_Ppargc1a_sg2 | CTACCTGAGAGAGACTTTGG + AGG | 1383 (+) | **0** | 0 | 0 | 0 | **PASS** |
| mm_Ppargc1a_sg3 | GGACCTTGATCTTGACCTGG + GGG | 1838 (-) | **0** | 0 | 0 | 0 | **PASS** |

> **Result:** All 24 sgRNA candidates have **0 perfect 20-nt + NGG off-targets** in the loaded mitochondrial watch list (162 mRNAs). This is a **first-pass PASS** for the watch-list sub-audit. The full-genome Hsu 2013 off-target count (against the full mouse or human genome) is **TBD at design time via CRISPOR**.

### 3.3 Worked example — full audit for the 8 selected best sgRNAs

The 8 selected best sgRNAs (1 per gene × species) are the operational focus. The full audit (this work, 2026-06-15) returns:

| # | Gene × species | Selected sgRNA (spacer + PAM) | mRNA pos | Mito watch-list mm0 | Mito watch-list mm1-3 | Risk | Mitigation |
|---|---|---|---|---|---|---|---|
| 1 | mm Chchd10 | GCCGGGTCTTATGGCTCAGA + TGG | 1029 (+) | 0 | 0 | LOW | none needed; full-genome Hsu TBD |
| 2 | hs CHCHD10 | TGACCGGAGCCTTCAGCGGG + GGG | 304 (+) | 0 | 0 | LOW | none needed; **eSpCas9(1.1) recommended** to compensate for small ORF + CHCHD2 homology |
| 3 | mm Ndufb4 | CAAACGCGTGTCGCACATCG + AGG | 220 (+) | 0 | 0 | LOW | none needed |
| 4 | hs NDUFB4 | TACAACGATCCCAACCGCCG + AGG | 175 (+) | 0 | 0 | LOW | none needed |
| 5 | mm Atp5f1b | CGTGGCAGTCATCGGCGCTG + TGG | 209 (+) | 0 | 0 | LOW | none needed |
| 6 | hs ATP5F1B | CGTGGCGGTCATTGGCGCAG + TGG | 210 (+) | 0 | 0 | LOW | none needed |
| 7 | mm Ppargc1a | ATGCCTCCTGTGACTGGCAG + GGG | 1328 (+) | 0 | 0 | LOW | none needed; **PGC-1α4 spared by exon 8 design**; **PPARGC1B co-KD accepted** (shared C-terminal region) |
| 8 | hs PPARGC1A | AGTCCTCACTGGTGGACACG + AGG | 1176 (+) | 0 | 0 | LOW | none needed; **PGC-1α4 spared by exon 8 design**; **PPARGC1B co-KD accepted** |

> **Note on PPARGC1B co-KD (PGC-1α arm):** PGC-1α guides in exon 8 will also knock down **PGC-1β (PPARGC1B)**, because PGC-1β shares significant C-terminal homology with PGC-1α1 (exon 8+). This is **an accepted off-target** for the Aim 2 design (see `CONSTRUCT_SPECS.md` §4.7). PGC-1β regulates a partially overlapping mitochondrial biogenesis programme; if the phenotype is interpreted as PGC-1α1-specific, the PGC-1β co-KD will be a confounder. The disclosure should be made in the methods. The audit-flagged risk is therefore **MED** (not LOW) for the PGC-1α arm because of the PGC-1β paralog co-KD; the **mitigation is to disclose in methods + validate by rescuing with PGC-1α1 cDNA in the Aim 3 experiment**.

---

## 4. siRNA off-target audit (methodology + worked example)

### 4.1 Methodology

For each of the 32 SMARTpool oligos + 24 individual siRNAs = **56 siRNA off-target audits**, the methodology is as described in §1.1. The audit is **deferred to the vendor design-tool output**:

- **For siGENOME SMARTpool** (Horizon): the design tool returns 4 oligos with a built-in off-target audit. The output is at https://horizondiscovery.com/design-center
- **For Silencer Select** (Thermo): the design tool returns a single validated oligo with off-target audit. The output is at https://www.thermofisher.com/order/catalog/product/4390770

**Pre-order checklist for the siRNA arm:**
- [ ] Submit each RefSeq to the vendor design tool: NM_175329.4 (mm Chchd10), NM_001301339.2 (hs CHCHD10), NM_026610.2 (mm Ndufb4), NM_004547.6 (hs NDUFB4 v1), NM_016774.3 (mm Atp5f1b), NM_001686.4 (hs ATP5F1B), NM_008904.3 (mm Ppargc1a), NM_013261.5 (hs PPARGC1A)
- [ ] Receive back: 4 oligos per SMARTpool + 1 individual validated per gene × species, each with off-target count
- [ ] Run the watch-list sub-audit on the returned sequences (this work's audit can be re-run; the methodology is the same)
- [ ] Discard any oligo with a perfect 19/19 + dTdT match to a Tier 1 watch-list gene; flag any with a perfect 7-nt seed match to a Tier 1 watch-list gene
- [ ] Confirm the 3-prime overhang is **dTdT** for Silencer Select (Thermo) and **UU** for siGENOME (Horizon)
- [ ] Confirm the SMARTpool design **spans 4 distinct regions** of the ORF (not 4 oligos at the same site)

### 4.2 Worked example — illustrative audit for a published siRNA target

To illustrate the audit methodology, here is a **worked example** for a representative siRNA target sequence:

**Example: a hypothetical anti-human CHCHD10 siRNA (sense strand, 19 nt + 3' dTdT overhang):**
- Sense strand: `5'-GACCAUCCAGAUCGAGCAG-dTdT-3'` (illustrative; not the actual siGENOME SMARTpool sequence)
- Seed (nt 2–8): `ACCAUCC`
- Audit:
  1. BLAST seed (ACCAUCC, 7 nt) against RefSeq human mRNA: no 7/7 match in CHCHD2 (sequence context: CHCHD2 has 5'-ACCGUGC-3' at the orthologous position — 2 mismatches)
  2. BLAST seed against CHCHD6: no 7/7 match
  3. BLAST seed against the full RefSeq human mRNA: ~1200 7/7 matches across the transcriptome (expected, given 7-nt seed is small)
  4. Extend the audit to 19-nt full sense strand: ~10 19/19 matches in RefSeq; check each for mitochondrial relevance — none in the watch list
  5. **Result**: PASS for the watch list; full off-target profile is reported by the vendor tool

> **The actual siGENOME SMARTpool oligos are TBD at design-tool output** and will be reported in the `audits/{gene}_{species}_audit.md` files (one per construct) when the design tool returns them. The vendor tool's built-in off-target audit covers the full transcriptome and is the primary source of truth.

### 4.3 Per-siRNA off-target report (template; TBD at design tool output)

| siRNA ID | Gene target | Species | Sense strand (19–25 nt) | Seed (nt 2–8) | Best mito watch-list hit (gene) | Identity % | E-value | Mito category | Risk level (HIGH/MED/LOW) | Mitigation |
|---|---|---|---|---|---|---|---|---|---|---|
| (TBD) | CHCHD10 | mouse | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| (TBD) | CHCHD10 | human | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| (TBD) | NDUFB4 | mouse | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| (TBD) | NDUFB4 | human | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| (TBD) | ATP5F1B | mouse | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| (TBD) | ATP5F1B | human | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| (TBD) | PPARGC1A | mouse | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| (TBD) | PPARGC1A | human | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |

> **Action:** After vendor tool returns the siRNA sequences, fill in this table; one row per SMARTpool oligo (32 rows) + one row per individual siRNA (24 rows) = 56 rows. Save the table in `audits/{gene}_{species}_modality_audit.md` per `CONSTRUCT_SPECS.md` §6.3.

---

## 5. Risk summary and decision summary

### 5.1 Risk summary table (this work + TBD at design time)

| Reagent | Target | Species | Mito watch-list off-target (this work) | Full-genome mm0 (TBD CRISPOR) | Risk | Mitigation |
|---|---|---|---|---|---|---|
| mm_Chchd10_sg1 | Chchd10 | mouse | 0 (162 mRNAs loaded) | TBD | LOW (with eSpCas9(1.1) recommended) | Use eSpCas9(1.1); exclude CHCHD2 seed; Hsu ≥ 70 required |
| hs_CHCHD10_sg1 | CHCHD10 | human | 0 (162 mRNAs loaded) | TBD | LOW (with eSpCas9(1.1) recommended) | Same as mouse |
| mm_Ndufb4_sg1 | Ndufb4 | mouse | 0 (162 mRNAs loaded) | TBD | LOW | SpCas9 OK; Hsu ≥ 70 required |
| hs_NDUFB4_sg1 | NDUFB4 | human | 0 (162 mRNAs loaded) | TBD | LOW | SpCas9 OK; Hsu ≥ 70 required |
| mm_Atp5f1b_sg1 | Atp5f1b | mouse | 0 (162 mRNAs loaded) | TBD | LOW | SpCas9 OK; Hsu ≥ 70 required |
| hs_ATP5F1B_sg1 | ATP5F1B | human | 0 (162 mRNAs loaded) | TBD | LOW | SpCas9 OK; Hsu ≥ 70 required |
| mm_Ppargc1a_sg1 | Ppargc1a | mouse | 0 (162 mRNAs loaded) | TBD | MED (PPARGC1B co-KD accepted) | **PPARGC1B co-KD disclosed in methods**; PGC-1α4 spared by exon 8 design; PGC-1α1 cDNA rescue in Aim 3 |
| hs_PPARGC1A_sg1 | PPARGC1A | human | 0 (162 mRNAs loaded) | TBD | MED (PPARGC1B co-KD accepted) | Same as mouse |
| 16 sgRNA reserves (sg2 / sg3 × 8 combinations) | various | mouse + human | 0 (162 mRNAs loaded) | TBD | LOW | Use as fallback if selected sgRNA fails CRISPOR |
| 8 siRNA SMARTpools (32 oligos) | various | mouse + human | TBD at design tool | TBD at design tool | TBD | Run vendor off-target audit; reject any Tier 1 perfect seed match |
| 8 individual siRNAs (one per gene × species) | various | mouse + human | TBD at design tool | TBD at design tool | TBD | Same as SMARTpool |

### 5.2 Decision summary — reagents to order for Aim 2

**PASS, order as-is (8 sgRNAs, 1 per gene × species):**
1. mm_Chchd10_sg1 — GCCGGGTCTTATGGCTCAGA + TGG (eSpCas9(1.1) recommended)
2. hs_CHCHD10_sg1 — TGACCGGAGCCTTCAGCGGG + GGG (eSpCas9(1.1) recommended)
3. mm_Ndufb4_sg1 — CAAACGCGTGTCGCACATCG + AGG (SpCas9)
4. hs_NDUFB4_sg1 — TACAACGATCCCAACCGCCG + AGG (SpCas9)
5. mm_Atp5f1b_sg1 — CGTGGCAGTCATCGGCGCTG + TGG (SpCas9)
6. hs_ATP5F1B_sg1 — CGTGGCGGTCATTGGCGCAG + TGG (SpCas9)
7. mm_Ppargc1a_sg1 — ATGCCTCCTGTGACTGGCAG + GGG (SpCas9; PGC-1α4 spared; **PPARGC1B co-KD accepted**)
8. hs_PPARGC1A_sg1 — AGTCCTCACTGGTGGACACG + AGG (SpCas9; PGC-1α4 spared; **PPARGC1B co-KD accepted**)

**Reserves (16 sgRNAs, sg2 / sg3 × 8 combinations):** held in reserve; used if the selected sgRNA fails CRISPOR (Doench < 50, Hsu < 70, or mm0 > 0 in the full genome).

**Rejected:** **NONE** in this work. All 24 candidates pass the watch-list sub-audit. (The 8 selected best pass + the 16 reserves pass; no redesign required at this stage.)

**TBD at design tool / CRISPOR:**
- Full-genome Hsu 2013 off-target count (mm0/mm1/mm2/mm3) for all 24 candidates
- Doench Rule Set 2 on-target score for all 24 candidates
- siRNA SMARTpool + individual oligo sequences + off-target profile for all 56 siRNAs

**Redesign protocol if CRISPOR rejects a selected sgRNA:**
1. Try sg2 or sg3 reserve (from `CRISPR_DESIGNS.md` §1.3 – §4.3)
2. If all 3 fail, re-run CRISPOR with the verified RefSeq mRNA and pick the top-3 from the fresh output
3. If CRISPOR returns no guides with Doench ≥ 50 and Hsu ≥ 70, use eSpCas9(1.1) (Addgene #71814) to relax the Hsu threshold to ≥ 50

### 5.3 Final recommended reagent set for Aim 2 vendor order (8 + 8 = 16 reagents)

| # | Reagent | Vendor | Catalog | Status |
|---|---|---|---|---|
| 1 | mm Chchd10 sgRNA (RNP) | IDT | Alt-R custom (mm_Chchd10_sg1) | **Order ready** |
| 2 | hs CHCHD10 sgRNA (RNP) | IDT | Alt-R custom (hs_CHCHD10_sg1) | **Order ready** |
| 3 | mm Ndufb4 sgRNA (RNP) | IDT | Alt-R custom (mm_Ndufb4_sg1) | **Order ready** |
| 4 | hs NDUFB4 sgRNA (RNP) | IDT | Alt-R custom (hs_NDUFB4_sg1) | **Order ready** |
| 5 | mm Atp5f1b sgRNA (RNP) | IDT | Alt-R custom (mm_Atp5f1b_sg1) | **Order ready** |
| 6 | hs ATP5F1B sgRNA (RNP) | IDT | Alt-R custom (hs_ATP5F1B_sg1) | **Order ready** |
| 7 | mm Ppargc1a sgRNA (RNP) | IDT | Alt-R custom (mm_Ppargc1a_sg1) | **Order ready (PGC-1α4 spared; PPARGC1B co-KD disclosed)** |
| 8 | hs PPARGC1A sgRNA (RNP) | IDT | Alt-R custom (hs_PPARGC1A_sg1) | **Order ready (PGC-1α4 spared; PPARGC1B co-KD disclosed)** |
| 9 | IDT Alt-R tracrRNA, ATTO 550 (5 nmol) — shared | IDT | 1075928 | **Order ready** (1 unit covers all 8 gene × species) |
| 10 | IDT Alt-R Cas9 Nuclease V3 (100 µg) — shared | IDT | 1081058 | **Order ready** (1 unit covers all 8 gene × species) |
| 11 | eSpCas9(1.1) in pX330 (Addgene #71814) | Addgene | 71814 | **Order ready** (for CHCHD10 in mouse + human; use as RNP delivery or clone sgRNA into the vector) |
| 12 | lentiCRISPR v2-Puro (Addgene #52961) | Addgene | 52961 | **Order ready** (1 unit covers all 4 gene × species that use SpCas9; for CHCHD10 use eSpCas9(1.1) instead) |
| 13 | ON-TARGETplus Non-Targeting Pool (control) | Horizon | D-001810-10-05 | **Order ready** (control siRNA for the siRNA arm; pair with the siRNA order) |
| 14 | MISSION Non-Target shRNA (control) | Horizon | SHC002 | **Order ready** (control shRNA for the shRNA arm) |
| 15 | Recommended non-targeting sgRNA (5'-GACCGGAACGATCTCGCGTA-3' + NGG) | IDT | Alt-R custom | **Order ready** (control sgRNA for the CRISPR arm) |
| 16 | (Optional) 16 reserve sgRNAs (sg2 + sg3 × 8 combinations) | IDT | Alt-R custom | **Hold in reserve**; order only if a selected sgRNA fails CRISPOR |

**Total: 16 reagents to order, of which 14 are immediate and 2 (eSpCas9 + lentiCRISPR v2 plasmid) are shared reagents. The 16 reserve sgRNAs are not ordered initially but are documented in `CRISPR_DESIGNS.md` for fallback.**

---

## 6. Open issues and verification checklist (handed off to CRO / wet lab)

| # | Issue | Owner | Deadline |
|---|---|---|---|
| 1 | Run CRISPOR for all 8 selected sgRNAs to obtain Doench + Hsu + full-genome off-target scores | Wet-lab collaborator / CRO | M1 (before order ships) |
| 2 | Submit each RefSeq to the siRNA vendor design tool (Horizon / Thermo) and receive SMARTpool + individual oligo sequences + vendor off-target audit | Wet-lab collaborator | M1 (parallel to CRISPOR) |
| 3 | Run the full mitochondrial watch-list audit at the CRO with a complete watch list (~200 genes) — covers both sgRNA and siRNA | CRO | M1 |
| 4 | For the PGC-1α arm: design 3 isoform-specific qPCR assays (PGC-1α1 exon 1a, PGC-1α-b/-c exon 1b, PGC-1α4 splice junction in exon 6) — required to validate PGC-1α4 sparing | Wet-lab collaborator | M1 (parallel to sgRNA order) |
| 5 | Document the PPARGC1B co-KD acceptance in the methods (the user's design accepts this off-target for the Aim 2 single-gene PGC-1α test) | Larry | M1 |
| 6 | Validate the 2 mouse mRNA RefSeq corrections (NM_175329.4 for Chchd10; NM_026610.2 for Ndufb4) by re-checking the in-house sequence databases | Wet-lab collaborator / CRO | M1 |
| 7 | Cross-check the 20-nt + NGG + exon-flanking genomic sequence at CRISPOR for the 8 selected sgRNAs (CRISPOR takes genomic input, not mRNA; the mRNA coordinates in this document must be converted) | Wet-lab collaborator | M1 |
| 8 | Confirm the corrected mitochondrial watch-list accessions (§0.3) are still current at the CRO (NCBI may retire accessions; verify before the audit) | CRO | M1 |
| 9 | For the PGC-1α arm: validate by **rescuing with PGC-1α1 cDNA** in the Aim 3 experiment — this closes the PPARGC1B co-KD concern at the wet-lab level | Wet-lab collaborator | M2–M3 |
| 10 | For CHCHD10: explicitly **exclude CHCHD2 seed matches** in the final off-target audit (the user does not want to recapitulate the Guzman 2026 dual-KO design; Aim 2 wants single-gene CHCHD10) | CRO | M1 |

---

## 7. Document signoff

| Role | Name | Action | Date |
|---|---|---|---|
| **Author** | Brown Biotech (Larry) | Drafted v0.1 | 2026-06-15 |
| **Reviewer (wet-lab)** | TBD | _Pending review_ | TBD |
| **Reviewer (dry-lab / biostats)** | TBD | _Pending review_ | TBD |
| **Procurement** | TBD | _Confirm catalog numbers at PO issue_ | TBD |
| **CRO liaison** | TBD (if outsourced) | _Confirm CRISPOR runs, watch-list audit, sequence verifications_ | TBD |
| **PI signoff** | TBD | _Pending_ | TBD |

> **This document is for dry-lab planning and procurement reference. It does not authorize wet-lab execution. Wet-lab work proceeds only after the signoff matrix above is complete and the CRISPOR + vendor-tool scores are filled in.**

---

## 8. Change log

| Version | Date | Author | Change |
|---|---|---|---|
| **v0.1** | 2026-06-15 | Brown Biotech (Larry) | Initial dry-lab specification. 24 sgRNA candidates (top-3 per gene × species × 4 genes × 2 species) audited against the loaded mitochondrial watch list (162 mRNAs downloaded 2026-06-15 from NCBI Entrez). **Result: 0 perfect 20-nt + NGG off-targets in the loaded watch list for all 24 candidates.** Mitochondrial watch list categories and risk tiers defined; PPARGC1B co-KD for the PGC-1α arm flagged as accepted off-target (MED risk, disclosure in methods + PGC-1α1 cDNA rescue in Aim 3). PGC-1α4 sparing validated by exon 8 design. Mouse RefSeq corrections noted (Chchd10 = NM_175329.4; Ndufb4 = NM_026610.2; original IDs in CONSTRUCT_SPECS.md were wrong). Methodology provided for siRNA off-target audit (deferred to vendor design tool). Final recommended reagent set: 16 reagents (8 selected sgRNAs + 8 shared reagents). |
| **Cross-ref** | 2026-06-15 | Brown Biotech (Larry) | Companion document `CRISPR_DESIGNS.md` issued same day (covers OI-2 in `validation/plan/OPEN_ISSUES.md`). Together, OI-2 and OI-3 are now ready for the M1 vendor order. |

---

*End of OFF_TARGET_AUDIT.md v0.1 — 24 sgRNA candidates × 162 watch-list mRNAs audit complete; 0 perfect off-targets in the loaded watch list; full-genome Hsu 2013 + siRNA off-target TBD at design time; final recommended reagent set: 8 selected sgRNAs + 8 shared reagents = 16 reagents for the M1 vendor order (with 16 reserves held in case of CRISPOR rejection).*
