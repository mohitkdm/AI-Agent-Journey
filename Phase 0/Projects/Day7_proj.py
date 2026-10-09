# Student Management System v2.

# Add Student 
def add_student():
    try:
        name=input("Enter Your Name : ").strip()
        if not name:
            print("Student name cannot be Empty! ")
            return
        
        age=int(input("Enter Your Age : "))
        if age<=0:
            print("Age must be greater than 0! ")
            return
        
        course=input("Enter Your Course : ")
        if not course:
            print("Course not Empty! ")
            return
        
        marks=int(input("Enter Your Marks : "))
        if 0>marks or marks>100:
            print("Marks must be between 0 and 100! ")
            return
        
        with open("student.txt",'a')as file:
            file.write(f"{name},{age},{course},{marks} \n")
        print("Student Added Successfully........")
    
    except ValueError:
        print("Invalid Input! Age and Marks must be Integers. ")
    except OSError as e:
        print("File Error : ",e)


# View Student 
def view_student():
    try:
        with open("student.txt",'r') as file:
            students=file.readlines()

        if not students:
            print("No Student Record Found ! ")
            return
        
        print("\n ----- All Student Record ----- ")
        for student in students:
            name,age,course,marks=student.strip().split(",")
            print("Name : ",name)
            print("Age : ",age)
            print("Course : ",course)
            print("Marks : ",marks)
            print("-"*20)
    
    except FileNotFoundError:
        print("Student File does not exist yet. First Add a Student... ")
    
    except ValueError:
        print("Student file contains Invalid Data.....")
    
    except OSError as e:
        print("File Error : ",e)

# Search Student 
def search_student():
    try:
        search_name=input("Enter the Student Name For Search : ")

        if not search_name:
            print("Search name cannot be Empty! ")
            return
        
        found=False
        
        with open("student.txt",'r') as file:
            for student in file:
                name,age,course,marks=student.strip().split(",")
                if name.lower()==search_name.lower():
                    print("\n Student Found.....")
                    print("Name : ",name)
                    print("Age : ",age)
                    print("Course : ",course)
                    print("Marks : ",marks)
                    found=True
        
        if not found:
            print("Student Not Found! ")
        
    except FileNotFoundError:
        print("Student file does not exist Yet.")
    except ValueError:
        print("Student file Contains Invalid Data...")
    except OSError as e:
        print("File Error : ",e)

# Delete Student 
def delete_student():
    try:
        delete_name=input("Enter The Student Name For Delete : ")
        
        if not delete_name:
            print("Student Name Cannot be Empty! ")
            return
        
        with open("student.txt",'r') as file:
            students=file.readlines()
        
        updated_student=[]
        found=False
        for student in students:
            name,age,course,marks=student.strip().split()

            if name.lower()==delete_name.lower() and not found:
                found=True
            
            else:
                updated_student.append(student)
        
        if found:
            with open("student.txt",'r') as file:
                file.writelines(updated_student)

            print("Student Deleted SuccessFully!....... " )
    
    except FileNotFoundError:
        print("Student File Does Not Exist Yet. ")
    except ValueError:
        print("Student File Contains Invaid Data ")
    except OSError as e:
        print("File Error : ",e)

# Main Menu
while True:
    print("\n ===================== ")
    print("Student Management System")
    print("=======================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student ")
    print("4. Delete Student ")
    print("5. Exit Program")

    choice=input("Enter Your Choice : ").strip()

    if choice=='1':
        add_student()
    elif choice=='2':
        view_student()
    elif choice=='3':
        search_student()
    elif choice=='4':
        delete_student()
    elif choice=='5':
        print("Program Completed........ ")
        print("\n Thanks For Using Student Management System... ")
        break
    else:
        print("Invalid Menu Choice! Please select 1 to 5 ")