# Companion-document audit — 30 August 2026

Triggered by the PI: *"CHECK THE OTHER DOCS"*. Every companion document and deck was scanned for
descriptions of the scoring architecture superseded by the 29–30 August approvals (§7.3 amendment;
PART 5 items 2, 3, 4, 5). Search terms: `majority verdict`, `AC1`, `0.75`, `at least three`,
`scoring weight`, `40%`, `30%`, `0.804`, `0.784`, `two gates`.

## Result

| Document | Status |
|---|---|
| `docs/protocol/PROTOCOL_v3_CONSOLIDATED.md` | **Current** — carries all approved changes |
| `docs/protocol_scientific_introduction_v3.md` | **Resynced 30 Aug** (PI-approved) |
| `docs/protocol/PHYSICIAN_ONBOARDING_BRIEFING.md` | **Clean** — 0 hits. Describes the architecture qualitatively (physicians sovereign, primary endpoint deterministic) without naming weights, judge counts, gates, or thresholds. Nothing to change |
| `docs/irb_letter_farkouh_v2.md` | **Clean** — 0 hits |
| `docs/compliance_checklist.md` | **Clean** — 0 hits |
| `docs/extended_rationale.md` | **Clean** — 0 hits |
| `docs/implementation_guide.md` | **Clean** — 0 hits |
| `docs/Triage_Benchmark_Technical_Review.pptx` | **STALE — action recommended.** Slides 6, 8, 9 |
| `docs/cedars_ramaswamy_nm2026_redraft_plan.md` | **Stale but historical** — line 219 |
| `docs/friday_meeting_brief.md` | **Stale but historical** — line 16 |
| `docs/Cedars_Onboarding_Aug7_Addendum.pptx` | **Stale but historical** — slides 5, 6 |

The onboarding briefing being clean is not luck: it was written to explain *why* the study exists,
and it describes the judging architecture by principle rather than by parameter. Documents written
at that altitude do not go stale when parameters change.

## The one that needs a decision: Triage_Benchmark_Technical_Review.pptx

This is the ten-slide technical design-review deck for PhD-level AI reviewers. It is **undated and
presented as current**, which is what makes it different from the three historical artifacts below.
It currently tells a technical audience:

- **Slide 6:** "~40% Deterministic / ~30% Cross-vendor ensemble / …", "≥3 independent frontier
  judges … majority verdict", "(ii) Gwet AC1 ≥ 0.75", "Failing either gate reverts the component",
  and "NOHARM accepted its autograder only because κ vs physicians (0.804) matched inter-physician
  κ (0.784). We adopt that bar."
- **Slide 8:** "Agreement: Gwet AC1 primary…" — this one is still **correct**; §8.2 keeps AC1 primary
  for *reliability reporting*. Only its use as a gate was retired. No change needed.
- **Slide 9:** "The ensemble carries ~30% of scoring weight behind falsifiable gates. If the gates
  fail, that weight reverts to physicians."

Slide 6 is the problem: it states two gates where there are now three, majority verdict where
unanimity is required, a retired threshold as live, and quotes two figures that could not be
verified from any retrievable source. Presenting that to AI reviewers understates the design and
cites numbers we cannot stand behind.

**Recommended:** rewrite slides 6 and 9 to match the current §7.3 / §7.6, leave slide 8 alone.
I have not touched the deck — it needs PI approval, and the rebuild should be visually inspected
slide by slide before delivery.

## The three historical artifacts — recommend a status note, not a rewrite

`cedars_ramaswamy_nm2026_redraft_plan.md` line 219 records the agent-judge ensemble sub-study **as
the PI proposed it at Rev. 3/4**. `friday_meeting_brief.md` is the brief for a specific meeting on
7 August. `Cedars_Onboarding_Aug7_Addendum.pptx` is dated in its own filename.

Rewriting any of these would falsify the record of what was actually proposed and said on those
dates — and the redraft plan in particular is the project's integration ledger, whose value is that
it shows how each decision was reached. **Recommended: add a dated forward-pointing status note to
the redraft plan** ("superseded 29–30 Aug 2026 by the §7.3 amendment; see PROTOCOL_v3 §7.3–§7.6"),
and leave the two dated artifacts untouched. Also not applied pending PI approval.
