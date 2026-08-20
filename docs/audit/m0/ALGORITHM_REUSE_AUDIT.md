# M0 Algorithm Reuse Audit

Source tasks: TASK-M0-005, TASK-M0-006  
Status: PARTIAL — strategy references, not accepted algorithms

## Deep research capability reuse map

| Candidate | Repository/source | Relevant capability | Evidence | Candidate classification | Failure/fit gap |
|---|---|---|---|---|---|
| LangChain Open Deep Research | https://github.com/langchain-ai/open_deep_research | research orchestration, query planning, report synthesis | L1/L2 candidate; `1b7d2e80db9faa586165c60e09096dbbfd483a64`, MIT | REFERENCE/ADAPT | LangGraph/LangChain coupling, state/provenance mapping and behavior pin |
| GPT Researcher | https://github.com/assafelovic/gpt-researcher | research loop, source collection, report/citation patterns | L1/L2 candidate; `5d84d2f5553e70a2765a8ff3a0d2672d60437ce8`, Apache-2.0 | REFERENCE/ADAPT | broad framework coupling, citation quality and runtime control |
| Deep Searcher | https://github.com/zilliztech/deep-searcher | deep-search orchestration and retrieval patterns | L1 candidate; `d89e37cdfbbef5e44ae6162ce9cc2c627a69b7e1`, Apache-2.0 | REFERENCE/UNKNOWN | exact behavior and integration boundary unverified |

M0 conclusion: these are useful comparison/reference candidates. No direct dependency or copied loop is authorized.

## Discovery strategy cards

| Strategy | Reference | Capability signal | Classification | PoC question |
|---|---|---|---|---|
| Perspective discovery | STORM / Co-STORM: https://github.com/stanford-oval/storm | multiple perspectives and research planning | L1/L2; `fb951af7744dab086e34962e9bc6fe878e145f83`, MIT | REFERENCE | Does perspective coverage improve source diversity without runaway cost? |
| Dynamic graph / iterative research | MindSearch: https://github.com/InternLM/MindSearch | dynamic question/source graph candidate | L1/L2 partial; `7952c5f8a956fe6a44228a6a7d528a35340e7c87`, Apache-2.0 | REFERENCE/UNKNOWN | Can graph state map to PI Discovery without owning Evidence? |
| Alibaba DeepResearch family | https://github.com/Alibaba-NLP/DeepResearch | long-horizon planning and tool use references | L1/L2 partial; `f72f75d8c3eb842f2bbbab096a12206ff66e270f`, Apache-2.0 | REFERENCE/UNKNOWN | Which stopping/recovery patterns are reproducible and license-compatible? |
| Context compression | multiple deep-research baselines above | reduce context while preserving citations | REFERENCE | What evidence-preserving compression invariant is required? |
| Outline/gap/stopping | STORM/ODR/GPT Researcher references | outline, missing-angle and stopping heuristics | REFERENCE | Which heuristic can be benchmarked without freezing M1 behavior? |

## Capability answers

Perspective discovery: candidate references exist; no verified PI integration.  
Dynamic graph: candidate references exist; ownership and persistence unknown.  
Question expansion: candidate capability likely present in research baselines; exact callable boundary unknown.  
Context compression: reference only; citation-preservation behavior unverified.  
Outline construction: reference only.  
Gap detection: reference only.  
Stopping: reference only; thresholds remain M1 experiment decisions.  
Source coverage: reference only; evidence/source ownership remains unresolved.  
Candidate verification: reference only; must not move identity ownership into Discovery.

## Guardrail

No algorithm is `REUSE` or `ACCEPTED` based on README/paper existence. The future Strategy Registry must preserve strategy, evidence, failure modes, fit and benchmark question separately.
