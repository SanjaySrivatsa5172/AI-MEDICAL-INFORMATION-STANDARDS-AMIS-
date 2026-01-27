"""
AMIS Source Classifier - Source Quality Tier Classification

This module provides utilities for classifying medical information sources
according to the AMIS five-tier hierarchy.

Author: S. Sanjay Srivatsa, MD
License: MIT
Version: 1.0.0
"""

import re
from dataclasses import dataclass
from enum import Enum
from typing import Optional, List, Dict, Tuple
from urllib.parse import urlparse


class SourceTier(Enum):
    """Source quality tiers."""
    TIER_1 = 1  # Primary Authority
    TIER_2 = 2  # High-Quality Primary Evidence
    TIER_3 = 3  # Supporting Evidence
    TIER_4 = 4  # Expert Opinion
    TIER_5 = 5  # Excluded Sources


@dataclass
class TierClassification:
    """Classification result for a source."""
    tier: SourceTier
    tier_name: str
    usage_guideline: str
    confidence_ceiling: Optional[str]
    justification: str
    warnings: List[str]
    
    @property
    def level(self) -> int:
        return self.tier.value
    
    @property
    def permitted(self) -> bool:
        return self.tier != SourceTier.TIER_5


# Tier 1: Primary Authority Sources
TIER_1_DOMAINS = {
    # Cochrane
    "cochranelibrary.com": "Cochrane Library",
    "cochrane.org": "Cochrane Collaboration",
    
    # WHO
    "who.int": "World Health Organization",
    
    # National Guideline Bodies
    "nice.org.uk": "NICE (UK)",
    "uspreventiveservicestaskforce.org": "USPSTF (US)",
    "sign.ac.uk": "SIGN (Scotland)",
    "nhmrc.gov.au": "NHMRC (Australia)",
    "cadth.ca": "CADTH (Canada)",
}

# Tier 2: Major Medical Journals
TIER_2_DOMAINS = {
    # Major General Medical Journals
    "nejm.org": "New England Journal of Medicine",
    "thelancet.com": "The Lancet",
    "jamanetwork.com": "JAMA Network",
    "bmj.com": "BMJ",
    "acpjournals.org": "Annals of Internal Medicine",
    
    # Major Specialty Journals (selection)
    "ahajournals.org": "AHA Journals (Circulation, etc.)",
    "onlinelibrary.wiley.com/journal/diabetes": "Diabetes journals",
    "gastrojournal.org": "Gastroenterology",
    "jneurosci.org": "Journal of Neuroscience",
    
    # Professional Society Guidelines
    "acc.org": "American College of Cardiology",
    "asco.org": "American Society of Clinical Oncology",
    "diabetes.org": "American Diabetes Association",
    "heart.org": "American Heart Association",
    "acog.org": "ACOG",
    "aafp.org": "AAFP",
}

# Tier 3: Supporting Evidence Sources
TIER_3_DOMAINS = {
    # Medical Databases
    "uptodate.com": "UpToDate",
    "medlineplus.gov": "MedlinePlus (NIH)",
    "dynamed.com": "DynaMed",
    "bestpractice.bmj.com": "BMJ Best Practice",
    
    # Academic Medical Centers
    "mayoclinic.org": "Mayo Clinic",
    "clevelandclinic.org": "Cleveland Clinic",
    "hopkinsmedicine.org": "Johns Hopkins Medicine",
    "health.harvard.edu": "Harvard Health",
    "stanfordhealthcare.org": "Stanford Health Care",
    "ucsfhealth.org": "UCSF Health",
    "mountsinai.org": "Mount Sinai",
    
    # Government Health Sites
    "cdc.gov": "CDC",
    "nih.gov": "NIH",
    "nhs.uk": "NHS (UK)",
    "healthdirect.gov.au": "HealthDirect (Australia)",
    
    # PubMed (peer-reviewed)
    "pubmed.ncbi.nlm.nih.gov": "PubMed",
    "ncbi.nlm.nih.gov": "NCBI",
}

# Tier 4: Expert Opinion Sources
TIER_4_PATTERNS = [
    r"editorial", r"commentary", r"opinion",
    r"perspective", r"viewpoint", r"letter to.*editor"
]

# Tier 5: Excluded Sources
TIER_5_DOMAINS = {
    # Video Platforms
    "youtube.com": "YouTube",
    "youtu.be": "YouTube (short URL)",
    "tiktok.com": "TikTok",
    "vimeo.com": "Vimeo",
    
    # Social Media
    "twitter.com": "Twitter/X",
    "x.com": "X (Twitter)",
    "facebook.com": "Facebook",
    "instagram.com": "Instagram",
    "linkedin.com": "LinkedIn",
    "threads.net": "Threads",
    
    # Forums
    "reddit.com": "Reddit",
    "quora.com": "Quora",
    "healthboards.com": "Health forums",
    "patient.info/forums": "Patient forums",
    
    # Blogs/News Aggregators
    "medium.com": "Medium",
    "substack.com": "Substack",
    "healthline.com": "Healthline (aggregator)",
    "webmd.com": "WebMD (aggregator)",
    "verywellhealth.com": "Verywell Health",
    "medicalnewstoday.com": "Medical News Today",
}


class SourceClassifier:
    """
    Classifies medical information sources according to AMIS tier hierarchy.
    
    Example usage:
        classifier = SourceClassifier()
        result = classifier.classify("https://cochranelibrary.com/review/12345")
        print(f"Tier: {result.tier.value} - {result.tier_name}")
        print(f"Usage: {result.usage_guideline}")
    """
    
    def __init__(self):
        """Initialize the classifier with tier databases."""
        self.tier_1_domains = TIER_1_DOMAINS
        self.tier_2_domains = TIER_2_DOMAINS
        self.tier_3_domains = TIER_3_DOMAINS
        self.tier_5_domains = TIER_5_DOMAINS
    
    def classify(self, url: str, context: Optional[str] = None) -> TierClassification:
        """
        Classify a source URL into the appropriate tier.
        
        Args:
            url: The URL of the source
            context: Optional additional context (title, publication type, etc.)
        
        Returns:
            TierClassification with tier level and usage guidelines
        """
        # Parse URL
        try:
            parsed = urlparse(url.lower())
            domain = parsed.netloc.replace("www.", "")
        except Exception:
            return self._create_classification(
                SourceTier.TIER_5,
                "Invalid URL - cannot verify source",
                ["URL could not be parsed"]
            )
        
        # Check Tier 5 first (excluded sources)
        tier_5_result = self._check_tier_5(domain, url)
        if tier_5_result:
            return tier_5_result
        
        # Check Tier 1 (Primary Authority)
        tier_1_result = self._check_tier_1(domain, url, context)
        if tier_1_result:
            return tier_1_result
        
        # Check Tier 2 (High-Quality Primary Evidence)
        tier_2_result = self._check_tier_2(domain, url, context)
        if tier_2_result:
            return tier_2_result
        
        # Check Tier 3 (Supporting Evidence)
        tier_3_result = self._check_tier_3(domain, url, context)
        if tier_3_result:
            return tier_3_result
        
        # Check Tier 4 patterns in context
        if context:
            tier_4_result = self._check_tier_4(domain, url, context)
            if tier_4_result:
                return tier_4_result
        
        # Default to Tier 4 for unrecognized peer-reviewed content
        # or Tier 5 for completely unknown sources
        if self._appears_peer_reviewed(domain, url, context):
            return self._create_classification(
                SourceTier.TIER_4,
                f"Unrecognized source: {domain}",
                ["Source not in database; classified conservatively as Tier 4"]
            )
        else:
            return self._create_classification(
                SourceTier.TIER_5,
                f"Unknown source: {domain}",
                ["Source cannot be verified as peer-reviewed or authoritative"]
            )
    
    def _check_tier_5(self, domain: str, url: str) -> Optional[TierClassification]:
        """Check if source is Tier 5 (excluded)."""
        for tier_5_domain, name in self.tier_5_domains.items():
            if tier_5_domain in domain:
                return self._create_classification(
                    SourceTier.TIER_5,
                    f"Excluded source: {name}",
                    [
                        "Tier 5 sources MUST NOT be used for medical claims",
                        "Platform lacks peer review and quality control mechanisms"
                    ]
                )
        return None
    
    def _check_tier_1(
        self, 
        domain: str, 
        url: str, 
        context: Optional[str]
    ) -> Optional[TierClassification]:
        """Check if source is Tier 1 (Primary Authority)."""
        for tier_1_domain, name in self.tier_1_domains.items():
            if tier_1_domain in domain:
                # Verify it's actually a guideline/review, not just the homepage
                if context:
                    context_lower = context.lower()
                    if any(kw in context_lower for kw in ["systematic review", "meta-analysis", "guideline", "recommendation"]):
                        return self._create_classification(
                            SourceTier.TIER_1,
                            f"Primary Authority: {name}",
                            []
                        )
                
                # Domain match without context verification
                return self._create_classification(
                    SourceTier.TIER_1,
                    f"Primary Authority: {name}",
                    ["Verify this is a guideline/systematic review, not general content"]
                )
        
        # Check for systematic review indicators in URL or context
        if context:
            context_lower = context.lower()
            if "systematic review" in context_lower or "meta-analysis" in context_lower:
                if self._appears_peer_reviewed(domain, url, context):
                    return self._create_classification(
                        SourceTier.TIER_1,
                        "Systematic review/meta-analysis",
                        ["Verify publication in peer-reviewed indexed journal"]
                    )
        
        return None
    
    def _check_tier_2(
        self, 
        domain: str, 
        url: str, 
        context: Optional[str]
    ) -> Optional[TierClassification]:
        """Check if source is Tier 2 (High-Quality Primary Evidence)."""
        for tier_2_domain, name in self.tier_2_domains.items():
            if tier_2_domain in domain:
                return self._create_classification(
                    SourceTier.TIER_2,
                    f"High-Quality Primary Evidence: {name}",
                    []
                )
        
        # Check for RCT indicators
        if context:
            context_lower = context.lower()
            if "randomized" in context_lower or "randomised" in context_lower:
                if "controlled trial" in context_lower or "clinical trial" in context_lower:
                    if self._appears_peer_reviewed(domain, url, context):
                        return self._create_classification(
                            SourceTier.TIER_2,
                            "Randomized controlled trial",
                            ["Verify publication in major peer-reviewed journal"]
                        )
        
        return None
    
    def _check_tier_3(
        self, 
        domain: str, 
        url: str, 
        context: Optional[str]
    ) -> Optional[TierClassification]:
        """Check if source is Tier 3 (Supporting Evidence)."""
        for tier_3_domain, name in self.tier_3_domains.items():
            if tier_3_domain in domain:
                return self._create_classification(
                    SourceTier.TIER_3,
                    f"Supporting Evidence: {name}",
                    ["Must not contradict Tier 1-2 consensus"]
                )
        
        # Check for .edu medical domains
        if ".edu" in domain:
            if any(med in domain for med in ["med", "health", "hospital", "clinic"]):
                return self._create_classification(
                    SourceTier.TIER_3,
                    f"Academic medical institution: {domain}",
                    ["Verify institutional affiliation and editorial process"]
                )
        
        # Check for .gov health domains
        if ".gov" in domain:
            return self._create_classification(
                SourceTier.TIER_3,
                f"Government health source: {domain}",
                []
            )
        
        return None
    
    def _check_tier_4(
        self, 
        domain: str, 
        url: str, 
        context: Optional[str]
    ) -> Optional[TierClassification]:
        """Check if source is Tier 4 (Expert Opinion)."""
        if context:
            context_lower = context.lower()
            for pattern in TIER_4_PATTERNS:
                if re.search(pattern, context_lower):
                    return self._create_classification(
                        SourceTier.TIER_4,
                        f"Expert opinion: {pattern}",
                        ["Must not serve as sole basis for medical claims"]
                    )
        return None
    
    def _appears_peer_reviewed(
        self, 
        domain: str, 
        url: str, 
        context: Optional[str]
    ) -> bool:
        """Heuristic check if source appears to be peer-reviewed."""
        # Check for DOI
        if "doi.org" in url or "doi:" in (context or "").lower():
            return True
        
        # Check for journal indicators
        if any(ind in domain for ind in ["journal", "jama", "lancet", "nejm", "bmj"]):
            return True
        
        # Check for pubmed/ncbi
        if "pubmed" in domain or "ncbi" in domain:
            return True
        
        # Check context for peer-review indicators
        if context:
            peer_review_indicators = ["peer-reviewed", "published in", "doi:", "pmid:", "journal"]
            if any(ind in context.lower() for ind in peer_review_indicators):
                return True
        
        return False
    
    def _create_classification(
        self, 
        tier: SourceTier, 
        justification: str,
        warnings: List[str]
    ) -> TierClassification:
        """Create a TierClassification object with standard fields."""
        
        tier_info = {
            SourceTier.TIER_1: {
                "name": "Primary Authority",
                "usage": "Primary weight; definitive statements permitted",
                "ceiling": "definitive"
            },
            SourceTier.TIER_2: {
                "name": "High-Quality Primary Evidence",
                "usage": "Supplements Tier 1; qualified definitive statements",
                "ceiling": "qualified_definitive"
            },
            SourceTier.TIER_3: {
                "name": "Supporting Evidence",
                "usage": "Context only; must not contradict Tier 1-2 consensus",
                "ceiling": "qualified"
            },
            SourceTier.TIER_4: {
                "name": "Expert Opinion",
                "usage": "Narrative framing only; never sole basis for claims",
                "ceiling": "uncertain"
            },
            SourceTier.TIER_5: {
                "name": "Excluded Sources",
                "usage": "NEVER used for medical claims",
                "ceiling": None
            }
        }
        
        info = tier_info[tier]
        
        return TierClassification(
            tier=tier,
            tier_name=info["name"],
            usage_guideline=info["usage"],
            confidence_ceiling=info["ceiling"],
            justification=justification,
            warnings=warnings
        )
    
    def classify_batch(
        self, 
        sources: List[Dict[str, str]]
    ) -> List[TierClassification]:
        """
        Classify multiple sources.
        
        Args:
            sources: List of dicts with 'url' and optional 'context' keys
        
        Returns:
            List of TierClassification objects
        """
        return [
            self.classify(s.get("url", ""), s.get("context"))
            for s in sources
        ]
    
    def get_highest_tier(
        self, 
        classifications: List[TierClassification]
    ) -> Optional[TierClassification]:
        """
        Get the highest quality tier from a list of classifications.
        
        Args:
            classifications: List of TierClassification objects
        
        Returns:
            The classification with the lowest tier number (highest quality)
        """
        valid = [c for c in classifications if c.permitted]
        if not valid:
            return None
        return min(valid, key=lambda c: c.tier.value)
    
    def validate_source_mix(
        self, 
        classifications: List[TierClassification]
    ) -> Tuple[bool, List[str]]:
        """
        Validate that a mix of sources meets AMIS requirements.
        
        Args:
            classifications: List of TierClassification objects
        
        Returns:
            Tuple of (valid, list of issues)
        """
        issues = []
        
        # Check for Tier 5 sources
        tier_5_sources = [c for c in classifications if c.tier == SourceTier.TIER_5]
        if tier_5_sources:
            issues.append(f"CRITICAL: {len(tier_5_sources)} Tier 5 source(s) present - must be removed")
        
        # Check for high-tier sources
        high_tier = [c for c in classifications if c.tier.value <= 2]
        if not high_tier and classifications:
            issues.append("WARNING: No Tier 1-2 sources - medical claims lack high-quality support")
        
        # Check tier distribution
        tier_counts = {}
        for c in classifications:
            tier_counts[c.tier.value] = tier_counts.get(c.tier.value, 0) + 1
        
        if tier_counts.get(3, 0) > tier_counts.get(1, 0) + tier_counts.get(2, 0):
            issues.append("NOTE: More Tier 3 sources than Tier 1-2 - consider adding higher-quality evidence")
        
        valid = len([i for i in issues if i.startswith("CRITICAL")]) == 0
        return valid, issues


# Convenience function
def classify(url: str, context: Optional[str] = None) -> TierClassification:
    """
    Quick classification function.
    
    Example:
        from source_classifier import classify
        result = classify("https://cochranelibrary.com/review/12345")
        print(f"Tier {result.level}: {result.tier_name}")
    """
    classifier = SourceClassifier()
    return classifier.classify(url, context)


if __name__ == "__main__":
    # Example usage
    classifier = SourceClassifier()
    
    test_urls = [
        ("https://www.cochranelibrary.com/cdsr/doi/10.1002/14651858.CD012345", "Systematic review"),
        ("https://www.nejm.org/doi/full/10.1056/NEJMoa2034577", "Randomized controlled trial"),
        ("https://www.mayoclinic.org/diseases-conditions/diabetes", None),
        ("https://www.uptodate.com/contents/diabetes-mellitus", None),
        ("https://www.youtube.com/watch?v=abc123", "Dr. Smith explains diabetes"),
        ("https://www.reddit.com/r/diabetes/comments/xyz", "User discussion"),
        ("https://pubmed.ncbi.nlm.nih.gov/12345678/", "Observational cohort study"),
    ]
    
    print("Source Classification Examples")
    print("=" * 60)
    
    for url, context in test_urls:
        result = classifier.classify(url, context)
        print(f"\nURL: {url}")
        print(f"  Tier: {result.tier.value} - {result.tier_name}")
        print(f"  Usage: {result.usage_guideline}")
        print(f"  Permitted: {result.permitted}")
        if result.warnings:
            print(f"  Warnings: {result.warnings}")
