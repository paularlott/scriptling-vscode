"""
Scriptling os library stubs.

Scriptling implements a focused, path-restricted subset of Python's os module
plus convenience text file helpers.
"""

from typing import Dict, List, Optional

from . import path as path

sep: str
linesep: str
name: str
platform: str
environ: Dict[str, str]

def getenv(key: str, default: Optional[str] = None) -> Optional[str]:
    """Return the environment variable value, or default/None if unset."""
    ...

def getcwd() -> str:
    """Return the current working directory."""
    ...

def listdir(path: str = ".") -> List[str]:
    """Return entry names in a directory."""
    ...

def read_file(path: str) -> str:
    """Read an entire file as a string. Use read_bytes() for binary files."""
    ...

def read_bytes(path: str) -> bytes:
    """Read an entire file as bytes (preserves binary data)."""
    ...

def read_lines(path: str) -> "Iterator[str]":
    """Iterate over lines in a file lazily (memory-efficient for large files).

    Yields one str per line (without trailing newline). The file handle is
    closed when the iterator reaches EOF; if the loop exits early, the handle
    is closed when the iterator is garbage-collected.
    """
    ...

def write_file(path: str, content: "str | bytes", mode: int = 0o644) -> None:
    """Write a string or bytes to a file, creating or overwriting it."""
    ...

def append_file(path: str, content: "str | bytes") -> None:
    """Append a string or bytes to a file, creating it if needed."""
    ...

def remove(path: str) -> None:
    """Remove a file."""
    ...

def chmod(path: str, mode: int) -> None:
    """Change file or directory permissions."""
    ...

def mkdir(path: str, mode: int = 0o777) -> None:
    """Create a directory with an optional permission mode."""
    ...

def makedirs(path: str, mode: int = 0o777, exist_ok: bool = False) -> None:
    """Create a directory and all missing parents."""
    ...

def rmdir(path: str) -> None:
    """Remove an empty directory."""
    ...

def removedirs(name: str) -> None:
    """Remove an empty directory and empty parent directories."""
    ...

def rename(old: str, new: str) -> None:
    """Rename a file or directory."""
    ...

def symlink(src: str, dst: str) -> None:
    """Create a symbolic link named dst that points to src."""
    ...
