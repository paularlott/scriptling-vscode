"""
Scriptling Runtime MCP Library - Type stubs for IntelliSense support.

Server-side MCP registration: the @mcp.tool, @mcp.resource, @mcp.prompt and
@mcp.skill decorators for statically registered entries, and the
register_request_* functions middleware uses to expose tools, resources and
prompts for the life of a single request (per-user tool sets).
"""

from typing import Any, Callable, Optional

# Request-scoped registration (call from middleware)


def register_request_tool(
    name: str,
    *,
    handler: str,
    description: str = "",
    params: Optional[dict[str, Any]] = None,
    keywords: Optional[list[str]] = None,
    discoverable: bool = False,
    ui: Optional[dict[str, Any]] = None,
    icons: Optional[list[dict[str, Any]]] = None,
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
        ui: Links this tool to a companion UI resource per the MCP Apps
            extension (https://github.com/modelcontextprotocol/ext-apps). A
            dict with an optional "resourceUri" (str, the ui:// resource —
            omit it for an "app"-only action tool with no view of its own,
            such as a form submission only ever called by a view that's
            already open) and optional "visibility" (list of "model" and/or
            "app"; defaults to both). At least one of "resourceUri" or
            "visibility" is required if "ui" is given at all
        icons: Visual identifiers for this tool's tools/list descriptor. Each
            element is a dict with a required "src" (str, an https:// URL or
            data: URI) and optional "mimeType", "sizes" (list of strings like
            "48x48"), and "theme" ("light" or "dark")

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
    *,
    handler: str,
    name: str = "",
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
            "application/json" for dict/list results). Ignored for a
            "ui://" uri — the MCP Apps extension MUSTs that exact
            mimeType, so it's always set for you
        template: Treat uri as a {var} URI template

    Only meaningful while serving MCP over HTTP (in middleware); raises an
    error otherwise.
    """
    ...


def register_request_prompt(
    name: str,
    *,
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
    ui: Optional[dict[str, Any]] = None,
    icons: Optional[list[dict[str, Any]]] = None,
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
        ui: Links this tool to a companion UI resource per the MCP Apps
            extension (https://github.com/modelcontextprotocol/ext-apps). A
            dict with an optional "resourceUri" (str, the ui:// resource —
            omit it for an "app"-only action tool with no view of its own,
            such as a form submission only ever called by a view that's
            already open) and optional "visibility" (list of "model" and/or
            "app"; defaults to both). At least one of "resourceUri" or
            "visibility" is required if "ui" is given at all
        icons: Visual identifiers for this tool's tools/list descriptor. Each
            element is a dict with a required "src" (str, an https:// URL or
            data: URI) and optional "mimeType", "sizes" (list of strings like
            "48x48"), and "theme" ("light" or "dark")

    Example:
        @mcp.tool(
            description="Calculate a mathematical expression",
            params={"expr": "Expression to evaluate (e.g. 2+3*4)"},
        )
        def calc(expr):
            return f"{expr} = {eval(expr)}"

        @mcp.tool(description="Get the sales report",
                  ui={"resourceUri": "ui://sales-dashboard/dashboard.html"},
                  icons=[{"src": "https://example.com/sales.png", "mimeType": "image/png"}])
        def sales_report():
            return {"records": [...]}

        @mcp.tool(description="Add a sale record (called by the dashboard's own form, not the model)",
                  ui={"visibility": ["app"]})
        def add_sale(date, product, amount):
            return {"records": [...]}
    """
    ...


def resource(
    uri: str,
    *,
    name: str = "",
    description: str = "",
    mime_type: str = "",
    template: bool = False,
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    Decorator for MCP resources.

    Decorates a function to register it as an MCP resource (or, with
    template=True, a URI template like "user://docs/{path}"). For a static
    resource the function takes no parameters; for a template its parameters
    are the URI's {var} variables. A string return is the content; a
    dict/list return is JSON encoded. The function runs on every
    resources/read, so content can change between reads.

    Parameters:
        uri: Resource URI, or the URI template when template=True
        name: Human-readable resource name (defaults to the URI)
        description: Resource description
        mime_type: Content type (default "text/plain", or "application/json"
            for dict/list results). Ignored for a "ui://" uri — the MCP Apps
            extension MUSTs that exact mimeType, so it's always set for you
        template: Treat uri as a {var} URI template

    Example:
        @mcp.resource("config://app", name="App config", mime_type="application/json")
        def app_config():
            return {"version": "1.0"}

        @mcp.resource("user://docs/{path}", template=True, mime_type="text/markdown")
        def user_doc(path):
            return "# doc " + path
    """
    ...


def prompt(
    description: str = "",
    *,
    arguments: Optional[list[dict[str, Any]]] = None,
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    Decorator for MCP prompts.

    Decorates a function to register it as an MCP prompt under the function's
    own name. The function's parameters become the prompt's arguments and are
    passed on every prompts/get. A string return is a single user message; a
    dict with a "messages" list of {"role": "user"|"assistant",
    "content": "..."} builds a multi-message prompt.

    Parameters:
        description: Prompt description
        arguments: Argument metadata dicts with "name", "description" and
            "required". Inferred from the function signature when omitted (a
            parameter without a default is required).

    Example:
        @mcp.prompt(description="Summarise a document")
        def summarise(text, style="brief"):
            return "Summarise (style=" + style + "): " + text
    """
    ...


def skill(
    *,
    files: Optional[dict[str, str]] = None,
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    Decorator for MCP skills.

    Decorates a function to register it as an MCP skill (the Agent Skills
    format) under the function's own name. The function takes no parameters
    and returns the SKILL.md content, including its YAML frontmatter; the
    frontmatter's name must match the function name and its description seeds
    the skill's listing. The function runs once when the server starts
    (skills are static content; they do not reload).

    Parameters:
        files: Supporting files mapping file name to content string, served
            alongside SKILL.md as skill://<name>/<file>

    Example:
        @mcp.skill(files={"regions.md": "eu-west: Europe\\n"})
        def region_guide():
            return "---\\nname: region_guide\\ndescription: d\\n---\\n\\nbody"
    """
    ...
