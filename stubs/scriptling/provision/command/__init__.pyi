"""
Scriptling Provision Command Library - Type stubs for IntelliSense support.

Runs commands while provisioning a machine, as the script's user or, with
become=True, as root, through sudo: asked once per script, without a password
where sudo allows that. The scriptling CLI refuses become=True with
--deny-become.

Example:
    import scriptling.provision.command as command

    command.run(["systemctl", "restart", "nginx"], become=True)

    r = command.run(["grep", "-q", "docker", "/etc/group"], check=False)
    if not r.ok:
        print("no docker group")
"""

from typing import Optional, Union


class Result:
    """How a command ended."""

    args: list[str]
    """The command, as given (a shell command line is one element)."""
    returncode: int
    """Its exit status."""
    stdout: str
    """What it wrote to standard output."""
    stderr: str
    """What it wrote to standard error."""
    ok: bool
    """True when returncode is 0."""


def run(
    cmd: Union[list[str], str],
    become: bool = False,
    cwd: Optional[str] = None,
    env: Optional[dict[str, str]] = None,
    input: Optional[str] = None,
    timeout: Optional[float] = None,
    check: bool = True,
) -> Result:
    """
    Run a command and wait for it, capturing its output.

    A list is a program and its arguments, run as they are; a string is a
    command line for /bin/sh, so it may use pipes, && and the like.

    Parameters:
        cmd: The command
        become: Run as root (default False)
        cwd: Working directory (supports ~ expansion). Default: the current one
        env: Environment variables to add to the inherited environment
        input: Text for the command's standard input. Default: none
        timeout: Seconds to allow; the command is stopped after that and an
            error raised
        check: Raise an error when the command exits with a non-zero status
            (default True)

    Returns:
        The Result

    Raises:
        PermissionError: for become=True where running as root is not allowed
    """
    ...


def is_root() -> bool:
    """Whether the script itself runs as root (with sudo scriptling, say)."""
    ...


def require_root() -> None:
    """
    Stop the script unless it runs as root.

    For a script meant to run as a whole with sudo. A script that runs as a
    user and needs root for some steps passes become=True to them instead.
    """
    ...
