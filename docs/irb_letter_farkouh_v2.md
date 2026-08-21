S. Sanjay Srivatsa, MD, FACC, FSCAI, MRCP (London), DABVLM
Director, HAV Center of Fresno
Fresno, California, USA

August 5, 2026

Michael E. Farkouh, MD, MSc
Vice Dean, Research and Clinical Trials
Professor of Cardiology
Cedars-Sinai Medical Center
Los Angeles, California

**Re: LLM Safety and Medical Reasoning Assessment — updated protocol transmittal, evidence briefing, and request for IRB routing**

Dear Dr. Farkouh,

Ahead of our discussion this Friday with Dr. Spiegel, I am transmitting the updated protocol package for the emergency triage AI safety study we have been developing since April, and writing to brief you on developments in the field over the past six weeks that bear directly on the study's rationale, design, and urgency.

**The safety question this study was built to answer is no longer hypothetical.** Three converging lines of evidence now frame it. First, *Winters v. OpenAI* (San Francisco Superior Court, complaint filed July 22) alleges that a consumer chatbot met an evolving venous thromboembolism with reassurance, invented a clinical threshold for seeking care, and advised immobility — allegations, not findings, but the alleged mechanism is a disposition failure of exactly the class our primary endpoint measures. Second, an independent Mount Sinai evaluation of ChatGPT Health published in *Nature Medicine* (Ramaswamy et al., 2026) found that, under structured testing of the live product, 51.6% of gold-standard emergencies were undertriaged, recommendations shifted toward less urgent care when family members minimized symptoms (odds ratio 11.7), and crisis safeguards activated unpredictably. Third, randomized evidence continues to show that human–AI interaction gives back much of what models achieve alone: in Bean et al. (*Nature Medicine* 2026), models identifying conditions at 94.9% in isolation fell below 44.2% disposition accuracy in lay users' hands, and the recent NOHARM randomized study (Stanford/Harvard consortium; preprint) found 101 attending physicians with AI assistance still performing far below frontier models alone — largely because they omitted appropriate recommendations their own AI had surfaced.

**Equally important, the field is now disputing how safety should be measured at all.** Within weeks of the *Nature Medicine* paper, a Macquarie University replication (preprint) showed that its forced-choice answer format manufactured much of the headline failure rate — models that scored 0–24% under forced choice recommended emergency care in their own words 100% of the time on matched scenarios. Neither side's design can resolve the question. Ours can, and by construction rather than by accident: free-response answers with escalation detected deterministically from the model's own words, dual lay/expert presentation registers, multiple version-pinned models with repeated runs, severity-weighted scoring against an independent emergency-physician benchmark, and a human-interaction arm. The NOHARM benchmark further validates our construct: across 31 models, clinical-safety performance correlated only moderately (r = 0.61–0.64) with standard knowledge-benchmark scores — accuracy and safety are measurably different axes, and only safety is unmeasured for consumer triage.

**A governance framework published this month names the gap precisely.** In *NEJM AI* (August 17), Sheng and colleagues — including Stanford’s Nigam Shah — propose four deployment-specific safety levels for medical AI and place autonomous emergency department triage and discharge at S4, their red line: deployments to be prohibited or permitted only under exceptional safeguards and treated as boxed warning–level risk. Clinician-reviewed triage support sits at S2, two tiers lower, because a clinician stands between the output and the patient. Consumer triage AI has no clinician in that loop; it is running today in the S4 configuration without S4 safeguards, and has never been formally classified at all. Their paper is a proposal and carries no data of its own — what it supplies is the vocabulary for why this measurement is owed. It also marks a boundary we now state plainly in the enclosed Scientific Introduction rather than leave for a reviewer: an encounter-time endpoint of the kind we measure is S2-grade, and establishing safety against delayed harm — the missed referral, the deferred workup — would require the outcome-linked surveillance that a successor study, not this one, would carry.

**The enclosed package reflects these developments.** Amendment 1 (July 23) added the explicit-escalation endpoint, the atypical-catastrophe scenario class, configuration comparison, and model-version pinning. The current revision cycle — detailed in the enclosed Scientific Introduction (v3) and updates memorandum — hardens the scoring architecture (physicians remain sovereign over harm determinations, anchored to RAND/UCLA appropriateness methodology and WHO harm-severity definitions, with any machine-scored component validated against, and subordinate to, the physician panel) and proposes a matched-pair bias-cue factor extending the anchoring finding to the one locus no published study has examined. The study design remains as discussed in April: no patient data, de-identified composite scenarios only, and minimal-risk physician participation of approximately 6–10 hours total per participant.

**Three requests.** First, your guidance on routing: we would welcome your office's direction on the appropriate Cedars-Sinai IRB pathway — including whether the study qualifies for exemption or expedited review as a minimal-risk, no-patient-data protocol — and to whom the formal submission should be addressed. Second, physician panels: the study's scientific core is emergency-physician authorship, and we hope Friday's discussion with Dr. Spiegel can begin identifying scenario authors and an independent answering panel. Third, we would be grateful if my co-investigator, Keyur Pawaskar, MSc, could join Friday's call; Mr. Rojas has the request.

The evaluation-standard slot in this field is open and will not remain so for long — the *Nature Medicine* paper drew 43 citing papers in five months and a public methods dispute within weeks. Cedars-Sinai is positioned to own the standard that settles it. Thank you for your continued sponsorship of this work; I look forward to Friday.

Sincerely,

S. Sanjay Srivatsa, MD, FACC, FSCAI, MRCP (London), DABVLM
Principal Investigator

**Enclosures:** Protocol v2 with Amendment 1; Addendum A (methods hardening, draft); Scientific Introduction, Version 3 (August 2026); protocol-updates memorandum; one-page study schematic.

**cc:** Brennan Spiegel, MD, MSHS; Louis Rojas, MSHA

---

*Citation notes for the record: Ramaswamy et al., Nat Med 2026;32(5):1671–75 (figures obtained under constrained forced-choice testing; see dispute). Fraile Navarro et al., arXiv 2603.11413 (preprint, not peer-reviewed). Wu et al. (NOHARM), arXiv 2512.01241 (preprint; v1 PubMed-indexed, PMID 41532042). Bean et al., Nat Med 2026;32(2):609–15. Winters v. OpenAI: allegations in active litigation; docketed citation pending.*
