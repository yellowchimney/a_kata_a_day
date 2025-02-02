"""
Function takes an array and a value, and removes the value from the array in place
"""

def removeElement(nums, val):
    if val not in nums:
        return len(nums)  
    else:
        nums.remove(val)
        removeElement(nums, val)