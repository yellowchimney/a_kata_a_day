"""
Given a string, write a function to check if it is a valid IPv4 address.
A valid IPv4 address is a string that consists of four decimal numbers, 
each ranging from 0 to 255, separated by dots. Leading zeros (e.g. 00.01.02.03) 
are considered invalidInputs are guaranteed to be a single string.

The function should return True if the string is a valid IPv4 address, and False otherwise.
"""

def is_valid_IP(strng):
    nums = strng.split(".")
    if len(nums) != 4:
        return False
    if not all(num.isdigit() for num in nums) or any(num.startswith("0") and num !="0" for num in nums):
        return False
    else:
        nums_checked = [int(num) for num in nums]
        if all(0 <= num <= 255 for num in nums_checked):
            return True
        else: return False

 