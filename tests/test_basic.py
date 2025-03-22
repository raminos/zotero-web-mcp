"""Basic tests for zotero-mcp package structure."""

import pytest


def test_version():
    """Test that the version is correctly imported."""
    from zotero_mcp import __version__
    assert isinstance(__version__, str)
    assert len(__version__.split(".")) >= 3


def test_server_setup():
    """Test that the MCP server is set up correctly."""
    from zotero_mcp import mcp
    assert mcp is not None
    assert mcp.name == "Zotero"
