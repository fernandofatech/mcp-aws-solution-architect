"""Curated mapping of use-case keywords → AWS services with rationale.

Intentionally compact and explicit. Extending it is a one-file diff.
"""

from __future__ import annotations


# Each entry maps a keyword set → a list of (service, category, rationale).
# Matching is OR across keywords within the same pattern. A use case may match
# multiple patterns and the suggestions are deduplicated by service.
CATALOG: list[dict[str, object]] = [
    {
        "keywords": ["real-time", "realtime", "chat", "websocket", "multiplayer", "live"],
        "services": [
            {
                "service": "Amazon API Gateway (WebSocket)",
                "category": "Networking",
                "rationale": "Managed WebSocket endpoint with built-in connection registry.",
            },
            {
                "service": "AWS Lambda",
                "category": "Compute",
                "rationale": "Event-driven handlers for connect/disconnect/message routes; pay-per-use.",
            },
            {
                "service": "Amazon DynamoDB",
                "category": "Database",
                "rationale": "Single-digit-ms reads/writes for session and connection state.",
            },
            {
                "service": "Amazon ElastiCache (Redis)",
                "category": "Cache",
                "rationale": "Low-latency pub/sub or presence tracking when needed across instances.",
            },
        ],
    },
    {
        "keywords": ["rag", "retrieval", "knowledge base", "kb", "embedding", "semantic search"],
        "services": [
            {
                "service": "Amazon Bedrock",
                "category": "AI/ML",
                "rationale": "Managed access to foundation models (Claude, Nova, Titan) and Knowledge Bases.",
            },
            {
                "service": "Amazon OpenSearch Serverless (vector)",
                "category": "Search",
                "rationale": "Managed vector store with hybrid search; pairs with Bedrock KB out of the box.",
            },
            {
                "service": "Amazon S3",
                "category": "Storage",
                "rationale": "Source of truth for documents fed into the KB.",
            },
            {
                "service": "AWS Lambda",
                "category": "Compute",
                "rationale": "Ingestion and retrieval orchestration.",
            },
        ],
    },
    {
        "keywords": ["agent", "agents", "tool use", "tool-use", "mcp", "workflow", "multi-agent"],
        "services": [
            {
                "service": "Amazon Bedrock Agents",
                "category": "AI/ML",
                "rationale": "First-class agent runtime with action groups, KB integration and guardrails.",
            },
            {
                "service": "AWS Step Functions",
                "category": "Orchestration",
                "rationale": "Deterministic orchestration when multi-step agent workflows need durable state.",
            },
            {
                "service": "Amazon DynamoDB",
                "category": "Database",
                "rationale": "Agent memory / session storage.",
            },
            {
                "service": "AWS Lambda",
                "category": "Compute",
                "rationale": "Action-group implementations and tool backends.",
            },
        ],
    },
    {
        "keywords": ["web app", "webapp", "website", "spa", "frontend", "static site"],
        "services": [
            {
                "service": "Amazon S3 + CloudFront",
                "category": "Hosting",
                "rationale": "Static asset hosting with global CDN.",
            },
            {
                "service": "AWS Amplify Hosting",
                "category": "Hosting",
                "rationale": "Git-based deployment for SPAs and SSR frontends with branch previews.",
            },
            {
                "service": "Amazon API Gateway",
                "category": "Networking",
                "rationale": "REST/HTTP entrypoint for the backend.",
            },
            {
                "service": "AWS Lambda",
                "category": "Compute",
                "rationale": "Serverless backend handlers.",
            },
            {
                "service": "Amazon Cognito",
                "category": "Identity",
                "rationale": "Managed auth (OAuth, social IdP, MFA).",
            },
        ],
    },
    {
        "keywords": ["batch", "etl", "pipeline", "data pipeline", "ingest", "transform"],
        "services": [
            {
                "service": "AWS Glue",
                "category": "Data",
                "rationale": "Serverless Spark ETL with a managed data catalog.",
            },
            {
                "service": "Amazon S3",
                "category": "Storage",
                "rationale": "Raw / staging / curated zones — the canonical data lake foundation.",
            },
            {
                "service": "AWS Step Functions",
                "category": "Orchestration",
                "rationale": "Workflow control and retries across the ETL stages.",
            },
            {
                "service": "Amazon Athena",
                "category": "Analytics",
                "rationale": "Pay-per-query SQL over S3 for exploration and downstream consumption.",
            },
        ],
    },
    {
        "keywords": ["event", "event-driven", "queue", "pubsub", "fanout", "async"],
        "services": [
            {
                "service": "Amazon EventBridge",
                "category": "Eventing",
                "rationale": "Schema-aware event bus with rule-based routing and partner sources.",
            },
            {
                "service": "Amazon SQS",
                "category": "Messaging",
                "rationale": "Decoupling and back-pressure with at-least-once delivery.",
            },
            {
                "service": "Amazon SNS",
                "category": "Messaging",
                "rationale": "Fan-out to multiple subscribers (Lambda, SQS, email, HTTP).",
            },
            {
                "service": "AWS Lambda",
                "category": "Compute",
                "rationale": "Consumers triggered by events.",
            },
        ],
    },
    {
        "keywords": ["ml", "machine learning", "training", "inference", "model"],
        "services": [
            {
                "service": "Amazon SageMaker",
                "category": "AI/ML",
                "rationale": "Managed training, hosting and pipelines for custom models.",
            },
            {
                "service": "Amazon S3",
                "category": "Storage",
                "rationale": "Datasets and model artifacts.",
            },
            {
                "service": "AWS Lambda",
                "category": "Compute",
                "rationale": "Lightweight inference proxies or pre/post-processing.",
            },
        ],
    },
    {
        "keywords": ["analytics", "dashboard", "bi", "reporting", "warehouse"],
        "services": [
            {
                "service": "Amazon Redshift Serverless",
                "category": "Data Warehouse",
                "rationale": "On-demand columnar warehouse for ad-hoc analytics.",
            },
            {
                "service": "Amazon QuickSight",
                "category": "BI",
                "rationale": "Managed dashboards with per-session pricing.",
            },
            {
                "service": "AWS Glue",
                "category": "Data",
                "rationale": "Catalog + ETL feeding the warehouse.",
            },
        ],
    },
]


# Sensible defaults applied to almost every use case.
BASELINE_SERVICES: list[dict[str, str]] = [
    {
        "service": "AWS IAM",
        "category": "Security",
        "rationale": "Least-privilege access — required for every workload.",
    },
    {
        "service": "Amazon CloudWatch",
        "category": "Observability",
        "rationale": "Metrics, logs and alarms for the stack.",
    },
    {
        "service": "AWS CloudTrail",
        "category": "Governance",
        "rationale": "Audit trail of API calls — non-negotiable for any production account.",
    },
]
