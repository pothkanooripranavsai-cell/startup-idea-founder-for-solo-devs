# SCORING RUBRIC

Applied only after every gate in `rules/hard_gates.md` is resolved. Six dimensions, scored 0–5. `scripts/score.py` computes the weighted total and the verdict; the evaluator supplies the per-dimension score and its justification.

Keep this file and `scripts/score.py` in sync. The script asserts the weights sum to 1.0.

## WEIGHTS

| Dimension | Weight |
|---|---|
| Bootstrap feasibility | 25% |
| Domain / tacit fit | 25% |
| Solo feasibility | 15% |
| Solo transfer | 15% |
| Validation accessibility | 10% |
| Distribution | 10% |

Weighted total = Σ (weight × score), on a 0–5 scale.

## BOOTSTRAP FEASIBILITY (25%)

Gate 1 has already established that cash validation cost is zero. This dimension grades how far the candidate is from *revenue*, not how far it is from a budget.

* **0** — cannot produce revenue without a build, a spend, or a scale the founder cannot reach
* **1** — revenue only after substantial unpaid build, with no signal available before then
* **2** — revenue reachable, but only after weeks of work with no interim confirmation anyone will pay
* **3** — a paying signal is obtainable after moderate unpaid effort
* **4** — a paying signal is obtainable within days, from work that is useful either way
* **5** — can be pre-sold or manually delivered for payment before anything is built

A candidate that reaches ₹0 cost by deferring all value creation into unpaid founder labour is not scoring 5. Zero cash is the gate; speed to a paying customer is the score.

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

## SOLO TRANSFER (15%)

The mechanism was proven by somebody. How much of what made it work is still available to a solo operator with zero capital, zero audience, and no team?

* **0** — the mechanism only works with capital, a team, or an existing audience; strip those and nothing is left
* **1** — depends heavily on scale or funded distribution
* **2** — significant reworking needed, and the reworked version is unproven
* **3** — the core loop survives at solo scale with real compromises
* **4** — transfers with minor adaptation; scale was an accelerant, not a precondition
* **5** — already demonstrably run by solo operators at zero capital

This is not about geography. It asks what survives when the funded company's advantages are removed.

Where the original operators' starting advantages are unknown, this dimension is `null`.

## VALIDATION ACCESSIBILITY (10%)

How quickly can a real signal be obtained?

* **0** — no meaningful test short of building the whole thing
* **1** — long test cycle before any signal
* **2** — testable, but slow or ambiguous feedback
* **3** — testable within weeks with a clear signal
* **4** — testable within days; a paying signal is obtainable
* **5** — pre-sale or manual test gives an immediate paying signal

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
