"""
Scriptling sys library stubs.

System-specific parameters and functions. sys.stdout and sys.stderr are
environment-bound streams: their destination is resolved at write time, so
output capture and host-configured writers apply as they do for print().
"""

from typing import Iterator, List, NoReturn, Union

class StdinStream:
    """Standard input stream (sys.stdin). Iterating yields lines."""

    def read(self) -> str:
        """Read all remaining data from stdin."""
        ...

    def readline(self) -> str:
        """Read one line from stdin, including the trailing newline."""
        ...

    def __iter__(self) -> Iterator[str]:
        """Iterate over lines of stdin."""
        ...

class OutputStream:
    """Output stream (sys.stdout / sys.stderr)."""

    def write(self, s: str) -> int:
        """Write string s to the stream; returns the number of characters written."""
        ...

    def writelines(self, lines: List[str]) -> None:
        """Write each string in lines to the stream; no separators are added."""
        ...

    def flush(self) -> None:
        """Flush the write buffer; a no-op for unbuffered streams."""
        ...

    def isatty(self) -> bool:
        """Return True if the stream is a terminal."""
        ...

    def __enter__(self) -> OutputStream:
        """Return the stream itself for use in a with statement."""
        ...

    def __exit__(self, *args: object) -> bool:
        """Flush the stream; never suppresses exceptions."""
        ...

platform: str
version: str
maxsize: int
path_sep: str
argv: List[str]
stdin: StdinStream
stdout: OutputStream
stderr: OutputStream

def exit(arg: Union[int, str] = 0) -> NoReturn:
    """Exit the interpreter. An int sets the exit code; a string exits with code 1 and that message. Cannot be caught by try/except (finally blocks still run)."""
    ...
