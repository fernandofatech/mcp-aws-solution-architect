"""Smoke tests for the server module and its tool registration."""

from mcp_aws_sa import __version__, server


def test_version_is_exposed() -> None:
    assert __version__


def test_server_module_imports() -> None:
    assert hasattr(server, "main")
    assert hasattr(server, "mcp")


def test_server_info_tool_returns_metadata() -> None:
    info = server.server_info()
    assert info["name"] == "mcp-aws-solution-architect"
    assert info["version"] == __version__
    assert info["transport"] == "stdio"


def test_tools_callable_via_module() -> None:
    # Ensure the public tool wrappers work end-to-end through the server module.
    assert server.suggest_services("static website")["services"]
    assert "mermaid" in server.generate_architecture_diagram("web-app")
    assert server.estimate_cost([])["monthly_total_usd"] == 0.0
    assert server.review_well_architected("Lambda + IAM")["findings"]
    assert "Decision" in server.generate_adr("t", "c", "d")["content"]
