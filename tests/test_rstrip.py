# tests/test_rstrip.py
import io
import sys
import os
import runpy
import pytest
from pathlib import Path
from types import SimpleNamespace


def _load_rstrip_module():
    repo_root = Path(__file__).resolve().parents[1]
    module_path = repo_root / "rstrip"
    mod_dict = runpy.run_path(str(module_path))
    return SimpleNamespace(**mod_dict)


rstrip = _load_rstrip_module()


def test_trim_from_stdin(monkeypatch):
    input_text = "Hello \nWorld \n"
    monkeypatch.setattr(sys, "stdin", io.StringIO(input_text))
    result = rstrip.trim_trailing_spaces()
    assert result == "HelloWorld"


def test_trim_from_file(tmp_path):
    p = tmp_path / "sample.txt"
    p.write_text("Line1 \nLine2\t\n")
    result = rstrip.trim_trailing_spaces(str(p))
    assert result == "Line1Line2"


def test_print_help_outputs_usage(capsys):
    rstrip.print_help()
    captured = capsys.readouterr()
    out = captured.out
    assert "Usage:" in out
    assert "Options:" in out
    assert "rstrip" in out


def test_file_not_found_exits_with_code_1():
    nonexisting = "this_file_should_not_exist_12345.txt"
    if os.path.exists(nonexisting):
        os.remove(nonexisting)
    with pytest.raises(SystemExit) as exc:
        rstrip.trim_trailing_spaces(nonexisting)
    assert exc.value.code == 1
