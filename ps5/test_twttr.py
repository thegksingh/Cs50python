from twttr import shorten


def test_lowercase():
    assert shorten("twitter") == "twttr"
    assert shorten("hello") == "hll"


def test_uppercase():
    assert shorten("EDUCATION") == "DCTN"
    assert shorten("CS50") == "CS50"


def test_mixedcase():
    assert shorten("PyThOn") == "PyThn"
    assert shorten("AI") == ""


def test_numbers_symbols():
    assert shorten("1234") == "1234"
    assert shorten("h@ack") == "h@ck"


def test_empty():
    assert shorten("") == ""
