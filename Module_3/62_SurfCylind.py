"""
Write a Python program to calculate surface volume and area of a cylinder.
"""

r = int(input('Enter radious: '))
h = int(input('Enter height : '))

π = 3.14
surface_volume = lambda : π*r*r*h

print('surface volume is',surface_volume())

r = int(input('Enter radious: '))
h = int(input('Enter height : '))
area_of_cylinder = lambda : 2*π*r*(h+r)

print('Area of cylinder is ', area_of_cylinder())