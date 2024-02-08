"""
Write a Python program to map two lists into a dictionary.
"""

list1 = ['Hello','Python','World']
list2 = [1, 2, 3]
dict1 = {}

for i in range(len(list2)):
    dict1.setdefault(list2[i],list1[i])

print(dict1)