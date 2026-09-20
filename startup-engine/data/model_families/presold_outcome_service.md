---
id: presold_outcome_service
name: Pre-sold fixed outcome, delivered manually, productised from revenue
mechanism: Sell a specific named outcome at a flat price before it can be delivered efficiently, deliver it by hand, and use the revenue to automate what recurs
instances: [zappos]
company_count: 1
independent_company_count: 1
revenue_evidenced_count: 0
mechanism_proof_only: true
differentiating_axes: [outcome_sold, buyer_urgency, manual_delivery_cost, automatable_fraction, recurrence]
typical_validation_capital: Zero at the sequencing level the mechanism describes - the one recorded instance did not itself stay zero-capital past the validation phase, see the caution below
typical_scaling_capital: The recorded instance required outside capital to scale past manual delivery. Untested whether a fully digital, solo version avoids this.
domain_expertise_required: UNKNOWN - depends entirely on the outcome sold
network_required: UNKNOWN
known_regions: [not_applicable]
target_market_presence: not_applicable
known_failures: []
evidence: [ev_010, ev_011, ev_023]
---

# Pre-sold fixed outcome, delivered manually, productised from revenue

## Mechanism

Rather than building something and then seeking buyers, name a specific outcome, sell it at a flat price, and deliver it by hand. The buyer pays for the result, indifferent to how it is produced. Whatever recurs across deliveries is then automated, funded by the revenue the deliveries generated.

## Why it pays

The ordering is the whole point. Revenue arrives before the build, which means the build is funded by customers rather than by capital, and is informed by work already paid for rather than by guesses (`ev_010`).

This is the only mechanism on file whose defining property is that money comes first. Every other family here requires an audience, a corpus, or an integration before anyone pays.

A second, less obvious property: a failed attempt costs nothing but time. If nobody buys the outcome, no asset was built and no money was spent — the negative result arrives early and cheap.

## How instances differ

**One instance is recorded, and it is a mechanism proof rather than a transferable business.** Zappos (`ev_023`) is real, famous, and independently well documented — but it is a physical-goods company that needed outside capital to move past its manual-fulfilment phase. `mechanism_proof_only: true` is set deliberately: this record establishes that the *sequencing* (sell, deliver manually, automate from revenue) works at the scale of a 1.2-billion-dollar acquisition. It does not establish that the sequencing stays zero-capital, solo, or online-only past validation, because in its one recorded instance it did not.

`revenue_evidenced_count` stays at 0 for that reason. Zappos's revenue does not evidence that *this* founder's constraints are compatible with the mechanism past the first sale — it evidences that the ordering itself is sound.

What else exists is documentation of the practice (`ev_010`, community tier) and one uncorroborated case study recorded as HYPOTHESIS rather than fact (`ev_011`). No solo, zero-capital, online-only operator has been sourced running this mechanism to a sustained, self-funded business.

The axes on which real instances would differ, once found: what outcome is sold, how urgent the buyer's need is, how expensive manual delivery is, what fraction of the work is actually automatable, and whether the outcome recurs or is one-shot.

That last axis decides whether this becomes a business or stays a job. A one-shot outcome means hunting a new buyer every time; a recurring one compounds.

## Requirements

Capital: zero by construction.

Expertise: entirely dependent on the outcome sold. Selling an outcome you cannot personally deliver is not a version of this mechanism, it is fraud.

Network: `UNKNOWN`, and the same first-customer problem applies as everywhere else. An outcome sold to strangers requires a reason for a stranger to trust the seller.

## Open questions

Whether any named, verifiable operator has run this successfully **while staying solo, zero-capital and online-only past the first sale**. Zappos closes the "does the sequencing work at all" question and leaves this one open — its own answer was capital, not continued bootstrapping.

What fraction of the manual work is genuinely automatable, as opposed to appearing automatable before the work is understood.

Whether the outcome can be specified tightly enough that a stranger will buy it without a call, which determines whether acquisition can be asynchronous.
