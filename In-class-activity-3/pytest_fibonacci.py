import pytest
from fibonacci import fibonacci, factorial

def test_fibTwo():
    assert fibonacci(2) == 1

def test_fibTen():
    assert fibonacci(10) == 55

def test_factThree():
    assert factorial(3) == 6

def test_factSeven():
    assert factorial(7) == 5040
