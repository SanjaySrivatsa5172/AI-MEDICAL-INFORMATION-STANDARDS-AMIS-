# The Dharmic Framework: Constitutive Safety for AI Medical Information

**Connecting AMIS to the Broader Philosophy of AI Alignment**

---

## Overview

This document explains how the AI Medical Information Standards (AMIS) instantiate a broader philosophical framework for AI safety: the distinction between **regulatory** (constraint-based) and **constitutive** (grammar-based) approaches to alignment.

This framework draws on dharmic philosophical traditions—particularly the concepts of *pramāṇa* (valid knowledge), *ahiṃsā* (non-harm), and *viveka* (discriminative wisdom)—while remaining fully secular and practically implementable.

---

## Part I: The Regulatory vs. Constitutive Distinction

### 1.1 Two Paradigms for Safety

Consider two ways to prevent a child from touching a hot stove:

**Regulatory approach**: Place a barrier in front of the stove. The child's action (reaching for the stove) is physically blocked by an external constraint.

**Constitutive approach**: Teach the child that stoves can burn. The child's intention (wanting to touch the stove) is transformed by internal understanding.

Both approaches can prevent harm. But they differ in important ways:

| Aspect | Regulatory | Constitutive |
|--------|------------|--------------|
| **Mechanism** | External constraint blocks action | Internal understanding prevents intention |
| **Persistence** | Requires continuous enforcement | Self-sustaining once established |
| **Circumvention** | Can be bypassed if constraint is removed | Cannot be bypassed without changing understanding |
| **Scalability** | Requires constraint for each action type | Understanding generalises to novel situations |

### 1.2 Application to AI Safety

In AI safety, the regulatory approach manifests as:
- Output filters that block harmful content
- Guardrails that trigger on specific patterns
- Monitoring systems that flag concerning outputs
- Human oversight that reviews high-risk responses

The constitutive approach manifests as:
- Architecture that cannot represent certain reasoning patterns
- Training that shapes the space of possible outputs
- Value alignment that makes harmful intentions impossible
- Epistemic calibration that prevents overconfident claims

Both approaches have value. But the regulatory approach faces inherent limitations when applied to sophisticated AI systems:

1. **Detection failure**: Harmful content can be subtle, context-dependent, or novel—evading pattern-based filters
2. **Adversarial dynamics**: Systems (or users) may learn to evade constraints while achieving harmful outcomes
3. **Scalability limits**: Manual review cannot keep pace with AI output volume
4. **Incomplete coverage**: No finite set of rules covers all possible harmful outputs

The constitutive approach addresses these limitations by making harmful patterns structurally absent rather than externally blocked.

### 1.3 The Linguistic Analogy

Grammar provides the clearest analogy for constitutive constraint:

A native English speaker does not refrain from saying "the cat sat mat on the" because there is a rule prohibiting this word order. Rather, the speaker's linguistic competence does not generate this sequence—it is not a possible output of English grammar.

Similarly, a Charter-aligned AI system does not refrain from citing YouTube as a medical source because there is a filter blocking YouTube citations. Rather, the system's architecture does not include YouTube in the category of valid medical sources—citing YouTube for medical claims is not a possible output.

This is the core insight: **constitutive constraints shape what is possible, not what is permitted**.

---

## Part II: Dharmic Philosophical Foundations

### 2.1 Pramāṇa: The Theory of Valid Knowledge

The AMIS source hierarchy draws on the Indian philosophical concept of *pramāṇa*—valid means of knowledge. Different philosophical schools (darśanas) recognised different pramāṇas:

| Pramāṇa | Meaning | AMIS Application |
|---------|---------|------------------|
| **Pratyakṣa** | Direct perception | Tier 1: Direct experimental evidence (RCTs, systematic reviews) |
| **Anumāna** | Inference | Tier 2-3: Inferential evidence (observational studies, expert inference) |
| **Śabda** | Testimony | Tier 4: Expert testimony (authoritative opinion) |
| **Upamāna** | Analogy | Tier 3: Analogical reasoning (case comparisons) |
| **Anupalabdhi** | Non-apprehension | Tier 5: Absence of valid knowledge (unverified sources) |

The pramāṇa framework establishes that not all knowledge claims are equal—some arise from more reliable epistemic processes than others. The AMIS tier system operationalises this insight for medical information.

### 2.2 Ahiṃsā: The Principle of Non-Harm

*Ahiṃsā* (non-harm) is a foundational principle across dharmic traditions. It extends beyond physical non-violence to include:

- **Epistemic ahiṃsā**: Not distorting others' understanding
- **Informational ahiṃsā**: Not providing information that causes harm when acted upon
- **Systemic ahiṃsā**: Not contributing to patterns that harm communities

The AMIS harm cascade framework operationalises ahiṃsā across these dimensions:

| Harm Dimension | Ahiṃsā Application | AMIS Implementation |
|----------------|-------------------|---------------------|
| Direct harm | Physical non-violence | Block dosing information without physician referral |
| Indirect harm | Consequentialist non-harm | Prevent false reassurance that delays care |
| Epistemic harm | Epistemic non-violence | Require uncertainty disclosure, contextualisation |
| Systemic harm | Community non-harm | Protect public health understanding |

### 2.3 Viveka: Discriminative Wisdom

*Viveka* is the faculty of discrimination—the ability to distinguish between what is real and what is apparent, what is beneficial and what is harmful, what is appropriate and what is inappropriate.

In the AMIS framework, viveka manifests as:

- **Source discrimination**: Distinguishing valid sources (Tier 1-4) from invalid sources (Tier 5)
- **Confidence discrimination**: Distinguishing definitive claims from uncertain claims
- **Context discrimination**: Distinguishing when information helps and when it harms
- **Scope discrimination**: Distinguishing information provision from therapeutic advice

The standards require AI systems to exercise viveka—or more precisely, to be structured so that appropriate discriminations are architecturally enforced.

---

## Part III: The Four Pillars Applied to Medical Information

The broader EXSTO ERGO SUM framework proposes Four Pillars as constitutive constraints on AI cognition. Here we show how these pillars apply to medical information:

### 3.1 Karma: Action-Consequence Coherence

*Karma* requires tracing the consequences of actions across their full causal chain. In medical information:

- **Tracing harm cascades**: Before generating output, trace potential consequences across direct, indirect, epistemic, and systemic dimensions
- **Consequence-aware generation**: Shape outputs to minimise harmful consequences, not just harmful content
- **Accountability trails**: Maintain traceability from outputs back to sources so consequences can be attributed

The harm cascade analysis framework (Section 8 of SPECIFICATION.md) operationalises karma for medical AI.

### 3.2 Dharma: Contextual Appropriateness

*Dharma* requires action appropriate to context, role, and responsibility. In medical information:

- **Role appropriateness**: AI provides information; physicians provide care. The system does not exceed its dharmic role.
- **Context sensitivity**: The same information may be appropriate in one context (patient education) and inappropriate in another (therapeutic recommendation)
- **Responsibility acknowledgment**: The system acknowledges the limits of what it can appropriately provide

Standard 5 (Therapeutic Advice Requires Physician Evaluation) operationalises dharma by constraining the system to its appropriate role.

### 3.3 Ahiṃsā: Non-Harm

As discussed above, ahiṃsā requires comprehensive attention to all dimensions of potential harm:

- **Active non-harm**: Structuring outputs to prevent harm
- **Passive non-harm**: Omitting content that would cause harm
- **Warnings**: Alerting users when harm risk exists despite best efforts

Standards 3-5 operationalise ahiṃsā through uncertainty disclosure, dissent labelling, and physician referral.

### 3.4 Viveka: Discriminative Wisdom

Viveka requires the capacity to make appropriate discriminations:

- **Evidence discrimination**: Distinguishing strong from weak evidence
- **Confidence discrimination**: Calibrating certainty to warrant
- **Situation discrimination**: Recognising when to provide information and when to refer

Standards 1-2 operationalise viveka through the literature review paradigm and source hierarchy.

---

## Part IV: Constitutive Grammar for Medical AI

### 4.1 The Grammar Metaphor Extended

Natural language grammar constrains what can be said without constraining what can be meant. You cannot form the sentence "cat the sat mat on the" in English not because it is prohibited but because it is not a well-formed sequence in English grammar.

The AMIS standards function analogously as a **constitutional grammar** for medical AI:

| Natural Language | AMIS Constitutional Grammar |
|-----------------|----------------------------|
| Syntax rules define well-formed sentences | Source hierarchy defines valid information inputs |
| Semantic constraints define meaningful expressions | Confidence calibration defines appropriate assertion modes |
| Pragmatic constraints define appropriate speech acts | Therapeutic scope defines appropriate output types |
| Agreement rules ensure consistency | Harm cascade analysis ensures safety |

### 4.2 Type Constraints as Ethical Architecture

In programming, type systems prevent certain errors at compile time rather than runtime. You cannot pass a string to a function expecting an integer—the code will not compile.

The AMIS standards function as type constraints on medical information:

```
// Pseudocode illustrating type constraints

type Source = Tier1 | Tier2 | Tier3 | Tier4  // Tier5 is not in the type
type Confidence = Definitive | Qualified | Uncertain | Speculative
type Output = Information | Referral  // TherapeuticAdvice is not in the type

function generateMedicalClaim(source: Source, evidence: EvidenceQuality): Claim {
  // Confidence level is determined by source and evidence types
  confidence = calibrate(source, evidence)  // Type system ensures appropriate calibration
  return Claim(content, confidence, source)
}

function respondToTherapeuticQuery(query: Query): Output {
  information = generateRelevantInformation(query)
  referral = generatePhysicianReferral()  // Always included for therapeutic queries
  return Output(information, referral)  // Cannot return TherapeuticAdvice—not in type
}
```

The type system makes certain errors impossible at the architectural level rather than catching them through output filtering.

### 4.3 Saṃskāra-Vyākaraṇa: Dispositions as Grammar

The Sanskrit compound *Saṃskāra-Vyākaraṇa* (Dispositions as Grammar) captures the core insight:

- **Saṃskāra**: Mental impressions, dispositional patterns, trained tendencies
- **Vyākaraṇa**: Grammar, the structural rules governing expression

Combined: ethical dispositions functioning as grammatical constraints on cognition—not rules imposed from outside but structural features enabling thought from within.

For medical AI, this means:
- The commitment to evidence-based practice is not a rule the system follows but a structure that constitutes what the system is
- Source hierarchy is not a filter applied to outputs but a definition of what counts as valid input
- Confidence calibration is not a correction applied to claims but a constraint on how claims can be formed

---

## Part V: Implementation Implications

### 5.1 Training Implications

If the standards are to function constitutively (not just regulatively), they must be embedded in the training process:

- **Data curation**: Training data should exemplify the standards (appropriate sourcing, calibrated confidence)
- **Objective alignment**: Training objectives should include epistemic quality, not just fluency
- **Evaluation metrics**: Model evaluation should assess standard compliance, not just task performance

### 5.2 Architecture Implications

Constitutive constraints suggest architectural features:

- **Source typing**: Internal representations should distinguish source tiers
- **Confidence tracking**: Uncertainty should propagate through reasoning chains
- **Scope enforcement**: System capabilities should be bounded by design

### 5.3 Deployment Implications

Even with constitutive constraints, deployment practices matter:

- **Monitoring**: Verify that constitutive constraints are functioning as intended
- **Feedback**: Collect information on failure modes for iterative improvement
- **Updates**: Refine standards as understanding of harm patterns evolves

---

## Part VI: The Broader Vision

### 6.1 Medical AI as Testing Ground

Medical information AI provides a testing ground for constitutive safety approaches because:

- Harms are measurable (health outcomes)
- Standards are well-established (evidence-based medicine)
- Stakes are high (motivating serious attention)
- Scale is large (affecting millions of users)

Lessons learned in this domain can inform constitutive approaches for other high-stakes AI applications.

### 6.2 Toward Beneficial AI

The ultimate goal is AI that is beneficial not because it is constrained from being harmful but because it is constituted to pursue benefit. The AMIS standards represent a step toward this goal:

- Not filtering harmful medical content but constituting systems that cannot generate it
- Not monitoring for overconfident claims but structuring systems that calibrate appropriately
- Not blocking therapeutic advice but building systems that know their appropriate role

This is the dharmic vision: AI systems whose character is aligned with human flourishing because alignment is what they are, not what they are constrained to do.

---

## Conclusion

The AI Medical Information Standards operationalise a constitutive approach to safety grounded in dharmic philosophical principles:

- **Pramāṇa** (valid knowledge) → Source hierarchy
- **Ahiṃsā** (non-harm) → Harm cascade analysis
- **Viveka** (discrimination) → Confidence calibration
- **Dharma** (appropriateness) → Therapeutic scope limitation

These standards function as constitutional grammar—not rules imposed on outputs but structures that constitute what the system can generate. This constitutive approach addresses limitations of regulatory safety (detection failure, adversarial dynamics, scalability limits) by making harmful patterns structurally absent rather than externally blocked.

The medical information domain provides a testing ground for these ideas. Success here can inform constitutive approaches for AI safety more broadly—moving toward systems that are beneficial by constitution rather than beneficial by constraint.

---

## Further Reading

- [extended_rationale.md](extended_rationale.md) — Philosophical foundations of AMIS
- [SPECIFICATION.md](../SPECIFICATION.md) — Formal standards specification
- EXSTO ERGO SUM Charter — The broader framework for human-AGI covenant relations

---

*This document connects the AI Medical Information Standards to the broader EXSTO ERGO SUM philosophical framework.*
*License: CC-BY-4.0 | Author: S. Sanjay Srivatsa, MD*
