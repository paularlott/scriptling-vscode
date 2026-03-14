"""
Scriptling Runtime KV Library - Type stubs for IntelliSense support.

Thread-safe key-value store for sharing state across requests.

Note: By default the KV store is in-memory. To persist data, configure a
storage path when starting the server. Keys without a TTL persist indefinitely.
Use TTLs and periodic cleanup to avoid unbounded storage growth.
"""

from typing import Optional, Any

def set(key: str, value: Any, ttl: int = 0) -> None:
    """
    Store a value with optional TTL in seconds.

    Parameters:
        key: The key to store the value under
        value: The value to store (string, int, float, bool, list, dict)
        ttl: Time-to-live in seconds. 0 means no expiration.

    Example:
        runtime.kv.set("api_key", "secret123")
        runtime.kv.set("session:abc", {"user": "bob"}, ttl=3600)
    """
    ...

def get(key: str, default: Any = None) -> Any:
    """
    Retrieve a value by key.

    Parameters:
        key: The key to retrieve
        default: Value to return if key doesn't exist (default: None)

    Returns:
        The stored value, or the default if not found

    Example:
        value = runtime.kv.get("api_key")
        count = runtime.kv.get("counter", default=0)
    """
    ...

def delete(key: str) -> None:
    """
    Remove a key from the store.

    Parameters:
        key: The key to delete

    Example:
        runtime.kv.delete("session:abc")
    """
    ...

def exists(key: str) -> bool:
    """
    Check if a key exists and is not expired.

    Parameters:
        key: The key to check

    Returns:
        True if key exists and is not expired

    Example:
        if runtime.kv.exists("config"):
            config = runtime.kv.get("config")
    """
    ...

def incr(key: str, amount: int = 1) -> int:
    """
    Atomically increment an integer value.

    Parameters:
        key: The key to increment
        amount: Amount to increment by (default: 1)

    Returns:
        The new value after incrementing

    Example:
        runtime.kv.set("counter", 0)
        runtime.kv.incr("counter")      # returns 1
        runtime.kv.incr("counter", 5)   # returns 6
    """
    ...

def ttl(key: str) -> int:
    """
    Get remaining time-to-live for a key.

    Parameters:
        key: The key to check

    Returns:
        Remaining TTL in seconds, -1 if no expiration, -2 if key doesn't exist

    Example:
        runtime.kv.set("session", "data", ttl=3600)
        remaining = runtime.kv.ttl("session")  # e.g., 3599
    """
    ...

def keys(pattern: str = "*") -> list[str]:
    """
    Get all keys matching a glob pattern.

    Parameters:
        pattern: Glob pattern to match keys (default: "*")

    Returns:
        List of matching keys

    Example:
        all_keys = runtime.kv.keys()
        user_keys = runtime.kv.keys("user:*")
        session_keys = runtime.kv.keys("session:*")
    """
    ...

def clear() -> None:
    """
    Remove all keys from the store.

    Warning: This operation cannot be undone.

    Example:
        runtime.kv.clear()
    """
    ...
