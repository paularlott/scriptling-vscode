"""
Scriptling Runtime Sync Library - Type stubs for IntelliSense support.

Cross-environment named concurrency primitives for coordinating
concurrent operations across different execution contexts.
"""

from typing import Optional, Any, Callable

class WaitGroup:
    """
    Go-style synchronization primitive.

    WaitGroups allow multiple goroutines to coordinate completion.
    """

    def add(self, delta: int = 1) -> None:
        """
        Add to the wait group counter.

        Parameters:
            delta: Amount to add (default: 1)
        """
        ...

    def done(self) -> None:
        """
        Decrement the wait group counter.
        """
        ...

    def wait(self) -> None:
        """
        Block until counter reaches zero.
        """
        ...

class Queue:
    """
    Thread-safe queue for producer-consumer patterns.

    Queues support blocking put/get operations with optional max size.
    """

    def put(self, item: Any) -> None:
        """
        Add item to queue (blocks if full, respects context timeout).

        Parameters:
            item: Item to add to the queue
        """
        ...

    def get(self) -> Any:
        """
        Remove and return item from queue (blocks if empty, respects context timeout).

        Returns:
            The next item from the queue
        """
        ...

    def size(self) -> int:
        """
        Return number of items in queue.

        Returns:
            Current queue size
        """
        ...

    def close(self) -> None:
        """
        Close the queue.
        """
        ...

class Atomic:
    """
    Atomic integer with lock-free operations.
    """

    def add(self, delta: int = 1) -> int:
        """
        Atomically add delta and return new value.

        Parameters:
            delta: Amount to add (default: 1)

        Returns:
            New value after addition
        """
        ...

    def get(self) -> int:
        """
        Atomically read the value.

        Returns:
            Current value
        """
        ...

    def set(self, value: int) -> None:
        """
        Atomically set the value.

        Parameters:
            value: New value to set
        """
        ...

class Shared:
    """
    Shared variable with thread-safe access.

    Values stored should be treated as immutable. Use set() to replace.
    For atomic read-modify-write, use update() with a callback.
    """

    def get(self) -> Any:
        """
        Get the current value (thread-safe read).

        Returns:
            Current value
        """
        ...

    def set(self, value: Any) -> None:
        """
        Set the value (thread-safe write).

        Parameters:
            value: New value to set
        """
        ...

    def update(self, fn: Callable[[Any], Any]) -> Any:
        """
        Atomically read-modify-write.

        Parameters:
            fn: Function that receives current value and returns new value

        Returns:
            The new value after update
        """
        ...

def WaitGroup(name: str) -> WaitGroup:
    """
    Get or create a named wait group.

    Parameters:
        name: Unique name for the wait group (shared across environments)

    Returns:
        WaitGroup instance

    Example:
        wg = runtime.sync.WaitGroup("tasks")

        def worker(id):
            print(f"Worker {id}")
            wg.done()

        for i in range(10):
            wg.add(1)
            runtime.run(worker, i)

        wg.wait()
    """
    ...

def Queue(name: str, maxsize: int = 0) -> Queue:
    """
    Get or create a named queue.

    Parameters:
        name: Unique name for the queue (shared across environments)
        maxsize: Maximum queue size (0 = unbounded)

    Returns:
        Queue instance

    Example:
        queue = runtime.sync.Queue("jobs", maxsize=100)

        def producer():
            for i in range(10):
                queue.put(i)

        def consumer():
            for i in range(10):
                item = queue.get()
                print(item)

        runtime.run(producer)
        runtime.run(consumer)
    """
    ...

def Atomic(name: str, initial: int = 0) -> Atomic:
    """
    Get or create a named atomic counter.

    Parameters:
        name: Unique name for the counter (shared across environments)
        initial: Initial value (only used if creating new counter)

    Returns:
        Atomic instance

    Example:
        counter = runtime.sync.Atomic("requests", initial=0)
        counter.add(1)      # Atomic increment
        counter.add(-5)     # Atomic add
        counter.set(100)    # Atomic set
        value = counter.get()  # Atomic read
    """
    ...

def Shared(name: str, initial: Any = None) -> Shared:
    """
    Get or create a named shared variable.

    Parameters:
        name: Unique name for the variable (shared across environments)
        initial: Initial value (only used if creating new variable)

    Returns:
        Shared instance

    Note: Values should be treated as immutable. Use set() to replace,
    or update() for atomic read-modify-write operations.

    Example:
        counter = runtime.sync.Shared("counter", 0)

        def increment(current):
            return current + 1

        # Atomic increment using update()
        counter.update(increment)

        # Simple get/set for immutable values
        counter.set(42)
        value = counter.get()
    """
    ...
