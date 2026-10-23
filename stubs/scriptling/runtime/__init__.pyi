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

    Returned by runtime.background(). In server mode the task is queued until
    the server starts, and the promise resolves once it runs.
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
) -> Promise:
    """
    Register and start a background task.

    Registers a background task and starts it immediately in a goroutine
    (in server mode it is queued until the server starts). Returns a Promise
    object that can be used to wait for completion or get the result.
    Calling background() with the name of a task that is already queued or
    running starts nothing and returns that task's promise.

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
        daemon (bool, default False): when True, the CLI does not wait for this
            task at script exit. By default the CLI waits for outstanding
            background tasks before exiting; pass daemon=True for long-running
            tasks that must not hold the process open. shared and daemon are
            control kwargs and are not passed to the handler.

    Returns:
        Promise object (always; in server mode it resolves once the queued task runs)

    Raises:
        RuntimeError: "background task limit reached: N tasks are queued or
            running, the limit is M" when the interpreter already has as many
            tasks queued or running as its background task limit allows
            (--max-background-tasks, off by default). Under a memory limit each
            live task also counts about 48 KiB against it; if starting the task
            would exceed the memory limit the run is stopped ("memory limit
            exceeded", which a script cannot catch).
        An error if a non-dotted handler is not a defined function ("function
            not found: ...") or an argument is not a transferable type.

    Example:
        def my_task(x, y, operation="add"):
            if operation == "add":
                return x + y
            return x * y

        promise = background("calc", "my_task", 10, 5, operation="multiply")
        result = promise.get()  # Returns 50

        # Long-running task the CLI should not wait for at exit:
        background("poller", "poll_forever", daemon=True)

        # Shared-environment thread over live state:
        state = {"n": 0}
        def worker():
            state["n"] = state["n"] + 1
        background("w", "worker", shared=True).wait()
    """
    ...
