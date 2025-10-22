from working import convert
import pytest

def test_basic_times():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"

def test_with_minutes():
    assert convert("9:30 AM to 5:15 PM") == "09:30 to 17:15"
    assert convert("11:59 PM to 12:01 AM") == "23:59 to 00:01"

def test_invalid_format():
    with pytest.raises(ValueError):
        convert("9AM - 5PM")
    with pytest.raises(ValueError):
        convert("13 AM to 5 PM")
    with pytest.raises(ValueError):
        convert("10:60 AM to 5 PM")
    with pytest.raises(ValueError):
        convert("10 AM 5 PM")