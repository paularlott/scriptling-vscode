"""
Scriptling CSV Library - Type stubs for IntelliSense support.

CSV parsing and formatting (string-based, no filesystem access).
"""

from typing import Optional


def parse(content: str, *, delimiter: str = ",") -> list[list[str]]:
    """
    Parse a CSV string into a list of rows.

    Handles quoting, embedded commas, and embedded newlines per RFC 4180.

    Parameters:
        content   CSV text to parse
        delimiter Field delimiter character (default ",")

    Returns:
        List of rows, each a list of string values.
    """
    ...


def parse_dict(content: str, *, delimiter: str = ",") -> list[dict]:
    """
    Parse CSV text into a list of dicts. First row is treated as headers.

    Parameters:
        content   CSV text to parse
        delimiter Field delimiter character (default ",")

    Returns:
        List of dicts keyed by header names.
    """
    ...


def format(rows: list[list[str]], *, delimiter: str = ",") -> str:
    """
    Format a list of lists into CSV text.

    Values containing commas, quotes, or newlines are automatically quoted.

    Parameters:
        rows      List of rows (each a list of string values)
        delimiter Field delimiter character (default ",")

    Returns:
        CSV-formatted text.
    """
    ...


def format_dict(
    rows: list[dict],
    *,
    delimiter: str = ",",
    columns: Optional[list[str]] = None,
) -> str:
    """
    Format a list of dicts into CSV text with a header row.

    Column headers are taken from the columns kwarg if provided, otherwise
    from the sorted keys of the first dict.

    Parameters:
        rows      List of dicts
        delimiter Field delimiter character (default ",")
        columns   Explicit column order (default: sorted keys)

    Returns:
        CSV-formatted text with a header row.
    """
    ...
