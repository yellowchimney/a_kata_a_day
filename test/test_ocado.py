import pytest
from src.ocado import solution

def test_single_week():
    assert solution(["Mon", "Tue", "Wed"]) == 1
    assert solution(["Mon", "Wed", "Fri"]) == 1
    assert solution(["Wed", "Thu", "Fri"]) == 1

def test_multiple_weeks():
    assert solution(["Mon", "Tue", "Wed", "Mon", "Tue"]) == 2
    assert solution(["Wed", "Thu", "Mon", "Tue"]) == 2
    assert solution(["Fri", "Sat", "Sun", "Mon", "Tue"]) == 2

def test_empty_list():
    assert solution([]) == 0

def test_single_day():
    assert solution(["Mon"]) == 1
    assert solution(["Wed"]) == 1
    assert solution(["Sun"]) == 1

def test_same_day_multiple_weeks():
    assert solution(["Mon", "Mon", "Mon"]) == 3

def test_descending_order():
    assert solution(["Sun", "Sat", "Fri"]) == 3
    assert solution(["Wed", "Tue", "Mon"]) == 3

def test_mixed_weeks():
    assert solution(["Mon", "Wed", "Fri", "Tue", "Thu", "Mon"]) == 2
    assert solution(["Wed", "Thu", "Mon", "Tue", "Wed", "Thu"]) == 2

def test_full_weeks():
    assert solution(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]) == 1
    assert solution(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun", "Mon"]) == 2

def test_alternating_days():
    assert solution(["Mon", "Wed", "Mon", "Wed", "Mon"]) == 3

def test_edge_cases():
    # Single day repeated
    assert solution(["Mon"] * 5) == 5
    
    # All days in reverse
    assert solution(["Sun", "Sat", "Fri", "Thu", "Wed", "Tue", "Mon"]) == 7
    
    # Complex pattern
    assert solution(["Mon", "Wed", "Fri", "Mon", "Wed", "Fri", "Sun"]) == 3

