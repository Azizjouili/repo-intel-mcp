import os
from pathlib import Path

# The repo we answer questions about. Defaults to the current folder;
# override by setting the REPO_PATH environment variable.
REPO_PATH = Path(os.environ.get("REPO_PATH", ".")).resolve()


def safe_path(relative: str) -> Path:
    """Resolve a user-supplied path and ensure it stays inside REPO_PATH."""
    target = (REPO_PATH / relative).resolve()
    if target != REPO_PATH and not target.is_relative_to(REPO_PATH):
        raise ValueError(f"Path escapes the repo root: {relative!r}")
    return target