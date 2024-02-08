"""
How can you pick a random item from a list or tuple?

==> In Python, you can randomly sample elements from a list with choice() , sample() , and choices() of the random module. These functions can also be applied to a string and tuple. choice() returns one random element, and sample() and choices() return a list of multiple random elements.
"""
import random 

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

random_item = random.choice(list)
print(f'your random number is {random_item}')