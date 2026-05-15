"""Tool: generate_architecture_diagram — pattern → Mermaid diagram."""

from __future__ import annotations

from mcp_aws_sa.data.patterns import PATTERNS, list_patterns


def list_architecture_patterns() -> list[dict[str, str]]:
    """Return the available pattern keys and their titles.

    Useful for clients that want to surface choices before calling
    `generate_architecture_diagram`.
    """
    return list_patterns()


def generate_architecture_diagram(pattern: str, title: str | None = None) -> dict[str, object]:
    """Return a Mermaid diagram for a named pattern.

    Args:
        pattern: One of the keys returned by `list_architecture_patterns`
            (e.g. ``web-app``, ``rag``, ``event-driven``, ``batch-etl``, ``agent``, ``streaming``).
        title: Optional custom title — defaults to the pattern's canonical title.

    Returns:
        A dict with ``pattern``, ``title`` and ``mermaid`` keys. The ``mermaid``
        value is a string that can be rendered directly by Mermaid-compatible
        clients.
    """
    key = pattern.strip().lower()
    if key not in PATTERNS:
        return {
            "error": f"Unknown pattern '{pattern}'.",
            "available_patterns": list_patterns(),
        }

    entry = PATTERNS[key]
    return {
        "pattern": key,
        "title": title or entry["title"],
        "mermaid": entry["mermaid"],
    }
