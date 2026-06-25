"""
Scriptling HMAC Library - Type stubs for IntelliSense support.

Keyed-Hashing for Message Authentication (HMAC), typically used to verify
webhook signatures.

Note: Scriptling has no `bytes` type. Strings are used as byte buffers, and
lists of byte values (as returned by str.encode()) are also accepted.
"""

from typing import List, Optional, Union

from hashlib import Hash

ByteString = Union[str, List[int]]
DigestMod = Union[str, Hash, None]


class HMAC:
    """
    An HMAC object returned by hmac.new().

    Call .hexdigest() to get the MAC as a lowercase hex string, or .digest()
    for the raw bytes (as a string).
    """

    name: str
    digest_size: int
    block_size: int

    def update(self, data: ByteString) -> None:
        """
        Feed data into the message being authenticated. May be called repeatedly.

        Parameters:
            data: A string (treated as bytes) or a list of byte values

        Returns:
            None
        """
        ...

    def digest(self) -> str:
        """
        Return the raw MAC as a byte string.

        Returns:
            The MAC bytes as a string
        """
        ...

    def hexdigest(self) -> str:
        """
        Return the MAC as a lowercase hexadecimal string.

        Returns:
            Hex string
        """
        ...

    def copy(self) -> "HMAC":
        """
        Return an independent copy of this HMAC object.

        Returns:
            A new HMAC with the same key, algorithm and accumulated data
        """
        ...


def new(key: ByteString, msg: Optional[ByteString] = ..., digestmod: DigestMod = ...) -> HMAC:
    """
    Create an HMAC object.

    Parameters:
        key: Secret key (string as bytes, or list of byte values)
        msg: Optional initial message data
        digestmod: Hash algorithm to use. A string name ("sha256" default,
            "sha1", "md5"), a hashlib constructor (e.g. hashlib.sha256),
            a Hash object, or None (defaults to sha256)

    Returns:
        HMAC object
    """
    ...


def digest(key: ByteString, msg: ByteString, digestmod: DigestMod) -> str:
    """
    One-shot HMAC. Equivalent to hmac.new(key, msg, digestmod).digest().

    Parameters:
        key: Secret key
        msg: Message data
        digestmod: Hash algorithm (string name, Hash object, or hashlib constructor)

    Returns:
        The raw MAC as a byte string
    """
    ...


def compare_digest(a: str, b: str) -> bool:
    """
    Compare two strings using a constant-time comparison.

    Use this when comparing signature values so that timing differences do
    not leak information about the expected value.

    Parameters:
        a: First string
        b: Second string

    Returns:
        True if the strings are equal, False otherwise
    """
    ...
