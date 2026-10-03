from pathlib import Path

from repo_intel_mcp.repo import safe_path

# Folders that are noise for understanding a codebase.
IGNORE = {".git", ".venv", "__pycache__", "node_modules",
          ".mypy_cache", ".pytest_cache", ".ruff_cache"}


def get_repo_tree(subpath: str = ".", max_depth: int = 2) -> str:
    """List the directory structure of the repo as an indented tree.

    Call this first to understand how the codebase is organized before
    searching or reading files.

    Args:
        subpath: folder to start from, relative to the repo root.
        max_depth: how many levels deep to show.
    """
    root = safe_path(subpath)
    if not root.is_dir():
        return f"Not a directory: {subpath}"

    lines: list[str] = []

    def walk(directory: Path, depth: int) -> None:
        if depth > max_depth:
            return
        # Directories first, then files, each alphabetically.
        entries = sorted(directory.iterdir(),
                         key=lambda p: (p.is_file(), p.name.lower()))
        for entry in entries:
            if entry.name in IGNORE:
                continue
            indent = "  " * (depth - 1)
            suffix = "/" if entry.is_dir() else ""
            lines.append(f"{indent}{entry.name}{suffix}")
            if entry.is_dir():
                walk(entry, depth + 1)

    walk(root, 1)
    return "\n".join(lines) if lines else "(empty)"