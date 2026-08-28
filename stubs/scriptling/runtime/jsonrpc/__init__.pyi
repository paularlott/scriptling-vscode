"""
Scriptling Runtime JSON-RPC Library - Type stubs for IntelliSense support.

Concurrent JSON-RPC 2.0 server method and notification registration.
Handlers are referenced by string ("library.function") and run on a fresh,
isolated evaluator per request, matching runtime.http. The server runs over
stdio with ``scriptling --json-rpc setup.py`` or over HTTP at ``POST /json-rpc``
with ``scriptling --server :8000 --json-rpc setup.py``.
"""

from typing import Any, Optional, Callable, overload, TypeVar

from scriptling.runtime.http import Request

F = TypeVar('F', bound=Callable[..., Any])


class JSONRPCError:
    """
    JSON-RPC error object produced by runtime.jsonrpc.error().

    Return an instance of this from a method handler to emit a JSON-RPC
    error response with a custom code, message, and optional data.

    Attributes:
        code: JSON-RPC error code (e.g. -32602 for invalid params)
        message: Human-readable error message
        data: Optional structured data attached to the error
    """

    code: int
    message: str
    data: Any


@overload
def method(name: str) -> Callable[[F], F]: ...
@overload
def method(name: str, handler: str) -> None: ...
def method(name: str, handler: str = ...) -> Optional[Callable[[F], F]]:
    """
    Register a JSON-RPC method handler, or use as decorator.

    Decorator form::

        @jsonrpc.method("echo")
        def echo(params):
            return params

    Imperative form::

        runtime.jsonrpc.method("echo", "handlers.echo")

    The handler receives the decoded JSON-RPC params as its single argument
    and returns a JSON-compatible result. Return runtime.jsonrpc.error(...)
    to produce an error response.
    """
    ...


@overload
def notification(name: str) -> Callable[[F], F]: ...
@overload
def notification(name: str, handler: str) -> None: ...
def notification(name: str, handler: str = ...) -> Optional[Callable[[F], F]]:
    """
    Register a JSON-RPC notification handler, or use as decorator.

    Decorator form::

        @jsonrpc.notification("progress")
        def on_progress(params):
            pass

    Imperative form::

        runtime.jsonrpc.notification("progress", "handlers.on_progress")

    Notifications are JSON-RPC requests without an id. The handler receives
    the decoded params but no response is written.
    """
    ...


def error(code: int, message: str, data: Any = None) -> JSONRPCError:
    """
    Build a structured JSON-RPC error response.

    Parameters:
        code: JSON-RPC error code (e.g. -32602 for invalid params)
        message: Human-readable error message
        data: Optional structured data attached to the error

    Returns:
        A JSONRPCError instance; return it from a method handler to emit a
        JSON-RPC error response with a custom code.

    Example:
        def divide(params):
            if params["b"] == 0:
                return runtime.jsonrpc.error(-32602, "division by zero", {"field": "b"})
            return params["a"] / params["b"]
    """
    ...


def get_request() -> Optional[Request]:
    """
    Get the HTTP request this call is being served for.

    Returns the same Request object the middleware saw (method, path, headers,
    query, path_params, remote_addr and the context dict the middleware may
    have populated), or None over the stdio transport where there is no HTTP
    request.

    Example:
        def who(params):
            req = runtime.jsonrpc.get_request()
            if req:
                return {"ip": req.remote_addr}
            return {"ip": "stdio"}
    """
    ...


def request_context() -> dict[str, Any]:
    """
    Get the context dict set by the middleware.

    Middleware can write to request.context (e.g. request.context["user"] = name
    after authenticating); this returns a copy of that dict. It is always a
    dict — empty when no middleware ran or set anything — so
    request_context().get("user", "default") is always safe. Each call gets its
    own copy, so writes from the handler are local — with a batch dispatching
    concurrently, one element's writes are never visible to the others.

    Example:
        def who(params):
            user = runtime.jsonrpc.request_context().get("user", "anonymous")
            return {"user": user}
    """
    ...


def transport() -> Optional[str]:
    """
    How the JSON-RPC server is being served: "http", "stdio" or None.

    Lets one setup script work in every mode: over stdio the middleware never
    runs, so anything middleware would gate per user must be handled
    differently there.

    Returns "http" when serving at POST /json-rpc (also from method handlers
    mid-request), "stdio" for the --json-rpc stdio server, and None when the
    script is not being served at all.

    Example:
        if runtime.jsonrpc.transport() == "stdio":
            # No middleware over stdio: treat every caller alike.
            ...
    """
    ...
