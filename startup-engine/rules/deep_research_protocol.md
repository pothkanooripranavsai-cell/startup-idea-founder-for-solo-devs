# DEEP RESEARCH PROTOCOL

Reserved for survivors of screening. Never run across a whole generated batch.

## WHEN TO TRIGGER

* `verdict: DEEP_EXPLORE` — all gates PASS, all dimensions scored, evidence sufficient.
* `verdict: WATCH` where the blocking item is a single identified unknown that is cheap to resolve.

## WHEN NOT TO TRIGGER

* `verdict: REJECT`.
* `WATCH` where the unknown is expensive or unanswerable — record it and set the candidate aside.
* Whole batches. The protocol runs per candidate, on named questions.

## STEPS

1. **Scope the question.** State the claim needing evidence and which gate or dimension it resolves. "Research the market" is not a question. "Do lenders in segment X pay per qualified lead, and at what rate" is.
2. **Prioritize local viability.** Proof that the mechanism works elsewhere is already partly established. The expensive unknowns are local unit economics, local competition, regulatory friction, and hidden expertise or network requirements.
3. **Search** across the tiers in `rules/evidence_policy.md`, primary sources first.
4. **Record** each usable source as a `data/evidence/` record per `schemas/evidence.md`, with classification, `as_of`, `underlying_source`, and geography.
5. **Update reference data.** A newly surfaced competitor, failure, or market fact goes into `data/companies/`, `data/failures/`, or `data/market/` so it is reusable.
6. **Re-gate and re-score** by re-running the evaluation and `scripts/score.py`.
7. **Log the trail** to `runs/deep_research/<idea_id>.md`: questions asked, sources checked, sources used and discarded, and what remains unresolved.

## STOPPING

Stop when every flagged gate or dimension is answered, or is explicitly marked researched-and-still-UNKNOWN with a note on what was searched.

Do not loop on an unanswerable question.

A claim that stays UNKNOWN after a good-faith search stays UNKNOWN. It is not upgraded to a favorable assumption. The dimension remains unscored and the candidate's writeup states the open question plainly.

## OUTPUT

* `runs/deep_research/<idea_id>.md` — the trail, including unresolved questions
* new or updated records under `data/evidence/`, and where applicable `data/companies/`, `data/failures/`, `data/market/`
