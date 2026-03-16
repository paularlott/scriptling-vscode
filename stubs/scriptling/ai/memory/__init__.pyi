"""
Scriptling AI Memory Library - Type stubs for IntelliSense support.

This library provides long-term memory storage for AI agents backed by
a key-value store. It supports semantic similarity search, automatic
deduplication, and optional LLM-based compaction.

Example:
    import scriptling.runtime.kv as kv
    import scriptling.ai.memory as memory
    import scriptling.ai as ai

    # Basic usage
    mem = memory.new(kv.default)
    mem.remember("User's name is Alice", type="fact", importance=0.9)
    results = mem.recall("Alice")

    # With LLM compaction (Mode 2)
    client = ai.Client("http://127.0.0.1:1234/v1")
    mem = memory.new(kv.default, ai_client=client, model="qwen3-8b")
"""

from typing import Literal, Optional, Any
from typing_extensions import TypedDict

# Memory type constants
TYPE_FACT: str
TYPE_PREFERENCE: str
TYPE_EVENT: str
TYPE_NOTE: str

# Memory type alias
MemoryType = Literal["fact", "preference", "event", "note"]


class Memory(TypedDict):
    """A single stored memory entry."""

    id: str
    """Unique identifier (UUIDv7)"""

    content: str
    """The memory content"""

    type: MemoryType
    """Memory type: fact, preference, event, or note"""

    importance: float
    """Importance score (0.0-1.0)"""

    created_at: str
    """ISO 8601 timestamp when memory was created"""

    accessed_at: str
    """ISO 8601 timestamp when memory was last accessed"""


class MemoryStore:
    """
    Memory store object for storing and recalling memories.

    Created by calling memory.new() with a kv store.
    """

    def remember(
        self,
        content: str,
        type: MemoryType = "note",
        importance: float = 0.5
    ) -> Memory:
        """
        Store a memory for later recall.

        Parameters:
            content: What to remember (should be a single concise sentence)
            type: Memory type - "fact", "preference", "event", or "note" (default: "note")
            importance: Importance score 0.0-1.0 (default: 0.5)
                       Use 0.9 for critical facts, 0.5 for general notes

        Returns:
            The stored memory dict with id, content, type, importance, created_at, accessed_at

        Example:
            mem.remember("User prefers dark mode", type="preference", importance=0.7)
            mem.remember("Meeting scheduled for Friday", type="event", importance=0.8)
        """
        ...

    def recall(
        self,
        query: str = "",
        limit: int = 10,
        type: str = ""
    ) -> list[Memory]:
        """
        Search memories by keyword and semantic similarity.

        Parameters:
            query: Keyword search query. Empty string with no type filter triggers
                   context load mode (all preferences + top limit non-preferences)
            limit: Maximum results for non-preference memories in context load,
                   or total results when querying (default: 10, use -1 for unlimited)
            type: Filter by type: "fact", "preference", "event", "note", or
                  "!type" to exclude (e.g., "!preference" excludes preferences).
                  Setting this disables context load mode.

        Returns:
            List of matching memory dicts ranked by relevance

        Example:
            # Context load at start of conversation
            context = mem.recall()

            # Search for specific memories
            results = mem.recall("project deadline", limit=5)

            # Get all preferences
            prefs = mem.recall("", limit=-1, type="preference")

            # Get non-preferences
            other = mem.recall("", limit=20, type="!preference")
        """
        ...

    def forget(self, id: str) -> bool:
        """
        Remove a memory by ID.

        Parameters:
            id: Memory ID returned by remember()

        Returns:
            True if a memory was removed, False otherwise
        """
        ...

    def count(self) -> int:
        """
        Return the total number of stored memories.

        Returns:
            Count of all stored memories
        """
        ...

    def compact(self) -> dict[str, int]:
        """
        Manually trigger compaction (prune + deduplicate).

        Returns:
            Dict with "removed" and "remaining" counts
        """
        ...


def new(
    kv_store: Any,
    ai_client: Optional[Any] = None,
    model: str = ""
) -> MemoryStore:
    """
    Create a memory store backed by a kv store.

    Parameters:
        kv_store: A kv store object (e.g., kv.default or kv.open(...))
        ai_client: Optional ai.Client instance to enable Mode 2 LLM compaction.
                   When provided, the LLM can merge similar memories during
                   remember() and compact() operations.
        model: Model name to use for LLM compaction (required if ai_client provided)

    Returns:
        Memory store object with remember, recall, forget, list, count, compact methods

    Example:
        import scriptling.runtime.kv as kv
        import scriptling.ai.memory as memory
        import scriptling.ai as ai

        # Basic memory (Mode 1 - rule-based only)
        mem = memory.new(kv.default)

        # With LLM compaction (Mode 2)
        client = ai.Client("http://127.0.0.1:1234/v1")
        mem = memory.new(kv.default, ai_client=client, model="qwen3-8b")

        # Disable Mode 2 explicitly
        mem = memory.new(kv.default, ai_client=None)
    """
    ...
