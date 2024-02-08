string = "I know you are not poor."

a = string.find('not')    
b= string.find('poor')
    
if a != -1 and b!= -1 and a < b:
    print(string[:a] + 'good' + string[b+4:])
else:
    print(string)