"""
Scriptling Messaging Library - Type stubs for IntelliSense support.

This library provides messaging functions for sending messages with
rich content and interactive keyboards across platforms.

All platforms (telegram, discord, slack, console) share the same API.
"""

from typing import TypedDict, Optional, Union, Literal, Callable, Any

# =============================================================================
# Message Types
# =============================================================================

class MessageDict(TypedDict, total=False):
    """Rich message content structure for reply() and send_message()."""
    title: str
    """Message title (rendered bold on Telegram, as embed title on Discord)."""
    body: str
    """Main message body text."""
    color: str
    """Message accent color (e.g., 'blue', 'red', '#00ff00')."""
    image: str
    """URL of an image to display in the message."""
    url: str
    """URL to link the message to."""

Message = Union[str, MessageDict]
"""A message can be a simple string or a rich MessageDict."""

# =============================================================================
# Keyboard Types
# =============================================================================

class ButtonWithData(TypedDict, total=False):
    """Button with callback data for handling clicks."""
    text: str
    """Button label text."""
    data: str
    """Callback data returned when button is clicked."""

class ButtonWithURL(TypedDict, total=False):
    """Button that opens a URL when clicked."""
    text: str
    """Button label text."""
    url: str
    """URL to open when button is clicked."""

Button = Union[ButtonWithData, ButtonWithURL]
"""A button can have either callback data or a URL."""

KeyboardRow = list[Button]
"""A row of buttons in a keyboard."""

Keyboard = list[KeyboardRow]
"""A keyboard is a list of button rows."""

# =============================================================================
# Context Dict Types
# =============================================================================

class UserDict(TypedDict):
    """User information in context."""
    id: str
    """User ID."""
    name: str
    """User display name."""
    platform: str
    """Platform name (telegram, discord, slack, console)."""

class FileDict(TypedDict):
    """File attachment information in context."""
    id: str
    """File ID."""
    name: str
    """File name."""
    mime: str
    """MIME type."""
    size: int
    """File size in bytes."""
    url: str
    """File URL."""

class ContextDict(TypedDict):
    """
    Context dict passed to handlers.

    Contains message/update info and helper methods as callable fields:
    - ctx.reply(text_or_dict, parse_mode="", keyboard=None)
    - ctx.typing()
    - ctx.answer(text="")
    - ctx.download() -> str (base64)
    - ctx.capabilities() -> list[str]
    - ctx.has_capability(name) -> bool
    """
    dest: str
    """Destination/channel ID for replies."""
    message_id: str
    """Message ID."""
    text: str
    """Message text content."""
    command: str
    """Command name (e.g., '/start')."""
    is_callback: bool
    """True if this is a button callback."""
    callback_id: str
    """Callback ID for answering."""
    callback_token: str
    """Callback token (Discord)."""
    callback_data: str
    """Callback data from button press."""
    args: list[str]
    """Command arguments."""
    user: UserDict
    """User information."""
    file: Optional[FileDict]
    """File attachment if present, else None."""

Handler = Callable[[ContextDict], Any]
"""Handler function that receives context dict."""

AuthHandler = Callable[[ContextDict], bool]
"""Auth handler that returns True to allow, False to deny."""

# =============================================================================
# Client Interface (shared by all platforms)
# =============================================================================

class MessagingClient:
    """
    Messaging client with bot framework methods.

    All platforms (telegram, discord, slack, console) return a client
    with this interface from their client() function.
    """

    # Bot Framework
    def command(
        self,
        name: str,
        help_text: str,
        handler: Handler
    ) -> None:
        """
        Register a command handler.

        Parameters:
            name: Command name (e.g., '/start', '/help')
            help_text: Description shown in help
            handler: Function called with context dict
        """
        ...

    def on_callback(
        self,
        handler: Handler,
        prefix: str = ""
    ) -> None:
        """
        Register a callback/button handler.

        Parameters:
            handler: Function called with context dict when button pressed
            prefix: Optional prefix to filter callbacks
        """
        ...

    def on_message(
        self,
        handler: Handler
    ) -> None:
        """
        Register default message handler.

        Parameters:
            handler: Function called for non-command messages
        """
        ...

    def on_file(
        self,
        handler: Handler
    ) -> None:
        """
        Register file attachment handler.

        Parameters:
            handler: Function called when file/photo received
        """
        ...

    def auth(
        self,
        handler: AuthHandler
    ) -> None:
        """
        Register auth handler.

        Parameters:
            handler: Function that returns True to allow access, False to deny
        """
        ...

    def run(self) -> None:
        """
        Start the bot event loop (blocks until stopped).
        """
        ...

    def capabilities(self) -> list[str]:
        """
        Get list of platform capability strings.
        """
        ...

    # Messaging
    def send_message(
        self,
        dest: str,
        message: Message,
        *,
        parse_mode: str = "",
        keyboard: Optional[Keyboard] = None
    ) -> None:
        """
        Send a message to a destination.

        Parameters:
            dest: Destination ID (user/channel)
            message: String or MessageDict with rich content
            parse_mode: Parse mode (e.g., 'markdown', 'html')
            keyboard: Optional button keyboard
        """
        ...

    def send_rich_message(
        self,
        dest: str,
        message: MessageDict
    ) -> None:
        """
        Send a rich message.

        Parameters:
            dest: Destination ID
            message: MessageDict with title, body, color, image, url
        """
        ...

    def edit_message(
        self,
        dest: str,
        message_id: str,
        text: str
    ) -> None:
        """
        Edit a sent message.

        Parameters:
            dest: Destination ID
            message_id: Message ID to edit
            text: New text content
        """
        ...

    def delete_message(
        self,
        dest: str,
        message_id: str
    ) -> None:
        """
        Delete a message.

        Parameters:
            dest: Destination ID
            message_id: Message ID to delete
        """
        ...

    def send_file(
        self,
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
            dest: Destination ID
            source: File path, URL, or base64 data
            filename: Optional filename
            caption: Optional caption
            base64: True if source is base64-encoded data
        """
        ...

    def typing(self, dest: str) -> None:
        """
        Send typing indicator.

        Parameters:
            dest: Destination ID
        """
        ...

    def answer_callback(
        self,
        id: str,
        text: str = "",
        token: str = ""
    ) -> None:
        """
        Acknowledge a button press.

        Parameters:
            id: Callback ID
            text: Optional text to show
            token: Callback token (Discord)
        """
        ...

    def download(self, ref: str) -> str:
        """
        Download a file by ID or URL.

        Parameters:
            ref: File ID or URL

        Returns:
            Base64-encoded file data
        """
        ...

def keyboard(rows: Keyboard) -> Keyboard:
    """
    Build a platform-agnostic button keyboard.

    Parameters:
        rows: List of button rows, each row is a list of button dicts

    Returns:
        The keyboard (pass-through for type checking)

    Example:
        keyboard([
            [{"text": "Yes", "data": "yes"}, {"text": "No", "data": "no"}],
            [{"text": "Help", "url": "https://example.com/help"}]
        ])
    """
    ...
