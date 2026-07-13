"""
Scriptling XML Library - Type stubs for IntelliSense support.

XML parsing and formatting (dict-based, string-only).
"""


def loads(content: str) -> dict:
    """
    Parse an XML string into a nested dict.

    Element tags become dict keys, attributes become @-prefixed keys,
    repeated elements become lists, and text alongside attributes/children
    uses #text.

    Parameters:
        content  XML text to parse

    Returns:
        Nested dict representing the XML document.
    """
    ...


def dumps(data: dict, *, indent: str = "") -> str:
    """
    Format a dict into an XML string.

    The dict should have a single root key. Keys prefixed with "@" become
    attributes, "#text" becomes text content, and list values produce
    repeated elements.

    Parameters:
        data    Dict with a single root element key
        indent  Indentation string (default "" = compact)

    Returns:
        XML-formatted text.
    """
    ...
