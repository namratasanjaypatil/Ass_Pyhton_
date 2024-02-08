# with temp variable.
a=5
b=10

temp=a
a=b
b=temp

print(a)
print(b)

# without temp variable.
a=5
b=10

a,b=b,a
print(a)
print(b)