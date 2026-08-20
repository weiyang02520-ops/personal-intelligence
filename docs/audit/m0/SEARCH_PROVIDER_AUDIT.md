# M0 Search / Crawler / Community Connector Audit

Source tasks: TASK-M0-007, TASK-M0-008, TASK-M0-009  
Status: PARTIAL — provider facts and implementation behavior require later verification

## Provider capability matrix

| Candidate | Repository / source | Evidence point | License/status | Interface evidence | Decision candidate | Main gap |
|---|---|---|---|---|---|---|
| SearXNG | https://github.com/searxng/searxng | public metasearch HTTP API/docs | `5ffd32ca2f5e3648bcaa61ad18b94f258852edcb`, AGPL-3.0 | L2 candidate | ADAPT | Operator quality, engine availability, rate limits and result normalization |
| Brave Search | https://brave.com/search/api/ | official Search API docs/terms | Hosted API; not a PI dependency license claim | L2 candidate | ADAPT/UNKNOWN | Credential, cost, regional/terms and live response verification |
| Exa | https://exa.ai/ | official API docs | Hosted API | L2 candidate | ADAPT/UNKNOWN | Cost, terms, rate limits, freshness and live behavior |
| Tavily | https://tavily.com/ | official API docs | Hosted API | L2 candidate | ADAPT/UNKNOWN | Cost, terms, regional availability and live behavior |
| GitHub vertical | https://docs.github.com/en/rest/search | official GitHub REST search docs | Hosted service/API | L2 candidate | ADAPT | Auth/rate limits, pagination, code/search semantics and provenance |

The provider rows are candidates, not a selected M1 combination. Hosted APIs are not classified as open-source code reuse merely because an API exists.

## Required provider dimensions

| Dimension | Current evidence | Status |
|---|---|---|
| API stability/versioning | Official docs candidate only | PARTIAL |
| Query operators | Provider-specific; not normalized | PARTIAL |
| Pagination | Documented for some candidates; live shape not tested | PARTIAL |
| Metadata/provenance | Candidate fields exist; canonical PI mapping not tested | PARTIAL |
| Freshness | Provider-dependent | UNKNOWN |
| Cost/rate limits | Must be checked against account/terms | UNKNOWN |
| Regional availability/legal | Must be reviewed before selection | UNKNOWN |
| Structured output | Candidate API feature; schema normalization unverified | PARTIAL |

## Crawler / fetch / browser escalation ladder

1. Direct HTTP fetch for a known URL, bounded timeout and provenance capture.
2. Site crawl only when multiple same-site pages are required and robots/terms allow it.
3. Adaptive crawl when ordinary fetch misses material content and the source is permitted.
4. Browser fallback only for rendered/authenticated/interaction-dependent content, isolated and permissioned.
5. Stop and emit a typed failure when trust, permission, legal, cost or safety conditions are not met.

Candidate references:

| Candidate | Source | Candidate mode | Evidence | Risk |
|---|---|---|---|---|
| Crawl4AI | https://github.com/unclecode/crawl4ai | `7e801521428ee12509994d39151006f64055ebe3`, Apache-2.0 | L1/L2 candidate | Browser/runtime footprint and isolation |
| Firecrawl | https://github.com/firecrawl/firecrawl | `c76f4fd20044b4d60e289559bb029422ae1e6540`, AGPL-3.0 | L1/L2 candidate | Service/self-host boundary, cost, licensing and data handling |
| Browser Use | https://github.com/browser-use/browser-use | `85ddbfedf609166b2d2c76c3d80506649fee82a9`, MIT | L1/L2 candidate | Tool permissions, browser isolation and nondeterminism |
| Direct HTTP | Python standard/client boundary | REFERENCE / PI custom design | L1 | SSRF, parsing, robots/terms and provenance |

## Community-source adapter candidates

| Candidate | Source | Candidate capability | Classification | Unknown |
| SurfSense | https://github.com/MODSetter/SurfSense | community-source integrations / REST/MCP patterns; `2b50e7a4025582e0b6a3df097249f1e439362bce`, license metadata `NOASSERTION` | REFERENCE/ADAPT | Exact connector contracts, license interpretation, auth and maintenance at pinned commit |
| REST connector | Provider official API | stable source adapter boundary | ADAPT | Source-specific terms, pagination, error and provenance mapping |
| MCP connector | MCP server contract | tool/source integration pattern | ADAPT/UNKNOWN | Permission, trust, schema evolution and server quality |

## Search ownership guardrail

Search may own request-level query execution, provider selection and provider health candidate signals. Long-lived source identity, observation dedup, entity resolution and evidence assessment remain separate unresolved ownership questions from the blueprint; this audit does not merge them.

## PoC questions

- What is the smallest two-provider combination that produces stable provenance and pagination?
- Can direct HTTP satisfy the common case without browser escalation?
- Which crawler license/hosting model is compatible with the repository and user deployment?
- How are source terms, rate limits, SSRF controls and untrusted content represented in the future contract?
