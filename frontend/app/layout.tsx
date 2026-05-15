import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "mcp-aws-solution-architect — MCP copilot for AWS architects",
  description:
    "An MCP server that exposes AWS Solution Architect tools (services, diagrams, cost, Well-Architected, ADR) to any MCP-aware client.",
  authors: [{ name: "Fernando Francisco Azevedo", url: "https://fernando.moretes.com" }],
  openGraph: {
    title: "mcp-aws-solution-architect",
    description:
      "MCP server exposing AWS Solution Architect tools (services, diagrams, cost, Well-Architected, ADR).",
    url: "https://mcp-aws-solution-architect.vercel.app",
    siteName: "mcp-aws-solution-architect",
    type: "website",
  },
  twitter: {
    card: "summary_large_image",
    title: "mcp-aws-solution-architect",
    description: "MCP server exposing AWS Solution Architect tools.",
  },
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body className="antialiased">{children}</body>
    </html>
  );
}
