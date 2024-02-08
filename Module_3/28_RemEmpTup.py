"""
Write a Python program to remove an empty tuple(s) from a list of tuples.
"""

tuple = (1, 2, 3, (), 4, 4.5, (1, 2, 3), (), {4, 5, 6, 9, 8}, (), {21:12, 'py':23})

val = [v for v in tuple if v]
print(val)