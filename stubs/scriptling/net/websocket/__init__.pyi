"""
Scriptling WebSocket Client Library - Type stubs for IntelliSense support.

This library provides WebSocket client functionality to connect to WebSocket
servers and exchange messages.

Example:
    import scriptling.net.websocket as ws

    # Connect to a WebSocket server
    conn = ws.connect("ws://echo.websocket.org", timeout=5)

    # Send messages
    conn.send("Hello, World!")
    conn.send({"type": "json", "data": [1, 2, 3]})

    # Send binary data
    conn.send_binary([72, 101, 108, 108, 111])

    # Receive messages
    msg = conn.receive(timeout=10)

    # Close connection
    conn.close()
"""

from typing import Union, Optional, Any


class WebSocketMessage:
    """
    Base type for received WebSocket messages.

    Use is_text() and is_binary() helper functions to determine message type.
    """
    ...


class WebSocketClientConn:
    """
    WebSocket client connection object.

    Returned by connect() and provides methods to send and receive messages.

    Attributes:
        remote_addr: Remote address of the connected server
    """

    remote_addr: str

    def send(self, message: Union[str, dict[str, Any]]) -> Optional[Exception]:
        """
        Send a text message to the server.

        Parameters:
            message: Text string or dict (will be JSON-encoded)

        Returns:
            None on success, or an error/exception if send fails

        Example:
            conn.send("Hello, World!")
            conn.send({"type": "ping", "data": {"timestamp": 123456}})
        """
        ...

    def send_binary(self, data: list[int]) -> Optional[Exception]:
        """
        Send binary data to the server.

        Parameters:
            data: List of byte values (0-255)

        Returns:
            None on success, or an error/exception if send fails

        Example:
            conn.send_binary([72, 101, 108, 108, 111])  # "Hello" as bytes
        """
        ...

    def receive(self, timeout: float = 30) -> Optional[WebSocketMessage]:
        """
        Receive a message from the server.

        Parameters:
            timeout: Maximum time to wait for a message (seconds)

        Returns:
            The received message, or None if timeout or connection closed

        Example:
            msg = conn.receive(timeout=10)
            if msg:
                if is_text(msg):
                    print(f"Text: {msg}")
                elif is_binary(msg):
                    print(f"Binary: {list(msg)}")
        """
        ...

    def connected(self) -> bool:
        """
        Check if the connection is still open.

        Returns:
            True if connected, False otherwise
        """
        ...

    def close(self) -> None:
        """
        Close the WebSocket connection.
        """
        ...


def connect(
    url: str,
    timeout: float = 10,
    headers: Optional[dict[str, str]] = None
) -> WebSocketClientConn:
    """
    Connect to a WebSocket server.

    Parameters:
        url: WebSocket URL (ws:// or wss://)
        timeout: Connection timeout in seconds (default: 10)
        headers: Optional HTTP headers to send during handshake

    Returns:
        WebSocketClientConn object for sending/receiving messages

    Example:
        # Basic connection
        conn = ws.connect("ws://localhost:8080/chat")

        # With custom headers
        conn = ws.connect(
            "wss://api.example.com/ws",
            timeout=5,
            headers={"Authorization": "Bearer token123"}
        )
    """
    ...


def is_text(message: WebSocketMessage) -> bool:
    """
    Check if a received message is a text message.

    Parameters:
        message: Message received from receive()

    Returns:
        True if the message is text, False otherwise

    Example:
        msg = conn.receive()
        if msg and is_text(msg):
            print(f"Received text: {msg}")
    """
    ...


def is_binary(message: WebSocketMessage) -> bool:
    """
    Check if a received message is a binary message.

    Parameters:
        message: Message received from receive()

    Returns:
        True if the message is binary, False otherwise

    Example:
        msg = conn.receive()
        if msg and is_binary(msg):
            data = list(msg)  # Convert to list of bytes
            print(f"Received {len(data)} bytes")
    """
    ...


def send(conn: WebSocketClientConn, message: Union[str, dict[str, Any]]) -> None:
    """
    Send a message on a connection.

    Note: This is a module-level placeholder. It does not send anything and
    always raises an error ("send() requires a connection object - use
    ws.connect() first, then conn.send()"); use conn.send(message) instead.

    Parameters:
        conn: Connection returned by connect()
        message: Text string or dict (will be JSON-encoded)

    Raises:
        An error, always
    """
    ...


def send_binary(conn: WebSocketClientConn, data: list[int]) -> None:
    """
    Send binary data on a connection.

    Note: This is a module-level placeholder. It does not send anything and
    always raises an error; use conn.send_binary(data) instead.

    Parameters:
        conn: Connection returned by connect()
        data: List of byte values (0-255)

    Raises:
        An error, always
    """
    ...


def receive(conn: WebSocketClientConn, timeout: float = 30) -> Optional[WebSocketMessage]:
    """
    Receive a message from a connection.

    Note: This is a module-level placeholder. It does not receive anything and
    always raises an error; use conn.receive(timeout) instead.

    Parameters:
        conn: Connection returned by connect()
        timeout: Maximum time to wait for a message (seconds, default: 30)

    Raises:
        An error, always
    """
    ...


def connected(conn: WebSocketClientConn) -> bool:
    """
    Check if a connection is still open.

    Note: This is a module-level placeholder. It always raises an error; use
    conn.connected() instead.

    Parameters:
        conn: Connection returned by connect()

    Raises:
        An error, always
    """
    ...


def close(conn: WebSocketClientConn) -> None:
    """
    Close a connection.

    Note: This is a module-level placeholder. It does not close the connection
    and always raises an error; use conn.close() instead.

    Parameters:
        conn: Connection returned by connect()

    Raises:
        An error, always
    """
    ...
