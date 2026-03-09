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

def Client(
    base_url: str,
    *,
    namespace: str = "",
    bearer_token: str = ""
) -> MCPClient:
    """
    Create a new MCP client.

    Creates a new MCP client for connecting to a remote MCP server.

    Parameters:
        base_url: URL of the MCP server
        namespace: Namespace for tool names (e.g., "scriptling" makes tools
                   available as "scriptling/tool_name")
        bearer_token: Bearer token for authentication

    Returns:
        Client instance with methods for interacting with the server

    Example:
        # Without namespace or auth
        client = Client("https://api.example.com/mcp")

        # With namespace only
        client = Client("https://api.example.com/mcp", namespace="scriptling")

        # With bearer token only
        client = Client("https://api.example.com/mcp", bearer_token="secret")

        # With both namespace and bearer token
        client = Client("https://api.example.com/mcp",
                       namespace="scriptling",
                       bearer_token="secret")

        tools = client.tools()
        for tool in tools:
            print(tool.name)
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
