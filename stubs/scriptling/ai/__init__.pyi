"""
Scriptling AI Library - Type stubs for IntelliSense support.

This library provides AI and LLM functions for interacting with multiple
AI provider APIs including OpenAI, Claude, Gemini, Ollama, ZAI, and Mistral.
"""

from typing import Literal, Optional, Any, Callable, Union

# Provider constants
OPENAI: str
CLAUDE: str
GEMINI: str
OLLAMA: str
ZAI: str
MISTRAL: str

# Type aliases
ProviderType = Literal["openai", "claude", "gemini", "ollama", "zai", "mistral"]

class ToolRegistry:
    """
    Registry for AI tool definitions.

    Tools allow AI models to call functions with structured parameters.
    """

    def add(
        self,
        name: str,
        description: str,
        params: dict[str, str],
        handler: Callable[[dict[str, Any]], Any]
    ) -> None:
        """
        Add a tool to the registry.

        Parameters:
            name: Tool name (e.g., "read_file")
            description: Tool description for the AI
            params: Parameter definitions (e.g., {"path": "string", "limit": "integer?"})
                    Use "?" suffix for optional parameters
            handler: Function to execute when tool is called, receives arguments dict
        """
        ...

    def build(self) -> list[dict[str, Any]]:
        """
        Build OpenAI-compatible tool schemas.

        Returns:
            List of tool schema dicts suitable for passing to completion requests
        """
        ...

    def get_handler(self, name: str) -> Callable[[dict[str, Any]], Any]:
        """
        Get tool handler by name.

        Parameters:
            name: Tool name

        Returns:
            Tool handler function
        """
        ...

class ChatStream:
    """Stream object for chat completions."""

    def next(self) -> Optional[dict[str, Any]]:
        """
        Get the next chunk from the stream.

        Returns:
            The next response chunk, or None if the stream is complete
        """
        ...

    def next_timeout(self, timeout: int) -> Optional[dict[str, Any]]:
        """
        Get the next chunk from the stream, but stop waiting after a timeout.

        Parameters:
            timeout: Timeout in seconds

        Returns:
            The next response chunk, {"timed_out": True}, or None if the stream is complete
        """
        ...

    def err(self) -> Optional[str]:
        """
        Get any error from the stream.

        Returns:
            Error message, or None if no error
        """
        ...

class ResponseStream:
    """Stream object for Responses API."""

    def next(self) -> Optional[dict[str, Any]]:
        """
        Get the next event from the response stream.

        Event types:
            - "response.output_text.delta": {type, delta, item_id, output_index, content_index}
            - "response.output_text.done": {type, text, item_id, output_index, content_index}
            - "response.completed": {type, response} where response is the full ResponseObject

        Returns:
            The next event dict, or None if the stream is complete
        """
        ...

class OpenAIClient:
    """AI client for making API calls to supported services."""

    def completion(
        self,
        model: str,
        messages: Union[str, list[dict[str, Any]]],
        *,
        system_prompt: Optional[str] = None,
        tools: Optional[list[dict[str, Any]]] = None,
        temperature: Optional[float] = None,
        top_p: Optional[float] = None,
        max_tokens: Optional[int] = None,
        timeout: Optional[int] = None
    ) -> dict[str, Any]:
        """
        Create a chat completion.

        Parameters:
            model: Model identifier (e.g., "gpt-4", "gpt-3.5-turbo")
            messages: Either a string (user message) or a list of message dicts
            system_prompt: System prompt to use when messages is a string
            tools: List of tool schema dicts from ToolRegistry.build()
            temperature: Sampling temperature (0.0-2.0)
            top_p: Nucleus sampling threshold (0.0-1.0)
            max_tokens: Maximum tokens to generate
            timeout: Request timeout in seconds

        Returns:
            Response dict containing id, choices, usage, etc.
        """
        ...

    def completion_stream(
        self,
        model: str,
        messages: Union[str, list[dict[str, Any]]],
        *,
        system_prompt: Optional[str] = None,
        tools: Optional[list[dict[str, Any]]] = None,
        temperature: Optional[float] = None,
        top_p: Optional[float] = None,
        max_tokens: Optional[int] = None,
        timeout: Optional[int] = None
    ) -> ChatStream:
        """
        Create a streaming chat completion.

        Parameters:
            model: Model identifier (e.g., "gpt-4", "gpt-3.5-turbo")
            messages: Either a string (user message) or a list of message dicts
            system_prompt: System prompt to use when messages is a string
            tools: List of tool schema dicts from ToolRegistry.build()
            temperature: Sampling temperature (0.0-2.0)
            top_p: Nucleus sampling threshold (0.0-1.0)
            max_tokens: Maximum tokens to generate
            timeout: Overall request timeout in seconds

        Returns:
            ChatStream object with a next() method
        """
        ...

    def models(self) -> dict[str, Any]:
        """
        List available models.

        Returns:
            Response dict with object and data fields. data contains the model list.
        """
        ...

    def response_create(
        self,
        model: str,
        input: Union[str, list[Any]],
        *,
        system_prompt: Optional[str] = None,
        background: bool = False
    ) -> dict[str, Any]:
        """
        Create a response using the OpenAI Responses API.

        Parameters:
            model: Model identifier (e.g., "gpt-4o", "gpt-4")
            input: Either a string (user message content) or a list of input items
            system_prompt: System prompt to use when input is a string
            background: If true, runs asynchronously and returns immediately

        Returns:
            Response object with id, status, output, usage, etc.
        """
        ...

    def response_get(self, id: str) -> dict[str, Any]:
        """
        Get a response by ID.

        Parameters:
            id: Response ID

        Returns:
            Response object with id, status, output, usage, etc.
        """
        ...

    def response_cancel(self, id: str) -> dict[str, Any]:
        """
        Cancel a response.

        Parameters:
            id: Response ID to cancel

        Returns:
            Cancelled response object
        """
        ...

    def response_delete(self, id: str) -> None:
        """
        Delete a response by ID.

        Parameters:
            id: Response ID to delete
        """
        ...

    def response_stream(
        self,
        model: str,
        input: Union[str, list[Any]],
        *,
        system_prompt: Optional[str] = None
    ) -> ResponseStream:
        """
        Stream a response using the Responses API.

        Parameters:
            model: Model identifier (e.g., "gpt-4o", "gpt-4")
            input: Either a string (user message content) or a list of input items
            system_prompt: System prompt to use when input is a string

        Returns:
            ResponseStream object with a next() method
        """
        ...

    def response_compact(self, id: str) -> dict[str, Any]:
        """
        Compact a response by removing intermediate reasoning steps.

        Parameters:
            id: Response ID to compact

        Returns:
            Compacted response object with reasoning removed
        """
        ...

    def embedding(
        self,
        model: str,
        input: Union[str, list[str]]
    ) -> dict[str, Any]:
        """
        Create an embedding vector for the given input text(s).

        Parameters:
            model: Model identifier (e.g., "text-embedding-3-small")
            input: Input text(s) to embed - can be a string or list of strings

        Returns:
            Response containing data (list of embeddings), model, and usage
        """
        ...

    def ask(
        self,
        model: str,
        messages: Union[str, list[dict[str, Any]]],
        *,
        system_prompt: Optional[str] = None,
        tools: Optional[list[dict[str, Any]]] = None,
        temperature: Optional[float] = None,
        top_p: Optional[float] = None,
        max_tokens: Optional[int] = None
    ) -> str:
        """
        Quick completion that returns text directly (thinking blocks removed).

        Parameters:
            model: Model identifier (e.g., "gpt-4", "gpt-3.5-turbo")
            messages: Either a string (user message) or a list of message dicts
            system_prompt: System prompt to use when messages is a string
            tools: List of tool schema dicts from ToolRegistry.build()
            temperature: Sampling temperature (0.0-2.0)
            top_p: Nucleus sampling threshold (0.0-1.0)
            max_tokens: Maximum tokens to generate

        Returns:
            The response text with thinking blocks removed
        """
        ...

def Client(
    base_url: str,
    *,
    provider: ProviderType = "openai",
    api_key: str = "",
    max_tokens: int = 0,
    temperature: Optional[float] = None,
    top_p: Optional[float] = None,
    remote_servers: Optional[list[dict[str, str]]] = None
) -> OpenAIClient:
    """
    Create a new AI client.

    Parameters:
        base_url: Base URL of the API (defaults to https://api.openai.com/v1 if empty)
        provider: Provider type. Use constants: OPENAI, CLAUDE, GEMINI, OLLAMA, ZAI, MISTRAL
        api_key: API key for authentication
        max_tokens: Default max_tokens for all requests (Claude defaults to 4096 if not set)
        temperature: Default temperature for all requests (0.0-2.0)
        top_p: Default top_p for all requests (0.0-1.0)
        remote_servers: List of remote MCP server configs, each with:
            - base_url (str, required): URL of the MCP server
            - namespace (str, optional): Namespace prefix for tools
            - bearer_token (str, optional): Bearer token for authentication

    Returns:
        Client instance with methods for API calls

    Example:
        # OpenAI API (default service)
        client = Client("", api_key="sk-...", max_tokens=2048, temperature=0.7)

        # Claude
        client = Client("https://api.anthropic.com", provider=CLAUDE, api_key="sk-ant-...")

        # LM Studio / Local LLM
        client = Client("http://127.0.0.1:1234/v1")
    """
    ...

def extract_thinking(text: str) -> dict[str, Any]:
    """
    Extract thinking blocks from AI response.

    Supports multiple formats:
        - XML-style: <think...</think...
        - XML-style: <thinking>...</thinking>
        - Markdown code blocks: ```thinking\\n...\\n```
        - OpenAI <Thought>...</Thought> style

    Parameters:
        text: The AI response text to process

    Returns:
        Dict containing 'thinking' (list of extracted blocks) and 'content' (cleaned text)
    """
    ...

def text(response: dict[str, Any]) -> str:
    """
    Get text content from response (without thinking blocks).

    Parameters:
        response: Chat completion response from client.completion()

    Returns:
        The response text with thinking blocks removed
    """
    ...

def thinking(response: dict[str, Any]) -> list[str]:
    """
    Get thinking blocks from response.

    Parameters:
        response: Chat completion response from client.completion()

    Returns:
        List of thinking block strings (empty if no thinking blocks)
    """
    ...

def tool_calls(response_or_message: Union[dict[str, Any], list[Any]]) -> list[dict[str, Any]]:
    """
    Extract normalized tool calls from a completion response, message dict, or tool call list.

    Parameters:
        response_or_message: Completion response dict, assistant message dict, or tool call list

    Returns:
        List of normalized tool call dicts with id, type, and function fields
    """
    ...

def execute_tool_calls(
    registry: ToolRegistry,
    tool_calls: list[dict[str, Any]]
) -> list[dict[str, Any]]:
    """
    Execute normalized tool calls using handlers from a ToolRegistry.

    Parameters:
        registry: Tool registry containing handlers
        tool_calls: Tool call dicts, typically from tool_calls(...)

    Returns:
        List of tool result message dicts with role, tool_call_id, and content
    """
    ...

def collect_stream(
    stream: ChatStream,
    *,
    chunk_timeout: Optional[int] = None,
    first_chunk_timeout: Optional[int] = None,
    on_event: Optional[Callable[[dict[str, Any]], Any]] = None
) -> dict[str, Any]:
    """
    Consume a ChatStream and aggregate content, reasoning, tool calls, and finish status.

    Parameters:
        stream: Stream returned by client.completion_stream()
        chunk_timeout: Per-chunk timeout in seconds
        on_event: Optional callback invoked with event dicts while chunks are processed

    Returns:
        Aggregated result dict with content, reasoning, tool_calls, finish_reason, timed_out,
        assistant_message, and error (only present when timed_out is true)
    """
    ...

def tool_round(
    client: OpenAIClient,
    model: str,
    messages: Union[str, list[dict[str, Any]]],
    registry: ToolRegistry,
    *,
    stream: bool = False,
    chunk_timeout: Optional[int] = None,
    on_event: Optional[Callable[[dict[str, Any]], Any]] = None,
    system_prompt: Optional[str] = None,
    temperature: Optional[float] = None,
    top_p: Optional[float] = None,
    max_tokens: Optional[int] = None,
    timeout: Optional[int] = None
) -> dict[str, Any]:
    """
    Run one tool-enabled completion round and return the assistant message, tool calls, and tool results.

    Parameters:
        client: AI client instance
        model: Model identifier
        messages: User message string or message list
        registry: Tool registry containing schemas and handlers
        stream: Use completion_stream() instead of completion()
        chunk_timeout: Per-chunk timeout in seconds for streaming mode
        on_event: Optional callback invoked with event dicts while chunks are processed
        system_prompt: System prompt when messages is a string
        temperature: Sampling temperature
        top_p: Nucleus sampling threshold
        max_tokens: Maximum tokens to generate
        timeout: Overall request timeout in seconds

    Returns:
        Round result dict with assistant_message, content, reasoning, tool_calls, tool_results,
        finish_reason, and timed_out. Non-streaming mode also includes response.
    """
    ...

def estimate_tokens(
    request: Union[str, list[dict[str, Any]], dict[str, Any]],
    response: dict[str, Any]
) -> dict[str, int]:
    """
    Estimate token counts for request messages and response.

    Uses a character-based heuristic (~4 characters per token) to provide
    a fast, reproducible approximation of token counts.

    Parameters:
        request: The messages sent to the AI. Can be:
            - A string (user message)
            - A list of message dicts with "role" and "content" keys
            - A completion request dict with a "messages" key
        response: The completion response from client.completion() or client.response_create()

    Returns:
        Dict with token usage estimates:
            - prompt_tokens (int): Estimated tokens in the request messages
            - completion_tokens (int): Estimated tokens in the response
            - total_tokens (int): Sum of prompt and completion tokens
    """
    ...
