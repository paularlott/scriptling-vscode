"""
Scriptling Template HTML Library - Type stubs for IntelliSense support.

Go html/template rendering with automatic HTML escaping.
"""

from typing import Any


class Set:
    """
    An HTML template set. Add template sources with add(), render with render().
    Values are automatically HTML-escaped when rendered.
    """

    def add(self, source: str) -> None:
        """
        Add a template source to the set.

        Parameters:
            source: Template source, may contain {{define "name"}}...{{end}} blocks

        Example:
            tmpl.add('{{define "header"}}<h1>{{.Title}}</h1>{{end}}')
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
            Rendered HTML string (values are auto-escaped)

        Example:
            # Anonymous template
            tmpl.render({"Name": "Alice"})

            # Named template
            tmpl.render("page", {"Title": "Home", "Body": "Welcome"})
        """
        ...


def Set() -> Set:
    """
    Create a new HTML template set (uses html/template with auto-escaping).

    Returns:
        Set: A template set

    Example:
        import scriptling.template.html as html

        # Simple template
        tmpl = html.Set()
        tmpl.add("Hello, {{.Name}}!")
        print(tmpl.render({"Name": "Alice"}))

        # With partials
        tmpl = html.Set()
        tmpl.add('{{define "header"}}<h1>{{.Title}}</h1>{{end}}')
        tmpl.add('{{define "page"}}{{template "header" .}}<p>{{.Body}}</p>{{end}}')
        print(tmpl.render("page", {"Title": "Home", "Body": "Welcome"}))

        # From file
        import os
        tmpl = html.Set()
        tmpl.add(os.read_file("templates/page.html"))
        print(tmpl.render({"Title": "Home"}))
    """
    ...
