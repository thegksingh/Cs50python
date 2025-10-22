from seasons import main
from datetime import date
import pytest
import inflect

p = inflect.engine()

def test_valid(monkeypatch, capsys):
    today = date.today()
    birth = date(today.year - 1, today.month, today.day)
    monkeypatch.setattr("builtins.input", lambda _: birth.isoformat())
    main()
    out = capsys.readouterr().out.strip()
    expected_minutes = 365 * 24 * 60
    expected_words = p.number_to_words(expected_minutes, andword="").capitalize()
    assert out == f"{expected_words} minutes"

def test_invalid(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "invalid-date")
    with pytest.raises(SystemExit):
        main()