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

def client() -> MessagingClient:
    """
    Create a console bot client.

    Returns:
        MessagingClient instance

    Example:
        import scriptling.messaging.console as msg_console

        client = msg_console.client()
        client.run()
    """
    ...

def keyboard(rows: Keyboard) -> Keyboard:
    """Build a console keyboard. See scriptling.messaging.keyboard for details."""
    ...
