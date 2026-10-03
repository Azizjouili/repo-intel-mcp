from mcp.server.fastmcp import FastMCP

from repo_intel_mcp.tools.tree import get_repo_tree

mcp = FastMCP("repo-intel")

# Register tools (we'll add the other four here as we build them).
mcp.tool()(get_repo_tree)

if __name__ == "__main__":
    mcp.run()