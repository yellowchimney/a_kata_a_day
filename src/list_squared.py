"""
Function takes two numbers,m and n, checks which numbers in the range 
return perfect squares for the sum of their divisors. The function returns 
an array of arrays, where each subarray contains the number and the sum of 
the squares of its divisors.
"""

def list_squared(m, n):
    def get_divisors_sum_squared(num):
        divisors = set()
        for i in range(1, int(num**0.5) + 1):
            if num % i == 0:
                divisors.add(i)
                divisors.add(num // i)
        return sum(d * d for d in divisors)
    
    result = []
    for num in range(m, n + 1):
        sum_squared = get_divisors_sum_squared(num)
        root = int(sum_squared**0.5)
        if root * root == sum_squared:
            result.append([num, sum_squared])
    
    return result