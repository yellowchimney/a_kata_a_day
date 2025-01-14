from src.sum_sub_arrays import sum_max_sub_array

def test_returns_zero_for_empty_list():
    assert sum_max_sub_array([])== 0

def test_returns_zero_for_negative_numbers_list():  
    assert sum_max_sub_array([-2])== 0
    assert sum_max_sub_array([-2,-6,-4])== 0

def test_returns_num_for_single_positive_num_list():
    assert sum_max_sub_array([2])== 2
    assert sum_max_sub_array([5])== 5

def test_returns_sum_of_num_for_positive_list():
    assert sum_max_sub_array([2,5])== 7
    assert sum_max_sub_array([5,7,8])== 20  

def test_returns_max_sub_list_sum_for_mixed_list():
    assert sum_max_sub_array([2,5,-2,1])== 7
    assert sum_max_sub_array([5,7,-3,6,-8,4,2])== 15 