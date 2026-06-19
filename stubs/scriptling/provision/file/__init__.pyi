"""
Scriptling Provision File Library - Type stubs for IntelliSense support.

This library provides file provisioning utilities for creating and updating
files with correct permissions.

Constants:
    CREATED: Status returned when a file was newly written.
    UPDATED: Status returned when a file existed but content differed.
    UNCHANGED: Status returned when a file existed with identical content.
    REMOVED: Status returned when a file or directory was deleted.
    ABSENT: Status returned when a file or directory did not exist.
    EXISTS: Status returned when a directory already existed.

Example:
    import scriptling.provision.file as file

    status = file.ensure("~/.gitconfig", "[user]\\nname = Jane\\n", mode=0o600)
    if status == file.CREATED:
        print("File created")
"""

CREATED: str
UPDATED: str
UNCHANGED: str
REMOVED: str
ABSENT: str
EXISTS: str


def ensure(path: str, content: str, mode: int = 0o644, create_only: bool = False) -> str:
    """
    Ensure a file exists with the given content.

    Creates parent directories if needed. If the file already exists with the
    same content, it is left unchanged. Otherwise the file is written with the
    specified mode.

    When create_only is True, an existing file is never modified: the call
    returns file.UNCHANGED without writing, even if the content differs. New
    files are still written normally.

    Parameters:
        path: Path to the file (supports ~ expansion)
        content: File contents
        mode: File permission mode (default 0o644)
        create_only: If True, never modify an existing file (default False)

    Returns:
        file.CREATED, file.UPDATED, or file.UNCHANGED
    """
    ...


def absent(path: str) -> str:
    """
    Ensure a file does not exist.

    Removes the file if it exists. Does nothing if the file is already absent.

    Parameters:
        path: Path to the file (supports ~ expansion)

    Returns:
        file.REMOVED if the file was deleted,
        file.ABSENT if the file did not exist
    """
    ...


def ensure_directory(path: str, mode: int = 0o755) -> str:
    """
    Ensure a directory exists.

    Creates the directory and all parent directories if needed.

    Parameters:
        path: Path to the directory (supports ~ expansion)
        mode: Directory permission mode (default 0o755)

    Returns:
        file.CREATED if the directory was newly created,
        file.EXISTS if the directory already existed
    """
    ...


def absent_directory(path: str) -> str:
    """
    Ensure an empty directory does not exist.

    Removes the directory if it exists and is empty. Returns an error if the
    directory is not empty.

    Parameters:
        path: Path to the directory (supports ~ expansion)

    Returns:
        file.REMOVED if the directory was deleted,
        file.ABSENT if the directory did not exist
    """
    ...
