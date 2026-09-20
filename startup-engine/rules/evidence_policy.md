# EVIDENCE POLICY

## CLASSIFICATION

Every claim carries exactly one label.

* **FACT** — directly stated by a qualifying source, with citation.
* **INFERENCE** — derived from facts through stated reasoning. The reasoning is written out, not implied.
* **HYPOTHESIS** — proposed but untested. Not support for a gate or a score.
* **UNKNOWN** — no evidence in either direction.

An UNKNOWN is never converted into a favorable assumption.

Missing information is not positive evidence.

## SOURCE HIERARCHY

1. **Primary** — filings, regulatory records, first-party pricing and product pages, platform data, direct operator interviews.
2. **Secondary** — trade press, analyst reports, credible industry surveys.
3. **Community** — forums, social posts, individual operator anecdotes.
4. **Promotional** — company marketing, PR, funding announcements.

Community sources cannot alone support a FACT.

Promotional sources are never sole support for a viability claim.

Funding raised is not evidence that a model works.

## FRESHNESS

Freshness and classification are independent axes.

Age never changes a classification. An old FACT is still a FACT. It is recorded as `classification: FACT` with `freshness_status: stale`, and it then fails any check that requires currency. It is not demoted to INFERENCE or UNKNOWN.

Freshness is judged on `as_of` — when the claim was true — not on `retrieved_at`, which records only when the source was fetched.

Freshness requirements, applied where `freshness_sensitive: true`:

* Unit economics and pricing: 24 months or newer.
* Competitive landscape: 12 months or newer.
* Regulatory status: current only.
* Structural facts: not freshness-sensitive. Record the vintage.

A stale claim can still be used where currency does not matter for that specific use. Mark `freshness_sensitive: false` and say why.

## INDEPENDENT SOURCES

Two sources are independent only when they come from different organizations **and** do not reproduce the same underlying material — the same press release, dataset, company announcement, wire story, or identical source text.

Three websites repeating one press release are one underlying source, not three.

Every evidence record carries `underlying_source` so that republication is detectable. Without it, syndication reads as corroboration.

When validating a model family, count three things separately and never conflate them:

* number of companies
* number of independent companies
* number of companies with revenue evidence

## GEOGRAPHIC RELEVANCE

Evidence from the origin market supports the claim that the model is proven.

It does not support the claim that the model is locally viable.

Local viability claims require target-market evidence.

Transfer across markets is INFERENCE at best. It is never FACT.

## CONFLICTING SOURCES

Record both sources.

Resolve in this order: higher tier, then more recent, then more geographically relevant.

If the conflict does not resolve, label UNKNOWN and record the conflict.

Do not silently adopt the more favorable source.

## STRONG EVIDENCE

Strong evidence is:

* two or more independent sources, as defined above — distinct organizations *and* distinct underlying material
* primary or secondary tier
* within its date window
* from the relevant geography
* specific and quantified
* checked against a search for disconfirming evidence

Weak evidence is single-source, promotional, undated, from the wrong market, or vague.

Strong evidence is required to mark a gate PASS where a FACT is obtainable.

## PROHIBITED

* inventing numbers
* labelling a claim FACT without a citation
* treating "not found" as evidence of absence
* using intuition to fill a gap that should be UNKNOWN
* using a HYPOTHESIS as support when gating or scoring
