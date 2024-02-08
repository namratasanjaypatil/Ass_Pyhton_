"""
Write a Python program to convert a tuple to a string. 
"""

tuple1 =[1, 1.5, 2, 2.5, 'python', [2,5,3,7],{92,46,14}, {'hello':23, 'hello':'py'}]

str1 = tuple(tuple1)

string = str(str1)

print(string)
print(type(string))
