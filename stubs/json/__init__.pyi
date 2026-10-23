"""
Scriptling json Library - Type stubs for IntelliSense support.

JSON encoding and decoding: parse JSON strings into Scriptling values and
serialize them back.
"""

from typing import Any, Optional, Union

class JSONDecodeError(ValueError):
    """Raised by loads() on malformed JSON; subclasses ValueError, as in Python."""
    ...

def loads(json_string: str) -> Any:
    """
    Parse a JSON string into Scriptling values.

    Objects become dicts, arrays become lists, numbers become integers or
    floats, and true/false/null become True/False/None.

    Example:
        data = json.loads('{"count": 42}')
        print(data["count"])  # 42
    """
    ...

def parse(json_string: str) -> Any:
    """
    Parse a JSON string (alias for loads).

    Example:
        data = json.parse("[1, 2, 3]")
    """
    ...

def dumps(
    obj: Any,
    indent: Union[str, int, float] = None,
    separators: Optional[tuple[str, str]] = None,
    sort_keys: bool = False,
    ensure_ascii: bool = True
) -> str:
    """
    Serialize a Scriptling value to a JSON string.

    Dict keys are emitted in the dict's insertion order, as in Python;
    sort_keys=True sorts them.

    Parameters:
        obj: The value to serialize (dicts, lists, strings, numbers,
             booleans, None).
        indent: Pretty-printing indentation. A string is used verbatim
            (indent="\\t"); a number gives that many spaces, with
            indent=2 the common idiom; indent=0 newline-separates with no
            spaces. Without it the output is on one line.
        separators: An (item_separator, key_separator) pair (tuple or list).
            Defaults to (", ", ": "), or (",", ": ") when indent is given;
            pass (",", ":") for compact output.
        sort_keys: If True, emit dict keys in sorted order (default False).
        ensure_ascii: If True (default), escape non-ASCII characters as
            \\uXXXX; pass False to emit them as-is.

    Example:
        json.dumps({"b": 1, "a": 2})                         # '{"b": 1, "a": 2}'
        json.dumps({"b": 1, "a": 2}, sort_keys=True)         # '{"a": 2, "b": 1}'
        json.dumps({"a": [1, 2]}, separators=(",", ":"))     # '{"a":[1,2]}'
        json.dumps({"a": "é"}, ensure_ascii=False)           # '{"a": "é"}'
        json.dumps({"a": [1, 2]}, indent=2)                  # newlines, two-space indent
        json.dumps({"a": [1, 2]}, indent="  ")               # same, string indent verbatim
    """
    ...

def stringify(
    obj: Any,
    indent: Union[str, int, float] = None,
    separators: Optional[tuple[str, str]] = None,
    sort_keys: bool = False,
    ensure_ascii: bool = True
) -> str:
    """
    Serialize a Scriptling value to a JSON string (alias for dumps).

    Same parameters and behavior as dumps().
    """
    ...
