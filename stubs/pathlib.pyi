"""
Scriptling pathlib stubs.
"""

from typing import Tuple

class Path:
    name: str
    stem: str
    suffix: str
    parent: str
    parts: Tuple[str, ...]

    def __init__(self, path: str) -> None:
        ...

    def joinpath(self, *other: str) -> "Path":
        """Combine this path with other path segments."""
        ...

    def exists(self) -> bool:
        """Return True if the path exists."""
        ...

    def is_file(self) -> bool:
        """Return True if this path is a regular file."""
        ...

    def is_dir(self) -> bool:
        """Return True if this path is a directory."""
        ...

    def mkdir(
        self,
        mode: int = 0o777,
        parents: bool = False,
        exist_ok: bool = False,
    ) -> None:
        """Create this directory."""
        ...

    def chmod(self, mode: int) -> None:
        """Change file or directory permissions."""
        ...

    def rmdir(self) -> None:
        """Remove this empty directory."""
        ...

    def unlink(self, missing_ok: bool = False) -> None:
        """Remove this file or symbolic link."""
        ...

    def read_text(self) -> str:
        """Read the file contents as a string."""
        ...

    def write_text(self, data: str) -> None:
        """Write a string to the file."""
        ...

    def read_bytes(self) -> str:
        """Read the file contents as bytes."""
        ...

    def write_bytes(self, data: str) -> None:
        """Write bytes to the file."""
        ...
