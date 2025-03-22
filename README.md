# Model Context Protocol Server for Zotero

This project is a Python server that implements the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) for [Zotero](https://www.zotero.org/), giving you access to your Zotero library within AI assistants. It uses the [pyzotero](https://github.com/urschrei/pyzotero) library to interact with Zotero's API, allowing AI assistants to search your Zotero library, retrieve metadata, and access full text content.

## Features

This MCP server provides the following tools:

- **Search functionality**
  - `zotero_search_items`: Search for items in your Zotero library by title, creator, or full text
  - `zotero_advanced_search`: Perform advanced searches with multiple criteria
  - `zotero_get_collections`: List all collections in your Zotero library
  - `zotero_get_collection_items`: Get all items in a specific collection
  - `zotero_get_tags`: Get all tags used in your Zotero library
  - `zotero_get_recent`: Get recently added items to your library

- **Item access**
  - `zotero_get_item_metadata`: Get detailed metadata for a specific item
  - `zotero_get_item_fulltext`: Get the full text content of a specific item
  - `zotero_get_item_children`: Get child items (attachments, notes) for a specific item



All tool responses are formatted using Markdown for optimal readability when used with AI assistants.

## Installation

### Using pip

```bash
pip install zotero-mcp
```

### From source

```bash
git clone https://github.com/yourusername/zotero-mcp.git
cd zotero-mcp
pip install -e .
```

## Configuration

The server can be configured through environment variables:

- `ZOTERO_LOCAL=true`: Use the local Zotero API (default: false)
- `ZOTERO_API_KEY`: Your Zotero API key (not required for the local API)
- `ZOTERO_LIBRARY_ID`: Your Zotero library ID (your user ID for user libraries, not required for the local API)
- `ZOTERO_LIBRARY_TYPE`: The type of library (user or group, default: user)

### Local Zotero Instance (Zotero 7+)

If you're running Zotero 7 or newer, you can use this server with the local API. Make sure to:

1. Enable the local API in Zotero's preferences
2. Set `ZOTERO_LOCAL=true` in your environment variables

> **Note:** For access to the fulltext API locally, you'll need Zotero 7 or newer. Earlier versions don't support this feature.

### Claude Desktop Integration

To use this with Claude Desktop, add the following to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "zotero": {
      "command": "zotero-mcp",
      "env": {
        "ZOTERO_LOCAL": "true"
      }
    }
  }
}
```

## Usage

Once configured, you can run the server directly:

```bash
zotero-mcp
```

Or run it with specific options:

```bash
zotero-mcp --transport stdio|sse
```

## Development

We welcome contributions! To set up a development environment:

```bash
# Clone the repository
git clone https://github.com/yourusername/zotero-mcp.git
cd zotero-mcp

# Install in development mode
pip install -e ".[dev]"

# Run tests
pytest
```

## License

MIT
