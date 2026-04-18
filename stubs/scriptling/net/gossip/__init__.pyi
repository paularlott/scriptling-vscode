"""
Scriptling Gossip Library - Type stubs for IntelliSense support.

Gossip protocol cluster membership and messaging with support for
automatic failure detection, metadata propagation, tag-based routing,
encryption, and compression.

Example:
    import scriptling.net.gossip as gossip

    cluster = gossip.create(
        bind_addr="127.0.0.1:8000",
        tags=["web"]
    )
    cluster.start()
    cluster.join(["127.0.0.1:8001"])
    cluster.handle(128, lambda msg: print(msg["payload"]))
    cluster.send(128, "Hello cluster!")
    cluster.stop()
"""

from typing import Optional, Callable, Any

# Constants
MSG_USER: int
"""Minimum user-defined message type (128)."""


class NodeDict:
    """Node information returned by node queries."""

    id: str
    """Node UUID string."""

    addr: str
    """Advertised address of the node."""

    state: str
    """Node state: 'alive', 'suspect', 'dead', or 'leaving'."""

    metadata: dict[str, str]
    """Node metadata key-value pairs."""


class MessageDict:
    """Message dict passed to message handlers."""

    type: int
    """Message type integer."""

    sender: NodeDict
    """Sender node information."""

    payload: Any
    """Decoded message payload."""


class Cluster:
    """
    Gossip cluster object returned by create().

    Provides methods for cluster membership, messaging, metadata,
    and state change monitoring.
    """

    def start(self) -> None:
        """
        Start the cluster node.

        Starts transport, health monitoring, and gossip routines.

        Example:
            cluster.start()
        """
        ...

    def join(self, peers: object) -> None:
        """
        Join an existing cluster by connecting to known peers.

        Parameters:
            peers: A single address string or list of address strings

        Example:
            cluster.join("127.0.0.1:8001")
            cluster.join(["127.0.0.1:8001", "127.0.0.1:8002"])
        """
        ...

    def leave(self) -> None:
        """
        Gracefully leave the cluster.

        Example:
            cluster.leave()
        """
        ...

    def stop(self) -> None:
        """
        Stop the cluster and clean up resources.

        Example:
            cluster.stop()
        """
        ...

    def send(
        self,
        message_type: int,
        data: object,
        reliable: bool = False
    ) -> None:
        """
        Broadcast a message to all cluster nodes.

        Parameters:
            message_type: Message type integer (must be >= 128)
            data: Message payload (string, int, float, list, dict)
            reliable: Use reliable TCP transport (default: False)

        Example:
            cluster.send(128, "Hello!")
            cluster.send(128, {"key": "value"}, reliable=True)
        """
        ...

    def send_tagged(
        self,
        tag: str,
        message_type: int,
        data: object,
        reliable: bool = False
    ) -> None:
        """
        Send a tagged message (only delivered to nodes with matching tag).

        Parameters:
            tag: Tag string for routing
            message_type: Message type integer (must be >= 128)
            data: Message payload
            reliable: Use reliable TCP transport (default: False)

        Example:
            cluster.send_tagged("web", 128, "Hello web nodes!")
        """
        ...

    def send_to(
        self,
        node_id: str,
        message_type: int,
        data: object,
        reliable: bool = False
    ) -> None:
        """
        Send a direct message to a specific node.

        Parameters:
            node_id: Target node UUID string
            message_type: Message type integer (must be >= 128)
            data: Message payload
            reliable: Use reliable TCP transport (default: False)

        Example:
            cluster.send_to("abc-123", 128, "Direct message!")
        """
        ...

    def handle(
        self,
        message_type: int,
        handler: Callable[[MessageDict], Any]
    ) -> None:
        """
        Register a message handler for a specific message type.

        Parameters:
            message_type: Message type to handle (must be >= 128)
            handler: Function called with message dict for each message

        The handler receives a dict with:
          - type: message type (int)
          - sender: dict with id, addr, state, metadata
          - payload: decoded message payload

        Example:
            def on_message(msg):
                print(f"From {msg['sender']['id']}: {msg['payload']}")

            cluster.handle(128, on_message)
        """
        ...

    def on_state_change(
        self,
        handler: Callable[[str, str], Any]
    ) -> None:
        """
        Register a node state change handler.

        Parameters:
            handler: Function called with (node_id, new_state)

        States: 'alive', 'suspect', 'dead', 'leaving'

        Example:
            def on_change(node_id, state):
                print(f"Node {node_id} is now {state}")

            cluster.on_state_change(on_change)
        """
        ...

    def nodes(self) -> list[NodeDict]:
        """
        Get all known nodes.

        Returns:
            List of node dicts with id, addr, state, metadata
        """
        ...

    def alive_nodes(self) -> list[NodeDict]:
        """
        Get all alive nodes.

        Returns:
            List of node dicts for nodes in 'alive' state
        """
        ...

    def local_node(self) -> NodeDict:
        """
        Get the local node info.

        Returns:
            Node dict with id, addr, state, metadata
        """
        ...

    def num_nodes(self) -> int:
        """
        Get total number of known nodes.
        """
        ...

    def num_alive(self) -> int:
        """
        Get number of alive nodes.
        """
        ...

    def set_metadata(self, key: str, value: object) -> None:
        """
        Set local node metadata (automatically gossiped to other nodes).

        Parameters:
            key: Metadata key string
            value: Metadata value (string, int, float, or bool)

        Example:
            cluster.set_metadata("role", "worker")
            cluster.set_metadata("version", 2)
        """
        ...

    def get_metadata(self, key: str) -> Optional[str]:
        """
        Get local node metadata value.

        Parameters:
            key: Metadata key string

        Returns:
            The metadata value as a string, or None if not found
        """
        ...

    def all_metadata(self) -> dict[str, str]:
        """
        Get all local node metadata.

        Returns:
            Dict of all metadata key-value pairs
        """
        ...

    def delete_metadata(self, key: str) -> None:
        """
        Delete a metadata key.

        Parameters:
            key: Metadata key to delete
        """
        ...

    def node_id(self) -> str:
        """
        Get the local node's unique ID.

        Returns:
            Node UUID string
        """
        ...


def create(
    bind_addr: str = "127.0.0.1:8000",
    node_id: str = "",
    advertise_addr: str = "",
    encryption_key: str = "",
    tags: Optional[list[str]] = None,
    compression: bool = False,
    bearer_token: str = "",
    app_version: str = ""
) -> Cluster:
    """
    Create a gossip cluster node.

    Parameters:
        bind_addr: Address to bind to (default: "127.0.0.1:8000")
        node_id: Unique node ID (auto-generated if empty)
        advertise_addr: Address to advertise to peers (default: same as bind_addr)
        encryption_key: Encryption key (16, 24, or 32 bytes for AES)
        tags: Tags for tag-based message routing
        compression: Enable Snappy compression (default: False)
        bearer_token: Authentication bearer token
        app_version: Application version for compatibility checks

    Returns:
        Cluster object with methods for membership and messaging

    Example:
        import scriptling.net.gossip as gossip

        cluster = gossip.create(
            bind_addr="127.0.0.1:8000",
            tags=["web"]
        )
        cluster.start()
        cluster.join(["127.0.0.1:8001"])
        cluster.handle(128, lambda msg: print(msg))
        cluster.send(128, "Hello!")
        cluster.stop()
    """
    ...


def decode_json(json_string: str) -> Any:
    """
    Decode a JSON string to a scriptling value.

    Parameters:
        json_string: JSON string to decode

    Returns:
        Decoded value (dict, list, string, int, float, bool, or None)
    """
    ...
