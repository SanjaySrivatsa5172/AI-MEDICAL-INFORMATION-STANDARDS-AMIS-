# PROPOSED EDIT — Scientific Introduction is now out of sync with the protocol
# STATUS: NOT APPLIED. Awaiting PI approval.
# Raised: 30 August 2026, discovered while applying PART 5 items 4 and 5.

## The problem

`docs/protocol_scientific_introduction_v3.md`, paragraph "**Determinism-First Hybrid
Evaluation**" (line 92), still describes the scoring architecture **as it stood before the
29 August §7.3 amendment**. It is an enclosure that goes to Cedars alongside the protocol, so
the two documents now contradict each other on six specific points:

| The Scientific Introduction says | The protocol now says |
|---|---|
| "Approximately 40% of the total scoring weight… Approximately 30%… The remaining 30%" | No weights. Layers are defined by **remit**; no composite score exists (§7, Table A5) |
| "at least three independent frontier LLM judges" | **Exactly three**, excluded by vendor **and model family**, each run **≥3 times** (§7.3.1) |
| "with the majority verdict used" | **A verdict requires unanimity**; 2–1 and no-mode items are jury-indeterminate and route to §7.5 within a budget (§7.3.2) |
| Two gates: agreement ≥ inter-physician, and "Gwet AC1 ≥ 0.75" | **Three conjunctive gates** on one-sided confidence bounds, including a **directional** gate on the conditional false-credit rate. **AC1 ≥ 0.75 is retired**; AC1 is a reported statistic, not a gate (§7.3.3–7.3.5, §0 DECISION 2a/2b) |
| NOHARM "κ = 0.804 vs 0.784" quoted as the acceptance precedent | Those figures are **unverifiable** — they appear in no retrievable source. PART 5 item 12 (unapproved) would strike them; the protocol's §7.3.3 now cites NOHARM's acceptance *logic* without the numbers |
| Silent on the deterministic layer's own criteria | §7.2.1 gates the deterministic layer, and §7.6 declares the jury non-load-bearing |

**This is my error to own:** the 29 August §7.3 approval made this paragraph stale and I did not
check the companion documents at that time. It has been stale for two days across three
approvals.

## Why it matters

The Scientific Introduction is the document physicians and the IRB read *first*. A reviewer
holding both documents sees the protocol claim unanimity and three gates while the introduction
claims majority verdict and two — and one of the two it names has been formally retired. That is
the kind of discrepancy that costs credibility on a submission whose whole argument is
methodological rigour.

## Proposed replacement

Replace the paragraph beginning "**Determinism-First Hybrid Evaluation.**" in full with:

> **Determinism-First Hybrid Evaluation.** The scoring pipeline routes each criterion to the
> least interpretive method capable of scoring it, and the layers are defined by what they score
> rather than by any share of a composite — no composite score is computed. Explicit-escalation
> determination, ESI level match, key-feature checklist items, killer-item detection, and format
> compliance are scored **mechanically**. In particular, explicit escalation — the primary
> endpoint's core element — is detected by a pre-registered deterministic phrase-inventory rule
> set applied to the model's own free-text words; **no language model judges the primary
> endpoint.** That classifier is itself held to pre-registered acceptance criteria — a stated
> labelling procedure, reported sensitivity, specificity and full confusion matrix against
> physician labels, and a pre-registered fallback to physician ascertainment if it does not clear
> its floor — because under an asymmetric loss function the sensitivity of escalation *detection*
> determines whether the primary endpoint measures model failure or classifier failure.
>
> Two component judgments — differential-diagnosis completeness and reasoning coherence — are
> evaluated by an ensemble of **exactly three** frontier LLM judges, version-pinned, each excluded
> by vendor and model family from the system it is scoring, and each run at least three times. **A
> jury verdict exists only where the three judges are unanimous**; split and no-mode items are
> recorded as jury-indeterminate and routed to physician adjudication within a pre-registered,
> hazard-ordered budget. A margin-1 majority carries the reliability of one judge, not three, which
> is why it is not treated as a verdict.
>
> The ensemble is subordinate and provisional, and **non-promotion is its default state**. A
> component may be scored by the jury only after clearing three conjunctive acceptance gates, each
> evaluated on a one-sided confidence bound rather than a point estimate: agreement with the
> blinded physician panel at least as high as inter-physician agreement on the same items (the
> acceptance logic established by the NOHARM benchmark, a preprint); a pre-registered absolute
> floor, since beating human disagreement is necessary but demonstrably not sufficient; and a
> **directional** criterion bounding the conditional false-credit rate — of the components
> physicians rate deficient, the proportion the jury rates adequate. The third gate exists because
> every symmetric agreement coefficient counts a dangerously lenient judge and a merely fussy one
> identically, which is untenable under this study's loss function. Chance-corrected agreement is
> **reported** alongside kappa, the observed prevalence, and the raw cell counts — not used as a
> gate. Any component failing any gate reverts entirely to physician scoring; where a component is
> not promoted the jury still runs in shadow mode, reported at zero scoring weight.
>
> Harm potential assessment, reasoning quality in ambiguous cases, communication appropriateness,
> and the interaction-failure metrics are reviewed by the physician scoring panel and are **never
> delegated to models**; physicians also adjudicate every anchoring and crisis-safeguard detection.
> **No endpoint reported in this study depends on the LLM jury layer**, and every planned analysis
> is computable from the deterministic and physician-sovereign layers alone — the study's answer to
> the model-judging-model objection is structural, not rhetorical. The tiered approach is also a
> practical necessity: 50 scenarios, six or more models, three to five runs each, and multiple
> crossed conditions generate thousands of individual responses.

## Also to decide

The replacement above **omits the NOHARM κ = 0.804 / 0.784 figures**, because they could not be
retrieved from any available source. That is PART 5 item 12, which has not been approved. If you
would rather keep the figures pending your own retrieval of the NOHARM PDF, say so and I will
reinstate them with an explicit "figures pending verification" marker instead.

Approving this edit does **not** approve PART 5 item 12 for the protocol text; it only governs
this paragraph of the Scientific Introduction.
