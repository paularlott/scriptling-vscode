"""
Scriptling Runtime MCP Library - Type stubs for IntelliSense support.

Server-side MCP registration: the @mcp.tool decorator for statically
registered tools, and the register_request_* functions middleware uses to
expose tools, resources and prompts for the life of a single request
(per-user tool sets).
"""

from typing import Any, Callable, Optional

# Request-scoped registration (call from middleware)


def register_request_tool(
    name: str,
    handler: str,
    description: str = "",
    params: Optional[dict[str, Any]] = None,
    keywords: Optional[list[str]] = None,
    discoverable: bool = False,
) -> None:
    """
    Register an MCP tool for this request.

    Call from middleware to expose a tool for the life of the request being
    served: tools/list shows it and tools/call runs it, but only for requests
    whose middleware registered it — which makes per-user tool sets possible.
    Authorization is re-evaluated on every MCP message, since the middleware
    runs per request.

    Parameters:
        name: Tool name (static tools win on a name collision)
        handler: Handler function as "module.function", called with the tool
            arguments as keyword parameters on a fresh interpreter
        description: Tool description shown to the AI
        params: Parameter metadata keyed by name; each value is a string
            (description) or a dict with "type", "description" and "required"
        keywords: Keywords for tool search/discovery
        discoverable: Hide from tools/list, expose via search only

    Only meaningful while serving MCP over HTTP (in middleware); raises an
    error otherwise. Inside the handler, mcp.tool.get_string() reads arguments
    and mcp.tool.request_context() reads the middleware's context.

    Example:
        def auth(request):
            user = identify(request)
            if user == "admin":
                mcp.register_request_tool(
                    "restart_service",
                    handler="admintools.restart",
                    description="Restart a service",
                    params={"service": {"type": "string", "description": "Service to restart", "required": True}},
                )
            return None
    """
    ...


def register_request_resource(
    uri: str,
    handler: str,
    name: str,
    description: str = "",
    mime_type: str = "",
    template: bool = False,
) -> None:
    """
    Register an MCP resource for this request.

    Call from middleware to expose a resource (or, with template=True, a URI
    template like "user://docs/{path}") for the life of the request being
    served. resources/list and resources/templates/list show it;
    resources/read runs the handler. Static resources win on a URI collision.

    Parameters:
        uri: Resource URI, or the URI template when template=True
        handler: Handler function as "module.function", called with the
            template variables as keyword parameters (and "__uri" holding the
            full URI); a string return is the content, a dict/list is JSON
            encoded
        name: Human-readable resource name
        description: Resource description
        mime_type: Content type (default "text/plain", or
            "application/json" for dict/list results)
        template: Treat uri as a {var} URI template

    Only meaningful while serving MCP over HTTP (in middleware); raises an
    error otherwise.
    """
    ...


def register_request_prompt(
    name: str,
    handler: str,
    description: str = "",
    arguments: Optional[list[dict[str, Any]]] = None,
) -> None:
    """
    Register an MCP prompt for this request.

    Call from middleware to expose a prompt for the life of the request being
    served. prompts/list shows it; prompts/get renders it by running the
    handler with the prompt arguments as keyword parameters. Static prompts
    win on a name collision.

    Parameters:
        name: Prompt name
        handler: Handler function as "module.function". A string return is a
            single user message; a dict with a "messages" list of
            {"role": "user"|"assistant", "content": "..."} builds a
            multi-message prompt
        description: Prompt description
        arguments: Argument metadata dicts with "name", "description" and
            "required"

    Only meaningful while serving MCP over HTTP (in middleware); raises an
    error otherwise.
    """
    ...


def transport() -> Optional[str]:
    """
    How the MCP server is being served: "http", "stdio" or None.

    Lets one setup script work in every mode: over stdio the middleware never
    runs, so registrations that middleware would gate per user must be made
    unconditionally instead.

    Returns "http" when serving over HTTP (also from middleware and tool
    handlers mid-request), "stdio" for the MCP stdio server, and None when
    the script is not being served at all.

    Example:
        if mcp.transport() == "stdio":
            # No middleware over stdio: expose the extra tools to everyone.
            ...
    """
    ...


# Static registration (decorator)


def tool(
    description: str,
    params: Optional[dict[str, Any]] = None,
    keywords: Optional[list[str]] = None,
    discoverable: bool = False,
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    Decorator for MCP tools.

    Decorates a function to register it as an MCP tool. The function's
    parameters become the tool's input schema; the return value becomes the
    tool response.

    Parameters:
        description: Tool description shown to the AI
        params: Parameter metadata keyed by name. Each value is either a
            string (the description; type inferred from default or defaults
            to "string") or a dict with keys "type", "description", and
            optional "required"
        keywords: Keywords for tool search/discovery
        discoverable: If True, tool is hidden from tools/list and only
            available via search

    Example:
        @mcp.tool(
            description="Calculate a mathematical expression",
            params={"expr": "Expression to evaluate (e.g. 2+3*4)"},
        )
        def calc(expr):
            return f"{expr} = {eval(expr)}"
    """
    ...
