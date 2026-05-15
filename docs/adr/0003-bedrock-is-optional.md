# 0003 — Bedrock is an optional backend, not a hard dependency

- Status: **accepted**
- Date: 2026-05-15

## Context and problem statement

Several tools (`suggest_services`, `generate_architecture_diagram`, `review_well_architected`) could benefit from LLM reasoning to produce richer, less keyword-driven output. We have to decide whether that is *required* or *optional*.

Considerations:

- The server is meant to be embedded in an MCP client that is *already* an LLM. Adding a second LLM call inside the server can be redundant.
- Requiring AWS credentials and a Bedrock model would raise the barrier to first-run dramatically.
- The deterministic, keyword-based implementation is auditable — anyone can read the catalog and the rules in a few minutes.

## Decision

Tools are **deterministic by default**. Bedrock is an optional backend that can be enabled per tool via the `bedrock` extras and an env-var-toggled flag. When disabled (the default), every tool ships a useful, transparent response without making any AWS API call.

## Alternatives considered

- **Bedrock as the primary backend.** Rejected — raises barrier, slower iteration, harder to test.
- **No LLM ever.** Rejected as a long-term stance — some tasks (free-form architecture review) are genuinely LLM-shaped.

## Consequences

- The first-run experience is `pip install + run`. No AWS setup needed.
- Bedrock integration is a clean, optional layer we can ship later without breaking the deterministic path.
- The keyword-based catalog and rules must stay readable and well-tested — they remain the reference implementation.
