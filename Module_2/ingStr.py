str1 = input('Please enter the value : ')

if len(str1)>3:
    if str1.endswith('ing'):
        print(str1+'ly')
    else:
        print(str1+'ing')
else:
    print('string length is less than 3 ')