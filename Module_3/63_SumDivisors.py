"""
Write a Python program to returns sum of all divisors of a number.
"""

num = int(input('Enter the number '))

def sum_div(num):
    divisors = [1]
    for i in range(2,num):
        if (num % i) == 0:
            divisors.append(i)

    print('Sum of divisors is',sum(divisors))

sum_div(num)
