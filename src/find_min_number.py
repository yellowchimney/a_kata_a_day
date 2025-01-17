"""
Function takes an array of integers and returns the smallest positive integer
that is not in the array.
"""

def solution(A):
    for x in range(1,1000001):
        if x not in A:
            return x
