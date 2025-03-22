.PHONY: clean test install format

# Install the package in development mode
install:
	pip install -e ".[dev]"

# Run tests
test:
	pytest

# Run tests with coverage
test-coverage:
	pytest --cov=zotero_mcp

# Format code
format:
	black src tests
	isort src tests

# Clean up temporary files and build artifacts
clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf __pycache__/
	rm -rf .pytest_cache/
	rm -rf .coverage
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete

# Build the package
build:
	python -m build

# Run the server with stdio transport
run:
	python -m zotero_mcp.cli --transport stdio

# Run the server with SSE transport
run-sse:
	python -m zotero_mcp.cli --transport sse
