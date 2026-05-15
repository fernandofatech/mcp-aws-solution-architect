const features = [
  {
    title: "Deterministic by default",
    body:
      "No LLM dependency to ship. The catalog, pricing and patterns are explicit Python data — anyone can read them in two minutes.",
  },
  {
    title: "MCP-native",
    body:
      "Uses the official mcp Python SDK with FastMCP-style tool registration. Wires into Claude Desktop, Cursor, Cline and custom agents.",
  },
  {
    title: "Typed and tested",
    body:
      "Strict mypy, Pydantic models, full pytest coverage of every tool's behavior. CI runs on Python 3.11 and 3.12.",
  },
  {
    title: "Bedrock-ready (optional)",
    body:
      "Each tool can be backed by Amazon Bedrock for richer output, gated behind extras. Off by default — first run requires zero AWS setup.",
  },
  {
    title: "Documented end-to-end",
    body:
      "MkDocs Material site with per-tool reference, ADRs, architecture sequence diagrams, and a roadmap.",
  },
  {
    title: "Conventional Commits + gitflow",
    body:
      "Every change is a PR with a Conventional Commit title. main is protected, develop is the integration branch.",
  },
];

export default function Features() {
  return (
    <section className="px-6 py-16 max-w-6xl mx-auto">
      <h2 className="text-2xl md:text-3xl font-semibold mb-10">Why this exists</h2>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {features.map((f) => (
          <div key={f.title} className="card p-6">
            <h3 className="text-base font-semibold mb-2">{f.title}</h3>
            <p className="text-sm text-white/70 leading-relaxed">{f.body}</p>
          </div>
        ))}
      </div>
    </section>
  );
}
