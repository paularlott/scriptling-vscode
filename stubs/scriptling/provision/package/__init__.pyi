"""
Scriptling Provision Package Library - Type stubs for IntelliSense support.

Installs and removes system packages with apt, dnf, yum, apk or Homebrew. It
asks which packages are installed first, and runs the package manager only
when something needs doing.

apt, dnf, yum and apk install as root: a script running as a user does so
through sudo, asked once (without a password where sudo allows that). The
scriptling CLI refuses it with --deny-become. Homebrew installs as the user.

Constants:
    CREATED: Status returned when anything was installed.
    UNCHANGED: Status returned when every package was already installed.
    REMOVED: Status returned when anything was removed.
    ABSENT: Status returned when no package was installed to remove.

Example:
    import scriptling.provision.package as package

    if package.ensure(["nginx", "curl"]) == package.CREATED:
        print("installed")
"""

from typing import Optional, Union

CREATED: str
UNCHANGED: str
REMOVED: str
ABSENT: str


def ensure(packages: Union[str, list[str]], update: bool = False, manager: Optional[str] = None) -> str:
    """
    Ensure packages are installed.

    Installs those of packages that are not installed. If an install fails,
    the package lists are refreshed and it is tried once more, as a new
    machine needs.

    Parameters:
        packages: A package name, or a list of them
        update: Refresh the package lists before installing (default False)
        manager: "apt", "dnf", "yum", "apk" or "brew". Default: the first of
            these found

    Returns:
        package.CREATED if anything was installed, package.UNCHANGED if all
        were already

    Raises:
        PermissionError: where root is needed and running as root is not allowed
    """
    ...


def absent(packages: Union[str, list[str]], manager: Optional[str] = None) -> str:
    """
    Ensure packages are not installed.

    Parameters:
        packages: A package name, or a list of them
        manager: As for ensure()

    Returns:
        package.REMOVED if anything was removed, package.ABSENT if none was
        installed
    """
    ...


def installed(packages: Union[str, list[str]], manager: Optional[str] = None) -> bool:
    """Whether every one of packages is installed."""
    ...


def manager() -> Optional[str]:
    """The package manager ensure() would use: "apt", "dnf", "yum", "apk" or "brew"; None when there is none."""
    ...
