"""
Scriptling Package Library - Type stubs for IntelliSense support.

Read-only access to files inside loaded packages (app bundles and library
bundles). Available when running via --package. Every function takes the
package name (from manifest.toml) as its first argument.
"""

from typing import Optional


def names() -> list[str]:
    """
    List all loaded package names.

    Returns:
        list of str: The manifest name of each loaded package.
    """
    ...


def version(name: str) -> str:
    """
    Get the version of a loaded package.

    Parameters:
        name: Package name from manifest.toml.

    Returns:
        Version string (e.g. "1.0.0").
    """
    ...


def exists(name: str) -> bool:
    """
    Check if a package is loaded.

    Parameters:
        name: Package name from manifest.toml.

    Returns:
        True if the package is loaded.
    """
    ...


def file_exists(name: str, path: str) -> bool:
    """
    Check if a file exists in a package.

    Parameters:
        name: Package name from manifest.toml.
        path: File path relative to the package root.

    Returns:
        True if the file exists in the package.
    """
    ...


def read_file(name: str, path: str) -> str:
    """
    Read a file from a package.

    Parameters:
        name: Package name from manifest.toml.
        path: File path relative to the package root.

    Returns:
        File contents as a string. Use read_bytes() for binary files.

    Example:
        import scriptling.package as package
        spec = package.read_file("myapp", "data/spec.md")
    """
    ...


def read_bytes(name: str, path: str) -> bytes:
    """
    Read a file from a package as bytes (preserves binary data).

    Parameters:
        name: Package name from manifest.toml.
        path: File path relative to the package root.

    Returns:
        File contents as bytes.

    Example:
        import scriptling.package as package
        import msgpack
        data = msgpack.unpackb(package.read_bytes("myapp", "data/payload.msgpack"))
    """
    ...


def list(name: str, path: str) -> list[str]:
    """
    List files in a directory within a package.

    Parameters:
        name: Package name from manifest.toml.
        path: Directory path relative to the package root ("." for root).

    Returns:
        list of str: File and directory names (directories end with /).
    """
    ...


def glob(name: str, pattern: str) -> list[str]:
    """
    Find files matching a glob pattern in a package.

    Parameters:
        name: Package name from manifest.toml.
        pattern: Glob pattern (* and ? wildcards, ** for recursive).

    Returns:
        list of str: Matching file paths relative to the package root.

    Example:
        import scriptling.package as package
        py_files = package.glob("myapp", "**/*.py")
    """
    ...
