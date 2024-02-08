"""
Write a Python function to check whether a number is perfect or not.
"""

def perfect_number(n):
    sum = 0
    for c in range(1, n):
        if n % c == 0:
            sum += c
    return sum == n
print(perfect_number(6))