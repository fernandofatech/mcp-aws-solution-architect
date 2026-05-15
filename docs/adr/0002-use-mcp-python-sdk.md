# 0002 — Use the official MCP Python SDK (FastMCP)

- Status: **accepted**
- Date: 2026-05-15

## Context and problem statement

The Model Context Protocol has multiple language bindings. We need to pick one and ideally an ergonomic API on top of it.

The trade-offs:

- **Official `mcp` Python SDK** — first-party, follows the spec closely, includes a `FastMCP` API that mirrors decorator-style web frameworks (Flask, FastAPI).
- **TypeScript SDK** — also first-party, equally mature. Different audience.
- **Hand-rolled JSON-RPC.** Maximum control, but every protocol revision becomes our problem.

## Decision

Use the official `mcp` Python SDK with the `FastMCP` API. Python is the de-facto language for the AWS/AI tooling community we are targeting; `FastMCP` reduces boilerplate to a `@mcp.tool()` decorator per tool.

## Consequences

- We accept a minor version pin on `mcp>=1.2.0` to stay close to spec changes.
- Tool functions are normal Python — easy to unit-test without the protocol in the loop.
- A future port to TypeScript would be plausible but is out of scope.
