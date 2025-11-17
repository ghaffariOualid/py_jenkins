import pytest
import tempfile
import os
from src.io_utils import load_numbers, sum_numbers

def test_load_numbers():
    # Create a temporary file with numbers
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
        f.write("1\n2\n3\n4\n5\n")
        temp_path = f.name

    try:
        result = load_numbers(temp_path)
        assert result == [1, 2, 3, 4, 5]
    finally:
        os.unlink(temp_path)

def test_load_numbers_empty_file():
    # Create an empty temporary file
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
        temp_path = f.name

    try:
        result = load_numbers(temp_path)
        assert result == []
    finally:
        os.unlink(temp_path)

def test_sum_numbers():
    assert sum_numbers([1, 2, 3, 4, 5]) == 15
    assert sum_numbers([]) == 0
    assert sum_numbers([-1, 1]) == 0