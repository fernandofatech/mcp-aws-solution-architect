from mcp_aws_sa.tools.cost import estimate_cost


def test_empty_line_items_returns_zero_total_and_hints() -> None:
    out = estimate_cost([])
    assert out["monthly_total_usd"] == 0.0
    assert "supported_services" in out
    assert "lambda" in out["supported_services"]


def test_lambda_within_free_tier_costs_zero() -> None:
    out = estimate_cost(
        [{"service": "lambda", "usage": {"requests": 1_000_000, "gb_seconds": 400_000}}]
    )
    assert out["monthly_total_usd"] == 0.0


def test_lambda_above_free_tier_costs_money() -> None:
    out = estimate_cost(
        [{"service": "lambda", "usage": {"requests": 10_000_000, "gb_seconds": 1_400_000}}]
    )
    assert out["monthly_total_usd"] > 0
    assert "lambda" in out["by_service"]


def test_multiple_services_sum_correctly() -> None:
    out = estimate_cost(
        [
            {"service": "s3", "usage": {"gb_storage": 1000}},
            {"service": "dynamodb", "usage": {"gb_storage": 100}},
        ]
    )
    expected = round(out["by_service"]["s3"] + out["by_service"]["dynamodb"], 2)
    assert out["monthly_total_usd"] == expected


def test_unknown_service_is_skipped_with_note() -> None:
    out = estimate_cost([{"service": "imaginary", "usage": {}}])
    assert out["monthly_total_usd"] == 0.0
    assert any("Unknown service" in n for n in out["notes"])


def test_disclaimer_always_present() -> None:
    out = estimate_cost([{"service": "s3", "usage": {"gb_storage": 10}}])
    assert "disclaimer" in out
    assert "Approximate" in out["disclaimer"]


def test_bedrock_pricing_scales_with_tokens() -> None:
    cheap = estimate_cost(
        [{"service": "bedrock", "usage": {"input_ktokens": 100, "output_ktokens": 50}}]
    )["monthly_total_usd"]
    pricey = estimate_cost(
        [{"service": "bedrock", "usage": {"input_ktokens": 10_000, "output_ktokens": 5_000}}]
    )["monthly_total_usd"]
    assert pricey > cheap * 50
