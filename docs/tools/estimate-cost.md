# `estimate_cost`

Rough monthly cost estimate from a list of `{service, usage}` items.

!!! warning "Approximate"
    Uses an embedded simplified pricing table (us-east-1, on-demand). **Verify with the AWS Pricing Calculator** before any commercial decision.

## Signature

```python
estimate_cost(line_items: list[dict]) -> dict
```

## Supported services and usage knobs

| Service key | Usage knobs |
| --- | --- |
| `lambda` | `requests`, `gb_seconds` |
| `dynamodb` | `on_demand_reads`, `on_demand_writes`, `gb_storage` |
| `s3` | `gb_storage`, `get_requests`, `put_requests`, `egress_gb` |
| `api_gateway` | `http_requests` |
| `cloudfront` | `egress_gb`, `requests` |
| `rds` | `instance_hours`, `hourly_rate`, `gb_storage` |
| `ec2` | `instance_hours`, `hourly_rate` |
| `bedrock` | `input_ktokens`, `output_ktokens` |
| `opensearch_serverless` | `ocu_hours` |
| `step_functions` | `transitions` |
| `sqs` | `requests` |
| `eventbridge` | `events` |
| `cognito` | `maus` |

## Example

```json
{
  "line_items": [
    { "service": "lambda", "usage": { "requests": 50000000, "gb_seconds": 5000000 } },
    { "service": "dynamodb", "usage": { "on_demand_reads": 200000000, "on_demand_writes": 50000000, "gb_storage": 200 } },
    { "service": "api_gateway", "usage": { "http_requests": 50000000 } },
    { "service": "bedrock", "usage": { "input_ktokens": 50000, "output_ktokens": 20000 } }
  ]
}
```

Returns a `monthly_total_usd` plus a per-service breakdown and a transparency disclaimer.
