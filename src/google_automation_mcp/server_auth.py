"""
Authentication Tool Registrations

Registers authentication tools with the MCP server.
"""

from .tools import start_google_auth, complete_google_auth


def register_auth_tools(mcp):
    """Register authentication tools with the MCP server."""

    @mcp.tool()
    async def start_google_auth_tool() -> str:
        """
        Start Google OAuth authentication flow.

        Returns an authorization URL that must be opened in a browser.
        After authorizing, call complete_google_auth with the redirect URL.
        """
        return await start_google_auth()

    @mcp.tool()
    async def complete_google_auth_tool(redirect_url: str) -> str:
        """
        Complete the Google OAuth flow with the redirect URL.

        Args:
            redirect_url: The full URL from the browser after authorization
                          (looks like: http://localhost/?code=4/0A...&scope=...)
        """
        return await complete_google_auth(redirect_url)
