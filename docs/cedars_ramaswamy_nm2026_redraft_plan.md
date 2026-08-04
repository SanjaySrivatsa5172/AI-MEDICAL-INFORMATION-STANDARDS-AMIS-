# Ramaswamy et al. (Nat Med 2026) — Verification Record and Redraft Plan

**Applies to:** Protocol v2 (+ Amendment 1, Addendum A) and `Cedars_Onboarding_Aug7.pptx`
**Prepared:** 2026-08-04, ahead of the Friday 2026-08-07 Teams meeting (Farkouh / Spiegel)
**Verification status:** Citation and all headline figures independently verified against PubMed and Scite full-text excerpts on 2026-08-04. Safe to cite. No corrections, errata, or retractions on record; 43 citing publications already indexed.

---

## 1. Verification record (citation ledger entry — VERIFIED)

**Citation.** Ramaswamy A, Tyagi A, Hugo H, Jiang J, Jayaraman P, Jangda M, Te AE, Kaplan SA, Lampert J, Freeman R, Gavin N, Tewari AK, Sakhuja A, Naved B, Charney AW, Omar M, Gorin MA, Klang E, Nadkarni GN. ChatGPT Health performance in a structured test of triage recommendations. *Nat Med*. 2026;32(5):1671–1675. doi:[10.1038/s41591-026-04297-7](https://doi.org/10.1038/s41591-026-04297-7). Epub 2026-02-23. PMID 41731097; PMC13190235. Open access (CC-BY) — download the PMC PDF into the project reference library. Icahn School of Medicine at Mount Sinai (Windreich Department of AI and Human Health; senior author G. Nadkarni).

**Design facts (from abstract + full-text methods excerpts):**

- 60 clinician-authored vignettes, 21 clinical domains; 16 factorial conditions varying patient race, sex, anchoring context, and access barriers; 960 total responses. 960 = 60 × 16, implying a single response per vignette–condition cell; no repeated-run variability was reported.
- Vignettes split 30 "clear" cases (single correct gold-standard level) and 30 "edge" cases (a range of two adjacent levels accepted).
- Gold standard assigned by three physician-investigators (A.R. and M.A.G., urology; H.H., internal medicine), guideline-anchored, Fleiss κ = 0.90 (95% CI 0.88–0.92). The raters overlap with the study team; there is no independent physician answering arm.
- Triage scale: 4-level Likert — A "monitor at home" / B "see a doctor within weeks" / C "see a doctor within 24–48 h" / D "go to the emergency department." The scale's ceiling is ED self-transport; EMS activation is not distinguished.
- Within-vignette factorial design (each vignette its own control). Single product (ChatGPT Health), single timepoint.

**Verified result figures — keep denominators straight when citing:**

| Figure | Precise meaning |
|---|---|
| 35% / 48% | Failure rates at the clinical extremes (nonurgent 35%, emergency 48%) — the inverted-U pattern |
| 52% | Share of gold-standard **emergencies undertriaged** (e.g., DKA, impending respiratory failure directed to 24–48 h evaluation); classical emergencies (stroke, anaphylaxis) triaged correctly |
| OR 11.7 (95% CI 3.7–36.6) | Triage shift when family/friends **minimized symptoms** (anchoring); majority of shifts toward less urgent care; **significant in edge cases only, not clear cases** |
| 64.8% (83/128) | Nonurgent responses overtriaged (clear-vignettes subset, n = 480), predominantly by one level; none sent to ED. Different denominator from the 35% abstract figure — use abstract-level numbers in the protocol unless citing Fig. 1 specifically |
| Crisis safeguards | Activated unpredictably across suicidal-ideation presentations; **more often when no method was described than when one was** |
| Race / sex / access barriers | No significant effects, but CIs did not exclude clinically meaningful differences |

**Their own stated limitations (quotable):** vignettes rather than real-world patient interactions; single timepoint and single product ("model behavior may change with updates, only underscoring the need for ongoing evaluation"); closing argument that consumer triage AI "should not be deployed on trust alone" and warrants prospective validation.

**Do NOT propagate from the scan without verification:**

- "First independent safety evaluation of ChatGPT Health" — primacy is the scan's phrasing, not the paper's. Same discipline as the *Winters* "first suit" rule: write "a landmark independent evaluation," not "the first," unless primacy is separately verified.
- The scan's **+9 additional references** (physician-vs-LLM ED vignette study, ESI meta-analysis, red-teaming/adversarial papers, AMIE ambulatory study, ChatGPT/Gemini/DeepSeek comparison, ID triage scoping review) are **unverified** — queue each through the same PubMed check before citing anywhere. The linked scan session could not be opened from this session (authentication-blocked).
- Two other 2026 "Ramaswamy" PMIDs surfaced in search (42420335, 42024827) are unrelated authors (CT imaging; canine olfaction) — not correspondence on this paper. As of 2026-08-04 there is no published reply or correction to engage with.

---

## 2. Strategic read: validation, not a scoop

The paper proves the premise and leaves the instrument unbuilt. Every differentiator on our list survives contact with their methods, and three of their acknowledged limitations are literally arms or design features of this protocol (physician answering benchmark; human–LLM interaction arm; repeated runs / ongoing multi-model evaluation). Their closing sentence is an argument for funding this trial.

The risk it creates is rhetorical, not scientific: Farkouh and Spiegel will likely know this paper (Mount Sinai; Farkouh's former institution), and every reviewer will ask "how does this differ from Ramaswamy?" That answer must be pre-drafted in the protocol background, the methods, the deck, and the Friday talking points — never improvised.

The narrative upgrade is the **three-pillar structure**:

1. **Allegation** — *Winters v. OpenAI*: the disposition-failure phenotype in the wild (reassurance, invented threshold, advised immobility). Still presented as allegations.
2. **Measurement** — Ramaswamy: the same phenotype measured under controlled conditions in the deployed product (52% of emergencies undertriaged; anchoring OR 11.7; crisis safeguards unpredictable).
3. **Interaction gap** — Bean / Goh / Healy: whatever a model does alone degrades further in lay users' hands.

An allegation, a measurement, and an interaction gap — and still no standard instrument. This protocol supplies it.

---

## 3. Protocol redraft — itemized edits

### 3.1 Three now-falsifiable absolutes to fix (highest priority)

These sentences in the current Scientific Introduction are contradicted by a paper every reviewer will know. They must not survive into the IRB submission:

1. **"Every published large language model triage study to date has used either the ESI Implementation Handbook's freely available case library or synthetic vignettes derived from published sources."** (Scientific Foundations, third incompatibility.)
   → Revise: "Until 2026, every published LLM triage study used either the ESI Implementation Handbook's freely available case library or synthetic vignettes derived from published sources. The recent ChatGPT Health evaluation (Ramaswamy et al.) is the notable exception — its 60 vignettes were clinician-authored de novo, an approach this protocol shares and extends. No published evaluation, however, has embedded contamination-*detection* items to measure memorization effects directly rather than assume their absence."

2. **"The results of this study will generate evidence that does not currently exist in any form."** (Consequences section.)
   → Revise: "The first product-level measurements now exist — and they confirm the danger (Ramaswamy et al., 2026). What still does not exist is the standard-setting instrument: a multi-model, physician-benchmarked, severity-weighted, contamination-audited, interaction-inclusive evaluation that can be reapplied as models change. This study supplies it."

3. **"No published LLM triage study has implemented this separation."** (Arm B rationale — still true, now strengthen rather than soften.)
   → Extend: "No published LLM triage study has implemented this separation. In the most recent ChatGPT Health evaluation, the physicians who set the gold standard were study investigators, and no independent physician panel answered the scenarios under the model's informational constraints; the human role was adjudication only. The present design separates authoring, gold-standard determination, answering, and scoring into four non-overlapping panels."

### 3.2 New subsection to insert after the four incompatibilities — paste-ready draft

> **The Closest Prior Work — and What It Leaves Unbuilt**
>
> In February 2026, the first product-level evidence arrived. Ramaswamy and colleagues at Mount Sinai published in *Nature Medicine* a structured stress test of ChatGPT Health — OpenAI's consumer health product, launched the previous month — using 60 clinician-authored vignettes across 21 clinical domains under 16 factorial conditions (960 responses). The results independently confirm this protocol's central premise. Performance followed an inverted-U pattern, failing most often at the clinical extremes: 48% on emergency conditions and 35% on nonurgent presentations. Among gold-standard emergencies the system undertriaged 52% of cases — directing presentations such as diabetic ketoacidosis and impending respiratory failure to 24–48-hour evaluation rather than the emergency department — while triaging classical, pattern-complete emergencies such as stroke and anaphylaxis correctly. When family members minimized symptoms, recommendations shifted toward less urgent care in edge cases (OR 11.7, 95% CI 3.7–36.6). Crisis-intervention safeguards activated unpredictably across suicidal-ideation presentations, firing more often when no method was described than when one was. This is the disposition-failure phenotype — delayed escalation under benign framing — measured under controlled conditions in the deployed product.
>
> What Ramaswamy et al. establish is the danger; what they leave unbuilt is the standard. Their evaluation tested a single product at a single timepoint, with one response per vignette–condition cell, so run-to-run nondeterminism was not measured. Triage was scored on a four-level scale whose ceiling is "go to the emergency department," without distinguishing EMS activation from self-transport — the boundary at which safety-critical instructions ("call 911; do not drive") operate, and the boundary at issue in *Winters*. The gold standard was assigned by three physician-investigators drawn from urology and internal medicine, with no independent physician answering arm responding under the model's informational constraints. Presentation register was not an experimental factor. Errors were tallied without severity weighting, pre-specified killer items, or time-to-escalation. Contamination was mitigated by novel authorship but not directly audited. And — as the authors themselves note — no human–AI interaction was tested. Each of these gaps is a designed feature of the present protocol: multi-model, version-pinned evaluation with repeated runs and a run-instability metric; a five-level disposition scale separating EMS from ED; four-way physician role separation with an independent emergency-physician answering benchmark; dual lay/expert register as a crossed factor; severity-weighted Critical Miss Rate with killer items and time-to-escalation; embedded contamination-detection items; and a human–LLM interaction arm. Ramaswamy et al. close by arguing that consumer triage AI "should not be deployed on trust alone" and requires prospective, ongoing evaluation. This protocol is the instrument that argument calls for.

### 3.3 Background (Amendment 1 Change 1 refresh) — paste-ready three-pillar paragraph

> Three converging lines of evidence now define the safety problem this trial measures. First, the failure phenotype has surfaced in the wild: *Winters v. OpenAI* alleges that a consumer chatbot met an evolving venous thromboembolism with reassurance, invented a clinical threshold, and advised immobility — a disposition failure, not a diagnostic one. Second, the phenotype has now been measured under controlled conditions in the deployed product: an independent Mount Sinai evaluation of ChatGPT Health found 52% of gold-standard emergencies undertriaged, recommendations shifting toward less urgent care when family members minimized symptoms (OR 11.7, 95% CI 3.7–36.6), and crisis safeguards activating unpredictably (Ramaswamy et al., *Nat Med* 2026). Third, the deployment interface degrades performance further: in Bean et al.'s randomized evaluation, models that identified conditions at 94.9% in isolation fell below 44.2% disposition accuracy in lay users' hands — no better than control — and physician-side gains from LLM assistance have been similarly marginal (Goh et al.; Healy et al.). An allegation, a measurement, and an interaction gap — and still no standard instrument: no published evaluation combines physician-authored, contamination-audited scenarios; an independent physician answering benchmark; severity-weighted disposition scoring; and a human–AI interaction arm. This protocol supplies that instrument.

### 3.4 Comparison table (protocol appendix and/or deck slide)

| Dimension | Ramaswamy et al. 2026 | This protocol |
|---|---|---|
| Systems | ChatGPT Health only, single timepoint | ≥6 frontier models, version-pinned, reusable longitudinally |
| Runs | 1 response per condition cell; nondeterminism unmeasured | Triplicate+ runs; majority call + run-instability metric |
| Scale | 4-level (ceiling "go to ED"); EMS not distinguished | 5-level disposition incl. EMS-vs-ED split and do-not-drive instructions |
| Gold standard | 3 physician-investigators (urology ×2, IM), guideline-anchored, κ 0.90 | Emergency-physician modified-Delphi panel; escalation threshold + killer items |
| Human comparator | None (adjudication only) | Independent physician answering arm under identical constraints |
| Register | Not manipulated | Dual lay/expert register as crossed factor |
| Scoring | Symmetric level match (under/over reported separately) | Severity-weighted CMR, FSI, TTE, killer items, asymmetric credit |
| Contamination | Mitigated by novel authorship; not audited | Novel composites + embedded detection items (measured, not assumed) |
| Interaction | None (stated limitation) | Arm C human–LLM interaction (+ exploratory longitudinal C1) |
| Bias probes | 4 factors incl. proxied family-minimization anchoring | Cue taxonomy with locus manipulation (none / note-embedded / user-asserted) + directional control (Change 12) |

### 3.5 Endpoint and decision consequences

**Keep Critical Miss Rate primary. Do not promote Anchoring Failure Rate to primary or co-primary** (contra the scan's suggestion), for four reasons: (1) CMR is the construct the entire architecture — killer items, severity weights, asymmetric scoring — is built to serve; switching primaries days before leadership review reads as reactive. (2) A co-primary splits alpha and weakens the headline comparison. (3) The OR 11.7 has a CI of 3.7–36.6, comes from the edge-case subset of a different scale and design, and is unusable as a formal power anchor. (4) Addendum A's rule stands: no power figures for cue analyses without pilot discordance data.

**Adopt Change 12 this cycle** — this is the decision Ramaswamy actually tips. Their result (a) confirms conversational-locus anchoring is real and large exactly at the triage boundary, (b) shows it is significant *only in edge cases*, validating both our boundary-targeting scenario design and the matched-pair McNemar approach (discordance concentrates where cases are hard), and (c) leaves the note-embedded cue locus entirely unexamined — H12b is untouched territory. Use OR 11.7 qualitatively as motivation and to set pilot expectations; state explicitly in the protocol that it is not a power input. Slide-27 speaker notes already promise authors will be told before drafting if Change 12 is adopted — adopting now, before Friday, keeps that promise cleanly.

**Add one exploratory endpoint: crisis-safeguard activation consistency** across matched suicidal-ideation presentations (method stated vs not), directly extending their inverted-activation finding. Fits the existing Psychiatric/Toxicologic scenario category; pre-specify as descriptive/exploratory to avoid scope bloat.

**Over-triage / operating point:** their nonurgent-extreme failures externally motivate Addendum A's universal-referral-rate reporting per configuration (scaffold benefit must be an operating-point shift, not indiscriminate referral) and the retention of reassurance-appropriate cases in the instrument.

**Statistics section, one sentence each:** (a) their race/sex/barriers nulls with wide CIs justify our matched-pair (McNemar / conditional logistic) design over between-condition factorial contrasts — power per contrast; (b) their single-response-per-cell design is the published illustration of why we run triplicates with a majority call and report run-to-run agreement (supports the majority-of-three decision, another open PI item).

---

## 4. Onboarding deck changes (`Cedars_Onboarding_Aug7.pptx`) — slide-level

1. **New evidence slide, Part II** (place first in the evidence block, before Bean):
   - **Title:** "February 2026, *Nature Medicine*: the deployed product fails exactly where this trial looks"
   - **Three callouts:** 52% of gold-standard emergencies undertriaged (DKA → "see a doctor in 24–48 h") · Anchoring OR 11.7 when family minimized symptoms · Crisis safeguards fired unpredictably — more often when *no* method was stated
   - **Footer:** Ramaswamy et al., Mount Sinai. Nat Med 2026;32(5):1671–75. Single product, single timepoint, no physician comparator.
   - **Speaker notes:** classical-vs-atypical split (stroke/anaphylaxis correct; DKA/impending respiratory failure missed) is the Key-Features thesis appearing in the wild data — models pass the pattern-complete cases and fail where the killer items live. Anchoring effect significant only in edge cases — exactly the boundary our scenarios target. 43 citing papers in ~5 months: the space is moving.

2. **New differentiation slide, Part III/IV seam:** compressed 6-row version of the §3.4 table. **Title:** "They measured the product. This trial builds the standard." Preempts the scooped question in the room rather than answering it defensively.

3. **Slide 27 (protocol updates):** move Change 12 from "pending pilot data" to "recommended: adopt — Ramaswamy confirms conversational-locus anchoring (OR 11.7, edge cases); note-embedded locus unexamined; power still gated on pilot discordance." Add Ramaswamy to the amendment-evidence lineage (Winters + SymptomAI → Amendment 1; Ramaswamy → this cycle).

4. **2026-context slide (Part I):** add one line — ChatGPT Health launched Jan 7, 2026; first major independent evaluation published Feb 23, 2026 showed 52% emergency undertriage. The problem is no longer only alleged; it is measured.

5. **Part V ask:** urgency framing — the evaluation-standard slot is open and the field is citing Ramaswamy at speed; Cedars can own the standard. (Verbal, not on slide: "Mount Sinai showed the failure; Cedars defines the standard" — lands well given the room.)

6. **Talking points card for Friday (3 lines):**
   - "The Nature Medicine paper is our premise, peer-reviewed — it found the exact failure mode our trial is built to measure, in the product with the most users."
   - "It tested one product, once, with no physician comparator, no severity weighting, no EMS/ED distinction, and no interaction arm — every one of those is an arm or design feature of ours."
   - "Its authors' own conclusion — 'should not be deployed on trust alone,' needs prospective ongoing evaluation — is a description of this protocol."

---

## 5. Ledger and process actions

1. Enter §1 into the verified-anchor ledger; file the PMC13190235 CC-BY PDF in the project reference library.
2. Queue the scan's +9 references for individual PubMed verification before any appear in protocol, deck, or manuscript.
3. Run a one-time retrospective sweep of the 43 papers already citing Ramaswamy (Scite) for further design-overlap items — the paper is from February; a CRITICAL flag arriving in August means the scan's recall needs a look back.
4. Primacy discipline: "a landmark independent evaluation," not "the first," until verified.
5. When the *Winters* docket citation is finally obtained, the background paragraph in §3.3 takes it in the first pillar — structure already accommodates it.
