from app import add, subtract, multiply, divide

def test_add():
    assert add(1,2) == 3
    assert add(3,4) == 7

def test_subtract():
    assert subtract(1,2) == -1
    assert subtract(3,4) == -1

def test_multiply():
    assert multiply(1,2) == 2
    assert multiply(3,4) == 12


test_add()