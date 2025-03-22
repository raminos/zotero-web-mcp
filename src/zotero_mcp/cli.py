"""
Command-line interface for Zotero MCP server.
"""

import argparse
import sys

from zotero_mcp.server import mcp


def main():
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(
        description="Zotero Model Context Protocol server"
    )
    parser.add_argument(
        "--transport",
        choices=["stdio", "sse"],
        default="stdio",
        help="Transport to use (default: stdio)",
    )
    parser.add_argument(
        "--host",
        default="localhost",
        help="Host to bind to for SSE transport (default: localhost)",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=8000,
        help="Port to bind to for SSE transport (default: 8000)",
    )
    parser.add_argument(
        "--version",
        action="store_true",
        help="Print version information and exit",
    )

    args = parser.parse_args()

    if args.version:
        from zotero_mcp._version import __version__
        print(f"Zotero MCP v{__version__}")
        sys.exit(0)

    if args.transport == "stdio":
        mcp.run(transport="stdio")
    elif args.transport == "sse":
        mcp.run(transport="sse", host=args.host, port=args.port)


if __name__ == "__main__":
    main()
