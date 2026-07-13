"""
Scriptling tempfile Library - Type stubs for IntelliSense support.

Temporary file and directory creation with security restrictions.
"""

from typing import Optional


def mkstemp(
    suffix: str = "",
    prefix: str = "tmp",
    dir: Optional[str] = None,
) -> str:
    """
    Create a temporary file and return its path.

    The file is created with mode 0600 and immediately closed. Unlike Python's
    mkstemp (which returns (fd, path)), this returns just the path.

    Parameters:
        suffix  Suffix for the filename (default "")
        prefix  Prefix for the filename (default "tmp")
        dir     Directory to create the file in (default: system temp directory)

    Returns:
        The absolute path to the created file.

    Example:
        import tempfile
        path = tempfile.mkstemp(prefix="app_", suffix=".toml")
    """
    ...


def mkdtemp(
    suffix: str = "",
    prefix: str = "tmp",
    dir: Optional[str] = None,
) -> str:
    """
    Create a temporary directory and return its path.

    The directory is created with mode 0700 (owner only).

    Parameters:
        suffix  Suffix for the directory name (default "")
        prefix  Prefix for the directory name (default "tmp")
        dir     Parent directory (default: system temp directory)

    Returns:
        The absolute path to the created directory.

    Example:
        import tempfile
        scratch = tempfile.mkdtemp(prefix="build_")
    """
    ...


def gettempdir() -> str:
    """
    Return the default temporary directory.

    When allowedPaths restricts access and the system temp directory is outside
    the allowed set, the first allowed path is returned instead.

    Returns:
        The temp directory path.
    """
    ...


def gettempprefix() -> str:
    """
    Return the default temporary file name prefix.

    Returns:
        "tmp"
    """
    ...
