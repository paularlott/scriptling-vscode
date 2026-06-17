"""
Scriptling Markdown Library - Type stubs for IntelliSense support.

Provides Markdown parsing and conversion to HTML using the
GitHub Flavored Markdown (GFM) specification.

Usage:
    import scriptling.markdown as markdown

    html = markdown.to_html("# Hello\\n\\nThis is **bold**.")
"""


def to_html(markdown_string: str) -> str:
    """
    Convert a Markdown string to HTML.

    Converts Markdown source to an HTML string using GitHub Flavored Markdown
    (GFM). Supports headings, bold, italic, code blocks, fenced code,
    blockquotes, ordered and unordered lists, tables, strikethrough, task
    lists, and auto-linked URLs.

    Parameters:
        markdown_string: The Markdown source to convert.

    Returns:
        HTML representation of the Markdown input.

    Example:
        import scriptling.markdown as markdown

        html = markdown.to_html("# Hello\\n\\nThis is **bold** and _italic_.")
        # <h1 id="hello">Hello</h1>
        # <p>This is <strong>bold</strong> and <em>italic</em>.</p>

        html = markdown.to_html("- item one\\n- item two")
        # <ul>
        # <li>item one</li>
        # <li>item two</li>
        # </ul>

        html = markdown.to_html("| Col A | Col B |\\n|---|---|\\n| 1 | 2 |")
        # <table>...
    """
    ...
