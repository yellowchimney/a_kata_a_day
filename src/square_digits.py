'''Square every digit of a number and concatenate them.
For example, if we run 9119 through the function, 811181 will come out.
The function accepts an integer and returns an integer.'''

def square_digits(num):
    string_num = str(num)
    list_of_squares = [int(i)**2 for i in string_num]
    list_of_square_str = [str(i) for i in list_of_squares]
    result_str = "".join(list_of_square_str)
    return int(result_str)