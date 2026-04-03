"""
Scriptling Similarity Library - Type stubs for IntelliSense support.

This library provides string matching and similarity utilities including
fuzzy search and MinHash for approximate set similarity.
"""

from typing import Optional, Any, Union

def search(
    query: str,
    items: list[Union[str, dict[str, Any]]],
    *,
    max_results: int = 5,
    threshold: float = 0.5,
    key: str = "name"
) -> list[dict[str, Any]]:
    """
    Search for fuzzy matches in a list of items.

    Uses a multi-tier algorithm (exact → substring → word boundary →
    Levenshtein distance).

    Parameters:
        query: The search query string
        items: List of items to search. Each item can be:
               - A string (id will be index)
               - A dict with 'id' and 'name' keys (or keys specified by 'key' param)
        max_results: Maximum results to return. Default: 5
        threshold: Minimum similarity threshold (0.0-1.0). Default: 0.5
        key: Key to use for item name in dicts. Default: "name"

    Returns:
        List of match dictionaries, each with:
            - id: The matched item's ID
            - name: The matched item's name
            - score: Match score (0.0 to 1.0, higher is better)

    Example:
        import scriptling.similarity as similarity

        # Search list of strings
        results = similarity.search("proj", ["Project Alpha", "Task Beta", "Project Gamma"])
        for r in results:
            print(f"{r['name']}: {r['score']}")

        # Search list of dicts
        projects = [
            {"id": 1, "name": "Website Redesign"},
            {"id": 2, "name": "Mobile App Development"},
            {"id": 3, "name": "Server Migration"},
        ]
        results = similarity.search("web", projects, max_results=3)

        # Search with custom key field
        items = [{"id": 1, "title": "My Project"}]
        results = similarity.search("proj", items, key="title")
    """
    ...

def best(
    query: str,
    items: list[Union[str, dict[str, Any]]],
    *,
    entity_type: str = "item",
    key: str = "name",
    threshold: float = 0.5
) -> dict[str, Any]:
    """
    Find the best match with error formatting.

    If no match is found, returns an error message with suggestions.
    Ideal for command-line tools where you want to suggest alternatives
    when a name is not found.

    Parameters:
        query: The search query string
        items: List of items to search. Each item can be:
               - A string (id will be index)
               - A dict with 'id' and 'name' keys (or keys specified by 'key' param)
        entity_type: Type name for error messages. Default: "item"
        key: Key to use for item name in dicts. Default: "name"
        threshold: Minimum similarity threshold (0.0-1.0). Default: 0.5

    Returns:
        Dictionary with:
            - found (bool): True if a match was found
            - id (int or None): The matched item's ID
            - name (str or None): The matched item's name
            - score (float): Match score (0 if not found)
            - error (str or None): Error message with suggestions if not found

    Example:
        import scriptling.similarity as similarity

        projects = [
            {"id": 1, "name": "Website Redesign"},
            {"id": 2, "name": "Mobile App Development"},
            {"id": 3, "name": "Server Migration"},
        ]

        # Exact match (case-insensitive)
        result = similarity.best("website redesign", projects, entity_type="project")
        if result['found']:
            print(f"Found project ID: {result['id']}")

        # Fuzzy match with error handling
        result = similarity.best("web design", projects, entity_type="project")
        if not result['found']:
            print(result['error'])  # "project 'web design' is unknown..."
    """
    ...

def score(s1: str, s2: str) -> float:
    """
    Calculate similarity score between two strings.

    Uses normalized Levenshtein distance. Returns a value between
    0.0 (completely different) and 1.0 (identical).

    Parameters:
        s1: First string
        s2: Second string

    Returns:
        Similarity score (0.0 to 1.0)

    Example:
        import scriptling.similarity as similarity

        s = similarity.score("hello", "hallo")  # ~0.8
        s = similarity.score("hello", "hello")  # 1.0
        s = similarity.score("hello", "xyz")    # ~0.2
    """
    ...

def tokenize(text: str) -> list[str]:
    """
    Split text into lowercase alphanumeric tokens.

    Only letters a-z and digits 0-9 are retained; everything else becomes a
    word boundary.

    Parameters:
        text: Text to tokenize

    Returns:
        List of lowercase tokens

    Example:
        import scriptling.similarity as similarity

        tokens = similarity.tokenize("Hello, World! 123")
        # ["hello", "world", "123"]
    """
    ...

def minhash(text: str, *, num_hashes: int = 64) -> list[int]:
    """
    Compute a MinHash signature for text.

    Useful for approximate set similarity and semantic-ish recall over
    tokenized text. The default output contains 64 32-bit hash values.

    Parameters:
        text: Text to compute MinHash for
        num_hashes: Number of hash values in the signature. Default: 64

    Returns:
        MinHash signature (list of integers)

    Example:
        import scriptling.similarity as similarity

        sig = similarity.minhash("hello world")
        sig = similarity.minhash("hello world", num_hashes=128)
    """
    ...

def minhash_similarity(a: list[int], b: list[int]) -> float:
    """
    Compare two MinHash signatures.

    Returns the fraction of matching positions between two signatures.
    This is an estimate of Jaccard similarity.

    Parameters:
        a: First MinHash signature (list of integers)
        b: Second MinHash signature (list of integers)

    Returns:
        Similarity score between 0.0 and 1.0

    Example:
        import scriptling.similarity as similarity

        sig1 = similarity.minhash("hello world")
        sig2 = similarity.minhash("hello earth")
        sim = similarity.minhash_similarity(sig1, sig2)
    """
    ...
