def lefthalfpyramid():
    a=5
    for i in range(1,1+a):
        print(" "*(a-i)+"*"*i)


    b=int(input("Enter the number of rows for left half pyramid:"))
    for i in range(1,b+1):
        for j in range(b-i):
            print(" ",end="")
        for k in range(i):
            print("*",end="")
        print()
if __name__ == "__main__":
    lefthalfpyramid()
