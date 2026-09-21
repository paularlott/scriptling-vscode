import * as vscode from 'vscode';

/**
 * IntelliSense for Scriptling's legacy MCP tool metadata files (`tools/*.toml`,
 * paired with a same-named `.py`). There is no bundled TOML language service in
 * this extension, so completions are offered on any `.toml` file via a
 * pattern-based document selector, with context inferred from the nearest
 * enclosing `[table]` / `[[array-of-tables]]` header.
 *
 * Field reference: /reference/libraries/mcp/writing-mcp-tools/
 */

interface FieldSpec {
    label: string;
    insertText: string;
    detail: string;
    documentation: string;
}

/** Top-level scalar fields of a tool `.toml`. */
const ROOT_FIELDS: FieldSpec[] = [
    {
        label: 'description',
        insertText: 'description = "$1"',
        detail: 'string (required)',
        documentation: 'Tool description shown to the AI.'
    },
    {
        label: 'keywords',
        insertText: 'keywords = [$1]',
        detail: 'string[] (optional)',
        documentation: 'Keywords for search (array of strings).'
    },
    {
        label: 'discoverable',
        insertText: 'discoverable = ${1|true,false|}',
        detail: 'boolean (optional, default false)',
        documentation:
            'Registration mode. `false` (default, native mode): the tool appears in `tools/list` and can be ' +
            'called directly. `true` (discovery mode): the tool is hidden from `tools/list`, searchable via ' +
            '`tool_search`, and callable via `execute_tool`.'
    }
];

/** Table headers offered at the root of a tool `.toml`. */
const ROOT_TABLES: FieldSpec[] = [
    {
        label: '[[parameters]]',
        insertText: '[[parameters]]\nname = "$1"\ntype = "$2"\ndescription = "$3"\nrequired = ${4|true,false|}\n',
        detail: 'array of tables (optional)',
        documentation: 'Declares one tool parameter. Repeat `[[parameters]]` for each parameter.'
    },
    {
        label: '[ui]',
        insertText: '[ui]\nresourceUri = "ui://$1"\n',
        detail: 'table (optional)',
        documentation:
            'Links this tool to a companion interactive HTML UI resource, per the ' +
            '[MCP Apps](https://github.com/modelcontextprotocol/ext-apps) extension. A compliant host renders ' +
            'the linked `ui://` resource in a sandboxed iframe; other hosts ignore it and the tool behaves as ' +
            'plain text. `resourceUri` and `visibility` are each optional, but at least one must be present — ' +
            'an `"app"`-only action tool (e.g. a form submission, only ever called by a view that\'s already ' +
            'open) typically declares `visibility` alone, with no `resourceUri` of its own.'
    },
    {
        label: '[[icons]]',
        insertText: '[[icons]]\nsrc = "$1"\n',
        detail: 'array of tables (optional)',
        documentation:
            'Attaches a visual identifier to this tool\'s `tools/list` descriptor. Repeat `[[icons]]` for ' +
            'multiple icons (e.g. different sizes or themes). Not required on every tool.'
    }
];

/** Fields inside a `[[parameters]]` entry. */
const PARAMETER_FIELDS: FieldSpec[] = [
    { label: 'name', insertText: 'name = "$1"', detail: 'string (required)', documentation: 'Parameter name.' },
    {
        label: 'type',
        insertText: 'type = "$1"',
        detail: 'string (required)',
        documentation: 'Parameter data type, e.g. `string`, `integer`, `number`, `boolean`, `array:string`.'
    },
    {
        label: 'description',
        insertText: 'description = "$1"',
        detail: 'string (required)',
        documentation: 'Description shown to the AI.'
    },
    {
        label: 'required',
        insertText: 'required = ${1|true,false|}',
        detail: 'boolean (optional, default false)',
        documentation: 'Whether the parameter must be provided.'
    }
];

const PARAMETER_TYPE_VALUES = [
    'string', 'integer', 'int', 'number', 'float', 'boolean', 'bool',
    'array:string', 'array:integer', 'array:int', 'array:number', 'array:float', 'array:boolean', 'array:bool'
];

/** Fields inside the `[ui]` table (MCP Apps extension linkage). */
const UI_FIELDS: FieldSpec[] = [
    {
        label: 'resourceUri',
        insertText: 'resourceUri = "ui://$1"',
        detail: 'string (optional — at least one of resourceUri/visibility required)',
        documentation:
            'URI of the companion `ui://` resource (served with mimeType `text/html;profile=mcp-app`) that a ' +
            'compliant host renders in a sandboxed iframe. Omit it for an `"app"`-only action tool with no view ' +
            'of its own — one only ever called by a view that\'s already open, such as a form submission.'
    },
    {
        label: 'visibility',
        insertText: 'visibility = [$1]',
        detail: 'string[] (optional, default ["model", "app"])',
        documentation:
            'Which surfaces can see this tool: `"model"` (the LLM), `"app"` (the rendered UI), or both. ' +
            'Omit to accept the default of both.'
    }
];

const UI_VISIBILITY_VALUES = ['model', 'app'];

/** Fields inside an `[[icons]]` entry. */
const ICON_FIELDS: FieldSpec[] = [
    {
        label: 'src',
        insertText: 'src = "$1"',
        detail: 'string (required)',
        documentation: 'The icon\'s location: an `https://` URL or a `data:` URI.'
    },
    {
        label: 'mimeType',
        insertText: 'mimeType = "$1"',
        detail: 'string (optional)',
        documentation: 'The icon\'s media type, e.g. `image/png`. Useful when it can\'t be inferred from `src`.'
    },
    {
        label: 'sizes',
        insertText: 'sizes = [$1]',
        detail: 'string[] (optional)',
        documentation: 'Size hints such as `"48x48"`, or `"any"` for a scalable format like SVG.'
    },
    {
        label: 'theme',
        insertText: 'theme = "$1"',
        detail: 'string (optional)',
        documentation: 'Preferred host theme for this icon: `"light"` or `"dark"`. Omit for a theme-neutral icon.'
    }
];

const ICON_THEME_VALUES = ['light', 'dark'];

const TABLE_HEADER_PATTERN = /^\s*\[\[?\s*([^\]\s]+)\s*\]?\]\s*$/;

/**
 * Finds the name of the TOML table (`[name]` or `[[name]]`) enclosing the given
 * line, by scanning upward from `fromLine` for the nearest preceding table
 * header. Returns `undefined` when `fromLine` is at the document root (before
 * any table header).
 *
 * Exported for unit testing independent of the `vscode` API.
 */
export function findEnclosingTable(lines: string[], fromLine: number): string | undefined {
    for (let i = Math.min(fromLine, lines.length - 1); i >= 0; i--) {
        const match = lines[i].match(TABLE_HEADER_PATTERN);
        if (match) {
            return match[1];
        }
    }
    return undefined;
}

function toCompletionItem(field: FieldSpec, kind: vscode.CompletionItemKind): vscode.CompletionItem {
    const item = new vscode.CompletionItem(field.label, kind);
    item.insertText = new vscode.SnippetString(field.insertText);
    item.detail = field.detail;
    item.documentation = new vscode.MarkdownString(field.documentation);
    return item;
}

/** True when `linePrefix` has an odd number of `"` characters, i.e. the cursor is inside an open string. */
function isInsideString(linePrefix: string): boolean {
    const quoteCount = (linePrefix.match(/"/g) || []).length;
    return quoteCount % 2 === 1;
}

function enumCompletionItem(value: string, quoted: boolean): vscode.CompletionItem {
    const item = new vscode.CompletionItem(quoted ? `"${value}"` : value, vscode.CompletionItemKind.EnumMember);
    item.insertText = quoted ? `"${value}"` : value;
    item.filterText = value;
    return item;
}

export class ToolMetadataCompletionProvider implements vscode.CompletionItemProvider {
    provideCompletionItems(
        document: vscode.TextDocument,
        position: vscode.Position
    ): vscode.ProviderResult<vscode.CompletionItem[]> {
        const linePrefix = document.lineAt(position.line).text.slice(0, position.character);
        const lines: string[] = [];
        for (let i = 0; i < position.line; i++) {
            lines.push(document.lineAt(i).text);
        }
        const table = findEnclosingTable(lines, position.line - 1);

        // Inside `visibility = [...]` in the [ui] table: suggest "model" / "app".
        if (table === 'ui' && /visibility\s*=\s*\[[^\]]*$/.test(linePrefix)) {
            const quoted = !isInsideString(linePrefix);
            return UI_VISIBILITY_VALUES.map(value => enumCompletionItem(value, quoted));
        }

        // Inside `type = "..."` in a [[parameters]] entry: suggest known parameter types.
        if (table === 'parameters' && /type\s*=\s*"[^"]*$/.test(linePrefix)) {
            return PARAMETER_TYPE_VALUES.map(value => enumCompletionItem(value, false));
        }

        // Inside `theme = "..."` in an [[icons]] entry: suggest "light" / "dark".
        if (table === 'icons' && /theme\s*=\s*"[^"]*$/.test(linePrefix)) {
            return ICON_THEME_VALUES.map(value => enumCompletionItem(value, false));
        }

        if (table === 'ui') {
            return UI_FIELDS.map(f => toCompletionItem(f, vscode.CompletionItemKind.Property));
        }

        if (table === 'parameters') {
            return PARAMETER_FIELDS.map(f => toCompletionItem(f, vscode.CompletionItemKind.Property));
        }

        if (table === 'icons') {
            return ICON_FIELDS.map(f => toCompletionItem(f, vscode.CompletionItemKind.Property));
        }

        if (table === undefined) {
            return [
                ...ROOT_FIELDS.map(f => toCompletionItem(f, vscode.CompletionItemKind.Property)),
                ...ROOT_TABLES.map(f => toCompletionItem(f, vscode.CompletionItemKind.Struct))
            ];
        }

        return undefined;
    }
}

export function registerToolMetadataCompletions(context: vscode.ExtensionContext): void {
    // Scoped to the conventional directory layouts this metadata actually
    // lives in (tools/*.toml, prompts/*.toml, resources/**/_{stem}.toml
    // sidecars — see mimeType/[ui] above) rather than every .toml in the
    // workspace: an unrelated file like Cargo.toml or pyproject.toml would
    // otherwise get these fields suggested too.
    const selector: vscode.DocumentSelector = [
        { pattern: '**/{tools,prompts}/*.toml' },
        { pattern: '**/resources/**/_*.toml' },
    ];
    context.subscriptions.push(
        vscode.languages.registerCompletionItemProvider(selector, new ToolMetadataCompletionProvider(), '[', '"', '=')
    );
}
