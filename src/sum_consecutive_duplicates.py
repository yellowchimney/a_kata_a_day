"""
Function takes a list of numbers and returns a list of numbers 
where each number is the sum of all consecutive duplicates.
"""
def sum_consecutive_duplicates(lst):
    if not lst:
        return []
    loop_counter = 0
    new_item = lst[0]
    result_list = []
    for item in lst:
        if item == new_item:
            loop_counter +=1
        else:
            result_list.append(new_item * loop_counter)
            new_item = item
            loop_counter = 1

    result_list.append(new_item * loop_counter)

    return result_list

"""
Recursively sums up all consecutive duplicates in the list 
until no consecutive duplicates are left.
"""
def reduce_consecutiveness(lst):
    reduced_list = sum_consecutive_duplicates(lst)
    if reduced_list == lst:
        return lst
    else:
        return reduce_consecutiveness(sum_consecutive_duplicates(reduced_list))