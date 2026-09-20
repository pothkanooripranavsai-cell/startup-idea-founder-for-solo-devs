# SCHEMA: MARKET FACT

A discrete, sourced fact about a market. Stored as `data/market/<id>.md`.

## FRONTMATTER

| Field | Type | Required | Description |
|---|---|---|---|
| `id` | string | yes | Matches the filename. |
| `statement` | string | yes | The fact, stated precisely, with units and timeframe. |
| `fact_type` | string | yes | One of `size`, `growth`, `buyer_behavior`, `pricing_norm`, `regulatory`, `competition`, `other`. |
| `value` | number \| null | no | Numeric value, if applicable. |
| `unit` | string | no | Unit for `value`. |
| `geography` | string | yes | The market it describes. A fact about one market says nothing about another. |
| `classification` | string | yes | `FACT`, `INFERENCE`, `HYPOTHESIS`, or `UNKNOWN`. |
| `source` | string | yes | Citation. |
| `source_org` | string | yes | Publishing organization. |
| `underlying_source` | string | yes | The material it derives from. Two records sharing this value are one source. |
| `source_tier` | string | yes | `primary`, `secondary`, `community`, or `promotional`. |
| `as_of` | date | yes | When the fact was true. |
| `retrieved_at` | date | yes | When the source was accessed. |
| `freshness_sensitive` | boolean | yes | Whether currency matters for this fact's use. |
| `freshness_status` | string | yes | `current`, `stale`, or `not_applicable`. |

## RULES

Market sizing from vendors selling into that market is `promotional` tier. Treat accordingly — it is never sole support for a viability claim.

Age does not demote a fact. An old market size is still a fact about that date, recorded `FACT` with `freshness_status: stale`, and it fails any check requiring currency.

`geography` is load-bearing. Origin-market facts support the claim that a mechanism works somewhere; they do not support local viability.

## BODY

The fact in context: what it does and does not establish, and any conflicting figure with its source.
