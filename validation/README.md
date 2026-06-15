# HMSR Aim 2 Validation — Operationalization

> **Branch:** `validation/aim2-causation` (worktree: `.worktrees/validation-aim2/`)
> **Source plan:** `sarcopenia-multiomic-resource/manuscripts/experimental_validation_plan_v0.2.md`
> **Goal:** Convert the v0.2 plan (in-vitro Aim 2 — C2C12 + HSMM siRNA → Seahorse + force at matched CSA) into wet-lab-executable specifications: construct designs, antibody panels, SOPs, power analysis, vendor shortlist, and an updated v0.3 plan with concrete IDs and cost line items.

## Why Aim 2 first
Aim 2 is the **causation arm** of the HMSR v0.4 finding ("the entire mitochondrial
biogenesis programme is coordinately down-regulated in sarcopenic muscle"). It is:

- The **single experiment that can move the v0.4 paper from JCR 5–10% to top-tier** —
  by establishing that suppressing the programme (or its strongest nodes) reduces
  mitochondrial respiration and **specific force at matched CSA**, the muscle-quality
  pillar of the companion Perspective is tested directly.
- The **fastest in-vitro arm** (6-month PoC; C2C12 myotubes + commercially validated
  siRNA, no colony, no AAV, no aged mice).
- The **cleanest decision gate**: a Tier-1/2 knockdown that drops OCR ≥20% at matched
  CSA = quality driver; if force only falls in proportion to diameter loss, the gene
  acts via mass, not quality.

## Tier ranking (from v0.4 stats)
| Tier | Gene | β (RE meta) | p (meta) | FDR (BH) | I² | Function |
|---|---|---|---|---|---|---|
| 1 | **CHCHD10** | −0.164 | 7.5×10⁻⁶ | 0.255 | 0% | MICOS / cristae (IMS) |
| 2 | **NDUFB4** | −0.190 | 3.1×10⁻³ | 0.534 | 47% | Complex I accessory |
| 2 | **ATP5F1B** | −0.221 | 3.5×10⁻³ | 0.544 | 39% | Complex V (ATP synthase) F₁β |
| master | **PPARGC1A** (PGC-1α) | — | — | — | — | Biogenesis master switch |

## Directory layout
| Subdir | Contents |
|---|---|
| `constructs/` | siRNA, shRNA, CRISPR gRNA sequences (mouse + human); vendor-mapped where possible (siGENOME, Edit-R, GeneCopoeia, IDT, Twist) |
| `antibodies/` | Mitochondrial program protein panel — WB primary Abs + IHC; vendor, catalog #, RRID, validation status for C2C12/HSMM |
| `protocols/` | SOPs: Seahorse Mito Stress Test, single-fibre/myobundle specific force at matched CSA, AAV9-shRNA (Exp B), iPSC-CRISPR (Aim 3) |
| `power_analysis/` | Effect-size update from Guzman 2026 + current literature; per-experiment n with 0.80 power at α=0.05; SD rationale |
| `vendors/` | Cell line sourcing (C2C12 ATCC, HSMM Lonza/Cambrex, iPSC-derived myocyte CROs), reagents, kits, instruments, CRO shortlist |
| `plan/` | `experimental_validation_plan_v0.3.md` — operationalized v0.2 with construct IDs, vendor, cost line items |

## Linked papers
- **Paper 1 (current, v0.4):** HMSR mitochondrial-programme resource — GeroScience/npj Aging/JCSM (JCR 5–10%)
- **Paper 2:** In-vitro causation (Aims 1–3) — JCSM / Aging Cell
- **Paper 3:** In-vivo quality + therapeutic (Exp B+D), muscle-quality framing — Nature Aging / Cell Metabolism (top-5%)
