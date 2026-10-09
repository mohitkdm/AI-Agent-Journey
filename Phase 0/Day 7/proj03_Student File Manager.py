# Student File Manager 

# Add Student 
def add_stud():
    try:
        name=input("Enter Name : ")
        age=(input("Enter Age : "))
        course=input("Enter Course : ")
        marks=(input("Enter Marks : "))

        with open("student.txt",'a') as file:
            file.write(f"Name : {name} | Age : {age} | Course : {course} | Marks : {marks} \n")
        print("Student Added Successfully....")
    except Exception as e:
        print("Error : ",e)

# View Student
def view_stud():
    try:
        with open("student.txt",'r') as file:
            data=file.read()
        if data:
            print("\n ----- Student Records ----- ")
            print(data)
        else:
            print("No Student Record Found ")
    except FileNotFoundError:
        print("Student File does Not Exist ! ..")

#  Main Menu
while True:
    try:
        print("\n ----- Student File Manager ----- ")
        print("1. Add Student")
        print("2. View Student")
        print("3. Exit ")

        choice=input("Enter Your Choice : ")
        if choice=="1":
            add_stud()
        
        elif choice=='2':
            view_stud()

        elif choice=='3':
            print("Program Completed......... ")
            break
        
        else:
            print("Please Choose Correct option ......")
            continue

    except Exception as e:
        print("Error : ",e)