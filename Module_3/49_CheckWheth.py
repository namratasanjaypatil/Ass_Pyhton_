"""
Write a Python function to check whether a number is in a given range
"""

start = int(input('Enter start point of the range : '))
stop = int(input('Enter end point of the range : '))
number = int(input('Enter the number to be checked : '))

def find_num(rng,num):
    if num in rgn:
        print(num,'in range')
    else:
        print(num,'not in range')

if start > stop :
    rgn = range(start, stop + 1, -1)
else:
    rgn = range(start, stop + 1)
    
find_num(rgn,num = number)