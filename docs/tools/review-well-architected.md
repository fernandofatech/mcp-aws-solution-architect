# `review_well_architected`

Lightweight Well-Architected review across the six pillars: operational excellence, security, reliability, performance efficiency, cost optimization and sustainability.

!!! info "Scope"
    This is a **checklist primer**, not a substitute for the AWS Well-Architected Tool. Use it for a fast first pass, then run a formal review for anything going to production.

## Signature

```python
review_well_architected(architecture: str) -> dict
```

## How it works

The tool runs a set of explicit keyword-based heuristics against your architecture description. Each rule fires when a "must-have-any" trigger is present and a "must-have-none" trigger is absent. The full ruleset is in `src/mcp_aws_sa/tools/well_architected.py` — read it in two minutes.

## Returns

```json
{
  "summary": "Heuristic review: average score 78/100 across 6 pillars. 4 finding(s), 1 high-severity. ...",
  "findings": [
    {
      "pillar": "security",
      "severity": "high",
      "message": "No mention of IAM / least privilege.",
      "recommendation": "Define IAM policies with least-privilege per role; avoid wildcard `*` actions."
    }
  ],
  "score_by_pillar": {
    "operational_excellence": 85,
    "security": 70,
    "reliability": 70,
    "performance_efficiency": 100,
    "cost_optimization": 70,
    "sustainability": 100
  }
}
```

## Example

Architecture:

> *"Public-facing API on API Gateway → Lambda → DynamoDB. Bedrock for inference. KMS-encrypted at rest."*

Top findings: missing IAM least privilege, no multi-AZ statement, no DLQ/retry policy.

## Extending

To add a rule, append a tuple to `_RULES`. Each tuple is `(pillar, severity, (must_any, must_none), message, recommendation)`.
