"""
Scriptling Mercure Library - Type stubs for IntelliSense support.

A client for Mercure hubs (https://mercure.rocks): publish updates to topics
and subscribe to them over Server-Sent Events, against any Mercure hub (the
official hub, FrankenPHP's, or a gossiper cluster).

It speaks Mercure 1.0 by default: access tokens bound to the hub, and
subscriptions by exact topic or URL pattern. Draft-07 (the "mercure" claim and
URI templates), for hubs that take only that, is create_token(draft07=True)
and subscribe(topics=...).

By default each publish is a POST of its own, as Mercure's HTTP protocol has
it, which every hub takes. stream=True publishes to a gossiper hub over one
long streaming request instead, many times faster for many updates.
Subscriptions reconnect by themselves and resume from their last event ID.
"""

from typing import Any, Iterator, Literal, Optional, Union


def Client(
    url: str,
    *,
    key: Optional[str] = None,
    publish: Optional[Union[str, list[str]]] = None,
    subscribe: Optional[Union[str, list[str]]] = None,
    token_ttl: float = 3600,
    token: Optional[str] = None,
    stream: Union[bool, Literal["auto"]] = False,
    verify: Union[bool, str] = True,
    timeout: float = 30,
    headers: Optional[dict[str, str]] = None,
    host: Optional[str] = None,
    h2c: bool = False,
    max_event_size: int = 8388608,
    payload: Optional[dict[str, Any]] = None,
    issuer: str = "https://localhost",
    audience: Optional[str] = None,
    match_type: Literal["exact", "urlpattern"] = "exact",
    subject: Optional[str] = None,
    client_id: str = "scriptling",
    algorithm: Literal["HS256", "HS384", "HS512"] = "HS256",
    draft07: bool = False,
) -> "MercureClient":
    """
    A client of a Mercure hub, to publish updates and subscribe to topics.

    Give it the hub's key and it makes its own tokens, renewing each before it
    expires: subscriptions and publish streams run for as long as the script
    does. A token made elsewhere is given with token= and replaced with
    set_token() before it expires.

    Parameters:
        url (str): The hub's URL, e.g. "https://example.com/.well-known/mercure"
        key (str, optional): The hub's JWT key, for the client to make and
            renew its own tokens. Not with token=
        publish (str or list, optional): With key=, the topics its tokens may
            publish to. Default: every topic (with subscribe unset too)
        subscribe (str or list, optional): With key=, the topics its tokens may
            receive private updates of. Default: every topic (with publish
            unset too)
        token_ttl (float, optional): With key=, each token's lifetime in
            seconds (at least 10; 0, none, only with draft07). Tokens are
            renewed at half their life. Default: 3600
        token (str, optional): A token made elsewhere, presented as it is
        stream (bool or "auto", optional): How to publish. False (default): a
            POST per update, which every hub takes. True: one long streaming
            publish to a gossiper hub. "auto": stream to a gossiper hub, a POST
            per update to any other
        verify (bool or str, optional): Verify the hub's TLS certificate
            (default: True); False accepts any certificate (development only);
            a path names a PEM bundle of CA certificates to trust
        timeout (float, optional): Seconds to wait for the hub to answer a
            publish, or to accept a subscription. Default: 30
        headers (dict, optional): Headers added to every request
        host (str, optional): The host name to ask for, when it is not the
            URL's (a node reached by its address)
        h2c (bool, optional): Speak HTTP/2 without TLS to an http:// gossiper
            hub, so the publish stream and every subscription share one
            connection
        max_event_size (int, optional): Largest event a subscription takes, in
            bytes. Default: 8 MiB
        payload, issuer, audience, match_type, subject, client_id, algorithm,
        draft07: With key=, the token's other claims, as create_token() takes
            them. audience defaults to url

    Returns:
        MercureClient

    Example:
        import os
        import scriptling.mercure as mercure

        hub = mercure.Client("https://example.com/.well-known/mercure", key=os.getenv("MERCURE_JWT_KEY"))
        sub = hub.subscribe(match_urlpattern="https://example.com/books/:id")
        hub.publish("https://example.com/books/1", {"title": "Dune"})
        for event in sub:
            print(event.id, event.json())
    """
    ...


def create_token(
    key: str,
    audience: Optional[str] = None,
    *,
    publish: Optional[Union[str, list[str]]] = None,
    subscribe: Optional[Union[str, list[str]]] = None,
    payload: Optional[dict[str, Any]] = None,
    expires: float = 3600,
    issuer: str = "https://localhost",
    match_type: Literal["exact", "urlpattern"] = "exact",
    subject: Optional[str] = None,
    client_id: str = "scriptling",
    algorithm: Literal["HS256", "HS384", "HS512"] = "HS256",
    draft07: bool = False,
) -> str:
    """
    A Mercure JWT, signed with a hub's HMAC key.

    By default a Mercure 1.0 access token (RFC 9068, with
    authorization_details) for the hub at audience, which current hubs take:
    the official hub, gossiper. draft07=True makes a draft-07 token (the
    "mercure" claim) for hubs that take only that.

    Parameters:
        key (str): The hub's publisher or subscriber JWT key. Keep it out of the
            script: read it with scriptling.secret or os.getenv
        audience (str): The hub's URL, its resource identifier (the aud claim),
            by position or name. Not for draft07=True
        publish (str or list, optional): Topics the token may publish to,
            e.g. ["*"]
        subscribe (str or list, optional): Topics the token may receive
            private updates of
        payload (dict, optional): Shared with other subscribers in
            subscription events
        expires (float, optional): Seconds until the token expires. Default:
            3600 (0, none, only for draft07=True)
        issuer (str, optional): The iss claim, an issuer the hub trusts.
            Default: "https://localhost", which the official hub's image and
            gossiper trust unless configured otherwise
        match_type (str, optional): How publish and subscribe match topics:
            "exact" (default) or "urlpattern"
        subject (str, optional): The sub claim. Default: the client ID (none
            for draft07=True)
        client_id (str, optional): The client_id claim. Default: "scriptling"
        algorithm (str, optional): "HS256" (default), "HS384" or "HS512"
        draft07 (bool, optional): Make a draft-07 token instead: publish and
            subscribe are draft-07 selectors, with no audience or issuer

    Returns:
        str: the token

    Example:
        URL = "https://hub.example.com/.well-known/mercure"
        jwt = mercure.create_token(os.getenv("MERCURE_JWT_KEY"), URL, publish=["*"], subscribe=["*"])
    """
    ...


class MercureClient:
    """A client of a Mercure hub. Obtain one with mercure.Client()."""

    url: str
    """The hub's URL."""

    transport: Literal["http", "stream", "auto"]
    """How the client publishes now: "http" or "stream" ("auto" before a
    client with stream="auto" first publishes)."""

    closed: bool
    """Whether the client has been closed."""

    def publish(
        self,
        topic: Union[str, list[str]],
        data: Any = None,
        *,
        id: Optional[str] = None,
        type: Optional[str] = None,
        private: bool = False,
        retry: Optional[float] = None,
        replicas: int = 0,
    ) -> str:
        """
        Publish an update and return its event ID once the hub has it.

        Parameters:
            topic (str or list): The update's topic, or its canonical topic
                then alternates
            data (str or any, optional): The update's content. A str is sent as
                is; any other value (a dict, a list, a number) as JSON
            id (str, optional): The event ID. Default: the hub makes one
            type (str, optional): The SSE event type
            private (bool, optional): Deliver only to subscribers allowed the
                topic. Default: False
            retry (float, optional): The reconnection time subscribers are
                given, in seconds
            replicas (int, optional): Copies a gossiper hub keeps, on as many
                nodes, before it answers

        Returns:
            str: the event ID
        """
        ...

    def publish_many(self, updates: list[dict[str, Any]]) -> list[str]:
        """
        Publish several updates and return their event IDs, in order. Over a
        stream they are pipelined, in order; with a POST per update they are
        published one after another.

        Parameters:
            updates (list): Dicts with the arguments of publish(): topic, data,
                id, type, private, retry, replicas

        Returns:
            list: the event IDs. If one fails, the error names it; the updates
            before it were published
        """
        ...

    def subscribe(
        self,
        *match_topics: Union[str, list[str]],
        match: Optional[Union[str, list[str]]] = None,
        match_urlpattern: Optional[Union[str, list[str]]] = None,
        topics: Optional[Union[str, list[str]]] = None,
        last_event_id: Optional[str] = None,
        buffer: int = 1024,
    ) -> "Subscription":
        """
        Subscribe to topics; returns once the hub accepted the subscription.
        The subscription reconnects by itself, resuming from its last event ID,
        until it is closed.

        Parameters:
            *match_topics (str or list): Topics to subscribe to, exactly
                (Mercure 1.0 match); "*" for every topic
            match (str or list, optional): More exact topics, as by position
            match_urlpattern (str or list, optional): URL patterns (Mercure
                1.0), e.g. "https://example.com/books/:id"
            topics (str or list, optional): Draft-07 topic selectors, for hubs
                that take only draft-07: topics, URI templates (e.g.
                "https://example.com/books/{id}") or "*"
            last_event_id (str, optional): Resume after that event ("earliest"
                for the hub's whole history)
            buffer (int, optional): Events held for the script before the
                stream waits. Default: 1024

        Returns:
            Subscription

        Raises:
            RuntimeError: When the host lets scripts publish only; catch it
                to carry on without subscribing
        """
        ...

    def set_token(self, token: str) -> None:
        """
        Replace the token of a client made with token=. The next request, and
        every stream the client opens or reopens from then on, presents it. A
        client made with key= renews its own tokens and refuses it.

        Example:
            issued.refresh()
            hub.set_token(issued.access_token)
        """
        ...

    def close(self) -> None:
        """Close the client, its subscriptions and its publish stream."""
        ...

    def __enter__(self) -> "MercureClient": ...
    def __exit__(self, *args: Any) -> bool: ...


class Subscription:
    """An open subscription. Obtain one with MercureClient.subscribe()."""

    last_event_id: Optional[str]
    """The ID of the last event received, which the subscription resumes from
    should it reconnect."""

    def receive(self, timeout: Optional[float] = 30) -> Optional["Event"]:
        """
        The next event, or None when none comes within timeout seconds.

        Parameters:
            timeout (float, optional): Seconds to wait. Default: 30. None waits
                until an event comes or the subscription is closed; 0 takes
                only an event already received

        Returns:
            Event, or None on a timeout or once the subscription is closed.
            Raises when the hub refused the subscription for good once
            reconnecting (its token expired, say)
        """
        ...

    def close(self) -> None:
        """End the subscription."""
        ...

    def __iter__(self) -> Iterator["Event"]:
        """Iterate over the events as they come, until the subscription is closed."""
        ...

    def __enter__(self) -> "Subscription": ...
    def __exit__(self, *args: Any) -> bool: ...


class Event:
    """An event a subscription received."""

    id: str
    """The event ID."""

    type: Optional[str]
    """The SSE event type, or None."""

    data: str
    """The event's data."""

    retry: Optional[float]
    """The reconnection time the hub gave, in seconds, or None."""

    def json(self) -> Any:
        """The event's data parsed as JSON. Raises ValueError when it is not JSON."""
        ...

    def to_dict(self) -> dict[str, Any]:
        """The event as a dict: id, type, data and retry."""
        ...
