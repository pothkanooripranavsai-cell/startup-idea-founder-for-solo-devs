---
id: public_corpus_aggregation
name: Public corpus aggregation with demand-side subscription
mechanism: Assemble a corpus that is already public but scattered across thousands of sources and structurally uniform, parse it into the fields that matter, and sell filtered access to whichever side is underserved by the scatter
instances: [remote_rocketship]
company_count: 1
independent_company_count: 1
revenue_evidenced_count: 1
differentiating_axes: [corpus_source, structural_uniformity, refresh_rate, which_side_is_desperate, permissibility]
typical_validation_capital: Zero. The corpus is public and free, the parsing runs on ordinary tooling, and no supplier is paid or contacted.
typical_scaling_capital: None evidenced. The single instance is solo and unfunded.
domain_expertise_required: Low. Knowing which fields a buyer filters on requires understanding the buyer, not the industry.
network_required: None. This is the mechanism's defining property and the reason it was separated from niche_listing_board.
known_regions: [not_applicable]
target_market_presence: not_applicable
attempt_denominator: UNKNOWN
denominator_basis: Not established. Every instance on file is one that survived; no source records how many operators attempted this mechanism and failed, so the success count here is survivor-selected and is not evidence about odds.
known_failures: []
evidence: [ev_016, ev_017, ev_018, ev_022]
---

# Public corpus aggregation with demand-side subscription

## Mechanism

Some valuable information is already public and still hard to use, because it is scattered across thousands of separate sources that each publish a fragment. No single publisher has an incentive to consolidate it, and every consumer of it pays the search cost individually.

The operator consolidates it, parses it into comparable fields, and charges the party who was paying that search cost.

## Why it is separated from `niche_listing_board`

They look alike and are not. The distinction is who pays and what must be assembled first.

`niche_listing_board` concentrates an audience and charges the supply side per listing. It therefore needs an audience before anyone pays, which is the cold-start problem that stalled candidates across runs 02 and 03.

This family never contacts the supply side. The inventory is taken from public sources, and the *demand* side subscribes. Assembling inventory stops being a business problem and becomes an engineering one.

`ev_017` establishes the distinction concretely: the instance scrapes applicant tracking systems and company pages, no employer posts or is contacted, and job seekers pay 5 dollars weekly or 18 monthly.

## Why it pays

The buyer is not paying for information they could not obtain. They are paying to stop paying the search cost. That is a weaker-sounding proposition than exclusivity and in practice a more durable one, because the scatter that creates the cost is structural - it exists because thousands of publishers each act independently, and none of them will ever consolidate.

Price is correspondingly low and recurring rather than high and occasional. The single evidenced instance sits at a few dollars a week and around 6000 dollars monthly.

## Distribution is an output, not an input

This is the property that distinguishes the family from everything else examined in this project.

A parsed corpus of thousands of entries is thousands of indexable pages, each answering a specific query somebody is already typing. Search traffic is therefore produced by the asset rather than supplied by the founder. `ev_018` attributes the instance's sustained traffic to search.

Set against `data/failures/audience_first_product_launch.md`, which records that the celebrated solo online businesses were launched into audiences their founders spent years building, this is the material difference. The audience is an output here.

## The four tests a corpus must pass

Drawn from the single instance, and unvalidated against any other, so they are a hypothesis about the family rather than a finding:

1. **Public** - obtainable without payment, credentials, or permission.
2. **Scattered** - spread across enough sources that consolidating is genuinely useful.
3. **Structurally uniform** - enough sources share a format that parsing is tractable for one person.
4. **Continuously refreshed** - the corpus decays, so the buyer keeps paying.

A corpus failing any one of these breaks the mechanism. Failing the fourth turns a subscription into a one-off sale.

## How instances differ

Only one instance is on file, so the differentiating axes are recorded from reasoning rather than observed variation. This is a weakness of the family record and should be stated as such wherever it is used.

**Which side is desperate** is the axis that decides monetisation. The corpus is the same either way; the payer is whoever bears the search cost most acutely.

**Permissibility** is the axis that decides whether a candidate is viable at all. It was bounded in run 04 rather than left open - see the section below.

## Permissibility, bounded in run 04

Researched under the `idea_13` deep research pass and now carrying a rule rather than an open risk.

The Ninth Circuit held that accessing a public page with no access permissions cannot violate the CFAA. In the same litigation the scraper settled with a 500000 dollar judgment, conceded trespass to chattels and misappropriation, and was enjoined (`ev_022`). It won the statute and lost the case.

The exposure attached to the counterparty rather than to the activity: a single platform that objected, had sent a cease and desist, and asserted interests in its own compiled database.

**The operating rule for this family: take from primary publishers, never from another aggregator's compilation.** Employer career pages and applicant tracking systems publish openly in order to be found, so collection serves the publisher's interest rather than opposing it, which is the favourable side of the line.

This is INFERENCE, not clearance. The specific terms of service of specific source systems have not been read, and that is the cheapest outstanding research task attached to this family.

## Open questions

Whether the mechanism generalises off job postings at all. Every fact on file comes from one instance in one corpus. The four tests above are a generalisation from a single case and nothing yet confirms that a second corpus behaves the same way.

How long the search channel takes to produce revenue from a standing start. The instance's first traffic came from a viral post, which is not reproducible, and nothing records how long the durable channel would have taken alone.
