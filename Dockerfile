# Generated by https://smithery.ai. See: https://smithery.ai/docs/config#dockerfile
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy the project files
COPY . /app

# Install build dependencies and install the package
RUN pip install --no-cache-dir build hatchling \
    && pip install --no-cache-dir .

# Start the MCP server
ENTRYPOINT ["zotero-web-mcp", "serve", "--transport", "stdio"]
