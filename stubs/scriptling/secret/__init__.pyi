"""
Secret Library - Type stubs for IntelliSense support.

Provider-agnostic secret access using host-configured aliases.
Scripts only see aliases, paths, and optional field names.
"""

def get(alias: str, path: str, field: str = "") -> str:
    """
    Resolve a secret through a host-configured provider alias.

    Parameters:
        alias: Registered provider alias such as "prod_vault" or "op"
        path: Provider-specific secret path or identifier
        field: Optional field to extract from a multi-value secret

    Returns:
        Resolved secret value as a string

    Example:
        import scriptling.secret as secret

        db_password = secret.get("prod_vault", "secret/data/app", "password")
        api_key = secret.get("op", "Engineering/api-key", "credential")
    """
    ...

def list(alias: str, path: str) -> list[str]:
    """
    List keys at a path through a host-configured provider alias.

    Returns key names at the given path for Vault, or item titles in a vault for 1Password.

    Parameters:
        alias: Registered provider alias such as "prod_vault" or "op"
        path: Provider-specific path (Vault secret path, or 1Password vault name)

    Returns:
        List of key or item name strings

    Example:
        import scriptling.secret as secret

        keys = secret.list("prod_vault", "secret/data/app")
        items = secret.list("op", "Engineering")
    """
    ...
