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

**https://amis-claim-calculator.onrender.com**

(source: https://github.com/SanjaySrivatsa5172/AI-MEDICAL-INFORMATION-STANDARDS-AMIS-;
paper: https://arxiv.org/pdf/2608.07418).

On the ResidencyRL PDF the calculator flags the autorater, the shared training-and-grading
rubric, and the in-domain Goodhart disclosure as *asserted* methodological failures, while
credit is given for the authors’ own caveat. That is the intended behaviour: a paper that
describes a contaminated examiner should not hide behind the fact that it also mentions
the contamination.

The same axis scores two further conversational benchmarks without adding a standard.
CRAFT-MD (Johri et al., *Nat Med* 2025) uses a patient-AI and a grader-AI and shows
every model dropping from vignette to conversation. AgentClinic (Schmidgall et al.,
*npj Digit Med* 2026) uses an LLM moderator to score MedQA-in-dialogue, where
accuracy can fall to about one-tenth of the static number. The drop is the slide;
the in-family examiner is the tooth.

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
9. Johri S, Jeong J, Tran BA, et al. An evaluation framework for clinical use of large language models in patient interaction tasks. *Nat Med.* 2025;31:77-86. doi:10.1038/s41591-024-03328-5.
10. Schmidgall S, Ziaei R, Harris C, et al. AgentClinic: a multimodal benchmark for tool-using clinical AI agents. *npj Digit Med.* 2026;9:499. doi:10.1038/s41746-026-02674-7.
