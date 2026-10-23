"""
Scriptling Slack Messaging - Type stubs for IntelliSense support.

Provides a bot client for the Slack messaging platform using Socket Mode.

Setup:
    1. Create an app at https://api.slack.com/apps
    2. Enable Socket Mode and generate an App-Level Token (xapp-...)
    3. Add bot scopes: chat:write, files:write, users:read, im:history
    4. Subscribe to bot event: message.im
    5. Enable "Messages Tab" in App Home
    6. Install app and copy Bot User OAuth Token (xoxb-...)

Usage:
    export SLACK_BOT_TOKEN="xoxb-..."
    export SLACK_APP_TOKEN="xapp-..."

    import scriptling.messaging.slack as slack
    client = slack.client(os.environ["SLACK_BOT_TOKEN"], os.environ["SLACK_APP_TOKEN"])
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

class SlackClient(MessagingClient):
    """
    Slack bot client returned by client().

    Has every MessagingClient method; each is also a module-level function
    taking the client as its first argument (e.g. slack.run(client)).
    """

    def open_dm(self, user_id: str) -> str:
        """
        Open or retrieve a DM channel with a user.

        Parameters:
            user_id: Slack user ID (e.g. "U12345678")

        Returns:
            The DM channel ID, usable as dest
        """
        ...

def client(
    bot_token: str,
    app_token: str,
    *,
    allowed_users: Optional[list[str]] = None
) -> SlackClient:
    """
    Create a Slack bot client.

    Parameters:
        bot_token: Bot User OAuth Token (xoxb-...)
        app_token: App-Level Token (xapp-...)
        allowed_users: Optional list of user IDs allowed to use the bot

    Returns:
        SlackClient instance

    Example:
        client = slack.client("xoxb-...", "xapp-...")
        client = slack.client(bot_token, app_token, allowed_users=["U12345678"])
    """
    ...

def keyboard(rows: Keyboard) -> Keyboard:
    """Build a Slack keyboard. See scriptling.messaging.keyboard for details."""
    ...

@overload
def answer_callback(client: SlackClient, id: str, text: str = "") -> None: ...
@overload
def answer_callback(client: SlackClient, id: str, token: str, text: str) -> None: ...
def answer_callback(client: SlackClient, id: str, *args: str) -> None:
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

def auth(client: SlackClient, handler: AuthHandler) -> None:
    """
    Register auth handler.

    Parameters:
        client: Client from client()
        handler: Function that returns True to allow access, False to deny
    """
    ...

def capabilities(client: SlackClient) -> list[str]:
    """
    Get list of platform capability strings.

    Parameters:
        client: Client from client()

    Returns:
        List of capability strings for this platform
    """
    ...

@overload
def command(client: SlackClient, name: str, handler: Handler) -> None: ...
@overload
def command(client: SlackClient, name: str, help_text: str, handler: Handler) -> None: ...
def command(client: SlackClient, name: str, *args: Any) -> None:
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

def delete_message(client: SlackClient, dest: str, message_id: str) -> None:
    """
    Delete a message.

    Parameters:
        client: Client from client()
        dest: Destination ID
        message_id: Message ID to delete
    """
    ...

def download(client: SlackClient, ref: str) -> str:
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

def edit_message(client: SlackClient, dest: str, message_id: str, text: str) -> None:
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
def on_callback(client: SlackClient, handler: Handler) -> None: ...
@overload
def on_callback(client: SlackClient, prefix: str, handler: Handler) -> None: ...
def on_callback(client: SlackClient, *args: Any) -> None:
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

def on_file(client: SlackClient, handler: Handler) -> None:
    """
    Register file attachment handler.

    Parameters:
        client: Client from client()
        handler: Function called when file/photo received
    """
    ...

def on_message(client: SlackClient, handler: Handler) -> None:
    """
    Register default message handler.

    Parameters:
        client: Client from client()
        handler: Function called for non-command messages
    """
    ...

def open_dm(client: SlackClient, user_id: str) -> str:
    """
    Open or retrieve a DM channel with a user.

    Parameters:
        client: Client from client()
        user_id: Slack user ID (e.g. "U12345678")

    Returns:
        The DM channel ID, usable as dest

    Example:
        channel = slack.open_dm(client, "U12345678")
        slack.send_message(client, channel, "Hello!")
    """
    ...

def run(client: SlackClient) -> None:
    """
    Start the bot event loop (blocks until stopped).

    Parameters:
        client: Client from client()
    """
    ...

def send_file(
    client: SlackClient,
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
    client: SlackClient,
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

def send_rich_message(client: SlackClient, dest: str, message: MessageDict) -> None:
    """
    Send a rich message.

    Parameters:
        client: Client from client()
        dest: Destination ID
        message: MessageDict with title, body, color, image, url
    """
    ...

def typing(client: SlackClient, dest: str) -> None:
    """
    Send typing indicator.

    Parameters:
        client: Client from client()
        dest: Destination ID
    """
    ...
