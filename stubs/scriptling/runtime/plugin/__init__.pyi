"""
Scriptling Runtime Plugin Library - Type stubs for IntelliSense support.

Declare a script as a Scriptling plugin server. When ``runtime.start_server()``
is called the CLI switches from the plain JSON-RPC loop to the full
Scriptling plugin protocol (``scriptling.handshake``, ``function.call``, etc.)
so that clients can load the script with ``scriptling=True`` and receive
auto-generated proxy libraries.

Available in the **agent variant** of scriptling only (registered alongside
``scriptling.ai.agent``). Not exposed in the general CLI runtime.

Typical setup script::

    import scriptling.runtime.plugin as plugin_srv
    import scriptling.runtime as runtime

    plugin_srv.serve("myservice", "1.0", "My service")
    plugin_srv.register_function("greet", "handlers.greet")
    plugin_srv.register_function("compute", "handlers.compute")
    plugin_srv.register_constant("VERSION", "1.0.0")
    plugin_srv.register_class("handlers.Config")

    runtime.start_server()

Or via the parent runtime dict::

    import scriptling.runtime as runtime

    runtime.plugin.serve("myservice", "1.0", "My service")
    runtime.plugin.register_function("greet", "handlers.greet")
    runtime.start_server()
"""

from typing import Any, Callable, overload, TypeVar, Type

F = TypeVar('F', bound=Callable[..., Any])
T = TypeVar('T')


def serve(name: str, version: str = "", description: str = "") -> None:
    """
    Declare this script as a Scriptling plugin server.

    When ``runtime.start_server()`` is called in stdio mode the server serves
    the full Scriptling plugin protocol instead of the plain JSON-RPC loop.
    Clients load the script with ``scriptling=True`` and receive an importable
    ``plugin.<name>`` proxy library with generated wrappers for every
    registered function, constant, and class.

    Must be called before ``runtime.start_server()``. Calling it after the
    server has started has no effect (a warning is emitted to stderr).

    Parameters:
        name:        Library name (e.g. ``"myservice"``). Clients import it as
                     ``plugin.myservice``.
        version:     Optional version string (e.g. ``"1.0.0"``).
        description: Optional human-readable description surfaced in plugin
                     metadata (``scriptling.plugin.info()``).

    Example::

        import scriptling.runtime.plugin as plugin_srv

        plugin_srv.serve("calculator", "1.0", "Basic arithmetic operations")
    """
    ...


@overload
def register_function(name: str) -> Callable[[F], F]: ...
@overload
def register_function(fn: F) -> F: ...
@overload
def register_function(name: str, handler: str) -> None: ...
def register_function(name: Any, handler: Any = ...) -> Any:
    """
    Register a function for the plugin server, or use as decorator.

    Three forms:

    Named decorator::

        @plugin.register_function("add")
        def add(a, b):
            return a + b

    Bare decorator (uses the function's own name)::

        @plugin.register_function
        def greet(name):
            return "hello " + name

    Imperative::

        plugin.register_function("add", "handlers.add")

    The handler receives individual positional arguments decoded from the
    plugin transport. Callbacks are supported over stdio only.
    """
    ...


def register_constant(name: str, value: Any) -> None:
    """
    Register a constant exported by the plugin server.

    Constants are included in the ``scriptling.handshake`` schema and sent to
    clients as part of the plugin library. Clients can read them as plain
    attributes: ``plugin.myservice.VERSION``.

    Parameters:
        name:  Constant name exposed to plugin clients.
        value: Any JSON-serialisable value — ``bool``, ``int``, ``float``,
               ``str``, ``list``, ``dict``, or ``None``.

    Must be called before ``runtime.start_server()``. Calling it after the
    server has started has no effect (a warning is emitted to stderr).

    Example::

        import scriptling.runtime.plugin as plugin_srv

        plugin_srv.register_constant("VERSION", "1.0.0")
        plugin_srv.register_constant("MAX_RETRIES", 5)
    """
    ...


@overload
def register_class(cls: Type[T]) -> Type[T]: ...
@overload
def register_class(handler: str) -> None: ...
def register_class(handler: Any) -> Any:
    """
    Register a class exported by the plugin server, or use as bare decorator.

    Decorator form::

        @plugin.register_class
        class Config:
            def __init__(self, prefix):
                self.prefix = prefix

    Imperative form::

        plugin.register_class("handlers.Config")

    The exposed class name is taken from the class name (decorator) or the
    last segment of the handler ref (imperative). The server handles the
    full object lifecycle (new, call_method, destroy).
    """
    ...
