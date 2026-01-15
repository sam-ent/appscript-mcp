# Contributing

## Development Setup

```bash
git clone https://github.com/sam-ent/google-automation-mcp.git
cd google-automation-mcp
uv sync
```

## Running Tests

```bash
uv run pytest tests/ -v
```

## Linting

```bash
uv run ruff check .
uv run ruff format .
```

## Upstream Sync

This standalone MCP is also maintained as part of [google_workspace_mcp](https://github.com/sam-ent/google_workspace_mcp), a fork of [taylorwilsdon/google_workspace_mcp](https://github.com/taylorwilsdon/google_workspace_mcp).

**When adding features to this project, also add them to the upstream fork** to keep both in sync and contribute back to the broader Google Workspace MCP ecosystem.

Upstream location: `gappsscript/apps_script_tools.py`

## Publishing

Package is published to PyPI. To release a new version:

1. Update version in `pyproject.toml`
2. Run tests: `uv run pytest tests/ -v`
3. Build: `uv build`
4. Publish: `uv publish --token $PYPI_UPLOAD_TOKEN`
