"""
Scriptling pathlib stubs.
"""

from typing import List, Tuple

class Path:
    name: str
    stem: str
    suffix: str
    suffixes: List[str]
    parent: "Path"
    parts: Tuple[str, ...]

    def __init__(self, path: str) -> None:
        ...

    def joinpath(self, *other: "str | Path") -> "Path":
        """Combine this path with other path segments."""
        ...

    def __truediv__(self, other: "str | Path") -> "Path":
        """Path("/etc") / "hosts": join a segment, like joinpath()."""
        ...

    def __str__(self) -> str:
        """The path as a string."""
        ...

    def __eq__(self, other: object) -> bool:
        """Paths are equal when their paths are."""
        ...

    def __lt__(self, other: "Path") -> bool:
        """Order paths by their path strings."""
        ...

    def __hash__(self) -> int:
        """Hash of the path string, so paths work in sets and as dict keys."""
        ...

    def with_name(self, name: str) -> "Path":
        """A new path with the final component replaced."""
        ...

    def with_suffix(self, suffix: str) -> "Path":
        """A new path with the suffix changed (added, or removed with "")."""
        ...

    def with_stem(self, stem: str) -> "Path":
        """A new path with the stem changed, keeping the suffix."""
        ...

    def is_absolute(self) -> bool:
        """True for a path starting at the root."""
        ...

    def as_posix(self) -> str:
        """The path as a string with forward slashes."""
        ...

    def relative_to(self, other: "str | Path") -> "Path":
        """This path relative to other; ValueError when it is not under other."""
        ...

    def is_relative_to(self, other: "str | Path") -> bool:
        """True when this path is under other."""
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

    def read_bytes(self) -> bytes:
        """Read the file contents as bytes (preserves binary data)."""
        ...

    def write_bytes(self, data: "bytes | str") -> None:
        """Write bytes to the file. Accepts bytes or str (UTF-8 encoded)."""
        ...

    def copy(self, target: str) -> "Path":
        """Copy this file or directory to the target path."""
        ...

    def rename(self, target: str) -> "Path":
        """Rename this file or directory to the target path."""
        ...

    def iterdir(self) -> List["Path"]:
        """Return a list of Path objects for the directory contents."""
        ...

    def glob(self, pattern: str) -> List["Path"]:
        """Return a list of Path objects matching the pattern."""
        ...


PathClass = Path
"""The class of Path objects, e.g. isinstance(p, pathlib.PathClass). pathlib.Path(...) is the constructor."""
