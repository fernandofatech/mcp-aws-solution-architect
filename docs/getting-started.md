# Getting started

## Install

=== "From source"

    ```bash
    git clone git@github.com:fernandofatech/mcp-aws-solution-architect.git
    cd mcp-aws-solution-architect
    python -m venv .venv && source .venv/bin/activate
    pip install -e ".[dev]"
    ```

=== "PyPI (planned)"

    ```bash
    pip install mcp-aws-solution-architect
    ```

## Run

```bash
mcp-aws-sa
```

The server speaks **stdio** (the MCP default). It reads JSON-RPC messages on stdin and writes responses to stdout, so it is meant to be launched **by an MCP client**, not directly inspected in a terminal.

## Wire into a client

=== "Claude Desktop"

    Edit `~/Library/Application Support/Claude/claude_desktop_config.json`:

    ```json
    {
      "mcpServers": {
        "aws-solution-architect": {
          "command": "mcp-aws-sa",
          "args": []
        }
      }
    }
    ```

    Restart Claude Desktop. The tools appear in the tool list.

=== "Cursor"

    Open Settings → Features → MCP and add:

    ```json
    {
      "mcpServers": {
        "aws-solution-architect": { "command": "mcp-aws-sa" }
      }
    }
    ```

=== "Cline / Continue / custom"

    Any client that speaks the MCP protocol can launch the server with `mcp-aws-sa`. Use a virtual env-aware path if you don't expose the binary globally.

## Verify

Once wired, ask the assistant:

> *"What AWS services would you recommend for a multi-tenant SaaS with file uploads and async processing? Use the SA tools."*

You should see tool calls flowing to `mcp-aws-solution-architect`.

## Troubleshooting

| Symptom | Likely cause |
| --- | --- |
| Tools don't show up in Claude Desktop | Restart Claude Desktop after editing the config; check the log at `~/Library/Logs/Claude/`. |
| `mcp-aws-sa: command not found` | Activate the venv where you installed, or use the absolute path in the client config. |
| Server hangs | It is waiting on stdin — that is correct when not invoked by a client. |
