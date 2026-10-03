import subprocess

from repo_intel_mcp.repo import REPO_PATH


def search_code(query: str, file_glob: str | None = None, max_results: int = 50) -> str:
    """Search the repo's tracked files for a string or regex pattern.

    Use this to find where something is defined or used — a function name,
    a config key, an error message. Returns matches as `path:line:text`.

    Args:
        query: text or regex to search for.
        file_glob: optional filter like '*.py' to limit which files are searched.
        max_results: cap on the number of matching lines returned.
    """
    cmd = ["git", "-C", str(REPO_PATH), "grep", "-n", "-I", "-e", query]
    if file_glob:
        cmd += ["--", file_glob]

    result = subprocess.run(cmd, capture_output=True, text=True, check=False)

    # git grep exits 1 when there are simply no matches — not an error for us.
    if result.returncode not in (0, 1):
        return f"Search failed: {result.stderr.strip() or 'unknown error'}"

    lines = result.stdout.splitlines()
    if not lines:
        return "No matches."

    shown = lines[:max_results]
    extra = len(lines) - len(shown)
    note = f"\n… and {extra} more matches." if extra > 0 else ""
    return "\n".join(shown) + note