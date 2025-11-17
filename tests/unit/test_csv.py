import pytest
import tempfile
import os
from src.csv import load_users, filter_adults

def test_load_users():
    # Create a temporary CSV file
    csv_content = "name,age\nAlice,25\nBob,17\nCharlie,30\n"
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv', newline='') as f:
        f.write(csv_content)
        temp_path = f.name

    try:
        result = load_users(temp_path)
        expected = [
            {"name": "Alice", "age": 25},
            {"name": "Bob", "age": 17},
            {"name": "Charlie", "age": 30}
        ]
        assert result == expected
    finally:
        os.unlink(temp_path)

def test_load_users_empty_file():
    # Create an empty CSV file with headers
    csv_content = "name,age\n"
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv', newline='') as f:
        f.write(csv_content)
        temp_path = f.name

    try:
        result = load_users(temp_path)
        assert result == []
    finally:
        os.unlink(temp_path)

def test_filter_adults():
    users = [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 17},
        {"name": "Charlie", "age": 30},
        {"name": "David", "age": 16}
    ]
    result = filter_adults(users)
    expected = [
        {"name": "Alice", "age": 25},
        {"name": "Charlie", "age": 30}
    ]
    assert result == expected

def test_filter_adults_all_adults():
    users = [
        {"name": "Alice", "age": 25},
        {"name": "Charlie", "age": 30}
    ]
    result = filter_adults(users)
    assert result == users

def test_filter_adults_no_adults():
    users = [
        {"name": "Bob", "age": 17},
        {"name": "David", "age": 16}
    ]
    result = filter_adults(users)
    assert result == []