"""
Write a Python function that checks whether a passed string is palindrome or not.
"""

string = input('Enter a string : ')

def palindrome(string):
    if string == string[len(string)::-1]:
        print(string,'is a palindrome string')
    else:
        print(string,'is not a palindrome string')
    
palindrome(string)