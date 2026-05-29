"""
Scriptling Requests Library - Type stubs for IntelliSense support.

HTTP client library for making web requests. Provides functions for
GET, POST, PUT, DELETE, PATCH requests and parallel execution.
"""

from typing import Any, Optional, Union

class Response:
    """HTTP response object returned by all request functions."""

    status_code: int
    """HTTP status code (e.g. 200, 404, 500)."""

    text: str
    """Response body as string."""

    body: str
    """Response body as string (alias for text)."""

    headers: dict[str, str]
    """Response headers."""

    url: str
    """The URL of the response."""

    def json(self) -> Any:
        """
        Parse the response body as JSON.

        Returns:
            Parsed JSON data (dict, list, string, number, bool, or None)

        Raises:
            Exception: If the body is not valid JSON
        """
        ...

    def raise_for_status(self) -> None:
        """
        Raise an exception if the response status code indicates an error (>= 400).

        Raises:
            HTTPError: If status_code >= 400
        """
        ...


# Exception types for except clause matching
RequestException: str
"""Base exception type for request errors."""

HTTPError: str
"""Exception type for HTTP error responses (4xx, 5xx)."""


def get(url: str, **kwargs: Any) -> Response:
    """
    Send a GET request.

    Parameters:
        url: The URL to request
        **kwargs: Optional arguments
            timeout (int): Request timeout in seconds (default: 5)
            headers (dict): HTTP headers to send
            params (dict): Query parameters to append to the URL
            auth (tuple/list): Basic authentication as (username, password)

    Returns:
        Response object
    """
    ...


def post(url: str, data: Optional[str] = None, **kwargs: Any) -> Response:
    """
    Send a POST request.

    Parameters:
        url: The URL to request
        data: Request body as string (optional)
        **kwargs: Optional arguments
            json (dict/list): JSON-encode as request body (sets Content-Type)
            timeout (int): Request timeout in seconds (default: 5)
            headers (dict): HTTP headers to send
            params (dict): Query parameters to append to the URL
            auth (tuple/list): Basic authentication as (username, password)

    Returns:
        Response object
    """
    ...


def put(url: str, data: Optional[str] = None, **kwargs: Any) -> Response:
    """
    Send a PUT request.

    Parameters:
        url: The URL to request
        data: Request body as string (optional)
        **kwargs: Optional arguments
            json (dict/list): JSON-encode as request body (sets Content-Type)
            timeout (int): Request timeout in seconds (default: 5)
            headers (dict): HTTP headers to send
            params (dict): Query parameters to append to the URL
            auth (tuple/list): Basic authentication as (username, password)

    Returns:
        Response object
    """
    ...


def delete(url: str, **kwargs: Any) -> Response:
    """
    Send a DELETE request.

    Parameters:
        url: The URL to request
        **kwargs: Optional arguments
            timeout (int): Request timeout in seconds (default: 5)
            headers (dict): HTTP headers to send
            params (dict): Query parameters to append to the URL
            auth (tuple/list): Basic authentication as (username, password)

    Returns:
        Response object
    """
    ...


def patch(url: str, data: Optional[str] = None, **kwargs: Any) -> Response:
    """
    Send a PATCH request.

    Parameters:
        url: The URL to request
        data: Request body as string (optional)
        **kwargs: Optional arguments
            json (dict/list): JSON-encode as request body (sets Content-Type)
            timeout (int): Request timeout in seconds (default: 5)
            headers (dict): HTTP headers to send
            params (dict): Query parameters to append to the URL
            auth (tuple/list): Basic authentication as (username, password)

    Returns:
        Response object
    """
    ...


def parallel(requests: list[dict[str, Any]], max_parallel: int = 4) -> list[Response]:
    """
    Execute multiple HTTP requests in parallel.

    Sends multiple HTTP requests concurrently with a configurable concurrency
    limit. Results are returned in the same order as the input requests
    regardless of completion order.

    Parameters:
        requests: List of request specification dicts, each containing:
            - method (str): HTTP method — "GET", "POST", "PUT", "DELETE", "PATCH" (default: "GET")
            - url (str, required): The URL to request
            - data (str, optional): Request body as string
            - json (dict/list, optional): Data to JSON-encode as request body
            - headers (dict, optional): HTTP headers
            - params (dict, optional): Query parameters
            - auth (list, optional): Basic auth as [username, password]
            - timeout (int, optional): Timeout in seconds (default: 30)
        max_parallel: Maximum number of concurrent requests (default: 4)

    Returns:
        List of Response objects in the same order as input.
        Failed requests return a Response with status_code=0 and the error in body.

    Example:
        results = requests.parallel([
            {"method": "GET", "url": "https://api.example.com/items/1"},
            {"method": "GET", "url": "https://api.example.com/items/2"},
            {"method": "POST", "url": "https://api.example.com/items", "json": {"name": "new"}},
        ], max_parallel=4)

        for resp in results:
            if resp.status_code == 200:
                data = resp.json()
    """
    ...
