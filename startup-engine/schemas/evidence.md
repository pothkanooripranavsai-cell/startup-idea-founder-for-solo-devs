# SCHEMA: EVIDENCE

One sourced claim. Stored as `data/evidence/ev_NNN.md`.

Markdown with YAML frontmatter. Referenced by id from gates and dimensions in an evaluation.

## FRONTMATTER

| Field | Type | Required | Description |
|---|---|---|---|
| `id` | string | yes | e.g. `ev_001`. Matches the filename. |
| `claim` | string | yes | The claim, stated precisely, with units and timeframe. |
| `classification` | string | yes | `FACT`, `INFERENCE`, `HYPOTHESIS`, or `UNKNOWN`. |
| `supports` | list | yes | What it bears on: `gate_3_tacit_network`, `dimension:transferability`, etc. |
| `supports_or_contradicts` | string | yes | `supports` or `contradicts`. Contradicting evidence is recorded, not discarded. |
| `source` | string | yes | Citation — URL or full reference. |
| `source_org` | string | yes | Organization that published it. |
| `underlying_source` | string | yes | The material it ultimately derives from — a press release id, dataset, filing, announcement. Two records sharing this value are **one** source, however many outlets carried it. |
| `source_tier` | string | yes | `primary`, `secondary`, `community`, or `promotional`. |
| `geography` | string | yes | Market the claim pertains to. Origin-market evidence does not establish target-market viability. |
| `as_of` | date | yes | When the claim was true. |
| `retrieved_at` | date | yes | When the source was accessed. |
| `freshness_sensitive` | boolean | yes | Whether currency matters for this claim's use. Structural facts are not freshness-sensitive. |
| `freshness_status` | string | yes | `current`, `stale`, or `not_applicable`. |
| `reasoning` | string | conditional | Required when `classification: INFERENCE`. The derivation, written out. |
| `conflicts_with` | list | no | Evidence ids this contradicts. |

## AGE AND CLASSIFICATION

These are independent axes and must stay that way.

Age never changes a classification. A FACT that is old is still a FACT — it is recorded as `classification: FACT` with `freshness_status: stale`. It then fails any check that requires currency, which is the correct consequence, rather than being demoted to INFERENCE or UNKNOWN.

`as_of` drives freshness. `retrieved_at` records only when the fetch happened and never affects classification.

## INDEPENDENCE

Two evidence records are independent sources only when `source_org` differs **and** `underlying_source` differs.

Three outlets reproducing one press release share an `underlying_source` and count as one. Recording `underlying_source` is what makes that detectable — without it, republication looks like corroboration.

## TIER RULES

`community` alone cannot support a `FACT`.

`promotional` is never sole support for a viability claim. Funding raised is not evidence that a model works.

## EXAMPLE

```markdown
---
id: ev_001
claim: NerdWallet derived the majority of 2024 revenue from lead and affiliate fees paid by financial institutions
classification: FACT
supports: [dimension:transferability, gate_7_distribution_access]
supports_or_contradicts: supports
source: https://...
source_org: US Securities and Exchange Commission
underlying_source: nerdwallet-10k-fy2024
source_tier: primary
geography: US
as_of: 2024-12-31
retrieved_at: 2026-09-20
freshness_sensitive: false
freshness_status: not_applicable
---

Context, caveats, and any conflict with other records.
```
