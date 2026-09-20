---
id: nonconsensual_public_ranking
name: Publicly ranking or comparing named third parties who did not opt in
model_family: artifact_embedded_distribution
company: null
region: [not_applicable]
failure_reason: unmanageable_liability
failure_detail: A benchmark or comparison built entirely from public information, ranking identifiable companies or people who were not asked and did not agree to be included, differs from every proven instance of artifact_embedded_distribution examined in this project. G2's reviewed vendors and RankInPublic's compared products both opted into inclusion. A search for whether unsolicited public ranking of identifiable businesses carries distinct legal exposure - defamation, unfair competition, platform liability - did not resolve either way, and resolving it properly requires legal judgement this project cannot supply.
still_applies: yes
still_applies_reason: The exposure is structural, not evidentiary. A zero-capital solo founder has no legal resources to absorb a dispute if the risk materialises, and no amount of further desk research changes that capacity. This is not the same as an ordinary BLOCKED gate awaiting one cheap search - it is a risk this founder specifically cannot afford to be wrong about, which is why it is recorded as a standing caution rather than left as an open unknown on one candidate's file.
classification: HYPOTHESIS
source_tier: community
as_of: 2026-09-20
evidence: []
---

# Publicly ranking or comparing named third parties who did not opt in

## What it looks like

Take the artifact-sharing mechanism that works when participants choose to be compared (`data/model_families/artifact_embedded_distribution.md`), and apply it to parties who did not choose anything — build a benchmark from public data and rank real, named companies or people against each other without their participation.

It is tempting because it appears to solve the family's one remaining weakness: G2 and RankInPublic both still need participants to show up voluntarily. Ranking without consent looks like it removes that dependency and lets the operator include everyone relevant from day one.

## What actually goes wrong

The two proven instances of this mechanism are proven specifically as *voluntary* systems. Nothing in `ev_024` or `ev_025` establishes that the sharing incentive, the credibility, or the legal safety of the mechanism survives removing consent from the design.

A subject who is ranked unfavourably and did not agree to appear has a live grievance a voluntary reviewer does not. Whether that grievance has legal teeth was not resolved by the research done for `idea_19`, and that is itself the finding: it is not a settled-safe pattern, and treating the open question as a minor unknown understates what is actually at stake for a founder with zero legal resources.

## Why this is recorded as HYPOTHESIS rather than a firmer classification

No actual dispute, lawsuit, or enforcement action was found or sourced — this is not a record of an observed failure the way `lead_data_products.md` is. It is a structural caution derived from the absence of consent in a mechanism whose only proven instances have it. The classification reflects that: a reasoned expectation, not a documented event.

## What would change this

A specific legal analysis of comparative-ranking liability for a given jurisdiction and a given ranking methodology, or a sourced instance of a solo operator running a non-consensual public ranking without incident over a sustained period. Neither exists in this corpus.

## What still works

The underlying `artifact_embedded_distribution` mechanism is not closed by this record — only the non-consensual variant is. A future candidate built on voluntary participation, the way both proven instances are, does not inherit this caution.
