export default function Quickstart() {
  return (
    <section className="px-6 py-16 max-w-6xl mx-auto">
      <h2 className="text-2xl md:text-3xl font-semibold mb-10">Quickstart</h2>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div>
          <h3 className="text-sm uppercase tracking-wider text-white/50 mb-3">Install</h3>
          <pre className="text-sm">
{`git clone git@github.com:fernandofatech/mcp-aws-solution-architect.git
cd mcp-aws-solution-architect
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"`}
          </pre>
        </div>
        <div>
          <h3 className="text-sm uppercase tracking-wider text-white/50 mb-3">Wire into Claude Desktop</h3>
          <pre className="text-sm">
{`{
  "mcpServers": {
    "aws-solution-architect": {
      "command": "mcp-aws-sa"
    }
  }
}`}
          </pre>
          <p className="text-xs text-white/50 mt-2">
            File: <code>~/Library/Application Support/Claude/claude_desktop_config.json</code>
          </p>
        </div>
      </div>
    </section>
  );
}
