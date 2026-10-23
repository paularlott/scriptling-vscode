"""
Scriptling Console Messaging - Type stubs for IntelliSense support.

Provides a local TUI console bot for testing handlers without network.
Useful for testing before deploying to Telegram/Discord/Slack.

Usage:
    import scriptling.messaging.console as msg_console

    client = msg_console.client()
    client.command("/start", "Start the bot", handle_start)
    client.run()
"""

from typing import Any, Optional, overload
from scriptling.messaging import (
    MessagingClient,
    Handler,
    AuthHandler,
    Message,
    MessageDict,
    Keyboard,
    Button,
    ButtonWithData,
    ButtonWithURL,
    ContextDict,
    UserDict,
    FileDict,
)

class ConsoleClient(MessagingClient):
    """
    Console bot client returned by client().

    Has every MessagingClient method; each is also a module-level function
    taking the client as its first argument (e.g. msg_console.run(client)).
    """
    ...

def client() -> ConsoleClient:
    """
    Create a console bot client.

    Returns:
        ConsoleClient instance

    Example:
        import scriptling.messaging.console as msg_console

        client = msg_console.client()
        client.run()
    """
    ...

@overload
def answer_callback(client: ConsoleClient, id: str, text: str = "") -> None: ...
@overload
def answer_callback(client: ConsoleClient, id: str, token: str, text: str) -> None: ...
def answer_callback(client: ConsoleClient, id: str, *args: str) -> None:
    """
    Acknowledge a button press.

    Called as answer_callback(client, id, text="") or
    answer_callback(client, id, token, text); text may also be given as text=.

    Parameters:
        client: Client from client()
        id: Callback ID (ctx["callback_id"])
        token: Callback token (Discord, ctx["callback_token"])
        text: Optional text to show
    """
    ...

def auth(client: ConsoleClient, handler: AuthHandler) -> None:
    """
    Register auth handler.

    Parameters:
        client: Client from client()
        handler: Function that returns True to allow access, False to deny
    """
    ...

def capabilities(client: ConsoleClient) -> list[str]:
    """
    Get list of platform capability strings.

    Parameters:
        client: Client from client()

    Returns:
        List of capability strings for this platform
    """
    ...

@overload
def command(client: ConsoleClient, name: str, handler: Handler) -> None: ...
@overload
def command(client: ConsoleClient, name: str, help_text: str, handler: Handler) -> None: ...
def command(client: ConsoleClient, name: str, *args: Any) -> None:
    """
    Register a command handler.

    Called as command(client, name, handler) or
    command(client, name, help_text, handler).

    Parameters:
        client: Client from client()
        name: Command name (e.g., '/start', '/help')
        help_text: Optional description shown in help
        handler: Function called with context dict
    """
    ...

def delete_message(client: ConsoleClient, dest: str, message_id: str) -> None:
    """
    Delete a message.

    The console client accepts this and does nothing.

    Parameters:
        client: Client from client()
        dest: Destination ID
        message_id: Message ID to delete
    """
    ...

def download(client: ConsoleClient, ref: str) -> str:
    """
    Download a file by ID or URL.

    Parameters:
        client: Client from client()
        ref: File ID or URL

    Returns:
        Base64-encoded file data (always "" on the console, which has no files)
    """
    ...

def edit_message(client: ConsoleClient, dest: str, message_id: str, text: str) -> None:
    """
    Edit a sent message.

    The console client accepts this and does nothing.

    Parameters:
        client: Client from client()
        dest: Destination ID
        message_id: Message ID to edit
        text: New text content
    """
    ...

@overload
def on_callback(client: ConsoleClient, handler: Handler) -> None: ...
@overload
def on_callback(client: ConsoleClient, prefix: str, handler: Handler) -> None: ...
def on_callback(client: ConsoleClient, *args: Any) -> None:
    """
    Register a callback/button handler.

    Called as on_callback(client, handler) or
    on_callback(client, prefix, handler).

    Parameters:
        client: Client from client()
        prefix: Optional prefix to filter callbacks
        handler: Function called with context dict when button pressed
    """
    ...

def on_file(client: ConsoleClient, handler: Handler) -> None:
    """
    Register file attachment handler.

    Parameters:
        client: Client from client()
        handler: Function called when file/photo received
    """
    ...

def on_message(client: ConsoleClient, handler: Handler) -> None:
    """
    Register default message handler.

    Parameters:
        client: Client from client()
        handler: Function called for non-command messages
    """
    ...

def run(client: ConsoleClient) -> None:
    """
    Start the bot event loop (blocks until stopped).

    Parameters:
        client: Client from client()
    """
    ...

def send_file(
    client: ConsoleClient,
    dest: str,
    source: str,
    *,
    filename: str = "",
    caption: str = "",
    base64: bool = False
) -> None:
    """
    Send a file.

    Not supported on the console: always raises an error
    ("console: send_file not supported").

    Parameters:
        client: Client from client()
        dest: Destination ID
        source: File path, URL, or base64 data
        filename: Optional filename
        caption: Optional caption
        base64: True if source is base64-encoded data

    Raises:
        An error, always
    """
    ...

def send_message(
    client: ConsoleClient,
    dest: str,
    message: Message,
    *,
    parse_mode: str = "",
    keyboard: Optional[Keyboard] = None
) -> None:
    """
    Send a message to a destination.

    Parameters:
        client: Client from client()
        dest: Destination ID (user/channel)
        message: String or MessageDict with rich content
        parse_mode: Parse mode (e.g., 'markdown', 'html')
        keyboard: Optional button keyboard
    """
    ...

def send_rich_message(client: ConsoleClient, dest: str, message: MessageDict) -> None:
    """
    Send a rich message.

    Parameters:
        client: Client from client()
        dest: Destination ID
        message: MessageDict with title, body, color, image, url
    """
    ...

def typing(client: ConsoleClient, dest: str) -> None:
    """
    Send typing indicator.

    Parameters:
        client: Client from client()
        dest: Destination ID
    """
    ...
