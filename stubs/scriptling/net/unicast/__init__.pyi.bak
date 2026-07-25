"""
Scriptling Unicast Library - Type stubs for IntelliSense support.

UDP and TCP point-to-point messaging for direct host-to-host communication.

Example:
    import scriptling.net.unicast as uc

    # TCP client
    conn = uc.connect("192.168.1.1", 8080, protocol="tcp")
    conn.send("Hello!")
    msg = conn.receive(timeout=5)
    conn.close()

    # TCP server
    server = uc.listen("0.0.0.0", 8080)
    conn = server.accept(timeout=60)
    if conn:
        msg = conn.receive()
        conn.send("Echo: " + msg["data"])
        conn.close()
    server.close()
"""

from typing import Optional


class Connection:
    """
    Connection object returned by connect().

    Provides methods for sending and receiving messages.
    """

    def send(self, message: object) -> None:
        """
        Send a message to the remote peer.

        Parameters:
            message: Message to send. Strings sent as-is, dicts are
                     automatically JSON encoded.

        Example:
            conn.send("Hello!")
            conn.send({"action": "ping"})
        """
        ...

    def receive(self, timeout: float = 30) -> Optional[dict]:
        """
        Receive a message from the remote peer.

        Parameters:
            timeout: Timeout in seconds (default: 30)

        Returns:
            Dict with "data" and "source" keys, or None on timeout

        Example:
            msg = conn.receive(timeout=5)
            if msg:
                print(f"From {msg['source']}: {msg['data']}")
        """
        ...

    def close(self) -> None:
        """
        Close the connection.
        """
        ...

    def connected(self) -> bool:
        """
        Check if connection is still open.

        Returns:
            True if connected, False otherwise
        """
        ...

    local_addr: str
    """Local address of the connection."""

    remote_addr: str
    """Remote address of the connection."""


class UDPListener:
    """
    UDP listener object returned by listen(protocol="udp").

    Provides methods for receiving from any sender and replying.
    """

    def receive(self, timeout: float = 30) -> Optional[dict]:
        """
        Receive a message from any sender.

        Parameters:
            timeout: Timeout in seconds (default: 30)

        Returns:
            Dict with "data" and "source" keys, or None on timeout
        """
        ...

    def send_to(self, address: str, message: object) -> None:
        """
        Send a message to a specific address.

        Parameters:
            address: Target address (e.g., "192.168.1.1:8080")
            message: Message to send (string or dict)
        """
        ...

    def close(self) -> None:
        """
        Close the listener.
        """
        ...

    addr: str
    """Local address the listener is bound to."""


class TCPListener:
    """
    TCP listener object returned by listen(protocol="tcp").

    Provides methods for accepting incoming connections.
    """

    def accept(self, timeout: float = 30) -> Optional[Connection]:
        """
        Accept an incoming TCP connection.

        Parameters:
            timeout: Timeout in seconds (default: 30)

        Returns:
            TCP Connection object, or None on timeout

        Example:
            conn = server.accept(timeout=60)
            if conn:
                msg = conn.receive()
                conn.close()
        """
        ...

    def close(self) -> None:
        """
        Close the listener.
        """
        ...

    addr: str
    """Local address the listener is bound to."""


def connect(
    host: str,
    port: int,
    protocol: str = "udp",
    timeout: float = 10
) -> Connection:
    """
    Connect to a remote host.

    Parameters:
        host: Remote host address
        port: Remote port number
        protocol: "udp" or "tcp" (default: "udp")
        timeout: Connection timeout in seconds (default: 10)

    Returns:
        Connection object with send(), receive(), close(), connected()
        and local_addr, remote_addr properties

    Example:
        import scriptling.net.unicast as uc

        conn = uc.connect("192.168.1.1", 8080, protocol="tcp")
        conn.send("Hello!")
        msg = conn.receive(timeout=5)
        conn.close()
    """
    ...


def listen(
    host: str,
    port: int = 0,
    protocol: str = "tcp"
) -> object:
    """
    Listen for incoming connections.

    Parameters:
        host: Bind address (use "0.0.0.0" to bind all interfaces)
        port: Port number to listen on
        protocol: "udp" or "tcp" (default: "tcp")

    For TCP: returns a TCPListener with accept(), close(), addr
    For UDP: returns a UDPListener with receive(), send_to(), close(), addr

    Example:
        import scriptling.net.unicast as uc

        # TCP server
        server = uc.listen("0.0.0.0", 8080)
        conn = server.accept(timeout=60)
        if conn:
            msg = conn.receive()
            conn.send("Echo: " + msg["data"])
            conn.close()
        server.close()
    """
    ...
