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
    """Read an entire file as a string."""
    ...

def write_file(path: str, content: str, mode: int = 0o644) -> None:
    """Write a string to a file, creating or overwriting it."""
    ...

def append_file(path: str, content: str) -> None:
    """Append a string to a file, creating it if needed."""
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
