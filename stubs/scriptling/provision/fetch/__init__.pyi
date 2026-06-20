"""
Scriptling Provision Fetch Library - Type stubs for IntelliSense support.

This library fetches files over HTTP/HTTPS and can optionally unpack fetched ZIP
archives into a destination directory.

Constants:
    CREATED: Status returned when new content was written or unpacked.
    UPDATED: Status returned when existing content changed.
    UNCHANGED: Status returned when the destination already matched.

Example:
    import scriptling.provision.fetch as fetch

    result = fetch.file("https://example.com/tool.zip", "~/bin/tool", unpack_zip=True)
    if result["status"] != fetch.UNCHANGED:
        print("updated", result["files"])
"""

from typing import Any

CREATED: str
UPDATED: str
UNCHANGED: str


def file(
    url: str,
    dest: str,
    insecure: bool = False,
    unpack_zip: bool = False,
    timeout: int = 30,
    mode: int = 0o644,
    dir_mode: int = 0o755,
) -> dict[str, Any]:
    """
    Fetch a file over HTTP or HTTPS.

    Downloads url and writes it to dest. Parent directories are created as
    needed. When unpack_zip is True, dest is treated as a directory and the
    response body is unpacked as a ZIP archive.

    Parameters:
        url: HTTP or HTTPS URL to fetch
        dest: Output file path, or destination directory when unpack_zip is True
        insecure: If True, skip HTTPS certificate verification (default False)
        unpack_zip: If True, unpack the fetched body as a ZIP archive (default False)
        timeout: Request timeout in seconds (default 30)
        mode: File permission mode for created files (default 0o644)
        dir_mode: Directory permission mode for created directories (default 0o755)

    Returns:
        A dict with status, url, path, bytes, unpacked, and files keys.
        status is fetch.CREATED, fetch.UPDATED, or fetch.UNCHANGED.
    """
    ...
