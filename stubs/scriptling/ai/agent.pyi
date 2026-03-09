"""
Scriptling AI Agent Library - Type stubs for IntelliSense support.

This library provides an Agent class for building AI agents that can
use tools and maintain conversation state.

The Agent class is implemented in Scriptling and provides an agentic
loop for tool-calling conversations.
"""

from typing import Optional, Any
from scriptling.ai import OpenAIClient, ToolRegistry

class Message:
    """Represents a message in the conversation."""

    content: Optional[str]
    role: str
    tool_calls: Optional[list[Any]]

class Agent:
    """
    AI Agent with tool-calling capabilities.

    An agent maintains conversation state and can execute tools
    in an agentic loop until a response is ready.
    """

    client: OpenAIClient
    tools: Optional[ToolRegistry]
    system_prompt: str
    model: str
    messages: list[dict[str, Any]]
    tool_schemas: list[dict[str, Any]]

    def __init__(
        self,
        client: OpenAIClient,
        *,
        tools: Optional[ToolRegistry] = None,
        system_prompt: str = "",
        model: str = ""
    ) -> None:
        """
        Initialize an Agent.

        Parameters:
            client: AI client to use for completions
            tools: Optional ToolRegistry with tool definitions
            system_prompt: System prompt for the agent
            model: Model identifier (e.g., "gpt-4")
        """
        ...

    def trigger(
        self,
        message: Union[str, dict[str, Any]],
        *,
        max_iterations: int = 1
    ) -> Message:
        """
        Trigger the agent with a message and run the agentic loop.

        The agent will:
        1. Add the message to the conversation
        2. Call the AI with available tools
        3. Execute any tool calls
        4. Repeat until no more tool calls or max_iterations reached

        Parameters:
            message: Either a string (user message) or a message dict
                     with "role" and "content" keys
            max_iterations: Maximum number of agentic loop iterations. Default: 1

        Returns:
            The final message from the agent (content field has thinking blocks removed)

        Example:
            import scriptling.ai as ai
            from scriptling.ai.agent import Agent

            client = ai.Client("", api_key="sk-...")
            tools = ai.ToolRegistry()
            tools.add("get_time", "Get current time", {}, lambda args: "12:00 PM")

            agent = Agent(client, tools=tools, model="gpt-4")
            response = agent.trigger("What time is it?", max_iterations=3)
            print(response.content)
        """
        ...

    def get_messages(self) -> list[dict[str, Any]]:
        """
        Get the current conversation messages.

        Returns:
            List of message dicts in the conversation
        """
        ...

    def set_messages(self, messages: list[dict[str, Any]]) -> None:
        """
        Set the conversation messages.

        Parameters:
            messages: List of message dicts to set
        """
        ...

# Re-export Union for the type hint
from typing import Union
