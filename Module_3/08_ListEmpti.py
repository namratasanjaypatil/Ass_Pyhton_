"""
Write a Python program to check a list is empty or not. 
"""

list1 = list(input("Enter your list : "))

if len(list1) == 0:
    print('list is empty')
else:
    print('list is not empty')
    print(len(list1),'elements available')