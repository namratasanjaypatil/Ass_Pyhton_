"""
How will you randomizes the items of a list in place?

==> In Python, you can randomize the items of a list in place using the random module and the list method
shuffle(). 
"""

import random

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

random.shuffle(list)
print('Randomizes item list is ',list)