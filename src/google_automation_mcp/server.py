"""
Google Automation MCP Server

MCP server for Google Apps Script and Google Workspace with unified authentication.
Supports clasp (no GCP project needed), OAuth 2.0, and OAuth 2.1.

Tool registrations are split into modules:
- server_auth.py: Authentication tools
- server_appscript.py: Apps Script project, deployment, version, process, and metrics tools
- server_workspace.py: Gmail, Drive, Sheets, Calendar, and Docs tools
"""

import logging

from fastmcp import FastMCP

from . import __version__
from .server_auth import register_auth_tools
from .server_appscript import register_appscript_tools
from .server_workspace import register_workspace_tools

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

# Create MCP server
mcp = FastMCP("Apps Script MCP")

# Register all tools
register_auth_tools(mcp)
register_appscript_tools(mcp)
register_workspace_tools(mcp)


def main():
    """Run the MCP server."""
    logger.info(f"Starting Apps Script MCP Server v{__version__}")
    logger.info("Authentication: clasp (recommended) or OAuth 2.0/2.1")
    logger.info("Run 'google-automation-mcp setup' to configure authentication")
    mcp.run()


if __name__ == "__main__":
    main()
