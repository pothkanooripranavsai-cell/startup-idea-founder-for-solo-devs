# SCHEMA: COMPANY RECORD

A specific company running a model family's mechanism. Stored as `data/companies/<id>.md`.

Companies are evidence that a mechanism pays. They are not templates to clone, and they are not interchangeable with each other.

## FRONTMATTER

| Field | Type | Required | Description |
|---|---|---|---|
| `id` | string | yes | Matches the filename. |
| `name` | string | yes | Company name. |
| `model_family` | string | yes | The `data/model_families/` id whose mechanism it runs. |
| `region` | list | yes | Where it operates. |
| `founded` | date \| null | yes | Founding date, or `null`. |
| `status` | string | yes | `active`, `acquired`, `shut_down`, or `UNKNOWN`. |
| `information_source` | string | yes | Where its aggregated information comes from — editorial, user-generated, merchant feed, licensed data. |
| `monetization` | string | yes | How it is actually paid — affiliate, lead fee, vendor subscription, CPC, transaction cut. |
| `buyer_decision` | string | yes | What decision its users are making. |
| `moat` | string | yes | What makes it hard to displace, or `UNKNOWN`. |
| `revenue_evidenced` | boolean | yes | Whether sustained revenue is evidenced. Funding is not revenue. |
| `revenue_evidence` | string | yes | What the evidence is, or why it is `UNKNOWN`. |
| `independent` | boolean | yes | Whether it is a genuinely separate operation, not a subsidiary or rebrand of another instance. |
| `founder_advantage` | string | yes | What the founders started with — expertise, audience, relationships — or `UNKNOWN`. Often the hidden requirement. |
| `regulatory_exposure` | string | yes | Regulatory constraints on its category, or `none`. |
| `evidence` | list | yes | `data/evidence/` ids. |

## RULES

`revenue_evidenced` is the field that decides whether this company counts toward a model family's `revenue_evidenced_count`. Set it `true` only on evidence of revenue, never on funding raised, headcount, press coverage, or valuation.

`founder_advantage` is the field most often quietly wrong. A company whose founders began with an audience, an industry network, or years of domain practice tells you the mechanism may carry a requirement its public story omits. When the founders' starting position is not documented, the value is `UNKNOWN` — never an assumed "none".

`information_source`, `monetization`, `buyer_decision`, and `moat` exist to keep instances distinguishable. Do not fill them with the model family's generic description.

## BODY

1. `## What it does` — one paragraph.
2. `## How it makes money` — the actual payer and the actual trigger for payment.
3. `## What made it work` — including any founder advantage.
4. `## How it differs from other instances` — the point of the record.
5. `## Open questions` — what is UNKNOWN.
