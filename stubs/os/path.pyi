"""
Scriptling os.path stubs.
"""

from typing import Tuple

def join(*paths: str) -> str:
    """Join path components."""
    ...

def exists(path: str) -> bool:
    """Return True if path exists."""
    ...

def isfile(path: str) -> bool:
    """Return True if path is a regular file."""
    ...

def isdir(path: str) -> bool:
    """Return True if path is a directory."""
    ...

def basename(path: str) -> str:
    """Return the final path component."""
    ...

def dirname(path: str) -> str:
    """Return the directory component."""
    ...

def split(path: str) -> Tuple[str, str]:
    """Split path into directory and filename."""
    ...

def splitext(path: str) -> Tuple[str, str]:
    """Split path into root and extension."""
    ...

def abspath(path: str) -> str:
    """Return an absolute path."""
    ...

def normpath(path: str) -> str:
    """Normalize a path."""
    ...

def relpath(path: str, start: str = ".") -> str:
    """Return a relative path from start."""
    ...

def isabs(path: str) -> bool:
    """Return True if path is absolute."""
    ...

def getsize(path: str) -> int:
    """Return file size in bytes."""
    ...

def getmtime(path: str) -> float:
    """Return the modification time as a timestamp."""
    ...
