"""
Write a Python program to calculate the area of a trapezoid.
"""

a = int(input('Enter upper base a : '))
b = int(input('Enter lower base b : '))
h = int(input('Enter height h : '))

area = lambda:(a+b)/2*h

print('area of trapezoid is ', area())
