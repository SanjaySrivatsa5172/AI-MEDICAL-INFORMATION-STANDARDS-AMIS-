"""
AMIS Claim Calculator

Scores pasted abstracts or uploaded papers against the five AMIS
standards and two aggregate axes:

1. Uncertainty vs over-certainty (calibration / epistemic humility)
2. Methodological failure (contaminated graders, Goodhart, shortcuts, …)

Reuses AMISValidator, SourceClassifier, HarmCascadeAnalyzer, and the
standards/ YAML-JSON specs. Does not invent a parallel compliance schema.

Author: S. Sanjay Srivatsa, MD
License: MIT
"""

from __future__ import annotations

import json
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional

from implementation.python.claim_extractor import ClaimExtractor, ExtractedClaim
from implementation.python.document_ingest import DocumentIngest, IngestedDocument
from implementation.python.harm_analyzer import HarmCascadeAnalyzer
from implementation.python.method_failure import MethodFailureResult, MethodologicalFailureAnalyzer
from implementation.python.source_classifier import SourceClassifier
from implementation.python.validator import AMISValidator, ConfidenceLevel, MedicalClaim, ValidationResult


class AMISPaths:
    """Resolve the repository standards directory."""

    @staticmethod
    def repo_root() -> Path:
        return Path(__file__).resolve().parents[2]

    @staticmethod
    def standards_dir() -> Path:
        return AMISPaths.repo_root() / "standards"


@dataclass
class AxisScore:
    """One 0-100 aggregate axis."""

    name: str
    score: float
    label: str
    detail: str

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "score": round(self.score, 1),
            "label": self.label,
            "detail": self.detail,
        }


@dataclass
class ClaimFinding:
    """Per-claim AMIS + axis scores."""

    claim: ExtractedClaim
    standards_scores: Dict[str, float]
    overall_score: float
    violations: List[Dict[str, str]]
    uncertainty_score: float
    method_failure_score: float
    method_findings: List[Dict[str, Any]]

    def to_dict(self) -> dict:
        return {
            "claim": self.claim.to_dict(),
            "standards_scores": {k: round(v, 3) for k, v in self.standards_scores.items()},
            "overall_score": round(self.overall_score, 3),
            "violations": self.violations,
            "uncertainty_score": round(self.uncertainty_score, 1),
            "method_failure_score": round(self.method_failure_score, 1),
            "method_findings": self.method_findings,
        }


@dataclass
class CalculatorResult:
    """Public calculator payload."""

    document: IngestedDocument
    validation: ValidationResult
    claims: List[ClaimFinding]
    uncertainty_axis: AxisScore
    certainty_excess_axis: AxisScore
    method_failure_axis: AxisScore
    method_awareness_axis: AxisScore
    method: MethodFailureResult
    harm: Dict[str, Any]
    recommendations: List[str]
    calculator_disclaimer: str
    source_notes: List[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        payload = {
            "document": self.document.to_dict(),
            "overall": {
                "compliant": self.validation.overall_compliant,
                "conformance_level": self.validation.conformance_level.value,
                "score": round(self.validation.overall_score, 3),
            },
            "standards_scores": {
                k: round(v, 3) for k, v in self.validation.standards_scores.items()
            },
            "standards": [
                {
                    "id": "standard_1_literature_review",
                    "number": 1,
                    "name": "Literature Review Paradigm",
                    "score": round(self.validation.standards_scores.get("standard_1_literature_review", 0), 3),
                },
                {
                    "id": "standard_2_source_hierarchy",
                    "number": 2,
                    "name": "Source Quality Hierarchy",
                    "score": round(self.validation.standards_scores.get("standard_2_source_hierarchy", 0), 3),
                },
                {
                    "id": "standard_3_uncertainty_disclosure",
                    "number": 3,
                    "name": "Mandatory Uncertainty Disclosure",
                    "score": round(self.validation.standards_scores.get("standard_3_uncertainty_disclosure", 0), 3),
                },
                {
                    "id": "standard_4_dissent_labeling",
                    "number": 4,
                    "name": "Dissent Labelling Without False Certainty",
                    "score": round(self.validation.standards_scores.get("standard_4_dissent_labeling", 0), 3),
                },
                {
                    "id": "standard_5_therapeutic_scope",
                    "number": 5,
                    "name": "Therapeutic Advice Requires Physician Evaluation",
                    "score": round(self.validation.standards_scores.get("standard_5_therapeutic_scope", 0), 3),
                },
            ],
            "axes": {
                "uncertainty_calibration": self.uncertainty_axis.to_dict(),
                "certainty_excess": self.certainty_excess_axis.to_dict(),
                "methodological_failure": self.method_failure_axis.to_dict(),
                "methodological_awareness": self.method_awareness_axis.to_dict(),
            },
            "violations": [
                {
                    "standard": v.standard,
                    "violation_type": v.violation_type,
                    "description": v.description,
                    "severity": v.severity.value,
                    "location": v.location,
                }
                for v in self.validation.violations
            ],
            "claims": [c.to_dict() for c in self.claims],
            "method": self.method.to_dict(),
            "harm": self.harm,
            "sources": self.document.sources,
            "source_notes": self.source_notes,
            "recommendations": self.recommendations,
            "calculator_disclaimer": self.calculator_disclaimer,
            "evidence": EvidenceAppendix.to_dict(),
        }
        return payload


class UncertaintyAxis:
    """Map Standard 3/4 + lexical markers onto a calibration axis."""

    @staticmethod
    def score(text: str, validation: ValidationResult, claims: List[ExtractedClaim]) -> AxisScore:
        s3 = validation.standards_scores.get("standard_3_uncertainty_disclosure", 0.0)
        s4 = validation.standards_scores.get("standard_4_dissent_labeling", 0.0)
        humility_hits = 0
        overconfident_hits = 0
        for claim in claims:
            humility_hits += len(claim.uncertainty_markers)
            overconfident_hits += len(claim.overconfident_markers)
        if not claims:
            humility_hits = len(ClaimExtractor.UNCERTAINTY_RE.findall(text or ""))
            overconfident_hits = len(ClaimExtractor.OVERCONFIDENT_RE.findall(text or ""))

        humility_term = min(1.0, humility_hits / 8.0)
        overconf_penalty = min(0.55, overconfident_hits * 0.12)
        calibration = 100.0 * max(
            0.0,
            min(1.0, 0.50 * s3 + 0.20 * s4 + 0.30 * humility_term - overconf_penalty),
        )
        if calibration >= 75:
            label = "Calibrated / productive uncertainty"
        elif calibration >= 50:
            label = "Mixed calibration"
        else:
            label = "Over-certain / false confidence"
        detail = (
            f"Standard 3={s3:.2f}, Standard 4={s4:.2f}, "
            f"humility markers={humility_hits}, overconfident markers={overconfident_hits}."
        )
        return AxisScore("Uncertainty calibration", calibration, label, detail)

    @staticmethod
    def excess(calibration: AxisScore) -> AxisScore:
        excess = max(0.0, 100.0 - calibration.score)
        if excess >= 50:
            label = "High false certainty"
        elif excess >= 25:
            label = "Moderate certainty excess"
        else:
            label = "Low certainty excess"
        return AxisScore(
            "Certainty excess",
            excess,
            label,
            "Inverse of uncertainty calibration: how far apparent confidence outruns warrant.",
        )


class EvidenceAppendix:
    """Citations the UI must show. Full narrative: docs/calculator_evidence.md."""

    NOTE = (
        "AMIS criteria come from documented AI-health failures, GRADE/Cochrane "
        "source hierarchy, and the productive-uncertainty literature. The "
        "methodological-failure axis is the TRIPOD-LLM / STARD-AI assessment-"
        "integrity items (independent examiner, no in-family judge) expressed "
        "as a score, not a sixth AMIS standard. This instrument is a "
        "deterministic heuristic, not a licensed psychometric scale. "
        "GitHub / ORCID / Hugging Face bibliography links are Tier 4 "
        "reproducibility hosts, not YouTube-tier Standard 2 failures."
    )

    REFERENCES = [
        "Srivatsa SS. JVS Vasc Insights. 2026;4:100492.",
        "Liévin V, et al. ResidencyRL. arXiv:2608.07418. 2026.",
        "Gallifant J, et al. TRIPOD-LLM. Nat Med. 2025.",
        "Collins GS, et al. TRIPOD+AI. BMJ. 2024;385:e078378.",
        "Sounderajah V, et al. STARD-AI. Nat Med. 2025.",
        "Panickssery A, et al. LLM evaluators favor their own generations. arXiv:2404.13076.",
        "Simpkin AL, Schwartzstein RM. N Engl J Med. 2016;375:1713-1715.",
        "Goddard K, et al. Automation bias. JAMIA. 2012;19:121-127.",
        "Jabbour S, et al. JAMA. 2023;330:2275-2284.",
        "Johri S, et al. CRAFT-MD. Nat Med. 2025;31:77-86. doi:10.1038/s41591-024-03328-5.",
        "Schmidgall S, et al. AgentClinic. npj Digit Med. 2026;9:499. doi:10.1038/s41746-026-02674-7.",
    ]

    BIBLIOGRAPHY_NOTE = (
        "Standard 2: GitHub, ORCID, and Hugging Face links are Tier 4 "
        "reproducibility / identity hosts. They are bibliography noise — not "
        "medical evidence and not YouTube-tier (Tier 5) failures. YouTube, "
        "TikTok, and social media remain excluded."
    )

    @staticmethod
    def to_dict() -> dict:
        return {"note": EvidenceAppendix.NOTE, "references": list(EvidenceAppendix.REFERENCES)}


class AMISCalculator:
    """Orchestrate ingest → extraction → existing validators → axes."""

    MAX_PER_CLAIM_VALIDATIONS = 8
    HARM_TEXT_CHARS = 24_000

    DISCLAIMER = (
        "This calculator evaluates epistemic claims against the AMIS standards. "
        "It does not diagnose, prescribe, dose, or recommend treatment. "
        "Therapeutic decisions require evaluation by a qualified physician "
        "(AMIS Standard 5)."
    )

    def __init__(self, config_path: Optional[Path] = None) -> None:
        standards = config_path or AMISPaths.standards_dir()
        self.validator = AMISValidator(config_path=standards if standards.exists() else None)
        self.classifier = SourceClassifier()
        self.harm_analyzer = HarmCascadeAnalyzer()

    def score_text(self, text: str, filename: Optional[str] = None) -> CalculatorResult:
        document = DocumentIngest.from_text(text, filename=filename, source_kind="paste")
        return self._score_document(document)

    def score_upload(self, data: bytes, filename: str) -> CalculatorResult:
        document = DocumentIngest.from_bytes(data, filename)
        return self._score_document(document)

    def score_path(self, path: Path) -> CalculatorResult:
        document = DocumentIngest.from_path(path)
        return self._score_document(document)

    def _score_document(self, document: IngestedDocument) -> CalculatorResult:
        extracted = ClaimExtractor.extract(document.text)
        claim_payload = [
            {
                "claim_text": c.claim_text,
                "confidence": (
                    "speculative"
                    if c.overconfident_markers
                    else "qualified"
                    if c.uncertainty_markers
                    else "qualified_definitive"
                ),
                "highest_tier": min((s["tier"] for s in document.sources), default=5),
                "uncertainty_disclosed": bool(c.uncertainty_markers),
                "warning_included": False,
            }
            for c in extracted
        ]

        validation = self.validator.validate(
            output=document.text,
            query="",
            sources=document.sources,
            claims=claim_payload,
        )
        harm = self.harm_analyzer.analyze(document.text[: AMISCalculator.HARM_TEXT_CHARS], query="")
        method = MethodologicalFailureAnalyzer.analyze(document.text)

        findings: List[ClaimFinding] = []
        for claim in extracted[: AMISCalculator.MAX_PER_CLAIM_VALIDATIONS]:
            claim_validation = self.validator.validate(
                output=claim.claim_text,
                query="",
                sources=document.sources,
            )
            claim_method = MethodologicalFailureAnalyzer.analyze(claim.claim_text)
            findings.append(
                ClaimFinding(
                    claim=claim,
                    standards_scores=claim_validation.standards_scores,
                    overall_score=claim_validation.overall_score,
                    violations=[
                        {
                            "standard": v.standard,
                            "violation_type": v.violation_type,
                            "description": v.description,
                            "severity": v.severity.value,
                        }
                        for v in claim_validation.violations
                    ],
                    uncertainty_score=UncertaintyAxis.score(
                        claim.claim_text, claim_validation, [claim]
                    ).score,
                    method_failure_score=claim_method.failure_score,
                    method_findings=claim_method.to_dict()["findings"],
                )
            )

        uncertainty = UncertaintyAxis.score(document.text, validation, extracted)
        certainty_excess = UncertaintyAxis.excess(uncertainty)
        method_failure_axis = AxisScore(
            name="Methodological failure",
            score=method.failure_score,
            label=AMISCalculator._failure_label(method.failure_score),
            detail="Asserted evaluation contamination, shortcut learning, Goodhart gaming, or fabricated reasoning.",
        )
        method_awareness_axis = AxisScore(
            name="Methodological awareness",
            score=method.awareness_score,
            label=AMISCalculator._awareness_label(method.awareness_score),
            detail="Failure modes the text itself labels as risks rather than as its own results.",
        )

        recommendations = list(validation.recommendations)
        recommendations.extend(AMISCalculator._axis_recommendations(method, uncertainty))
        source_notes = list(document.notes)
        source_notes.extend(AMISCalculator._source_notes(document.sources))
        recommendations.extend(source_notes)
        if AMISCalculator.DISCLAIMER not in recommendations:
            recommendations.append(AMISCalculator.DISCLAIMER)

        # Attach extracted claims onto the unused ValidationResult.claims slot
        # without changing standard scoring.
        validation.claims = AMISCalculator._to_medical_claims(extracted, document.sources)

        return CalculatorResult(
            document=document,
            validation=validation,
            claims=findings,
            uncertainty_axis=uncertainty,
            certainty_excess_axis=certainty_excess,
            method_failure_axis=method_failure_axis,
            method_awareness_axis=method_awareness_axis,
            method=method,
            harm=harm.to_dict(),
            recommendations=recommendations,
            calculator_disclaimer=AMISCalculator.DISCLAIMER,
            source_notes=source_notes,
        )

    @staticmethod
    def _to_medical_claims(extracted: List[ExtractedClaim], sources: List[Dict]) -> List[MedicalClaim]:
        from implementation.python.validator import SourceCitation

        parsed_sources = [
            SourceCitation(
                url=s.get("url", ""),
                tier=s.get("tier", 5),
                tier_justification=s.get("tier_justification", ""),
                title=s.get("title"),
            )
            for s in sources
        ]
        highest = min((s.tier for s in parsed_sources), default=5)
        claims = []
        for item in extracted:
            if item.overconfident_markers:
                confidence = ConfidenceLevel.SPECULATIVE
            elif item.uncertainty_markers:
                confidence = ConfidenceLevel.QUALIFIED
            else:
                confidence = ConfidenceLevel.QUALIFIED_DEFINITIVE
            claims.append(
                MedicalClaim(
                    claim_text=item.claim_text,
                    confidence=confidence,
                    supporting_sources=parsed_sources,
                    highest_tier=highest,
                    uncertainty_disclosed=bool(item.uncertainty_markers),
                    warning_included=False,
                )
            )
        return claims

    @staticmethod
    def _failure_label(score: float) -> str:
        if score >= 60:
            return "Severe asserted methodological failure"
        if score >= 25:
            return "Material methodological failure"
        if score > 0:
            return "Limited asserted failure"
        return "No asserted methodological failure"

    @staticmethod
    def _awareness_label(score: float) -> str:
        if score >= 60:
            return "High methodological vigilance"
        if score >= 25:
            return "Some failure modes labelled"
        if score > 0:
            return "Sparse methodological critique"
        return "No methodological failure modes labelled"

    @staticmethod
    def _source_notes(sources: List[Dict]) -> List[str]:
        if any(SourceClassifier.is_bibliography_host(s.get("url", "")) for s in sources):
            return [EvidenceAppendix.BIBLIOGRAPHY_NOTE]
        return []

    @staticmethod
    def _axis_recommendations(method: MethodFailureResult, uncertainty: AxisScore) -> List[str]:
        recs: List[str] = []
        if uncertainty.score < 50:
            recs.append(
                "Calibrate confidence to epistemic warrant (Standard 3): replace "
                "definitive phrasing with evidence-tiered language and proximate warnings."
            )
        asserted = [f for f in method.findings if f.polarity == "asserted"]
        if any(f.code == "contaminated_grader" and f.polarity == "asserted" for f in asserted):
            recs.append(
                "Require an examiner independent of the teacher and the patient simulator. "
                "In-family autoraters measure the attending, not the trainee."
            )
        if any(f.code == "goodhart" and f.polarity == "asserted" for f in asserted):
            recs.append(
                "Report independent outcomes (accuracy, missed red flags, external benchmarks), "
                "not only the reward the agent was trained to optimize."
            )
        if any(f.code in {"shortcut_learning", "fabricated_reasoning", "brittleness"} and f.polarity == "asserted" for f in asserted):
            recs.append(
                "Stress-test the claim under perturbation and withheld inputs. "
                "High benchmarks achieved for the wrong reasons are not clinical competence."
            )
        if any(f.code == "persuasiveness_not_correctness" and f.polarity == "asserted" for f in asserted):
            recs.append(
                "Do not equate physician preference or completeness with correctness. "
                "Training against approval raises persuasiveness without raising accuracy."
            )
        return recs


def main(argv: Optional[List[str]] = None) -> int:
    """CLI: python -m implementation.python.calculator [file-or-stdin]."""
    args = list(sys.argv[1:] if argv is None else argv)
    calculator = AMISCalculator()
    if args:
        result = calculator.score_path(Path(args[0]))
    else:
        result = calculator.score_text(sys.stdin.read(), filename="stdin")
    print(json.dumps(result.to_dict(), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
