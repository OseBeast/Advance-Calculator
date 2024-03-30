'''My Calculator Test'''
import pytest
from app import App


def test_app_start_add_command(capfd, monkeypatch):
    """Test how the REPL handles add command before exiting."""
    inputs = iter(['add', '1', '2', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()

    with pytest.raises(SystemExit) as e:
        app.start()
    assert e.type == SystemExit

    out, _ = capfd.readouterr()

    #assert "Type 'exit' to exit." in out
    assert "3" in out

def test_app_start_subtract_command(capfd, monkeypatch):
    """Test how the REPL handles Subract command before exiting."""
    inputs = iter(['subtract', '2', '1', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()

    with pytest.raises(SystemExit) as e:
        app.start()
    assert e.type == SystemExit

    out, _ = capfd.readouterr()

    #assert "Type 'exit' to exit." in out
    assert "1" in out

def test_app_start_multiply_command(capfd, monkeypatch):
    """Test how the REPL handles Mulitply command before exiting."""
    inputs = iter(['multiply', '3', '3', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()

    with pytest.raises(SystemExit) as e:
        app.start()
    assert e.type == SystemExit

    out, _ = capfd.readouterr()

    #assert "Type 'exit' to exit." in out
    assert "9" in out

def test_app_start_divide_command(capfd, monkeypatch):
    """Test how the REPL handles Divide command before exiting."""
    inputs = iter(['divide', '9', '3', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()

    with pytest.raises(SystemExit) as e:
        app.start()
    assert e.type == SystemExit

    out, _ = capfd.readouterr()

    #assert "Type 'exit' to exit." in out
    assert "3" in out

    #assert "Type 'exit' to exit." in out


def test_app_start_unknown_command(capfd, monkeypatch):
    """Test how the REPL handles an unknown command before exiting."""
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()

    with pytest.raises(SystemExit):
        app.start()

    captured = capfd.readouterr()
    assert "No such command: unknown_command" in captured.out
