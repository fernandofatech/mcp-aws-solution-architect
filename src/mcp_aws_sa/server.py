"""MCP server entrypoint.

Registers all five tools and runs over stdio (the MCP default).
"""

from __future__ import annotations

from typing import Any

from mcp.server.fastmcp import FastMCP

from mcp_aws_sa import __version__
from mcp_aws_sa.tools import (
    estimate_cost as _estimate_cost,
)
from mcp_aws_sa.tools import (
    generate_adr as _generate_adr,
)
from mcp_aws_sa.tools import (
    generate_architecture_diagram as _generate_architecture_diagram,
)
from mcp_aws_sa.tools import (
    list_architecture_patterns as _list_architecture_patterns,
)
from mcp_aws_sa.tools import (
    review_well_architected as _review_well_architected,
)
from mcp_aws_sa.tools import (
    suggest_services as _suggest_services,
)


mcp = FastMCP("aws-solution-architect")


@mcp.tool()
def suggest_services(use_case: str, include_baseline: bool = True) -> dict[str, Any]:
    """Suggest AWS services for a use case.

    Args:
        use_case: Free-form description of what is being built.
        include_baseline: Append baseline services (IAM, CloudWatch, CloudTrail).
    """
    return _suggest_services(use_case=use_case, include_baseline=include_baseline)


@mcp.tool()
def list_architecture_patterns() -> list[dict[str, str]]:
    """List the available architecture pattern keys and titles."""
    return _list_architecture_patterns()


@mcp.tool()
def generate_architecture_diagram(pattern: str, title: str | None = None) -> dict[str, Any]:
    """Return a Mermaid diagram for a named architecture pattern.

    Use `list_architecture_patterns` to discover valid pattern keys.
    """
    return _generate_architecture_diagram(pattern=pattern, title=title)


@mcp.tool()
def estimate_cost(line_items: list[dict[str, Any]]) -> dict[str, Any]:
    """Rough monthly cost estimate for a list of `{service, usage}` items.

    Approximate. Verify with the AWS Pricing Calculator for commercial decisions.
    """
    return _estimate_cost(line_items=line_items)


@mcp.tool()
def review_well_architected(architecture: str) -> dict[str, Any]:
    """Lightweight Well-Architected review across the six pillars.

    Best used as a primer or first pass — not a substitute for the AWS WA Tool.
    """
    return _review_well_architected(architecture=architecture)


@mcp.tool()
def generate_adr(
    title: str,
    context: str,
    decision: str,
    alternatives: list[str] | None = None,
    consequences: list[str] | None = None,
    status: str = "proposed",
) -> dict[str, str]:
    """Render a MADR-style Architecture Decision Record from inputs."""
    return _generate_adr(
        title=title,
        context=context,
        decision=decision,
        alternatives=alternatives,
        consequences=consequences,
        status=status,
    )


@mcp.tool()
def server_info() -> dict[str, str]:
    """Return basic metadata about this server (version, transport, repo)."""
    return {
        "name": "mcp-aws-solution-architect",
        "version": __version__,
        "transport": "stdio",
        "repository": "https://github.com/fernandofatech/mcp-aws-solution-architect",
        "docs": "https://fernandofatech.github.io/mcp-aws-solution-architect/",
    }


def main() -> None:
    """Console entrypoint used by the ``mcp-aws-sa`` script."""
    mcp.run()


if __name__ == "__main__":
    main()
