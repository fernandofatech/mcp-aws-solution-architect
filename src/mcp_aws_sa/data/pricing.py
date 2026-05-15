"""Simplified monthly pricing table for `estimate_cost`.

Values are *order-of-magnitude* approximations of us-east-1 on-demand pricing.
They are intentionally embedded (not fetched) so the server is self-contained.

Each entry is a function `usage_dict → usd_monthly` so callers can pass
service-specific knobs (e.g. requests, GB-storage, GB-seconds) without the
server needing to know every dimension upfront.
"""

from __future__ import annotations

from collections.abc import Callable


def _lambda(usage: dict[str, float]) -> float:
    requests = usage.get("requests", 0)
    gb_seconds = usage.get("gb_seconds", 0)
    request_cost = max(0.0, requests - 1_000_000) * 0.20 / 1_000_000
    compute_cost = max(0.0, gb_seconds - 400_000) * 0.0000166667
    return round(request_cost + compute_cost, 2)


def _dynamodb(usage: dict[str, float]) -> float:
    on_demand_writes = usage.get("on_demand_writes", 0) * 1.25 / 1_000_000
    on_demand_reads = usage.get("on_demand_reads", 0) * 0.25 / 1_000_000
    gb_storage = usage.get("gb_storage", 0) * 0.25
    return round(on_demand_writes + on_demand_reads + gb_storage, 2)


def _s3(usage: dict[str, float]) -> float:
    gb_storage = usage.get("gb_storage", 0) * 0.023
    get_requests = usage.get("get_requests", 0) * 0.0004 / 1_000
    put_requests = usage.get("put_requests", 0) * 0.005 / 1_000
    egress_gb = usage.get("egress_gb", 0) * 0.09
    return round(gb_storage + get_requests + put_requests + egress_gb, 2)


def _api_gateway(usage: dict[str, float]) -> float:
    http_requests = usage.get("http_requests", 0) * 1.00 / 1_000_000
    return round(http_requests, 2)


def _cloudfront(usage: dict[str, float]) -> float:
    egress_gb = usage.get("egress_gb", 0) * 0.085
    requests = usage.get("requests", 0) * 0.0075 / 10_000
    return round(egress_gb + requests, 2)


def _rds(usage: dict[str, float]) -> float:
    instance_hours = usage.get("instance_hours", 730)
    hourly_rate = usage.get("hourly_rate", 0.082)  # db.t3.medium MySQL default
    gb_storage = usage.get("gb_storage", 0) * 0.115
    return round(instance_hours * hourly_rate + gb_storage, 2)


def _ec2(usage: dict[str, float]) -> float:
    instance_hours = usage.get("instance_hours", 730)
    hourly_rate = usage.get("hourly_rate", 0.0416)  # t3.medium default
    return round(instance_hours * hourly_rate, 2)


def _bedrock(usage: dict[str, float]) -> float:
    input_ktokens = usage.get("input_ktokens", 0)
    output_ktokens = usage.get("output_ktokens", 0)
    # Approx. Claude Sonnet pricing.
    return round(input_ktokens * 0.003 + output_ktokens * 0.015, 2)


def _opensearch_serverless(usage: dict[str, float]) -> float:
    ocu_hours = usage.get("ocu_hours", 730 * 2)  # min 2 OCU
    return round(ocu_hours * 0.24, 2)


def _step_functions(usage: dict[str, float]) -> float:
    transitions = usage.get("transitions", 0)
    return round(max(0.0, transitions - 4_000) * 0.025 / 1_000, 2)


def _sqs(usage: dict[str, float]) -> float:
    requests = usage.get("requests", 0)
    return round(max(0.0, requests - 1_000_000) * 0.40 / 1_000_000, 2)


def _eventbridge(usage: dict[str, float]) -> float:
    events = usage.get("events", 0)
    return round(events * 1.00 / 1_000_000, 2)


def _cognito(usage: dict[str, float]) -> float:
    maus = usage.get("maus", 0)
    return round(max(0.0, maus - 50_000) * 0.0055, 2)


PRICING: dict[str, Callable[[dict[str, float]], float]] = {
    "lambda": _lambda,
    "dynamodb": _dynamodb,
    "s3": _s3,
    "api_gateway": _api_gateway,
    "cloudfront": _cloudfront,
    "rds": _rds,
    "ec2": _ec2,
    "bedrock": _bedrock,
    "opensearch_serverless": _opensearch_serverless,
    "step_functions": _step_functions,
    "sqs": _sqs,
    "eventbridge": _eventbridge,
    "cognito": _cognito,
}


SERVICE_USAGE_HINTS: dict[str, list[str]] = {
    "lambda": ["requests", "gb_seconds"],
    "dynamodb": ["on_demand_reads", "on_demand_writes", "gb_storage"],
    "s3": ["gb_storage", "get_requests", "put_requests", "egress_gb"],
    "api_gateway": ["http_requests"],
    "cloudfront": ["egress_gb", "requests"],
    "rds": ["instance_hours", "hourly_rate", "gb_storage"],
    "ec2": ["instance_hours", "hourly_rate"],
    "bedrock": ["input_ktokens", "output_ktokens"],
    "opensearch_serverless": ["ocu_hours"],
    "step_functions": ["transitions"],
    "sqs": ["requests"],
    "eventbridge": ["events"],
    "cognito": ["maus"],
}
