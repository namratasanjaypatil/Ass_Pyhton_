"""
Write a Python program to find the highest 3 values in a dictionary.
"""

val_dict = {'a': 38, 'b': 98, 'c': 67, 'd': 82, 'e': 53, 'f': 102}

val_dict = list(val_dict.values())
val_dict.sort()
print(val_dict)

print('Highest 3 value is : ', val_dict[-3], val_dict[-2], val_dict[-1])