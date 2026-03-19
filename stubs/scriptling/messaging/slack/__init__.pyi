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
    bot_token: str,
    app_token: str,
    *,
    allowed_users: Optional[list[str]] = None
) -> MessagingClient:
    """
    Create a Slack bot client.

    Parameters:
        bot_token: Bot User OAuth Token (xoxb-...)
        app_token: App-Level Token (xapp-...)
        allowed_users: Optional list of user IDs allowed to use the bot

    Returns:
        MessagingClient instance

    Example:
        client = slack.client("xoxb-...", "xapp-...")
        client = slack.client(bot_token, app_token, allowed_users=["U12345678"])
    """
    ...

def keyboard(rows: Keyboard) -> Keyboard:
    """Build a Slack keyboard. See scriptling.messaging.keyboard for details."""
    ...
