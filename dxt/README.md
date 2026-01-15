# Google Automation MCP - Desktop Extension

This directory contains a Node.js-based Desktop Extension (DXT) for one-click installation in Claude Desktop.

## How It Works

The DXT is a Node.js wrapper that spawns the Python MCP server. It tries multiple methods to start the server:

1. `uvx google-automation-mcp` (recommended)
2. `pipx run google-automation-mcp`
3. `google-automation-mcp` (if in PATH)
4. `python -m google_automation_mcp`

## Prerequisites

Before installing the DXT, you need:

1. **Python 3.10+** installed
2. **The Python package** installed via one of:
   - `pip install google-automation-mcp`
   - `pipx install google-automation-mcp`
   - Or just have `uv`/`uvx` available (it will auto-install)

3. **CLASP authentication** for Google Apps Script access:
   ```bash
   npx @anthropic-ai/clasp login
   ```

## Building the DXT

To build the `.dxt` file:

```bash
# Install dxt CLI if you don't have it
npm install -g @anthropic-ai/dxt

# Build the extension
cd dxt
dxt pack
```

This creates `google-automation-mcp.dxt` which can be installed in Claude Desktop.

## Manual Installation

If you prefer not to use the DXT, add this to your Claude Desktop config (`~/.config/claude/claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "google-automation-mcp": {
      "command": "uvx",
      "args": ["google-automation-mcp"]
    }
  }
}
```

## Development

To test the wrapper locally:

```bash
cd dxt
node index.js
```

Then send MCP messages via stdin (JSON-RPC format).
