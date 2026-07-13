"""
Scriptling glob Library - Type stubs for IntelliSense support.

Unix shell-style wildcard matching for filenames, similar to Python's glob
module.
"""

from typing import Iterator


def glob(
    pattern: str,
    root_dir: str = ".",
    *,
    recursive: bool = False,
    include_hidden: bool = False,
) -> list[str]:
    """
    Find all pathnames matching a shell-style wildcard pattern.

    Parameters:
        pattern        Shell-style wildcard pattern to match
        root_dir       Directory to search from (default: current directory)
        recursive      When True, ** matches files and directories recursively,
                       descending into every subdirectory (default: False). When
                       False, ** is treated as *.
        include_hidden When True, entries whose name starts with "." are matched;
                       when False (the default) they are skipped.

    Returns:
        List of matching pathnames as strings (arbitrary order).

    Recursive searches use a bounded parallel directory walk, the same worker
    model as scriptling.grep.

    Example:
        import glob

        # Match all .txt files in the current directory
        txt_files = glob.glob("*.txt")

        # Recursively find all markdown files
        docs = glob.glob("**/*.md", recursive=True)

        # Also descend into dot-directories such as .github
        all_docs = glob.glob("**/*.md", recursive=True, include_hidden=True)
    """
    ...


def iglob(
    pattern: str,
    root_dir: str = ".",
    *,
    recursive: bool = False,
    include_hidden: bool = False,
) -> Iterator[str]:
    """
    Find all pathnames matching a shell-style wildcard pattern, returned as an
    iterator. Memory efficient for large result sets. See glob() for pattern
    syntax and parameter details.

    Parameters:
        pattern        Shell-style wildcard pattern to match
        root_dir       Directory to search from (default: current directory)
        recursive      When True, ** matches recursively (default: False)
        include_hidden When True, dot-entries are matched (default: False)

    Returns:
        Iterator yielding matching pathnames as strings.

    Example:
        import glob

        for filename in glob.iglob("**/*.py", recursive=True):
            print(f"Found: {filename}")
    """
    ...


def escape(pattern: str) -> str:
    """
    Escape all special characters (*, ?, [, ]) in a pattern so they are treated
    as literal characters rather than wildcards.

    Parameters:
        pattern  Pattern containing characters to escape

    Returns:
        The escaped pattern.

    Example:
        import glob

        pattern = glob.escape("file*.txt")
        # Returns "file[*].txt" which matches the literal "file*.txt"
    """
    ...
