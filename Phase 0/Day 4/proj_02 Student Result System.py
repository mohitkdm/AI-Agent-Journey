def student():

    name=input("Enter Your Name : ")

    mark1=int(input("Enter Your Marks subject Hindi "))
    mark2=int(input("Enter Your Marks subject Emglish "))
    mark3=int(input("Enter Your Marks subject Mathematics "))
    mark4=int(input("Enter Your Marks subject Social Science "))
    mark5=int(input("Enter Your Marks subject Science "))

    total=mark1+mark2+mark3+mark4+mark5
    perc=(total ) / 5

    print("\n--Student Details-- ")
    print("Student Name",name)
    print("Student Marks",total)
    print("Student Percentage",perc)

    if 90<perc<=100:
        print("Student Grade A+ ")
    elif 80<perc<=90:
        print("Student Grade A ")
    elif 70<perc<=80:
        print("Student Grade B ")
    elif 60<perc<=70:
        print("Student Grade C ")
    elif 50<perc<=60:
        print("Student Grade D ")
    else:
        print("Student Grade F ")

student()