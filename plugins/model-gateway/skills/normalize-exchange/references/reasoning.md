# Reasoning evidence policy

PMCR-O never requires hidden chain-of-thought. Model outputs may be fully opaque.

When an explicit rationale is available, normalize it as one of `provider-summary`, `explicit-rationale`, or `derived-rationale`. A derived rationale is a new artifact created by `reasoning-agent`; it is not a recovered internal trace from another model.

Reasoning evidence may help routing, effort selection, voting, review, or explanation, but authorization still comes from grants/governance and correctness still comes from independent CHECK and outcome evidence.
