# SCHEMA: IDEA

Output of `agents/generator.md`. One file per candidate: `runs/generated/idea_NN.md`.

Markdown with YAML frontmatter. Frontmatter holds machine-readable fields; the body holds reasoning.

## FRONTMATTER

| Field | Type | Required | Description |
|---|---|---|---|
| `id` | string | yes | e.g. `idea_01`. Matches the filename. |
| `title` | string | yes | Short name of the adaptation. |
| `model_family` | string | yes | `id` of the `data/model_families/` record being adapted. |
| `source_companies` | list | yes | `data/companies/` ids informing the adaptation. Evidence that the mechanism runs, not templates to clone. |
| `niche` | string | yes | The specific buyer group, defined by what they do, never by where they are. Geography is not a segmentation axis. |
| `delivery` | string | yes | How the work reaches the buyer online end to end. |
| `mechanism` | string | yes | One line: how value is created and captured. Detail goes in the body. |
| `adaptation` | string | yes | One line: what is deliberately different in the target market. |
| `cash_validation_cost` | number \| null | yes | Cash that must leave before the first customer payment, **excluding** the tooling carve-out in `config/founder_constraints.md`. Must be `0` to pass Gate 1. `null` when unknown — which makes Gate 1 BLOCKED, never PASS. |
| `cash_validation_cost_basis` | string | yes | How the figure was derived, or why it is unknown. Name every cost considered, including ones judged to fall under the carve-out. |
| `tooling_required` | list | yes | Subscriptions or tools the candidate relies on. Each must be general-purpose and one the founder would hold anyway; anything candidate-specific is cash, not tooling. |
| `revenue_before_cost` | string | yes | How customer payment precedes and funds the next increment of cost. Feeds Gate 8. |
| `hours_per_week_est` | number \| null | yes | Estimated operating load through validation. `null` → Gate 5 BLOCKED. |
| `assumptions` | list | yes | Things taken as true without evidence. Required by generator.md. |
| `unknowns` | list | yes | Things not known and not assumed. Feeds the evaluator's gate states. |
| `ceiling_annual_revenue` | number | yes | Plausible annual revenue ceiling in USD. Required - a candidate without one cannot reach DEEP_EXPLORE, because expected value needs a payoff term and "a ceiling worth chasing" is a word, not a number. |
| `ceiling_basis` | string | yes | How the figure was derived, citing the source company's disclosed revenue where one exists. |
| `revenue_horizon` | string | no | When first revenue is expected. Required in practice for any candidate claiming the long-horizon exception. |
| `interim_signals` | list | no | Specific checkable things that should be observably true at months two, four and eight. Required to claim the long-horizon exception in `rules/scoring_rubric.md`; without them a long wait scores 1. |
| `beachhead` | string | yes, from run 08 | The narrow first segment, and why it pays early. |
| `expansion_path` | list | yes, from run 08 | Ordered steps out of the beachhead into adjacent segments, each reusing what the previous step built. |
| `expansion_evidence` | string | yes, from run 08 | A real company that made the same expansion, with the evidence id. Like magnitude, the expansion path is reported alongside the score, never folded into it, because `economic_model` already judges the ceiling. |
| `created` | date | yes | Generation date. |

## BODY

Required sections, in order:

1. `## Mechanism` — the underlying economics of the proven model, stated independently of any one company.
2. `## Why the original works` — what actually makes the mechanism pay, and who pays whom.
3. `## What changes at solo scale` — what is different when a solo, zero-capital, online-only operator runs this instead of the funded company that proved it. Never geography.
4. `## Adaptation` — the designed adaptation, and why it follows from the differences above.
5. `## Assumptions` — each assumption, with why it is an assumption rather than a fact.
6. `## Unknowns` — each unknown, and which gate or dimension it threatens.

## RULES

The generator records unknowns; it does not resolve them. An unknown left honest here becomes a BLOCKED gate downstream, which is the intended behavior.

No claim in the body may be asserted as fact without an evidence reference. Unreferenced claims belong in `## Assumptions`.

Do not clone a source company's product or interface. The unit of adaptation is the mechanism.

## EXAMPLE

```markdown
---
id: idea_01
title: Vernacular loan comparison for tier-2 borrowers
model_family: aggregation_decision_monetization
source_companies: [nerdwallet]
niche: Solo agency owners running paid ads for clients
delivery: Async written deliverable plus one video call
mechanism: Aggregate loan terms, assist the choice, monetize via lender lead fees
adaptation: Vernacular-first, agent-assisted rather than self-serve search
cash_validation_cost: 0
cash_validation_cost_basis: No spend before first payment; drafting and outreach done with existing subscriptions
tooling_required: [Claude Code, existing AI subscription]
revenue_before_cost: Lender pays per qualified lead; no cost incurred until a lead converts
hours_per_week_est: 20
assumptions:
  - Lenders will pay per qualified lead without an existing relationship
unknowns:
  - Whether lead-gen for regulated credit products requires registration
created: 2026-09-20
---

## Mechanism
...
```
