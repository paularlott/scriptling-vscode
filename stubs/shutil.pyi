"""
Scriptling shutil Library - Type stubs for IntelliSense support.

High-level file and directory operations — copy, move, rmtree, disk_usage.
"""


def copy(src: str, dst: str) -> str:
    """
    Copy a file or directory tree. File modes are preserved.

    Parameters:
        src  Source file or directory
        dst  Destination path

    Returns:
        The destination path.

    Example:
        import shutil
        shutil.copy("config.toml", "config.toml.bak")
    """
    ...


def copy2(src: str, dst: str) -> str:
    """
    Copy a file with metadata. Identical to copy() — file mode is always
    preserved. Provided for Python compatibility.

    Parameters:
        src  Source file or directory
        dst  Destination path

    Returns:
        The destination path.
    """
    ...


def copytree(src: str, dst: str) -> str:
    """
    Recursively copy a directory tree. File modes are preserved.

    Parameters:
        src  Source directory (must exist and be a directory)
        dst  Destination path (must not exist)

    Returns:
        The destination path.

    Raises:
        Error if src is not a directory.
    """
    ...


def rmtree(path: str) -> None:
    """
    Recursively delete a directory tree. Unlike os.removedirs, the directory
    does not need to be empty.

    Parameters:
        path  Directory to remove

    Example:
        import shutil, tempfile
        scratch = tempfile.mkdtemp()
        # ... work ...
        shutil.rmtree(scratch)
    """
    ...


def move(src: str, dst: str) -> str:
    """
    Move or rename a file or directory (same as os.rename).

    Parameters:
        src  Source path
        dst  Destination path

    Returns:
        The destination path.
    """
    ...


def disk_usage(path: str) -> dict:
    """
    Return disk usage statistics for the file system containing path.

    Parameters:
        path  Any path on the file system to query

    Returns:
        Dict with keys:
            - total (int): Total space in bytes
            - used (int): Used space in bytes (includes reserved blocks)
            - free (int): Free space available to non-privileged users

    Example:
        import shutil
        du = shutil.disk_usage("/")
        print(f"{du['used'] / du['total'] * 100:.1f}% used")
    """
    ...
