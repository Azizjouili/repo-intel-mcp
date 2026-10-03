from mcp.server.fastmcp import FastMCP

from repo_intel_mcp.tools.files import read_file
from repo_intel_mcp.tools.search import search_code
from repo_intel_mcp.tools.tree import get_repo_tree

mcp = FastMCP("repo-intel")

mcp.tool()(get_repo_tree)
mcp.tool()(search_code)
mcp.tool()(read_file)

if __name__ == "__main__":
    mcp.run()