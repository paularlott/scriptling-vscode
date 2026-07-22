"""
Scriptling Runtime JSON-RPC Library - Type stubs for IntelliSense support.

Concurrent JSON-RPC 2.0 server method and notification registration.
Handlers are referenced by string ("library.function") and run on a fresh,
isolated evaluator per request, matching runtime.http. The server runs over
stdio with ``scriptling --json-rpc setup.py`` or over HTTP at ``POST /json-rpc``
with ``scriptling --server :8000 --json-rpc setup.py``.
"""

from typing import Any, Optional, Callable, overload, TypeVar

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
