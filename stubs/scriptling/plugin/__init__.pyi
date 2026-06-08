"""
Scriptling plugin control library stubs.
"""

from typing import Any


def list() -> list[dict[str, Any]]:
    """Return metadata for loaded plugins."""
    ...


def describe(name: str) -> dict[str, Any]:
    """Return metadata for one loaded plugin."""
    ...


def call_function(library: str, name: str, *args: Any, **kwargs: Any) -> Any:
    """Call a function exposed by a loaded plugin."""
    ...


def call_method(obj: Any, name: str, *args: Any, **kwargs: Any) -> Any:
    """Call a method on a remote plugin object."""
    ...


def _new_object(library: str, class_name: str, *args: Any, **kwargs: Any) -> Any:
    """Internal: construct a remote plugin object. Used by generated wrappers."""
    ...


def release(obj: Any) -> None:
    """Explicitly release a remote plugin object."""
    ...
