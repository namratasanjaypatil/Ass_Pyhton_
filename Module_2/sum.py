a = int(input('Please enter the number : '))
b = int(input('Please enter the number : '))
c = int(input('Please enter the number : '))

sum=a+b+c
if a==b or b==c or c==a:
    print('Addition is',(sum*0))
else:
    print('Addition is',sum)