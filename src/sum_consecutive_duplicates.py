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


def reduce_consecutiveness(lst):
    reduced_list = sum_consecutive_duplicates(lst)
    if reduced_list == lst:
        return lst
    else:
        return reduce_consecutiveness(sum_consecutive_duplicates(reduced_list))