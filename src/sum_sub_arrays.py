def sum_max_sub_array(list_of_nums):
    if not list_of_nums:
        return 0
    if all(num < 0 for num in list_of_nums):
        return 0
    
    max_sum = current_sum = list_of_nums[0]
    for num in list_of_nums[1:]:
        current_sum = max(num, current_sum+num)
        max_sum = max(current_sum, max_sum)
    return max_sum

