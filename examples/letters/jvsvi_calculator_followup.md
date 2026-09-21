# Draft letter to the editor (follow-up)

**Journal**: JVS–Vascular Insights  
**Type**: Letter / correspondence, follow-up to Srivatsa SS. *JVS Vasc Insights.* 2026;4:100492.  
**Status**: Draft for the author’s revision. Not submitted.  
**Accompanying instrument**: AMIS Claim Calculator (`implementation/web/` in the AMIS repository).

---

Editor:

In this journal I argued that automation bias, overconfidence, and deskilling erode productive
uncertainty, and that competency assessment must remain independent of the system being
assessed.1 ResidencyRL, from Google DeepMind, now offers a concrete test of that claim.2
The authors train a Gemini 3.5 Flash policy in a Gemini-simulated clinic, grade it with a
Gemini 3.1 Pro autorater, and report that diagnostic rubric scores ≥4 rose from 81.0% to
88.0% under adversarial simulation, that missed red flags fell, and that blinded physicians
preferred the agent in 87.6% of 97 comparisons. They also write the sentence that should
govern the reading: in-domain results “primarily validate that the agent successfully learns
to optimize its training signals.”2 That is Goodhart’s law, stated by the investigators.

A letter can name the contamination. A public instrument can let a reader *score* it.
I have therefore released a small AMIS claim calculator that accepts an abstract or a PDF
and returns (i) the five AMIS standards already specified for AI medical information,3
(ii) an uncertainty-versus-certainty axis, and (iii) a methodological-failure axis aimed
at self-grading, in-family judges, shortcut learning, and preference without correctness.
The code reuses the published AMIS validator, source hierarchy, and harm cascade; it does
not invent a parallel schema. It is a deterministic heuristic, not a licensed psychometric
scale, and it does not prescribe treatment (AMIS Standard 5).

Readers can paste Liévin et al. — or any other clinical-AI claim — at:

**https://github.com/SanjaySrivatsa5172/AI-MEDICAL-INFORMATION-STANDARDS-AMIS-**

(local run: `python3 -m implementation.web.app`; paper: https://arxiv.org/pdf/2608.07418).

On the ResidencyRL PDF the calculator flags the autorater, the shared training-and-grading
rubric, and the in-domain Goodhart disclosure as *asserted* methodological failures, while
credit is given for the authors’ own caveat. That is the intended behaviour: a paper that
describes a contaminated examiner should not hide behind the fact that it also mentions
the contamination.

Two interface risks from the original analysis should be named in the same breath, because
simulated clinics make them concrete. The first is **epistemic loss at intake**. A clinician
elicits symptoms *and* signs. She discards what is irrelevant, pursues what a prior answer
cued, and corroborates suspicion on the body before she writes a plan.9 An agent that only
conducts a standardised dialogue, or that “examines” by querying another language model,
never performs that selection. What never enters the record cannot be graded. The drop from
static vignette to conversation — shown for every model in CRAFT-MD and, more sharply, for
MedQA-in-dialogue in AgentClinic — is the remnant of this loss even when the “patient” is
already a compressed script.10,11

The second is **epistemic substitution at output**. When the AI speaks to the patient it
tends to present one version of events. Fluency installs a narrative. If that narrative is
incomplete or false, the patient has not merely received a wrong fact; they have lost the
differential. AMIS Standard 3 forbids confidence in excess of warrant, and Standard 4
forbids unlabelled dissent, precisely so that a single story cannot masquerade as the case.
Physician preference for a complete-sounding note, as in ResidencyRL, is the same failure
scored as persuasiveness without correctness.

The calculator can flag the second risk in text. It cannot restore a sign that was never
elicited. That limit is constitutive: an instrument that reads claims cannot examine the
patient. Productive uncertainty therefore still requires a physician at both interfaces.

I am not proposing a sixth AMIS standard. TRIPOD-LLM, STARD-AI, CONSORT-AI, and DECIDE-AI
remain the correct *reporting* instruments for model papers and trials.4–7 AMIS asks a
prior question: may this claim be believed at the confidence with which it is written, and
who graded it? Those are the questions a resident should ask. They are now questions a
reader can run.

S. Sanjay Srivatsa, MD, FACC, FACP  
Heart Artery and Vein Center of Fresno

**Disclosures**: The author maintains the AMIS repository. No industry funding.  
**AI declaration**: Drafting assistance was used; the author takes responsibility for the letter.

## References

1. Srivatsa SS. The epistemic risk of artificial intelligence over-reliance in clinical medicine: why productive uncertainty matters. *JVS Vasc Insights.* 2026;4:100492.
2. Liévin V, Schmidgall S, Strother T, et al. ResidencyRL: reinforcement learning in simulated clinical environments. arXiv:2608.07418. 2026.
3. Srivatsa SS. AI Medical Information Standards (AMIS) v1.0.0. https://github.com/SanjaySrivatsa5172/AI-MEDICAL-INFORMATION-STANDARDS-AMIS-
4. Gallifant J, et al. The TRIPOD-LLM reporting guideline for studies using large language models. *Nat Med.* 2025.
5. Collins GS, et al. TRIPOD+AI statement. *BMJ.* 2024;385:e078378.
6. Sounderajah V, et al. The STARD-AI reporting guideline. *Nat Med.* 2025.
7. Vasey B, et al. DECIDE-AI. *Nat Med.* 2022;28:924-933.
8. Panickssery A, Bowman SR, Feng S. LLM evaluators recognize and favor their own generations. arXiv:2404.13076. 2024.
9. Hampton JR, Harrison MJG, Mitchell JRA, Prichard JS, Seymour C. Relative contributions of history-taking, physical examination and laboratory investigation to diagnosis and management of medical outpatients. *BMJ.* 1975;2:486-489.
10. Johri S, Jeong J, Tran BA, et al. An evaluation framework for clinical use of large language models in patient interaction tasks. *Nat Med.* 2025;31:77-86. doi:10.1038/s41591-024-03328-5.
11. Schmidgall S, Ziaei R, Harris C, et al. AgentClinic: a multimodal benchmark for tool-using clinical AI agents. *npj Digit Med.* 2026;9:499. doi:10.1038/s41746-026-02674-7.

---

## Notes for revision (not for submission)

These two risks are *directional*. They are not a sixth AMIS number and should not be
coded as one.

| Direction | Risk | Clinical act that is lost | What the instrument can see |
|---|---|---|---|
| Patient → AI (intake) | Epistemic **loss** | Selective history; discard noise; cue the next question; elicit a *sign* that corroborates before the plan | Almost nothing. A missing sign leaves no token to score. CRAFT-MD / AgentClinic score only the remnant: accuracy falls once the vignette is unpacked into dialogue. |
| AI → patient (output) | Epistemic **substitution** | A contested differential, labelled dissent, confidence ≤ warrant | The calculator’s Standard 3/4 axis and “persuasiveness without correctness.” One fluent story is the failure. |

Intake loss is why a patient-AI plus a measurement-agent “exam” is not an examination.
The measurement agent returns text the doctor-agent requested. A physician feels the
abdomen, watches the gait, and notices the thing that was not on the list. Substitution
is why a complete-sounding discharge explanation can be the more dangerous object: it
crowds out the other versions of events.

If the editor cuts for length, keep the two bolded names and the last three sentences
(“The calculator can flag… both interfaces.”). Those are the amendment. The CRAFT-MD /
AgentClinic sentence is optional illustration, not a new claim about those papers.
