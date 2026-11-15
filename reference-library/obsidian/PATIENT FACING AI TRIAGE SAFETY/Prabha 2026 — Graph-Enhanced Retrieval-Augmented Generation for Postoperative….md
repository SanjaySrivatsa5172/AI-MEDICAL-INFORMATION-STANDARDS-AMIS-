---
title: "Graph-Enhanced Retrieval-Augmented Generation for Postoperative Patient Question Answering: A Comparative Evaluation of Knowledge Graph, Retrieval-Augmented Generation, and Hybrid GraphRAG Approaches"
authors: "Prabha S, Collaco BG, Rosa Malena C, Haider SA, Wood N, Forte AJ"
journal: "Bioengineering (Basel)"
year: 2026
doi: "10.3390/bioengineering13101097"
pmid: "42938952"
url: "https://doi.org/10.3390/bioengineering13101097"
type: "journal-article"
tier: "ancillary"
design-overlap: false
date-added: 2026-10-28
source: "pubmed-verified"
tags: [patient-facing-ai, ai-safety-failure-modes, emergency-triage-ai, benchmark-methodology, ancillary]
---
# Graph-Enhanced Retrieval-Augmented Generation for Postoperative Patient Question Answering: A Comparative Evaluation of Knowledge Graph, Retrieval-Augmented Generation, and Hybrid GraphRAG Approaches

**Prabha S, Collaco BG, Rosa Malena C, Haider SA, Wood N, Forte AJ** — *Bioengineering (Basel)* (2026)

> [!note] Clinical relevance
> Patient-facing postoperative patient-messaging question-answering study (Mayo Clinic) comparing knowledge-graph-only, RAG-only, and hybrid GraphRAG architectures on a 250-question benchmark that includes a pre-specified 20-question EMERGENCY-INTENT arm (plus 200 in-scope and 30 out-of-scope), with three blinded clinicians rating all 750 outputs. Overall accuracy 96.8% (GraphRAG) / 94.8% (RAG-only) / 56.0% (KG-only); LLM-as-a-judge estimated hallucination risk 0.108 / 0.132 / 0.436. CRITICALLY, EMERGENCY-INTENT accuracy was only 75.0% for BOTH retrieval-augmented systems -- the authors conclude the architecture is 'suited to supervised clinical workflows with clinician review, not autonomous patient-facing triage,' and call for prospective validation on authentic patient messages. The sub-threshold emergency-intent accuracy (a missed-emergency / under-triage risk when patients message about acute concerns) is squarely the protocol's failure mode. Relevant via emergency-relevance (defined emergency-intent arm; undertriage risk) + patient-facing (postoperative patient-facing messaging) + AI-safety FAILURE-MODE (hallucination-risk estimation; 25% emergency-intent miss -> explicit 'not autonomous patient-facing triage'). Ancillary, design_overlap FALSE: the primary design is a RAG-ARCHITECTURE comparison and the patient-facing emergency-triage-safety signal is a small (ancillary) arm within it, not the protocol's dual-register harm-weighted triage twin. Surfaced by the 2026-10-28 reconciler's PubMed edat sweep. Verification: PubMed-verified (PMID 42938952; DOI 10.3390/bioengineering13101097; Bioengineering (Basel) 2026;13(10):1097; PMC13701952; authors Prabha/Collaco/Rosa Malena/Haider/Wood/Forte; article type Journal Article) AND Scite-confirmed (record present, OA gold CC-BY, NO editorial notices). source pubmed-verified; no identifier invented.

**Link:** https://doi.org/10.3390/bioengineering13101097
**DOI:** `10.3390/bioengineering13101097`
**PMID:** `42938952`

Topics: Patient-facing AI · AI safety failure modes · Emergency triage AI · Benchmark methodology

Index: [[00 INDEX — Patient-Facing AI Triage Safety]]
