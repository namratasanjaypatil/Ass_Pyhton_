"""
Write a Python script to sort (ascending and descending) a dictionary by
value.
"""

dict1 = {4:'nammu', 2:'nik', 1:'sanju', 3:'piu', 5:'kishu'} 
                                         
list1 = list(dict1.items())  
list1.sort()            
print('Ascending order is',list1) 

list1 = list(dict1.items())
list1.sort(reverse=True)
print('Descending order is',list1)

dict = dict(list1)
print("Dictionary",dict) 