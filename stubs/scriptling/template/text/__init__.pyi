"""
Scriptling Template Text Library - Type stubs for IntelliSense support.

Go text/template rendering with no HTML escaping.
"""

from typing import Any


class Set:
    """
    A text template set. Add template sources with add(), render with render().
    No HTML escaping is applied.
    """

    def add(self, source: str) -> None:
        """
        Add a template source to the set.

        Parameters:
            source: Template source, may contain {{define "name"}}...{{end}} blocks

        Example:
            tmpl.add('{{define "greeting"}}Hello, {{.Name}}!{{end}}')
        """
        ...

    def render(self, *args: Any) -> str:
        """
        Render a template from the set.

        Signatures:
            render(data)         - render the anonymous/default template
            render(name, data)   - render a named template (from {{define "name"}})

        Parameters:
            name (str, optional): Template name defined with {{define "name"}}
            data (dict): Template data

        Returns:
            Rendered string

        Example:
            # Anonymous template
            tmpl.render({"Name": "Alice"})

            # Named template
            tmpl.render("email", {"Name": "Alice", "Product": "Scriptling Pro"})
        """
        ...


def Set(*, left: str = "{{", right: str = "}}") -> Set:
    """
    Create a new text template set (uses text/template, no HTML escaping).

    Parameters:
        left: Left action delimiter (default "{{"). Pass an empty string to
            keep the default.
        right: Right action delimiter (default "}}"). Pass an empty string to
            keep the default.

    Returns:
        Set: A template set

    Example:
        import scriptling.template.text as text

        # Simple template
        tmpl = text.Set()
        tmpl.add("Hello, {{.Name}}!")
        print(tmpl.render({"Name": "Alice"}))

        # With partials
        tmpl = text.Set()
        tmpl.add('{{define "greeting"}}Hello, {{.Name}}!{{end}}')
        tmpl.add('{{define "email"}}{{template "greeting" .}}\\n\\nYour order is ready.{{end}}')
        print(tmpl.render("email", {"Name": "Alice"}))

        # Custom delimiters, e.g. to keep {{ }} literally in the output
        tmpl = text.Set(left="{%", right="%}")
        tmpl.add("Hello, {%.Name%}! Config: {{ service.tag }}")
        print(tmpl.render({"Name": "Alice"}))

        # From file
        import os
        tmpl = text.Set()
        tmpl.add(os.read_file("templates/email.txt"))
        print(tmpl.render({"Name": "Alice"}))
    """
    ...
