# CLAUDE.md

Guidance for Claude Code when working in this repository.

## Resume phrases — read this first

When the user says any of:

- **"LLM SAFETY PROTOCOL"**
- **"CEDARS SINAI LLM SAFETY PROTOCOL"**
- **"CEDARS PROTOCOL"** / **"the protocol"** in a clinical-research context

…they are resuming the Cedars-Sinai IRB protocol work. **Immediately read
`docs/protocol/CONTEXT_MEMORY.md` end to end** before responding or acting. It carries the
full project state: people, design, evidence base, standing automation, working constraints,
and the open items that block IRB filing. Then check `git log --oneline -10` and confirm the
branch, because the memory file records state as of its last update and decisions move.

Do not reconstruct project context from memory or from this file alone — `CONTEXT_MEMORY.md`
is the source of truth for that work.

## Two things live here

**1. AMIS — AI Medical Information Standards** (the repository's primary subject)
`README.md`, `SPECIFICATION.md`, `standards/*.yaml`, `implementation/python/`, `examples/`.

**2. The Cedars-Sinai LLM triage-safety protocol** (a sub-package under `docs/`)
Protocol of record, scientific introduction, physician onboarding briefing, IRB
correspondence, the weekly literature-review agent, and `reference-library/library.json`.

Do not assume a task in `docs/protocol/` is about AMIS, or that a task in `standards/` is
about the protocol.

## Hard rules for the protocol work

- **Branch:** develop and push only on `claude/cedars-sinai-safety-protocol-0gb0wg`.
- **Permission first:** never edit the protocol or its companion documents without the PI's
  explicit approval. Proposed changes are written as reviewable patch files under
  `docs/protocol/weekly_reviews/` and justified against specific current literature —
  citation, finding, and the section affected. This applies even to claims the literature has
  falsified: flag them URGENT, then wait.
- **Dashboard alerts are PI-only.** Never resolve one.
- **Never create additional triggers or routines** for this project.
- **Citations:** verify through the PubMed or Scite MCP before a citation enters any
  document. Label preprints as preprints. Report unverifiable figures as unverified — never
  reconstruct them.
- **Document builds:** `pandoc X.md -o X.docx --standalone`, then
  `libreoffice --headless --convert-to pdf --outdir . X.docx`. No `--toc`, no `--metadata
  title/subtitle/author` — the markdown carries its own title block. Render the resulting PDF
  to PNG and look at it before delivering; text validation alone has missed real layout
  defects here.
- **Edits are anchored and assert-once:** a scripted replacement must verify its anchor
  appears exactly once and fail loudly otherwise, so silent drift is impossible.

## Reference library schema

`reference-library/library.json` uses a strict 14-key schema per entry — no extra keys:
`title, authors, journal, year, pmid, doi, url, type, topics, tier, relevance, source,
design_overlap, date_added`.

Before any merge touching this file, diff against the canonical reconciler branch
`claude/cedars-sinai-ai-safety-refs-nw6h0p` — this branch has silently fallen dozens of
references behind before.

## File naming

Lowercase with hyphens for new code and scripts. Existing protocol documents keep their
established uppercase names (`PROTOCOL_v3_CONSOLIDATED.md`, `CONTEXT_MEMORY.md`).
