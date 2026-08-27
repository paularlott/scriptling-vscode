"""
Scriptling Runtime HTTP Library - Type stubs for IntelliSense support.

HTTP server route registration and response helpers for building
web servers and APIs.
"""

from typing import Optional, Any, Callable, Union, overload, TypeVar

F = TypeVar('F', bound=Callable[..., Any])

class Request:
    """
    HTTP request object passed to route handlers.

    Attributes:
        method: HTTP method (GET, POST, PUT, PATCH, DELETE)
        path: Request path
        body: Request body as string
        headers: Request headers (lowercase keys)
        query: Query parameters
        path_params: Path parameters captured from route wildcards
        remote_addr: Remote address of the client
    """

    method: str
    path: str
    body: str
    headers: dict[str, str]
    query: dict[str, str]
    path_params: dict[str, str]
    remote_addr: str

    def path_param(self, name: str, default: Optional[Any] = None) -> Any:
        """
        Get a path parameter captured from a route wildcard.

        Route patterns like "/api/users/{id}" capture the matching request
        path segments, percent-decoded.

        Parameters:
            name: Path parameter name
            default: Value returned when the parameter is absent

        Returns:
            The captured value, default, or None
        """
        ...

    def query_param(self, name: str, default: Optional[Any] = None) -> Any:
        """
        Get a query parameter.

        Parameters:
            name: Query parameter name
            default: Value returned when the parameter is absent

        Returns:
            The first value of the parameter, default, or None
        """
        ...

    def header(self, name: str, default: Optional[Any] = None) -> Any:
        """
        Get a request header. Header names are case-insensitive.

        Parameters:
            name: Header name
            default: Value returned when the header is absent

        Returns:
            The header value, default, or None
        """
        ...

    def json(self) -> Any:
        """
        Parse request body as JSON.

        Returns:
            Parsed JSON as dict or list, or None if body is empty
        """
        ...

@overload
def get(path: str) -> Callable[[F], F]: ...
@overload
def get(path: str, handler: str) -> None: ...
def get(path: str, handler: str = ...) -> Optional[Callable[[F], F]]:
    """
    Register a GET route, or use as decorator.

    Decorator form::

        @http.get("/health")
        def health(request):
            return http.json(200, {"status": "ok"})

    Imperative form::

        runtime.http.get("/health", "handlers.health_check")
    """
    ...

@overload
def post(path: str) -> Callable[[F], F]: ...
@overload
def post(path: str, handler: str) -> None: ...
def post(path: str, handler: str = ...) -> Optional[Callable[[F], F]]:
    """Register a POST route, or use as decorator."""
    ...

@overload
def put(path: str) -> Callable[[F], F]: ...
@overload
def put(path: str, handler: str) -> None: ...
def put(path: str, handler: str = ...) -> Optional[Callable[[F], F]]:
    """Register a PUT route, or use as decorator."""
    ...

@overload
def patch(path: str) -> Callable[[F], F]: ...
@overload
def patch(path: str, handler: str) -> None: ...
def patch(path: str, handler: str = ...) -> Optional[Callable[[F], F]]:
    """Register a PATCH route, or use as decorator."""
    ...

@overload
def delete(path: str) -> Callable[[F], F]: ...
@overload
def delete(path: str, handler: str) -> None: ...
def delete(path: str, handler: str = ...) -> Optional[Callable[[F], F]]:
    """Register a DELETE route, or use as decorator."""
    ...

@overload
def route(path: str, *, methods: list[str] = ...) -> Callable[[F], F]: ...
@overload
def route(path: str, handler: str, methods: list[str] = ...) -> None: ...
def route(path: str, handler: str = ..., methods: list[str] = ...) -> Optional[Callable[[F], F]]:
    """
    Register a route for multiple methods, or use as decorator.

    Decorator form::

        @http.route("/api", methods=["GET", "POST"])
        def handler(request):
            ...

    Imperative form::

        runtime.http.route("/api", "handlers.api", methods=["GET", "POST"])
    """
    ...

@overload
def middleware(handler: F) -> F: ...
@overload
def middleware(handler: str) -> None: ...
def middleware(handler: Union[str, F]) -> Optional[F]:
    """
    Register middleware for all routes, or use as bare decorator.

    Decorator form::

        @http.middleware
        def auth(request):
            return None

    Imperative form::

        runtime.http.middleware("auth.check_request")

    The middleware receives the request object and should return:
        - None to continue to the handler
        - A response dict to short-circuit (block the request)
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


@overload
def not_found(handler: F) -> F: ...
@overload
def not_found(handler: str) -> None: ...
def not_found(handler: Union[str, F]) -> Optional[F]:
    """
    Register a custom 404 Not Found handler, or use as bare decorator.

    Decorator form::

        @http.not_found
        def handle_404(request):
            return http.html(404, "<h1>Not Found</h1>")

    Imperative form::

        runtime.http.not_found("handlers.not_found")
    """
    ...

@overload
def websocket(path: str) -> Callable[[F], F]: ...
@overload
def websocket(path: str, handler: str) -> None: ...
def websocket(path: str, handler: str = ...) -> Optional[Callable[[F], F]]:
    """
    Register a WebSocket route, or use as decorator.

    Decorator form::

        @http.websocket("/chat")
        def chat_handler(client):
            client.send("Welcome!")

    Imperative form::

        runtime.http.websocket("/chat", "handlers.chat_handler")

    The handler receives a WebSocketClient object and runs for the
    connection lifetime.
    """
    ...
