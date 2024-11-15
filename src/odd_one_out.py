'''The function takes a list of integers, entirely comprised either of odd or even numbers,
   ecxept for one integer, which will be a misfit. The function sorts through the list
   and returns the misfit integer'''

def find_outlier(integers):
    counter_odd = {}
    counter_even ={}
    for i in integers:
        if i % 2 == 1:
            counter_odd[i] = 1
        else:
            counter_even[i] = 1
    if len(counter_odd.items()) == 1:
        number = list(counter_odd.keys())
        return number[0]
    else:
        number = list(counter_even.keys())
        return number[0]