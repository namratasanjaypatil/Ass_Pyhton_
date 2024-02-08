num = int(input("Enter the number : "))

a=0
b=1
c=0

for i in range(1, num + 1, 1):
    print(a, end = ',')
    c = a + b
    a = b
    b = c