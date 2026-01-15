"""
Google Authentication Tools

Provides OAuth authentication helpers for the MCP server.
"""

from ..auth import (
    start_auth_flow,
    complete_auth_flow,
    set_pending_flow,
    get_pending_flow,
    clear_pending_flow,
)


async def start_google_auth() -> str:
    """
    Start Google OAuth authentication flow.

    Returns an authorization URL that must be opened in a browser.
    After authorizing, call complete_google_auth with the redirect URL.

    Returns:
        str: Instructions with the authorization URL
    """
    try:
        auth_url, flow = start_auth_flow()
        set_pending_flow(flow)

        return (
            "Google OAuth Authentication\n"
            "============================\n\n"
            "1. Open this URL in your browser:\n\n"
            f"   {auth_url}\n\n"
            "2. Sign in and authorize the application\n\n"
            "3. You will be redirected to http://localhost (page will not load)\n\n"
            "4. Copy the FULL URL from your browser address bar\n"
            "   (looks like: http://localhost/?code=4/0A...&scope=...)\n\n"
            "5. Call complete_google_auth with the redirect URL"
        )
    except FileNotFoundError as e:
        return str(e)
    except Exception as e:
        return f"Failed to start authentication: {str(e)}"


async def complete_google_auth(redirect_url: str) -> str:
    """
    Complete the Google OAuth flow with the redirect URL.

    Args:
        redirect_url: The full URL from the browser after authorization

    Returns:
        str: Success or error message
    """
    flow = get_pending_flow()
    if flow is None:
        return "No pending authentication flow. Please run start_google_auth first."

    try:
        creds = complete_auth_flow(flow, redirect_url)
        clear_pending_flow()

        # Get user email to confirm
        try:
            from google.oauth2 import id_token
            from google.auth.transport import requests

            info = id_token.verify_oauth2_token(
                creds.id_token, requests.Request(), creds.client_id
            )
            email = info.get("email", "unknown")
        except Exception:
            email = "authenticated user"

        return f"Authentication successful for {email}.\n\nYou can now use all Apps Script tools."
    except Exception as e:
        clear_pending_flow()
        return f"Authentication failed: {str(e)}\n\nPlease run start_google_auth to try again."
