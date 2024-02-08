"""
Write a Python program to check whether a list contains a sub list.
"""

list1 = input('Enter main list : ')

list2 = input('Enter sub list : ')

sub_list = list1.index(list2[0])

if list1[sub_list:sub_list + len(list2)] == list2:
    print("yes it's contains sub list")
else:
    print('not sub list contains')