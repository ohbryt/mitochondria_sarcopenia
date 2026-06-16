#!/usr/bin/env python3
"""
Build the HMSR sarcopenia Paper 1 submission bundle.

Mirrors the established submission/v0.4 convention (manuscript + figures +
supplementary + manifest.tsv with SHA256 + README provenance), but for the
HMSR mitochondrial-sarcopenia manuscript (distinct from the Eda2r/Hjv paper).

Usage:  python3 scripts/build_submission_package.py
Output: submission/v0.4/  (under sarcopenia-multiomic-resource)
"""
from __future__ import annotations

import hashlib
import shutil
import subprocess
from pathlib import Path

BASE = Path("/Volumes/4TB/exerciseomics/sarcopenia-multiomic-resource")
OUT = BASE / "submission" / "v0.4"
GEN_DATE = "2026-06-13"  # passed explicitly; no Date.now in builds


def sha256(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def git_head() -> str:
    try:
        return subprocess.check_output(
            ["git", "-C", str(BASE), "rev-parse", "HEAD"], text=True
        ).strip()
    except Exception:
        return "unknown"


# (source_path, dest_relative_path)
MANUSCRIPT = (BASE / "manuscripts" / "paper1_v0.4.md", "paper1_sarcopenia_v0.4.md")

FIGURES = [
    (BASE / "output/figures/Fig1_study_overview.png", "figures/Fig1_study_overview.png"),
    (BASE / "output/figures/Fig2_forest_plots.png", "figures/Fig2_forest_plots.png"),
    (BASE / "output/figures/Fig3_volcano_meta.png", "figures/Fig3_volcano_meta.png"),
    (BASE / "output/figures/Fig4_heatmap_top50.png", "figures/Fig4_heatmap_top50.png"),
    (BASE / "output/figures/Fig5_pathway_enrichment.png", "figures/Fig5_pathway_enrichment.png"),
    (BASE / "output/figures/Fig1_study_overview.pdf", "figures/Fig1_study_overview.pdf"),
    (BASE / "output/figures/Fig2_forest_plots.pdf", "figures/Fig2_forest_plots.pdf"),
    (BASE / "output/figures/Fig3_volcano_meta.pdf", "figures/Fig3_volcano_meta.pdf"),
    (BASE / "output/figures/Fig4_heatmap_top50.pdf", "figures/Fig4_heatmap_top50.pdf"),
    (BASE / "output/figures/Fig5_pathway_enrichment.pdf", "figures/Fig5_pathway_enrichment.pdf"),
]

SUPPLEMENTARY = [
    (BASE / "output/manuscript_tables/Table1_cohort_characteristics.tsv", "supplementary/Table1_cohort_characteristics.tsv"),
    (BASE / "output/manuscript_tables/Table2_top20_gate_pass.tsv", "supplementary/Table2_top20_gate_pass.tsv"),
    (BASE / "output/manuscript_tables/Table3_mito_candidates.tsv", "supplementary/Table3_mito_candidates.tsv"),
    (BASE / "output/manuscript_tables/TableS1_all195_gate_pass.tsv", "supplementary/TableS1_all195_gate_pass.tsv"),
    (BASE / "output/signatures/wp3b_confound_sensitivity.tsv", "supplementary/TableS3_confound_sensitivity.tsv"),
    (BASE / "output/signatures/wp3b_mito_enrichment_adjusted.tsv", "supplementary/TableS4_mito_enrichment_adjusted.tsv"),
    (BASE / "output/signatures/wp3c_permutation.tsv", "supplementary/TableS5_permutation_enrichment.tsv"),
    (BASE / "output/signatures/wp3c_pathway_enrichment.tsv", "supplementary/TableS5b_descriptive_enrichment.tsv"),
    (BASE / "output/signatures/wp6_therapeutic_axis.tsv", "supplementary/TableS6_therapeutic_axis.tsv"),
    (BASE / "output/signatures/wp3d_freedman_lane.tsv", "supplementary/TableS7_freedman_lane.tsv"),
    (BASE / "output/signatures/wp3e_libsize_sensitivity.tsv", "supplementary/TableS8_libsize_sensitivity.tsv"),
    (BASE / "manuscripts/CODEX_REVIEW_v0.3.md", "supplementary/codex_adversarial_review_v0.3.md"),
    (BASE / "manuscripts/experimental_validation_plan_v0.1.md", "supplementary/experimental_validation_plan_v0.1.md"),
    (BASE / "manuscripts/experimental_validation_plan_v0.2.md", "supplementary/experimental_validation_plan_v0.2.md"),
    (BASE / "validation/plan/experimental_validation_plan_v0.3.md", "supplementary/experimental_validation_plan_v0.3.md"),
    (BASE / "validation/plan/OPEN_ISSUES.md", "supplementary/validation_open_issues.md"),
    (BASE / "validation/constructs/CRISPR_DESIGNS.md", "supplementary/crispr_designs.md"),
    (BASE / "validation/constructs/OFF_TARGET_AUDIT.md", "supplementary/off_target_audit.md"),
    (BASE / "validation/HYPOTHESIS.md", "supplementary/hypothesis.md"),
    (BASE / "validation/WET_VALIDATION_PLAN.md", "supplementary/wet_validation_plan.md"),
    (BASE / "manuscripts/CRITICAL_REVIEW_v0.1.md", "supplementary/internal_critical_review_v0.1.md"),
    (BASE / "manuscripts/CRITICAL_REVIEW_v0.2.md", "supplementary/internal_critical_review_v0.2.md"),
    (BASE / "results/modality_detected.csv", "supplementary/modality_detected.csv"),
    (BASE / "results/dataset_audit.csv", "supplementary/dataset_audit.csv"),
]


def verify_status() -> str:
    try:
        r = subprocess.run(["python3", str(BASE / "scripts" / "verify.py")],
                           capture_output=True, text=True, cwd=BASE)
        last = [l for l in r.stdout.splitlines() if "PASS:" in l or "STATUS=" in l]
        return " | ".join(last) if last else "verify.py output unavailable"
    except Exception as e:
        return f"verify.py not run: {e}"


def gen_reproducibility_receipt(head: str) -> str:
    code = [
        ("pipeline/recompute_disease_signatures.py", "WP3 DE + DL random-effects meta + gate"),
        ("pipeline/split_regulatory_exercise_evidence.py", "WP5 evidence split"),
        ("scripts/confound_sensitivity.py", "WP3b composition + genomic-control sensitivity"),
        ("scripts/pathway_permutation.py", "WP3c correlation-aware label-permutation gene-set test"),
        ("scripts/pathway_enrichment.py", "WP3c descriptive AUC effect sizes"),
        ("scripts/sensitivity_freedman_libsize.py", "WP3d Freedman-Lane + WP3e library-size sensitivities"),
        ("scripts/make_manuscript_figures.py", "Figures 1-5 + Tables 1-3"),
        ("scripts/verify.py", "Terminal verifier gate"),
    ]
    lines = [
        "# HMSR Sarcopenia Paper 1 — Reproducibility Receipt",
        "",
        f"**Generated:** {GEN_DATE}",
        f"**Source repository HEAD:** `{head}`",
        f"**Verifier:** {verify_status()}",
        "**Environment:** `environment.yml` / `environment.lock.yml` (Python 3.14.4; numpy 1.26.4, pandas 2.3.3, scipy 1.17.1, statsmodels 0.14.6, scikit-learn 1.8.0)",
        "",
        "## Code → claim map",
        "",
        "| Script | SHA256 (16) | Role |",
        "|---|---|---|",
    ]
    for rel, role in code:
        p = BASE / rel
        h = sha256(p)[:16] if p.exists() else "MISSING"
        lines.append(f"| `{rel}` | `{h}` | {role} |")
    lines += [
        "",
        "## Re-run (one path)",
        "",
        "```bash",
        "conda env create -f environment.yml && conda activate hmsr-sarcopenia",
        "python3 pipeline/recompute_disease_signatures.py     # WP3 + gate",
        "python3 pipeline/split_regulatory_exercise_evidence.py  # WP5",
        "python3 scripts/confound_sensitivity.py              # WP3b sensitivity",
        "python3 scripts/make_manuscript_figures.py           # figures + tables",
        "python3 scripts/verify.py                            # terminal gate (expect STATUS=PASS)",
        "```",
        "",
        "## Large regenerable inputs (not bundled; hashes in data/CHECKSUMS.txt)",
        "- `output/signatures/replication_matrix.tsv` (37,469-gene DL meta matrix; Supplementary Table S2)",
        "- `output/signatures/differential_by_cohort.tsv` (per-cohort OLS DE)",
        "",
        "All reported numbers are produced by the committed scripts above; none are hand-computed.",
    ]
    return "\n".join(lines) + "\n"


COVER_LETTER = """# Cover Letter

*Journal-agnostic template — substitute the target journal/editor, confirm the
scope statement, and sign/date before submission.*

To the Editorial Office,

We submit our manuscript, "A reproducible skeletal-muscle resource reveals
coordinated down-regulation of mitochondrial genes in sarcopenia," for
consideration as a resource/discovery study.

Sarcopenia lacks a consensus molecular signature. We assemble a reproducible
transcriptomic meta-analysis across two independent human studies (four sample
sets; the Hertfordshire/Jamaica/Singapore Sarcopenia Study family + an independent
cohort, GSE226151) using cohort-stratified differential
expression and DerSimonian-Laird random-effects meta-analysis over 37,469 genes.
We report transparently that **no gene survives genome-wide FDR**, and we treat
downstream gene lists as exploratory candidates from a clearly-disclosed post-hoc
gate. The defensible, novel contribution is a **pathway-level finding**:
coordinated down-regulation of the mitochondrial gene programme (mitoribosome,
cristae/MICOS, and respiratory-chain genes), which we show is **robust to
muscle-composition (stromal/immune purity) adjustment**, to **Freedman–Lane
covariate-exchangeable permutation**, and to **library-size (sequencing-depth)
covariate adjustment** — all of which argue against a simple fiber-loss artifact.
We pair the resource with a concrete in vitro/in vivo validation plan for the
prioritised candidates (see Supplementary experimental_validation_plan_v0.2 and
its operationalized v0.3 plan).

We believe this combination — methodological rigor, honest reporting of an FDR
null, a confound-tested pathway signal, and a forward validation plan — is well
suited to your readership in muscle physiology and aging biology.

The work is original, not under consideration elsewhere, and all authors approve
the submission. The author declares no competing interests. Brown Biotech (the
author's affiliation) had no role in study design, data analysis, interpretation,
or the decision to submit the work for publication.

**Suggested reviewers (3–5):** [TBD — Larry to provide 3–5 names with brief
rationale: e.g., 1–2 sarcopenia clinical researchers with EWGSOP experience; 1–2
muscle mitochondrial biologists; 1–2 biostatisticians with random-effects
meta-analysis experience.]

**Excluded reviewers:** [TBD — Larry to declare any conflicts (collaborators,
co-PIs, recent co-authors).]

Sincerely,

**Larry Oh**, on behalf of the author
Brown Biotech, Seoul, South Korea
`ohbryt@gmail.com`
"""

AVAILABILITY = """# Code & Data Availability

## Data
All primary data are public on NCBI GEO: GSE111006, GSE111010, GSE111016,
GSE226151. No new human/animal data were generated for the computational resource.

## Code
HMSR analysis code is publicly available at
`https://github.com/BrownBiotech/hmsr-sarcopenia` (release tag `v0.4-paper1`,
DOI: `10.5281/zenodo.<TBD-auto-on-release>` via Zenodo GitHub integration) under
the **MIT License** (`LICENSE` file at repository root).

The code is provided in the repository under `pipeline/`, `scripts/`,
`validation/`. Environment pinned in `environment.yml` /
`environment.lock.yml`. A one-command re-run and a terminal verifier
(`scripts/verify.py`, STATUS=PASS) reproduce all reported numbers. Output
provenance hashes are in `data/CHECKSUMS.txt`.

The companion in-vitro / in-vivo validation plan (v0.2, v0.3) and its
operationalized deliverables (construct designs, antibody panel, Seahorse /
myobundle force SOPs, power analysis, vendor shortlist) are included in the
`validation/` subdirectory of the repository as supporting documentation and
are also bundled here as Supplementary files
(`experimental_validation_plan_v0.2.md`, `experimental_validation_plan_v0.3.md`,
`validation_open_issues.md`).

## Bundled supplementary tables
- Table S1: all 195 candidate genes with full meta-statistics.
- Table S2 (not bundled; regenerable): full 37,469-gene replication matrix.
- Table S3: composition-confound sensitivity (WP3b).
- Table S4: composition-adjusted mitochondrial enrichment per cohort.
- Table S5: gene-set permutation enrichment + descriptive AUC.
- Table S6: therapeutic-axis transparency projection (15-PGDH / PGE₂ / atrogene / myostatin / biogenesis).
- Table S7: Freedman–Lane covariate-exchangeable permutation enrichment.
- Table S8: library-size (sequencing-depth) covariate sensitivity.

## Scope / honesty statement
Gene-level findings are exploratory candidates (no genome-wide FDR survivor); the
pathway-level mitochondrial signal is robust to composition adjustment, to
Freedman–Lane permutation, and to library-size adjustment. A non-composition
technical factor in one cohort is not fully excluded without RIN/QC metadata.
See `internal_critical_review_v0.2.md` and the Codex adversarial review
`codex_adversarial_review_v0.3.md` for the full self-audit.
"""


def main() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "figures").mkdir(parents=True)
    (OUT / "supplementary").mkdir(parents=True)

    copied: list[tuple[str, Path]] = []

    def copy(src: Path, dest_rel: str) -> None:
        dest = OUT / dest_rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)
        copied.append((dest_rel, dest))

    # manuscript + assets
    copy(MANUSCRIPT[0], MANUSCRIPT[1])
    for s, d in FIGURES:
        if s.exists():
            copy(s, d)
    for s, d in SUPPLEMENTARY:
        if s.exists():
            copy(s, d)

    head = git_head()

    # generated support docs
    (OUT / "supplementary" / "reproducibility_receipt.md").write_text(gen_reproducibility_receipt(head))
    copied.append(("supplementary/reproducibility_receipt.md", OUT / "supplementary" / "reproducibility_receipt.md"))
    (OUT / "supplementary" / "cover_letter.md").write_text(COVER_LETTER)
    copied.append(("supplementary/cover_letter.md", OUT / "supplementary" / "cover_letter.md"))
    (OUT / "supplementary" / "code_data_availability.md").write_text(AVAILABILITY)
    copied.append(("supplementary/code_data_availability.md", OUT / "supplementary" / "code_data_availability.md"))

    # README
    readme = f"""# HMSR Sarcopenia Paper 1 — Submission Bundle (v0.4)

Self-contained submission bundle for the HMSR mitochondrial-sarcopenia manuscript.
**Distinct from** `submission/v0.4` in the parent repo, which is the separate
Eda2r/Hjv rat-exercise paper.

## Contents
- `paper1_sarcopenia_v0.4.md` — manuscript (v0.4: Codex MAJORs fixed; Table 1
  demographics corrected from real GEO metadata; Stouffer-vs-DL disambiguated;
  "replicated" → "candidate" in figures; Freedman–Lane + library-size
  sensitivity both confirm the mitochondrial result; bounded translational
  paragraph linking to the muscle-quality companion Perspective with HPGD
  transparency).
- `figures/` — Figures 1–5 (PNG + PDF). Figure 5 = pathway-level competitive
  shift (in-set minus out-set) for the mitochondrial programme + 6 sub-modules
  + non-mitochondrial controls, from a label-permutation test (N=2,000).
- `supplementary/` — Tables S1/S3/S4/S5/S5b/S6/S7/S8, main Tables 1–3,
  experimental validation plan v0.1 + v0.2 + v0.3 (operationalized), validation
  open-issues tracker, two internal critical reviews (v0.1, v0.2), Codex
  adversarial review v0.3, modality/dataset audits, reproducibility receipt,
  cover letter, code/data availability (updated to include MIT License + Zenodo
  DOI + validation/ deliverables).
- `manifest.tsv` — path, SHA256, byte size for every packaged file.

## Provenance
- Generated: `{GEN_DATE}`
- Source repository HEAD: `{head}` (branch `sarcopenia/paper1-v0.4`)
- Builder: `python3 scripts/build_submission_package.py`
- Verifier: {verify_status()}
- License: MIT (full text at `sarcopenia-multiomic-resource/LICENSE`)
- Repository: `https://github.com/BrownBiotech/hmsr-sarcopenia` (release tag
  `v0.4-paper1`; DOI: 10.5281/zenodo.<TBD-auto-on-release>)

## Honesty note
No gene survives genome-wide FDR; gene lists are exploratory candidates from a
disclosed post-hoc gate. The pathway-level mitochondrial finding is robust to
muscle-composition adjustment (Table S3/S4), to Freedman–Lane covariate-
exchangeable permutation (Table S7), and to library-size covariate adjustment
(Table S8). See `supplementary/internal_critical_review_v0.2.md` and
`supplementary/codex_adversarial_review_v0.3.md`.
"""
    (OUT / "README.md").write_text(readme)
    copied.append(("README.md", OUT / "README.md"))

    # manifest
    manifest = ["path\tsha256\tbytes"]
    for rel, p in sorted(copied):
        manifest.append(f"{rel}\t{sha256(p)}\t{p.stat().st_size}")
    (OUT / "manifest.tsv").write_text("\n".join(manifest) + "\n")

    print(f"Submission bundle built: {OUT}")
    print(f"Files packaged: {len(copied)} (+ manifest.tsv)")
    for rel, _ in sorted(copied):
        print(f"  {rel}")


if __name__ == "__main__":
    main()
