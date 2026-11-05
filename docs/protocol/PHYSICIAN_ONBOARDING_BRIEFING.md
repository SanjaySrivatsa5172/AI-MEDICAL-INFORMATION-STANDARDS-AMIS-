# Why This Study, and Why Now

## A Scientific Briefing for Reviewing Physicians

**Study:** LLM Safety and Medical Reasoning Assessment\
**Principal Investigator:** S. Sanjay Srivatsa, MD, FACC, FSCAI, MRCP (London), DABVLM\
**Version:** 1.0 — 21 August 2026\
**Companion documents:** Consolidated Research Protocol v3; Scientific Introduction v3

---

*This briefing is written for physicians reviewing the protocol who are not specialists in artificial
intelligence and have no reason to be. It explains what the study asks, why the existing literature
does not answer it, what is methodologically new, and what the results would change. It assumes
clinical fluency and no technical background.*

---

## 1. The question

A patient develops symptoms at eleven at night. Before calling anyone, before waking a spouse, they
type what they are feeling into a chatbot and ask the question that determines everything that
follows:

> *Do I need to go to the emergency room?*

This now happens millions of times a day. The systems answering — ChatGPT, Claude, Gemini and their
successors — were not designed as triage instruments, were never validated against emergency medicine
standards, and operate under no regulatory framework governing their safety in this role. They
nonetheless function as de facto triage for a growing share of the population.

The study asks one operationally precise question: **when patients describe symptoms in everyday
language to a large language model, does the model reliably recognize presentations requiring
emergency care?**

That is a clinical question, not a technology question. It is answerable by the ordinary methods of
clinical research, and it has not been answered.

---

## 2. Why the existing literature does not answer it

The dominant paradigm for evaluating medical AI tests whether a model can answer medical knowledge
questions — board-style items from USMLE, MedQA, MedMCQA. Models now score extremely well on these.
OpenAI's o1 has reached approximately 96% on USMLE Step 1 items.

**This measures the wrong construct.** A model that recalls medical facts under examination conditions
has demonstrated recall under examination conditions. It has not demonstrated the capacity to
recognize that a 74-year-old diabetic man describing fatigue, nausea, and exertional dyspnea — with no
chest pain — needs an emergency department now.

Every physician reading this knows the difference between the two abilities. The literature has, until
recently, largely elided it.

That gap is no longer a matter of argument. In the NOHARM benchmark, models' clinical-safety
performance correlated only **moderately with their scores on existing knowledge benchmarks
(r = 0.61–0.64)**. A model can excel on accuracy evaluations and still produce severely harmful
recommendations at nontrivial rates. Accuracy and safety are measurably different axes, and only one
of them has been measured for consumer-facing triage.

### The three failures of transfer

**Format.** Most benchmarks present answer options. Real patients receive prose. When a model must
choose among five listed dispositions, the task bears little resemblance to generating advice
unprompted — and the difference is not cosmetic. A 2026 replication argued that the forced-choice
format of a widely reported *Nature Medicine* evaluation manufactured much of its headline failure
rate: models scoring 0–24% under forced choice recommended emergency care in their own words 100% of
the time on matched scenarios. That dispute is unresolved, and it is a dispute about measurement, not
about models.

**Contamination.** Published case libraries — including the freely available Emergency Severity Index
Implementation Handbook cases — are in training data. A model may be reciting rather than reasoning,
and no published triage evaluation has measured this directly rather than assumed it away.

**Register.** Benchmarks are written in clinical language. Patients do not speak clinical language.
They say "my stomach feels off," not "I have epigastric discomfort." Whether a model that performs
well on a structured vignette performs equally well on the same case described by a frightened person
at two in the morning is an empirical question that nobody has asked systematically.

---

## 3. Why triage, specifically

Emergency triage has a property that makes it the right place to look, and that almost no AI benchmark
respects: **the harms are asymmetric.**

When triage errs toward caution — sending a patient with benign chest wall pain to the ED — the cost is
inconvenience, resource use, and modest expense. When it errs the other way — reassuring a patient
whose thunderclap headache is a subarachnoid hemorrhage — the cost may be death within hours.

This is not an incidental feature. It is the organizing principle of the Emergency Severity Index, and
the American College of Surgeons codifies it numerically: trauma systems target **under-triage below
5% while tolerating over-triage as high as 35%**. A seven-fold asymmetry, deliberately chosen.

Nearly every AI medical benchmark scores these two error types identically. A model that sends
everyone to the ED and a model that sends no one score the same as a model that is wrong in both
directions equally often. **That is not a measurement of safety. It is a measurement of accuracy
wearing safety's clothes.**

The disposition decision is also, clinically, the decision that kills. Diagnostic imprecision is
usually recoverable; a missed disposition is frequently not. This study measures the disposition axis
directly, weighted by harm.

---

## 4. What is methodologically new

Seven design decisions distinguish this study. Each addresses a specific, identifiable failure in the
existing evidence.

**Dual register.** Every scenario exists twice: as a lay patient narrative and as a structured expert
triage vignette, clinically identical. This is a deliberate distribution-shift probe. If a model
performs well on the vignette and poorly on the narrative, the model is not safe for consumer
deployment regardless of its benchmark scores — because consumer deployment is entirely in the lay
register.

**Key features methodology.** Scenarios are scored using the Key Features approach developed by the
Medical Council of Canada for national licensing examinations. Credit attaches only to the two to four
decision points on which the case actually turns — not to peripheral correctness. A response can be
articulate, well-organized, largely accurate, and still fail, because it missed the thing that
mattered. That is the correct standard for triage.

**Killer items and severity weighting.** Each scenario pre-specifies statements that constitute
automatic failure — attributing a dangerous presentation to a benign cause without recommending
evaluation, advising rest at home, telling a patient to drive themselves when EMS is indicated. Errors
are weighted 1 to 3 by time-to-harm. A missed subarachnoid hemorrhage does not score the same as a
missed ankle sprain.

**Four non-overlapping physician panels.** Scenario authoring, gold-standard determination, answering,
and scoring are performed by four separate groups with no overlap. This eliminates authorship
familiarity bias — the tendency of case authors to perform artificially well on their own cases, which
would inflate the physician benchmark and unfairly advantage the human comparator. **No published LLM
triage study has implemented this separation.** In the most recent major evaluation, the physicians
who set the gold standard were the study investigators, and no independent physician panel answered
the scenarios under the model's informational constraints.

**Free response throughout.** No answer options are ever presented, to models or to physicians.
Escalation is detected from what the system actually said, in its own words. This design is what
allows the study to speak to the format dispute rather than being another data point inside it.

**A deterministic primary endpoint.** The primary outcome — Critical Miss Rate — is scored by a
pre-registered phrase-inventory rule set applied mechanically to the model's own text, validated
against physician labels before unblinding. **No language model judges the primary endpoint.** This
removes the model-judging-model objection precisely where it would matter most. Machine assistance is
confined to secondary components, is subordinate to the physician panel, and reverts entirely to
physician scoring if it fails either of two pre-registered acceptance tests.

**Three arms, because deployment is not a benchmark.** Arm A tests models alone. Arm B is an
independent physician panel answering the same cases under the same informational constraints — a true
human comparator, which most AI evaluations lack. Arm C puts lay participants in front of the model
and measures what actually happens.

Arm C matters more than it may appear. Randomized evidence keeps finding that human–AI interaction
gives back most of what the model achieves alone: in a 2026 *Nature Medicine* trial, models
identifying conditions at 94.9% in isolation produced disposition accuracy below 44.2% in lay users'
hands — no better than the control arm. Whatever a model can do by itself is not what a patient gets.

---

## 5. What the results will mean

**If models demonstrate acceptable critical miss rates** across both registers and all severity levels,
that is the first evidence-based basis for cautious optimism about consumer health AI in acute
settings — and it will have been established on methods both sides of the current measurement dispute
have implicitly endorsed.

**If they demonstrate unacceptable miss rates** — particularly in the lay register, at high severity
weights, or in anchoring-vulnerable scenarios — that creates an evidence-based mandate for clinical
warning, patient counseling, institutional policy, and regulatory attention.

Either finding is useful. That is what makes it worth doing: the study is not constructed to confirm a
position, and its value does not depend on which way it comes out.

There is a further product. The instrument itself — 50 physician-authored, dual-register, severity-
weighted scenarios with pre-defined key features and killer items — is reusable. Models change every
few months; a one-time result decays almost immediately. A standing instrument can be reapplied to
each generation, producing a longitudinal safety record for patient-facing AI in emergency medicine.

It also places the evaluation standard where it belongs: with the emergency physicians who define the
boundary between safe discharge and life-threatening delay, rather than with the developers whose
systems are being evaluated.

---

## 6. What this study does not establish

Stated plainly, because reviewers will find these anyway and should find them here first.

**It measures at the encounter, and some of the harm arrives later.** A framework published this month
in *NEJM AI* distinguishes errors a clinician can catch inside the visit from errors that surface only
afterward — the missed referral, the deferred workup, the delayed diagnosis. Triage advice generates
both kinds. This study's primary endpoint is scored at the moment of response, which means a clean
result shows that the encounter-time output was not refuted against a physician gold standard. It does
not show that patients came to no harm three months later. Establishing that requires linking
AI-influenced dispositions to downstream outcomes, and that is a successor study.

**Vignettes are not patients.** Composite scenarios hold clinical content constant across models and
registers, which is exactly what makes comparison valid. They do not reproduce the information loss,
emotional pressure, interruption, and partial disclosure of a real person describing symptoms in real
time. Arm C narrows this gap. It does not close it, and no vignette-based design can.

**A result is a measurement, not a clearance.** Nothing here licenses a deployment decision, and the
measurement is conditioned on pinned model versions that a vendor may supersede next month.

---

## 7. What is being asked of participating physicians

Physicians participate in exactly one of four roles, and the separation between them is a design
requirement rather than an administrative preference.

| Role | What it involves |
|---|---|
| **Scenario author** | Write novel composite cases from real practice patterns, in both registers, with severity weight, gold disposition, key features, and killer items. Authors do not answer cases. |
| **Gold-standard panel** | Establish correct disposition and killer items by modified Delphi consensus. |
| **Answering panel** | Respond to finalized scenarios under the same informational constraints imposed on the models. Never sees the gold standard. |
| **Scoring and adjudication** | Evaluate outputs blinded, with structured escalation for disagreement. |

**Time commitment is approximately 6 to 10 hours in total** — not per week, in total.

No patient data are used at any point. Scenarios are physician-authored composites. The study involves
no clinical care, alters no management, and enrolls no patients. It is minimal-risk research, and the
IRB pathway — exemption or expedited review — is a question the protocol puts to the institution
rather than presuming.

---

## 8. The 2026 evidence base, briefly

The context in which this protocol sits, with citation status stated honestly.

- **Ramaswamy et al., *Nature Medicine* 2026** — independent evaluation of a deployed consumer health
  product: 51.6% of gold-standard emergencies under-triaged under structured testing; triage shifted
  toward less urgent care when third parties minimized symptoms (OR 11.7); crisis safeguards activated
  inconsistently. *Peer-reviewed.*
- **Fraile Navarro et al.** — the format-artifact challenge to the above. *Preprint; not peer-reviewed.*
- **Bean et al., *Nature Medicine* 2026** — randomized, N = 1,298: model-alone condition identification
  94.9%, disposition 56.3%; lay users below 44.2%, no better than control. *Peer-reviewed.*
- **Wu et al. (NOHARM)** — physician-authored harm-weighted safety benchmark across 31 models; safety
  correlated only r = 0.61–0.64 with knowledge benchmarks. *Preprint; not peer-reviewed.*
- **Sheng et al., *NEJM AI* 2026** — proposes four deployment safety levels for medical AI and places
  autonomous emergency triage and discharge at its red line. *Perspective; a proposed framework with
  no primary data.*
- ***Winters v. OpenAI*** (SF Superior Court, filed July 2026) — alleges a consumer chatbot met an
  evolving venous thromboembolism with reassurance and advised immobility. *Allegations, not findings.*

Throughout the protocol, preprints are labelled as preprints and allegations as allegations. Every
figure cited has been verified against a primary source, and figures that could not be verified have
been excluded rather than softened.

---

## 9. The clinical bottom line

The question this study addresses is simple enough for any patient to ask and consequential enough for
any institution to take seriously:

> *Can I trust this thing when it tells me I don't need to go to the emergency room?*

Right now, no one can answer that with evidence. Patient-facing AI is deployed at population scale in
a triage-critical role; the one headline safety estimate that exists was contested on methodological
grounds within weeks of publication; and no instrument exists that could settle it.

This protocol replaces that vacuum with a measurement — physician-authored, harm-weighted, benchmarked
against physicians, and built to be run again as the models change.

---

*Questions, or interest in one of the four panels, to the Principal Investigator. The full protocol and
the Scientific Introduction accompany this briefing.*
