import pytest
from fuel import convert, gauge


def test_fraction():
    assert convert("1/4") == 25
    assert convert("1/2") == 50
    assert convert("0/1") == 0
    assert convert("1/1") == 100

def test_x_y_error():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ValueError):
        convert("2/1")

def test_input_error():
    with pytest.raises(ValueError):
        convert("cat")
        
def test_negative_frac():
    with pytest.raises(ValueError):
        convert("-1/2")

def test_percentage():
    assert gauge(25) == "25%"
    assert gauge(50) == "50%"
    assert gauge(100) == "F"
    assert gauge(0) == "E"
    assert gauge(99) == "F"
    assert gauge(1) == "E"
