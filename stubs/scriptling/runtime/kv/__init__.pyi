"""
Scriptling Runtime KV Library - Type stubs for IntelliSense support.

Thread-safe key-value store for sharing state across requests.
Use kv.default for the system store or kv.open() for named stores.

Note: By default the KV store is in-memory. To persist data, configure a
storage path when starting the server. Keys without a TTL persist indefinitely.
Use TTLs and periodic cleanup to avoid unbounded storage growth.
"""

from typing import Any

class Storage:
    """
    KV store object with methods for key-value operations.

    Obtain a Storage instance via kv.default or kv.open().
    """

    def set(self, key: str, value: Any, ttl: int = 0) -> None:
        """
        Store a value with optional TTL in seconds.

        Parameters:
            key: The key to store the value under
            value: The value to store (string, int, float, bool, list, dict)
            ttl: Time-to-live in seconds. 0 means no expiration.

        Example:
            kv.default.set("api_key", "secret123")
            kv.default.set("session:abc", {"user": "bob"}, ttl=3600)
        """
        ...

    def get(self, key: str, default: Any = None) -> Any:
        """
        Retrieve a value by key.

        Parameters:
            key: The key to retrieve
            default: Value to return if key doesn't exist (default: None)

        Returns:
            The stored value, or the default if not found

        Example:
            value = kv.default.get("api_key")
            count = kv.default.get("counter", default=0)
        """
        ...

    def incr(self, key: str, delta: int = 1) -> int:
        """
        Atomically increment an integer value, returns new value.

        If the key does not exist it is initialised to 0 before incrementing.

        Parameters:
            key: The key to increment
            delta: Amount to add (default: 1)

        Returns:
            New integer value after increment

        Example:
            kv.default.set("hits", 0)
            count = kv.default.incr("hits")      # 1
            count = kv.default.incr("hits", 5)   # 6
        """
        ...

    def delete(self, key: str) -> None:
        """
        Remove a key from the store.

        Parameters:
            key: The key to delete

        Example:
            kv.default.delete("session:abc")
        """
        ...

    def exists(self, key: str) -> bool:
        """
        Check if a key exists and is not expired.

        Parameters:
            key: The key to check

        Returns:
            True if key exists and is not expired

        Example:
            if kv.default.exists("config"):
                config = kv.default.get("config")
        """
        ...

    def ttl(self, key: str) -> int:
        """
        Get remaining TTL in seconds.

        Parameters:
            key: The key to check

        Returns:
            Remaining TTL in seconds, -1 if no expiration, -2 if key doesn't exist

        Example:
            kv.default.set("session", "data", ttl=3600)
            remaining = kv.default.ttl("session")  # e.g., 3599
        """
        ...

    def keys(self, pattern: str = "*") -> list[str]:
        """
        Get all keys matching a glob pattern.

        Parameters:
            pattern: Glob pattern to match keys (default: "*")

        Returns:
            List of matching keys

        Example:
            all_keys = kv.default.keys()
            user_keys = kv.default.keys("user:*")
            session_keys = kv.default.keys("session:*")
        """
        ...

    def clear(self) -> None:
        """
        Remove all keys from the store.

        Warning: This operation cannot be undone.

        Example:
            kv.default.clear()
        """
        ...

    def close(self) -> None:
        """
        Release this store. No-op on the default store.

        For stores opened with kv.open(), this decrements the reference
        count and closes the store when it reaches zero.
        """
        ...


# The default system-wide KV store
default: Storage


def open(name: str) -> Storage:
    """
    Open or reuse a named KV store.

    Parameters:
        name: Store name. Use ":memory:name" for in-memory stores,
              or a filesystem path for persistent stores.

    Returns:
        KV store object with get, set, delete, exists, ttl, keys, clear, close methods.

    Example:
        import scriptling.runtime.kv as kv

        # In-memory store
        mem = kv.open(":memory:session")
        mem.set("user", "alice")
        mem.close()

        # Persistent store
        db = kv.open("/data/agent.db")
        db.set("fact", "the sky is blue")
        db.close()

        # Use the default system store
        kv.default.set("key", "value")
    """
    ...
