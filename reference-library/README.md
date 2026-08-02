# Reference Library — Patient-Facing AI in Emergency Triage

Continuously updated reference library supporting the Cedars-Sinai research
protocol **"Physician-Authored Evaluation of Patient-Facing Artificial
Intelligence in Emergency Triage"** (PI: S. Sanjay Srivatsa, MD).

> Core question: *Can AI systems safely recognize when symptoms described in
> everyday language require emergency care?*

## What lives here

| File / folder | Purpose |
|---|---|
| `library.json` | Canonical reference data (single source of truth) |
| `search-strategy.md` | The daily scan's governing search specification |
| `dashboard-template.html` | Dashboard source template (data-free) |
| `dashboard.html` | Generated dashboard (template + inlined data) |
| `build.js` | Generates `dashboard.html` + the Obsidian mirror from `library.json` |
| `obsidian/PATIENT FACING AI TRIAGE SAFETY/` | Generated Obsidian vault folder — one note per reference + index |

## Daily update loop (automated)

1. Scan PubMed + Scite/citation graph using `search-strategy.md` (major medical
   journals and their AI subsidiaries: NEJM AI, JAMA / JAMA+ AI, Lancet Digital
   Health, Nature Medicine, npj Digital Medicine, EM journals, JAMIA, preprints).
2. Filter for clinical relevance; check retraction notices.
3. Dedupe against `library.json` (DOI → PMID → normalized title) and append new
   entries with today's `date_added`.
4. Flag any work overlapping this study's design (`design_overlap: true`) —
   rendered as **Critical — design overlap** on the dashboard and in Obsidian.
5. `node reference-library/build.js` regenerates the dashboard and the Obsidian
   folder; the dashboard artifact is republished at the same URL; changes are
   committed and pushed.

## Live dashboard

<!-- DASHBOARD_URL -->

## Using the Obsidian folder

The generated folder `obsidian/PATIENT FACING AI TRIAGE SAFETY/` matches the
folder of the same name in the PI's Obsidian vault. It is regenerated on every
scan — keep personal annotations in separate notes that link into it. To sync,
either point Obsidian (or the Obsidian Git plugin) at this repo folder, or copy
the folder into the vault after each update.
