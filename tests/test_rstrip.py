import io
import sys
import pytest
from unittest.mock import patch
from pathlib import Path
import runpy


def _load_rstrip_module():
    repo_root = Path(__file__).resolve().parents[1]
    module_path = repo_root / "rstrip" / "rstrip.py"
    return runpy.run_path(str(module_path))


rstrip = _load_rstrip_module()


def test_trim_from_stdin(monkeypatch):
    input_text = "Hello \nWorld \n"
    monkeypatch.setattr(sys, "stdin", io.StringIO(input_text))

    with patch("sys.stdout", new=io.StringIO()) as fake_stdout:
        rstrip["trim_trailing_spaces"]()  # Call the function directly
        result = fake_stdout.getvalue()

    assert result == "HelloWorld"  # Check for expected output


def test_trim_from_file(tmp_path):
    p = tmp_path / "sample.txt"
    p.write_text("Line1 \nLine2\t\n")

    with patch("sys.stdout", new=io.StringIO()) as fake_stdout:
        rstrip["trim_trailing_spaces"](str(p))  # Call the function directly
        result = fake_stdout.getvalue()

    assert result == "Line1Line2"  # Check for expected output


def test_print_help_outputs_usage(capsys):
    rstrip["print_help"]()  # Call the function directly
    captured = capsys.readouterr()
    out = captured.out
    assert "Usage:" in out
    assert "Arguments:" in out
    assert "Options:" in out


def test_file_not_found_exits_with_code_1():
    nonexisting = "this_file_should_not_exist_12345.txt"
    with pytest.raises(SystemExit) as exc:
        rstrip["trim_trailing_spaces"](nonexisting)  # Call the function directly
    assert exc.value.code == 1
