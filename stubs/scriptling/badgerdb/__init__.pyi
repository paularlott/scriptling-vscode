"""
BadgerDB plugin — embedded key/value store.

The string-KV core is mirrored by scriptling.valkey, so those scripts move
between a shared cache and local storage unchanged. Valkey's sets, queues
and database selection have no counterpart here. Badger allows one process to
hold a database open at a time; the directory must fall inside the host's
allowed paths.
"""

from typing import Dict, List, Optional


class Client:
    """A handle to an open BadgerDB database."""

    def get(self, key: str) -> Optional[str]:
        """Value stored at key, or None when the key does not exist."""
        ...

    def set(self, key: str, value: str, ttl_seconds: int = 0) -> None:
        """Store a string value. ttl_seconds of 0 (default) means no expiry."""
        ...

    def set_if_absent(self, key: str, value: str, ttl_seconds: int = 0) -> bool:
        """Store only when the key does not exist; whether it was stored."""
        ...

    def mget(self, *keys: str) -> List[Optional[str]]:
        """Values for the keys in one call, in order; None where missing."""
        ...

    def mset(self, mapping: Dict[str, str], ttl_seconds: int = 0) -> None:
        """Store every entry of a dict in one call."""
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

    def persist(self, key: str) -> bool:
        """Remove a key's expiry so it lives forever. False when missing."""
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

    def hash_set(self, key: str, field: str, value: str) -> int:
        """Set one hash field; 1 when the field was new, 0 when it overwrote."""
        ...

    def hash_get(self, key: str, field: str) -> Optional[str]:
        """The field's value, or None when the key or field is missing."""
        ...

    def hash_delete(self, key: str, *fields: str) -> int:
        """Delete fields, returning how many existed.

        The hash key disappears with its last field, expiry included.
        """
        ...

    def hash_all(self, key: str) -> Dict[str, str]:
        """Every field and value; an empty dict when the key is missing."""
        ...

    def hash_size(self, key: str) -> int:
        """How many fields the hash holds. 0 when the key is missing."""
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
