"""
Write a Python program to count the number of strings where the string length is 2 or more and the 
first and last character are same from a given list of strings.
 """

list1 = input('Enter list : ')

list1 = list1.split(' ')

print('Original list :- ',list1)
count = 0
for element in list1: 
    if len(element)>=2 and element[0]==element[-1]:
        count = count + 1
print('number of string that satisfies the above condition is/are :- ', count)

# def match_words(words):  
#     ctr = 0  
  
#     for word in words:  
#         if len(word) > 1 and word[0] == word[-1]:  
#             ctr += 1  
#         return ctr  
# print(match_words(['abc', 'xyz', 'aba', '1221'])) 
