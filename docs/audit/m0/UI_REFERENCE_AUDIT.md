# M0 UI Reference Audit

Source task: TASK-M0-010  
Status: PARTIAL — reference inventory only; no brand or implementation copied

| Candidate | Source | Primitive/pattern candidate | Evidence | Classification | Gap |
|---|---|---|---|---|---|
| Morphic | https://github.com/miurla/morphic | research/search workspace hierarchy and result presentation; `d4aba02a14a5cb2c6ed0e7ef917123a681b05f14`, Apache-2.0 | L1/L2 candidate | REFERENCE | Exact component extraction pending |
| Vane | https://github.com/ItzCrazyKns/Vane | visual interaction/reference candidate; `7dc5d088f7262fbc5e39037f84940a8a2193c5fb`, MIT | L1/L2 candidate | REFERENCE | Exact component fit pending |
| DeerFlow frontend | https://github.com/bytedance/deer-flow | runtime/research UI information hierarchy; commit `a5acc25de6742b2166b3f41c97bd895822277b94` | L1 | REFERENCE | Component/API behavior and license-level reuse not inspected |
| CC Switch | https://github.com/farion1231/cc-switch | provider/configuration interaction reference; `0b5da510168914b251481654a568c3ffacd62cf4`, MIT | L1/L2 candidate | REFERENCE | Visual reference must not become brand/code copy |

## Reusable primitives to validate later

- Dense source/result list with explicit provenance.
- Run status and event timeline with cancellation affordance.
- Evidence/claim detail panel with confidence and source links.
- Provider/configuration state presented separately from Product Core state.
- Clear empty/error/partial-result states.

These are information-architecture references, not accepted UI components. Exact colors, width, radius and brand treatment remain M4/non-blocking decisions per the Blueprint.

## Constraints

UI must call PI Public API only; no external product branding, proprietary assets or unverified code is copied. License and component-level reuse require a later explicit review.
