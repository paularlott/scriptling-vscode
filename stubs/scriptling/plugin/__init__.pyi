"""
Scriptling plugin control library stubs.

Two flavours of plugin live side by side:

* Discovered plugins -- loaded eagerly from --plugin-dir directories or a
  --plugin executable (with arguments supplied by --plugin-arg), and exposed as
  importable ``plugin.<name>`` libraries with auto-generated proxies for
  functions, classes, and constants.
* Runtime-loaded JSON-RPC peers -- spawned on demand as executables or connected
  over HTTP(S) with ``load()`` and driven through ``call_function``. Peers
  loaded with ``scriptling=True`` also register importable ``plugin.*`` proxy
  libraries.

HTTP(S) plugin transport is request/response only: it supports calls, objects,
and batches, but the server cannot initiate callbacks back to the client. Host
callbacks and ``plugin.Logger(ctx)`` require stdio plugins.
"""

from typing import Any, Optional, TypedDict


class BatchCall(TypedDict, total=False):
    """One call entry for batch_call()."""

    name: str
    args: list[Any]
    kwargs: dict[str, Any]


def list() -> list[dict[str, Any]]:
    """Return metadata for all loaded executables (discovered + runtime-loaded).

    Each metadata dict carries the keys documented on :func:`describe`.
    """
    ...


def describe(name: str) -> dict[str, Any]:
    """Return metadata for one loaded plugin.

    Accepts the short name (e.g. ``"widgets"``) or the normalised name
    (``"plugin.widgets"``).

    The returned dict has the keys:

    * ``name`` -- normalised library name (``"plugin.widgets"``).
    * ``version``, ``description`` -- as declared by the plugin.
    * ``transport`` -- ``"json"``.
    * ``capabilities`` -- list of plugin capabilities (currently only
      ``"remote_objects"``).
    * ``scheme`` -- the source scheme this plugin's fetcher serves, e.g.
      ``"knot"`` (present on fetcher plugins; one scheme per plugin, and its
      library attaches automatically when the plugin loads).
    * ``functions``, ``classes``, ``constants`` -- names from the plugin's
      schema.
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
    insecure_skip_tls: bool = False,
    headers: Optional[dict[str, str]] = None,
) -> str:
    """Register a JSON-RPC peer under ``name``.

    ``path`` may be a filesystem executable path, or an ``http://`` /
    ``https://`` JSON-RPC endpoint. Executable peers use newline-delimited
    JSON-RPC over stdio; HTTP peers send one JSON-RPC object or batch per POST.

    With ``scriptling=False`` (the default), :func:`call_function` sends the
    requested function name directly as a raw JSON-RPC method. With
    ``scriptling=True``, the peer must implement the Scriptling plugin
    handshake and ``function.call`` dispatch method. Handshaken peers also
    register an importable ``plugin.*`` proxy library. With
    ``scriptling=False``, the loaded client is helper-only and reachable via
    :func:`call_function`, :func:`describe`, and :func:`list`.

    Parameters:
        name: Library name to register under. Normalised into the plugin.*
            namespace (e.g. "widgets" becomes "plugin.widgets"). Must not
            collide with an existing plugin library name.
        path: Filesystem path to the executable, or an HTTP(S) JSON-RPC
            endpoint such as ``"http://127.0.0.1:8000/json-rpc"``.
        scriptling: If ``True``, perform the plugin protocol handshake,
            register an importable ``plugin.*`` proxy library, and fill
            :func:`describe` / :func:`list` from peer metadata. If ``False``
            (default), the handshake and proxy registration are skipped but
            transport is still reported as ``"json"``.
        args: Command-line arguments passed to the executable (e.g.
            ``["--json-rpc", "./setup.py"]``). Ignored for HTTP endpoints.
        insecure_skip_tls: Skip HTTPS certificate verification for HTTP
            endpoints. Intended for local or trusted self-signed servers.
        headers: Additional HTTP headers sent with every HTTP(S) JSON-RPC
            request, including handshake, calls, and batches.

    Identity is by absolute path for executables and by URL for HTTP endpoints.
    A second ``load()`` of the same path or URL with the same name is a no-op
    (returns the existing client, ignoring
    ``scriptling``/``args``/``insecure_skip_tls``/``headers``). Loading an
    already-loaded peer under a different name, or loading a new peer under a
    name in use, raises an error.

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
