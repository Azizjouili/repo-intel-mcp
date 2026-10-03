import ast
import re

from repo_intel_mcp.repo import REPO_PATH, safe_path


def _python_symbols(source: str) -> list[tuple[int, str]]:
    """Return (line, label) for every top-level func/class in Python source."""
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return []
    found: list[tuple[int, str]] = []
    for node in tree.body:  # top-level only — keeps the list readable
        if isinstance(node, ast.FunctionDef | ast.AsyncFunctionDef):
            found.append((node.lineno, f"def {node.name}"))
        elif isinstance(node, ast.ClassDef):
            found.append((node.lineno, f"class {node.name}"))
    return found


def list_file_symbols(path: str) -> str:
    """List the functions and classes defined in one file, with line numbers.

    A fast way to see what a module contains without reading all of it.

    Args:
        path: file path relative to the repo root.
    """
    target = safe_path(path)
    if not target.is_file():
        return f"Not a file: {path}"

    source = target.read_text(encoding="utf-8", errors="replace")
    symbols = _python_symbols(source) if path.endswith(".py") else []

    if not symbols:
        return f"No top-level functions or classes found in {path}."
    return "\n".join(f"{line:>5} | {label}" for line, label in symbols)


def find_definition(symbol: str) -> str:
    """Find where a function or class named `symbol` is defined.

    Searches all Python files in the repo and returns each match as
    `path:line: <signature>`. Use this to jump straight to a definition.

    Args:
        symbol: the function or class name to look for (exact match).
    """
    hits: list[str] = []
    pattern = re.compile(rf"^\s*(?:async\s+)?(?:def|class)\s+{re.escape(symbol)}\b")

    for py_file in REPO_PATH.rglob("*.py"):
        if ".venv" in py_file.parts or "__pycache__" in py_file.parts:
            continue
        try:
            text = py_file.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for lineno, line in enumerate(text.splitlines(), start=1):
            if pattern.match(line):
                rel = py_file.relative_to(REPO_PATH)
                hits.append(f"{rel}:{lineno}: {line.strip()}")

    return "\n".join(hits) if hits else f"No definition found for {symbol!r}."