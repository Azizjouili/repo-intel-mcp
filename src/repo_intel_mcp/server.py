from mcp.server.mcpserver import MCPServer

from repo_intel_mcp.tools.files import read_file
from repo_intel_mcp.tools.search import search_code
from repo_intel_mcp.tools.symbols import find_definition, list_file_symbols
from repo_intel_mcp.tools.tree import get_repo_tree

mcp = MCPServer("repo-intel")

mcp.tool()(get_repo_tree)
mcp.tool()(search_code)
mcp.tool()(read_file)
mcp.tool()(find_definition)
mcp.tool()(list_file_symbols)

if __name__ == "__main__":
    mcp.run(transport="stdio")