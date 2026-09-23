# SCORING RUBRIC

Applied only after every gate in `rules/hard_gates.md` is resolved. Six dimensions, scored 0–5. `scripts/score.py` computes the total and the verdict; the evaluator supplies the per-dimension score and its justification.

Keep this file and `scripts/score.py` in sync. The script asserts the weights sum to 1.0.

## WHAT THIS RUBRIC IS FOR

The founder's requirement, stated by them: **something with good product-market fit, startable now, with little money, on their own.** Best economic model wins. Time per week and number of founders are explicitly not concerns.

So the rubric asks one question — **is this worth betting on?** — and it answers it by weighting demand and economics above everything else. Sixty percent of the total weight sits on `demand_evidence` and `economic_model` together.

### Run 09: product-market fit is the single primary goal

The founder set it for run 09: product-market fit first, worry less about competition. `demand_evidence` - direct proof that buyers in this niche pay - became the heaviest dimension at 35 percent, and `contestedness` fell from 15 to 5 percent. `economic_model` moved from 30 to 25 percent.

What this does and does not do, stated plainly. It lifts candidates with proven demand in crowded markets and lowers candidates in open ground with unproven demand, **with no new evidence either way** - the before and after for all earlier candidates is in the run 09 record. Competition still counts: a crowded market still costs points, and a contestedness of 0, meaning funded incumbents sell the exact product to the exact buyer, still zeroes the total under the geometric mean. The weight change says a proven market is worth more than an empty one; it does not say competitors are harmless.

## WEIGHTS

| Dimension | Weight |
|---|---|
| Demand evidence | 35% |
| Economic model | 25% |
| Bootstrap feasibility | 15% |
| Distribution | 10% |
| Domain / tacit fit | 10% |
| Contestedness | 5% |

Previous weights, used from 22 Sep through run 08: economic model 30, demand evidence 20, contestedness 15, bootstrap 15, distribution 10, domain fit 10.

**Removed:** `solo_feasibility` — the founder will adjust hours later, so capacity is no longer decision-relevant. **Merged:** `validation_accessibility` folded into `bootstrap_feasibility`; they moved together in every rescoring because both were measuring time-to-feedback, and summing them double-counted one construct.

## THE TOTAL IS MULTIPLICATIVE

```
total = 5 × Π (score / 5) ^ weight
```

A weighted **sum** lets a strength average away a fatal weakness — a 0 on distribution would cost half a point out of five, when in truth a business whose buyers are unreachable is worth nothing. A weighted **geometric mean** fixes that: any dimension at 0 drives the total to 0, and weak dimensions drag proportionally rather than being smoothed over.

The scale is preserved at the ends — straight 5s give 5.00, straight 3s give 3.00 — so the thresholds still read naturally. What changes is the middle: a candidate scoring 5 everywhere except a 1 in distribution lands at **4.26**, where the old arithmetic gave it 4.60.

The 2.5 and 3.5 thresholds keep their previous values. They were invented and they remain invented. Because the geometric mean shifts the distribution slightly downward, they are now *relatively* stricter than before — noted here rather than silently retuned.

## ECONOMIC MODEL (25%)

**Second-heaviest since run 09. Is this economic model worth betting on?**

Margin, ceiling, defensibility. Not team size at the source — a mechanism that worked for two founders and one that worked for one are the same mechanism.

* **0** — the economics never work, or no first sale is possible without capital or a pre-existing audience
* **1** — thin margins, a hard ceiling, no defensibility; effort in, roughly the same effort out, forever
* **2** — workable economics but a low ceiling, or a ceiling that exists only if something unevidenced holds
* **3** — sound unit economics and a real ceiling, with defensibility that depends on execution rather than structure
* **4** — strong margins and a ceiling worth chasing, with at least one structural advantage that accrues over time
* **5** — strong margins, a large ceiling, and a moat that grows on its own as the business operates, evidenced at a real company rather than argued

### The two inputs that are genuinely unavailable

**Capital before first revenue**, and **an audience that must already exist before the first sale.** Only these.

A team, outside investment, and scaling capital of any kind are all available later and must never be scored as deficiencies. "This mechanism needed money to get big" is not a finding against a candidate. "This mechanism needs money before anyone pays" is.

Where margin, pricing and ceiling evidence are all absent, this dimension is `null`.

## DEMAND EVIDENCE (35%)

**The heaviest dimension since run 09 - this is the product-market-fit measure.**

**Is there direct proof that buyers in this specific niche pay for this specific thing, at a price that works?**

This dimension exists because the engine used to infer demand from "the mechanism is proven," and those are different claims. A proven mechanism pointed at a niche nobody wants is still nothing. Product-market fit is what the founder asked for and it was never being scored.

* **0** — no evidence anyone wants this; demand is assumed from the mechanism working elsewhere
* **1** — demand inferred only from adjacent or analogous markets
* **2** — people express the need, but nothing shows them paying for it
* **3** — buyers in this niche pay for *something* addressing this need, at unclear prices
* **4** — named buyers in this niche pay, with at least one sourced price point
* **5** — demonstrated, priced, recurring demand in this exact niche, with named payers and figures

Complaints, upvotes and survey intent are not demand. **Someone paying is demand.** Where nothing distinguishes wanting from paying, score no higher than 2.

## CONTESTEDNESS (5%)

**How crowded and defended is this niche right now?**

Previously this surfaced only by accident, when a disconfirming search happened to find incumbents — which is how idea_10 died. Identical mechanics in an empty and a saturated niche used to score identically.

* **0** — funded incumbents serve this exact buyer with this exact thing, and are entrenched
* **1** — several credible operators already here; entry means direct displacement
* **2** — contested, with a plausible but narrow underserved seam
* **3** — some operators present, none dominant, room on at least one axis
* **4** — mechanism proven elsewhere, few or no operators serving this niche with it
* **5** — genuinely open: demonstrated demand, a proven mechanism, and nobody competently serving it

Score the niche **as it is now**, not as it was when the source company entered. A mechanism that worked in 2017 in an empty field may be entering a full one today.

### A seam must be checked, not asserted (added in run 08)

A score of **2 or higher** requires the evaluator to name the seam and to record in `disconfirming_search` a search for anyone already occupying it — including competitors' own placed articles and pricing pages, not just the first competitor found. A seam asserted without that search scores 1.

Added because run 07's `idea_23` checked one competitor, treated its proposed wedge as open, and scored 0.35 too high until deep research found the wedge already sold. Before run 08, 14 of 25 candidates sat at exactly 2, mostly without such a search. The rule applies to every evaluation from run 08 on, and was re-applied to the four earlier candidates scored 3 or 4; the older 2s are flagged as unchecked rather than silently kept or silently cut.

## BOOTSTRAP FEASIBILITY (15%)

How far from revenue, and how fast does feedback arrive? This dimension absorbed the former `validation_accessibility`.

* **0** — cannot produce revenue without a build, a spend, or a scale the founder cannot reach
* **1** — revenue only after substantial unpaid build, with no signal available before then
* **2** — revenue reachable after weeks of work with no interim confirmation anyone will pay
* **3** — a paying signal obtainable after moderate unpaid effort, or clear non-revenue feedback within weeks
* **4** — a paying signal obtainable within days, from work useful either way
* **5** — can be pre-sold or manually delivered for payment before anything is built

Reaching zero cash by deferring all value creation into unpaid labour is not a 5.

### The long-horizon exception

The anchors read in days and weeks, which would floor every compounding mechanism at 1–2 by construction — exactly the mechanisms worth wanting.

**A candidate whose first revenue is expected within roughly a year may score 3 or 4 despite the wait, on one condition: it must name specific, checkable interim signals** — what should be observably true at month two, four, eight.

The condition is the whole exception. "This will take a year, trust it" still scores 1. A long instrumented wait and a long silent wait are different bets; only the first earns relief.

## DISTRIBUTION (10%)

How hard is it to reach buyers, given Gate 7 established that *some* unpaid path exists?

* **0** — reachable only through channels the founder cannot access
* **1** — the only realistic channels are paid, which is unavailable
* **2** — an unpaid channel exists but is saturated, slow, or low-yield
* **3** — identifiable channel reachable with sustained effort
* **4** — direct, low-cost channel available
* **5** — buyers actively searching; organic or inbound demand exists

## DOMAIN / TACIT FIT (10%)

How far is the required knowledge from what the founder has or can obtain? Lowered to 10% because expertise can be hired out of revenue, while broken economics cannot be fixed at all.

* **0** — requires deep domain expertise *and* established relationships
* **1** — requires substantial tacit knowledge that transfers only through years of practice
* **2** — requires meaningful expertise, learnable in months, with real execution risk while learning
* **3** — requires documented, publicly learnable knowledge
* **4** — generalist skills suffice; minor domain learning
* **5** — no meaningful expertise or relationship barrier

Relationships weigh heavier than credentials. Where the original operators' starting advantages are unknown, this is `null`, not a guess.

## MAGNITUDE — REQUIRED, NOT SCORED

Every idea must state `ceiling_annual_revenue` and `ceiling_basis` in its frontmatter — a number, and how it was derived, citing the source company's disclosed revenue where one exists.

It is deliberately **not folded into the 0–5**, because `economic_model` already judges ceiling qualitatively and folding it in would double-count the same judgement. It is reported alongside the score.

**A candidate with no stated ceiling cannot reach `DEEP_EXPLORE`.** Expected value needs a payoff term, and "a ceiling worth chasing" is a word, not a number. Two candidates can score `economic_model: 4` with ceilings differing by a hundredfold.

## SURVIVORSHIP — REPORTED, NEVER ASSUMED AWAY

Every source company in this corpus succeeded. There is no denominator anywhere, and a count of successes without one is survivor-selected.

Model families carry `attempt_denominator` and `denominator_basis`. `score.py` prints the denominator on every run, and where it is `UNKNOWN` it says so explicitly rather than letting `revenue_evidenced_count: 6` read as proof of good odds.

**This does not cap `economic_model`,** and the distinction matters: `economic_model` describes the payoff *conditional on the thing working*, while survivorship is a fact about *probability*. They are different axes, and burying a probability problem inside a payoff score is how the confusion started.

Expect most families to report `UNKNOWN`. That is the finding, not a failure of the pass.

## UNSCORED DIMENSIONS

A dimension with no resolved evidence is `null`, never a midpoint. Any `null` suppresses the total, and a candidate with an unscored dimension cannot reach `DEEP_EXPLORE`.

## VERDICT

Computed by `scripts/score.py`, in order. First match wins.

1. Any gate `FAIL` → **REJECT**
2. `total` is exactly `0.00` → **REJECT**, naming the zeroed dimension
3. Any gate `BLOCKED` → **WATCH** (the blocking gate becomes the critical unknown)
4. Any dimension `null` → **WATCH**
5. `total` < 2.5 → **REJECT**
6. `total` ≥ 3.5 **and** a stated ceiling **and** `fact_coverage` ≥ 0.5 **and** `unknown_rate` ≤ 0.3 → **DEEP_EXPLORE**
7. Otherwise → **WATCH**

**Rule 2 was added after the first full recalculation.** idea_10 — whose niche is served by funded incumbents selling the same thing to the same buyer — scored `contestedness: 0` and therefore `0.00`, and still read `WATCH` because a different gate was unresolved. That understates it badly. `BLOCKED` routes to `WATCH` because it represents *ignorance*, and rejecting on ignorance is wrong; a scored zero is a *judgement* that the dimension is fatal, and resolving some other gate cannot rescue it.

Rule 6 is why coverage is decomposed and why magnitude is required: a high score built on thin evidence, or on an unstated payoff, stays at `WATCH`. Inference never substitutes for direct support.

## RANKING

The total exists to threshold into a verdict. It is not a ranking. Do not order candidates by score unless a run explicitly asks for it.
