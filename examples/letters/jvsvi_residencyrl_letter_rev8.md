# Letter to the Editor (rev. 8 + calculator paragraph)

**Journal**: JVS–Vascular Insights  
**Title**: ResidencyRL is not a residency: what clinician-educators should take from an AI trained on a simulated one  
**Status**: Author revision of the uploaded rev. 8 draft. Not submitted from this file.  
**Change**: one short paragraph on the public AMIS Claim Calculator, inserted before “For programs.”

---

To the Editor:

My article argued that automation bias, overconfidence, and deskilling erode productive uncertainty and asked programs to keep competency assessment AI-independent.1 ResidencyRL, from Google DeepMind, claims to train an agent as residency trains physicians: “thousands of encounters, with diverse sources of feedback and progressively greater autonomy.”2 Any residency is judged by who taught and who examined the resident.

Plainly, one model family wrote 57,453 scenarios, played the patient, computed the reward, and graded the graduate (Table). By that grader it did well: diagnostic rubric scores ≥4 rose from 81.0% to 88.0% under adversarial simulation, missed red flags fell from 45.5% to 31.5%, and blinded physicians preferred it in 87.6% of comparisons.2 The authors say so themselves: in-domain results “primarily validate that the agent successfully learns to optimize its training signals”; their autorater favored the agent where physicians did not; the mechanism is Goodhart's law.2 Language-model judges favor their own lineage,3 a generator and its reviewer share blind spots,4 and LLM-written cases and rubrics undermine measurement validity.5 Google's evaluators report intraclass correlation 0.88 and κ 0.79 for their judge against experts, κ 0.43 for a deployed baseline.6 ResidencyRL reports no agreement coefficient, only a one-sided Mann-Whitney test on 97 cases, 85 favoring it. No program director would accredit a residency in which one attending wrote the case, played the patient, graded the note, and signed the milestone; the milestone would then measure the attending.

Physicians preferred it for completeness (90.7%) yet found no accuracy difference (77.3% ties; adjusted P = .229); no external benchmark showed significant diagnostic gain.2 Training against approval raises persuasiveness without raising correctness.7 Residents learn what is graded8; so did the agent, whose rubric awards “epistemic humility” for well-phrased deferral.2 Humility that is scored is a performance.

A letter can name the contamination; a reader can also score it. I have released a public AMIS claim calculator (https://amis-claim-calculator.onrender.com) that accepts an abstract or a PDF and returns the five AMIS standards already specified for AI medical information, together with an uncertainty-versus-certainty axis and a methodological-failure axis for self-grading and in-family judges. It is a deterministic heuristic, not a licensed psychometric scale, and it does not prescribe treatment. On ResidencyRL it flags the autorater and the authors' own Goodhart sentence as asserted methodological failure.

For programs: (1) language-model scoring of notes or simulated encounters shares this contamination and needs independent examiners. (2) Unaided practice and AI-independent competency assessment stay mandatory; deskilling after routine AI exposure is measured.9 (3) All residents should ask of any AI claim who graded it and whether the grader trained it. Biased AI input degrades physician accuracy; explanation does not repair it.10

S. Sanjay Srivatsa, MD, FACC, FACP  
Heart Artery and Vein Center of Fresno  
Fresno, California

Disclosures: None. Funding: None.  
Declaration of generative AI and AI-assisted technologies: During the preparation of this letter, the author used Claude (Anthropic) to edit text and to check references. The author reviewed and edited the content and takes full responsibility for it.

## References

1. Srivatsa SS. The epistemic risk of artificial intelligence over-reliance in clinical medicine: why productive uncertainty matters. *JVS Vasc Insights.* 2026;4:100492. https://doi.org/10.1016/j.jvsvi.2026.100492
2. Liévin V, Schmidgall S, Strother T, et al. ResidencyRL: reinforcement learning in simulated clinical environments. arXiv:2608.07418. 2026.
3. Panickssery A, Bowman SR, Feng S. LLM evaluators recognize and favor their own generations. arXiv:2404.13076. 2024.
4. Sorin V, Klang E. Clinical AI generators and reviewers must be tested together. *J Med Syst.* 2026;50(1). https://doi.org/10.1007/s10916-026-02454-6
5. Rao AS, Esmail KP, Lee RS, et al. Large language model performance and clinical reasoning tasks. *JAMA Netw Open.* 2026;9(4):e264003.
6. Zhang W, Li Z, Palangi H, et al. RubricsTree: scalable and evolving open-ended evaluation of personal health agents across health memory and medical skills. arXiv:2606.18203. 2026.
7. Wen J, Zhong R, Khan A, et al. Language models learn to mislead humans via RLHF. arXiv:2409.12822. 2024.
8. Newble DI, Jaeger K. The effect of assessments and examinations on the learning of medical students. *Med Educ.* 1983;17:165-171.
9. Budzyń K, Romańczyk M, Kitala D, et al. Endoscopist deskilling risk after exposure to artificial intelligence in colonoscopy: a multicentre, observational study. *Lancet Gastroenterol Hepatol.* 2025;10:896-903.
10. Jabbour S, Fouhey D, Shepard S, et al. Measuring the impact of AI in the diagnosis of hospitalized patients: a randomized clinical vignette survey study. *JAMA.* 2023;330:2275-2284.

(Table unchanged from rev. 8.)
