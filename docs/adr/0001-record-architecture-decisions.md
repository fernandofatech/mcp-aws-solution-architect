# 0001 — Record architecture decisions

- Status: **accepted**
- Date: 2026-05-15

## Context and problem statement

We need a way to capture significant architectural decisions so contributors and future-us can understand *why* the code looks the way it does. Without a record, every onboarding becomes archaeology.

## Decision

We will keep Architecture Decision Records (ADRs) in `docs/adr/`, one Markdown file per decision, following the [MADR](https://adr.github.io/madr/) format. The `generate_adr` tool emits records in exactly this shape.

## Alternatives considered

- **No ADRs.** Rejected — institutional memory rots fast.
- **Wiki / Notion.** Rejected — drifts from code; not reviewable in PRs.
- **Long-form RFCs.** Overkill for the scale of this project.

## Consequences

- Every non-trivial change should add or update an ADR in the same PR.
- ADRs are numbered and immutable once accepted — superseding is the path forward, not editing.
