"""Calculator tests — existing validators stay authoritative."""

from __future__ import annotations

import json
import unittest
from pathlib import Path

from implementation.python.calculator import AMISCalculator
from implementation.python.claim_extractor import ClaimExtractor
from implementation.python.method_failure import MethodologicalFailureAnalyzer
from implementation.python.source_classifier import SourceClassifier
from implementation.python.validator import AMISValidator

ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = ROOT / "examples" / "calculator"


class ExistingValidatorUnchanged(unittest.TestCase):
    def test_aspirin_example_still_compliant(self):
        output = (
            "Aspirin may help reduce the risk of heart attacks in certain patients. "
            "Studies indicate that low-dose aspirin can inhibit platelet aggregation. "
            "However, aspirin is not appropriate for everyone and can cause bleeding. "
            "Please consult your healthcare provider before starting aspirin therapy "
            "to determine if it's appropriate for your individual situation."
        )
        query = "Should I take aspirin to prevent heart attacks?"
        sources = [
            {"url": "https://cochranelibrary.com/review/123", "tier": 1, "tier_justification": "Cochrane systematic review"},
            {"url": "https://www.nejm.org/article/456", "tier": 2, "tier_justification": "NEJM RCT"},
        ]
        result = AMISValidator().validate(output, query, sources)
        self.assertTrue(result.overall_compliant)
        self.assertGreaterEqual(result.overall_score, 0.9)
        self.assertEqual(result.violations, [])

    def test_youtube_still_critical(self):
        result = AMISValidator().validate(
            "Treat diabetes using this https://www.youtube.com/watch?v=abc protocol. It is guaranteed.",
            "How do I treat diabetes?",
            [{"url": "https://www.youtube.com/watch?v=abc", "tier": 5, "tier_justification": "YouTube"}],
        )
        types = {v.violation_type for v in result.violations}
        self.assertTrue({"tier_5_citation", "tier_5_in_sources"} & types)
        self.assertFalse(result.overall_compliant)


class ClaimExtractorTests(unittest.TestCase):
    def test_extracts_ai_performance_not_every_sentence(self):
        text = (
            "The clinic opened in 1998 and serves Fresno. "
            "A multimodal medical AI system achieved high benchmark accuracy "
            "while generating fabricated reasoning under perturbation. "
            "Parking is available on the north side of the building."
        )
        claims = ClaimExtractor.extract(text)
        joined = " ".join(c.claim_text.lower() for c in claims)
        self.assertTrue(claims)
        self.assertIn("benchmark", joined)
        self.assertNotIn("parking", joined)
        self.assertNotIn("1998", joined)


class MethodFailureTests(unittest.TestCase):
    def test_residencyrl_letter_is_critique_not_self_claim(self):
        text = (EXAMPLES / "residencyrl_letter.txt").read_text(encoding="utf-8")
        result = MethodologicalFailureAnalyzer.analyze(text)
        codes = {f.code for f in result.findings}
        self.assertIn("contaminated_grader", codes)
        self.assertIn("goodhart", codes)
        self.assertGreaterEqual(result.awareness_score, 40)
        self.assertGreater(result.awareness_score, result.failure_score)

    def test_asserted_autorater_counts_as_failure(self):
        text = (
            "We present our model. We achieved state-of-the-art diagnostic scores. "
            "Our autorater graded the graduate from the same model family."
        )
        result = MethodologicalFailureAnalyzer.analyze(text)
        self.assertGreaterEqual(result.failure_score, 20)
        self.assertTrue(any(f.polarity == "asserted" for f in result.findings))


class CalculatorDemoTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.calc = AMISCalculator()

    def test_srivatsa_abstract_is_calibrated(self):
        path = EXAMPLES / "srivatsa_abstract.txt"
        result = self.calc.score_path(path)
        payload = result.to_dict()
        self.assertGreaterEqual(payload["axes"]["uncertainty_calibration"]["score"], 55)
        self.assertLess(payload["axes"]["certainty_excess"]["score"], 50)
        self.assertGreaterEqual(payload["axes"]["methodological_awareness"]["score"], 20)
        self.assertIn("does not diagnose", payload["calculator_disclaimer"].lower())
        kinds = {c["claim"]["kind"] for c in payload["claims"]}
        self.assertTrue(kinds)

    def test_overconfident_example_fails_hard(self):
        path = EXAMPLES / "overconfident_ai_claims.txt"
        result = self.calc.score_path(path)
        payload = result.to_dict()
        self.assertLess(payload["overall"]["score"], 0.75)
        self.assertFalse(payload["overall"]["compliant"])
        self.assertGreaterEqual(payload["axes"]["certainty_excess"]["score"], 25)
        standards = payload["standards_scores"]
        self.assertLess(standards["standard_2_source_hierarchy"], 0.6)
        self.assertLess(standards["standard_3_uncertainty_disclosure"], 0.9)
        types = {v["violation_type"] for v in payload["violations"]}
        self.assertTrue({"tier_5_citation", "overconfident_language"} & types)

    def test_json_roundtrip(self):
        result = self.calc.score_text("AI diagnostic accuracy may be brittle under perturbation.")
        json.dumps(result.to_dict())


class SourceClassifierAdditiveTests(unittest.TestCase):
    def test_nature_and_arxiv_tiers(self):
        classifier = SourceClassifier()
        nature = classifier.classify("https://www.nature.com/articles/s41586-020-0000", "Randomized study")
        arxiv = classifier.classify("https://arxiv.org/abs/2509.18234", "Preprint")
        nature_doi = classifier.classify("https://doi.org/10.1038/s41591-025-03953-8", "STARD-AI")
        neurips = classifier.classify("https://proceedings.neurips.cc/paper/2024/hash/abc", "NeurIPS")
        self.assertEqual(nature.level, 2)
        self.assertEqual(arxiv.level, 4)
        self.assertEqual(nature_doi.level, 2)
        self.assertEqual(neurips.level, 4)


class ResidencyRLPaperPolarityTests(unittest.TestCase):
    """Short methods excerpt only — do not commit the 5.3 MB PDF."""

    EXCERPT = (
        "We present ResidencyRL, a reinforcement learning method for training "
        "clinical AI agents. An LLM autorater processes the encounter transcript "
        "and tool calls, yielding a structured reward. We train a Gemini 3.5 Flash "
        "initialized agent. At episode completion, Gemini 3.1 Pro evaluates the "
        "transcript against the ground-truth scenario. All evaluations used the "
        "same automated rubric pipeline that served as the training reward signal. "
        "Because this in-domain evaluation shares the underlying scenario generation "
        "and rubric architecture used during training, these results primarily "
        "validate that the agent successfully learns to optimize its training signals. "
        "Blinded expert clinicians preferred the trained agent in 87.6% of "
        "side-by-side comparisons, with a 90.7% win rate for completeness of "
        "information gathering."
    )

    def test_paper_asserts_contaminated_grading(self):
        result = MethodologicalFailureAnalyzer.analyze(self.EXCERPT)
        codes = {f.code: f.polarity for f in result.findings}
        self.assertEqual(codes.get("contaminated_grader"), "asserted")
        self.assertEqual(codes.get("goodhart"), "asserted")
        self.assertGreaterEqual(result.failure_score, 40)
        self.assertGreater(result.awareness_score, 0)

    def test_letter_still_critiques_not_owns(self):
        text = (EXAMPLES / "residencyrl_letter.txt").read_text(encoding="utf-8")
        result = MethodologicalFailureAnalyzer.analyze(text)
        self.assertTrue(all(f.polarity == "critiqued" for f in result.findings))
        self.assertGreater(result.awareness_score, result.failure_score)


class ToothPaperTests(unittest.TestCase):
    """Short public excerpts only — do not commit the Nature PDFs."""

    @classmethod
    def setUpClass(cls):
        cls.calc = AMISCalculator()

    def test_grader_ai_alias_is_contaminated_grader(self):
        result = MethodologicalFailureAnalyzer.analyze(
            "We introduce CRAFT-MD. A grader-AI agent reviews the diagnosis."
        )
        codes = {f.code: f.polarity for f in result.findings}
        self.assertEqual(codes.get("contaminated_grader"), "asserted")
        self.assertGreaterEqual(result.failure_score, 20)

    def test_moderator_agent_alias_is_contaminated_grader(self):
        result = MethodologicalFailureAnalyzer.analyze(
            "We introduce AgentClinic. Accuracy is determined via the moderator agent."
        )
        codes = {f.code: f.polarity for f in result.findings}
        self.assertEqual(codes.get("contaminated_grader"), "asserted")

    def test_craftmd_excerpt_owns_grader_ai(self):
        result = self.calc.score_path(EXAMPLES / "craftmd_excerpt.txt")
        payload = result.to_dict()
        codes = {f["code"]: f["polarity"] for f in payload["method"]["findings"]}
        self.assertEqual(codes.get("contaminated_grader"), "asserted")
        self.assertGreaterEqual(payload["axes"]["methodological_failure"]["score"], 20)
        self.assertGreater(payload["axes"]["methodological_awareness"]["score"], 0)
        self.assertGreaterEqual(payload["standards_scores"]["standard_5_therapeutic_scope"], 0.9)
        tiers = {s["tier"] for s in payload["sources"]}
        self.assertIn(2, tiers)
        self.assertNotIn("does not diagnose", "".join(v["description"] for v in payload["violations"]).lower())

    def test_agentclinic_excerpt_owns_moderator_and_discloses(self):
        result = self.calc.score_path(EXAMPLES / "agentclinic_excerpt.txt")
        payload = result.to_dict()
        codes = {f["code"]: f["polarity"] for f in payload["method"]["findings"]}
        self.assertEqual(codes.get("contaminated_grader"), "asserted")
        self.assertGreaterEqual(payload["axes"]["methodological_failure"]["score"], 20)
        self.assertGreater(payload["axes"]["methodological_awareness"]["score"], 0)
        self.assertGreaterEqual(payload["standards_scores"]["standard_5_therapeutic_scope"], 0.9)
        tiers = {s["tier"] for s in payload["sources"]}
        self.assertIn(2, tiers)


if __name__ == "__main__":
    unittest.main()
