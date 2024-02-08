"""
Write a Python function that takes a list and returns a new list with unique elements of the first list
"""

list = [1, 2, 3, 4, 5, 5, 6, 4, 7, 3, 1, 2, 5, 4, 6, 3, 2, 1, 4, 5, 2]

def uniq_list(list):
    list1 = []
    for i in list:
        if i not in list1:
            list1.append(i)
    return list1

print(uniq_list(list))