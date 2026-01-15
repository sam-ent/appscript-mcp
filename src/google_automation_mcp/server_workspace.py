"""
Google Workspace Tool Registrations

Registers Gmail, Drive, Sheets, Calendar, and Docs tools with the MCP server.
"""

from .tools import (
    # Gmail
    search_gmail_messages,
    get_gmail_message,
    send_gmail_message,
    list_gmail_labels,
    modify_gmail_labels,
    # Drive
    search_drive_files,
    list_drive_items,
    get_drive_file_content,
    create_drive_file,
    create_drive_folder,
    delete_drive_file,
    trash_drive_file,
    share_drive_file,
    list_drive_permissions,
    remove_drive_permission,
    # Sheets
    list_spreadsheets,
    get_sheet_values,
    update_sheet_values,
    create_spreadsheet,
    append_sheet_values,
    get_spreadsheet_metadata,
    # Calendar
    list_calendars,
    get_events,
    create_event,
    delete_event,
    update_event,
    # Docs
    search_docs,
    get_doc_content,
    create_doc,
    modify_doc_text,
    append_doc_text,
)


def register_workspace_tools(mcp):
    """Register Google Workspace tools with the MCP server."""

    # ========================================================================
    # Gmail Tools
    # ========================================================================

    @mcp.tool()
    async def search_gmail_messages_tool(
        user_google_email: str,
        query: str = "",
        max_results: int = 10,
    ) -> str:
        """
        Search for Gmail messages matching a query.

        Args:
            user_google_email: The user's Google email address
            query: Gmail search query (e.g., "from:user@example.com subject:hello")
            max_results: Maximum number of messages to return (default: 10)
        """
        return await search_gmail_messages(
            user_google_email=user_google_email,
            query=query,
            max_results=max_results,
        )

    @mcp.tool()
    async def get_gmail_message_tool(
        user_google_email: str,
        message_id: str,
        format: str = "full",
    ) -> str:
        """
        Get a specific Gmail message by ID.

        Args:
            user_google_email: The user's Google email address
            message_id: The message ID to retrieve
            format: Message format - "full", "metadata", or "minimal"
        """
        return await get_gmail_message(
            user_google_email=user_google_email,
            message_id=message_id,
            format=format,
        )

    @mcp.tool()
    async def send_gmail_message_tool(
        user_google_email: str,
        to: str,
        subject: str,
        body: str,
        cc: str = "",
        bcc: str = "",
        html: bool = False,
    ) -> str:
        """
        Send a Gmail message.

        Args:
            user_google_email: The user's Google email address
            to: Recipient email address(es), comma-separated
            subject: Email subject
            body: Email body content
            cc: Optional CC recipients, comma-separated
            bcc: Optional BCC recipients, comma-separated
            html: If True, body is treated as HTML
        """
        return await send_gmail_message(
            user_google_email=user_google_email,
            to=to,
            subject=subject,
            body=body,
            cc=cc if cc else None,
            bcc=bcc if bcc else None,
            html=html,
        )

    @mcp.tool()
    async def list_gmail_labels_tool(user_google_email: str) -> str:
        """
        List all Gmail labels for the user.

        Args:
            user_google_email: The user's Google email address
        """
        return await list_gmail_labels(user_google_email=user_google_email)

    @mcp.tool()
    async def modify_gmail_labels_tool(
        user_google_email: str,
        message_id: str,
        add_labels: list = None,
        remove_labels: list = None,
    ) -> str:
        """
        Modify labels on a Gmail message.

        Common label IDs:
        - INBOX - Message in inbox
        - UNREAD - Message is unread
        - STARRED - Message is starred
        - TRASH - Message in trash
        - SPAM - Message in spam
        - IMPORTANT - Message marked important

        Args:
            user_google_email: The user's Google email address
            message_id: The message ID to modify
            add_labels: List of label IDs to add (e.g., ["STARRED", "IMPORTANT"])
            remove_labels: List of label IDs to remove (e.g., ["UNREAD", "INBOX"])

        Examples:
            - Archive: remove_labels=["INBOX"]
            - Mark read: remove_labels=["UNREAD"]
            - Mark unread: add_labels=["UNREAD"]
            - Star: add_labels=["STARRED"]
            - Move to trash: add_labels=["TRASH"]
        """
        return await modify_gmail_labels(
            user_google_email=user_google_email,
            message_id=message_id,
            add_labels=add_labels,
            remove_labels=remove_labels,
        )

    # ========================================================================
    # Drive Tools
    # ========================================================================

    @mcp.tool()
    async def search_drive_files_tool(
        user_google_email: str,
        query: str,
        page_size: int = 10,
    ) -> str:
        """
        Search for files and folders in Google Drive.

        Args:
            user_google_email: The user's Google email address
            query: Search query string. Supports Drive query operators:
                   - name contains 'example'
                   - mimeType = 'application/vnd.google-apps.spreadsheet'
                   - fullText contains 'keyword'
                   - modifiedTime > '2024-01-01'
            page_size: Maximum number of files to return (default: 10)
        """
        return await search_drive_files(
            user_google_email=user_google_email,
            query=query,
            page_size=page_size,
        )

    @mcp.tool()
    async def list_drive_items_tool(
        user_google_email: str,
        folder_id: str = "root",
        page_size: int = 50,
    ) -> str:
        """
        List files and folders in a Drive folder.

        Args:
            user_google_email: The user's Google email address
            folder_id: The folder ID to list (default: 'root' for My Drive root)
            page_size: Maximum number of items to return (default: 50)
        """
        return await list_drive_items(
            user_google_email=user_google_email,
            folder_id=folder_id,
            page_size=page_size,
        )

    @mcp.tool()
    async def get_drive_file_content_tool(
        user_google_email: str,
        file_id: str,
    ) -> str:
        """
        Get the content of a Google Drive file.

        Supports Google Docs (-> text), Sheets (-> CSV), Slides (-> text), and text files.

        Args:
            user_google_email: The user's Google email address
            file_id: The Drive file ID
        """
        return await get_drive_file_content(
            user_google_email=user_google_email,
            file_id=file_id,
        )

    @mcp.tool()
    async def create_drive_file_tool(
        user_google_email: str,
        file_name: str,
        content: str = "",
        folder_id: str = "root",
        mime_type: str = "text/plain",
    ) -> str:
        """
        Create a new file in Google Drive.

        Args:
            user_google_email: The user's Google email address
            file_name: Name for the new file
            content: File content (text)
            folder_id: Parent folder ID (default: 'root')
            mime_type: MIME type of the file (default: 'text/plain')
        """
        return await create_drive_file(
            user_google_email=user_google_email,
            file_name=file_name,
            content=content,
            folder_id=folder_id,
            mime_type=mime_type,
        )

    @mcp.tool()
    async def create_drive_folder_tool(
        user_google_email: str,
        folder_name: str,
        parent_id: str = "root",
    ) -> str:
        """
        Create a new folder in Google Drive.

        Args:
            user_google_email: The user's Google email address
            folder_name: Name for the new folder
            parent_id: Parent folder ID (default: 'root' for My Drive root)
        """
        return await create_drive_folder(
            user_google_email=user_google_email,
            folder_name=folder_name,
            parent_id=parent_id,
        )

    @mcp.tool()
    async def delete_drive_file_tool(
        user_google_email: str,
        file_id: str,
    ) -> str:
        """
        Permanently delete a file from Google Drive.

        WARNING: This permanently deletes the file. Use trash_drive_file for recoverable deletion.

        Args:
            user_google_email: The user's Google email address
            file_id: The file ID to delete
        """
        return await delete_drive_file(
            user_google_email=user_google_email,
            file_id=file_id,
        )

    @mcp.tool()
    async def trash_drive_file_tool(
        user_google_email: str,
        file_id: str,
    ) -> str:
        """
        Move a file to trash in Google Drive (recoverable).

        Args:
            user_google_email: The user's Google email address
            file_id: The file ID to trash
        """
        return await trash_drive_file(
            user_google_email=user_google_email,
            file_id=file_id,
        )

    @mcp.tool()
    async def share_drive_file_tool(
        user_google_email: str,
        file_id: str,
        email: str,
        role: str = "reader",
        send_notification: bool = True,
    ) -> str:
        """
        Share a file or folder with a user.

        Args:
            user_google_email: The user's Google email address
            file_id: The file or folder ID to share
            email: Email address of the user to share with
            role: Permission role - "reader", "writer", "commenter", or "owner"
            send_notification: Whether to send an email notification (default: True)
        """
        return await share_drive_file(
            user_google_email=user_google_email,
            file_id=file_id,
            email=email,
            role=role,
            send_notification=send_notification,
        )

    @mcp.tool()
    async def list_drive_permissions_tool(
        user_google_email: str,
        file_id: str,
    ) -> str:
        """
        List all permissions on a file or folder.

        Args:
            user_google_email: The user's Google email address
            file_id: The file or folder ID
        """
        return await list_drive_permissions(
            user_google_email=user_google_email,
            file_id=file_id,
        )

    @mcp.tool()
    async def remove_drive_permission_tool(
        user_google_email: str,
        file_id: str,
        permission_id: str,
    ) -> str:
        """
        Remove a permission from a file or folder.

        Args:
            user_google_email: The user's Google email address
            file_id: The file or folder ID
            permission_id: The permission ID to remove (from list_drive_permissions)
        """
        return await remove_drive_permission(
            user_google_email=user_google_email,
            file_id=file_id,
            permission_id=permission_id,
        )

    # ========================================================================
    # Sheets Tools
    # ========================================================================

    @mcp.tool()
    async def list_spreadsheets_tool(
        user_google_email: str,
        query: str = "",
        page_size: int = 20,
    ) -> str:
        """
        List Google Sheets spreadsheets in Drive.

        Args:
            user_google_email: The user's Google email address
            query: Optional search query to filter spreadsheets
            page_size: Maximum number of spreadsheets to return (default: 20)
        """
        return await list_spreadsheets(
            user_google_email=user_google_email,
            query=query,
            page_size=page_size,
        )

    @mcp.tool()
    async def get_sheet_values_tool(
        user_google_email: str,
        spreadsheet_id: str,
        range: str = "Sheet1",
        value_render: str = "FORMATTED_VALUE",
    ) -> str:
        """
        Get values from a Google Sheet.

        Args:
            user_google_email: The user's Google email address
            spreadsheet_id: The spreadsheet ID
            range: A1 notation range (e.g., "Sheet1!A1:D10" or just "Sheet1")
            value_render: How values should be rendered - "FORMATTED_VALUE", "UNFORMATTED_VALUE", or "FORMULA"
        """
        return await get_sheet_values(
            user_google_email=user_google_email,
            spreadsheet_id=spreadsheet_id,
            range=range,
            value_render=value_render,
        )

    @mcp.tool()
    async def update_sheet_values_tool(
        user_google_email: str,
        spreadsheet_id: str,
        range: str,
        values: list,
        value_input: str = "USER_ENTERED",
    ) -> str:
        """
        Update values in a Google Sheet.

        Args:
            user_google_email: The user's Google email address
            spreadsheet_id: The spreadsheet ID
            range: A1 notation range (e.g., "Sheet1!A1:D10")
            values: 2D array of values to write. Example: [["Header1", "Header2"], ["Value1", "Value2"]]
            value_input: How input values should be interpreted - "USER_ENTERED" or "RAW"
        """
        return await update_sheet_values(
            user_google_email=user_google_email,
            spreadsheet_id=spreadsheet_id,
            range=range,
            values=values,
            value_input=value_input,
        )

    @mcp.tool()
    async def create_spreadsheet_tool(
        user_google_email: str,
        title: str,
        sheet_names: list = None,
    ) -> str:
        """
        Create a new Google Spreadsheet.

        Args:
            user_google_email: The user's Google email address
            title: Title for the new spreadsheet
            sheet_names: Optional list of sheet names to create (default: ["Sheet1"])
        """
        return await create_spreadsheet(
            user_google_email=user_google_email,
            title=title,
            sheet_names=sheet_names,
        )

    @mcp.tool()
    async def append_sheet_values_tool(
        user_google_email: str,
        spreadsheet_id: str,
        range: str,
        values: list,
        value_input: str = "USER_ENTERED",
    ) -> str:
        """
        Append values to a Google Sheet (adds rows after existing data).

        Args:
            user_google_email: The user's Google email address
            spreadsheet_id: The spreadsheet ID
            range: A1 notation range to append to (e.g., "Sheet1!A:D" or "Sheet1")
            values: 2D array of values to append. Example: [["Value1", "Value2"], ["Value3", "Value4"]]
            value_input: How input values should be interpreted - "USER_ENTERED" or "RAW"
        """
        return await append_sheet_values(
            user_google_email=user_google_email,
            spreadsheet_id=spreadsheet_id,
            range=range,
            values=values,
            value_input=value_input,
        )

    @mcp.tool()
    async def get_spreadsheet_metadata_tool(
        user_google_email: str,
        spreadsheet_id: str,
    ) -> str:
        """
        Get metadata about a spreadsheet including all sheet names and properties.

        Args:
            user_google_email: The user's Google email address
            spreadsheet_id: The spreadsheet ID
        """
        return await get_spreadsheet_metadata(
            user_google_email=user_google_email,
            spreadsheet_id=spreadsheet_id,
        )

    # ========================================================================
    # Calendar Tools
    # ========================================================================

    @mcp.tool()
    async def list_calendars_tool(user_google_email: str) -> str:
        """
        List all calendars accessible to the user.

        Args:
            user_google_email: The user's Google email address
        """
        return await list_calendars(user_google_email=user_google_email)

    @mcp.tool()
    async def get_events_tool(
        user_google_email: str,
        calendar_id: str = "primary",
        max_results: int = 10,
        time_min: str = "",
        time_max: str = "",
        query: str = "",
    ) -> str:
        """
        Get events from a calendar.

        Args:
            user_google_email: The user's Google email address
            calendar_id: Calendar ID (default: 'primary')
            max_results: Maximum number of events to return (default: 10)
            time_min: Start time in ISO format (default: now)
            time_max: End time in ISO format (default: 7 days from now)
            query: Optional search query string
        """
        return await get_events(
            user_google_email=user_google_email,
            calendar_id=calendar_id,
            max_results=max_results,
            time_min=time_min if time_min else None,
            time_max=time_max if time_max else None,
            query=query if query else None,
        )

    @mcp.tool()
    async def create_event_tool(
        user_google_email: str,
        summary: str,
        start_time: str,
        end_time: str,
        calendar_id: str = "primary",
        description: str = "",
        location: str = "",
        attendees: str = "",
        all_day: bool = False,
    ) -> str:
        """
        Create a new calendar event.

        Args:
            user_google_email: The user's Google email address
            summary: Event title
            start_time: Start time in ISO format (e.g., "2024-01-15T09:00:00") or date for all-day (e.g., "2024-01-15")
            end_time: End time in ISO format (e.g., "2024-01-15T10:00:00") or date for all-day (e.g., "2024-01-16")
            calendar_id: Calendar ID (default: 'primary')
            description: Optional event description
            location: Optional event location
            attendees: Optional comma-separated list of attendee emails
            all_day: If True, create an all-day event (use date format for start/end)
        """
        return await create_event(
            user_google_email=user_google_email,
            summary=summary,
            start_time=start_time,
            end_time=end_time,
            calendar_id=calendar_id,
            description=description if description else None,
            location=location if location else None,
            attendees=attendees if attendees else None,
            all_day=all_day,
        )

    @mcp.tool()
    async def delete_event_tool(
        user_google_email: str,
        event_id: str,
        calendar_id: str = "primary",
    ) -> str:
        """
        Delete a calendar event.

        Args:
            user_google_email: The user's Google email address
            event_id: The event ID to delete
            calendar_id: Calendar ID (default: 'primary')
        """
        return await delete_event(
            user_google_email=user_google_email,
            event_id=event_id,
            calendar_id=calendar_id,
        )

    @mcp.tool()
    async def update_event_tool(
        user_google_email: str,
        event_id: str,
        calendar_id: str = "primary",
        summary: str = "",
        start_time: str = "",
        end_time: str = "",
        description: str = "",
        location: str = "",
        attendees: str = "",
        all_day: bool = False,
    ) -> str:
        """
        Update an existing calendar event.

        Args:
            user_google_email: The user's Google email address
            event_id: The event ID to update
            calendar_id: Calendar ID (default: 'primary')
            summary: New event title (optional)
            start_time: New start time in ISO format (optional)
            end_time: New end time in ISO format (optional)
            description: New description (optional)
            location: New location (optional)
            attendees: New comma-separated list of attendee emails (optional)
            all_day: If True and updating times, use date format
        """
        return await update_event(
            user_google_email=user_google_email,
            event_id=event_id,
            calendar_id=calendar_id,
            summary=summary if summary else None,
            start_time=start_time if start_time else None,
            end_time=end_time if end_time else None,
            description=description if description else None,
            location=location if location else None,
            attendees=attendees if attendees else None,
            all_day=all_day,
        )

    # ========================================================================
    # Docs Tools
    # ========================================================================

    @mcp.tool()
    async def search_docs_tool(
        user_google_email: str,
        query: str,
        page_size: int = 10,
    ) -> str:
        """
        Search for Google Docs by name.

        Args:
            user_google_email: The user's Google email address
            query: Search query string
            page_size: Maximum number of docs to return (default: 10)
        """
        return await search_docs(
            user_google_email=user_google_email,
            query=query,
            page_size=page_size,
        )

    @mcp.tool()
    async def get_doc_content_tool(
        user_google_email: str,
        document_id: str,
    ) -> str:
        """
        Get the content of a Google Doc.

        Args:
            user_google_email: The user's Google email address
            document_id: The document ID
        """
        return await get_doc_content(
            user_google_email=user_google_email,
            document_id=document_id,
        )

    @mcp.tool()
    async def create_doc_tool(
        user_google_email: str,
        title: str,
        content: str = "",
    ) -> str:
        """
        Create a new Google Doc.

        Args:
            user_google_email: The user's Google email address
            title: Document title
            content: Optional initial content
        """
        return await create_doc(
            user_google_email=user_google_email,
            title=title,
            content=content,
        )

    @mcp.tool()
    async def modify_doc_text_tool(
        user_google_email: str,
        document_id: str,
        text: str,
        index: int = 1,
        replace_text: str = "",
    ) -> str:
        """
        Modify text in a Google Doc.

        Args:
            user_google_email: The user's Google email address
            document_id: The document ID
            text: Text to insert (or replace with)
            index: Position to insert text (default: 1, start of document)
            replace_text: If provided, find and replace this text with 'text'
        """
        return await modify_doc_text(
            user_google_email=user_google_email,
            document_id=document_id,
            text=text,
            index=index,
            replace_text=replace_text if replace_text else None,
        )

    @mcp.tool()
    async def append_doc_text_tool(
        user_google_email: str,
        document_id: str,
        text: str,
    ) -> str:
        """
        Append text to the end of a Google Doc.

        Args:
            user_google_email: The user's Google email address
            document_id: The document ID
            text: Text to append to the end of the document
        """
        return await append_doc_text(
            user_google_email=user_google_email,
            document_id=document_id,
            text=text,
        )
