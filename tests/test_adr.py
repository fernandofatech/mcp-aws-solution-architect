from mcp_aws_sa.tools.adr import generate_adr


def test_minimal_adr_renders() -> None:
    out = generate_adr(
        title="Use DynamoDB for session storage",
        context="We need single-digit-ms reads for session tokens.",
        decision="We will use DynamoDB on-demand with TTL-based expiry.",
    )
    assert out["filename"] == "use-dynamodb-for-session-storage.md"
    assert "# Use DynamoDB for session storage" in out["content"]
    assert "Status: **proposed**" in out["content"]
    assert "## Context and problem statement" in out["content"]
    assert "## Decision" in out["content"]


def test_alternatives_and_consequences_render_as_bullets() -> None:
    out = generate_adr(
        title="X",
        context="ctx",
        decision="dec",
        alternatives=["Option A", "Option B"],
        consequences=["+ Faster", "- More expensive"],
    )
    assert "- Option A" in out["content"]
    assert "- Option B" in out["content"]
    assert "- + Faster" in out["content"]
    assert "- - More expensive" in out["content"]


def test_status_is_respected() -> None:
    out = generate_adr(title="X", context="c", decision="d", status="accepted")
    assert "Status: **accepted**" in out["content"]


def test_empty_title_falls_back_to_default_slug() -> None:
    out = generate_adr(title="", context="c", decision="d")
    assert out["filename"].endswith(".md")
    assert out["filename"]  # non-empty


def test_slugify_handles_special_chars() -> None:
    out = generate_adr(title="Use Step Functions (orchestrate ETL!)", context="c", decision="d")
    assert out["filename"] == "use-step-functions-orchestrate-etl.md"
