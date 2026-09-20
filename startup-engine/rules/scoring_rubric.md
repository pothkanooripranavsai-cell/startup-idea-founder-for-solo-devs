# SCORING RUBRIC

Applied only after every gate in `rules/hard_gates.md` is resolved. Six dimensions, scored 0–5. `scripts/score.py` computes the weighted total and the verdict; the evaluator supplies the per-dimension score and its justification.

Keep this file and `scripts/score.py` in sync. The script asserts the weights sum to 1.0.

## WEIGHTS

| Dimension | Weight |
|---|---|
| Bootstrap feasibility | 25% |
| Economic model | 25% |
| Domain / tacit fit | 15% |
| Solo feasibility | 15% |
| Validation accessibility | 10% |
| Distribution | 10% |

Weighted total = Σ (weight × score), on a 0–5 scale.

### What this rubric is for

The question behind every dimension is whether a model is worth betting time on. Not whether it is safe, and not whether it can be run by exactly one person forever — whether the expected value justifies the work.

Two consequences follow, and they changed the weights above:

**Economic model rose from 15% to 25%** and became the joint-heaviest dimension. It was previously named "solo transfer" and spent much of its time adjudicating whether a source company had one founder or two, which is not a fact about the economics.

**Domain / tacit fit fell from 25% to 15%.** Expertise gaps are less fatal than they were, because hiring out of revenue is now explicitly allowed. A knowledge gap that can be closed with the business's own money later is a smaller problem than a broken economic model, which cannot.

Totals recorded for runs 01–06 were computed under the old weights and the old dimension meaning. They are left as recorded rather than recomputed, and are not directly comparable to totals produced after this revision.

## BOOTSTRAP FEASIBILITY (25%)

Gate 1 has already established that cash validation cost is zero. This dimension grades how far the candidate is from *revenue*, not how far it is from a budget.

* **0** — cannot produce revenue without a build, a spend, or a scale the founder cannot reach
* **1** — revenue only after substantial unpaid build, with no signal available before then
* **2** — revenue reachable, but only after weeks of work with no interim confirmation anyone will pay
* **3** — a paying signal is obtainable after moderate unpaid effort
* **4** — a paying signal is obtainable within days, from work that is useful either way
* **5** — can be pre-sold or manually delivered for payment before anything is built

A candidate that reaches ₹0 cost by deferring all value creation into unpaid founder labour is not scoring 5. Zero cash is the gate; speed to a paying customer is the score.

### The long-horizon exception

The anchors above are written in days and weeks, which systematically floors any compounding mechanism at 1–2 regardless of how good it is. An asset that compounds does so by accumulating, and accumulation takes months during which nobody pays. Scored literally, the rubric punishes exactly the mechanisms the founder's ambition preference asks for.

So: **a candidate whose first revenue is expected within roughly a year may score 3 or 4 despite the long wait, on one condition — it must name specific, checkable interim signals** that would show the wait is productive before the year is out. Concretely: what should be observably true at month two, month four, month eight. Contributions accumulating at some rate, usage growing, a dataset approaching a threshold known or estimated to unlock revenue.

The condition is the whole exception. A candidate that says "this will take a year, trust it" and names nothing checkable still scores 1. The founder is willing to wait; they are not willing to wait blind. A long silent wait and a long instrumented wait are different bets, and only the second one earns the relief.

## DOMAIN / TACIT FIT (25%)

How far is the required knowledge from what the founder has or can obtain?

* **0** — requires deep domain expertise *and* established relationships
* **1** — requires substantial tacit knowledge that transfers only through years of practice
* **2** — requires meaningful expertise, learnable in months, with real execution risk while learning
* **3** — requires documented, publicly learnable knowledge
* **4** — generalist skills suffice; minor domain learning
* **5** — no meaningful expertise or relationship barrier

Tacit knowledge and relationships weigh heavier than credentials. Where the original operators' starting advantages are unknown, this dimension is `null`, not a guess.

## SOLO FEASIBILITY (15%)

Can one person carry it through validation? Paid help is unavailable before revenue.

* **0** — requires a team before any revenue
* **1** — requires continuous part-time help
* **2** — solo-operable only at an unsustainable load
* **3** — solo-operable with tooling, but near the limit of one person's capacity
* **4** — comfortably solo through validation
* **5** — solo well past validation; low ongoing operating load

## ECONOMIC MODEL (25%)

**This is the dimension that matters most, and it asks one question: is this economic model worth betting on?**

Not "was the source company one person or two." Team size at the source is close to noise — a mechanism that worked for two founders and a mechanism that worked for one are the same mechanism. What is being scored is the economics: margin, ceiling, defensibility, and whether the model needs inputs the founder genuinely cannot get.

Judge it as expected value. A model with a modest chance of a large outcome can beat one with a high chance of a small outcome, and the rubric should say so.

* **0** — the economics never work, or the model cannot produce a first sale without capital or a pre-existing audience
* **1** — thin margins, a hard ceiling, and no defensibility; effort in, roughly the same effort out, forever
* **2** — workable economics but a low ceiling, or a ceiling that exists only if something unevidenced holds
* **3** — sound unit economics and a real ceiling, with defensibility that depends on execution rather than structure
* **4** — strong margins and a ceiling worth chasing, with at least one structural advantage that accrues over time — accumulating data, a network that gets denser, distribution that compounds
* **5** — strong margins, a large ceiling, and a moat that grows on its own as the business operates, evidenced at a real company rather than argued

### What counts as needing an input the founder cannot get

Exactly two things: **capital before first revenue**, and **an audience that must already exist before the first sale.** Those are the only inputs the founder genuinely cannot supply.

Everything else is available later and must not be scored as a deficiency:

* **A team** — hired once the work justifies it.
* **Outside investment** — the founder has confirmed they are fine raising it after the business is working.
* **Scaling capital of any kind** — self-funded or external.

So "this mechanism needed money to get big" is not a finding against a candidate. "This mechanism needs money before anyone pays" is, and it is the only version that counts.

Where the economics are genuinely unknown — no margin, pricing or ceiling evidence of any kind — this dimension is `null`.

## VALIDATION ACCESSIBILITY (10%)

How quickly can a real signal be obtained?

* **0** — no meaningful test short of building the whole thing
* **1** — long test cycle before any signal
* **2** — testable, but slow or ambiguous feedback
* **3** — testable within weeks with a clear signal
* **4** — testable within days; a paying signal is obtainable
* **5** — pre-sale or manual test gives an immediate paying signal

Read "signal" as *any unambiguous read on whether the mechanism is working*, not specifically a payment. A candidate on a year-long revenue horizon that can nonetheless observe contributions arriving, or usage compounding, within weeks is testable within weeks and scores accordingly — the long-horizon exception under Bootstrap feasibility applies here too, on the same condition that the interim signals are named and checkable.

What scores 1 is a candidate that cannot tell whether it is working until it is finished.

## DISTRIBUTION (10%)

How hard is it to reach buyers — given Gate 7 has already established that *some* accessible path exists?

* **0** — reachable only through channels the founder cannot access
* **1** — the only realistic channels are paid, which is unavailable
* **2** — an unpaid channel exists but is saturated, slow, or low-yield
* **3** — identifiable channel reachable with sustained effort
* **4** — direct, low-cost channel available
* **5** — buyers actively searching; organic or inbound demand exists

Gate 7 decides whether an unpaid path exists at all. This dimension grades how hard that path is. Paid acquisition is unavailable, so it cannot rescue a low score here.

## UNSCORED DIMENSIONS

A dimension with no resolved evidence is `null`. It is never defaulted to a midpoint.

Any `null` suppresses the weighted total. A candidate with an unscored dimension cannot reach `DEEP_EXPLORE`.

## VERDICT

Computed by `scripts/score.py`, in order. The first matching rule wins.

1. Any gate `FAIL` → **REJECT**
2. Any gate `BLOCKED` → **WATCH** (the blocking gate becomes the critical unknown)
3. Any dimension `null` → **WATCH**
4. `weighted_total` < 2.5 → **REJECT**
5. `weighted_total` ≥ 3.5 **and** `fact_coverage` ≥ 0.5 **and** `unknown_rate` ≤ 0.3 → **DEEP_EXPLORE**
6. Otherwise → **WATCH**

Rule 5 is why coverage is decomposed: a high score built on thin direct evidence stays at `WATCH` rather than earning deep research. Inference never substitutes for direct support in this test.

## RANKING

The weighted total exists to threshold into a verdict. It is not a ranking.

Do not order candidates by score unless a run explicitly asks for a ranked output.
