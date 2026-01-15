"""
Google Automation MCP Server

MCP server for Google Apps Script and Google Workspace automation.
Supports 50 tools across Gmail, Drive, Sheets, Calendar, Docs, and Apps Script.
"""

__version__ = "0.5.0"


def __getattr__(name):
    """Lazy import to avoid circular dependencies."""
    if name == "appscript_tools":
        from . import appscript_tools
        return appscript_tools
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
