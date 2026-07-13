"""
Scriptling zipfile Library - Type stubs for IntelliSense support.

Read and write ZIP archives.
"""


class ZipFile:
    def __init__(self, path: str, mode: str = "r") -> None:
        """
        Open a ZIP archive.

        Parameters:
            path  Path to the archive file
            mode  "r" for reading, "w" for writing (default "r")
        """
        ...

    def namelist(self) -> list[str]:
        """Return a list of archive member names."""
        ...

    def read(self, name: str) -> str:
        """Read a member from the archive as a string."""
        ...

    def extract(self, member: str, path: str = ".") -> str:
        """Extract a single member to path. Returns the extracted file path."""
        ...

    def extractall(self, path: str = ".") -> list[str]:
        """Extract all members to path. Returns list of extracted file paths."""
        ...

    def write(self, filename: str, arcname: str = "") -> None:
        """Add a file to the archive (write mode only)."""
        ...

    def writestr(self, name: str, data: str) -> None:
        """Write a string as a member in the archive (write mode only)."""
        ...

    def close(self) -> None:
        """Close the archive."""
        ...


def is_zipfile(path: str) -> bool:
    """Return True if path is a valid ZIP archive."""
    ...
