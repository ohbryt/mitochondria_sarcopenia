# HMSR Sarcopenia — Wet Validation Bundle v0.4

> **This folder is a self-contained, flat-format bundle** of all the wet-validation
> program documents for the HMSR (Human skeletal Muscle Sarcopenia multiomic
> Resource) project. It contains everything needed to understand, review, and
> execute the validation program — without needing to navigate the original
> `validation/`, `manuscripts/`, or `submission/` directory structures.
>
> **Built:** 2026-06-16
> **Source HEAD:** `9e3601b` on branch `sarcopenia/paper1-v0.4` (main worktree)
> **Built by:** Brown Biotech (Larry)
> **License for code:** MIT (full text at `sarcopenia-multiomic-resource/LICENSE`)

---

## 1. Quick navigation

| # | File | Lines | What it is | Authoritative or historical? |
|---|---|---|---|---|
| **00** | `00_HYPOTHESIS.md` | 289 | The central thesis + 7 sub-hypotheses (H0, H0.5, H1.1–H1.4, H2, H3) with explicit falsification clauses for each | **Authoritative** (v0.1) |
| **01** | `01_WET_VALIDATION_PLAN.md` | 1,217 | The self-contained wet validation plan v0.4 — 14 sections covering hypothesis, in vitro Aims 1-4, in vivo Exp A-D, decision gates, statistics, timeline, budget, risks, publication strategy | **Authoritative** (v0.4) — supersedes v0.2 + v0.3 |
| **02** | `02_CONSTRUCT_SPECS.md` | 831 | siRNA / shRNA / CRISPR construct design for 4 genes × 2 species (with vendor catalog mapping) | **Authoritative** (v0.1) — has 2 known RefSeq errors corrected in #03 |
| **03** | `03_CRISPR_DESIGNS.md` | 593 | Top-3 sgRNAs per gene × species (24 total) extracted from verified NCBI RefSeq mRNAs (2026-06-15) | **Authoritative** (v0.1) — includes **RefSeq corrections** to #02 |
| **04** | `04_OFF_TARGET_AUDIT.md` | 429 | BLAST off-target audit — 24 sgRNAs × 162-mRNA mitochondrial watch list — all 24 PASS (0 perfect 20-nt + NGG off-targets) | **Authoritative** (v0.1) |
| **05** | `05_ANTIBODY_PANEL.md` | 721 | 41-Ab tier-aligned mitochondrial program panel + non-mito specificity controls | **Authoritative** (v0.1) |
| **06** | `06_SEAHORSE_MITO_STRESS_TEST_SOP.md` | 802 | Seahorse XF Mito Stress Test SOP for C2C12 + HSMM (real Agilent catalog numbers) | **Authoritative** (v1.0) |
| **07** | `07_MYOBUNDLE_SPECIFIC_FORCE_SOP.md` | 807 | 3D myobundle + 2D single-myotube specific force SOP with matched-CSA design | **Authoritative** (v1.0) |
| **08** | `08_POWER_ANALYSIS.md` | 443 | Per-experiment n + effect-size update from Guzman 2026 + 16 primary papers (2011–2026) | **Authoritative** (v0.3) |
| **09** | `09_VENDOR_SHORTLIST.md` | 1,135 | RFP-ready vendor / CRO shortlist with 2025-2026 pricing + 5 ready-to-send RFP email templates | **Authoritative** (v0.1) |
| **10** | `10_PLAN_V0.3_OPS.md` | 356 | Plan v0.3 — the operationalized spec (5,263 lines when including all original sub-deliverables) | **Historical** — superseded by #01 |
| **11** | `11_OPEN_ISSUES.md` | 135 | Open issues + TBD tracking (12 issues tagged, 2 resolved, 1 blocking) | **Active** — cross-reference for current state |
| **12** | `12_README_ORIENTATION.md` | 42 | Original `validation/README.md` — project orientation + tier ranking | **Authoritative** for project context |
| **13** | `13_PAPER1_V0.4_DISCOVERY.md` | 518 | The discovery paper (HMSR v0.4) — the H0 foundation | **Authoritative** (v0.4) |
| **14** | `14_PLAN_V0.2_DESIGN_HISTORY.md` | 172 | Plan v0.2 — the design (precedes v0.3 ops + v0.4 consolidated) | **Historical** — superseded |

**Total: 8,490 lines / ~745 KB / 15 files**

---

## 2. Recommended reading order

1. **`00_HYPOTHESIS.md`** (15 min skim) — the central thesis + 7 sub-hypotheses
2. **`01_WET_VALIDATION_PLAN.md`** (30 min read) — the full wet program
3. **`13_PAPER1_V0.4_DISCOVERY.md`** (60 min read) — the discovery
4. Then the operational specs as needed:
   - For construct/sgRNA design: #02, #03, #04
   - For Ab panel: #05
   - For wet-lab execution: #06, #07
   - For power/budget: #08
   - For vendor sourcing: #09
5. **`11_OPEN_ISSUES.md`** — current state of TBDs

---

## 3. The hypothesis in one paragraph

**H0 (established, v0.4):** In sarcopenic human skeletal muscle, the
nuclear-encoded mitochondrial biogenesis programme (mitoribosome, cristae/MICOS,
import, respiratory chain) is coordinately and specifically down-regulated at
the transcript level (permutation p=2.0×10⁻³, robust to 3 confound controls).

**H1 (causation, to be tested in Aim 2):** Suppressing the programme — or
its strongest nodes — lowers mitochondrial respiration and **specific force
(force per CSA) at matched CSA** without lowering muscle mass. This is the
**muscle-quality signature** of the programme.

**H2 (exercise reversibility, Exp C):** Training rescues the programme +
specific force in aged mice.

**H3 (therapeutic, Exp D):** Restoring the programme (PGC-1α induction or
15-PGDH inhibition, the latter anchored to Palla 2020 *Science* PMID 33303683)
delivers function beyond an anabolic-only comparator at equal mass gain.

Each sub-hypothesis has a pre-specified **falsification clause** in
`00_HYPOTHESIS.md` §9.

---

## 4. The wet program in 30 seconds

- **In vitro** (Aims 1-4): cohort IHC, C2C12+HSMM siRNA/shRNA/CRISPR,
  PGC-1α1 rescue, CLTB
- **In vivo** (Exp A-D): aged C57BL/6J phenotype, AAV9-shRNA in TA,
  exercise reversibility, mass-matched therapeutic
- **4 decision gates** dictate progression (Aim 1 protein → Aim 2 in-vitro
  function → Exp B in-vivo quality → Exp D therapeutic)
- **Sample sizes:** n=11 (Exp B conservative, 20% Δ; or n=14 if 15% Δ);
  n=24/group (Exp D 4-arm); n=3-5 difs for in-vitro
- **Timeline:** 14 months (M0-M14) for all 4 in-vivo experiments
- **Budget:** $220-293K (full); $80-95K (minimum-viable: Aim 2 PoC + Exp B
  n=11)
- **3-paper output:** Paper 1 (HMSR discovery, ready) → Paper 2
  (JCSM/Aging Cell, M11-M14) → Paper 3 (Nature Aging/Cell Metabolism,
  M14-M16)

---

## 5. v0.4 corrections (vs the v0.2 design + v0.3 ops)

The v0.4 plan incorporates **all 10 corrections** from the v0.2 → v0.4
review. Briefly:

1. **Guzman 2026 (PMID 41496579)** specific force: 20% (not 15%) — abstract
   reports qualitative only; full PDF pending
2. **PGC-1α muscle-KO citation:** Handschin 2007 PMID 17702743 (not Ruas
   2012 PMID 22977227 — that's a lipid genetics paper)
3. **Exp B n=14** (not 10) — for 0.90 power given realistic AAV9 + in-vivo
   force SD ≈ 12%
4. **Addgene non-targeting:** #50946 (not #80263) — verified Yusa 2014
5. **Vector Biolabs Ad-PGC-1α:** ADV-280991 (mouse) / ADV-219511 (human)
   (not #1047) — current catalog
6. **Mouse Chchd10 RefSeq:** NM_175329.4 (was NM_001136064.2, which is
   actually mouse *Bscl2*) — verified 2026-06-15
7. **Mouse Ndufb4 RefSeq:** NM_026610.2 (was NM_026610.3, retired by NCBI)
8. **PGC-1α sgRNA target:** exon 8-13 of PGC-1α1 (spares PGC-1α4, the
   266-aa truncated isoform with premature stop in exon 6)
9. **Budget:** $220-293K itemised (not $120-160K — v0.2 omitted personnel)
10. **Seahorse Δ:** 22-25% (not 15%) — defensible from Guzman 2026 +
    Halling 2019 + Palla 2020

**Bonus correction (PubMed-verified 2026-06-16):** Hsu 2013 sgRNA
off-target paper: **PMID 23873081** (not 23775266 — that's the
unrelated "Mormile celiac disease" letter).

---

## 6. Open issues + next steps

See `11_OPEN_ISSUES.md` for the full list. The 1 blocking issue is:

- **OI-1:** Guzman 2026 specific-force number — request full PDF from
  Aguilar lab (U. Michigan) to verify the 15% / 20% assumption

The 4 important open issues are administrative/vendor decisions that
block the M0-M1 critical-path orders:

- **OI-4:** AAV9 in-house vs CRO (need quotes from VectorBuilder, Penn
  Vector Core, UNC)
- **OI-5:** iPSC model (bit.bio recommended; CDI backup)
- **OI-6:** Author list / affiliations / repo URL / ORCID (Larry's input)
- **OI-7:** Lonza MTA for HSMM sarcopenic donor (4-6 wk lead time)

**Next-step recommendation:** address OI-1 + OI-4 + OI-5 + OI-6 + OI-7 in
M1 (parallel) — these are the wet-lab-execution + administrative
prerequisites.

---

## 7. License and citation

- **License:** MIT (full text at `sarcopenia-multiomic-resource/LICENSE`)
- **Repository:** `https://github.com/ohbryt/mitochondria_sarcopenia` (release
  tag `v0.4-paper1`; DOI auto-mints via Zenodo on release)
- **Citation metadata:** `sarcopenia-multiomic-resource/CITATION.cff`
- **Paper 1 (v0.4)** is submitted to GeroScience / npj Aging / JCSM (JCR 5-10%)

---

*End of bundle README. 15 files / 8,490 lines / ~745 KB. Branch:
`sarcopenia/paper1-v0.4`. Not pushed; ready for internal review, grant
appendix, or CRO RFP handoff.*
