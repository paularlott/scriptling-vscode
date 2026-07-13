"""
Scriptling shlex Library - Type stubs for IntelliSense support.

Shell-style lexical analysis — quoting, splitting, and joining command-line
tokens.
"""


def quote(s: str) -> str:
    """
    Escape a string for use as a single shell argument.

    Parameters:
        s  The string to escape

    Returns:
        A shell-safe string. Safe characters are returned unchanged; everything
        else is wrapped in single quotes.

    Example:
        import shlex
        shlex.quote("hello world")  # "'hello world'"
        shlex.quote("simple")       # "simple"
    """
    ...


def split(s: str) -> list[str]:
    """
    Split a string into shell-style tokens.

    Parses using shell rules: single quotes preserve everything literally,
    double quotes preserve everything except backslash before special chars,
    and backslash outside quotes escapes the next character.

    Parameters:
        s  The string to split

    Returns:
        List of parsed tokens.

    Raises:
        Error on unterminated quotes or trailing backslash.

    Example:
        import shlex
        shlex.split('cmd --flag="my value"')  # ["cmd", "--flag=my value"]
    """
    ...


def join(split_command: list[str]) -> str:
    """
    Join a list of arguments into a shell-quoted string.

    Each argument is individually quoted with quote() and joined with spaces.

    Parameters:
        split_command  The arguments to join

    Returns:
        A single shell-safe command-line string.

    Example:
        import shlex
        shlex.join(["ls", "-la", "My Documents"])  # "ls -la 'My Documents'"
    """
    ...
