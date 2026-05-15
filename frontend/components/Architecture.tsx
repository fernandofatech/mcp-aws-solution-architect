export default function Architecture() {
  return (
    <section className="px-6 py-16 max-w-6xl mx-auto">
      <h2 className="text-2xl md:text-3xl font-semibold mb-6">How it fits together</h2>
      <div className="card p-6 md:p-8 overflow-x-auto">
        <pre className="text-xs md:text-sm leading-relaxed">
{`flowchart LR
    Client[MCP Client]
       |  stdio (JSON-RPC)
       v
    Server[mcp-aws-sa]
       |
       +--> suggest_services      ---> service_catalog.py
       +--> generate_diagram      ---> patterns.py
       +--> estimate_cost         ---> pricing.py
       +--> review_well_arch      ---> rules
       +--> generate_adr          ---> MADR template
       \\
        \\.. (optional) Amazon Bedrock`}
        </pre>
      </div>
      <p className="text-sm text-white/55 mt-4">
        See <a className="text-accent hover:underline" href="https://fernandofatech.github.io/mcp-aws-solution-architect/architecture/">architecture docs</a> for a sequence diagram and the full module map.
      </p>
    </section>
  );
}
