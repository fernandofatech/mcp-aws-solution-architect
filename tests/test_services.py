from mcp_aws_sa.tools.services import suggest_services


def test_real_time_chat_matches_websocket_pattern() -> None:
    out = suggest_services("Real-time chat app with WebSocket fan-out")
    names = [s["service"] for s in out["services"]]
    assert "Amazon API Gateway (WebSocket)" in names
    assert "AWS Lambda" in names
    assert "Amazon DynamoDB" in names
    assert out["matched_patterns"]


def test_rag_use_case_returns_bedrock_and_opensearch() -> None:
    out = suggest_services("Build a RAG knowledge base over internal docs")
    names = [s["service"] for s in out["services"]]
    assert "Amazon Bedrock" in names
    assert "Amazon OpenSearch Serverless (vector)" in names


def test_empty_use_case_is_handled() -> None:
    out = suggest_services("")
    assert out["services"] == []
    assert "Empty" in out["note"]


def test_unmatched_use_case_still_returns_baseline() -> None:
    out = suggest_services("Some very unusual workload xyz", include_baseline=True)
    names = [s["service"] for s in out["services"]]
    assert "AWS IAM" in names
    assert "Amazon CloudWatch" in names
    assert "AWS CloudTrail" in names


def test_baseline_can_be_excluded() -> None:
    out = suggest_services("Build a static website", include_baseline=False)
    names = [s["service"] for s in out["services"]]
    assert "AWS IAM" not in names


def test_dedup_across_overlapping_patterns() -> None:
    # 'agent' pattern and 'rag' pattern both reference Bedrock and Lambda.
    out = suggest_services("Agent with RAG over our knowledge base")
    names = [s["service"] for s in out["services"]]
    assert names.count("AWS Lambda") == 1
