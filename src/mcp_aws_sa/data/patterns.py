"""Mermaid templates for common AWS architecture patterns."""

from __future__ import annotations

PATTERNS: dict[str, dict[str, str]] = {
    "web-app": {
        "title": "Three-tier web app",
        "mermaid": """flowchart LR
    User((User)) --> CF[Amazon CloudFront]
    CF --> S3[(S3 - static assets)]
    CF --> APIG[API Gateway]
    APIG --> Lambda[AWS Lambda]
    Lambda --> DDB[(DynamoDB)]
    Lambda --> Cognito[Amazon Cognito]
""",
    },
    "rag": {
        "title": "RAG with Bedrock + OpenSearch",
        "mermaid": """flowchart LR
    User((User)) --> APIG[API Gateway]
    APIG --> Orchestrator[AWS Lambda - orchestrator]
    Orchestrator --> KB[Bedrock Knowledge Base]
    KB --> OS[(OpenSearch Serverless - vectors)]
    KB --> S3[(S3 - source documents)]
    Orchestrator --> LLM[Amazon Bedrock - Claude]
    LLM --> Orchestrator
    Orchestrator --> User
""",
    },
    "event-driven": {
        "title": "Event-driven processing",
        "mermaid": """flowchart LR
    Source[Producer / SaaS / app] --> EB[Amazon EventBridge]
    EB --> SQS[(SQS queue)]
    SQS --> Worker[AWS Lambda - worker]
    Worker --> DDB[(DynamoDB)]
    Worker --> S3[(S3)]
    EB -.failed.-> DLQ[(SQS DLQ)]
""",
    },
    "batch-etl": {
        "title": "Batch ETL pipeline",
        "mermaid": """flowchart LR
    Sources[Source systems] --> Raw[(S3 raw)]
    Raw --> Glue[AWS Glue ETL]
    Glue --> Curated[(S3 curated)]
    Curated --> Athena[Amazon Athena]
    Glue --> Catalog[Glue Data Catalog]
    SF[Step Functions] --> Glue
""",
    },
    "agent": {
        "title": "Agentic system with Bedrock Agents",
        "mermaid": """flowchart LR
    User((User)) --> APIG[API Gateway]
    APIG --> Agent[Bedrock Agent]
    Agent --> KB[Bedrock Knowledge Base]
    Agent --> AG1[Action Group: search]
    Agent --> AG2[Action Group: write]
    AG1 --> Lambda1[Lambda - search backend]
    AG2 --> Lambda2[Lambda - write backend]
    Lambda2 --> DDB[(DynamoDB)]
    Agent --> Guardrails[Bedrock Guardrails]
""",
    },
    "streaming": {
        "title": "Streaming ingestion + analytics",
        "mermaid": """flowchart LR
    Producers[Producers] --> Kinesis[Kinesis Data Streams]
    Kinesis --> Firehose[Kinesis Firehose]
    Firehose --> S3[(S3)]
    Kinesis --> Flink[Managed Service for Apache Flink]
    Flink --> DDB[(DynamoDB)]
    Flink --> CW[CloudWatch metrics]
""",
    },
}


def list_patterns() -> list[dict[str, str]]:
    """Return the catalog as a list of `{key, title}` pairs."""
    return [{"key": k, "title": v["title"]} for k, v in PATTERNS.items()]
