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
    Create a Discord bot client.

    Parameters:
        token: Bot token from Discord Developer Portal
        allowed_users: Optional list of user IDs allowed to use the bot

    Returns:
        MessagingClient instance

    Example:
        client = discord.client("MTk4NjIyNDgzNDc...")
        client = discord.client(token, allowed_users=["123456789012345678"])
    """
    ...

def keyboard(rows: Keyboard) -> Keyboard:
    """Build a Discord keyboard. See scriptling.messaging.keyboard for details."""
    ...
