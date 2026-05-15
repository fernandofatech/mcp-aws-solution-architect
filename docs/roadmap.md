# Roadmap

## Near term

- [ ] Optional **Bedrock backend** per tool (Claude Sonnet / Nova) for richer reasoning, gated behind an env var.
- [ ] **Live AWS Pricing API** integration for `estimate_cost` (the embedded table becomes the offline fallback).
- [ ] Additional architecture patterns: **data lake**, **ML inference**, **hybrid (on-prem ↔ AWS)**.

## Mid term

- [ ] **HTTP transport** in addition to stdio — enables remote MCP servers and shared team deployments.
- [ ] Export `generate_architecture_diagram` to **draw.io XML** and **PNG**.
- [ ] **Resource exposure** (MCP "resources" primitive) for service catalog and pricing table — clients can browse them.

## Long term

- [ ] **Prompt templates** for common SA flows (greenfield design, brownfield assessment, cost review) using the MCP "prompts" primitive.
- [ ] Multi-region pricing and SLA-aware recommendations.
- [ ] Companion CLI (`mcp-aws-sa-cli`) for non-MCP use cases.

## Out of scope (for now)

- Generating Terraform / CDK code. (There are excellent tools already.)
- Real-time monitoring or alerting on AWS accounts.
- Anything that requires write access to AWS.
