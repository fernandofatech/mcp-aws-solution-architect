# Contributing

Thanks for thinking about contributing!

## Workflow

This repo follows **gitflow**:

- `main` — stable releases only, protected branch, every commit is tagged.
- `develop` — integration branch, default for new work.
- `feature/*` — branched off `develop`, merged back with `--no-ff`.
- `release/*` — branched off `develop` when cutting a release.
- `hotfix/*` — branched off `main` for urgent fixes.

### Open a PR

1. `git checkout develop && git pull`
2. `git checkout -b feature/short-description`
3. Make your changes, following the conventions below.
4. `git push -u origin feature/short-description`
5. Open a PR **into `develop`** (not `main`). Fill the PR template.

## Conventions

- **Commits:** [Conventional Commits](https://www.conventionalcommits.org). Examples:
  - `feat(tools): add new pattern to generate_architecture_diagram`
  - `fix(cost): correct DynamoDB on-demand pricing`
  - `docs: update Claude Desktop wiring instructions`
- **Code style:** `ruff check . && ruff format .` must pass.
- **Types:** `mypy src` must pass (strict mode).
- **Tests:** add tests for every new tool or change in behavior. `pytest` must pass.
- **Docs:** if you change a tool's interface or add a new one, update both the docstring and the matching page in `docs/tools/`.

## Local setup

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev,docs]"
pre-commit install   # optional
```

## Running the server locally

```bash
mcp-aws-sa
```

For development with a real MCP client, point Claude Desktop / Cursor / Cline to your local binary path.

## Reporting bugs

Open an issue with a minimal repro, expected vs actual, and your environment (Python version, MCP client, OS).
