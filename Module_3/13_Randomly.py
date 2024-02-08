"""
Write a Python program to select an item randomly from a list.
"""

import random

items = [ (1, 2, 3, 4, 5), 3, 5, 2, 5, 4, 1, 8, 9, 'apple', 'banana', 'orange', 'pear', 'grape']

random = random.choice(items)

print("Selected item:", random)