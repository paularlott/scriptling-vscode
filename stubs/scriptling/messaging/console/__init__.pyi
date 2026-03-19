"""
Scriptling Console Messaging - Type stubs for IntelliSense support.

Provides a local TUI console bot for testing handlers without network.
Useful for testing before deploying to Telegram/Discord/Slack.

Usage:
    import scriptling.console as console
    import scriptling.messaging.console as messaging_console

    con = console.Console()
    client = messaging_console.client(con)
    client.command("/start", "Start the bot", handle_start)
    client.run()
"""

from typing import TYPE_CHECKING
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

if TYPE_CHECKING:
    from scriptling.console import Console

def client(console: "Console") -> MessagingClient:
    """
    Create a console bot client.

    Parameters:
        console: Console instance from scriptling.console

    Returns:
        MessagingClient instance

    Example:
        import scriptling.console as console
        import scriptling.messaging.console as msg_console

        con = console.Console()
        client = msg_console.client(con)
        client.run()
    """
    ...

def keyboard(rows: Keyboard) -> Keyboard:
    """Build a console keyboard. See scriptling.messaging.keyboard for details."""
    ...
