import pytest

from repo_intel_mcp.repo import safe_path
from repo_intel_mcp.tools.files import read_file
from repo_intel_mcp.tools.search import search_code
from repo_intel_mcp.tools.symbols import find_definition, list_file_symbols
from repo_intel_mcp.tools.tree import get_repo_tree

SAMPLE = "tests/fixtures/sample.py"


def test_repo_tree_lists_source():
    assert "src" in get_repo_tree(".", 2)


def test_search_finds_known_symbol():
    # 'safe_path' is defined in repo.py, which is committed/tracked.
    assert "repo.py" in search_code("safe_path", "*.py")


def test_read_file_has_line_numbers():
    out = read_file(SAMPLE)
    assert "class Greeter" in out
    assert "1 |" in out  # the line-number gutter is present


def test_list_symbols_top_level_only():
    out = list_file_symbols(SAMPLE)
    assert "class Greeter" in out
    assert "def add" in out
    assert "hello" not in out  # nested method — correctly not listed


def test_find_definition_locates_class():
    out = find_definition("Greeter")
    assert "sample.py" in out


def test_safe_path_blocks_escape():
    with pytest.raises(ValueError):
        safe_path("../../etc/passwd")