import pytest
from src.function import add, subtract, multiply, divide
from src.doublons import delete_doublons
def test_add(a,b,expected):
    assert add(a, b) == expected

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(1, 1) == 0
    assert subtract(0, 5) == -5

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1
    assert multiply(0, 5) == 0

def test_divide():
    assert divide(6, 3) == 2
    assert divide(5, 2) == 2.5
    assert divide(-6, 3) == -2

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(5, 0)

def test_delete_doublons():
    assert delete_doublons([1, 1, 2, 2, 3, 1] )==[1, 2, 3]
    