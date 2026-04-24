"""
Scriptling Runtime HTTP Library - Type stubs for IntelliSense support.

HTTP server route registration and response helpers for building
web servers and APIs.
"""

from typing import Optional, Any, Callable, Union

class Request:
    """
    HTTP request object passed to route handlers.

    Attributes:
        method: HTTP method (GET, POST, PUT, DELETE)
        path: Request path
        body: Request body as string
        headers: Request headers (lowercase keys)
        query: Query parameters
    """

    method: str
    path: str
    body: str
    headers: dict[str, str]
    query: dict[str, str]

    def json(self) -> Any:
        """
        Parse request body as JSON.

        Returns:
            Parsed JSON as dict or list, or None if body is empty
        """
        ...

def get(path: str, handler: str) -> None:
    """
    Register a GET route.

    Parameters:
        path: URL path for the route (e.g., "/api/users")
        handler: Handler function as "library.function" string

    Example:
        runtime.http.get("/health", "handlers.health_check")
    """
    ...

def post(path: str, handler: str) -> None:
    """
    Register a POST route.

    Parameters:
        path: URL path for the route
        handler: Handler function as "library.function" string

    Example:
        runtime.http.post("/webhook", "handlers.webhook")
    """
    ...

def put(path: str, handler: str) -> None:
    """
    Register a PUT route.

    Parameters:
        path: URL path for the route
        handler: Handler function as "library.function" string

    Example:
        runtime.http.put("/resource", "handlers.update_resource")
    """
    ...

def delete(path: str, handler: str) -> None:
    """
    Register a DELETE route.

    Parameters:
        path: URL path for the route
        handler: Handler function as "library.function" string

    Example:
        runtime.http.delete("/resource", "handlers.delete_resource")
    """
    ...

def route(
    path: str,
    handler: str,
    methods: list[str] = ["GET", "POST", "PUT", "DELETE"]
) -> None:
    """
    Register a route for multiple methods.

    Parameters:
        path: URL path for the route
        handler: Handler function as "library.function" string
        methods: List of HTTP methods to accept

    Example:
        runtime.http.route("/api", "handlers.api", methods=["GET", "POST"])
    """
    ...

def middleware(handler: str) -> None:
    """
    Register middleware for all routes.

    Parameters:
        handler: Middleware function as "library.function" string

    The middleware receives the request object and should return:
        - None to continue to the handler
        - A response dict to short-circuit (block the request)

    Example:
        runtime.http.middleware("auth.check_request")
    """
    ...

def static(path: str, directory: str) -> None:
    """
    Register a static file serving route.

    Parameters:
        path: URL path prefix for static files (e.g., "/assets")
        directory: Local directory to serve files from

    Example:
        runtime.http.static("/assets", "./public")
    """
    ...

def json(status_code: int, data: Any) -> dict[str, Any]:
    """
    Create a JSON response.

    Parameters:
        status_code: HTTP status code (e.g., 200, 404, 500)
        data: Data to serialize as JSON

    Returns:
        Response object for the server

    Example:
        return runtime.http.json(200, {"status": "ok"})
        return runtime.http.json(404, {"error": "Not found"})
    """
    ...

def redirect(location: str, status: int = 302) -> dict[str, Any]:
    """
    Create a redirect response.

    Parameters:
        location: URL to redirect to
        status: HTTP status code (default: 302)

    Returns:
        Response object for the server

    Example:
        return runtime.http.redirect("/new-location")
        return runtime.http.redirect("/permanent", status=301)
    """
    ...

def html(status_code: int, content: str) -> dict[str, Any]:
    """
    Create an HTML response.

    Parameters:
        status_code: HTTP status code
        content: HTML content to return

    Returns:
        Response object for the server

    Example:
        return runtime.http.html(200, "<h1>Hello World</h1>")
    """
    ...

def text(status_code: int, content: str) -> dict[str, Any]:
    """
    Create a plain text response.

    Parameters:
        status_code: HTTP status code
        content: Text content to return

    Returns:
        Response object for the server

    Example:
        return runtime.http.text(200, "Hello World")
    """
    ...

def parse_query(query_string: str) -> dict[str, Any]:
    """
    Parse a URL query string.

    Parameters:
        query_string: Query string to parse (with or without leading ?)

    Returns:
        Parsed key-value pairs

    Example:
        params = runtime.http.parse_query("name=John&age=30")
    """
    ...


class WebSocketClient:
    """
    WebSocket client connection passed to server-side WebSocket handlers.

    Represents a connected WebSocket client and provides methods to
    send and receive messages.

    Attributes:
        remote_addr: Remote address of the connected client
    """

    remote_addr: str

    def send(self, message: Union[str, dict[str, Any]]) -> Optional[Exception]:
        """
        Send a text message to the client.

        Parameters:
            message: Text string or dict (will be JSON-encoded)

        Returns:
            None on success, or an error/exception if send fails

        Example:
            client.send("Welcome to the chat!")
            client.send({"type": "message", "text": "Hello!"})
        """
        ...

    def send_binary(self, data: list[int]) -> Optional[Exception]:
        """
        Send binary data to the client.

        Parameters:
            data: List of byte values (0-255)

        Returns:
            None on success, or an error/exception if send fails

        Example:
            client.send_binary([72, 101, 108, 108, 111])
        """
        ...

    def receive(self, timeout: float = 30) -> Any:
        """
        Receive a message from the client.

        Parameters:
            timeout: Maximum time to wait for a message (seconds)

        Returns:
            The received message (str for text, list for binary),
            or None if timeout or connection closed

        Example:
            msg = client.receive(timeout=60)
            if msg:
                if isinstance(msg, str):
                    print(f"Text: {msg}")
                elif isinstance(msg, list):
                    print(f"Binary: {len(msg)} bytes")
        """
        ...

    def connected(self) -> bool:
        """
        Check if the client connection is still open.

        Returns:
            True if connected, False otherwise
        """
        ...

    def close(self) -> None:
        """
        Close the client connection.
        """
        ...


def not_found(handler: str) -> None:
    """
    Register a custom 404 Not Found handler.

    Parameters:
        handler: Handler function as "library.function" string

    The handler receives the request object and should return a response.
    It is called when no route matches the request path, or when the
    --web-root directory is configured but the file is not found.

    Example:
        runtime.http.not_found("handlers.not_found")
    """
    ...

def websocket(path: str, handler: str) -> None:
    """
    Register a WebSocket route.

    The handler function receives a WebSocketClient object for each
    connected client and typically runs a message loop.

    Parameters:
        path: URL path for the WebSocket endpoint (e.g., "/chat")
        handler: Handler function as "library.function" string

    Handler signature:
        def handler(client: WebSocketClient) -> None:
            client.send("Welcome!")
            while client.connected():
                msg = client.receive(timeout=60)
                if msg:
                    client.send(f"Echo: {msg}")

    Example:
        # Register WebSocket endpoint
        runtime.http.websocket("/chat", "handlers.chat_handler")

        # In handlers.py:
        def chat_handler(client):
            client.send("Welcome to the chat!")
            while client.connected():
                msg = client.receive(timeout=60)
                if msg:
                    client.send(f"Server: {msg}")
    """
    ...
