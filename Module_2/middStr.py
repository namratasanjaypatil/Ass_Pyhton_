first_last =input('Enter a string you want to change :')  

middle =input("Enter a word with you want to add in middle :")

a = first_last.split()
b = len(a) // 2
 
x = a[:b] + [middle] + a[b:] 

x = ' '.join(x)
 
print(str(x))