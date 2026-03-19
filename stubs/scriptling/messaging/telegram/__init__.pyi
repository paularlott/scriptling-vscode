"""
Scriptling Telegram Messaging - Type stubs for IntelliSense support.

Provides a bot client for the Telegram messaging platform.

Setup:
    1. Message @BotFather on Telegram and send /newbot
    2. Copy the token provided

Usage:
    export TELEGRAM_TOKEN="your-bot-token"

    import scriptling.messaging.telegram as telegram
    client = telegram.client(os.environ["TELEGRAM_TOKEN"])
    client.command("/start", "Start the bot", handle_start)
    client.run()
"""

from typing import Optional
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

def client(
    token: str,
    *,
    allowed_users: Optional[list[str]] = None
) -> MessagingClient:
    """
    Create a Telegram bot client.

    Parameters:
        token: Bot token from @BotFather
        allowed_users: Optional list of user IDs allowed to use the bot

    Returns:
        MessagingClient instance

    Example:
        client = telegram.client("123456:ABC-DEF...")
        client = telegram.client(token, allowed_users=["123456789"])
    """
    ...

def keyboard(rows: Keyboard) -> Keyboard:
    """Build a Telegram keyboard. See scriptling.messaging.keyboard for details."""
    ...
