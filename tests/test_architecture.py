from mcp_aws_sa.tools.architecture import (
    generate_architecture_diagram,
    list_architecture_patterns,
)


def test_list_patterns_returns_known_keys() -> None:
    patterns = list_architecture_patterns()
    keys = [p["key"] for p in patterns]
    for expected in ("web-app", "rag", "event-driven", "batch-etl", "agent", "streaming"):
        assert expected in keys


def test_generate_known_pattern_returns_mermaid() -> None:
    out = generate_architecture_diagram("rag")
    assert "error" not in out
    assert "mermaid" in out
    assert "Bedrock" in out["mermaid"]
    assert out["title"]


def test_custom_title_overrides_default() -> None:
    out = generate_architecture_diagram("web-app", title="My custom web app")
    assert out["title"] == "My custom web app"


def test_unknown_pattern_returns_error_and_available_list() -> None:
    out = generate_architecture_diagram("does-not-exist")
    assert "error" in out
    assert "available_patterns" in out
    assert len(out["available_patterns"]) >= 6


def test_pattern_key_is_case_insensitive() -> None:
    out = generate_architecture_diagram("RAG")
    assert "error" not in out
