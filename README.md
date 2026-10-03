# repo-intel-mcp

An MCP server that lets an LLM answer questions about a codebase by calling
tools — search, read files, find definitions — instead of guessing.

## Why
Gives any MCP-compatible agent (Claude Desktop, a LangGraph agent) grounded,
citeable answers about a real repository.

## Tools
- `get_repo_tree` — directory structure
- `search_code` — regex/string search across tracked files
- `read_file` — read a file or line range
- `find_definition` — locate where a symbol is defined
- `list_file_symbols` — functions/classes in a file

## Status
In active development — part of a production-oriented AI-engineering portfolio.

## Setup
    uv sync

## Demo
_(GIF coming — agent answering "how does routing work?" against a real repo)_