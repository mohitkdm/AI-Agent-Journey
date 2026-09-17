# Student Management System

students=[]

# add student 
def add_stu():
    name=input("Enter Your Name Here... ")
    age=input("Enter Your Age Here... ")
    course=input("Enter Your Course Here... ")

    student={
        "Name":name,
        "Age":age,
        "Course":course
    }
    students.append(student)
    print("--- Student addes successfull ---")

# View Student 
def view_stu():
    if len(students)==0:
        print("No student yet..")
    else:
        print("\n|| Student List ||")

        for student in students:
            print("Name :",student["Name"])
            print("Age :",student["Age"])
            print("Course :",student["Course"])
            print("------------------------")

# Search Student
def search_stu():
    name=input("Enter Student name to Search ")
    found=False
    for student in students:
        if student["Name"].lower()==name.lower():
            print("\n Student Found ")
            print("Name:", student["Name"]) 
            print("Age:", student["Age"]) 
            print("Course:", student["Course"]) 
            found = True 
            break

    if not found:
        print("Student Not Found ! ")

# Delete Student 
def delete_stu():
    name=input("Enter student name to delete :")
    for student in students:
        if student["Name"].lower()==name.lower():
            students.remove(student)
            print("Student Deleted SuccessFuly.... ")
            return
    print("Student Not Found ! ")

# Main Menu
while True:
    print("\n===== Student Management System =====") 
    print("1. Add Student") 
    print("2. View Students") 
    print("3. Search Student") 
    print("4. Delete Student") 
    print("5. Exit")

    choice=input("Enter your choice in 1,2,3,4,5    :-  ")

    if choice == "1": 
        add_stu() 
    elif choice == "2": 
        view_stu() 
    elif choice == "3": 
        search_stu() 
    elif choice == "4": 
        delete_stu() 
    elif choice == "5": 
        print("Thank you! Program exited.") 
        break 
    else: 
        print("Invalid choice! Please try again.")
