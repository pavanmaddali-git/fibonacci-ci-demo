"""Unit tests for fibonacci.py — these run automatically inside GitHub Actions."""

import sys
import os

# add the parent folder to the path so we can import fibonacci.py from the repo root
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from fibonacci import fibonacci_series  # import the function we want to test


def test_default_zero():
    # default input is 0, so the series should be empty
    assert fibonacci_series(0) == []


def test_one_term():
    # 1 term should return only [0]
    assert fibonacci_series(1) == [0]


def test_two_terms():
    # 2 terms should return [0, 1]
    assert fibonacci_series(2) == [0, 1]


def test_seven_terms():
    # 7 terms should be 0,1,1,2,3,5,8
    assert fibonacci_series(7) == [0, 1, 1, 2, 3, 5, 8]


def test_negative_number():
    # negative input should behave like 0 and return empty
    assert fibonacci_series(-5) == []
