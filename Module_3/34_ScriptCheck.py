"""
Write a Python script to check if a given key already exists in a dictionary.
"""

key = input("Enter a key : ")

dict = { 'mango': 1, 'apple': 2, 'banana': 3, 'orange': 4 }

if key in dict:
    print(f"{key} exists in the dictionary.")
else:
    print(f"{key} does not exist in the dictionary.")