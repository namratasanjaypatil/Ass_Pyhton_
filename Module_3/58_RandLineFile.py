"""
Write a Python program to read a random line from a file. 
"""

import random

with open('PattMatch.txt', 'r') as f:
    lines = f.readlines()
    random_line = random.choice(lines)
    print(random_line)
