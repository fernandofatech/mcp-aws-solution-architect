# `suggest_services`

Map a use case description to a curated list of AWS services with rationale.

## Signature

```python
suggest_services(use_case: str, include_baseline: bool = True) -> dict
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `use_case` | `str` | — | Free-form description of what is being built. |
| `include_baseline` | `bool` | `True` | Append baseline services (IAM, CloudWatch, CloudTrail). |

## Returns

```json
{
  "services": [
    { "service": "Amazon Bedrock", "category": "AI/ML", "rationale": "..." }
  ],
  "matched_patterns": ["rag, retrieval"],
  "note": "Matched 1 pattern(s)."
}
```

## Example

> *"Build a RAG knowledge base over internal product docs."*

```json
{
  "services": [
    { "service": "Amazon Bedrock", "category": "AI/ML", "rationale": "Managed access to foundation models (Claude, Nova, Titan) and Knowledge Bases." },
    { "service": "Amazon OpenSearch Serverless (vector)", "category": "Search", "rationale": "Managed vector store with hybrid search; pairs with Bedrock KB out of the box." },
    { "service": "Amazon S3", "category": "Storage", "rationale": "Source of truth for documents fed into the KB." },
    { "service": "AWS Lambda", "category": "Compute", "rationale": "Ingestion and retrieval orchestration." },
    { "service": "AWS IAM", "category": "Security", "rationale": "Least-privilege access — required for every workload." },
    { "service": "Amazon CloudWatch", "category": "Observability", "rationale": "Metrics, logs and alarms for the stack." },
    { "service": "AWS CloudTrail", "category": "Governance", "rationale": "Audit trail of API calls — non-negotiable for any production account." }
  ],
  "matched_patterns": ["rag, retrieval"],
  "note": "Matched 1 pattern(s)."
}
```

## Notes

- Matching is keyword-based and **deterministic**. See `src/mcp_aws_sa/data/service_catalog.py` for the full catalog.
- Unmatched use cases still return the baseline services with a hint to refine the description.
- The catalog is intentionally compact — extending it is a one-file diff.
