"""Tool: review_well_architected — architecture description → 6-pillar review.

The implementation is intentionally explicit: each pillar is a set of
keyword-based heuristics that produce findings (positive or negative). It is a
*lightweight* review, useful as a checklist primer or as a first pass before a
full WA Tool workshop.
"""

from __future__ import annotations

PILLARS = (
    "operational_excellence",
    "security",
    "reliability",
    "performance_efficiency",
    "cost_optimization",
    "sustainability",
)


# Each rule: (pillar, severity, trigger, message, recommendation)
# - trigger: a tuple (must_have_any, must_have_none). If text contains any of
#   ``must_have_any`` and *none* of ``must_have_none`` the finding fires.
_RULES: list[tuple[str, str, tuple[list[str], list[str]], str, str]] = [
    # security
    (
        "security",
        "high",
        ([" public "], ["vpc", "private subnet"]),
        "Workload appears to expose resources publicly without VPC isolation.",
        "Place compute in private subnets and front it with API Gateway / ALB + WAF.",
    ),
    (
        "security",
        "medium",
        (["encryption", "kms"], []),
        "Encryption is mentioned — good.",
        "Confirm encryption-at-rest (KMS keys, S3 bucket policies) AND in-transit (TLS 1.2+).",
    ),
    (
        "security",
        "high",
        ([], ["iam", "least privilege", "least-privilege"]),
        "No mention of IAM / least privilege.",
        "Define IAM policies with least-privilege per role; avoid wildcard `*` actions.",
    ),
    # reliability
    (
        "reliability",
        "high",
        ([], ["multi-az", "multi az", "fault toleran", "ha "]),
        "No mention of multi-AZ or fault tolerance.",
        "Deploy stateful services across at least two AZs; design for AZ failure.",
    ),
    (
        "reliability",
        "medium",
        (["dlq", "dead letter", "retry"], []),
        "Retries / DLQ are considered — good.",
        "Make sure DLQ has alarms and a runbook for replays.",
    ),
    # performance_efficiency
    (
        "performance_efficiency",
        "medium",
        (["cloudfront", "cdn", "cache"], []),
        "Caching / CDN is in the design — good.",
        "Set cache-control headers and TTLs explicitly. Cache invalidation strategy?",
    ),
    (
        "performance_efficiency",
        "low",
        (["auto scaling", "autoscaling", "scale-out"], []),
        "Auto scaling considered.",
        "Define scaling metrics (CPU vs custom CloudWatch) and warm-up behavior.",
    ),
    # cost_optimization
    (
        "cost_optimization",
        "medium",
        (["graviton", "arm64"], []),
        "Graviton / ARM64 mentioned — typically ~20% cheaper than x86.",
        "Verify your runtime/library compatibility, then standardise on Graviton.",
    ),
    (
        "cost_optimization",
        "high",
        ([" rds ", "ec2"], ["reserved", "savings plan", "spot"]),
        "Long-running compute / RDS without Reserved Instances or Savings Plans.",
        "For predictable workloads, commit via Compute Savings Plans (1- or 3-year).",
    ),
    # operational_excellence
    (
        "operational_excellence",
        "medium",
        ([], ["cloudwatch", "observab", "log", "metric", "trace"]),
        "Observability is not mentioned.",
        "Emit structured logs, metrics, and traces. Wire alarms to a paging channel.",
    ),
    (
        "operational_excellence",
        "low",
        (["cdk", "terraform", "cloudformation", "iac"], []),
        "Infrastructure as Code is used — good.",
        "Keep IaC under version control; run plan/diff in CI for every change.",
    ),
    # sustainability
    (
        "sustainability",
        "low",
        (["serverless", "lambda", "fargate"], []),
        "Serverless services scale to zero — sustainability win.",
        "Continue favoring managed/serverless to minimize idle capacity.",
    ),
]


def review_well_architected(architecture: str) -> dict[str, object]:
    """Lightweight Well-Architected review of an architecture description.

    Args:
        architecture: Free-form text describing the architecture. Bullet points,
            paragraphs or a list of services are all fine.

    Returns:
        A dict with ``summary``, ``findings`` (list of `{pillar, severity, message,
        recommendation}`) and ``score_by_pillar`` (0–100 per pillar).
    """
    if not architecture or not architecture.strip():
        return {
            "summary": "Empty architecture description — nothing to review.",
            "findings": [],
            "score_by_pillar": {p: 0 for p in PILLARS},
        }

    text = " " + architecture.lower() + " "
    findings: list[dict[str, str]] = []

    for pillar, severity, (must_any, must_none), message, recommendation in _RULES:
        any_ok = (not must_any) or any(token in text for token in must_any)
        none_ok = all(token not in text for token in must_none)
        if any_ok and none_ok:
            findings.append(
                {
                    "pillar": pillar,
                    "severity": severity,
                    "message": message,
                    "recommendation": recommendation,
                }
            )

    score_by_pillar = _score(findings)
    summary = _summary(findings, score_by_pillar)
    return {
        "summary": summary,
        "findings": findings,
        "score_by_pillar": score_by_pillar,
    }


def _score(findings: list[dict[str, str]]) -> dict[str, int]:
    weight = {"info": 0, "low": 5, "medium": 15, "high": 30}
    score = dict.fromkeys(PILLARS, 100)
    for f in findings:
        # Positive findings (those whose message ends with "good." or similar) shouldn't subtract.
        if f["message"].endswith("good.") or "Good." in f["message"]:
            continue
        score[f["pillar"]] = max(0, score[f["pillar"]] - weight.get(f["severity"], 10))
    return score


def _summary(findings: list[dict[str, str]], score_by_pillar: dict[str, int]) -> str:
    if not findings:
        return "No heuristics triggered. Provide a richer architecture description for a better review."
    avg = sum(score_by_pillar.values()) // len(score_by_pillar)
    highs = sum(1 for f in findings if f["severity"] == "high")
    return (
        f"Heuristic review: average score {avg}/100 across {len(PILLARS)} pillars. "
        f"{len(findings)} finding(s), {highs} high-severity. "
        "Treat this as a checklist primer, not a substitute for the AWS Well-Architected Tool."
    )
