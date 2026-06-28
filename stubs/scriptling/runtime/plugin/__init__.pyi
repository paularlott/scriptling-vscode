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

from typing import Any


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


def register_function(name: str, handler: str) -> None:
    """
    Register a function for the plugin server.

    Each registered function is listed in the ``scriptling.handshake`` schema
    and dispatched on a fresh evaluator when a client calls it via
    ``plugin.<name>.<function>()``.

    Parameters:
        name:    Function name exposed to plugin clients.
        handler: Handler as ``"library.function"`` string. The handler
                 receives individual positional arguments decoded from the
                 plugin transport (not a raw params blob). It may return any
                 JSON-serialisable value.

    Must be called before ``runtime.start_server()``. Calling it after the
    server has started has no effect (a warning is emitted to stderr).

    **Callbacks:** If a client passes a callable (function or lambda) as an
    argument, the handler receives it as a callable object and can call it
    normally. Callbacks are only supported over the stdio transport; HTTP
    connections are request/response only.

    Example::

        import scriptling.runtime.plugin as plugin_srv

        plugin_srv.register_function("apply", "handlers.apply")

    In ``handlers.py``::

        def apply(fn, x):
            return fn(x)   # fn is a callback from the client

    Raising an exception from the handler produces an error response on the
    client side.
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


def register_class(handler: str) -> None:
    """
    Register a class exported by the plugin server.

    The exposed class name is taken from the last segment of the handler
    (e.g. ``"mymodule.Config"`` → ``"Config"``). Clients instantiate it with
    ``plugin.myservice.Config(...)``; every instance is held server-side and
    clients receive a remote handle.

    The server handles the full object lifecycle: ``object.new`` (constructor),
    ``object.call_method`` (methods), and ``object.destroy`` (destructor /
    ``__del__``).

    Parameters:
        handler: Class as ``"library.ClassName"`` string.

    Must be called before ``runtime.start_server()``. Calling it after the
    server has started has no effect (a warning is emitted to stderr).

    Example::

        import scriptling.runtime.plugin as plugin_srv

        plugin_srv.register_class("handlers.Config")
    """
    ...
