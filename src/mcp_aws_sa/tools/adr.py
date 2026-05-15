"""Tool: generate_adr — inputs → MADR-formatted Architecture Decision Record."""

from __future__ import annotations

from datetime import UTC, datetime


def generate_adr(
    title: str,
    context: str,
    decision: str,
    alternatives: list[str] | None = None,
    consequences: list[str] | None = None,
    status: str = "proposed",
) -> dict[str, str]:
    """Render a Markdown ADR in the MADR (Markdown Architecture Decision Record) style.

    Args:
        title: Short title of the decision (one line). Will be slugified for the filename.
        context: Forces at play (technical, organizational, etc.).
        decision: The decision made — clear, in active voice ("We will...").
        alternatives: Other options considered. Pass an empty list to omit.
        consequences: Positive and negative outcomes. Pass an empty list to omit.
        status: One of ``proposed``, ``accepted``, ``deprecated``, ``superseded``.

    Returns:
        A dict with ``filename`` (slug.md) and ``content`` (the full Markdown).
    """
    title = (title or "").strip() or "untitled-decision"
    today = datetime.now(UTC).strftime("%Y-%m-%d")
    slug = _slugify(title)

    alts = alternatives or []
    cons = consequences or []

    lines: list[str] = [
        f"# {title}",
        "",
        f"- Status: **{status}**",
        f"- Date: {today}",
        "",
        "## Context and problem statement",
        "",
        context.strip() or "_TODO: describe the forces at play._",
        "",
        "## Decision",
        "",
        decision.strip() or "_TODO: state the decision._",
        "",
    ]

    if alts:
        lines.append("## Alternatives considered")
        lines.append("")
        for a in alts:
            lines.append(f"- {a}")
        lines.append("")

    if cons:
        lines.append("## Consequences")
        lines.append("")
        for c in cons:
            lines.append(f"- {c}")
        lines.append("")

    return {
        "filename": f"{slug}.md",
        "content": "\n".join(lines).rstrip() + "\n",
    }


def _slugify(text: str) -> str:
    out = []
    for ch in text.lower().strip():
        if ch.isalnum():
            out.append(ch)
        elif ch in (" ", "-", "_"):
            out.append("-")
    slug = "".join(out)
    while "--" in slug:
        slug = slug.replace("--", "-")
    return slug.strip("-") or "adr"
