import { access, readFile } from "node:fs/promises";

for (const file of ["public/index.html", "public/styles.css", "vercel.json"]) {
  await access(file);
}

const html = await readFile("public/index.html", "utf8");
const css = await readFile("public/styles.css", "utf8");
const links = [...html.matchAll(/href="([^"]+)"/g)].map((match) => match[1]);
const hasRepoLink = links.some((link) => {
  const url = new URL(link, "https://portfolio.local");
  return (
    url.protocol === "https:" &&
    url.hostname === "github.com" &&
    url.pathname === "/fernandofatech/mcp-aws-solution-architect"
  );
});

const checks = [
  [html.includes("<main"), "index.html must include a main landmark"],
  [html.includes("mcp-aws-solution-architect"), "index.html must include the project name"],
  [html.includes("suggest_services"), "index.html must include MCP tool names"],
  [hasRepoLink, "index.html must link to GitHub"],
  [css.includes(":focus-visible"), "styles.css must include visible focus states"],
  [css.includes("@media"), "styles.css must include responsive rules"],
];

const failures = checks.filter(([passed]) => !passed).map(([, message]) => message);

if (failures.length > 0) {
  console.error(failures.join("\n"));
  process.exit(1);
}

console.log("Static landing checks passed.");
