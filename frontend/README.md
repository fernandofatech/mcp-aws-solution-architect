# mcp-aws-sa landing

Dependency-free static landing page for [mcp-aws-solution-architect](../).

## Local development

```bash
cd frontend
npm run lint
npm run build
npm run dev
```

## Deploy on Vercel

The repo includes `.github/workflows/vercel.yml` for GitHub Actions based deploys.
Configure these repository secrets before enabling production deploys:

- `VERCEL_TOKEN`
- `VERCEL_ORG_ID`
- `VERCEL_PROJECT_ID`
