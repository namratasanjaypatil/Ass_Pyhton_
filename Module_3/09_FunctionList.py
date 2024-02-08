"""
Write a Python function that takes two lists and returns true if they have at least one common member. 
"""

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 3, 10, 11]

def common_member(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False

result = common_member(list1, list2)

print(result)