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
