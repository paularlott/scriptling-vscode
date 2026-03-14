"""
Scriptling Runtime Library - Type stubs for IntelliSense support.

This library provides runtime utilities for background tasks, HTTP routing,
KV store, concurrency primitives, and sandboxed execution.

Sub-libraries:
  - runtime.http: HTTP server route registration and response helpers
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
    """
    ...
