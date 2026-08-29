"""
Valkey / Redis plugin — key/value client.

Single-node servers; the string-KV core is mirrored by scriptling.badgerdb
(sets, queues and database selection are valkey-only). URL
schemes: ``valkey://``, ``redis://``, ``tcp://`` (plaintext) and
``valkeys://``, ``rediss://`` (TLS), with optional ``user:pass@`` and a
``/db`` path.
"""

from typing import List, Optional


class Client:
    """A handle to a connected Valkey or Redis server."""

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
        """Check the server is reachable, raising on failure."""
        ...

    def select(self, index: int) -> None:
        """Switch the connection to a different database (cheap reconnect)."""
        ...

    def db(self) -> int:
        """The database index this client currently addresses."""
        ...

    def set_add(self, key: str, *members: str) -> int:
        """Add members to a set; returns how many were new."""
        ...

    def set_remove(self, key: str, *members: str) -> int:
        """Remove members from a set; returns how many existed."""
        ...

    def set_members(self, key: str) -> List[str]:
        """Every member of the set, unordered."""
        ...

    def set_contains(self, key: str, member: str) -> bool:
        """Whether member is in the set."""
        ...

    def set_size(self, key: str) -> int:
        """Number of members in the set."""
        ...

    def queue_push(self, key: str, *values: str) -> int:
        """Push values onto the queue's tail; returns the queue length."""
        ...

    def queue_pop(self, key: str) -> Optional[str]:
        """Pop the value at the queue's head, or None when empty."""
        ...

    def queue_wait(self, key: str, timeout: float) -> Optional[str]:
        """Pop the head value, waiting up to timeout seconds; None on timeout.

        Fractional seconds allowed; 0 behaves like queue_pop. No infinite
        wait on purpose: a worker loop re-issues queue_wait.
        """
        ...

    def queue_peek(self, key: str) -> Optional[str]:
        """The value at the queue's head without removing it."""
        ...

    def queue_size(self, key: str) -> int:
        """Number of values in the queue."""
        ...

    def queue_range(self, key: str, start: int = 0, stop: int = -1) -> List[str]:
        """Values from the queue in order, head first, without removing them."""
        ...

    def close(self) -> None:
        """Close the client and release its connections."""
        ...


def connect(url: str = "valkey://localhost:6379") -> Client:
    """Connect to a Valkey or Redis server.

    The server address must pass the host's network policy.
    """
    ...
