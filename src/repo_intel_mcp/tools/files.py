from repo_intel_mcp.repo import safe_path

MAX_LINES = 400


def read_file(path: str, start: int = 1, end: int | None = None) -> str:
    """Read a file, or a range of lines, with line numbers prepended.

    Use this after `search_code` to read the code around a match. For large
    files, pass `start` and `end` to read one section at a time.

    Args:
        path: file path relative to the repo root.
        start: first line to read (1-based).
        end: last line to read; defaults to start + 400.
    """
    target = safe_path(path)
    if not target.is_file():
        return f"Not a file: {path}"

    try:
        lines = target.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError as exc:
        return f"Could not read {path}: {exc}"

    start = max(start, 1)
    end = min(end if end is not None else start + MAX_LINES - 1, len(lines))

    if start > len(lines):
        return f"{path} has only {len(lines)} lines; start={start} is past the end."

    selected = lines[start - 1:end]
    width = len(str(end))  # align the line-number gutter
    numbered = [f"{i:>{width}} | {text}" for i, text in enumerate(selected, start=start)]

    header = f"{path}  (lines {start}–{end} of {len(lines)})"
    return header + "\n" + "\n".join(numbered)