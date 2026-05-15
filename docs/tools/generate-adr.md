# `generate_adr`

Render a Markdown ADR in the **MADR** (Markdown Architecture Decision Record) style from inputs.

## Signature

```python
generate_adr(
    title: str,
    context: str,
    decision: str,
    alternatives: list[str] | None = None,
    consequences: list[str] | None = None,
    status: str = "proposed",
) -> dict
```

## Returns

```json
{
  "filename": "use-dynamodb-for-session-storage.md",
  "content": "# Use DynamoDB for session storage\n\n- Status: **proposed**\n..."
}
```

## Example

```python
generate_adr(
    title="Use DynamoDB for session storage",
    context="We need single-digit-ms reads for session tokens and predictable cost at low write volume.",
    decision="We will use DynamoDB on-demand with TTL-based expiry.",
    alternatives=["ElastiCache Redis", "RDS PostgreSQL with TTL job"],
    consequences=[
        "+ Native TTL — no cleanup job to maintain.",
        "+ Pay-per-request matches the bursty traffic pattern.",
        "- DynamoDB lacks server-side filtering primitives; expect denormalised data.",
    ],
)
```

Produces a fully-formed Markdown ADR ready to drop in `docs/adr/`.

## Why MADR

MADR is intentionally light: one Markdown file per decision, easy to review in PRs, easy to grep. See [adr.github.io/madr](https://adr.github.io/madr/) for the full spec.
