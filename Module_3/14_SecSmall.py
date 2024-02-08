"""
Write a Python program to find the second smallest number in a list. 
"""

list = [1, 4, 3, 13, 9, 24, 20, 46, 21, 33]

list.sort()

a = list[1]
b = list[-2]

print('This is second small: ', a)
print('This is second largest: ', b)