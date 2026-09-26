"""
Scriptling json Library - Type stubs for IntelliSense support.

JSON encoding and decoding: parse JSON strings into Scriptling values and
serialize them back.
"""

from typing import Any, Union

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

def dumps(obj: Any, indent: Union[str, int, float] = None) -> str:
    """
    Serialize a Scriptling value to a JSON string.

    Object keys are always emitted in sorted order.

    Parameters:
        obj: The value to serialize (dicts, lists, strings, numbers,
             booleans, None).
        indent: Pretty-printing indentation. A string is used verbatim
            (indent="\\t"); a number gives that many spaces, with
            indent=2 the common idiom; indent=0 newline-separates with no
            spaces. Without it the output is fully compact.

    Example:
        json.dumps({"b": 1, "a": 2})             # '{"a":2,"b":1}'
        json.dumps({"a": [1, 2]}, indent=2)      # newlines, two-space indent
        json.dumps({"a": [1, 2]}, indent="  ")   # same, string indent verbatim
    """
    ...

def stringify(obj: Any, indent: Union[str, int, float] = None) -> str:
    """
    Serialize a Scriptling value to a JSON string (alias for dumps).

    Same parameters and behavior as dumps().
    """
    ...
