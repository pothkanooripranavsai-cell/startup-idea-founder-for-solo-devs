# SCHEMA: MODEL FAMILY

A proven economic mechanism, defined independently of any company that runs it. Stored as `data/model_families/<id>.md`.

A model family is defined by **how value is created and captured**, not by a product category. "Comparison site" is a category. "Aggregate information → assist a decision → monetize the resulting transaction" is a mechanism.

## FRONTMATTER

| Field | Type | Required | Description |
|---|---|---|---|
| `id` | string | yes | Matches the filename. |
| `name` | string | yes | The mechanism, named. |
| `mechanism` | string | yes | One line: the value-creation and capture loop. |
| `instances` | list | yes | `data/companies/` ids running this mechanism. |
| `company_count` | number | yes | Number of companies recorded. |
| `independent_company_count` | number | yes | Companies that are genuinely separate operations — not subsidiaries, spinouts, or the same operator under another name. |
| `revenue_evidenced_count` | number | yes | Companies with actual evidence of sustained revenue, as opposed to funding or press coverage. |
| `differentiating_axes` | list | yes | The dimensions on which instances genuinely differ. Required — see below. |
| `typical_validation_capital` | string | yes | Cost of the smallest real test, or `UNKNOWN`. |
| `typical_scaling_capital` | string | no | Recorded separately. Never justifies a candidate at validation stage. |
| `domain_expertise_required` | string | yes | Be explicit about tacit knowledge, or `UNKNOWN`. |
| `network_required` | string | yes | Relationships the operator needs, or `UNKNOWN`. Rarely visible in public stories. |
| `known_regions` | list | yes | Where the mechanism demonstrably operates. |
| `target_market_presence` | string | yes | `proven`, `partial`, `none`, or `UNKNOWN`. |
| `known_failures` | list | no | `data/failures/` ids for this mechanism. |
| `evidence` | list | yes | `data/evidence/` ids supporting the proof claim. |

## THE THREE COUNTS

These are tracked separately and never conflated.

`company_count` is how many instances are on file. `independent_company_count` removes instances that are not genuinely separate operations. `revenue_evidenced_count` is the only one that speaks to whether the mechanism actually pays — funding raised is not revenue, and press coverage is not evidence.

A family with many companies and a `revenue_evidenced_count` of one is weakly proven, however long the instance list looks.

## DIFFERENTIATING AXES

Instances of a mechanism are not interchangeable. Record the axes on which they differ and preserve those differences in the company records, because the differences usually determine whether the mechanism transfers.

Typical axes: where the aggregated information comes from, how the operator is paid, what kind of decision the buyer is making, what the moat is, and what regulatory exposure the category carries.

Flattening distinct operators into one generic category destroys exactly the information adaptation depends on.

## BODY

1. `## Mechanism` — the loop, stated without reference to any single company.
2. `## Why it pays` — what makes buyers and payers keep participating.
3. `## How instances differ` — one paragraph per differentiating axis.
4. `## Requirements` — capital, expertise, network, regulatory exposure.
5. `## Open questions` — what is UNKNOWN about this family.

## SURVIVORSHIP FIELDS

| Field | Type | Required | Description |
|---|---|---|---|
| `attempt_denominator` | number \| `UNKNOWN` | yes | How many operators are known to have *attempted* this mechanism, successes and failures together. |
| `denominator_basis` | string | yes | How it was established, or why it could not be. |

Every source company in this corpus is one that survived. A count of successes without a denominator is survivor-selected and says little about the odds of a new attempt. `scripts/score.py` prints this on every run and states plainly when it is `UNKNOWN`, rather than letting `revenue_evidenced_count` read as proof of good odds.

Expect `UNKNOWN` to be the honest answer in most cases. Record it as such rather than leaving the field off.
