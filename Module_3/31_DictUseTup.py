"""
How will you create a dictionary using tuples in python ?

To create a dictionary using tuples in Python, you can use the built-in dict() function. 
The dict() function can take a list of tuples as an argument, where each tuple contains a 
key-value pair that will be added to the dictionary.
"""

tuple = ((1,'python'),(2,'hello'),(3,'world'),(4,'devloper'))

tuple = list(tuple)
n = {}
n.update(tuple)
tuple = n.copy()
print(tuple)
