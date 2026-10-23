"""
Scriptling Discord Messaging - Type stubs for IntelliSense support.

Provides a bot client for the Discord messaging platform.

Setup:
    1. Go to https://discord.com/developers/applications
    2. Create a new application and add a bot
    3. Enable "Message Content Intent" under Privileged Gateway Intents
    4. Copy the bot token

Usage:
    export DISCORD_TOKEN="your-bot-token"

    import scriptling.messaging.discord as discord
    client = discord.client(os.environ["DISCORD_TOKEN"])
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

class DiscordClient(MessagingClient):
    """
    Discord bot client returned by client().

    Has every MessagingClient method; each is also a module-level function
    taking the client as its first argument (e.g. discord.run(client)).
    """
    ...

def client(
    token: str,
    *,
    allowed_users: Optional[list[str]] = None
) -> DiscordClient:
    """
    Create a Discord bot client.

    Parameters:
        token: Bot token from Discord Developer Portal
        allowed_users: Optional list of user IDs allowed to use the bot

    Returns:
        DiscordClient instance

    Example:
        client = discord.client("MTk4NjIyNDgzNDc...")
        client = discord.client(token, allowed_users=["123456789012345678"])
    """
    ...

def keyboard(rows: Keyboard) -> Keyboard:
    """Build a Discord keyboard. See scriptling.messaging.keyboard for details."""
    ...

@overload
def answer_callback(client: DiscordClient, id: str, text: str = "") -> None: ...
@overload
def answer_callback(client: DiscordClient, id: str, token: str, text: str) -> None: ...
def answer_callback(client: DiscordClient, id: str, *args: str) -> None:
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

def auth(client: DiscordClient, handler: AuthHandler) -> None:
    """
    Register auth handler.

    Parameters:
        client: Client from client()
        handler: Function that returns True to allow access, False to deny
    """
    ...

def capabilities(client: DiscordClient) -> list[str]:
    """
    Get list of platform capability strings.

    Parameters:
        client: Client from client()

    Returns:
        List of capability strings for this platform
    """
    ...

@overload
def command(client: DiscordClient, name: str, handler: Handler) -> None: ...
@overload
def command(client: DiscordClient, name: str, help_text: str, handler: Handler) -> None: ...
def command(client: DiscordClient, name: str, *args: Any) -> None:
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

def delete_message(client: DiscordClient, dest: str, message_id: str) -> None:
    """
    Delete a message.

    Parameters:
        client: Client from client()
        dest: Destination ID
        message_id: Message ID to delete
    """
    ...

def download(client: DiscordClient, ref: str) -> str:
    """
    Download a file by ID or URL.

    Parameters:
        client: Client from client()
        ref: File ID or URL

    Returns:
        Base64-encoded file data

    The bot token is sent only to the platform's own hosts. A URL on
    any other host is fetched without it and must pass the host's
    network policy (raising an error if denied).
    """
    ...

def edit_message(client: DiscordClient, dest: str, message_id: str, text: str) -> None:
    """
    Edit a sent message.

    Parameters:
        client: Client from client()
        dest: Destination ID
        message_id: Message ID to edit
        text: New text content
    """
    ...

@overload
def on_callback(client: DiscordClient, handler: Handler) -> None: ...
@overload
def on_callback(client: DiscordClient, prefix: str, handler: Handler) -> None: ...
def on_callback(client: DiscordClient, *args: Any) -> None:
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

def on_file(client: DiscordClient, handler: Handler) -> None:
    """
    Register file attachment handler.

    Parameters:
        client: Client from client()
        handler: Function called when file/photo received
    """
    ...

def on_message(client: DiscordClient, handler: Handler) -> None:
    """
    Register default message handler.

    Parameters:
        client: Client from client()
        handler: Function called for non-command messages
    """
    ...

def run(client: DiscordClient) -> None:
    """
    Start the bot event loop (blocks until stopped).

    Parameters:
        client: Client from client()
    """
    ...

def send_file(
    client: DiscordClient,
    dest: str,
    source: str,
    *,
    filename: str = "",
    caption: str = "",
    base64: bool = False
) -> None:
    """
    Send a file.

    Parameters:
        client: Client from client()
        dest: Destination ID
        source: File path, URL, or base64 data
        filename: Optional filename
        caption: Optional caption
        base64: True if source is base64-encoded data

    Raises:
        PermissionError: (uncatchable) if source is a local file outside the
            host's allowed paths (--allowed-paths)
    """
    ...

def send_message(
    client: DiscordClient,
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

def send_rich_message(client: DiscordClient, dest: str, message: MessageDict) -> None:
    """
    Send a rich message.

    Parameters:
        client: Client from client()
        dest: Destination ID
        message: MessageDict with title, body, color, image, url
    """
    ...

def typing(client: DiscordClient, dest: str) -> None:
    """
    Send typing indicator.

    Parameters:
        client: Client from client()
        dest: Destination ID
    """
    ...
