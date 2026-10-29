# PENDING CO-INVESTIGATOR NOTIFICATION — queued, not yet sent

**Blocked by:** Gmail connector requires re-authorization. **Send once restored.**
Third queued notification; send in date order (29 Aug EDIT 1, 29 Aug §7.3, then this one).

---

**To:** pawaskarkeyur96@gmail.com
**Cc:** drsanjaysrivatsa@gmail.com
**Subject:** Cedars protocol — PI-approved changes 30 Aug 2026 (PART 5 items 2 and 3)

---

Keyur,

Follow-on to yesterday's §7.3 amendment. The PI has approved two of the fifteen consequential
edits, and together they fix the criticism the adversarial review considered the most serious
thing it found — one that had nothing to do with the LLM jury at all.

APPROVAL OF RECORD
Wording: "APPROVE PART 5 ITEMS 2 AND 3"
Date: 30 August 2026
Applied in commit (see repository log; branch claude/cedars-sinai-safety-protocol-0gb0wg)
Document after the edits: Protocol v3.1, now 31 pp

---

ITEM 2 — THE DETERMINISTIC LAYER NOW HAS ACCEPTANCE CRITERIA (new §7.2.1)

The problem, stated plainly: the deterministic phrase-inventory classifier carries the ENTIRE
primary endpoint and triggers the automatic zeros for killer items, and it had no acceptance
criteria whatsoever — while the LLM jury, which touches no reported endpoint, had two gates (now
three). The protocol's rigour was inverted. Under an asymmetric loss function the sensitivity of
escalation DETECTION decides whether Critical Miss Rate measures model failure or measures regex
failure, and a regulator reading FDA PCCP guidance or IMDRF N88 asks for the measuring instrument's
operating characteristics first.

§7.2.1 now specifies:
- Scope: escalation detection and killer-item detection (Appendix B Component 7).
  Differential-diagnosis completeness stays a jury component — PART 5 item 1 was not approved.
- Labelling procedure: physicians label a pre-registered sample of model outputs for presence or
  absence of explicit escalation, and separately for each killer-item form. A fast binary reading
  of the model's own text, distinct from the §7.4 sovereign judgments. Labels frozen before the
  classifier is finalised.
- Reported operating characteristics: sensitivity, specificity, and the FULL CONFUSION MATRIX
  against physician labels, with scenario-level cluster-bootstrap intervals, reported separately by
  register and by severity weight. The two off-diagonal cells are reported separately — a classifier
  that misses escalations and one that hallucinates them are not the same instrument.
- Acceptance and fallback: no numeric floor is asserted at this revision. It is fixed before
  unblinding on the same pre-registered rail as the jury gates (DECISION 2a) — a stated mapping on
  the blinded sample, judged on a one-sided confidence bound. If the classifier does not clear its
  floor, THE PRIMARY ANALYSIS MOVES TO PHYSICIAN ASCERTAINMENT. That fallback is expensive, which
  is exactly why it is priced before filing rather than discovered afterwards.

Appendix C in the §14 register was rewritten to match: it now covers the escalation AND killer-item
inventory, with its labelling procedure and acceptance criteria.

ITEM 3 — EVERY ENDPOINT IS NOW ASSIGNED TO A SCORING LAYER

Before this edit, Anchoring Failure Rate, crisis-safeguard activation consistency, and the four
interaction-failure metrics were assigned to NO scoring layer anywhere in the protocol body, and
Table A4's method column named an actual layer only for the primary endpoint. A reviewer would have
assumed by elimination that AFR fell to the jury — landing the circularity objection squarely on the
endpoint carrying the study's novelty claim about anchoring.

Table A4 now has a Layer column with a legend, §4.2 states each assignment inline, and §7.4 names
what the physician layer owns. The consequential decisions:
- ANCHORING FAILURE RATE: deterministic against the Component 7 killer-item form ("attribution to a
  benign cause without recommending evaluation"), which §7.2 already detects, WITH physician
  adjudication of every positive detection and of a pre-registered random sample of negatives, and
  EXPLICITLY NEVER JURY-SCORED.
- Crisis-safeguard consistency: same treatment — deterministic detection, physician-adjudicated,
  never jury-scored.
- Interaction-failure metrics: physician-sovereign (§7.4).
- The table now states outright that no reported endpoint depends on the jury layer, and that every
  §8 analysis is computable from the deterministic and physician-sovereign layers alone.

WHAT THIS MEANS FOR THE STUDY'S DEFENCE
The circularity objection — "you argue models cannot be trusted to recognise an MI, then trust
models to judge whether another model missed one" — is now answerable from the document itself
rather than by assertion. No endpoint we report depends on a language model's judgment.

LIVE REFERENCE DASHBOARD
https://claude.ai/code/artifact/528465e1-0a3b-40aa-81ab-00373aaa2461

STILL OPEN
PART 5 items 1 and 4–15, and supplement S1 (judge-input sanitization). Item 4 (replacing the
~40/30/30 weights with a statement of remit) is worth attention: with two jury components retained,
Table A5's single joint share does not say how it divides when one component reverts and the other
does not. Also open: DECISION 1 (Change 12), DECISION 2a/2b, DECISION 3, DECISION 4; the protocol
number; Dr. Farkouh's role; and the Winters docket number.

If you disagree with either applied edit, say so and it goes back to the PI.

Sanjay Srivatsa, MD — Principal Investigator
Prepared with Claude Code
