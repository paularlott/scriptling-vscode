"""
Scriptling Runtime Library - Type stubs for IntelliSense support.

This library provides runtime utilities for background tasks, HTTP routing,
KV store, concurrency primitives, and sandboxed execution.

Sub-libraries:
  - runtime.http: HTTP server route registration and response helpers
  - runtime.jsonrpc: Concurrent JSON-RPC 2.0 server over stdio or HTTP
  - runtime.kv: Thread-safe key-value store
  - runtime.sync: Concurrency primitives (WaitGroup, Queue, Atomic, Shared)
  - runtime.sandbox: Isolated script execution environments
"""

from typing import Optional, Any, Callable

class Promise:
    """
    Promise object representing an async operation result.

    Returned by runtime.background() in script mode.
    """

    def get(self) -> Any:
        """
        Wait for and return the result.

        Returns:
            The result of the background task
        """
        ...

    def wait(self) -> None:
        """
        Wait for completion and discard the result.
        """
        ...


def start_server(wait: bool = True) -> None:
    """
    Signal the server to start accepting requests.

    Call after all routes and methods are registered. The server collects
    registered routes/methods and begins listening for connections.

    Parameters:
        wait: If True (default), blocks until the server shuts down.
              If False, returns immediately so the script can keep
              running alongside the server.

    Backward compatible: scripts that exit without calling start_server()
    still work — the server starts automatically after the setup script
    finishes.

    Example (blocking, equivalent to Flask app.run()):
        runtime.http.get("/hello", "hello_handler")
        runtime.start_server()

    Example (non-blocking, script stays alive):
        runtime.http.get("/hello", "hello_handler")
        runtime.start_server(wait=False)
        while runtime.server_running():
            yield_now()
    """
    ...


def server_running() -> bool:
    """
    Returns True while the server is running.

    Returns False once the server receives a shutdown signal, or when
    called outside of server mode.

    Typical usage with start_server(wait=False):
        runtime.start_server(wait=False)
        while runtime.server_running():
            yield_now()
    """
    ...


def background(
    name: str,
    handler: str,
    *args: Any,
    **kwargs: Any
) -> Optional[Promise]:
    """
    Register and start a background task.

    Registers a background task and starts it immediately in a goroutine
    (unless in server mode). Returns a Promise object that can be used to
    wait for completion or get the result.

    Parameters:
        name: Unique name for the background task
        handler: Function name to execute (e.g., "my_task" or "lib.function")
        *args: Positional arguments to pass to the function
        **kwargs: Keyword arguments to pass to the function
        shared (bool, default False): when True, run the handler in the caller's
            OWN environment, sharing its live variables. The interpreter lock
            serializes script execution so shared access is safe without locks,
            and arguments are passed live (no transferable restriction). When
            False (default) the handler runs in an isolated, parallel copy.

    Returns:
        Promise object (in script mode) or None (in server mode)

    Example:
        def my_task(x, y, operation="add"):
            if operation == "add":
                return x + y
            return x * y

        promise = background("calc", "my_task", 10, 5, operation="multiply")
        if promise:
            result = promise.get()  # Returns 50

        # Shared-environment thread over live state:
        state = {"n": 0}
        def worker():
            state["n"] = state["n"] + 1
        background("w", "worker", shared=True).wait()
    """
    ...
