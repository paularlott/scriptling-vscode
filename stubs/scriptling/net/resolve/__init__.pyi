"""
Scriptling DNS Resolve Library - Type stubs for IntelliSense support.

This library provides DNS resolution utilities for IP lookup, SRV record
resolution, and srv+http(s):// URL resolution.

Example:
    import scriptling.net.resolve as resolve

    # Resolve a hostname to IP addresses
    ips = resolve.lookup_ip("example.com")
    print(ips)  # ["93.184.216.34"]

    # Resolve an SRV record
    addrs = resolve.lookup_srv("_myservice._tcp.example.com")
    for addr in addrs:
        print(addr["ip"], addr["port"])

    # Resolve a srv+https:// URL
    url = resolve.resolve_srv_http("srv+https://api.example.com/v1")
"""


def lookup_ip(host: str) -> list[str]:
    """
    Resolve a hostname to a list of IP address strings.

    Parameters:
        host: The hostname to resolve

    Returns:
        List of IP address strings

    Example:
        ips = resolve.lookup_ip("example.com")
        print(ips)  # ["93.184.216.34"]
    """
    ...


def lookup_srv(service: str) -> list[dict[str, object]]:
    """
    Resolve an SRV record to a list of address dicts.

    Parameters:
        service: The SRV service name (e.g. "_myservice._tcp.example.com")

    Returns:
        List of dicts with "ip" (str) and "port" (int) keys

    Example:
        addrs = resolve.lookup_srv("_myservice._tcp.example.com")
        for addr in addrs:
            print(addr["ip"], addr["port"])
    """
    ...


def resolve_srv_http(uri: str) -> str:
    """
    Resolve a srv+http(s):// URI to a concrete URL.

    Strips the srv+ prefix, resolves the SRV record for the host, and returns
    the URL with the correct port substituted. The original hostname is preserved
    for SNI/TLS. If the URI does not start with srv+, it is returned unchanged
    (with an https:// prefix added if no scheme is present).

    Parameters:
        uri: The URI to resolve (e.g. "srv+https://service.example.com/path")

    Returns:
        The resolved URL

    Example:
        url = resolve.resolve_srv_http("srv+https://api.example.com/v1")
        print(url)  # "https://api.example.com:8443/v1"
    """
    ...
