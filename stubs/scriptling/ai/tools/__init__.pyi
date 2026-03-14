"""
Scriptling AI Tools Library - Type stubs for IntelliSense support.

Tool schema builder for AI agents. Provides a Registry class for
building OpenAI-compatible tool schemas.
"""

from typing import Callable, Any

class Registry:
    """
    Registry for building tool schemas for AI agents.

    Tools allow AI models to call functions with structured parameters.
    """

    def __init__(self) -> None:
        """
        Create a new tool registry.
        """
        ...

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

        Example:
            registry.add("read_file", "Read a file", {"path": "string"}, read_func)
        """
        ...

    def build(self) -> list[dict[str, Any]]:
        """
        Build OpenAI-compatible tool schemas.

        Returns:
            List of tool schema dicts suitable for passing to AI completion requests

        Example:
            # Build tool schemas for use with Agent (recommended)
            import scriptling.ai as ai
            from scriptling.ai.tools import Registry

            tools = Registry()
            tools.add("read_file", "Read a file", {"path": "string"}, read_func)
            schemas = tools.build()

            # Use with Agent
            bot = agent.Agent(client, tools=tools, model="gpt-4")

            # Or with direct completion calls
            response = client.completion("gpt-4", [{"role": "user", "content": "What time is it?"}], tools=schemas)
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
