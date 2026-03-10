def printstatement():
    print("Hey!, This is the first time I am trying to write a code. I am in attending the client call and trying to learn")

    name = "Prasannavenkatesh Manigandan"
    print(name)
    age = 12+10
    print(age)
    intern_experience=0.6
    work_experience=0.8
    print("Total work experience", intern_experience+work_experience)

    name_input=input("Enter your name:")
    age_input=input("Enter your age:")
    workexp_input=float(input("Enter your total work experience:"))
    print(name_input,age_input,workexp_input, sep="\n")

if __name__ == "__main__":
    printstatement()
