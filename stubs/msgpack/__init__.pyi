"""
MessagePack binary serialisation library — type stubs for IntelliSense.

Mirrors Python's msgpack module. packb() returns bytes; unpackb() takes bytes.
The default backing codec is shamaton-msgpack (matching gossip's DefaultConfig)
but the library is codec-backed via stdlib.MsgpackCodec in the Go runtime.
"""

from typing import Any


def packb(obj: Any) -> bytes:
    """
    Serialise a Scriptling value (dict, list, str, int, float, bool, None,
    bytes) to MessagePack bytes.

    Returns:
        bytes: the MessagePack-encoded payload.
    """
    ...


def unpackb(packed: bytes) -> Any:
    """
    Parse MessagePack bytes into a Scriptling value.

    Parameters:
        packed: a bytes value containing a MessagePack payload.

    Returns:
        dict, list, str, int, float, bool, None, or bytes: the decoded value.
    """
    ...


# pack/unpack aliases (older Python msgpack naming).
def pack(obj: Any) -> bytes:
    """Alias for packb()."""
    ...


def unpack(packed: bytes) -> Any:
    """Alias for unpackb()."""
    ...


def codec_name() -> str:
    """
    Return the name of the backing MessagePack codec (e.g. "shamaton-msgpack").
    Useful for logging or branching when interoperating with gossip.
    """
    ...
