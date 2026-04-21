"""
Scriptling Text Library - Type stubs for IntelliSense support.

In-place file content replacement and capture group extraction.
Replace functions accept a file or directory as the path and return the number
of files modified. extract() returns a list of match dicts with capture groups.
"""

from typing import Optional

def replace(
    old: str,
    new: str,
    path: str,
    *,
    recursive: bool = False,
    ignore_case: bool = False,
    glob: str = "",
    follow_links: bool = False,
    max_size: Optional[int] = 1048576,
) -> int:
    """
    Replace all occurrences of a literal string in a file or directory.

    Files are modified in-place using atomic temp-file rename, so a partial
    write cannot corrupt a file. Binary files are skipped automatically.

    Parameters:
        old          Literal string to search for
        new          Replacement string
        path         File or directory to modify
        recursive    Recurse into subdirectories (default: False)
        ignore_case  Case-insensitive matching (default: False)
        glob         Only modify files matching this glob pattern, e.g. "*.py"
        follow_links Follow symlinks if they resolve within allowed paths (default: False)
        max_size     Skip files larger than this many bytes (default: 1 MiB, None = no limit)

    Returns:
        Number of files modified (int)

    Example:
        import scriptling.text as text

        # Replace in a single file
        n = text.replace("old_func()", "new_func()", "/path/to/file.py")

        # Replace across all Python files recursively
        n = text.replace("old_func()", "new_func()", "./src", recursive=True, glob="*.py")
        print(f"{n} file(s) modified")

        # Case-insensitive replace
        n = text.replace("TODO", "DONE", "./src", ignore_case=True, recursive=True)
    """
    ...

def replace_pattern(
    regex: str,
    new: str,
    path: str,
    *,
    recursive: bool = False,
    ignore_case: bool = False,
    glob: str = "",
    follow_links: bool = False,
    max_size: Optional[int] = 1048576,
) -> int:
    """
    Replace all regex matches in a file or directory.

    Files are modified in-place using atomic temp-file rename, so a partial
    write cannot corrupt a file. Binary files are skipped automatically.
    Capture groups are referenced in the replacement as ${1}, ${2}, ${name}.

    Parameters:
        regex        Regular expression pattern
        new          Replacement string (may reference capture groups as ${1}, ${2}, etc.)
        path         File or directory to modify
        recursive    Recurse into subdirectories (default: False)
        ignore_case  Case-insensitive matching (default: False)
        glob         Only modify files matching this glob pattern, e.g. "*.py"
        follow_links Follow symlinks if they resolve within allowed paths (default: False)
        max_size     Skip files larger than this many bytes (default: 1 MiB, None = no limit)

    Returns:
        Number of files modified (int)

    Example:
        import scriptling.text as text

        # Rename a function across all Python files
        n = text.replace_pattern(
            r"def old_(\w+)\(",
            "def new_${1}(",
            "./src",
            recursive=True,
            glob="*.py"
        )
        print(f"{n} file(s) modified")

        # Case-insensitive regex replace
        n = text.replace_pattern(r"foo\\.bar", "foo.baz", "./src", ignore_case=True)
    """
    ...

def extract(
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
    Extract regex capture groups from a file or directory.

    Parameters:
        regex        Regular expression with capture groups
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
            - text (str): Full content of the matched line
            - groups (list[str]): Captured group strings (empty if no capture groups)

    Example:
        import scriptling.text as text

        # Extract all function names from Python files
        matches = text.extract(r"def (\\w+)\\(", "./src", recursive=True, glob="*.py")
        for m in matches:
            print(f"{m['file']}:{m['line']}: {m['groups'][0]}")

        # Extract key=value pairs
        matches = text.extract(r"(\\w+)=(\\S+)", "./config.txt")
        for m in matches:
            key, value = m["groups"]
            print(f"{key} -> {value}")

        # Extract version strings across a project
        matches = text.extract(r"version\\s*=\\s*[\"']([\\d.]+)[\"']", "./src", recursive=True)
        versions = [m["groups"][0] for m in matches]
    """
    ...
