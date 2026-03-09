
c=int(input("enter the number of rows:"))
for i in range(1,c+1):
    for j in range(c-i):
        print(" ", end="")
    for k in range(i):
        print(i, end="")
    print()

a=int(input("Enter the number of rows required:"))
for i in range(1,1+a):
    for j in range(a-i):
        print(" ",end="")
    for k in range(1,1+i):
        print(k,end="")
    print()

b=5
for i in range(1,1+b):
    for j in range(i):
        print(i, end="")
    print()