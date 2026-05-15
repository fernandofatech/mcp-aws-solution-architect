export default function Hero() {
  return (
    <section className="px-6 pt-20 pb-16 md:pt-32 md:pb-24 max-w-6xl mx-auto">
      <div className="flex flex-col items-start gap-6">
        <div className="inline-flex items-center gap-2 rounded-full border border-white/10 bg-white/5 px-3 py-1 text-xs text-white/70">
          <span className="h-2 w-2 rounded-full bg-accent"></span>
          MCP server · Python · v0.1.0
        </div>
        <h1 className="text-4xl md:text-6xl font-semibold tracking-tight">
          The <span className="gradient-text">AWS Solution Architect</span>
          <br />
          copilot, exposed via MCP.
        </h1>
        <p className="text-lg md:text-xl text-white/70 max-w-2xl">
          Five deterministic tools — service suggestions, Mermaid diagrams, rough cost,
          Well-Architected review, ADR generation — callable from Claude Desktop, Cursor, Cline
          or any custom agent.
        </p>
        <div className="flex flex-wrap gap-3 pt-2">
          <a
            href="https://github.com/fernandofatech/mcp-aws-solution-architect"
            className="inline-flex items-center gap-2 rounded-lg bg-accent px-4 py-2.5 text-sm font-medium hover:bg-accent/90 transition"
          >
            View on GitHub →
          </a>
          <a
            href="https://fernandofatech.github.io/mcp-aws-solution-architect/"
            className="inline-flex items-center gap-2 rounded-lg border border-white/15 bg-white/5 px-4 py-2.5 text-sm font-medium hover:bg-white/10 transition"
          >
            Read the docs
          </a>
        </div>
      </div>
    </section>
  );
}
