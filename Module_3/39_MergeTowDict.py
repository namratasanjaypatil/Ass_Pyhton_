"""
Write a Python script to merge two Python dictionaries.
"""

dict1 = {'a': 100, 'b': 200}
dict2 = {'c': 300, 'd': 400}

d = dict1.copy()
d.update(dict2)

print(d)