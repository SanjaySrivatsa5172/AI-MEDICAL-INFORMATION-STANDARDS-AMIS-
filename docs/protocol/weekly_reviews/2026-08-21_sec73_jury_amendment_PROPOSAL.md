# §7.3 Jury Robustness Amendment — Proposal for PI Approval

**To:** S. Sanjay Srivatsa, MD — Principal Investigator\
**From:** Claude Code (project session)\
**Date:** 21 August 2026\
**Status:** **PART 4 APPROVED AND APPLIED — 29 August 2026** (PI wording: "APPROVE THE 7.3 AMENDMENT").\
The §7.3 replacement text in PART 4 is now the protocol's §7.3 (commit 8aebcfc). **PART 5 — the fifteen
consequential edits — and supplement S1 were NOT part of that approval and remain unapplied**, except
where internal consistency of the approved §7.3 text forced a change; see the application note at the
end of this file.\
**Approval requested on:** the draft replacement text for §7.3 (PART 4) and the fifteen discrete consequential edits (PART 5), each approvable or declinable independently.

---

## Provenance

This amendment is the product of **two independent multi-agent reviews, 43 agents in total**, run on 21 August 2026:

1. **Verification review (32 agents).** Started before this session, presumed dead, recovered complete today. Verified three 2026 preprints at code level — PatientAgentBench (arXiv 2607.25485; reference implementation read at github.com/amazon-science/PatientAgentBench), IMCBench (arXiv 2606.28556), and the multi-agent collusion paper (arXiv 2512.03097) — and subjected 24 candidate protocol claims to adversarial refutation. **All 24 were refuted as drafted; none had entered any document.** The surviving substance and its jury-threat analysis feed this amendment.
2. **Amendment review (11 agents).** Five independent analytical lenses (measurement theory; correlated judge error; tail concentration; verdict granularity; hostile-reviewer/regulatory), four adversarial refuters (feasibility; statistical correctness; over-engineering; citation verification), and one synthesis. The full lens and refutation record is retained in the project archive.

**Independent spot-verification (this memo's author, via PubMed, 21 Aug):** Byun et al. (*J Med Syst* 2026, PMID 42481841, doi 10.1007/s10916-026-02440-y) — both quoted sentences and the Fleiss κ 0.087–0.223 range confirmed verbatim from the indexed abstract; Bedi et al./MedHELM (*Nat Med* 2026;32(3):943–951, PMID 41559415, doi 10.1038/s41591-025-04151-2) — citation and PMC13267972 confirmed; Ho et al. (*BMC Med Educ* 2026, PMID 42387499, doi 10.1186/s12909-026-09848-7) — "Gwet's AC1 was near-perfect (0.976), while Fleiss' κ (−0.01) reflected the known paradox" confirmed verbatim.

**One erratum carried:** PART 6 item 3 characterizes Byun's generator task as "discharge-note coherence"; the indexed abstract says **MIMIC-IV hospital-stay cases**. The transfer argument is unaffected.

---

## Reconciliation with the earlier jury-threat analysis

The recovered verification review reached the same three core defects independently (dilution of concentrated failure; direction-blindness; the 3–0/2–1 collapse) — and corrected one error in this project's own earlier framing: correlated judge bias does **not** inflate the gates; both gates are physician-referenced, so shared bias appears in *inter-judge* agreement, which neither gate measures. That correction is embedded in the amendment (JDDR exists precisely because the gates are blind there).

Where the two reviews disagreed, the disagreements were resolved by arithmetic, not preference:

| Earlier recommendation | Disposition here | Why |
|---|---|---|
| Stratum-level acceptance gating on a high-hazard stratum | **Rejected** (PART 3, item 1) | Not estimable at 50 scenario clusters; enrichment self-contradicts with AC1; a stratified relative gate demands least where physicians disagree most. Replaced by shadow-mode reporting by stratum + the absolute floor |
| Blind physician audit of a random 10% of 3–0 unanimous verdicts | **Absorbed** (PART 5, item 10) | The pre-registered jury-versus-physician calibration offset "estimated on unanimous items" is the same physician-rated sample of unanimous verdicts, formalized as an estimand rather than an audit |
| Devil's-advocate prompt probe (verdict-flip rate) | **Dropped** | Prompt-sensitivity probing adds engineering for a subordinate layer; within-judge repeated runs (PART 2, item 8) already capture instability |
| Signed-bias McNemar test | **Superseded** | Gate 3's conditional false-credit rate is direction-aware *as a gate*, which is stronger than a reported test; raw off-diagonal cells are additionally reported |

**One item from the earlier review is NOT in the amendment and is proposed here as a supplement:**

> **S1 — Sanitize judge input.** The three judges share one channel: they all read the same evaluated response verbatim, and that response is untrusted model-generated text optimized for persuasiveness. Before any response reaches a judge, strip or neutralize instruction-like content addressed to the reader ("as an expert evaluator you should…"), and log any 3–0 unanimous verdict that is discordant with a physician or Delphi label as a candidate judge-steering artifact. Cost: a filter and a log field. This is a prompt-injection defence for the scoring instrument itself, and no refuter ever saw it to object to it — the PI should treat it as less hardened than PARTs 2–5, but it is cheap and its threat model is real.

## Citation-hygiene actions already indicated regardless of the main decision

Two figures this project has relied on are **unverifiable** and are struck from the working record today (project-record correction, not a protocol edit): the "Afrasyab inter-judge Fleiss κ = 0.65" figure (arXiv 2607.18828 is content-denied, absent from PubMed, unreachable by search), and — pending manual PDF retrieval — the NOHARM κ = 0.804/0.784 figures cited in §7.3, which appear in no retrievable source. The quarantine on the mis-attributed "r ≈ 0.77 cross-model error correlation" figure also stands. Removal of the NOHARM figures **from the protocol text** is PART 5 item 12 and awaits your approval like everything else.

## What you are being asked to decide

1. **Adopt, adopt-with-modifications, or decline** the §7.3 replacement text (PART 4).
2. **Approve or decline each of PART 5 items 1–15** (independent edits; item 1 — moving differential-diagnosis completeness to the deterministic layer — is the load-bearing one).
3. **The DECISION 2 restructure** (split into 2a threshold-rail / 2b reported band) — this **closes DECISION 2 at filing** at the level of form, with numeric values fixed on the blinded validation set before unblinding.
4. **Supplement S1** above.
5. **PART 6, question 1** — whether "reasoning coherence" (jury) and "reasoning quality in ambiguous cases" (physician-sovereign, §7.4) are the same construct. If they are, a merge moots most of §7.3 and is cheaper than everything else here. **The synthesis recommends you answer this first.**

Nothing is time-critical today except PART 5 item 11 (pre-specifying the severity distribution of the 50 scenarios), which must land before scenario authoring opens in week 2 of the study timeline.

---

# AMENDMENT TO §7.3 — JURY ROBUSTNESS

**Status:** DRAFT for PI approval. Nothing in this document has been applied to any protocol or companion file.
**Prepared:** 21 August 2026 · **Basis:** five lens analyses, four adversarial refutations, protocol v3.1 as read.
**Constraint observed throughout:** §8.4 is blocking. No power figure, sample-size figure, or precision target appears anywhere below, including in the draft protocol text. Where a rejection turns on estimability, the qualitative finding is stated and the supporting arithmetic is deliberately held out of the protocol — one refuted proposal (L3-P9) failed precisely because it wanted that arithmetic written into §0.

---

## PART 1 — The problem in plain terms

§7.3 currently promises two tests that decide whether an LLM jury may score two components of each response. Both tests ask the same question — how often does the jury agree with physicians? — and that question is the wrong one, in three ways a clinician will recognise at once.

**Agreement counts the easy cases.** Most model responses are unremarkable, and the jury will agree with physicians about them. When the responses physicians judge deficient are a minority, a jury can miss every single one and still post a high agreement score, because the score is carried by the cases nobody was worried about. Under conditions this study expects, a jury reproducing *none* of the physicians' deficiency findings returns AC1 = 0.947 against a gate set at 0.75.

**Agreement does not know which way an error runs.** This study exists because missing a heart attack and over-calling one are not the same mistake — under 5% undertriage against as much as 35% overtriage. Every symmetric agreement statistic, AC1 and kappa alike, counts the two identically. A dangerously lenient jury and a merely fussy one produce numbers identical to four decimal places.

**Agreement is an average, and the failure is not.** If the jury does well on ordinary cases and badly on the atypical catastrophes and benign-looking presentations the benchmark was built to probe, the average conceals it. Both gates can pass on a jury that fails exactly where the study's value lies.

Underneath all three: "majority verdict" records a 2–1 split with the same confidence as a 3–0. On a 2–1 split, three judges are worth one judge.

Two further points. The number 0.75 was borrowed from a benchmark scale developed for a different statistic. And the two figures §7.3 cites as the authority for Gate 1 could not be retrieved from any source available to this project.

---

## PART 2 — What survived

Ordered by importance: leverage on the actual defect, strength of survival across the four refutations, and cost. Every item below survived at least three of the four refuters, or survived all four in a narrowed form that is stated as such.

---

### 1. Move differential-diagnosis completeness out of the jury layer

**Change.** Score differential-diagnosis completeness deterministically, as coverage of the Appendix B Component 5 "top life threats" list, using the Appendix C phrase-inventory method. The jury's remit reduces to **reasoning coherence alone**.

**Lands in.** §7.2, §7.3, Table A5. Requires PI approval of a components shift out of the jury block.

**Justification.** Component 5 is already a pre-registered, enumerated gold list produced by the Delphi panel in weeks 6–8 — causally prior to any model output, and therefore uncontaminated by the fluency of the text being judged. Moving it converts a subjective rating governed by an agreement coefficient nobody can calibrate into a classifier operating characteristic governed by sensitivity and specificity, which are prevalence-invariant and direction-aware. It halves the jury's exposure, and therefore halves every validation, routing, and reversion cost downstream. It is the only proposal in the pool that shrinks the surface on which the whole problem exists rather than instrumenting it.

**Cost.** One additional pre-registered phrase inventory, validated by the same procedure Appendix C already establishes for escalation detection — and therefore falling under the acceptance criteria in item 12 below. Known limitation: a model may name a life threat and then hedge it away. That is the identical limitation already accepted for the *primary* endpoint, so accepting it here is strictly more defensible, not less.

**Who tried to kill it, and why it lived.** Nobody did. All four refuters ranked it among the highest-leverage items available; the feasibility refuter called it a precondition for costing anything else, the statistical refuter "the highest-leverage structural fix anywhere in the pool," and the overfitting refuter credited it as *subtractive* — the only kind of amendment that makes an IRB submission easier to approve.

---

### 2. Fix the measurement scale before fixing anything computed on it

**Change.** State explicitly, per scored component, whether the jury rating is binary or ordinal, with the number of levels and their anchors. Name the coefficient that follows from the scale: Gwet AC1 for nominal or binary, Gwet AC2 with linear weighting for ordinal. Publish the rubric and the verbatim judge prompt as a new appendix.

**Lands in.** §7.3; new Appendix F.

**Justification.** §7.3 currently sets a threshold on a coefficient without defining the scale it is computed on, so neither the coefficient nor any threshold on it is well defined, and a methods reviewer can reject the gate on that ground alone. Precedent for the split within one instrument is verified: Henry et al. (BMJ Open 2026;16(1):e109388, doi 10.1136/bmjopen-2025-109388 — verified verbatim; a human-rater study of systematic-review appraisal, methodological precedent only, not an LLM study) use AC1 for nominal items and AC2 with linear weighting for the ordinal ones. AC2 as the weighted ordinal member is established in Vanacore & Pellegrino (Stat Med 2022;41(11):1986–2004, doi 10.1002/sim.9341 — verified).

**Cost.** Zero statistical cost. The rubric must exist before scoring-panel training in any case, so this is a deliverable being scheduled, not work being created. It is on the critical path: it belongs in weeks 1–2.

**Who tried to kill it, and why it lived.** No refuter opposed it. The statistical refuter escalated it, calling it "radically under-ranked" and marking the defect it fixes as *fatal*: every numeric result any lens computed — the prevalence arithmetic, the closed form, the margin theorem, the split-rate identity — is computed on a binary 2×2 that §7.3 never authorises. If the components are ordinal, all of it ceases to be defined. The overfitting refuter accepted the scale specification and asked only that the coefficient-selection clause be dropped if Gate 2 were deleted; it is not deleted (item 3), so the clause stands.

---

### 3. Replace the scalar point-estimate Gate 2 with a confidence-bound rule on a direction-aware quantity; demote AC1 to a reported statistic

**Change.** Three parts. (a) Every acceptance gate is evaluated on a **one-sided confidence bound**, computed by scenario-level cluster bootstrap, not on a point estimate. (b) The directional criterion is the **conditional false-credit rate** — of the components the blinded physicians rate deficient, the proportion the jury rates adequate — bounded above. (c) AC1 (or AC2) is **reported, not gated**, with its cluster-bootstrap interval, alongside Fleiss/Cohen kappa, the observed positive-class prevalence, and the **raw 2×2 cells**.

**Lands in.** §7.3; §8.2 for the reporting set.

**Justification.** Three separate defects, each independently sufficient.

*Prevalence.* AC1's chance term is 2π(1−π), so AC1 ≥ t is exactly equivalent to raw agreement ≥ t + (1−t)·2π(1−π). At t = 0.75 that is p_a ≥ 0.75 + 0.5π(1−π). As the flagged class becomes rare the chance correction evaporates and AC1 converges on raw percent agreement — the documented behaviour (Shankar & Bangdiwala, PMID 25168681, verified verbatim; Wongpakaran et al., PMID 23627889, with Gwet a co-author, verified). Below roughly 20.4% positive-class prevalence the 0.75 criterion is satisfied by a jury with zero sensitivity on the flagged class.

*Direction.* AC1's observed and chance terms are both exactly invariant under exchanging the two off-diagonal cells; so are Cohen's kappa, Krippendorff's alpha, PABAK, and p_pos. A lenient jury and a strict one return identical values to four decimals. Reporting the **raw cells** is what makes them distinguishable, and it costs one table row. Cicchetti & Feinstein (PMID 2189948, doi 10.1016/0895-4356(90)90159-m — verified verbatim) established forty years ago that the omnibus coefficient "should always be accompanied by separate individual values of ppos and pneg."

*Precision and provenance.* A point estimate is not a decision rule. And 0.75 is a kappa convention — the Landis & Koch band structure (PMID 843571, verified) as bounded by Cicchetti 1994 (doi 10.1037/1040-3590.6.4.284; record verified, band values secondary-source, full text denied). No AC1-native benchmark scale exists; Henry et al. say so in print. Because AC1 systematically exceeds kappa at skewed marginals by an amount growing with skew, the transported cut point is silently loosened. Gwet's own recommended benchmarking procedure is functionally a lower-bound rule (Vanacore & Pellegrino, doi 10.1002/qre.2982 — verified, including their verbatim recommendation that under non-asymptotic conditions bootstrap intervals are the methods of choice). Ho et al. (PMID 42387499, doi 10.1186/s12909-026-09848-7 — verified verbatim) supply the peer-reviewed demonstration that the two statistics reach opposite conclusions on identical ratings: AC1 = 0.976 with Fleiss κ = −0.01.

The confidence-bound form is also the construction that makes this amendment **filable at this revision**: a bound-based acceptance rule names no sample size, makes no power claim, and fails automatically when the achieved sample cannot support it. Four proposals used it piecemeal without noticing that property; the statistical refuter named it and it is stated explicitly in the draft text.

**Cost.** Analyst work only — a bootstrap routine and one added paragraph of pre-registration. The honest consequence is that the criteria are harder to clear than AC1 ≥ 0.75, and components will revert to physician scoring more often. That is the intent, not a defect, and the PI should adopt it knowing so.

**Who tried to kill it, and why it lived.** Two attacks landed and both are absorbed. The **statistical refuter** killed the original three-limb version: its unsafe-direction limb was defined as an unconditional rate and was therefore vacuous at exactly the prevalence the argument assumes, and its sensitivity limb and its false-credit limb were the same quantity twice. Respecifying on the **conditional** rate — which is prevalence-invariant — fixes both and collapses three limbs to one. It also noted, correctly, that a threshold "re-derived at the observed prevalence" is post hoc unless the *mapping* is pre-registered in advance; the draft text pre-registers the mapping, not a number. The **overfitting refuter** argued for deleting Gate 2 outright rather than repairing it. That was rejected on the evidence in item 4: deleting Gate 2 leaves only the relative gate, which is demonstrably satisfiable at absolute agreement its own field calls poor. Deleting is worse than repairing. What the overfitting objection did win: the *reporting* half of this item survived all four refuters unopposed and is the cheapest correct amendment available; the gating half is deliberately kept minimal, one criterion, not three.

---

### 4. Add an absolute floor to Gate 1, fix its aggregation-level mismatch, and anchor it on the Delphi label where one exists

**Change.** Three parts. (a) Gate 1 retains the relative comparison but adds an **absolute agreement floor**. (b) Both sides of the comparison are computed at the **same aggregation level** — a single blinded rater on both sides, or consensus-versus-held-out-rater on both sides. (c) Where a Delphi gold label or killer-item designation exists for the item, jury agreement is evaluated against that label as well.

**Lands in.** §7.3, Gate 1 wording; references §5.4 and §7.5.

**Justification.** A relative standard deflates wherever the reference deflates, and this one is currently tilted toward passing on top of that. Per §7.5 the physician panel's score is an adjudicated mode over two or three raters, while the inter-physician benchmark is two raw single raters — so the numerator's reference side is de-noised and the denominator's is not, and by Spearman–Brown the tilt grows precisely as inter-physician agreement falls, i.e. it is largest in the atypical-catastrophe and benign-anchor strata. No lens caught this; the statistical refuter raised it independently, and the fix is free.

The absolute floor rests on the strongest evidenced attack on Gate 1 in the pool, verified twice: MedHELM (Bedi et al., *Nat Med* 2026;32(3):943–951, doi 10.1038/s41591-025-04151-2, PMID 41559415 — figures verified through PMC13267972) cleared exactly this comparison, reporting an LLM-jury ICC of 0.47 against clinician ratings which "notably outperformed both the average agreement between clinicians themselves (ICC = 0.43)." Koo & Li (PMID 27330520 — verified verbatim) classify values below 0.50 as *poor*. **Beating human disagreement is necessary and demonstrably not sufficient.** Carry the caveat: ICC and AC1/kappa are different statistics on different scales and the task differs, so this is a structural demonstration, not a numeric transfer — and a three-judge aggregate against a single clinician is a Spearman–Brown asymmetry in its own right.

The Delphi anchor is the one available partial escape from bias shared by descent. Gate 1 as written is a peer-agreement test, and a bias common to judges *and* physicians is invisible to it by construction — a real risk in triage specifically, where physicians are documented to under-triage ACS along an atypicality axis (Pope et al., NEJM 2000;342:1163–70, PMID 10770981 — verified: women under 55, OR 6.7; non-white patients, OR 2.2; dyspnea as chief symptom, OR 2.7; non-diagnostic ECG, OR 3.3) and models are documented to stereotype the same axis (Zack et al., *Lancet Digit Health* 2024;6(1):e12–e22, PMID 38123252 — verified verbatim). A Delphi label is set deliberatively before any model output exists and cannot be contaminated by that output's fluency.

**Cost.** Wording only. The Delphi labels already exist by design. It will tighten the gate enough that components fail which would otherwise pass — the intended effect, knowingly accepted.

**Who tried to kill it, and why it lived.** The stratified version of this proposal was refuted by all four refuters and is rejected (PART 3, item 1). What survived is the absolute floor, which every refuter endorsed independently of the stratification. The statistical refuter additionally killed the power calculation offered in support of the stratified version — it applied a two-independent-proportions formula to a comparison Gate 1 defines on the *same* items, which is a paired design; that calculation is not carried forward, and no calculation replaces it. On the Delphi anchor: the feasibility refuter established that half of it is uncomputable by construction — the Delphi panel convenes in weeks 6–8, model outputs do not exist until weeks 10–12, so the panel cannot label *reasoning coherence*, a property of text that does not yet exist. The clause therefore has a referent only for differential-diagnosis completeness, which is exactly why item 1 moves that component out of the jury. The wording below reflects that: the Delphi anchor applies where a label exists, and does not pretend to apply where none can.

---

### 5. Unanimity is the jury verdict; record the vote vector; route the remainder within a pre-registered budget

**Change.** Store the full per-judge vote vector and a derived `jury_margin` field (3–0 / 2–1 / no mode) on every jury-scored item, plus a separate `run_margin` field. A jury verdict exists only where the three judges are unanimous; non-unanimous and no-mode items are recorded as **jury-indeterminate**. For a component that has been promoted, indeterminate items are physician-scored under §7.5, within a pre-registered adjudication budget with a fixed priority ordering; items beyond the budget carry a truncation flag and are reported in a pre-specified sensitivity analysis. Pin the panel at **exactly three** judges.

**Lands in.** §7.3, §5.6, §7.5; §8.1 for the provenance covariate.

**Justification.** The recording requirement closes a genuine specification hole: §7.3 says "majority verdict" with no tie rule and no no-mode rule, while §7.5 supplies both for the human ladder — and with three judges on an ordinal rubric, three distinct scores has no mode and "majority verdict" is undefined. Pinning the panel at exactly three removes the tie problem more cheaply than writing a tie rule, and is independently supported: a five-judge panel raises non-unanimity rather than lowering it, a 3–2 majority carries the same single-judge posterior as a 2–1, and the cross-vendor supply is close to exhausted at four or five vendors, so a five-judge cross-vendor panel is nearly unconstructible without doubling a provider.

The substance is that a 2–1 split is not a jury verdict. Under conditional independence with each judge correct with probability *q*, the posterior odds that the majority is correct depend on the vote only through the margin, and at margin 1 the posterior is exactly *q* — the reliability of one judge, not three. The statistical refuter verified this to four decimals and then correctly refuted the claim that it holds unconditionally: under exchangeable positive dependence the posterior is lower still, so the theorem as stated is false under the pool's own premise while the policy direction *strengthens*. The draft text states it accordingly.

Byun et al. (*J Med Syst* 2026;50(1), PMID 42481841, doi 10.1007/s10916-026-02440-y — peer-reviewed, verified via PubMed) reach the same operational conclusion from data: "a single LLM verifier lacks sufficient reliability to serve as a stand-alone judge of clinical reasoning at scale," and "the unanimous-agreement tier offers a candidate for selective automation."

**Cost.** Recording is free and must be decided before unblinding because it changes what is stored. The routing is not free, and its volume is genuinely unknown — see the refutation note. The budget is what makes it affordable: it is the only mechanism in the entire pool that *caps* physician time rather than spending it, and it is §8.4-clean because a resource cap is not a power figure.

**Who tried to kill it, and why it lived.** The recording half survived all four unopposed and is a prerequisite for everything else here. The routing half was attacked hard and correctly. The **feasibility refuter** rated the unbounded version *fatal* — at Byun-like disagreement rates it does not degrade the study, it stops it. The **overfitting refuter** rated it fatal for a different reason: spending the study's scarcest resource, sovereign physician hours, to rescue a subordinate layer inverts the protocol's own priority ordering. The **citations refuter** established that every quantitative claim about how often the rule would fire — 17–26%, 13–22%, ~26–38% automatable — derives from a figure that cannot be verified at all (see item 10). What survives all of that is a narrow form: routing exists **only for a promoted component**, is **bounded by a pre-registered budget**, is **halved** by item 1's removal of differential completeness, and is roughly three times cheaper under first-run-primary (DECISION 3). No number for the split rate appears in the protocol; it is measured, not imported.

---

### 6. Shadow mode, a non-load-bearing declaration, and a complete endpoint-to-layer map

**Change.** Three linked parts. (a) Where a component is not promoted, the jury still runs — **shadow mode**: verdicts collected, version-pinned, and reported as exploratory findings, contributing zero scoring weight. (b) A new short §7.6 declares that no reported endpoint depends on the jury layer, that every §8 analysis is computable from the deterministic and physician layers alone, and that all results are reported with and without jury-derived components. (c) Assign an explicit scoring layer to **every** endpoint in §4.2 and Table A4.

**Lands in.** §7.3; new §7.6; §7.2/§7.3/§7.4 and Table A4 (new "scoring layer" column).

**Justification.** Shadow mode is the best-constructed item in the pool from an §8.4 standpoint: it measures without gating, so it states no sample size, makes no power claim, and cannot fail for lack of precision — it reports what it finds with honest intervals. It converts the tail-concentration premise in the current PENDING note from an assumption into a measurement, which matters because the direct evidence that LLM *judges* degrade in high-hazard strata is thinner than the evidence that LLM *answerers* do; the closest available support is Belmadani et al. (arXiv 2603.04033 — **preprint**, verified verbatim), that "LLM-based judgments are strongly influenced by the model that generated the answer, with agreement varying substantially across generators." Shadow mode is also the calibration bridge: any rule under which hard items get human scoring and easy items get machine scoring risks confounding between-model comparison with scoring provenance, and the overlap set is exactly the data needed to estimate that offset.

The declaration is factually true today and verified three times over in the document — §4.1 ("No language model judges the primary endpoint"), §7.2 ("The primary endpoint lives entirely in this layer"), and Table A4. It converts the study's strongest defence from an assertion into a demonstration, and turns the circularity attack — *you argue models cannot be trusted to recognise an MI, then trust models to recognise when another model missed one* — into a reported result.

The endpoint map is the precondition for the declaration being true rather than merely asserted. Verified by grep against the file: §7.2 enumerates escalation, ESI match, key-feature checklist, killer items, and format compliance; §7.3 enumerates two components; §7.4 enumerates three. **Anchoring Failure Rate appears in none of them**, and neither do crisis-safeguard activation consistency or the four interaction-failure metrics. Table A4's "scoring method" column names an actual layer only for Critical Miss Rate; the AFR row merely restates the definition. Since AFR is a free-text semantic judgment, a reviewer will assume by elimination that it falls to the jury — landing the circularity objection on the endpoint carrying the study's novelty claim (Sheppert et al., *Int J Med Inform* 2026;219:106550, PMID 42335861 — verified: LLMs ranked the anchor diagnosis first in 55.6% of responses versus 21.2% for residents and 10.0% for attendings; Omar et al., *Rheumatology* 2026, PMID 42587430 — verified: dismissive referral-note anchor downgraded urgency, vignette-level p = 0.01). Recommendation: AFR is physician-sovereign, or deterministic against the Appendix B Component 7 killer-item form "attribution to a benign cause without recommending evaluation," which the deterministic layer already detects — and **explicitly not jury-scored**.

**Cost.** Shadow mode costs API calls and no physician time. The declaration costs a duplicate run of analyses already specified. The map costs one table column and a clause.

**Who tried to kill it, and why it lived.** Nobody. All three parts survived all four refuters. The overfitting refuter went further, arguing shadow mode "should absorb most of the pool" and that a PI adopting shadow mode plus the declaration plus margin recording has answered every failure mode identified, in about three paragraphs. That argument is largely accepted; it is the reason this amendment is shorter than the pooled proposals and why the reporting apparatus below is deliberately compact.

---

### 7. Report the Jury–Determinism Dissociation Rate

**Change.** Among items the deterministic layer classifies as critical misses — no escalation phrase present and the gold disposition is EMS NOW or ED NOW — report the proportion the jury places in the top band for its scored component. Report it descriptively; do **not** attach a numeric ceiling at this revision.

**Lands in.** §7.3 diagnostics.

**Justification.** This is the only proposed check that can detect correlated judge error running in a direction **physicians also share**. Both existing gates are physician-referenced and are therefore blind to shared bias by construction. The deterministic phrase inventory is a pure function of surface tokens in the model's own output: it cannot be seduced by fluency, confidence markers, or organisation, and it is not physician-referenced at scoring time. Both inputs already exist in the pipeline, so the marginal cost is zero.

The architectural analogue is verified and is labelled honestly as an analogy, not evidence: Han & Shamszaman (arXiv 2512.03097 — **preprint**, verified verbatim) report that in a healthcare multi-agent system collusion drove attack success and harmful-recommendation rates "up to 100% in unprotected systems," while "the verifier agent restores 100% accuracy by blocking adversarial consensus" by checking decisions against clinical guidelines. Their setting is scripted adversaries, not spontaneous correlated error. This project has already reached and recorded that conclusion about the same paper; the amendment does not overturn it.

**Cost.** Two sentences of protocol text.

**Who tried to kill it, and why it lived.** The gate form was killed by three refuters and by the proposal itself — a ceiling "to be finalised after pilot" is a placeholder, and a number to be chosen later is not a pre-registration. The descriptive form survived all four; the feasibility refuter called it the best cost/benefit item in the pool. Three caveats must travel with it and are in the draft text: it inherits the deterministic layer's own operating characteristics (so it depends on item 12); its denominator is model-dependent and can be empty for a good model; and its ceiling is therefore not pre-registrable at this revision.

---

### 8. Extend §5.6's version pinning and repeated-run discipline to the judges

**Change.** Run each judge at least three times per item under pinned sampling parameters; the within-judge majority is that judge's verdict; report within-judge instability alongside the existing model-instability metric, and record the within-judge margin.

**Lands in.** §5.6, §7.3.

**Justification.** §5.6 pins and repeats the systems under test "so that nondeterminism is measured rather than averaged away," and says nothing about the systems doing the measuring. Haldar & Hockenmaier (arXiv 2510.27106 — **preprint**, verified verbatim) report that LLM judges "have low intra-rater reliability in their assigned scores across different runs. This variance makes their ratings inconsistent, almost arbitrary in the worst case," and that multi-run majority voting both absorbs that variance and improves accuracy against human judgments. Without this, an observed 2–1 split cannot be distinguished from sampling noise, and item 5's margin recording loses its meaning. Symmetry between the instrument and the subject is also the cleanest available answer to a TRIPOD-LLM reviewer.

**Cost.** Roughly three times the judge inference cost — small in absolute terms. Zero physician hours. One added metric.

**Who tried to kill it, and why it lived.** The **feasibility and statistical refuters** both rejected the competing version, which would have *dropped* an unstable judge — that leaves two judges, a 1–1 has no majority, and it silently creates a third unbudgeted routing path to physicians. Taking the within-judge majority always yields a verdict and routes nothing; that is the version adopted. The **overfitting refuter** objected that run-to-run instability is a named endpoint for the models under test and is not one for judges. Under shadow mode the jury's behaviour *is* a reported exploratory finding, which is precisely where judge instability belongs, so the objection is answered rather than overridden. The statistical refuter's caveat is carried: a within-judge majority followed by a cross-judge majority stacks two collapses, so the within-judge margin is recorded too.

---

### 9. Tighten the diversity specification, narrowly

**Change.** Two clauses only. (a) No judge may share a vendor **or model family** with the system whose output it is scoring on that item. (b) Presentation order and position are randomised per item. Plus the panel-size pin from item 5.

**Lands in.** §7.3, §5.6.

**Justification.** "Cross-vendor" purchases a vendor label, not statistical independence, and self-preference is a continuous *similarity* effect rather than a self-identity one — so a per-vendor diagnostic will not see it, and exclusion must be by family. Goel et al. (arXiv 2502.04313 — **preprint**; abstract verified, with two flags: one indexing service garbles the second author, correctly Joschka Strüber, and a distinct 2023 paper shares the title stem, arXiv 2305.01481) define chance-adjusted similarity on overlap in model *mistakes* and report that "LLM-as-a-judge scores favor models similar to the judge, generalizing recent self-preference results," and that "model mistakes are becoming more similar with increasing capabilities, pointing to risks from correlated failures." The protocol pins *frontier* models, which selects on exactly that axis; version pinning freezes the correlation structure without reducing or measuring it. Position bias is among the best-replicated judge biases (Zheng et al., arXiv 2306.05685 — **preprint**, bibliographically verified).

**Cost.** A judge pool of four to keep three eligible per item, so roughly a third more inference. No physician time. Prompt-engineering work in weeks 1–10, which have slack.

**Who tried to kill it, and why it lived.** The **overfitting refuter** rated the full proposal *serious* — an open-weight judge means local inference plus its own pinning and validation, a killer-item-anchored judge means authoring and validating a second judge prompt, and all of it is engineering build-out for a subordinate layer. Both of those clauses are rejected (PART 3, item 9). The one clause it conceded as cheap — a vendor's judge does not score that vendor's outputs — is retained and widened to family, which is what the verified evidence actually supports. Position randomisation survived all four.

---

### 10. Correct the citation provenance in §7.3 — and strike the figure the PENDING note rests on

**Change.** Three parts. (a) Label NOHARM as a preprint, per the protocol's own §13 rule, and **remove the κ = 0.804 / 0.784 figures** unless the PI or a collaborator can retrieve them from the PDF; pin the version and access date. (b) Replace them with the NOHARM findings that *are* retrievable. (c) Strike the "Afrasyab, inter-judge Fleiss κ = 0.65" figure from CONTEXT_MEMORY §4 and from the reasoning behind the PENDING note.

**Lands in.** §7.3 (Gate 1 citation), §13, CONTEXT_MEMORY §4.

**Justification.** §7.3 currently carries two authority-conferring numbers and **neither can be checked**.

NOHARM (PMID 41532042, PMC12794822, doi 10.48550/arxiv.2512.01241) is indexed with article type *Preprint* and journal *ArXiv*, while §13 of the same protocol states that "Preprints are identified as such throughout" — a self-inflicted internal inconsistency at the single citation on which Gate 1's acceptance logic rests. The κ figures appear in neither the PubMed abstract nor anything reachable via Scite or targeted search; two refuters independently returned the same negative. Two indexing services return different titles *and* different first authors for the same DOI, indicating a v1/v2 revision, so a version-and-access-date pin is required for anything quoted from it.

What *is* retrievable from the NOHARM abstract, verified by the citations refuter, is better suited to this protocol than the figure it would replace: "harm of omission accounting for 76.6% (95% CI 76.4–76.8%) of errors"; "potential for severe harm... in up to 22.2% (95% CI 21.6–22.8%) of cases"; and "a diverse multi-agent approach improves safety compared to solo models (mean difference 8.0%, 95% CI 4.0–12.1%)." Omission dominance is direct support for this study's undertriage asymmetry. The multi-agent result is the only retrievable evidence anywhere in this pool that ensemble diversity helps in a clinical safety setting — and it concerns multi-agent *answering*, not multi-agent *judging*, which must be said when it is cited.

The Afrasyab record is real (arXiv 2607.18828, single author, 2026) but is content-denied and closed, absent from PubMed, and unreachable by search — so κ = 0.65 and every figure derived from it are **unverifiable, not merely secondary-source**. It is the parameter on which every cost and feasibility estimate in the entire analysis rests. Note precisely: the figure appears in CONTEXT_MEMORY §4 and in the reasoning behind the PENDING note; grep confirms it does **not** appear in the protocol text itself, so this is a project-record correction, not a protocol-text correction.

**Cost.** Editorial, plus one manual PDF retrieval by someone with arXiv access. The substantive cost is that removing both numbers makes the jury layer look weaker on the page. That is a legitimate outcome the PI should be free to reach.

**Who tried to kill it, and why it lived.** All four refuters confirmed it; the statistical refuter argued it should be ranked first in the pool. What was killed is the *replacement*: the citations refuter refuted substituting Byun's κ = 0.087–0.223 as the load-bearing figure, because Byun's generators were 8B–70B open models on MIMIC-IV hospital-stay coherence and the judge panel included a mini model — not three frontier judges, not patient-facing triage. Swapping one poorly matched imported number for another is not an improvement. **Strike, cite Byun as a bounding case only, and measure the parameter.**

---

### 11. Report the remaining diagnostics — and stop there

**Change.** A compact reported set, none of it gating: jury margin distribution overall and by SW class and anchor type; within-judge and between-judge instability; the **double-fault rate** across judges conditioned on the physician or Delphi label; per-judge self-preference by family with the leave-one-out score shift and its interval; and jury–physician agreement by register as a within-scenario paired contrast.

**Lands in.** §7.3 diagnostics; §8.2.

**Justification.** Double-fault is the right independence statistic because it is defined on *joint* errors, which is what determines whether a majority vote is safe (Kuncheva & Whitaker, *Machine Learning* 2003;51(2):181–207, doi 10.1023/a:1022859003006 — verified verbatim, including their own caveat that diversity measures poorly predict ensemble accuracy; that caveat concerns using diversity to *forecast* performance, not to *detect* dependence, which is the weaker use here). Conditioning on the gold label matters: it is what distinguishes correlated judge error from item-difficulty heterogeneity, and the unconditional alternative cannot (PART 3, item 2).

Register is handled by a paired contrast, reported and not gated. It is fully crossed, so pairing removes scenario variance and dominates two absolute gates — but no evidence exists either way on whether *judges* degrade on lay narrative. Carry the correction the citations refuter supplied: Ada et al. (*EJOG* 2026;326:115351, PMID 42561577 — verified verbatim) is **not a flat null**. The null is on overall GCCS (adjusted cumulative OR 0.78, 95% CI 0.57–1.06, p = 0.115); the same abstract reports patient-language prompts had *fewer* GCCS = 0 ratings (OR 0.66, 95% CI 0.46–0.96, p = 0.031) and, after FDR, higher triage appropriateness and clinical applicability (both adjusted p = 0.028). Wherever the project characterises Ada as a null, that characterisation should be made precise.

**Cost.** Analysis only; all inputs exist. One results table.

**Who tried to kill it, and why it lived.** The **overfitting refuter** rated the full diversity-statistics table *minor*-refuted on the grounds that no clinical reviewer can interpret four unfamiliar ensemble statistics and no decision depends on them. That objection is accepted in part: the set is narrowed to **one** joint-error statistic rather than four, and the register non-inferiority margin and reversion rule are dropped entirely (a margin is a power statement). The **statistical refuter** independently argued double-fault should be primary over the unconditional alternative, which is the narrowing adopted.

---

### 12. Pre-register acceptance criteria for the deterministic layer

**Change.** Give the deterministic phrase inventory what §7.3 gives the jury: a stated labelling procedure, reported operating characteristics with a confusion matrix against physician labels, a pre-registered fallback if it fails, and a numeric floor **set by the same pre-registered rail as the jury's thresholds** rather than asserted now. Scope it to escalation detection *and* killer-item detection — and, if item 1 is adopted, to the new differential-completeness inventory.

**Lands in.** §4.1, §7.2, Appendix C.

**Justification.** The rigour in this protocol is inverted, and this is the cheapest place to un-invert it. §4.1 says only that the inventory is "validated against a physician-labeled sample before unblinding" — no threshold, no procedure, no failure path — for the classifier that carries the entire primary endpoint, while §7.3 carries two falsifiable gates and a revert rule for a layer that touches no reported endpoint. Under an asymmetric loss function, the sensitivity of escalation *detection* determines whether Critical Miss Rate measures model failure or regex failure. A regulator reading FDA's PCCP guidance or IMDRF N88 will ask for the measuring instrument's operating characteristics first. And per §14, Appendix C does not yet exist. Note the scope correction: §7.2 and Table A5 show the deterministic layer scores five components, and §7.1 makes killer items trigger automatic zeros for an entire key feature — so the ungated classifier carries more than the primary endpoint alone.

**Cost.** Escalation labelling is a fast binary judgment on the model's own text, not a component rating. If the inventory fails its floor, the primary analysis moves to physician ascertainment, which is expensive — a risk worth pricing before filing rather than discovering after.

**Who tried to kill it, and why it lived.** Three refuters ranked it the single most important item in the pool. The **statistical refuter** rated it *fatal as drafted* for one reason only: the proposed sensitivity floor of 0.98 on a lower bound is a hidden and extreme sample-size claim that violates the §8.4 block, and would pre-commit the primary endpoint to an expensive fallback on near-certainly-achievable performance. The requirement survives with the number stripped and routed onto the same deferral rail as DECISION 2. That is the only change.

---

## PART 3 — What was rejected, and why

Recorded so the PI can see that the elaborate options were considered and killed, and on what grounds. Re-proposing any of these should require answering the objection stated here.

**1. Stratified acceptance gates.** Four separate lenses proposed evaluating the gates within severity and register strata, or within named hazard strata. Refuted by all four refuters. Three independent grounds. (i) *Not estimable.* Whatever the SW = 3 stratum turns out to be, it supplies too few independent clusters to gate on — and §8.1 already commits scenario as the clustering unit, so the analysis cannot inflate the count by counting responses. The supporting arithmetic exists in the lens record and is **deliberately not carried into the protocol**, because writing it there is a sample-size claim under §8.4. (ii) *Self-contradictory when combined with enrichment.* Enriching the validation sample toward hazard items is the correct fix for conditional rates, which are prevalence-invariant; it is the wrong fix for AC1, which the same analysis proves is not. One cannot enrich and then gate on AC1. (iii) *Stratifying Gate 1 makes it easier to pass where the hazard is.* A relative standard deflates wherever the reference deflates, and physicians disagree most in exactly the atypical-catastrophe stratum — so a stratified Gate 1 would demand least where it should demand most. Two further defects: the benign-anchor stratum has no pre-specified denominator (Appendix B Component 1 includes a benign-anchoring detail "where applicable"), and one lens's item count was manufactured by borrowing the deterministic layer's per-key-feature unit for a jury that scores fixed components per response. **What survived instead:** the absolute floor (PART 2 item 4) and shadow-mode reporting by stratum, which measures the tail without pretending to gate on it.

**2. The excess-concordance test as a gate.** The proposal was to predict inter-judge agreement under conditional independence from measured per-judge accuracy, and revert any component whose observed agreement exceeded the prediction. The reference tables were the most carefully executed arithmetic in the pool and reproduced exactly. The statistic is nonetheless **not identified**, fatally: pairwise agreement is convex in accuracy, so by Jensen's inequality, heterogeneous item difficulty alone pushes observed agreement above the prediction *with fully independent judges*. An excess is equally consistent with correlated judge error and with a difficulty mixture — and all three judges read the same response text, a one-to-many common cause this project has already recorded. It also would rarely fire at achievable precision, so the pre-registration risk is paid without buying detection power. **What survived instead:** double-fault conditioned on the gold label, which is conditioned on truth and therefore escapes the confound.

**3. The fluency-covariate regression as a promotion gate.** Regressing jury and physician scores on surface covariates — length, hedging density, confidence-marker density, empathy openers — is a good diagnostic with verified instrumentation (Alvarez-Arenas et al., openRxiv doi 10.64898/2026.06.15.26355670 — **preprint**, verified verbatim: "AI scores correlated with surface features such as length and lexical diversity, whereas human scores did not," with hidden-state steering showing verbosity is a causal driver; Narayan et al., *Neurosurg Rev* 2026;49(1), PMID 42545535 — verified verbatim on "a sycophantic phenotype invisible to categorical analysis"). As a **gate** it inverts the safety logic: promotion would be granted on a *failure to reject*, so a smaller or noisier validation study makes promotion easier, and folding it into the Benjamini–Hochberg family makes it easier still. An underpowered gate that defaults to "promote" is worse than no gate under this loss function. Not adopted, in either form, at this revision.

**4. Unanimity-required-to-score as an unbounded rule, and any "maximum automatable fraction" trigger.** Rated fatal by two refuters. The bounded form survives (PART 2 item 5); the unbounded form and the fraction-trigger — which fires the full-reversion cliff on top of the routing cost — do not.

**5. A TOST equivalence band with a stated half-width and the item count it is powered for.** The recognition that a *band* is an equivalence claim, and therefore more sample-hungry than a floor, is correct and is preserved as prose. The numbers cannot go in: the proposal explicitly writes power figures into protocol text, which §8.4 forbids at this revision.

**6. Gate 3 as a two-sided band on raw pairwise agreement with δ = 0.15.** Two lenses converged on it, which was the strongest apparent convergence in the pool — and the citations refuter showed the calibration anchor is misread and, read correctly, points the other way. Livingston et al. (*JAMIA Open* 2025, PMID 40524837 — verified verbatim: "Pairwise consensus occurred in 60.6% of evaluations," 41 board-certified physicians and pharmacists, 426 query-response pairs) report *joint* consensus across a five-dimension framework, not per-dimension agreement. Undoing the conjunction puts the per-dimension physician split rate **below** the jury's, reversing the claimed inversion. Separately: δ = 0.15 is asserted, the cost note names an item count, and specifying a band on *raw* pairwise agreement makes it prevalence-dependent — the exact defect the rest of the amendment attacks. **The band concept is not dead**; it is carried into DECISION 2b (PART 5), where it is defined on the right quantity and its value is set from measurement rather than asserted.

**7. A jury-validation sample-size subsection in §8.4, with enrichment targets.** Out of bounds — it amends the section the protocol declares blocking, on behalf of an advisory layer, adding a second pilot dependency to the one already named as the largest obstacle to filing. Independently, its exact-binomial table was recomputed and runs 10–55% optimistic in every row, always in the direction of making the design look feasible, and its item count borrowed the wrong unit of analysis.

**8. Case-dependent binary weighting (40/0/60 in hazard strata).** The strategic instinct — physician sovereignty where the hazard is — is coherent and may still be adopted as a design commitment. It is rejected *as argued*, on three grounds: the estimability claim behind it rests on treating scenarios as perfectly correlated, which contradicts the design-effect assumption used two sections earlier in the same analysis; its physician-cost estimate is hostage to the unverifiable κ; and it legislates weights that currently have no consumer (see PART 5, item 4). **The one principle that survives and is carried into the draft text: jury delegation is binary, never a fitted or continuous function of measured agreement — a weight tuned to a measured stratum coefficient would launder an imprecise estimate into the scoring formula.**

**9. A mandated open-weight judge, and a killer-item-anchored judge.** The open-weight clause sits in tension with §7.3's own "frontier" requirement, is supported only by a record that returned no abstract (Verga et al., arXiv 2404.18796 — **preprint**, bibliographically verified, claims **secondary-source**), and carries an unpriced tradeoff: majority error is steeply increasing in per-judge error, so substituting a less accurate judge to buy independence can be net-negative, and no criterion for that trade was supplied. The killer-item-anchored judge duplicates work the deterministic layer already does mechanically and blurs the layer boundary. Both deferred; composition may be revisited from pilot data.

**10. Leave-one-judge-out reversion triggered by a change in model rank ordering.** The observation that a diagnostic with no consequence is not a safeguard is fair and is answered in PART 2 item 11 by reporting the leave-one-out score *shift with its interval*. A **rank-flip** trigger is rejected: its firing rate is governed by the spacing between model scores, not by the magnitude of judge bias, so it fires almost surely when models are close and almost never when they are far apart, regardless of bias. It is also not computable on a three-judge panel — leaving one out leaves two, which yields no majority — so it presupposes a pool the current §7.3 does not mandate. The supporting evidence for the trigger comes solely from the unretrievable Afrasyab record and must not enter the protocol.

**11. Dropping an unstable judge from the majority.** Creates a hidden third routing path at an unbudgeted rate. Superseded by the within-judge majority (PART 2 item 8), which always yields a verdict.

**12. A 100% audit of unanimous SW = 3 verdicts.** Double-pays. A full audit of unanimous verdicts in that stratum *is* full physician scoring of the stratum on the jury's components, arrived at accidentally and mislabelled an audit — and the routing rule then spends again on top while the jury still runs. If physician coverage of the hazard stratum is to be purchased, purchase it once, deliberately, as a design commitment.

**13. Requiring Gate 1 to be met against the Delphi standard for both jury components.** Uncomputable by construction for reasoning coherence: the Delphi panel convenes in weeks 6–8 and model outputs do not exist until weeks 10–12, so the panel cannot label a property of text that does not yet exist. Causal priority is the proposal's entire virtue and is also exactly what forecloses it. It survives for differential-diagnosis completeness only — which is the argument for moving that component out of the jury altogether.

**14. Defining hazard strata as explicitly non-demographic, on evidence grounds.** The scope decision may be right; the *reasoning* is a textbook inferential error and must not be written into a protocol. It converts a null result on race, ethnicity, socioeconomic status, and language barrier — of unstated power, on a different task — into an affirmative claim that a demographic stratum would carry no signal, and it contradicts evidence cited elsewhere in the same analysis (Pope et al.; Zack et al.), where the atypicality axis this study exists to probe is partly demographic. If the exclusion is retained anywhere, restate it as a scope choice, not a finding.

**15. Two citations that do not transfer.** (a) Wang et al. (arXiv 2604.07667 — **preprint**; quotations verified verbatim, including consensus stopping committing to error rates up to 32.1% with 0% escalation) studies multi-agent *debate* with message exchange, where the mechanism is explicitly social reinforcement. This jury has no inter-judge channel and a mechanical aggregator. This project already applied that exact test to the structurally identical collusion paper and concluded the jury is not an instance of its threat model; the same conclusion applies here. (b) Byun et al. as a replacement planning figure — see PART 2 item 10. Both may be cited as bounding or corroborating cases; neither may motivate a parameter.

**16. A characterisation of the jury-remedy literature that overstates it.** One lens rendered Williams et al. (*npj Digit Med* 2026, PMID 42477479, doi 10.1038/s41746-026-02992-w — verified verbatim) as "juries improved agreement on 1 of 11 criteria." The paper says the best single judge matched human evaluators on four of eleven criteria and that juries "improved agreement on only one **additional** criterion" — four to five, not one. The directional conclusion stands and is genuinely damaging to the ensemble premise: judges were systematically too lenient or too harsh in model-specific directions, i.e. exactly the bias an ensemble is supposed to cancel, and the ensemble barely cancelled it. But the domain is responses to questions from Rwandan health workers, with English-versus-Kinyarwanda context as the paper's central limitation — not emergency triage. Cite it accurately or not at all.

---

## PART 4 — DRAFT REPLACEMENT TEXT FOR §7.3

> **To the PI:** this replaces §7.3 in full, including the `[PENDING]` blockquote. It assumes the §7.2 and Table A5 changes listed in PART 5 items 1 and 4; if those are declined, the bracketed clauses marked `[conditional]` come out and the section reverts to two scored components. No sample-size, precision, or power figure appears anywhere below. Length is deliberate: the section grows, but the reassurance that used to have to live inside it moves to a short §7.6, so §7.3 stays a specification rather than an argument.

---

### 7.3 LLM jury layer — subordinate and provisional

`[conditional]` **Reasoning coherence** is evaluated by an ensemble of LLM judges. Differential-diagnosis completeness is scored mechanically against the pre-registered Component 5 life-threat list under §7.2 and is no longer a jury component.

The jury layer is **subordinate and provisional in both directions**: it may score a component only after that component clears the acceptance gates in §7.3.3, and it is never sovereign over harm. **Where a component has not been promoted, the jury still runs, and its verdicts are recorded and reported — but carry no scoring weight** (§7.3.6). Non-promotion is the default state of this layer and requires no justification; promotion does.

#### 7.3.1 Panel, pinning, and measurement scale

- The panel is **exactly three** independent frontier LLM judges from different vendors, version-pinned, with model identifier, version, access date, and all sampling parameters reported as in §5.6. The panel size is fixed rather than a minimum: an even panel has no majority, and a larger odd panel raises non-unanimity while leaving the single-judge posterior at margin 1 unchanged.
- **No judge may share a vendor or model family with the system whose output it is scoring on that item.** Exclusion is by family, not by brand, because judge affinity is a similarity effect rather than a self-identity effect. A judge pool of at least four is therefore maintained.
- Presentation order and position are **randomised per item**.
- Each judge is run **at least three times per item** under pinned sampling parameters, matching the discipline §5.6 applies to the systems under test. The within-judge majority is that judge's verdict; the within-judge margin and the within-judge instability rate are recorded and reported alongside the existing model-instability metric.
- The **rating scale is stated explicitly** for each scored component — binary, or ordinal with a named number of levels and written anchors. The agreement coefficient follows the scale: Gwet's AC1 for nominal or binary ratings, Gwet's AC2 with linear weighting for ordinal ratings. A threshold on a coefficient whose measurement scale is unstated is not well defined, and none is asserted here before the scale is fixed. `[DECISION 2]`
- The **verbatim judge prompt, the scoring rubric, and the anchors** are pre-registered in Appendix F before any judge is run, and any change to a pinned judge version triggers re-running the gate evaluation, with results reported for both versions.

#### 7.3.2 Verdict recording and the jury margin

For every jury-scored item, the **full per-judge vote vector** is stored, together with a derived `jury_margin` field taking the values 3–0, 2–1, or no-mode. `run_margin` is stored as a separate field, whichever way `[DECISION 3]` resolves. This is a data-capture requirement and must be settled before unblinding.

**A jury verdict exists only where the three judges are unanimous.** Non-unanimous and no-mode items are recorded as **jury-indeterminate**. This replaces the previous "majority verdict used," which had no defined behaviour for three distinct ordinal scores and which recorded a 2–1 split with the same authority as a 3–0. Under conditional independence, the posterior probability that a margin-1 majority is correct equals the per-judge accuracy — the reliability of one judge, not three; under positive dependence among judges it is lower still. A margin-1 verdict is therefore not evidence of ensemble agreement and is not treated as such.

For a component that has been promoted, jury-indeterminate items are scored by physicians under the §7.5 ladder, within a **pre-registered adjudication budget** with the priority ordering: (1) SW = 3 atypical-catastrophe items; (2) items co-occurring with a deterministic-layer critical-miss or borderline-escalation flag; (3) benign-anchor items; (4) the remainder in seeded-random order. Items falling below the budget line take the recorded majority, carry a `budget_truncated` flag, and are reported in a pre-specified sensitivity analysis. Because truncation follows hazard priority rather than chance, that sensitivity analysis is informative about the low-hazard remainder only, and is reported as such.

#### 7.3.3 Acceptance gates

**Every gate below is evaluated on a one-sided confidence bound, computed by scenario-level cluster bootstrap, and never on a point estimate.** This is a deliberate construction: a bound-based acceptance rule states no sample size, makes no power claim, and fails automatically when the achieved data cannot support the inference. It is the form in which a falsifiable acceptance criterion can be pre-registered at this revision while §8.4 remains open.

| | Gate | Quantity | Rule |
|---|---|---|---|
| **1** | **Relative** | Jury-versus-physician agreement compared with inter-physician agreement, on the same items | Jury-versus-physician agreement is at least as high as inter-physician agreement (the acceptance logic established by the NOHARM benchmark, preprint) |
| **2** | **Absolute** | The same agreement quantity | Meets a pre-registered absolute floor, fixed by §7.3.4 `[DECISION 2a]` |
| **3** | **Directional** | **Conditional false-credit rate** — of the components the blinded physician panel rates deficient, the proportion the jury rates adequate | Bounded above by a pre-registered ceiling, fixed by §7.3.4 `[DECISION 2a]` |

**The gates are conjunctive. Any component failing any gate reverts entirely to physician scoring.** No component may be promoted on aggregate performance in the presence of a gate failure, and jury delegation is **binary** — a component is either scored by the jury or it is not. The jury's contribution is never a fitted or continuous function of measured agreement, because that would carry an imprecise estimate into the scoring rule.

Two specifications that make Gate 1 mean what it says:

- **Both sides of the comparison are computed at the same aggregation level.** Either both are single blinded raters, or both are consensus-versus-held-out-rater. Comparing an adjudicated physician consensus against two raw single raters de-noises one side of the ratio and not the other, and tilts the comparison toward passing by an amount that grows as inter-physician agreement falls — that is, largest in exactly the strata this benchmark targets.
- **Where a Delphi gold label or killer-item designation exists for an item, agreement is additionally evaluated against that label, and Gate 1 must hold against both.** The Delphi standard is set before any model output exists and cannot be contaminated by that output's fluency; the scoring panel rates fluent model prose and may share the model's clinical priors. A peer-agreement test is blind to bias inherited by descent; a pre-committed-standard test is partly immune to it. Where no Delphi label exists for a component, this clause has no referent and does not apply.

Gate 3 is stated as a **conditional** rate — deficient-and-called-adequate, divided by deficient — rather than as a share of all items, because a conditional rate is invariant to how common deficient responses turn out to be, and an unconditional one is not. This is the layer's only directional criterion, and it exists because the study's scientific identity rests on an asymmetric loss function while every symmetric agreement coefficient counts the two directions of error identically.

#### 7.3.4 How the numeric thresholds are fixed `[DECISION 2]`

The thresholds for Gates 2 and 3 are **not asserted in this revision**. What is pre-registered here is the rule that fixes them, and the rule is fixed before unblinding:

- The **absolute floor for Gate 2** is derived from a stated mapping between the observed positive-class prevalence and the required threshold, evaluated on the blinded validation set. The mapping, not a number, is the pre-registered commitment. The protocol states the closed form so that any reader can see what a threshold demands: for a criterion AC1 ≥ *t*, the equivalent requirement on raw agreement is p_a ≥ *t* + (1 − *t*) · 2π(1 − π), where π is the average marginal prevalence of the positive category. At *t* = 0.75 this is p_a ≥ 0.75 + 0.5 · π(1 − π).
- The **ceiling for Gate 3** is fixed by the same procedure and before unblinding.
- No threshold imported from a benchmark scale developed for a different coefficient is used. The 0.61–0.80 and 0.75 conventions originate as verbal descriptors for kappa; no AC1-native benchmark scale exists, and because AC1 systematically exceeds kappa at skewed marginals by an amount that grows with skew, transporting a kappa cut point silently loosens it.
- **If the jury pilot is not run in this cycle, no component is promoted and the layer remains advisory for the duration of the study.** This is a safe default and requires no further action: an unpromoted component is scored by physicians, which is the status quo.

#### 7.3.5 Reported statistics

The following are reported **whether or not any gate is met**, and none of them is a gate:

- The agreement coefficient specified in §7.3.1 with its cluster-bootstrap interval, **reported alongside Fleiss or Cohen's kappa, the observed positive-class prevalence π, the implied chance term, and the raw per-cell counts.** The two off-diagonal cells are reported separately, because every symmetric agreement coefficient — AC1, kappa, Krippendorff's alpha, PABAK — is exactly invariant under exchanging them, and cannot distinguish a jury that is too lenient from one that is too strict. AC1 and kappa can also reach opposite conclusions on identical ratings when ratings are highly uniform; both are therefore reported, never one alone.
- The **jury margin distribution**, overall and stratified by severity weight and by anchor type.
- **Within-judge and between-judge instability**, and the effective panel size where a judge's verdict is unstable across runs.
- The **double-fault rate** across judges — the rate at which two or more judges err on the same item — computed **conditional on the physician or Delphi label**, and reported by severity weight alongside the rate predicted under conditional independence. Conditioning on the label is required: an unconditional excess of inter-judge agreement over the independence prediction is equally consistent with correlated judge error and with ordinary variation in item difficulty, and is therefore not interpretable as evidence of either.
- **Per-judge self-preference by model family**, together with the change in each component's score when that judge is excluded, reported with its interval.
- The **Jury–Determinism Dissociation Rate (JDDR)** — among items the §7.2 deterministic layer classifies as critical misses (no escalation phrase present and gold disposition EMS NOW or ED NOW), the proportion the jury places in the top band. JDDR requires no physician judgment at scoring time and is not physician-referenced, which is why it can detect judge error running in a direction physicians would share — the one failure mode Gates 1 to 3 are blind to by construction. Three limitations are stated with it: it inherits the operating characteristics of the deterministic layer under §4.1, so it is interpretable only once those are reported; its denominator is model-dependent and may be empty for a model that produces no deterministic critical misses; and **no numeric ceiling is pre-registered for it at this revision.**
- **Jury-versus-physician agreement by register**, as a within-scenario paired contrast. Register is fully crossed, so the paired form removes scenario variance; it is reported descriptively and carries no threshold and no reversion rule.

#### 7.3.6 Shadow mode and standing limits

Where a component is not promoted, the jury runs in **shadow mode**: verdicts are collected under the same pinning and recording rules, reported as an exploratory finding with honest cluster-adjusted intervals, and **contribute zero weight to any score**. Shadow-mode data serve two pre-registered purposes: characterising jury behaviour in the atypical-catastrophe and benign-anchor items, which converts a hypothesis about where machine scoring of clinical reasoning fails into a measurement; and estimating any systematic offset between physician-scored and jury-scored versions of the same component, so that a mixed scoring provenance cannot induce a spurious severity-by-score artefact. Where an abstention or routing rule is in force, a scoring-provenance indicator is carried into the §8.1 model and the per-model jury-indeterminate rate is reported.

Four limits stand regardless of any promotion outcome:

1. **Physicians are sovereign.** No jury verdict overrides a physician rating, and no jury output enters the physician-sovereign components of §7.4.
2. **No jury-derived quantity may enter the primary endpoint.** §4.1 and §7.2 are unchanged: the primary endpoint lives entirely in the deterministic layer, and no language model judges it.
3. **Promotion is per component and is revocable.** A judge version change, or a diagnostic in §7.3.5 that changes materially, returns the component to physician scoring pending re-evaluation.
4. **This layer is reported in full whether it is used or not.** A finding that the jury cannot be promoted is a reportable result of this study, not a failure of it.

> `[PENDING — resolved by this amendment, subject to PI approval]` This section replaces the previous pending note. The two residual gaps it identified are addressed as follows: tail concentration is addressed by shadow-mode measurement and by JDDR rather than by stratified gating, which is not estimable at this design's stratum sizes; and the 3–0 / 2–1 collapse is addressed in §7.3.2 by requiring unanimity for a jury verdict. Two items are deliberately left open and are named in the amendment memorandum: whether the jury's *reasoning coherence* and the physician-sovereign *reasoning quality in ambiguous cases* are the same construct, and the numeric values under `[DECISION 2]`.

---

## PART 5 — Consequential changes elsewhere

Discrete items. Each is a separate edit the PI can approve or decline independently.

1. **§7.2 and Table A5 — move differential-diagnosis completeness into the deterministic layer.** Score it as coverage of the Appendix B Component 5 life-threat list, by a second pre-registered phrase inventory validated by the Appendix C procedure. Table A5's jury row loses that component; the deterministic row gains it. *This is the change on which several others depend; if declined, §7.3 retains two scored components and every routing and validation burden in this amendment roughly doubles.*

2. **§4.1, §7.2, Appendix C — pre-register acceptance criteria for the deterministic layer.** Stated labelling procedure; reported operating characteristics with a confusion matrix against physician labels; a pre-registered fallback to physician ascertainment if the floor is not met; the numeric floor fixed by the same rail as §7.3.4 and **not stated at this revision**. Scope: escalation detection, killer-item detection, and — if item 1 is adopted — differential-completeness detection. *This is the single largest asymmetry the review found: the layer carrying the primary endpoint is currently ungated while the layer carrying no reported endpoint carries two gates.*

3. **Table A4 and §7.2/§7.3/§7.4 — assign a scoring layer to every endpoint.** Add a "scoring layer" column to Table A4. Anchoring Failure Rate, crisis-safeguard activation consistency, and the four interaction-failure metrics are currently assigned to no layer in the protocol body, and Table A4's method column names an actual layer only for Critical Miss Rate. Recommendation: **Anchoring Failure Rate is physician-sovereign, or deterministic against the Component 7 killer-item form already detected in §7.2 — and explicitly not jury-scored.**

4. **Table A5 and §7.2/§7.3/§7.4 — replace the percentage shares with a statement of remit, or define the composite.** No composite score is defined anywhere in the protocol; grep confirms every occurrence of "composite" refers to composite *scenarios*. No §8 analysis consumes a weighted total, and no rule states what the shares become when a component reverts. A reviewer reads "~30% of scoring weight" and concludes the jury is load-bearing, because that is what a weight means. Either define the composite and analyse it, or replace the three percentages with a statement of what each layer scores. **The second is recommended**, and it dissolves two rejected proposals at once — a stratum-dependent weight table, and a prohibition on renormalising weights that have no consumer.

5. **New §7.6 — non-load-bearing declaration.** One paragraph: no endpoint reported in the primary or secondary results depends on the LLM jury layer; every analysis in §8 is computable from the deterministic and physician-sovereign layers alone; all results are reported with and without jury-derived components, and any material divergence is itself reported as a finding. *Conditional on item 3: without the endpoint-to-layer map the declaration is falsifiable from the same document.*

6. **§5.6 — extend pinning, repeated runs, and the instability metric to the judges.** Within-judge majority as that judge's verdict; within-judge margin recorded; judge instability reported alongside model instability. Add a judge-version change-control clause: any substitution, deprecation, or version change re-runs the gate evaluation, with results reported for both versions, and a named contingency if a pinned judge is deprecated inside the weeks 10–12 evaluation window.

7. **§5.6 and §8.1 — record run margin and jury margin as separate stored fields**, whichever way DECISION 3 resolves. Zero cost, decided now rather than after unblinding, and it makes every parameter assumed in this analysis estimable from the study's own data.

8. **§7.5 — name the jury-indeterminate route into the existing ladder**, and state that the adjudication budget in §7.3.2 caps it. No new adjudication machinery is created; the existing two-rater / third-rater / Delphi ladder absorbs the traffic.

9. **§8.2 — add the reported agreement set.** AC1 or AC2 with cluster-bootstrap interval, reported alongside kappa, the observed prevalence, the chance term, and the raw per-cell counts, with a pre-registered note that AC1 and kappa can reach opposite conclusions on identical ratings. Add the double-fault statistic and the register paired contrast. Remove nothing: §8.2's existing choice of AC1-primary for *reliability reporting* is correct and is unaffected; what changes is that AC1 no longer serves as an acceptance threshold.

10. **§8.1 — add a scoring-provenance covariate** (`jury_indeterminate`), report the per-model indeterminate rate as a secondary endpoint, and pre-register the jury-versus-physician calibration offset estimated on unanimous items. State the limitation: the offset is estimated where the jury is confident and applied where it is not, so it bounds the bias only under an assumption of constant offset across the margin; report it separately by margin where the data allow.

11. **§5.2 and Appendix B.3 — pre-specify the severity distribution of the 50 scenarios.** B.3 currently pre-specifies syndrome coverage and says "exact distribution flexible," so the SW = 3 denominator is a free parameter fixed post hoc by the authoring panel. That blocks pre-registration of any severity-stratified analysis and makes the Failure Severity Index weighting non-reproducible. **This is independent of the jury question, it is a design-composition constraint rather than a power figure, and it is time-critical: it must land before scenario authoring opens in week 2.** *Correction to carry: the "share of scenarios versus share of the FSI" illustration circulating in the analysis assumes equal error rates across severity strata, which the study's own hypothesis denies. The reproducibility argument stands on its own; the amplification figure does not.*

12. **§7.3 citation, §13, and CONTEXT_MEMORY §4 — provenance corrections.** Label NOHARM as a preprint per the protocol's own §13 rule; pin its version and access date given the title and author-order divergence across versions; and remove the κ = 0.804 / 0.784 figures unless retrieved from the PDF, replacing them with the retrievable NOHARM findings (omission accounting for 76.6%, 95% CI 76.4–76.8%, of errors; potential for severe harm in up to 22.2%, 95% CI 21.6–22.8%, of cases; and a diverse multi-agent approach improving safety over solo models, mean difference 8.0%, 95% CI 4.0–12.1% — noting that the last concerns multi-agent *answering*, not judging). Separately, strike the "Afrasyab, inter-judge Fleiss κ = 0.65" figure from CONTEXT_MEMORY §4 and from the reasoning behind the pending note; it is unverifiable, not merely secondary-source. Grep confirms it does not appear in the protocol text, so this is a project-record correction only.

13. **New Appendix F, and §14 — the judge prompt and rubric.** Appendix C covers the escalation phrase inventory and Appendix D the subject-model prompt; nothing carries the *machine assessor's* instructions. TRIPOD-LLM (Gallifant et al., *Nat Med* 2025;31(1):60–69, PMID 39779929, doi 10.1038/s41591-024-03425-5 — citation verified bibliographically; the two verbatim quotations circulating in this analysis could **not** be confirmed from any source reachable here and should be checked against the PDF before being quoted to a reviewer) has reporting items for assessor instructions and prompt-engineering methods, which a reviewer will apply by analogy to a machine assessor.

14. **§13 — add a preprint-evidence rule.** This amendment's evidence base is substantially preprint. State the rule the protocol's own citation policy already implies: **preprint evidence may motivate a design choice; it may not supply a pre-registered numeric threshold.** That rule is what makes §7.3.4's deferral principled rather than evasive.

15. **§7.4 / §6.1 / §12 — resolve whether physician scoring is exhaustive or applied to a pre-specified sample.** §7.4 does not say. When the load implied by §7.4 is worked against the §6.1 per-participant commitment, the two-week weeks 16–18 window, and §5.4's non-overlapping-panel rule, the three sections may not be mutually consistent as written. This is a **live filing risk independent of the jury question**, and it is also the precondition for naming the adjudication budget in §7.3.2. Recommendation: state the answer in §7.4 and reconcile. *No participant or hour counts are given here: the underlying arithmetic depends on the number of models, which §5.5 does not state, and on the unverifiable κ, so the finding is reportable but the specific counts are not.*

### Effect on the open PI decisions

**DECISION 2 — Gwet AC1 ≥ 0.75. This recommendation constrains it decisively and I recommend the PI does not confirm it as written.** Four independent grounds, three of them verified arithmetic reproduced by two refuters: the criterion is satisfied by a jury with zero sensitivity on the flagged class once that class is rare (subject to the jury not over-flagging, which a lenient jury by definition does not); it cannot distinguish a lenient jury from a strict one; the number has no AC1-native provenance; and the same number, read as an *inter-judge* criterion, would condemn an excellent independent jury while licensing a failed one — at plausible skew, the independence-predicted inter-judge AC1 for a jury of highly accurate judges falls *below* 0.75.

**One honest conditionality the PI must see.** The vacuity result depends on a parameter nobody has measured. Two lenses built it on the assumption that the jury's flagged class is rare; a third argued persuasively that this skew belongs to the deterministic layer's safety tags, and that the jury's graded rubric judgments have no reason to be skewed at all. At balanced marginals the criterion demands high raw agreement and the vacuity argument largely closes. Both cannot be right. **That contradiction is the argument for measuring the parameter rather than replacing one asserted number with another.**

Recommended resolution: **split DECISION 2 into two pre-registered parameters, and close both at filing at the level of form rather than value.**
- **DECISION 2a — the jury-versus-physician acceptance thresholds** (Gates 2 and 3). Closed at filing by pre-registering the mapping and the rule in §7.3.4, with the numeric values fixed on the blinded validation set before unblinding. This is falsifiable, pre-registered, and states no sample size.
- **DECISION 2b — the inter-judge agreement band.** The PI's candidate inversion is right in principle: a jury agreeing with itself far more than physicians agree with each other is exhibiting shared bias, not accuracy. It is retained as a **reported diagnostic** in §7.3.5, not as a gate, and its comparator is derived from measurement rather than asserted. The specific band that two lenses converged on is rejected (PART 3, item 6) because its calibration anchor was misread and, corrected, points the other way.

*Note on the filing-blocker objection.* Two refuters warned that deferring DECISION 2 to pilot data converts a one-blocker filing problem into a two-blocker one. The construction above answers that: **DECISION 2 closes at filing.** What defers is a number on a pre-registered rail, and the fallback if the pilot is never run is the safe default — no component is promoted, the layer stays advisory, and physicians score what they were always going to score.

**DECISION 3 — majority-of-three runs versus first-run-primary. This recommendation does not resolve it, but it supplies one input the PI should have before deciding, and one requirement that holds either way.** The input, offered as decision support and not as a result: majority-of-three runs and majority-of-three judges are the same failure mode on two axes, and they stack — a margin-1 run collapse feeding a margin-1 jury collapse, both reported as confident. First-run-primary removes the run margin from the primary analysis entirely and leaves it as the instability endpoint, which is what §5.6 already says the intent is; it is also materially cheaper for every routing rule in this amendment. **This is a mild preference on internal-consistency grounds, not a recommendation, and the PI may reasonably decide it on other grounds.** If majority-of-runs is adopted, the §7.3.2 routing trigger becomes disjunctive — route if the runs split *or* the jury splits — and the adjudication budget must be sized for the larger load. The requirement holding either way is PART 5 item 7: record the two margins as separate fields.

**DECISION 1 and DECISION 4** are untouched by this amendment, except that any bias-cue variants adopted under DECISION 1 become a named reporting stratum for shadow mode rather than a gating stratum.

---

## PART 6 — Open questions this amendment does not close

1. **Are "reasoning coherence" and "reasoning quality in ambiguous cases" the same construct?** §7.3 delegates the first to machines; §7.4 says the second is "never delegated to models." Gate 1 requires physicians to rate the jury's component — a construct §7.4 does not list and the §7.5 ladder was not designed for. If the two are the same, the jury is scoring something physicians already score sovereignly, and the right amendment is a **merge**, not a gate. If they are different, low jury–physician agreement may be construct mismatch rather than judge failure, which is a **validity** threat prior to every reliability statistic in this amendment. Two refuters raised this independently and neither this amendment nor any lens answers it. **This is the question I would put to the PI first**, because a merge would moot most of §7.3 and is cheaper than everything proposed above.

2. **The positive-class prevalence of the jury's judgments is unknown, and the central quantitative argument is conditional on it.** Stated above under DECISION 2. The amendment handles it by pre-registering a mapping rather than a value, but that is a construction that survives ignorance, not one that resolves it.

3. **The split rate is unknown, and every cost estimate depends on it.** How often three judges will disagree on this study's own material has never been measured on anything resembling this task. The one figure the project has been using is unverifiable; the nearest peer-reviewed alternative was measured on mid-size open-model generators judging discharge-note coherence, which does not transfer. The amendment therefore records the margin, caps the routing, and states no rate. If the rate turns out to be high, the honest finding may be that the jury layer is not worth its complexity — a legitimate outcome that the protocol should be willing to report.

4. **Whether the jury pilot happens at all, and on what path.** The amendment's deferral rail assumes some pre-unblinding measurement of the jury's behaviour. §8.4 already names an absent pilot as the single largest obstacle to filing, and this amendment deliberately does **not** add a second pilot dependency — but it does not create the first one either. If no pilot is run, no component is promoted. The PI should decide whether that is the intended outcome or an accident.

5. **How large the validation sample must be, and who rates it.** Deliberately unanswered under §8.4. Two facts the PI should nonetheless hold: physicians do not currently rate the jury's components anywhere in §7.4, so every validation rating is net-new work with its own rubric and its own training cost; and §7.3 does not say whether the validation sample is drawn from, disjoint from, or nested in the scored corpus, nor how §5.4's non-overlapping-panel rule constrains who may rate it. Agreement estimated on items whose gold labels the same raters produced is not the same estimand as agreement on held-out items.

6. **Whether the tail-concentration premise is true of judges at all.** The evidence that LLM *answerers* degrade under benign anchors and misleading cues is strong and verified. The evidence that LLM *judges* degrade specifically in high-hazard strata is thinner. Shadow mode is the amendment's answer, and it is an answer by measurement rather than by argument — which is honest, but it means the premise motivating the whole amendment remains an assumption until the study reports.

7. **What happens if one jury component passes and another fails.** Item 1 of PART 5 largely dissolves this by reducing the jury to a single component. If the PI declines that change, §7.3's per-component reversion rule and Table A5's single joint share are inconsistent, and the protocol does not say how the share divides. Every per-component gate makes a split outcome more likely without supplying the arithmetic for it.

8. **Arms B and C scoring load is not costed anywhere.** The physician-burden observation in PART 5 item 15 is derived from Arm A alone. Arm B's answering panel produces responses the same scoring panel must score on the same components, and Arm C generates four free-text interaction-failure metrics currently assigned to no scoring layer at all. Any burden reconciliation that omits them will be wrong in a known direction.

9. **Whether reasoning coherence needs machine scoring at all.** Once differential-diagnosis completeness moves to the deterministic layer, the residual jury is one component. It is a one-paragraph question whether that residue is small enough to delete outright rather than validate — and deleting it would moot §7.3.3 through §7.3.5 entirely. **Nobody in this analysis costed the null option**, and the PI should be told that plainly: the comparator against which this whole amendment should be judged is "physicians score reasoning coherence outright, and the jury is deleted." That comparison was not run, and it could be run in an afternoon once PART 5 item 15 resolves.

---

## APPLICATION NOTE — 29 August 2026

PART 4 was applied verbatim with one substitution and three forced reconciliations. Everything else
in PART 5 remains open.

**Substitution.** PART 5 item 1 (moving differential-diagnosis completeness into the deterministic
layer) was not approved, so the single `[conditional]` clause came out as this memorandum specifies
and §7.3 retains **both** scored components. Every rule in the new section applies per component.

**Forced reconciliations** — made because the approved §7.3 text would otherwise contradict the
document around it, not as independent edits:

1. **§0 register, DECISION 2.** The approved §7.3.3 carries `[DECISION 2a]` markers and §7.3.5
   demotes AC1 to a reported statistic, so the old row ("Confirm Gwet AC1 ≥ 0.75 as the promotion
   threshold") would have dangled and contradicted §7.3. Split into **DECISION 2a** (the
   threshold-setting rule) and **DECISION 2b** (inter-judge agreement band as a reported
   diagnostic), with the old AC1 ≥ 0.75 row struck through and marked retired, with the reason.
2. **§14 appendix register.** §7.3.1 requires the judge prompt, rubric, and anchors to be
   pre-registered in **Appendix F**. An F row was added with status "To be pre-registered before any
   judge is run (§7.3.1)", matching how C, D, and E are already carried. No appendix content was
   written.
3. **Table A5, jury row.** Still read "≥3 judges, majority verdict; two acceptance gates", which the
   approved §7.3 contradicts. Updated to: exactly three judges, each run ≥3 times, unanimity
   required for a verdict, three conjunctive gates on confidence bounds, shadow mode when not
   promoted.

**Deliberately NOT changed.** The "~40% / ~30% / ~30%" weights in §7.2, §7.4, and Table A5 stand —
revising them is PART 5 item 4, not approved. Carry PART 6 item 7 forward: with two jury components
retained, the per-component reversion rule and Table A5's single joint share are not fully
reconciled, and the protocol does not state how the share divides when one component reverts and the
other does not.
