from src.sum_consecutive_duplicates import sum_consecutive_duplicates, reduce_consecutiveness

def test_returns_empty_list_when_passed_empty_list():
    assert sum_consecutive_duplicates([]) == []

def test_returns_new_list():
    input = []
    result = sum_consecutive_duplicates(input)
    assert result is not input

def test_input_remains_unchanged():
    input = []
    sum_consecutive_duplicates(input)
    assert input == []

def test_returns_unchanged_list_if_no_consecutive_duplicates_are_passed():
    assert sum_consecutive_duplicates([1,2,3,5]) == [1,2,3,5]

def test_returns_consecutive_duplicates_summed_up():
    assert sum_consecutive_duplicates([1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1]) == [2, 2, 4, 2, 3]

def test_recursive_fnx_returns_consecutive_duplicates_summed_up():
    assert reduce_consecutiveness([1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1]) == [8, 2, 3]