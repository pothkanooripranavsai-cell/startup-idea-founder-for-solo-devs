"""Minimal check of the coverage rules: python scripts/test_score.py"""
from score import coverage_from_claims

idx = {
    "a": {"source": "s1", "classification": "FACT", "tier": "primary"},
    "b": {"source": "s1", "classification": "FACT", "tier": "secondary"},
    "c": {"source": "s1", "classification": "FACT", "tier": "secondary"},
    "p": {"source": "s2", "classification": "FACT", "tier": "promotional"},
    "i": {"source": "s3", "classification": "INFERENCE", "tier": "primary"},
}
claims = [("direct", ["a"]), ("direct", ["b"]), ("direct", ["c"]),   # third from s1 is capped
          ("direct", ["p"]), ("direct", ["i"]), ("direct", []),      # three demoted
          ("direct", ["p", "a"]),                                    # qualifies via a, but s1 is full
          ("unknown", [])]
cov, unk, d = coverage_from_claims(claims, idx)
assert (d["direct_capped"], d["demoted"], d["capped_away"]) == (2, 3, 2), d
assert cov == 2 / 8 and unk == 1 / 8
print("ok", d)
