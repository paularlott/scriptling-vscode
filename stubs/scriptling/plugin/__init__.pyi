"""
Scriptling plugin control library stubs.

Two flavours of plugin live side by side:

* Discovered plugins -- loaded eagerly from --plugin-dir directories and
  exposed as importable ``plugin.<name>`` libraries with auto-generated
  proxies for functions, classes, and constants.
* Runtime-loaded executables -- spawned on demand with ``load()`` and driven
  through ``call_function``. No proxy library is generated.
"""

from typing import Any, Optional, TypedDict


class BatchCall(TypedDict, total=False):
    """One call entry for batch_call()."""

    name: str
    args: list[Any]
    kwargs: dict[str, Any]


def list() -> list[dict[str, Any]]:
    """Return metadata for all loaded executables (discovered + runtime-loaded)."""
    ...


def describe(name: str) -> dict[str, Any]:
    """Return metadata for one loaded plugin.

    Accepts the short name (e.g. ``"widgets"``) or the normalised name
    (``"plugin.widgets"``).
    """
    ...


def call_function(library: str, name: str, *args: Any, **kwargs: Any) -> Any:
    """Call a function on a loaded executable.

    Dispatch is automatic based on how the executable was loaded:

    * **Plugin protocol** (``scriptling=True``): sends ``function.call`` with
      typed plugin transport values. Arguments and return values preserve
      int/float distinction.
    * **Raw JSON-RPC** (``scriptling=False``, the default): sends the function
      name directly as the JSON-RPC method. If kwargs are present they become
      the ``params`` object (positional args are ignored); otherwise a single
      positional arg becomes ``params`` directly (any type — dict, list,
      string, number, etc.); multiple positional args become a ``params``
      array. Return values are raw JSON (numbers come back as floats).

    Parameters:
        library: Plugin library name -- short (``"widgets"``) or normalised
            (``"plugin.widgets"``).
        name: Function name within the plugin, or the raw JSON-RPC method name
            for non-plugin peers.
    """
    ...


def batch_call(library: str, calls: list[BatchCall]) -> list[Any]:
    """Call multiple functions on one executable in a JSON-RPC batch.

    Each call entry must include ``name`` and may include ``args`` and
    ``kwargs``:

        ``{"name": "add", "args": [1, 2]}``
        ``{"name": "search", "kwargs": {"query": "scriptling"}}``

    For ``scriptling=False`` clients, each ``name`` is sent directly as the
    raw JSON-RPC method. For ``scriptling=True`` clients, each entry is sent as
    a typed plugin ``function.call`` request. Results are returned in the same
    order as ``calls``. Callback arguments are not supported.
    """
    ...


def call_method(obj: Any, name: str, *args: Any, **kwargs: Any) -> Any:
    """Call a method on a remote plugin object."""
    ...


def _new_object(library: str, class_name: str, *args: Any, **kwargs: Any) -> Any:
    """Internal: construct a remote plugin object. Used by generated wrappers."""
    ...


def release(obj: Any) -> None:
    """Explicitly release a remote plugin object."""
    ...


def load(
    name: str,
    path: str,
    *,
    scriptling: bool = False,
    args: Optional[list[str]] = None,
) -> str:
    """Spawn an executable and register it under ``name``.

    With ``scriptling=False`` (the default), :func:`call_function` sends the
    requested function name directly as a raw JSON-RPC method. With
    ``scriptling=True``, the executable must implement the Scriptling plugin
    handshake and ``function.call`` dispatch method. The loaded client is
    reachable via :func:`call_function`, :func:`describe`, and :func:`list`;
    no proxy library is generated.

    Parameters:
        name: Library name to register under. Normalised into the plugin.*
            namespace (e.g. "widgets" becomes "plugin.widgets"). Must not
            collide with an existing plugin library name.
        path: Filesystem path to the executable.
        scriptling: If ``True``, perform the plugin protocol handshake so
            :func:`describe` / :func:`list` report version and schema from the
            executable. If ``False`` (default), the handshake is skipped but
            transport is still reported as ``"json"``.
        args: Command-line arguments passed to the executable (e.g.
            ``["--json-rpc", "./setup.py"]``).

    Identity is by absolute path. A second ``load()`` of the same path with
    the same name is a no-op (returns the existing client, ignoring
    ``scriptling``/``args``). Loading an already-loaded path under a different
    name, or loading a new path under a name in use, raises an error.

    Returns:
        The normalised library name (e.g. "plugin.widgets"). The short form
        ("widgets") may be used with :func:`call_function`, :func:`describe`,
        and :func:`unload`.
    """
    ...


def unload(name: str) -> None:
    """Close a loaded executable and remove it from the registry.

    Accepts the short name (e.g. ``"widgets"``) or the normalised name
    (``"plugin.widgets"``).
    """
    ...
