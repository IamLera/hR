import pytest
from src import module1

def test_add():
    assert module1.add(2, 3) == 5

def test_multiply():
    assert module1.multiply(2, 3) == 6