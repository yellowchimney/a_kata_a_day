"""
Function takes an array of strings, each representing a day of the week.
The days of one week can only go in order, so if a day is not in order,
it means that a new week has started. Function returns the minimum number of weeks
that are represented in array.

This was a task 1 from Ocado coding challenge interview.
"""
def solution(visits):
    week_dict  = {
        "Mon" : 1,
        "Tue" : 2,
        "Wed" : 3,
        "Thu" : 4,
        "Fri" : 5,
        "Sat" : 6,
        "Sun" : 7}
    list_of_weeks = []
    current_week = []
    for day in visits:
        day_order = week_dict[day]
        if len(current_week) == 0 or day_order > max(current_week):
            current_week.append(day_order)
        else:
            list_of_weeks.append(current_week)
            current_week = []
            current_week.append(day_order)
    if len(current_week) > 0:
        list_of_weeks.append(current_week)

    return len(list_of_weeks)