"""
Scriptling OAuth Library - Type stubs for IntelliSense support.

OAuth 2.0 and OpenID Connect against any identity provider that publishes
discovery metadata: device sign-in (RFC 8628), client credentials, refresh
tokens, and verification of the access tokens sent to an API a script serves.
"""

from typing import Any, Optional, Union


def Client(
    issuer: str,
    client_id: str,
    *,
    client_secret: str = "",
    verify: Union[bool, str] = True,
    timeout: float = 10,
) -> "OAuthClient":
    """
    A client at an identity provider. Its endpoints are read from the issuer's
    discovery document on first use, which must name the issuer.

    Parameters:
        issuer (str): The IdP's issuer URL, e.g. "https://id.example.com/o/acme".
            https only (plain http only on localhost); no query or fragment
        client_id (str): This script's client ID at the IdP (by position or name)
        client_secret (str, optional): A confidential client's secret, for
            client_credentials(). Read it with scriptling.secret or os.getenv
        verify (bool or str, optional): Verify the IdP's TLS certificate
            (default: True); False accepts any certificate (development only);
            a path names a PEM bundle of CA certificates to trust
        timeout (float, optional): Per-request timeout in seconds. Default: 10

    Returns:
        OAuthClient

    Example:
        import scriptling.oauth as oauth

        idp = oauth.Client("https://id.example.com/o/acme", client_id="c_cli")
        flow = idp.device_start(scope="openid profile", resource="https://api.example.com/")
        print("Open", flow.verification_uri, "and enter", flow.user_code)
        token = flow.wait()
        requests.get("https://api.example.com/items", headers=token.headers())
    """
    ...


class OAuthClient:
    """A client at an identity provider. Obtain one with oauth.Client()."""

    issuer: str
    """The issuer URL."""

    client_id: str
    """This script's client ID."""

    def metadata(self) -> dict:
        """The IdP's discovery document (endpoints and what it supports), read once an hour."""
        ...

    def device_start(
        self,
        *,
        scope: Optional[Union[str, list[str]]] = None,
        resource: Optional[Union[str, list[str]]] = None,
    ) -> "DeviceFlow":
        """
        Start a device sign-in (RFC 8628). The person opens verification_uri on
        any device, enters user_code and approves; wait() for it (a CLI) or
        poll() on each page load (a web page). No browser is opened.

        Parameters:
            scope (str or list, optional): Scopes, e.g. "openid profile"
                (add "offline_access" for a refresh token)
            resource (str or list, optional): The API(s) the token is for
                (RFC 8707); they become its audience

        Returns:
            DeviceFlow
        """
        ...

    def device_resume(self, flow: dict) -> "DeviceFlow":
        """
        Pick up a device sign-in from DeviceFlow.to_dict(), e.g. on a later
        web request.
        """
        ...

    def client_credentials(
        self,
        *,
        scope: Optional[Union[str, list[str]]] = None,
        resource: Optional[Union[str, list[str]]] = None,
    ) -> "Token":
        """
        A token for the client itself, with no person. Needs client_secret.

        Parameters:
            scope (str or list, optional): Scopes to ask for
            resource (str or list, optional): The API(s) the token is for
        """
        ...

    def token_from_dict(self, token: dict) -> "Token":
        """A token saved with Token.to_dict(), able to refresh itself with this client."""
        ...

    def verify(self, token: str, audience: str, *, typ: Optional[str] = None, leeway: float = 60) -> dict:
        """
        Check an access token sent to an API this script serves and return its
        claims: the signature against the issuer's published keys, iss, aud
        containing audience, exp and nbf (within leeway seconds), no key
        binding (cnf), and the JWT type when typ is given ("at+jwt" for
        RFC 9068 access tokens). Raises on any failure; the error never
        contains the token.

        Parameters:
            token (str): The access token (the Bearer value)
            audience (str): This API's identifier, as the IdP puts it in aud
            typ (str, optional): Require this JWT type
            leeway (float, optional): Allowed clock skew in seconds. Default: 60

        Returns:
            dict: The claims (sub, scope, client_id, ...)
        """
        ...


class DeviceFlow:
    """A device sign-in waiting for the person to approve it."""

    user_code: str
    """The code the person enters."""

    verification_uri: str
    """Where the person goes to enter the code."""

    verification_uri_complete: Optional[str]
    """The same with the code filled in, when the IdP gives one."""

    expires_at: int
    """When the code expires (Unix time)."""

    interval: int
    """Seconds between polls the IdP allows."""

    def poll(self) -> Optional["Token"]:
        """
        Check once whether the sign-in was approved: the Token once it is,
        None while waiting. Asks the IdP no sooner than its interval allows.
        Raises if the sign-in was denied or the code expired.
        """
        ...

    def wait(self, *, timeout: Optional[float] = None) -> "Token":
        """
        Wait, polling at the IdP's interval, until the sign-in is approved.
        Raises if it is denied, the code expires or timeout seconds pass.
        """
        ...

    def to_dict(self) -> dict:
        """
        The flow as a dict, for OAuthClient.device_resume(). It holds the
        device code: keep it server side, never in a page, URL or cookie.
        """
        ...


class Token:
    """An access token and what came with it. Refreshes itself when it can."""

    access_token: str
    token_type: str
    expires_at: Optional[int]
    """When the access token expires (Unix time), None when the IdP did not say."""
    refresh_token: Optional[str]
    scope: Optional[str]
    id_token: Optional[str]

    def headers(self) -> dict[str, str]:
        """
        {"Authorization": "Bearer <access token>"}, for requests. Refreshes the
        token first when it is about to expire and has a refresh token.
        """
        ...

    def is_expired(self, *, margin: float = 30) -> bool:
        """Whether the access token expires within margin seconds (False when unknown)."""
        ...

    def refresh(self, *, scope: Optional[Union[str, list[str]]] = None) -> None:
        """Get a new access token with the refresh token, in place."""
        ...

    def to_dict(self) -> dict[str, Any]:
        """
        The token as a dict (access_token, token_type, expires_at, expires_in,
        refresh_token, scope, id_token), to save between runs if the script
        chooses to. It holds the tokens: store it where only the script can
        read it.
        """
        ...

    def claims(self) -> dict:
        """What a JWT access token says, NOT verified: for showing or debugging only."""
        ...
