# HARD GATES

Applied before scoring. Each gate is marked PASS / FAIL / BLOCKED.

Gate ids are stable and are the keys used in `schemas/evaluation.md`.

## GATE STATES

* **PASS** — evidence shows the constraint is satisfied.
* **FAIL** — evidence shows the constraint is violated. Candidate is rejected.
* **BLOCKED** — cannot be determined from available evidence.

BLOCKED is never treated as PASS.

A candidate with any FAIL is rejected.

A candidate with any BLOCKED gate does not proceed to scoring until the gate is resolved.

## GATE 1: VALIDATION CAPITAL

`gate_1_validation_capital`

Can the adaptation be validated with zero founder cash?

The ceiling is zero, in any currency. The question is not "is this cheap" but "does any money leave before a customer pays".

* FAIL if any cash outlay is required before the first customer payment.
* BLOCKED if the cash cost of a minimum test is unknown.
* PASS only if the first real test can be run at zero cash outlay.

Deterministic: `cash_validation_cost <= validation_capital_ceiling`, which at a ceiling of 0 means the cost must be exactly 0.

**The tooling carve-out.** General-purpose AI and software subscriptions the founder holds anyway are excluded from `cash_validation_cost`, per `config/founder_constraints.md`. The carve-out is narrow. Advertising, inventory, infrastructure, per-customer costs, deposits, fees, paid help, and candidate-specific software purchases are all cash and all count.

Do not let a real cost pass by being relabelled a subscription. The test is whether money leaves before a customer pays.

Scaling capital is not considered here. Gate 8 handles it.

## GATE 2: DEEP DOMAIN EXPERTISE

`gate_2_domain_expertise`

Can the adaptation be operated without deep domain expertise?

* FAIL if competent operation requires expertise the founder does not have.
* BLOCKED if the required depth of expertise is unknown.

**Boundary with Gate 3.** Apply this test: if the knowledge is available through documented, public means — courses, manuals, published playbooks, regulations one can read — it is *learnable* and belongs to Gate 2. If it transfers only through relationships, apprenticeship, or time inside an industry, it is *tacit* and belongs to Gate 3. Knowledge that is learnable but slow scores low on the Domain/tacit fit dimension rather than failing this gate.

## GATE 3: TACIT EXPERTISE / NETWORK

`gate_3_tacit_network`

Can the adaptation be operated without tacit knowledge or pre-existing relationships?

* FAIL if it depends on supplier, distributor, institutional, or customer relationships the founder does not have.
* BLOCKED if the original operators' starting relationships are unknown.
* Absence of evidence of a network requirement is not evidence of its absence.

## GATE 4: CREDENTIALS / REGULATION

`gate_4_credentials_regulation`

Can the adaptation be operated without credentials or regulatory approval the founder cannot obtain?

* FAIL if the activity is regulated in a way that requires licensure, registration, or approval anywhere the founder would need it to sell.
* BLOCKED if the regulatory status of the activity is unknown.

Do not reason about a specific country. Ask whether the *activity itself* is a regulated one — handling client money, giving financial or medical or legal advice, brokering regulated products. Unregulated activities sold online to whoever will buy do not raise this gate.

At a zero ceiling, any registration carrying a fee also fails Gate 1.

## GATE 5: SOLO OPERABILITY

`gate_5_solo_operability`

Can one person operate the adaptation through validation?

* FAIL if the model requires a team, shifts, or parallel roles before revenue.
* BLOCKED if the operational load is unknown, or if the founder's available hours are unset.
* Post-validation hiring is not considered here.

Deterministic, against the band in `config/founder_constraints.md`:

* `hours_per_week_est <= hours_per_week` (20) — PASS
* `hours_per_week <  hours_per_week_est <= hours_per_week_stretch` (21–30) — BLOCKED, because the capacity is plausible but not committed
* `hours_per_week_est >  hours_per_week_stretch` (30) — FAIL
* unknown estimate — BLOCKED

Paid help is unavailable before revenue, so "could be outsourced" is not a route to PASS. Neither is future capacity from holidays or additional people: that arrives after revenue, and a candidate operable only once someone else joins has not been validated by this founder.

## GATE 6: PHYSICAL DEPENDENCY

`gate_6_physical_dependency`

Is the adaptation wholly online?

* FAIL if any part of it — acquisition, sale, delivery, support, payment — requires anything physical: inventory, shipping, warehousing, equipment, premises, in-person attendance, site visits, or local presence.
* BLOCKED if the delivery mechanics are unclear.
* PASS only if every part happens over the internet.

A service delivered by video call is online. A service requiring the operator to be somewhere is not.

## GATE 7: DISTRIBUTION ACCESS

`gate_7_distribution_access`

Is there a plausible first-customer acquisition path accessible online at zero spend, to a founder with no audience and no reputation?

Accessible means it does not require an existing reputation, institutional relationships, a network the founder cannot reach, or paid acquisition.

* FAIL if every known path to first customers depends on an existing audience, reputation, institutional access, relationships the founder lacks, or advertising spend.
* BLOCKED if how comparable operators acquire their first customers is unknown.
* PASS if at least one plausible unpaid path exists, recorded with its reasoning.

Paid acquisition is not merely expensive here, it is unavailable. A model whose only proven acquisition channel is advertising fails this gate regardless of how well the channel performs for funded operators.

This gate is a judgment about access, not a budget comparison. How *difficult* the accessible path is belongs to the Distribution dimension in `rules/scoring_rubric.md`.

## GATE 8: SELF-FUNDING

`gate_8_self_funding`

Can customer payments fund subsequent development and operations?

* FAIL if the model requires outside funding to reach or sustain operation.
* FAIL if it only works at a scale unreachable without capital — a mechanism whose unit economics need volume the founder cannot buy their way to.
* FAIL if costs arrive structurally ahead of revenue, so that operating the business at all requires a float the founder does not have.
* BLOCKED if the timing of costs against revenue is unknown.
* PASS if revenue can plausibly precede and then fund the next increment of cost.

The question is order, not size. A business with high costs that customers pay for in advance passes. A business with low costs that must all be incurred before anyone pays does not.

Funding raised by the original operators is relevant evidence here. If every known instance of the mechanism required capital to reach viability, that is a reason to FAIL this gate, not a detail to note and move past.

## RECORDING

Record the state and the reason for every gate, including PASS.

Record the evidence each state rests on.

Do not mark PASS on inference alone where a FACT is obtainable.
