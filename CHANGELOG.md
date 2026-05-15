# Changelog

All notable changes to this project will be documented in this file. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0] - 2026-05-15

### Added
- Initial MCP server with stdio transport (`mcp-aws-sa`).
- Tool `suggest_services` — use case → AWS service list with rationale.
- Tool `generate_architecture_diagram` — pattern → Mermaid diagram.
- Tool `estimate_cost` — services + usage → rough monthly cost.
- Tool `review_well_architected` — architecture description → 6-pillar review.
- Tool `generate_adr` — inputs → MADR-formatted ADR.
- pytest suite covering all five tools.
- MkDocs Material documentation site with per-tool reference and ADRs.
- Next.js landing page deployable to Vercel.
- GitHub Actions: CI (lint + test) and docs deploy to GitHub Pages.

[Unreleased]: https://github.com/fernandofatech/mcp-aws-solution-architect/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/fernandofatech/mcp-aws-solution-architect/releases/tag/v0.1.0
