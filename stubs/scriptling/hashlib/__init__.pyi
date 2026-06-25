"""
Scriptling Hashlib Library - Type stubs for IntelliSense support.

Cryptographic hash functions.

Note: Scriptling has no `bytes` type. Strings are used as byte buffers, and
lists of byte values (as returned by str.encode()) are also accepted.
"""

from typing import List, Union

ByteString = Union[str, List[int]]


class Hash:
    """
    A hash object returned by hashlib.md5(), hashlib.sha1() or hashlib.sha256().

    Call .hexdigest() to get the digest as a lowercase hex string, or
    .digest() for the raw bytes (as a string).
    """

    name: str
    digest_size: int
    block_size: int

    def update(self, data: ByteString) -> None:
        """
        Feed data into the hash. May be called repeatedly to accumulate input.

        Parameters:
            data: A string (treated as bytes) or a list of byte values

        Returns:
            None
        """
        ...

    def digest(self) -> str:
        """
        Return the raw digest as a byte string.

        Returns:
            The digest bytes as a string
        """
        ...

    def hexdigest(self) -> str:
        """
        Return the digest as a lowercase hexadecimal string.

        Returns:
            Hex string (length depends on algorithm: md5=32, sha1=40, sha256=64)
        """
        ...

    def copy(self) -> "Hash":
        """
        Return an independent copy of this hash object.

        Returns:
            A new Hash with the same algorithm and accumulated data
        """
        ...


def md5(data: ByteString = ...) -> Hash:
    """
    Create an MD5 hash object.

    Parameters:
        data: Optional initial data (string as bytes, or list of byte values)

    Returns:
        Hash object (digest_size 16, hexdigest length 32)
    """
    ...


def sha1(data: ByteString = ...) -> Hash:
    """
    Create a SHA-1 hash object.

    Parameters:
        data: Optional initial data (string as bytes, or list of byte values)

    Returns:
        Hash object (digest_size 20, hexdigest length 40)
    """
    ...


def sha256(data: ByteString = ...) -> Hash:
    """
    Create a SHA-256 hash object.

    Parameters:
        data: Optional initial data (string as bytes, or list of byte values)

    Returns:
        Hash object (digest_size 32, hexdigest length 64)
    """
    ...
