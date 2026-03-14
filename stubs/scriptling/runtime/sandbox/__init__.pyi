"""
Scriptling Runtime Sandbox Library - Type stubs for IntelliSense support.

Isolated script execution environments for running untrusted or
sandboxed code with controlled variable scope.
"""

from typing import Optional, Any

class Sandbox:
    """
    Isolated script execution environment.

    Sandboxes provide a fresh execution context with its own variable scope.
    The sandbox inherits the same library registrations and import paths as
    the parent, but variables are completely isolated.
    """

    def set(self, name: str, value: Any) -> None:
        """
        Set a variable in the sandbox.

        Parameters:
            name: Variable name
            value: Variable value
        """
        ...

    def get(self, name: str) -> Any:
        """
        Get a variable from the sandbox.

        Parameters:
            name: Variable name

        Returns:
            Variable value, or None if not found
        """
        ...

    def exec(self, code: str) -> None:
        """
        Execute script code in the sandbox.

        Parameters:
            code: Script code to execute
        """
        ...

    def exec_file(self, path: str) -> None:
        """
        Load and execute a script file in the sandbox.

        Parameters:
            path: Path to script file
        """
        ...

    def exit_code(self) -> int:
        """
        Get the exit code from the last execution.

        Returns:
            Exit code (0 = success, non-zero = error)
        """
        ...

def create(capture_output: bool = False) -> Sandbox:
    """
    Create a new isolated sandbox environment.

    Creates a fresh script execution environment with its own variable scope.
    The sandbox inherits the same library registrations and import paths as
    the parent, but variables are completely isolated.

    By default, print output from the sandbox is discarded. Set capture_output=True
    to capture output (retrievable via the sandbox's output methods).

    Requires the host application to configure a sandbox factory via
    extlibs.SetSandboxFactory() in Go. Available in CLI mode by default.

    Parameters:
        capture_output: If True, capture print output. Default: False

    Returns:
        Sandbox object with set(), get(), exec(), exec_file(), and exit_code() methods

    Example:
        import scriptling.runtime.sandbox as sandbox

        env = sandbox.create()
        env.set("config", {"debug": True})
        env.exec("result = config['debug']")
        print(env.get("result"))  # True
    """
    ...
