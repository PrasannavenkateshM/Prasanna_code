def righthalfpyramid():
    #hardcoding the input
    n=5
    for i in range(1,n+1):
        print("*"*i)

    m=10
    for i in range(1,m+1):
        print("*"*i)

    o=int(input("Enter the number of rows we want in right half triangle:"))
    for i in range(1,o+1):
        print("*"*i)

    #mestedlogic
    a=5
    for i in range(1,a+1):
        for j in range(i):
            print("* ",end="")
        print()

    b=int(input("Enter the number of rows required through nested loop:"))
    for i in range(1,1+b):
        for j in range(i):
            print("* ",end="")
        print()

    c=5
    for i in range(1,c+1):
        print("*"*i)

    d=int(input("enter the number of rows needed:"))
    for i in range(1,d+1):
        for j in range(i):
            print("*", end="")
        print()
if __name__=="__main__":
    righthalfpyramid()