"""
Scriptling MCP Tool Library - Type stubs for IntelliSense support.

MCP tool parameter access and result functions for building
MCP (Model Context Protocol) tool handlers.
"""

from typing import Optional, Any

# Parameter getters
def get_int(name: str, default: int = 0) -> int:
    """
    Get a parameter as integer.

    Safely gets a parameter and converts it to an integer, handling None,
    empty strings, and whitespace. Returns the default value if the parameter
    doesn't exist, is None, empty, or whitespace-only.

    Parameters:
        name: The parameter name
        default: Default value (optional, defaults to 0)

    Example:
        project_id = mcp.tool.get_int("project_id", 0)
        limit = mcp.tool.get_int("limit", 100)
    """
    ...

def get_float(name: str, default: float = 0.0) -> float:
    """
    Get a parameter as float.

    Safely gets a parameter and converts it to a float, handling None,
    empty strings, and whitespace. Returns the default value if the parameter
    doesn't exist, is None, empty, or whitespace-only.

    Parameters:
        name: The parameter name
        default: Default value (optional, defaults to 0.0)

    Example:
        price = mcp.tool.get_float("price", 0.0)
        percentage = mcp.tool.get_float("percentage", 100.0)
    """
    ...

def get_string(name: str, default: str = "") -> str:
    """
    Get a parameter as string.

    Safely gets a parameter as a string, handling None, empty strings, and
    whitespace. Trims whitespace and returns the default value if the parameter
    doesn't exist, is None, empty, or whitespace-only.

    Parameters:
        name: The parameter name
        default: Default value (optional, defaults to "")

    Example:
        name = mcp.tool.get_string("name", "guest")
        query = mcp.tool.get_string("query")
    """
    ...

def get_bool(name: str, default: bool = False) -> bool:
    """
    Get a parameter as boolean.

    Safely gets a parameter and converts it to a boolean. Handles string
    values "true"/"false" (case-insensitive) and numeric 0/1. Returns the
    default value if the parameter doesn't exist or cannot be converted.

    Parameters:
        name: The parameter name
        default: Default value (optional, defaults to false)

    Example:
        enabled = mcp.tool.get_bool("enabled", true)
        verbose = mcp.tool.get_bool("verbose")
    """
    ...

def get_list(name: str, default: Optional[list[Any]] = None) -> list[Any]:
    """
    Get a parameter as list.

    Gets a list parameter. If the value is a string, splits it by comma.
    Returns the default value if the parameter doesn't exist.

    Parameters:
        name: The parameter name
        default: Default value (optional, defaults to empty list)

    Example:
        ids = mcp.tool.get_list("ids")              # "1,2,3" -> ["1", "2", "3"]
        tags = mcp.tool.get_list("tags", ["all"])   # "tag1, tag2" -> ["tag1", "tag2"]
    """
    ...

def get_string_list(name: str, default: Optional[list[str]] = None) -> list[str]:
    """
    Get a string array parameter.

    Gets an array:string parameter as a list of strings.
    Returns the default value if the parameter doesn't exist.

    Parameters:
        name: The parameter name
        default: Default value (optional, defaults to empty list)

    Example:
        args = mcp.tool.get_string_list("arguments")  # ["--verbose", "-o", "file.txt"]
        tags = mcp.tool.get_string_list("tags", ["default"])
    """
    ...

def get_int_list(name: str, default: Optional[list[int]] = None) -> list[int]:
    """
    Get an integer array parameter.

    Gets an array:int parameter as a list of integers.
    Returns the default value if the parameter doesn't exist.

    Parameters:
        name: The parameter name
        default: Default value (optional, defaults to empty list)

    Example:
        ids = mcp.tool.get_int_list("ids")  # [1, 2, 3, 4]
        ports = mcp.tool.get_int_list("ports", [8080])
    """
    ...

def get_float_list(name: str, default: Optional[list[float]] = None) -> list[float]:
    """
    Get a float array parameter.

    Gets an array:float parameter as a list of floats.
    Returns the default value if the parameter doesn't exist.

    Parameters:
        name: The parameter name
        default: Default value (optional, defaults to empty list)

    Example:
        prices = mcp.tool.get_float_list("prices")  # [19.99, 29.99, 39.99]
        weights = mcp.tool.get_float_list("weights", [1.0])
    """
    ...

def get_bool_list(name: str, default: Optional[list[bool]] = None) -> list[bool]:
    """
    Get a boolean array parameter.

    Gets an array:bool parameter as a list of booleans.
    Returns the default value if the parameter doesn't exist.

    Parameters:
        name: The parameter name
        default: Default value (optional, defaults to empty list)

    Example:
        flags = mcp.tool.get_bool_list("flags")  # [true, false, true]
        options = mcp.tool.get_bool_list("options", [false])
    """
    ...

# Result functions
def return_string(text: str) -> None:
    """
    Return a string result from the tool and stop execution.

    Sets the tool's return value to the given string and stops script execution.
    No code after this call will execute.

    Parameters:
        text: The string to return

    Example:
        mcp.tool.return_string("Search completed successfully")
        # Code here will not execute
    """
    ...

def return_object(obj: Any) -> None:
    """
    Return an object as JSON from the tool and stop execution.

    Serializes the object to JSON and sets it as the tool's return value.
    Stops script execution immediately - no code after this call will execute.

    Parameters:
        obj: The object to serialize as JSON

    Example:
        mcp.tool.return_object({"status": "success", "count": 42})
        # Code here will not execute
    """
    ...

def return_toon(obj: Any) -> None:
    """
    Return an object encoded as TOON from the tool and stop execution.

    Serializes the object to TOON format and sets it as the tool's return value.
    TOON is a compact text format optimized for LLM consumption.
    Stops script execution immediately - no code after this call will execute.

    Parameters:
        obj: The object to encode as TOON

    Example:
        mcp.tool.return_toon({"result": data})
        # Code here will not execute
    """
    ...

def return_error(message: str) -> None:
    """
    Return an error from the tool and stop execution.

    Returns an error message to the MCP client and stops script execution immediately.

    Parameters:
        message: The error message

    Example:
        mcp.tool.return_error("Customer not found")
        mcp.tool.return_error("Invalid input: project ID is required")
    """
    ...
