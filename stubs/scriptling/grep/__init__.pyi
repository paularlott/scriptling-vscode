"""
Scriptling Grep Library - Type stubs for IntelliSense support.

Fast file content search. Use pattern() for regex searches and string() for
literal string searches. Both accept a file or directory as the path.
"""

from typing import Optional

def pattern(
    regex: str,
    path: str,
    *,
    recursive: bool = False,
    ignore_case: bool = False,
    glob: str = "",
    follow_links: bool = False,
    max_size: Optional[int] = 1048576,
) -> list[dict]:
    """
    Search for a regex pattern in a file or directory.

    Parameters:
        regex        Regular expression pattern
        path         File or directory to search
        recursive    Recurse into subdirectories (default: False)
        ignore_case  Case-insensitive matching (default: False)
        glob         Only search files matching this glob pattern, e.g. "*.py"
        follow_links Follow symlinks if they resolve within allowed paths (default: False)
        max_size     Skip files larger than this many bytes (default: 1 MiB, None = no limit)

    Returns:
        List of match dicts, each with:
            - file (str): Path to the matched file
            - line (int): 1-based line number of the match
            - text (str): Content of the matched line

    Example:
        import scriptling.grep as grep

        # Find all TODO comments in Python files
        matches = grep.pattern(r"\\bTODO\\b", "./src", recursive=True, glob="*.py")
        for m in matches:
            print(f"{m['file']}:{m['line']}: {m['text']}")

        # Case-insensitive regex search
        matches = grep.pattern("error|warning", "./logs", ignore_case=True, recursive=True)

        # Search a single file
        matches = grep.pattern(r"def \\w+\\(", "/path/to/script.py")
    """
    ...

def string(
    text: str,
    path: str,
    *,
    recursive: bool = False,
    ignore_case: bool = False,
    glob: str = "",
    follow_links: bool = False,
    max_size: Optional[int] = 1048576,
) -> list[dict]:
    """
    Search for a literal string in a file or directory.

    The text is treated exactly as written — no regex interpretation.
    Use this when searching for strings that contain regex special characters
    such as . ( ) * + ? [ ] ^ $ | \\ without needing to escape them.

    Parameters:
        text         Literal string to search for
        path         File or directory to search
        recursive    Recurse into subdirectories (default: False)
        ignore_case  Case-insensitive matching (default: False)
        glob         Only search files matching this glob pattern, e.g. "*.py"
        follow_links Follow symlinks if they resolve within allowed paths (default: False)
        max_size     Skip files larger than this many bytes (default: 1 MiB, None = no limit)

    Returns:
        List of match dicts, each with:
            - file (str): Path to the matched file
            - line (int): 1-based line number of the match
            - text (str): Content of the matched line

    Example:
        import scriptling.grep as grep

        # Search for a literal string (. is not treated as regex wildcard)
        matches = grep.string("foo.bar()", "./src", recursive=True)

        # Case-insensitive literal search
        matches = grep.string("TODO:", "./src", ignore_case=True, recursive=True)

        # Search a single file
        matches = grep.string("import os", "/path/to/script.py")
    """
    ...
