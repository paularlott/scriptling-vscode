"""
Scriptling MCP Library - Type stubs for IntelliSense support.

This library provides MCP (Model Context Protocol) tool interaction functionality
for connecting to MCP servers and executing tools.
"""

from typing import Optional, Any

class MCPClient:
    """MCP client for connecting to remote MCP servers."""

    def tools(self) -> list[dict[str, Any]]:
        """
        List available tools.

        Returns:
            List of tool dicts with name, description, input_schema

        Example:
            tools = client.tools()
            for tool in tools:
                print(tool.name + ": " + tool.description)
        """
        ...

    def call_tool(self, name: str, arguments: dict[str, Any]) -> Any:
        """
        Execute a tool by name with the provided arguments.

        Parameters:
            name: Tool name to execute
            arguments: Tool arguments

        Returns:
            Decoded tool response

        Example:
            result = client.call_tool("search", {"query": "golang"})
            print(result)
        """
        ...

    def refresh_tools(self) -> None:
        """
        Refresh the tool cache.

        Explicitly refreshes the cached list of tools from the server.

        Example:
            client.refresh_tools()
        """
        ...

    def tool_search(
        self,
        query: str,
        *,
        max_results: int = 10
    ) -> list[dict[str, Any]]:
        """
        Search for tools using the tool_search MCP tool.

        Useful when the server has many tools registered via a discovery registry.

        Parameters:
            query: Search query for tool names, descriptions, and keywords
            max_results: Maximum number of results (default: 10)

        Returns:
            List of matching tool dicts

        Example:
            # Get up to 10 weather-related tools (default)
            results = client.tool_search("weather")

            # Get up to 5 database tools
            results = client.tool_search("database", max_results=5)
        """
        ...

    def execute_discovered(
        self,
        name: str,
        arguments: dict[str, Any]
    ) -> Any:
        """
        Execute a tool by name using the execute_tool MCP tool.

        This is the only way to call tools that were discovered via tool_search.

        Parameters:
            name: Tool name to execute
            arguments: Tool arguments

        Returns:
            Tool response

        Example:
            result = client.execute_discovered("custom_tool", {"param": "value"})
        """
        ...

    def call_tools_parallel(
        self,
        calls: list[dict[str, Any]]
    ) -> list[dict[str, Any]]:
        """
        Execute multiple tools concurrently.

        Executes multiple tools in parallel and returns results in the same order
        as the input list.

        Parameters:
            calls: List of dicts with "name" (str) and "arguments" (dict) keys

        Returns:
            List of dicts with "name", "result", and "error" keys.
            "error" is an empty string on success.

        Example:
            results = client.call_tools_parallel([
                {"name": "search", "arguments": {"query": "golang"}},
                {"name": "weather", "arguments": {"city": "London"}},
            ])
            for r in results:
                if r["error"]:
                    print("Error:", r["error"])
                else:
                    print(r["name"], r["result"])
        """
        ...

    def execute_discovered_parallel(
        self,
        calls: list[dict[str, Any]]
    ) -> list[dict[str, Any]]:
        """
        Execute multiple discovered tools concurrently.

        Executes multiple discovered tools (found via tool_search) in parallel
        and returns results in the same order as the input list.

        Parameters:
            calls: List of dicts with "name" (str) and "arguments" (dict) keys

        Returns:
            List of dicts with "name", "result", and "error" keys.
            "error" is an empty string on success.

        Example:
            results = client.execute_discovered_parallel([
                {"name": "tool_a", "arguments": {"x": 1}},
                {"name": "tool_b", "arguments": {"y": 2}},
            ])
            for r in results:
                if r["error"]:
                    print("Error:", r["error"])
                else:
                    print(r["name"], r["result"])
        """
        ...

    def list_resources(self) -> list[dict[str, Any]]:
        """
        List static resources exposed by the server.

        Returns:
            List of resource dicts with uri, name, description, mimeType

        Example:
            for res in client.list_resources():
                print(res["uri"], res["name"])
        """
        ...

    def list_resource_templates(self) -> list[dict[str, Any]]:
        """
        List resource templates exposed by the server.

        Resource templates have a {var} URI placeholder the client expands
        before reading with read_resource().

        Returns:
            List of dicts with uriTemplate, name, description, mimeType

        Example:
            for t in client.list_resource_templates():
                print(t["uriTemplate"], t["name"])
        """
        ...

    def read_resource(self, uri: str) -> Any:
        """
        Read a resource by URI (static or expanded from a template).

        Parameters:
            uri: The resource URI to read

        Returns:
            A content dict (uri, mimeType, text|blob), or a list of them.
            text is parsed JSON when valid, else a plain string.

        Example:
            data = client.read_resource("config://app")
            print(data["text"])
        """
        ...

    def list_prompts(self) -> list[dict[str, Any]]:
        """
        List prompts exposed by the server.

        Returns:
            List of prompt dicts with name, description, and arguments
            (each argument: name, description, required)

        Example:
            for p in client.list_prompts():
                print(p["name"], p["description"])
        """
        ...

    def get_prompt(self, name: str, arguments: dict[str, Any]) -> dict[str, Any]:
        """
        Render a prompt by name into messages for the model.

        Prompt arguments are always strings; non-string values are coerced.

        Parameters:
            name: Prompt name
            arguments: Argument values

        Returns:
            dict with "description" and "messages" (a list of
            {"role": ..., "content": ...})

        Example:
            out = client.get_prompt("write_script", {"task": "greet a user"})
            for m in out["messages"]:
                print(m["role"], m["content"])
        """
        ...

    def close(self) -> None:
        """
        Close the client and release its transport.

        For a stdio client this shuts down the launched server subprocess;
        for an HTTP client it is a no-op. Safe to call more than once.

        Example:
            client.close()
        """
        ...

def Client(
    target: str,
    *,
    namespace: str = "",
    bearer_token: str = "",
    args: Optional[list[str]] = None
) -> MCPClient:
    """
    Create a new MCP client, over HTTP or stdio.

    The transport is chosen from `target`: an "http://" or "https://" URL
    connects over HTTP; any other value is treated as a local executable that
    is launched as a stdio MCP server subprocess.

    Parameters:
        target: HTTP(S) URL of the server, or path/command of a stdio server
        namespace: Namespace prefixed to tool names (e.g. "t1" exposes
                   "search" as "t1__search")
        bearer_token: Bearer token for authentication (HTTP only)
        args: Command-line arguments for the stdio server (stdio only)

    Passing `args` with an HTTP URL, or `bearer_token` with a command, raises
    an error.

    Returns:
        Client instance with methods for interacting with the server. For
        stdio clients, call close() when done to shut the subprocess down.

    Example:
        # HTTP server
        client = Client("https://api.example.com/mcp",
                       namespace="scriptling",
                       bearer_token="secret")

        # stdio server (a local executable)
        client = Client("/usr/local/bin/thebinary", args=["--server"], namespace="t1")

        # Scriptling itself can be a stdio MCP server
        client = Client("scriptling", args=["--mcp-exec-script"], namespace="local")

        tools = client.tools()
        for tool in tools:
            print(tool.name)
        client.close()
    """
    ...

def decode_response(response: dict[str, Any]) -> Any:
    """
    Decode an MCP tool response.

    Decodes a raw MCP tool response into scriptling objects.

    Parameters:
        response: Raw tool response dict

    Returns:
        Decoded response (parsed JSON or string)

    Example:
        decoded = decode_response(raw_response)
    """
    ...
