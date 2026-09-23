---
validation_capital_ceiling: 0
tooling_subscriptions_allowed: true
hours_per_week: 20
hours_per_week_stretch: 30
team_size: 1
team_size_scope: validation_only
team_after_revenue: allowed
domain_expertise: generalist
funding_mode: customer_funded_to_first_revenue
funding_after_revenue: any_including_external
delivery: fully_digital
geography: irrelevant
---

# FOUNDER CONSTRAINTS

Read first by both `agents/generator.md` and `agents/evaluator.md`.

## NO GEOGRAPHY

Geography is not a constraint and is not a consideration.

Do not reason about a home country, a local market, local buyer behaviour, local regulation, local payment habits, or national advantage. Do not generate candidates framed as "X for country Y", and do not treat a mechanism's country of origin as a reason for or against it.

The founder sells to whoever on the internet will pay. The relevant unit is the **niche**, not the nation.

When a gate or dimension would previously have asked "does this transfer to the target market", it now asks whether the mechanism survives being run by a solo, zero-capital, online-only operator rather than by the funded company that proved it.

## ONLINE ONLY

The business must be **wholly online**. Every part of it — finding buyers, selling, delivering, supporting, getting paid — happens over the internet.

Disqualifying at Gate 6: anything physical. Inventory, shipping, warehousing, premises, equipment, manufacturing, in-person delivery, site visits, local presence, anything that must be touched or attended.

A service delivered by video call is online. A service requiring the operator to be somewhere is not.

## VALIDATION CAPITAL: ZERO

`validation_capital_ceiling` is **0**, in any currency.

There is no cash to validate a candidate. Any candidate requiring cash outlay before its first customer payment fails Gate 1.

## THE TOOLING CARVE-OUT

`tooling_subscriptions_allowed` is true. The founder operates with existing resources plus AI and software subscriptions, treated as a standing operating expense rather than per-candidate validation capital.

The carve-out is narrow and is not a budget. It covers general-purpose subscriptions the founder would hold anyway — Claude Code, an AI API plan, ordinary software tooling.

It does not cover: advertising or any paid acquisition; per-customer or per-transaction costs that scale with volume; deposits, licences, registrations, or professional fees; contractors, freelancers, or any paid help; candidate-specific software bought only to make one idea work; paid data, paid APIs priced per call, or paid placement.

A candidate whose economics depend on spending merely *described* as a subscription fails Gate 1. The test is whether real money leaves before a customer pays.

## SELF-SUSTAINING REQUIREMENT

Four conditions, all required:

1. Validation begins at zero cash.
2. First customers are acquired before any significant build or spend.
3. Customer payments fund subsequent development and operations.
4. No inventory, infrastructure, ad spend, or outside funding **before revenue**. See the next section for what changes after.

## THE CONSTRAINT IS THE STARTING LINE ONLY

Stated by the founder as plainly as it can be put: **solo and self-funded for the initial days. That is it.**

**Initial days — binding, no exceptions.** One person. Zero capital. The business must reach its first revenue on the founder's own effort with no money going in, which is what Gate 1 and Gate 5 test.

**After that — open, and not a constraint on anything.** A team, hired when the work justifies it. Spending the business's own money on infrastructure, tooling and advertising. **Raising outside money** — investors, equity, loans — which the founder has confirmed they are fine with. None of it counts against any gate or dimension, and none of it should be raised as a caveat.

Do not extend the starting constraint past the starting line. The engine spent runs 04 to 06 doing exactly that: Zappos was marked down for needing outside investment to grow past manual fulfilment, Levels.fyi for taking institutional money on the way to 48 employees, and mechanisms generally for "needing capital to scale." Every one of those is retired. They were normal companies doing the normal thing once they had something worth funding.

The only question that ever mattered is whether a mechanism can be *started* by one person with nothing. Any evidence or family record still carrying a caveat about later capital or later headcount should be read against this section, and the caveat disregarded.

## VALIDATION TIMELINE

First revenue within roughly **a year** is acceptable. Weeks is not the standard.

The founder is explicit about this: waiting longer is fine in exchange for a bigger outcome, provided the wait is *visibly productive*. What is not acceptable is a year of silence followed by finding out it never worked.

So a candidate on a long horizon must name **specific, checkable interim signals** — what should be observably true at month two, month four, month eight. Contributions accumulating at a stated rate. Usage compounding. A dataset approaching a threshold estimated to unlock revenue.

A candidate that names them earns relief on Bootstrap feasibility (which absorbed the former Validation accessibility) per `rules/scoring_rubric.md`. A candidate that asks for a year on faith does not.

## HOURS

`hours_per_week` is **20** and `hours_per_week_stretch` is **30**, recorded for information only.

Hours are not a constraint. The founder has stated that hours per week and number of founders are not concerns and that time will be adjusted later, so Gate 5 never blocks or fails - see `rules/hard_gates.md`. An operating load far beyond one person's capacity is read as a signal about the economics, usually a model that trades time for money linearly, and belongs in `economic_model`.

## EXPERTISE AND NETWORK

No industry credibility, no insider knowledge, no professional network, no audience, no reputation, no following.

Assume the founder starts from zero standing with zero people who know their work. Where a mechanism's original operators' starting advantages are unknown, the answer is BLOCKED, never an assumption that none existed.

## INTEREST

Interest is not a filter. A candidate is not excluded for being boring or favoured for being exciting.

## NOVELTY

Prefer mechanisms that are **proven but under-exploited** over mechanisms that are proven and saturated.

This is not a licence to invent. The mechanism must still have evidence behind it. What is sought is a proven way of making money that few solo operators are currently running, not a novel idea nobody has tested.

## SOURCE COMPANY BAND

Mechanisms are reverse-engineered from **real companies with real teams and real revenue**. The band runs from category leaders down to small-but-serious businesses, and medium and smaller companies are explicitly preferred where they qualify, because at that size the mechanism is doing the work rather than accumulated capital, and the early history is recent enough to reconstruct honestly.

**The exclusion is about ceiling, not headcount.** A solo operator at two or six thousand dollars a month is excluded because the outcome is trivial, not because they were alone. Runs 02 through 05 leaned on exactly these and it is why the corpus drifted toward candidates with no path beyond modest niche income.

**Do not spend effort on how many founders a source company had.** One founder or two is close to irrelevant — the same mechanism with the same economics is the same mechanism. Wargraphs (one person, ~€12.3M revenue, sold for ~$54M) and Levels.fyi (two founders, ~48 employees) are both good sources for the same reason: the economics are real and the start was reproducible from nothing.

What a source record must state plainly is which parts of the mechanism were carried by **capital or a pre-existing audience** — the two things this founder genuinely cannot supply — and which survive without them. A team is not on that list, because a team can be hired later out of revenue.

## AMBITION

Candidates should have a plausible path to something large. Earlier runs produced a corpus of safe, defensible, modest-ceiling niches, and that is not what is wanted.

Prefer mechanisms with **compounding properties** — network effects, data that becomes a moat as it accumulates, distribution that grows without proportional founder effort — over mechanisms whose returns stay linear in hours worked.

Higher risk is acceptable in exchange for a real ceiling. A candidate that might fail outright but could become large is preferred over one that will reliably produce a small, permanently capped income. This does not relax any hard gate: ambition is a preference among candidates that pass, never a reason to pass one that does not.
