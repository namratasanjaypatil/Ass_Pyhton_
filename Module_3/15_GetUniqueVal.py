"""
Write a Python program to get unique values from a list
"""

list1 = [1, 3, 2, 4, 2, 3, 1, 0, 5, 6, 5, 6, 7, 9, 8, 7, 9, 8, 4, 0, 10, 11, 10]

a = set(list1)
b = a

uniq = list(b)

print(uniq)