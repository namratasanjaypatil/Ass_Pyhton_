str = input('Enter the characters : ')

if len(str) > 2:
    str1 = str[:2] + str[-2:]
    print(str)
else:
    print('Empty string')