import pytest
from um import count

def test_basic():
    assert count("Um, thanks, um...") == 2
    assert count("um um UM") == 3
    assert count("No ums here") == 0

def test_with_punctuation():
    assert count("Um? Yes, um!") == 2
    assert count("yummy um, umbrella um") == 2 

def test_empty_and_whitespace():
    assert count("") == 0
    assert count("   ") == 0