"""
Scriptling Find Library - Type stubs for IntelliSense support.

Find files and directories by name, type, modification time, and size —
similar in spirit to the Unix find command.
"""

from typing import List, Optional, TypedDict


class FindEntry(TypedDict):
    """A single matching entry returned by find.entries()."""

    path: str
    size: int
    mtime: float
    is_dir: bool
    file_perm: Optional[int]
    hash: Optional[str]
    link_target: Optional[str]


def path(
    path: str,
    *,
    recursive: bool = True,
    type: str = "any",
    name: str = "",
    mtime_min: Optional[float] = None,
    mtime_max: Optional[float] = None,
    size_min: Optional[int] = None,
    size_max: Optional[int] = None,
    include_hidden: bool = False,
    follow_links: bool = False,
    max_depth: Optional[int] = None,
) -> List[str]:
    """
    Find files and directories under a path by name, type, modification time,
    and size. Returns matching paths as a list of strings in arbitrary order.

    Recursive searches stat and filter entries concurrently using a bounded
    worker pool, the same model as scriptling.grep.

    Parameters:
        path           Directory (or file) to search under
        recursive      Descend into subdirectories (default: True). When False,
                       only the immediate children of path are examined.
        type           Restrict to "file", "dir", or "any" (default: "any")
        name           Shell-style glob pattern matched against the entry's base
                       name, e.g. "*.md". Empty matches everything (default).
        mtime_min      Include only entries modified at or after this epoch time
                       (float seconds). None = no lower bound (default).
        mtime_max      Include only entries modified at or before this epoch time
                       (float seconds). None = no upper bound (default).
        size_min       Include only entries whose size in bytes is >= this value.
                       None = no lower bound (default).
        size_max       Include only entries whose size in bytes is <= this value.
                       None = no upper bound (default).
        include_hidden When True, entries whose name starts with "." are matched;
                       when False (the default) they are skipped.
        follow_links   Follow symlinks if they resolve within allowed paths
                       (default: False)
        max_depth      Maximum recursion depth (1 = immediate children only).
                       None = unlimited (default).

    Returns:
        List of matching path strings.

    Example:
        import scriptling.find as find
        import time

        # Markdown files modified in the last 24 hours
        recent = find.path("/docs", name="*.md", type="file",
                           mtime_min=time.time() - 86400)

        # Large log files (> 100 MiB)
        big = find.path("/var/log", name="*.log", type="file",
                        size_min=100 * 1024 * 1024)
    """
    ...


def entries(
    path: str,
    *,
    recursive: bool = True,
    type: str = "any",
    name: str = "",
    mtime_min: Optional[float] = None,
    mtime_max: Optional[float] = None,
    size_min: Optional[int] = None,
    size_max: Optional[int] = None,
    include_hidden: bool = False,
    follow_links: bool = False,
    max_depth: Optional[int] = None,
    include_metadata: bool = False,
    include_hash: bool = False,
    include_symlinks: bool = False,
) -> List[FindEntry]:
    """
    Find files and directories under a path by name, type, modification time,
    and size, returning a list of dicts carrying each match's path, size,
    mtime, and is_dir flag. Use this when you need the metadata to compare
    trees without re-reading bytes; use path() when only the strings are
    needed, as path() skips the stat in the no-filter common case.

    Parameters are the same as path(), plus:
        include_metadata When True, file_perm is populated (extracted from the
                         entry stat, no extra syscall).
        include_hash     When True, each file is crc64-hashed and the hex
                         checksum is returned in the hash field.
        include_symlinks When True, symlink entries are yielded with their
                         link_target instead of being followed.

    Each entry dict has the keys:
        path    str   - the matching entry's path
        size    int   - size in bytes (0 for directories)
        mtime   float - modification time as epoch seconds
        is_dir  bool  - True when the entry is a directory
        file_perm int? - file permission bits (None unless include_metadata)
        hash    str?  - hex-encoded crc64 checksum (None unless include_hash)
        link_target str? - symlink target (None unless include_symlinks)

    Paths are returned in arbitrary order. Recursive searches stat and filter
    entries concurrently using a bounded worker pool, the same model as
    scriptling.grep.

    Example:
        import scriptling.find as find
        import time

        # Sync-relevant metadata: every markdown file with its size and mtime
        for e in find.entries("/docs", name="*.md", type="file"):
            print(e["path"], e["size"], e["mtime"])

        # Hash-based change detection
        for e in find.entries("/site", include_hash=True, type="file"):
            print(e["path"], e["hash"])

        # Detect symbolic links without following them
        for e in find.entries("/project", include_symlinks=True):
            if e["link_target"]:
                print(e["path"], "->", e["link_target"])
    """
    ...
