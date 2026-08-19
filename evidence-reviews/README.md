# Evidence Reviews

Worked examples that apply the AMIS standards to a real clinical question, end to end.

Each review is written the way a conformant AI medical information system would be required to answer: sources tier-classified, confidence capped by the evidence actually located, negative claims scoped to the search that produced them, and a harm cascade recorded before the answer is published.

They serve three purposes:

1. **Demonstration** — the standards in [SPECIFICATION.md](../SPECIFICATION.md) are testable against a concrete question rather than only stated in the abstract.
2. **Reference output** — a target format for systems implementing the standards, complementing [examples/compliant_output.md](../examples/compliant_output.md).
3. **Standing record** — where an evidence gap is documented, the search boundary is recorded so the finding can be re-tested rather than repeated on trust.

## Index

| Review | Question | Highest tier located | Confidence ceiling |
|---|---|---|---|
| [lipoedema-ultrasound-ml.md](lipoedema-ultrasound-ml.md) | Is there a published study applying machine learning to ultrasound detection of lipoedema? | Tier 3 | Uncertain |

The lipoedema review was revised on 2026-08-19 after its stated access limitation was lifted and the PubMed search it called for was completed. The negative finding held; the revision records the confirming search and the additional evidence it surfaced.

## Conformance requirements

A review in this directory MUST:

- State the question, the review date, and the conformance level claimed
- Classify every cited source by tier per Standard 2
- Cap confidence language at the ceiling justified by the located evidence per Standard 3
- Carry the mandatory warning proximate to the uncertain content, not as a trailing disclaimer (§5.3.3)
- Contain no therapeutic advice, per Standard 5
- Record a harm cascade per §8
- Where the review asserts that evidence does not exist, state the databases searched, the date, the terms including spelling variants, and any access limitation, per `standards/imaging_ml_evidence.yaml § absence_of_evidence`

Reviews making claims about machine-learning diagnostic models MUST additionally apply [standards/imaging_ml_evidence.yaml](../standards/imaging_ml_evidence.yaml).

## Scope limit

These documents appraise published evidence. They are not clinical guidance, and they do not diagnose or recommend treatment. Standard 5 applies without exception: AI informs; physicians prescribe.
