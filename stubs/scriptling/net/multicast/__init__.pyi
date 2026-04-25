"""
Scriptling Multicast Library - Type stubs for IntelliSense support.

UDP multicast group messaging for one-to-many communication on local
networks.

Example:
    import scriptling.net.multicast as mc

    group = mc.join("239.1.1.1", 9999)
    group.send("Hello group!")
    msg = group.receive(timeout=5)
    if msg:
        print(f"From {msg['source']}: {msg['data']}")
    group.close()
"""

from typing import Optional


class ReceiveResult:
    """Result from receive() containing data and source address."""

    data: str
    """Received message data as string."""

    source: str
    """Source address of the sender."""


class MulticastGroup:
    """
    Multicast group object returned by join().

    Provides methods for sending and receiving messages within the group.
    """

    def send(self, message: object) -> None:
        """
        Send a message to the multicast group.

        Parameters:
            message: Message to send. Strings sent as-is, dicts are
                     automatically JSON encoded.

        Example:
            group.send("Hello group!")
            group.send({"type": "ping", "ts": 1234})
        """
        ...

    def receive(self, timeout: float = 30) -> Optional[ReceiveResult]:
        """
        Receive a message from the multicast group.

        Parameters:
            timeout: Timeout in seconds (default: 30)

        Returns:
            Dict with "data" and "source" keys, or None on timeout

        Example:
            msg = group.receive(timeout=5)
            if msg:
                print(f"From {msg['source']}: {msg['data']}")
        """
        ...

    def close(self) -> None:
        """
        Leave the multicast group and close the connection.

        Example:
            group.close()
        """
        ...

    group_addr: str
    """Multicast group address."""

    port: int
    """Multicast port number."""

    local_addr: str
    """Local bound address."""


def join(
    group_addr: str,
    port: int,
    interface: str = "",
    ttl: int = 1
) -> MulticastGroup:
    """
    Join a multicast group.

    Parameters:
        group_addr: Multicast group address (e.g., "239.1.1.1")
        port: Port number for the multicast group
        interface: Network interface to bind to (default: auto-select)
        ttl: Multicast TTL / hop limit (default: 1, local network only;
             increase to route across subnets)

    Returns:
        Group object with send(), receive(), close() methods
        and group_addr, port, local_addr properties

    Example:
        import scriptling.net.multicast as mc

        group = mc.join("239.1.1.1", 9999)
        group.send("Hello!")
        msg = group.receive(timeout=5)
        group.close()
    """
    ...
