"""
Scriptling Gossip Library - Type stubs for IntelliSense support.

Gossip protocol cluster membership and messaging with support for
automatic failure detection, metadata propagation, tag-based routing,
encryption, compression, leader election, and node groups.

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

    tags: list[str]
    """Node tags for routing."""


class MessageDict:
    """Message dict passed to message handlers."""

    type: int
    """Message type integer."""

    sender: NodeDict
    """Sender node information."""

    payload: Any
    """Decoded message payload."""


class NodeGroup:
    """
    Metadata-criteria-based node group.

    Created by cluster.create_node_group(). Automatically tracks nodes
    whose metadata matches the specified criteria.
    """

    def nodes(self) -> list[NodeDict]:
        """
        Get all nodes currently in this group.

        Returns:
            List of node dicts matching the group criteria
        """
        ...

    def contains(self, node_id: str) -> bool:
        """
        Check if a node is in this group.

        Parameters:
            node_id: Node UUID to check

        Returns:
            True if the node is in the group
        """
        ...

    def count(self) -> int:
        """
        Get number of nodes in this group.

        Returns:
            Number of matching nodes
        """
        ...

    def send_to_peers(
        self,
        message_type: int,
        data: object,
        reliable: bool = False
    ) -> None:
        """
        Send a message to all peers in the group.

        Parameters:
            message_type: Message type (must be >= 128)
            data: Message payload
            reliable: Use reliable transport (default: False)
        """
        ...

    def close(self) -> None:
        """
        Close the node group and release resources.
        """
        ...


class LeaderElection:
    """
    Leader election manager.

    Created by cluster.create_leader_election(). Provides quorum-based
    leader election with optional metadata filtering.
    """

    def start(self) -> None:
        """
        Start the leader election process.
        """
        ...

    def stop(self) -> None:
        """
        Stop the leader election process.
        """
        ...

    def is_leader(self) -> bool:
        """
        Check if this node is the current leader.

        Returns:
            True if this node is the leader
        """
        ...

    def has_leader(self) -> bool:
        """
        Check if a leader is currently elected.

        Returns:
            True if any node is the leader
        """
        ...

    def get_leader_id(self) -> Optional[str]:
        """
        Get the current leader's node ID.

        Returns:
            Leader node UUID, or None if no leader
        """
        ...

    def send_to_peers(
        self,
        message_type: int,
        data: object,
        reliable: bool = False
    ) -> None:
        """
        Send a message to eligible leader election peers.

        Parameters:
            message_type: Message type (must be >= 128)
            data: Message payload
            reliable: Use reliable transport (default: False)
        """
        ...

    def on_event(
        self,
        event_type: str,
        handler: Callable[[str, str], Any]
    ) -> None:
        """
        Register a leader election event handler.

        Parameters:
            event_type: One of "elected", "lost", "became_leader", "stepped_down"
            handler: Function(event_type, node_id) called on event

        Example:
            def on_leader_change(event, node_id):
                if event == "became_leader":
                    print("I am now the leader!")

            election.on_event("became_leader", on_leader_change)
        """
        ...


class Cluster:
    """
    Gossip cluster object returned by create().

    Provides methods for cluster membership, messaging, metadata,
    node groups, leader election, and state monitoring.
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

    def send_request(
        self,
        node_id: str,
        message_type: int,
        data: object
    ) -> Any:
        """
        Send a request to a specific node and wait for a reply.

        Parameters:
            node_id: Target node UUID string
            message_type: Message type integer (must be >= 128)
            data: Message payload

        Returns:
            The reply payload from the target node

        Example:
            reply = cluster.send_request(target_id, 128, {"cmd": "ping"})
            print(reply)
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
          - sender: dict with id, addr, state, metadata, tags
          - payload: decoded message payload

        Example:
            def on_message(msg):
                print(f"From {msg['sender']['id']}: {msg['payload']}")

            cluster.handle(128, on_message)
        """
        ...

    def handle_with_reply(
        self,
        message_type: int,
        handler: Callable[[MessageDict], Any]
    ) -> None:
        """
        Register a request/reply message handler.

        Parameters:
            message_type: Message type to handle (must be >= 128)
            handler: Function called with message dict, must return reply data

        The handler receives the same dict as handle() and must return the reply.

        Example:
            def on_request(msg):
                return {"status": "ok", "echo": msg["payload"]}

            cluster.handle_with_reply(128, on_request)
        """
        ...

    def unhandle(self, message_type: int) -> bool:
        """
        Remove a previously registered message handler.

        Parameters:
            message_type: Message type to unregister (must be >= 128)

        Returns:
            True if a handler was removed, False otherwise

        Example:
            cluster.unhandle(128)
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

    def on_metadata_change(
        self,
        handler: Callable[[NodeDict], Any]
    ) -> None:
        """
        Register a handler for remote node metadata changes.

        Parameters:
            handler: Function called with node dict when any node's metadata changes

        Example:
            def on_meta(node):
                print(f"Node {node['id']} metadata changed: {node['metadata']}")

            cluster.on_metadata_change(on_meta)
        """
        ...

    def on_gossip_interval(
        self,
        handler: Callable[[], Any]
    ) -> None:
        """
        Register a periodic handler called every gossip interval.

        Parameters:
            handler: Function called at each gossip interval

        Example:
            def on_tick():
                print("gossip tick")

            cluster.on_gossip_interval(on_tick)
        """
        ...

    def create_node_group(
        self,
        criteria: dict[str, str],
        on_node_added: Optional[Callable[[NodeDict], Any]] = None,
        on_node_removed: Optional[Callable[[NodeDict], Any]] = None
    ) -> NodeGroup:
        """
        Create a metadata-criteria-based node group.

        Parameters:
            criteria: Metadata key-value pairs to match ("*" for any, "~value" for contains)
            on_node_added: Optional callback when a node joins the group
            on_node_removed: Optional callback when a node leaves the group

        Returns:
            NodeGroup object with nodes(), contains(), count(), send_to_peers(), close()

        Example:
            workers = cluster.create_node_group(criteria={"role": "worker"})
            print(f"Worker count: {workers.count()}")
            workers.send_to_peers(128, {"task": "process"})
        """
        ...

    def create_leader_election(
        self,
        check_interval: str = "1s",
        leader_timeout: str = "3s",
        heartbeat_msg_type: int = 65,
        quorum_percentage: int = 60,
        metadata_criteria: Optional[dict[str, str]] = None
    ) -> LeaderElection:
        """
        Create a leader election manager.

        Parameters:
            check_interval: Duration between leader checks (default: "1s")
            leader_timeout: Duration without heartbeat before leader lost (default: "3s")
            heartbeat_msg_type: Message type for heartbeats (default: 65)
            quorum_percentage: Percentage of nodes for quorum 1-100 (default: 60)
            metadata_criteria: Optional metadata to limit eligible nodes

        Returns:
            LeaderElection object with start(), stop(), is_leader(), has_leader(),
            get_leader_id(), on_event()

        Example:
            election = cluster.create_leader_election()
            election.on_event("became_leader", lambda e, n: print("I'm leader!"))
            election.start()
        """
        ...

    def nodes(self) -> list[NodeDict]:
        """
        Get all known nodes.

        Returns:
            List of node dicts with id, addr, state, metadata, tags
        """
        ...

    def alive_nodes(self) -> list[NodeDict]:
        """
        Get all alive nodes.

        Returns:
            List of node dicts for nodes in 'alive' state
        """
        ...

    def nodes_by_tag(self, tag: str) -> list[NodeDict]:
        """
        Get all nodes that have a specific tag.

        Parameters:
            tag: Tag to filter by

        Returns:
            List of node dicts with the matching tag
        """
        ...

    def get_node(self, node_id: str) -> Optional[NodeDict]:
        """
        Get a specific node by ID.

        Parameters:
            node_id: Node UUID string

        Returns:
            Node dict, or None if not found
        """
        ...

    def local_node(self) -> NodeDict:
        """
        Get the local node info.

        Returns:
            Node dict with id, addr, state, metadata, tags
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

    def num_suspect(self) -> int:
        """
        Get number of suspect nodes.
        """
        ...

    def num_dead(self) -> int:
        """
        Get number of dead nodes.
        """
        ...

    def is_local(self, node_id: str) -> bool:
        """
        Check if a node ID refers to the local node.

        Parameters:
            node_id: Node UUID to check

        Returns:
            True if the node ID is the local node
        """
        ...

    def candidates(self) -> list[NodeDict]:
        """
        Get a random subset of nodes for gossiping.

        Returns:
            List of node dicts
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
    app_version: str = "",
    transport: str = "socket",
    compress_min_size: int = 256,
    gossip_interval: str = "5s",
    gossip_max_interval: str = "20s",
    metadata_gossip_interval: str = "500ms",
    state_gossip_interval: str = "45s",
    fan_out_multiplier: float = 1.0,
    ttl_multiplier: float = 1.0,
    state_exchange_multiplier: float = 0.8,
    force_reliable_transport: bool = False,
    prefer_ipv6: bool = False,
    node_cleanup_interval: str = "20s",
    node_retention_time: str = "1h",
    leaving_node_timeout: str = "30s",
    health_check_interval: str = "2s",
    suspect_timeout: str = "1.5s",
    suspect_retry_interval: str = "1s",
    dead_node_timeout: str = "15s",
    peer_recovery_interval: str = "30s",
    insecure_skip_verify: bool = False
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
        transport: Transport type: "socket" or "http" (default: "socket")
        compress_min_size: Min message size for compression (default: 256)
        gossip_interval: Gossip interval duration (default: "5s")
        gossip_max_interval: Max gossip interval (default: "20s")
        metadata_gossip_interval: Metadata gossip interval (default: "500ms")
        state_gossip_interval: State exchange interval (default: "45s")
        fan_out_multiplier: Fan-out scaling factor (default: 1.0)
        ttl_multiplier: TTL scaling factor (default: 1.0)
        state_exchange_multiplier: State exchange scaling (default: 0.8)
        force_reliable_transport: Force TCP for all messages (default: False)
        prefer_ipv6: Prefer IPv6 for DNS resolution (default: False)
        node_cleanup_interval: Dead node cleanup interval (default: "20s")
        node_retention_time: How long to keep dead nodes (default: "1h")
        leaving_node_timeout: Timeout before moving leaving->dead (default: "30s")
        health_check_interval: Health check interval (default: "2s")
        suspect_timeout: Time before marking node suspect (default: "1.5s")
        suspect_retry_interval: Suspect node retry interval (default: "1s")
        dead_node_timeout: Time before marking suspect->dead (default: "15s")
        peer_recovery_interval: Peer recovery check interval (default: "30s")
        insecure_skip_verify: Skip TLS verification for HTTP (default: False)

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

