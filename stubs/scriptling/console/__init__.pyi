"""
Scriptling Console Library - Type stubs for IntelliSense support.

This library provides a TUI-based console for building interactive
chat-style applications with streaming output, spinners, and progress bars.
"""

from typing import Optional, Callable, Any

# Color constants
PRIMARY: str
SECONDARY: str
ERROR: str
DIM: str
USER: str
TEXT: str

class Console:
    """
    Interactive console with TUI backend.

    Provides a chat-style interface with streaming output, spinners,
    progress bars, and slash command support.
    """

    def __init__(self) -> None:
        """
        Create a new Console instance backed by a TUI.
        """
        ...

    def add_message(self, *args: Any, label: str = "") -> None:
        """
        Add a message to the output area.

        Parameters:
            *args: Values to display (joined with spaces)
            label: Optional label prefix for the message
        """
        ...

    def stream_start(self, label: str = "") -> None:
        """
        Begin a streaming message.

        Parameters:
            label: Optional label prefix for the stream
        """
        ...

    def stream_chunk(self, text: str) -> None:
        """
        Append a chunk to the current stream.

        Parameters:
            text: Text chunk to append
        """
        ...

    def stream_end(self) -> None:
        """
        Finalize the current stream.
        """
        ...

    def spinner_start(self, text: str = "Working") -> None:
        """
        Show a spinner with text.

        Parameters:
            text: Text to display next to spinner
        """
        ...

    def spinner_stop(self) -> None:
        """
        Hide the spinner.
        """
        ...

    def set_progress(self, label: str, pct: float) -> None:
        """
        Set progress bar (0.0-1.0, or <0 to clear).

        Parameters:
            label: Progress label
            pct: Progress percentage (0.0 to 1.0)
        """
        ...

    def set_labels(self, user: str, assistant: str, system: str) -> None:
        """
        Set role labels.

        Parameters:
            user: User role label
            assistant: Assistant role label
            system: System role label
        """
        ...

    def set_status(self, left: str, right: str) -> None:
        """
        Set both status bar texts.

        Parameters:
            left: Left status text
            right: Right status text
        """
        ...

    def set_status_left(self, text: str) -> None:
        """
        Set left status bar text.

        Parameters:
            text: Status text
        """
        ...

    def set_status_right(self, text: str) -> None:
        """
        Set right status bar text.

        Parameters:
            text: Status text
        """
        ...

    def register_command(self, name: str, description: str, fn: Callable[[str], None]) -> None:
        """
        Register a slash command.

        Parameters:
            name: Command name (without leading /)
            description: Command description
            fn: Handler function called with command arguments
        """
        ...

    def remove_command(self, name: str) -> None:
        """
        Remove a registered slash command.

        Parameters:
            name: Command name to remove
        """
        ...

    def clear_output(self) -> None:
        """
        Clear the output area.
        """
        ...

    def styled(self, color: str, text: str) -> str:
        """
        Apply theme color to text.

        Parameters:
            color: Color name (primary, secondary, error, dim, user, text, or #RRGGBB)
            text: Text to style

        Returns:
            Styled text string
        """
        ...

    def on_escape(self, fn: Callable[[], None]) -> None:
        """
        Register a callback for Esc key.

        Parameters:
            fn: Callback function
        """
        ...

    def on_submit(self, fn: Callable[[str], None]) -> None:
        """
        Register handler called when user submits input.

        Parameters:
            fn: Callback function receiving the submitted text
        """
        ...

    def run(self) -> None:
        """
        Start the console event loop (blocks until exit).
        """
        ...
