# Scriptling VSCode Extension

VSCode extension providing IntelliSense and language support for [Scriptling](https://github.com/paularlott/scriptling) extension libraries.

## Overview

Scriptling is a Python-like scripting language for LLM agents. This extension enhances the VSCode Python extension by providing type stubs and IntelliSense for Scriptling's extension libraries:

- **scriptling.ai** - AI/LLM library for OpenAI, Claude, Gemini, Ollama, ZAI, and Mistral
- **scriptling.mcp** - Model Context Protocol client library
- **scriptling.fuzzy** - Fuzzy string matching utilities
- **scriptling.ai.agent** - AI agent with tool-calling capabilities

## Features

- **IntelliSense** - Autocomplete for all Scriptling extension library functions and classes
- **Type hints** - Full type annotations for better code intelligence
- **Documentation** - Inline documentation for all APIs
- **Auto-configuration** - Automatically configures Python analysis settings

## Installation

### From VSCode Marketplace

1. Open VSCode
2. Go to Extensions (Cmd+Shift+X / Ctrl+Shift+X)
3. Search for "Scriptling"
4. Click Install

### From VSIX File

1. Download the `.vsix` file from [Releases](https://github.com/paularlott/scriptling-vscode/releases)
2. Open VSCode
3. Go to Extensions (Cmd+Shift+X / Ctrl+Shift+X)
4. Click the "..." menu → "Install from VSIX..."
5. Select the downloaded file

### Manual Installation

```bash
# Clone the repository
git clone https://github.com/paularlott/scriptling-vscode.git
cd scriptling-vscode

# Install dependencies
npm install

# Build the extension
npm run compile

# Package as VSIX
npm run package

# Install the VSIX
code --install-extension scriptling-0.1.0.vsix
```

## Building from Source

### Prerequisites

- Node.js 18+ and npm
- VSCode 1.85+

### Build Steps

```bash
# Clone the repository
git clone https://github.com/paularlott/scriptling-vscode.git
cd scriptling-vscode

# Install dependencies
npm install

# Compile TypeScript
npm run compile

# Watch for changes during development
npm run watch
```

### Packaging

```bash
# Create a .vsix package
npm run package
```

This creates `scriptling-0.1.0.vsix` (version from package.json).

## Usage

Once installed, the extension automatically activates when you open Python files. It configures VSCode's Python extension to use the bundled type stubs for Scriptling libraries.

### Example Code with IntelliSense

```python
import scriptling.ai as ai
import scriptling.mcp as mcp
import scriptling.fuzzy as fuzzy
from scriptling.ai.agent import Agent

# AI client with autocomplete
client = ai.Client(
    "",
    provider=ai.OPENAI,
    api_key="sk-...",
    max_tokens=2048,
    temperature=0.7
)

# Completion with type hints
response = client.completion("gpt-4", "Hello!")
print(response.choices[0].message.content)

# MCP client
mcp_client = mcp.Client("https://api.example.com/mcp", namespace="tools")
tools = mcp_client.tools()

# Fuzzy search
results = fuzzy.search("proj", ["Project Alpha", "Project Beta"])

# Agent with tools
tools = ai.ToolRegistry()
tools.add("get_time", "Get current time", {}, lambda args: "12:00 PM")
agent = Agent(client, tools=tools, model="gpt-4")
```

## Configuration

The extension contributes the following settings:

| Setting | Description | Default |
|---------|-------------|---------|
| `scriptling.stubPath` | Custom path to Scriptling type stubs (optional) | `""` (uses bundled stubs) |

## Project Structure

```
scriptling-vscode/
├── src/
│   └── extension.ts      # Extension entry point
├── stubs/
│   └── scriptling/
│       ├── __init__.pyi
│       ├── ai/
│       │   ├── __init__.pyi
│       │   └── agent.pyi
│       ├── mcp/
│       │   └── __init__.pyi
│       └── fuzzy/
│           └── __init__.pyi
├── package.json          # Extension manifest
├── tsconfig.json         # TypeScript configuration
└── README.md
```

## Updating Type Stubs

When the Scriptling library APIs change, update the corresponding `.pyi` files in the `stubs/scriptling/` directory. The stubs follow standard Python type hint syntax.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines.

## License

MIT License - see [LICENSE.txt](LICENSE.txt) for details.

## Related Projects

- [Scriptling](https://github.com/paularlott/scriptling) - The Scriptling interpreter
- [MCP Go Library](https://github.com/paularlott/mcp) - Model Context Protocol implementation
