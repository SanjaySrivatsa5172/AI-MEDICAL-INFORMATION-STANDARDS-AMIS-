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
        self.assertEqual(nature.level, 2)
        self.assertEqual(arxiv.level, 4)


if __name__ == "__main__":
    unittest.main()
