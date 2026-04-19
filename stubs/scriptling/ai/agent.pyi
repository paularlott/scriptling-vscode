"""
Scriptling AI Agent Library - Type stubs for IntelliSense support.

This library provides an Agent class for building AI agents that can
use tools and maintain conversation state.

The Agent class is implemented in Scriptling and provides an agentic
loop for tool-calling conversations.
"""

from typing import Optional, Any, TYPE_CHECKING, Union
from scriptling.ai import OpenAIClient, ToolRegistry

if TYPE_CHECKING:
    from scriptling.ai.memory import MemoryStore

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

    When a memory store is provided, the agent automatically:
    - Adds memory tools (memory_remember, memory_recall, memory_forget)
    - Appends memory instructions to the system prompt
    - Pre-loads preferences into the system prompt
    """

    client: OpenAIClient
    tools: Optional[ToolRegistry]
    system_prompt: str
    model: str
    messages: list[dict[str, Any]]
    tool_schemas: list[dict[str, Any]]
    memory: Optional["MemoryStore"]
    max_tokens: int
    compaction_threshold: int
    request_timeout: int

    def __init__(
        self,
        client: OpenAIClient,
        *,
        tools: Optional[ToolRegistry] = None,
        system_prompt: str = "",
        model: str = "",
        memory: Optional["MemoryStore"] = None,
        max_tokens: int = 32000,
        compaction_threshold: int = 80,
        request_timeout: int = 300
    ) -> None:
        """
        Initialize an Agent.

        Parameters:
            client: AI client to use for completions
            tools: Optional ToolRegistry with tool definitions
            system_prompt: System prompt for the agent
            model: Model identifier (e.g., "gpt-4")
            memory: Optional MemoryStore for persistent memory across conversations.
                    When provided, memory tools are automatically added and the
                    system prompt is augmented with memory instructions.
            max_tokens: Maximum token budget for the conversation. When the estimated
                       token count reaches the compaction threshold, the conversation
                       history is automatically summarized. Default: 32000
            compaction_threshold: Percentage of max_tokens at which auto-compaction
                                 triggers (0-100). Default: 80
            request_timeout: Timeout in seconds for each LLM completion request.
                           LLM calls can be slow, especially with tool-calling
                           loops or large contexts. Default: 300
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

    def interact(self, max_iterations: int = 25) -> None:
        """
        Start an interactive terminal session using the TUI console.

        Requires scriptling.console to be registered. After importing
        scriptling.ai.agent.interact, this method becomes available.

        During each turn:
        - Streams reasoning and assistant text into the main panel as it arrives
        - Keeps the spinner running until the turn is complete
        - Shows tool call and result messages with status and preview
        - Uses ai.collect_stream() for streaming with configurable timeouts
        - Preserves conversation history between turns

        Built-in commands: /clear, /model, /history, /exit

        Parameters:
            max_iterations: Maximum tool call rounds per message. Default: 25
        """
        ...

    def set_messages(self, messages: list[dict[str, Any]]) -> None:
        """
        Set the conversation messages.

        Parameters:
            messages: List of message dicts to set
        """
        ...
