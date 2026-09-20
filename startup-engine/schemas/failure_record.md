# SCHEMA: FAILURE RECORD

A documented failure, recorded so a known failure mode is not repeated unexamined. Stored as `data/failures/<id>.md`.

## FRONTMATTER

| Field | Type | Required | Description |
|---|---|---|---|
| `id` | string | yes | Matches the filename. |
| `name` | string | yes | Company or product name. |
| `model_family` | string | yes | The `data/model_families/` id whose mechanism failed. Required — a failure not linked to a mechanism cannot be found when that mechanism is next considered. |
| `company` | string \| null | yes | `data/companies/` id, if one exists. |
| `region` | list | yes | Where it operated. |
| `failure_reason` | string | yes | One of `timing`, `distribution`, `unit_economics`, `regulation`, `team`, `no_demand`, `competition`, `capital`, `other`. |
| `failure_detail` | string | yes | The specific mechanism of failure, not the category. |
| `still_applies` | string | yes | `yes`, `no`, or `UNKNOWN` — whether the cause still blocks new entrants. |
| `still_applies_reason` | string | yes | Why, or why not. `UNKNOWN` is acceptable; a guess is not. |
| `classification` | string | yes | `FACT`, `INFERENCE`, `HYPOTHESIS`, or `UNKNOWN` for the failure account itself. |
| `source_tier` | string | yes | `primary`, `secondary`, `community`, or `promotional`. |
| `as_of` | date | yes | When the failure occurred. |
| `evidence` | list | yes | `data/evidence/` ids. |

## RULES

Post-mortems are frequently self-serving and are often `community` or `promotional` tier. A founder's account of why their company failed is evidence of what they believe, which is not the same as evidence of what happened. Classify accordingly.

`still_applies` is the field the gates actually consume. A failure whose cause has since disappeared is useful context; a failure whose cause persists is a reason to reject. `UNKNOWN` routes to research rather than either conclusion.

The absence of recorded failures for a mechanism is not evidence that it is safe. It usually means no one has looked.

## BODY

1. `## What they built`
2. `## What actually went wrong` — the mechanism, not the label
3. `## Does it still apply` — with reasoning
4. `## Open questions`
