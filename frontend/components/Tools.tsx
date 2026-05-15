const tools = [
  {
    name: "suggest_services",
    desc: "Maps a use case description to a curated list of AWS services with rationale.",
    example: '"Real-time chat with WebSocket fan-out"',
  },
  {
    name: "generate_architecture_diagram",
    desc: "Produces a Mermaid diagram for common patterns (web app, RAG, event-driven, batch, agent, streaming).",
    example: 'pattern: "rag"',
  },
  {
    name: "estimate_cost",
    desc: "Rough monthly cost estimate from a list of {service, usage} items.",
    example: "lambda: 50M reqs, 5M GB-s",
  },
  {
    name: "review_well_architected",
    desc: "Lightweight 6-pillar review with findings and recommendations.",
    example: '"Public Lambda + DynamoDB, KMS encrypted"',
  },
  {
    name: "generate_adr",
    desc: "Renders an Architecture Decision Record in the MADR markdown style.",
    example: "title, context, decision, alternatives",
  },
];

export default function Tools() {
  return (
    <section className="px-6 py-16 max-w-6xl mx-auto">
      <h2 className="text-2xl md:text-3xl font-semibold mb-2">The five tools</h2>
      <p className="text-white/60 mb-10 max-w-2xl">
        Each tool is a single Python file, fully typed, fully tested. Add a tool in four steps.
      </p>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {tools.map((t) => (
          <div key={t.name} className="card p-6">
            <code className="text-accent text-sm">{t.name}</code>
            <p className="text-sm text-white/75 mt-2 leading-relaxed">{t.desc}</p>
            <p className="text-xs text-white/40 mt-3 font-mono">e.g. {t.example}</p>
          </div>
        ))}
      </div>
    </section>
  );
}
