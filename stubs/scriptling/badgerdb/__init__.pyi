"""
BadgerDB plugin — embedded key/value store.

The string-KV core is mirrored by scriptling.valkey, so those scripts move
between a shared cache and local storage unchanged. Valkey's sets, queues
and database selection have no counterpart here. Badger allows one process to
hold a database open at a time; the directory must fall inside the host's
allowed paths.
"""

from typing import List, Optional


class Client:
    """A handle to an open BadgerDB database."""

    def get(self, key: str) -> Optional[str]:
        """Value stored at key, or None when the key does not exist."""
        ...

    def set(self, key: str, value: str, ttl_seconds: int = 0) -> None:
        """Store a string value. ttl_seconds of 0 (default) means no expiry."""
        ...

    def delete(self, *keys: str) -> int:
        """Delete keys, returning how many existed."""
        ...

    def exists(self, *keys: str) -> int:
        """Return how many of the keys exist."""
        ...

    def expire(self, key: str, ttl_seconds: int) -> bool:
        """Set a key's time to live. False when the key is missing."""
        ...

    def ttl(self, key: str) -> Optional[int]:
        """Remaining seconds before expiry; None when missing, -1 when no expiry."""
        ...

    def incr(self, key: str, amount: int = 1) -> int:
        """Add amount to the integer stored at key, returning the new value."""
        ...

    def decr(self, key: str, amount: int = 1) -> int:
        """Subtract amount from the integer stored at key."""
        ...

    def keys(self, pattern: str) -> List[str]:
        """Keys matching a glob pattern (* and ?)."""
        ...

    def ping(self) -> None:
        """Check the store is reachable, raising on failure."""
        ...

    def close(self) -> None:
        """Close the database and release its lock."""
        ...


def open(path: str) -> Client:
    """Open (creating if needed) a BadgerDB database directory."""
    ...
