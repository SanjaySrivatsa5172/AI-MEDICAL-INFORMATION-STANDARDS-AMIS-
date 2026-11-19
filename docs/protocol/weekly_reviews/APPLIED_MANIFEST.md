# Applied weekly-review proposals — record of what was taken and what was not

## 16 November 2026 — seven proposals applied under PI approval

The PI approved all seven queued proposals in writing on 16 November 2026, answering a numbered
list item by item ("YES" to each of the seven, plus the consolidated §10 rewrite). Applied the
same day on `claude/cedars-sinai-safety-protocol-0gb0wg` by anchored assert-once replacement:
every anchor was verified to occur exactly once across the whole set **before** any write, and
again at the moment of its own replacement.

Thirteen content hunks were applied in this order.

| Source | Hunk | Section | What it does |
|---|---|---|---|
| 10 Sep | 1 | §5.6 | Pins the reasoning / inference-time-compute control as a reported parameter in its own right. §7.3.1 inherits it by reference, so the jury judges are covered without a second edit |
| 10 Sep | 2 | §0 | Adds BiasMedQA to the DECISION 1 evidence note and corrects the inference that model advancement confers anchoring resistance |
| 10 Sep | 3 | §5.3 | Gives the public/private split a measured magnitude, with the one-model/four-item bound stated |
| 17 Sep | 1c | §4.2 | Separates run-to-run instability (same-input nondeterminism) from challenge-induced flipping |
| 17 Sep | H1 | §13 | Library count refreshed to the **live** figure, 234 as of 16 Nov 2026 — not the 185 the patch itself carried, per that patch's own use-the-live-figure note |
| 24 Sep | 1a | §0 | DECISION 3 evidence note: dangerous outputs are mostly stochastic, so central-tendency rules hide them |
| 24 Sep | 1b | §8.1 | Any-run critical-miss rate reported alongside the primary analysis. No extra model calls, scenarios or participants; no bearing on §8.4 |
| 24 Sep | 2 (revised) | §11 | ACEP AI Task Force consensus and the patient-facing-AI-under-governance definition |
| 15 Oct | 1a | §5.3 | Access modality pinned and reported; we characterise the API surface, not the consumer app |
| 15 Oct | 1b | §11 | TRIPOD-LLM completeness is 40% in practice, so the protocol commits specifically rather than by reference |
| 22 Oct | 1 | §5.2 | Paraphrase-invariance floor: the register claim is conditioned on a floor this revision does not measure |
| consolidated | count | §10 | "Three boundaries" → "Six boundaries" |
| consolidated | insert | §10 | The 17 Sep, 8 Oct and 5 Nov boundaries inserted together, in that order, before the closing boundary |

### The §10 consolidation

The 17 Sep, 8 Oct and 5 Nov patches each carried their own §10 count hunk with conditional
CASE A/B/C forms, because each was written not knowing whether the others would be applied. Three
patches contending for one count line was a sign the queue had become the problem, and the PI
approved replacing them with a single consolidated rewrite. The three boundary texts are applied
**verbatim** from their patches; only the count hunks were discarded, replaced by one
three-to-six change. §10 now reads, in order: encounter-time S2/S3 tail; vignettes are not
patients; the disposition is measured once; safeguard activation is not safeguard robustness; no
claim is made about who the instrument protects; a benchmark result is not a clearance.

### Deliberately NOT applied

- **8 Oct hunk 1c (Table A4 crisis-safeguard clause).** The patch marked it an OPTIONAL companion
  and said the PI "may take hunk 1a+1b alone and leave this." The approval covered the §10
  boundary; hunk 1c was never put to the PI and is **still available**. Table A4's
  crisis-safeguard row is therefore unchanged.
- **Every "OPTION FOR THE PI" block** in the seven patches. These are design expansions, not
  edits: the 17 Sep stability probe, the 8 Oct bypass-robustness probe, the 15 Oct dual-access
  factor, and the 22 Oct within-register paraphrase condition. All four expand §8.4 and all four
  remain unproposed. The 22 Oct patch argues the paraphrase condition is the best value of the
  four if exactly one is ever adopted.
- **PART 5 items 1 and 6–15, and supplement S1.** Not part of this approval.

### Decisions recorded at the same time

- **DECISION 1 — deferred.** Change 12 is not adopted. §0, §4.3, §5.3 and §8.4 updated to say so.
  §8.4 remains UNRESOLVED and blocking, but the obstacle changed character: the power section
  against the primary endpoint alone is now work to be done, not a question waiting on pilot data
  that do not exist.
- **DECISION 3 — majority-of-three.** §0, §5.6, §7.3.2 and §8.1 updated.
- **DECISION 4 remains open.** The PI answered "YES" to the Arm C1 scope line, but scope is not a
  yes/no and no scope was specified, so **nothing in the protocol assumes it either way** and the
  §10 single-turn boundary still records Arm C1 as exploratory and unresolved. This needs a
  specified scope before it can be recorded.

### Build and verification

Rebuilt by the standard recipe (`pandoc` → `soffice`), 33 pp, PDF newer than both its sources.
Rendered to PNG and inspected page by page. The inspection caught one defect that text validation
would have missed: the READ FIRST block still said "Four PI decisions ... remain open" and that the
sample size "cannot be written at all until pilot data exist", both false once DECISION 1 and 3
were resolved. Corrected before the final build.

**Known cosmetic defect, not fixed:** in the title block, the Principal Investigator's
"Director, HAV Center of Fresno" line lacks a trailing hard-break, so "Co-Investigator" runs on to
the same rendered line. It predates this work and is a one-character fix, but it is protocol text
and nobody has approved changing it.
