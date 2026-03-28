"""
Scriptling Console Library - Type stubs for IntelliSense support.

This library provides a TUI-based console for building interactive
chat-style applications with streaming output, spinners, progress bars,
and multi-panel layouts.

All functions are module-level (no Console class).
"""

from typing import Optional, Callable, Any, List

# Color constants
PRIMARY: str
SECONDARY: str
ERROR: str
DIM: str
USER: str
TEXT: str

class Panel:
    """
    A content panel within the TUI layout.

    Panels support both raw text content (write, set_content) and
    message-based content (add_message, streaming).
    """

    def write(self, text: str) -> None:
        """
        Append text to the panel.

        Parameters:
            text: Text to append
        """
        ...

    def set_content(self, text: str) -> None:
        """
        Replace all panel content.

        Parameters:
            text: New content
        """
        ...

    def clear(self) -> None:
        """
        Remove all panel content.
        """
        ...

    def set_title(self, title: str) -> None:
        """
        Set the panel border title.

        Parameters:
            title: Title text (empty string hides title)
        """
        ...

    def set_color(self, color: str) -> None:
        """
        Set the panel border/accent color.

        Parameters:
            color: Color name (primary, secondary, error, dim, user, text) or hex (#RRGGBB)
        """
        ...

    def set_scrollable(self, scrollable: bool) -> None:
        """
        Set whether panel content scrolls.

        Parameters:
            scrollable: True = content scrolls, False = fixed viewport
        """
        ...

    def add_message(self, *args: Any, label: str = "") -> None:
        """
        Add a message to the panel.

        Parameters:
            *args: Values to display (joined with spaces)
            label: Optional label prefix for the message
        """
        ...

    def stream_start(self, label: str = "") -> None:
        """
        Begin a streaming message in this panel.

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

    def scroll_to_top(self) -> None:
        """
        Scroll to top of panel content.
        """
        ...

    def scroll_to_bottom(self) -> None:
        """
        Scroll to bottom of panel content.
        """
        ...

    def size(self) -> List[int]:
        """
        Get the panel dimensions.

        Returns:
            List of [width, height]
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

    def write_at(self, row: int, col: int, text: str) -> None:
        """
        Write text at a specific position (0-indexed).

        Parameters:
            row: Row index
            col: Column index
            text: Text to write
        """
        ...

    def clear_line(self, row: int) -> None:
        """
        Clear a specific line.

        Parameters:
            row: Row index to clear
        """
        ...

    def add_row(self, panel: "Panel") -> None:
        """
        Add a child panel as a vertical row (top to bottom).

        Parameters:
            panel: Panel to add as a row
        """
        ...

    def add_column(self, panel: "Panel") -> None:
        """
        Add a child panel as a horizontal column (left to right).

        Parameters:
            panel: Panel to add as a column
        """
        ...

# Module-level functions

def panel(name: str = "main") -> Optional[Panel]:
    """
    Get an existing Panel instance by name.

    Parameters:
        name: Panel name

    Returns:
        Panel instance, or None if not found
    """
    ...

def main_panel() -> Panel:
    """
    Get the main panel.

    Returns:
        The main Panel instance
    """
    ...

def create_panel(
    name: str = "",
    *,
    width: int = 0,
    height: int = 0,
    min_width: int = 0,
    scrollable: bool = False,
    title: str = "",
    no_border: bool = False,
    skip_focus: bool = False,
) -> Panel:
    """
    Create a new panel (independent of layout).

    Create panels first, then attach them to the layout with
    add_left, add_right, add_row, or add_column.

    Parameters:
        name: Panel identifier
        width: Panel width (positive=columns, negative=percentage)
        height: Panel height (positive=rows, negative=percentage)
        min_width: Minimum width to render
        scrollable: True = content scrolls
        title: Border title
        no_border: True = hide border
        skip_focus: True = exclude from Tab focus cycle

    Returns:
        Panel instance
    """
    ...

def add_left(panel: Panel) -> None:
    """
    Add a panel to the left of the main panel.

    Parameters:
        panel: Panel to add
    """
    ...

def add_right(panel: Panel) -> None:
    """
    Add a panel to the right of the main panel.

    Parameters:
        panel: Panel to add
    """
    ...

def clear_layout() -> None:
    """
    Remove the layout tree but keep all panels and their content.

    Panels can be re-added with add_left/add_right to toggle layouts.
    """
    ...

def has_panels() -> bool:
    """
    Check if multi-panel layout is active.

    Returns:
        True if multi-panel layout is active
    """
    ...

def styled(color: str, text: str) -> str:
    """
    Apply theme color to text.

    Parameters:
        color: Color name (primary, secondary, error, dim, user, text, or #RRGGBB)
        text: Text to style

    Returns:
        Styled text string
    """
    ...

def set_status(left: str, right: str) -> None:
    """
    Set both status bar texts.

    Parameters:
        left: Left status text
        right: Right status text
    """
    ...

def set_status_left(text: str) -> None:
    """
    Set left status bar text.

    Parameters:
        text: Status text
    """
    ...

def set_status_right(text: str) -> None:
    """
    Set right status bar text.

    Parameters:
        text: Status text
    """
    ...

def set_labels(user: str, assistant: str, system: str) -> None:
    """
    Set role labels.

    Parameters:
        user: User role label
        assistant: Assistant role label
        system: System role label
    """
    ...

def register_command(name: str, description: str, fn: Callable[[str], None]) -> None:
    """
    Register a slash command.

    Parameters:
        name: Command name (without leading /)
        description: Command description
        fn: Handler function called with command arguments
    """
    ...

def remove_command(name: str) -> None:
    """
    Remove a registered slash command.

    Parameters:
        name: Command name to remove
    """
    ...

def on_submit(fn: Callable[[str], None]) -> None:
    """
    Register handler called when user submits input.

    Parameters:
        fn: Callback function receiving the submitted text
    """
    ...

def on_escape(fn: Callable[[], None]) -> None:
    """
    Register a callback for Esc key.

    Parameters:
        fn: Callback function
    """
    ...

def spinner_start(text: str = "Working") -> None:
    """
    Show a spinner with text.

    Parameters:
        text: Text to display next to spinner
    """
    ...

def spinner_stop() -> None:
    """
    Hide the spinner.
    """
    ...

def set_progress(label: str, pct: float) -> None:
    """
    Set progress bar (0.0-1.0, or <0 to clear).

    Parameters:
        label: Progress label
        pct: Progress percentage (0.0 to 1.0)
    """
    ...

def run() -> None:
    """
    Start the console event loop (blocks until exit).
    """
    ...
