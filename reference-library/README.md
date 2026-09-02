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

**Dashboard:** https://claude.ai/code/artifact/528465e1-0a3b-40aa-81ab-00373aaa2461 (republished daily at the same URL)

## Using the Obsidian folder

The generated folder `obsidian/PATIENT FACING AI TRIAGE SAFETY/` matches the
folder of the same name in the PI's Obsidian vault
(`~/Documents/Obsidian Vault/PATIENT FACING AI TRIAGE SAFETY`). It is
regenerated on every scan — keep personal annotations in separate notes that
link into it.

**Automatic sync to the vault (macOS):** run `sync-obsidian-vault.sh` on the
Mac that hosts the vault. `bash sync-obsidian-vault.sh install` syncs
immediately and schedules a daily pull at 6:20 AM local time (after the cloud
scan); plain `bash sync-obsidian-vault.sh` syncs once; `uninstall` removes the
schedule. The script only adds/overwrites generated notes — it never deletes
personal files from the vault folder.
