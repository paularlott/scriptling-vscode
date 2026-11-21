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
    from scriptling.mcp import MCPClient

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

    Tool calls are checked before they run: a call missing a required
    parameter is answered with a message naming the parameters the tool
    accepts, so the model can correct it. A tool result too large for the
    context budget is shortened to its start and end, and a call repeated
    with the same arguments and the same result is pointed out to the model.

    When a memory store is provided, the agent automatically:
    - Adds memory tools (memory_remember, memory_recall, memory_forget)
    - Appends memory instructions to the system prompt
    - Pre-loads preferences into the system prompt

    When MCP servers are provided, the agent automatically:
    - Registers every server tool under its namespaced name (e.g. a
      "search" tool on a client with namespace="shop" becomes "shop__search"),
      keeping the server's own input schema
    - Lists the servers' skills in the system prompt with namespace-qualified
      skill:// URIs and adds a get_skill tool that fetches them on demand
    """

    client: OpenAIClient
    tools: Optional[ToolRegistry]
    system_prompt: str
    model: str
    messages: list[dict[str, Any]]
    tool_schemas: list[dict[str, Any]]
    memory: Optional["MemoryStore"]
    mcp_servers: list["MCPClient"]
    max_tokens: int
    compaction_threshold: int
    request_timeout: int
    extra_body: Optional[dict[str, Any]]
    stop_reason: str
    """Why the last trigger() stopped: "done" (the model answered),
    "max_iterations" (the tool-call limit was reached and the model was asked
    for a final answer) or "no_response"."""

    def __init__(
        self,
        client: OpenAIClient,
        *,
        tools: Optional[ToolRegistry] = None,
        system_prompt: str = "",
        model: str = "",
        memory: Optional["MemoryStore"] = None,
        mcp_servers: Optional[list["MCPClient"]] = None,
        max_tokens: int = 32000,
        compaction_threshold: int = 80,
        request_timeout: int = 300,
        extra_body: Optional[dict[str, Any]] = None
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
            mcp_servers: Optional list of MCP clients (scriptling.mcp.Client) whose
                    tools and skills the agent can use. Each must be created with a
                    distinct namespace: it prefixes the server's tool names and
                    routes skill URIs back to the server. MCP Apps tools degrade to
                    plain text results (an agent loop has no UI host). Close stdio
                    clients yourself when done; the agent does not own them.
            max_tokens: Token budget for the conversation: set it to the model's
                       context window. When the estimated token count (messages
                       plus tool schemas) reaches the compaction threshold, the
                       older part of the history is summarized and the most
                       recent messages are kept as they are. A single tool result
                       is limited to a quarter of this budget. Default: 32000
            compaction_threshold: Percentage of max_tokens at which auto-compaction
                                 triggers (0-100). Default: 80
            request_timeout: Timeout in seconds for each LLM completion request.
                           LLM calls can be slow, especially with tool-calling
                           loops or large contexts. Default: 300
            extra_body: Optional dict of provider-specific fields to merge into
                       every request body. Default: None

        Example:
            import scriptling.ai as ai
            import scriptling.mcp as mcp
            from scriptling.ai.agent import Agent

            client = ai.Client("", api_key="sk-...")
            shop = mcp.Client("https://shop.example.com/mcp", namespace="shop")

            agent = Agent(client, mcp_servers=[shop], model="gpt-4")
            response = agent.trigger("Find a blue mug", max_iterations=10)
            print(response.content)
            shop.close()
        """
        ...

    def trigger(
        self,
        message: Union[str, dict[str, Any]],
        *,
        max_iterations: int = 25
    ) -> Message:
        """
        Trigger the agent with a message and run the agentic loop.

        The agent will:
        1. Add the message to the conversation
        2. Call the AI with available tools
        3. Execute any tool calls
        4. Repeat until no more tool calls or max_iterations reached

        If max_iterations is reached while the model is still calling tools,
        the agent makes one more request, without tools, asking the model to
        answer from what it has found. stop_reason is then "max_iterations".

        Parameters:
            message: Either a string (user message) or a message dict
                     with "role" and "content" keys
            max_iterations: Maximum number of tool call rounds. Default: 25

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
        - Keeps the tool calls that already ran when a turn is interrupted
          with Esc, fails or stalls, and notes that it was cut short

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
