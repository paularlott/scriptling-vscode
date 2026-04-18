# Scriptling VSCode Extension

VSCode extension providing IntelliSense and language support for [Scriptling](https://scriptling.dev/) libraries.

## Overview

Scriptling is a Python-like scripting language for LLM agents. This extension enhances the VSCode Python extension by providing type stubs and IntelliSense for Scriptling's extension libraries:

- **scriptling.ai** - AI/LLM library for OpenAI, Claude, Gemini, Ollama, ZAI, and Mistral
- **scriptling.mcp** - Model Context Protocol client library
- **scriptling.similarity** - String matching and similarity utilities including fuzzy search and MinHash
- **scriptling.secret** - Provider-agnostic secret access through host-configured aliases
- **scriptling.ai.agent** - AI agent with tool-calling capabilities
- **scriptling.ai.tools** - AI tool registry and utilities
- **scriptling.ai.memory** - AI memory/context management
- **scriptling.console** - Console output and formatting utilities
- **scriptling.runtime** - Runtime environment APIs (http, kv, sync, sandbox)
- **scriptling.toon** - Animation utilities
- **scriptling.wait_for** - Async wait utilities

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

### From Source

```bash
git clone https://github.com/paularlott/scriptling-vscode.git
cd scriptling-vscode
npm install
npm run compile
npm run package
code --install-extension scriptling-x.x.x.vsix
```

Or use Task/Make:

```bash
task package    # Build and package
task release    # Tag + GitHub release
task publish    # Publish to VSCode Marketplace
```

## Usage

Once installed, the extension automatically activates when you open Python files and provides IntelliSense for Scriptling libraries.

```python
import scriptling.ai as ai
from scriptling.ai.agent import Agent

# AI client with autocomplete
client = ai.Client(
    "",
    provider=ai.OPENAI,
    api_key="sk-...",
    max_tokens=2048,
    temperature=0.7
)

response = client.completion("gpt-4", "Hello!")
print(response.choices[0].message.content)

# Agent with tools
tools = ai.ToolRegistry()
tools.add("get_time", "Get current time", {}, lambda args: "12:00 PM")
agent = Agent(client, tools=tools, model="gpt-4")
```

## Configuration

| Setting | Description | Default |
|---------|-------------|---------|
| `scriptling.stubPath` | Custom path to Scriptling type stubs | `""` (uses bundled stubs) |

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines.

## License

MIT License - see [LICENSE.txt](LICENSE.txt) for details.

## Related Projects

- [Scriptling](https://github.com/paularlott/scriptling) - The Scriptling interpreter
