"""Tool: suggest_services — use case → AWS service list with rationale."""

from __future__ import annotations

from mcp_aws_sa.data.service_catalog import BASELINE_SERVICES, CATALOG


def suggest_services(use_case: str, include_baseline: bool = True) -> dict[str, object]:
    """Suggest AWS services for a use case description.

    The implementation is deterministic and keyword-based — transparent and easy
    to audit. The returned shape is stable so MCP clients can render it.

    Args:
        use_case: Free-form description of what is being built.
        include_baseline: Whether to append baseline services (IAM, CloudWatch, CloudTrail).

    Returns:
        A dict with `services` (list of dicts) and `matched_patterns` (list of strings).
    """
    if not use_case or not use_case.strip():
        return {
            "services": [],
            "matched_patterns": [],
            "note": "Empty use case. Describe what you are building in one or two sentences.",
        }

    lowered = use_case.lower()
    matched_patterns: list[str] = []
    seen_services: set[str] = set()
    suggestions: list[dict[str, str]] = []

    for entry in CATALOG:
        keywords = entry["keywords"]
        assert isinstance(keywords, list)
        if any(kw in lowered for kw in keywords):
            matched_patterns.append(", ".join(keywords[:2]))
            services = entry["services"]
            assert isinstance(services, list)
            for svc in services:
                assert isinstance(svc, dict)
                key = svc["service"]
                if key not in seen_services:
                    seen_services.add(key)
                    suggestions.append(dict(svc))

    if include_baseline:
        for svc in BASELINE_SERVICES:
            if svc["service"] not in seen_services:
                seen_services.add(svc["service"])
                suggestions.append(dict(svc))

    return {
        "services": suggestions,
        "matched_patterns": matched_patterns,
        "note": (
            "No catalog pattern matched — only baseline services returned. "
            "Refine the use case with terms like 'real-time', 'rag', 'agent', 'event-driven', etc."
            if not matched_patterns
            else f"Matched {len(matched_patterns)} pattern(s)."
        ),
    }
