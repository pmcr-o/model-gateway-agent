---
name: normalize-exchange
description: "Normalize external or local model prompts, responses, and optional explicit reasoning summaries into provider-neutral PMCR-O evidence envelopes."
---
# normalize-exchange

Route: `@model-gateway-agent /model-gateway:normalize-exchange`.

Works with UI, API, or local model outputs; the provider does not need PMCR-O access.

## Reasoning evidence
- `opaque`: response only; no private internal reasoning is assumed.
- `provider-summary`: the provider/UI explicitly exposes a reasoning summary.
- `explicit-rationale`: the task explicitly requested concise decision factors or explanation.
- `derived-rationale`: `reasoning-agent` performs a separate structured reasoning pass and the exact `@reasoning-agent /reasoning:<skill>` route is recorded.

Reasoning evidence never grants authority. CHECK judges outcomes and evidence separately, and PMCR-O never requires hidden chain-of-thought.
