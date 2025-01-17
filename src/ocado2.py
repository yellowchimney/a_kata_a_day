"""
Function takes two arrays of integers, A and B, and two integers, X and Y.
A and B that represent assembly lines and each element on the array 
represents the time it takes to attach a detail to the car. 
X is the time it takes to switch from line A to line B and Y is the time it takes
to switch from line B to line A.
Function returns the minimum time it takes to attach all details to the car.

This was a task 2 from Ocado coding challenge interview.
"""

def solution(A, B, X, Y):
    timeA = A[0]
    timeB = B[0]
    
    for i in range(1,len(A)):
        new_time_A = min(timeA +A[i],
                        timeB + Y + A[i])
        new_time_B = min(timeB + B[i],
                         timeA + X + B[i])
        timeA = new_time_A
        timeB = new_time_B
    return min(timeA, timeB)

print(solution([1,2,3,4,5,6,2,8,9,10], [1,2,4,5,6,7,8,3,10,2], 1, 3))