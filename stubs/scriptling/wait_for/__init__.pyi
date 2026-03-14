"""
Wait For Library - Type stubs for IntelliSense support.

Wait for resources to become available with configurable timeouts
and polling rates.
"""

def file(path: str, timeout: int = 30, poll_rate: float = 1.0) -> bool:
    """
    Wait for a file to exist.

    Waits for the specified file to become available.

    Parameters:
        path: Path to the file to wait for
        timeout: Maximum time to wait in seconds (default: 30)
        poll_rate: Time between checks in seconds (default: 1)

    Returns:
        True if file exists, False if timeout exceeded
    """
    ...

def dir(path: str, timeout: int = 30, poll_rate: float = 1.0) -> bool:
    """
    Wait for a directory to exist.

    Waits for the specified directory to become available.

    Parameters:
        path: Path to the directory to wait for
        timeout: Maximum time to wait in seconds (default: 30)
        poll_rate: Time between checks in seconds (default: 1)

    Returns:
        True if directory exists, False if timeout exceeded
    """
    ...

def port(host: str, port: int, timeout: int = 30, poll_rate: float = 1.0) -> bool:
    """
    Wait for a TCP port to be open.

    Waits for the specified TCP port to accept connections.

    Parameters:
        host: Hostname or IP address
        port: Port number (int or string)
        timeout: Maximum time to wait in seconds (default: 30)
        poll_rate: Time between checks in seconds (default: 1)

    Returns:
        True if port is open, False if timeout exceeded
    """
    ...

def http(url: str, timeout: int = 30, poll_rate: float = 1.0, status_code: int = 200) -> bool:
    """
    Wait for HTTP endpoint.

    Waits for the specified HTTP endpoint to respond with the expected status code.

    Parameters:
        url: URL to check
        timeout: Maximum time to wait in seconds (default: 30)
        poll_rate: Time between checks in seconds (default: 1)
        status_code: Expected HTTP status code (default: 200)

    Returns:
        True if endpoint responds with expected status, False if timeout exceeded
    """
    ...

def file_content(path: str, content: str, timeout: int = 30, poll_rate: float = 1.0) -> bool:
    """
    Wait for file to contain content.

    Waits for the specified file to exist and contain the given content.

    Parameters:
        path: Path to the file to check
        content: Content to search for in the file
        timeout: Maximum time to wait in seconds (default: 30)
        poll_rate: Time between checks in seconds (default: 1)

    Returns:
        True if file contains the content, False if timeout exceeded
    """
    ...

def process_name(name: str, timeout: int = 30, poll_rate: float = 1.0) -> bool:
    """
    Wait for a process to be running.

    Waits for a process with the specified name to be running.

    Parameters:
        name: Process name to search for
        timeout: Maximum time to wait in seconds (default: 30)
        poll_rate: Time between checks in seconds (default: 1)

    Returns:
        True if process is running, False if timeout exceeded
    """
    ...
