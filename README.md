# Zotero Web MCP: Your Research Library in Claude

<p align="center">
  <a href="https://www.zotero.org/">
    <img src="https://img.shields.io/badge/Zotero-CC2936?style=for-the-badge&logo=zotero&logoColor=white" alt="Zotero">
  </a>
  <a href="https://www.anthropic.com/claude">
    <img src="https://img.shields.io/badge/Claude-6849C3?style=for-the-badge&logo=anthropic&logoColor=white" alt="Claude">
  </a>
  <a href="https://modelcontextprotocol.io/introduction">
    <img src="https://img.shields.io/badge/MCP-0175C2?style=for-the-badge&logoColor=white" alt="MCP">
  </a>
</p>

**Zotero Web MCP** seamlessly connects your [Zotero](https://www.zotero.org/) research library with [Claude](https://www.anthropic.com/claude) and other AI assistants ([Cherry Studio](https://cherry-ai.com/), [Cursor](https://www.cursor.com/), etc.) via the [Model Context Protocol](https://modelcontextprotocol.io/introduction). Uses Zotero's Web API for full read/write access to your library. Discuss papers, get summaries, analyze citations, create items, and more!

## ✨ Features

### 🔍 Search Your Library

- Find papers, articles, and books by title, author, or content
- Perform complex searches with multiple criteria
- Browse collections, tags, and recent additions

### 📚 Access Your Content

- Retrieve detailed metadata for any item
- Get full text content (when available)
- Access attachments, notes, and child items

### 📝 Work with Annotations

- Extract and search PDF annotations directly
- Access Zotero's native annotations
- Create and update notes and annotations

## 🚀 Quick Install

### Installing via Smithery

To install Zotero MCP for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@raminos/zotero-web-mcp):

```bash
npx -y @smithery/cli install @raminos/zotero-web-mcp --client claude
```

### Manual Installation

#### Installing via uv

```bash
uv tool install "git+https://github.com/raminos/zotero-web-mcp.git"
zotero-web-mcp setup  # Auto-configure for Claude Desktop
```

#### Installing via pip

```bash
pip install git+https://github.com/raminos/zotero-web-mcp.git
zotero-web-mcp setup  # Auto-configure for Claude Desktop
```

## 🖥️ Setup & Usage

Full documentation is available at [Zotero MCP docs](https://stevenyuyy.us/zotero-web-mcp/).

**Requirements**

- Python 3.10+
- Zotero 7+ (for local API with full-text access)
- Claude Desktop or compatible AI assistant

### For Claude Desktop

#### Configuration

After installation, either:

1. **Auto-configure** (recommended):

   ```bash
   zotero-web-mcp setup
   ```

2. **Manual configuration**:
   Add to your `claude_desktop_config.json`:
   ```json
   {
     "mcpServers": {
       "zotero": {
         "command": "zotero-web-mcp",
         "env": {
           "ZOTERO_LIBRARY_TYPE": "user",
           "ZOTERO_LIBRARY_ID": "0000000",
           "ZOTERO_API_KEY": "XXXXXXXXXXXXXXXXXXXXXXXX"
         }
       }
     }
   }
   ```

#### Usage

1. Start Zotero desktop (make sure local API is enabled in preferences)
2. Launch Claude Desktop
3. Access the zotero-web-mcp tool through Claude Desktop's tools interface

Example prompts:

- "Search my library for papers on machine learning"
- "Find recent articles I've added about climate change"
- "Summarize the key findings from my paper on quantum computing"
- "Extract all PDF annotations from my paper on neural networks"
- "Search my notes and annotations for mentions of 'reinforcement learning'"
- "Show me papers tagged '#Arm' excluding those with '#Crypt' in my library"
- "Search for papers on operating system with tag '#Arm'"
- "Export the BibTeX citation for papers on machine learning"

### For Cherry Studio

#### Configuration

Go to Settings -> MCP Servers -> Edit MCP Configuration, and add the following:

```json
{
  "mcpServers": {
    "zotero": {
      "name": "zotero",
      "type": "stdio",
      "isActive": true,
      "command": "zotero-web-mcp",
      "args": [],
      "env": {
        "ZOTERO_LIBRARY_TYPE": "user",
        "ZOTERO_LIBRARY_ID": "0000000",
        "ZOTERO_API_KEY": "XXXXXXXXXXXXXXXXXXXXXXXX"
      }
    }
  }
}
```

Then click "Save".

Cherry Studio also provides a visual configuration method for general settings and tools selection.

## 🔧 Advanced Configuration

### Using Web API Instead of Local API

For accessing your Zotero library via the web API (useful for remote setups):

```bash
zotero-web-mcp setup --api-key YOUR_API_KEY --library-id YOUR_LIBRARY_ID
```

### Environment Variables

- `ZOTERO_API_KEY`: Your Zotero API key (for web API)
- `ZOTERO_LIBRARY_ID`: Your Zotero library ID (for web API)
- `ZOTERO_LIBRARY_TYPE`: The type of library (user or group, default: user)

### Command-Line Options

```bash
# Run the server directly
zotero-web-mcp serve

# Specify transport method
zotero-web-mcp serve --transport stdio|streamable-http|sse

# Get help on setup options
zotero-web-mcp setup --help
```

## 📑 PDF Annotation Extraction

Zotero MCP includes advanced PDF annotation extraction capabilities:

- **Direct PDF Processing**: Extract annotations directly from PDF files, even if they're not yet indexed by Zotero
- **Enhanced Search**: Search through PDF annotations and comments
- **Image Annotation Support**: Extract image annotations from PDFs
- **Seamless Integration**: Works alongside Zotero's native annotation system

For optimal annotation extraction, it is **highly recommended** to install the [Better BibTeX plugin](https://retorque.re/zotero-better-bibtex/installation/) for Zotero. The annotation-related functions have been primarily tested with this plugin and provide enhanced functionality when it's available.

The first time you use PDF annotation features, the necessary tools will be automatically downloaded.

## 📚 Available Tools

### Search Tools

- `zotero_search_items`: Search your library
- `zotero_advanced_search`: Perform complex searches
- `zotero_get_collections`: List collections
- `zotero_get_collection_items`: Get items in a collection
- `zotero_get_tags`: List all tags
- `zotero_get_recent`: Get recently added items
- `zotero_search_by_tag`: Search your library using custom tag filters

### Content Tools

- `zotero_get_item_metadata`: Get detailed metadata (supports BibTeX export via `format="bibtex"`)
- `zotero_get_item_fulltext`: Get full text content
- `zotero_get_item_children`: Get attachments and notes

### Annotation & Notes Tools

- `zotero_get_annotations`: Get annotations (including direct PDF extraction)
- `zotero_get_notes`: Retrieve notes from your Zotero library
- `zotero_search_notes`: Search in notes and annotations (including PDF-extracted)
- `zotero_create_note`: Create a new note for an item (beta feature)

## 🔍 Troubleshooting

- **No results found**: Ensure Zotero is running and the local API is enabled
- **Can't connect to library**: Check your API key and library ID if using web API
- **Full text not available**: Make sure you're using Zotero 7+ for local full-text access

## 📄 License

MIT
