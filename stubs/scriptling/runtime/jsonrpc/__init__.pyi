"""
Scriptling Runtime JSON-RPC Library - Type stubs for IntelliSense support.

Concurrent stdio JSON-RPC 2.0 server method and notification registration.
Handlers are referenced by string ("library.function") and run on a fresh,
isolated evaluator per request, matching runtime.http.
"""

from typing import Any, Optional


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


def method(name: str, handler: str) -> None:
    """
    Register a JSON-RPC method handler.

    Parameters:
        name: JSON-RPC method name
        handler: Handler function as "library.function" string

    The handler receives the decoded JSON-RPC params as its single argument
    and returns a JSON-compatible result. Raise an exception or return
    runtime.jsonrpc.error(...) to produce an error response.

    Example:
        import scriptling.runtime as runtime

        runtime.jsonrpc.method("echo", "handlers.echo")
    """
    ...


def notification(name: str, handler: str) -> None:
    """
    Register a JSON-RPC notification handler.

    Parameters:
        name: JSON-RPC notification name
        handler: Handler function as "library.function" string

    Notifications are JSON-RPC requests without an id. The handler receives
    the decoded params but no response is written. Return values are ignored.

    Example:
        import scriptling.runtime as runtime

        runtime.jsonrpc.notification("progress", "handlers.on_progress")
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
