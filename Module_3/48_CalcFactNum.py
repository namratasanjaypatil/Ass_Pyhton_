"""
Write a Python function to calculate the factorial of a number (a nonnegative integer)
"""

def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    else:
        return n

val = factorial(5)

print('Factorial is : ', val)