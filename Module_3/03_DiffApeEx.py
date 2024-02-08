"""
Differentiate between append () and extend () methods ?

append() :

    The append() method adds a single element to the end of a list. 
    The element can be of any type, and it will be added as a new item in the list.

extend() :

    The extend() method add multiple elements to the end of a list. 
    It takes an iterable (such as a list, tuple, or string) as its argument, and adds each element in the
    iterable as a new item in the list.
"""

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [9, 8, 7, 6, 5, 4, 3, 2, 1]

list1.append('Nammu')
print(list1)

list2.extend('Namu')
print(list2)