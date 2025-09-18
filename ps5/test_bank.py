from bank import value


def test_hello():
    assert value("hello bank") == 0
    assert value("hello") == 0


def test_h():
    assert value("h bank") == 20
    assert value("h") == 20


def test_other():
    assert value("nice") == 100
    assert value("good") == 100


def test_empty():
    assert value("") == 100
