"""
Write a Python program to print all unique values in a dictionary.
"""

dict = {"a": 1, "b": 2, "c": 1, "d": 2, "e": 3, "nammu": 5, "kish": 6}

unique_value = set(dict.values())

print("Unique dictionary are : ")

for value in unique_value:
    print(value)