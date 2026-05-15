"""Tool: estimate_cost — line items → rough monthly USD cost."""

from __future__ import annotations

from mcp_aws_sa.data.pricing import PRICING, SERVICE_USAGE_HINTS


def estimate_cost(line_items: list[dict[str, object]]) -> dict[str, object]:
    """Estimate monthly cost from a list of `{service, usage}` items.

    Args:
        line_items: List of dicts shaped like
            ``{"service": "lambda", "usage": {"requests": 5_000_000, "gb_seconds": 1_200_000}}``.
            Recognised service keys are returned by ``list_supported_services()``
            via the ``supported_services`` field in the response when something
            is missing.

    Returns:
        A dict with ``monthly_total_usd``, ``by_service``, ``notes`` and a
        ``disclaimer``. Unknown services are reported in ``notes`` and skipped.
    """
    if not line_items:
        return {
            "monthly_total_usd": 0.0,
            "by_service": {},
            "notes": ["No line items provided."],
            "supported_services": sorted(PRICING.keys()),
            "usage_hints": SERVICE_USAGE_HINTS,
            "disclaimer": _DISCLAIMER,
        }

    by_service: dict[str, float] = {}
    notes: list[str] = []

    for item in line_items:
        service = str(item.get("service", "")).strip().lower()
        usage_raw = item.get("usage", {}) or {}
        if not isinstance(usage_raw, dict):
            notes.append(f"Item for '{service}': 'usage' must be a dict — skipped.")
            continue
        usage: dict[str, float] = {str(k): float(v) for k, v in usage_raw.items()}

        if service not in PRICING:
            notes.append(
                f"Unknown service '{service}' — skipped. "
                f"Supported: {', '.join(sorted(PRICING.keys()))}."
            )
            continue

        cost = PRICING[service](usage)
        by_service[service] = round(by_service.get(service, 0.0) + cost, 2)

    total = round(sum(by_service.values()), 2)

    return {
        "monthly_total_usd": total,
        "by_service": by_service,
        "notes": notes or ["All items priced."],
        "usage_hints": SERVICE_USAGE_HINTS,
        "disclaimer": _DISCLAIMER,
    }


_DISCLAIMER = (
    "Approximate. Uses an embedded simplified pricing table (us-east-1, on-demand). "
    "Verify with the AWS Pricing Calculator before any commercial decision."
)
