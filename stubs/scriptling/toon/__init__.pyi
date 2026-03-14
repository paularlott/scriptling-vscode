"""
Scriptling TOON Library - Type stubs for IntelliSense support.

TOON (Token-Oriented Object Notation) encoding/decoding library.
TOON is a compact text format optimized for LLM consumption.
"""

from typing import Any

def encode(data: Any) -> str:
    """
    Encode data to TOON format.

    Encodes a scriptling value (string, int, float, bool, list, dict) to TOON format.

    Parameters:
        data: Any scriptling value to encode

    Returns:
        TOON formatted string

    Example:
        text = toon.encode({"name": "Alice", "age": 30})
        # Returns: TOON formatted string
    """
    ...

def decode(text: str) -> Any:
    """
    Decode TOON format to scriptling objects.

    Decodes a TOON formatted string to scriptling objects
    (strings, ints, floats, bools, lists, dicts).

    Parameters:
        text: TOON formatted string

    Returns:
        Decoded scriptling value

    Example:
        data = toon.decode(text)
        # Returns: decoded dict/list/string/etc
    """
    ...

def encode_options(data: Any, indent: int, delimiter: str) -> str:
    """
    Encode data to TOON format with custom options.

    Encodes a scriptling value to TOON format with custom indentation and delimiter.

    Parameters:
        data: Any scriptling value to encode
        indent: Number of spaces per indentation level (default: 2)
        delimiter: Delimiter for arrays and tabular data (default: ",")

    Returns:
        TOON formatted string

    Example:
        text = toon.encode_options(data, 4, "|")
    """
    ...

def decode_options(text: str, strict: bool, indent_size: int) -> Any:
    """
    Decode TOON format with custom options.

    Decodes a TOON formatted string with custom parsing options.

    Parameters:
        text: TOON formatted string
        strict: Enable strict validation (default: true)
        indent_size: Expected indentation size (0 = auto-detect, default: 0)

    Returns:
        Decoded scriptling value

    Example:
        data = toon.decode_options(text, strict=False, indent_size=2)
    """
    ...
