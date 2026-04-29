"""
Scriptling FS Library - Type stubs for IntelliSense support.

Binary I/O library for reading and unpacking binary file formats.
Requires explicit registration with allowed paths.
"""

from typing import List, Optional, Union

def read_bytes(path: str, offset: int, length: int) -> str:
    """
    Read a range of bytes from a file.

    Parameters:
        path: File path to read
        offset: 0-based byte position to start reading
        length: Number of bytes to read (max 64 MiB per call)

    Returns:
        Raw bytes as a string
    """
    ...

def write_bytes(path: str, offset: int, data: str) -> None:
    """
    Write raw bytes at an offset. Creates the file if it does not exist.

    Parameters:
        path: File path to write
        offset: 0-based byte position to start writing
        data: Raw bytes to write

    Returns:
        None
    """
    ...

def unpack(format: str, data: str) -> List[Union[int, float]]:
    """
    Unpack binary data using format strings.

    Supported format characters: b(B) int8(uint8), h(H) int16(uint16),
    i(I) int32(uint32), q(Q) int64(uint64), f float32, d float64, e float16.
    Prefix with < for little-endian (default) or > for big-endian.
    A number before a format char means repeat count (e.g. "<4f" reads 4 float32s).

    Parameters:
        format: Format string describing the binary layout
        data: Binary data to unpack

    Returns:
        List of values
    """
    ...

def pack(format: str, values: List[Union[int, float]]) -> str:
    """
    Pack values into a binary string. Uses the same format strings as unpack().

    Parameters:
        format: Format string describing the binary layout
        values: Values to pack

    Returns:
        Binary string
    """
    ...

def byte_at(data: str, index: int) -> int:
    """
    Return the unsigned byte value (0-255) at the given index.

    Parameters:
        data: Binary data
        index: Byte index

    Returns:
        Unsigned byte value (0-255)
    """
    ...

def len(data: str) -> int:
    """
    Return the byte length of a binary string.
    Unlike the builtin len(), this counts bytes, not Unicode code points.

    Parameters:
        data: Binary data

    Returns:
        Byte length
    """
    ...

def slice(data: str, start: int, end: Optional[int] = None) -> str:
    """
    Byte-safe slicing of binary data.
    Unlike string slicing, this operates on byte offsets, not Unicode code points.

    Parameters:
        data: Binary data
        start: Start byte offset
        end: End byte offset (default: end of data)

    Returns:
        Binary string slice
    """
    ...
