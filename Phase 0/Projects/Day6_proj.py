
# Student Management System

students = []


# Add Student
def add_stud():

    name = input("Enter Your Name :- ")
    age = int(input("Enter Your Age :- "))
    course = input("Enter Your Course :- ")
    marks = float(input("Enter Your Marks :- "))

    student = {
        "name": name,
        "age": age,
        "course": course,
        "marks": marks
    }

    students.append(student)

    print("Student Added Successfully!")


# View Student
def view_stud():

    if len(students) == 0:
        print("Not Found Any Student Record...")
        return

    print("\n--- Students List ---")

    for student in students:

        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Course:", student["course"])
        print("Marks:", student["marks"])
        print("-" * 20)


# Search Student
def search_stud():

    search = input("Enter Student Name For Search :- ")

    for student in students:

        if student["name"].lower() == search.lower():

            print("\n|| Student Found ||")
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Course:", student["course"])
            print("Marks:", student["marks"])

            return

    print("Student Not Found!")


# Update Student
def update_stud():

    search = input("Enter Student Name For Updation :- ")

    for student in students:

        if student["name"].lower() == search.lower():

            print("\nUpdate The Details Of", student["name"])

            while True:

                print("\nChoose The Updation.....")
                print("1. For Update Name")
                print("2. For Update Age")
                print("3. For Update Course")
                print("4. For Update Marks")
                print("5. For Update Exit")

                choose = input("Enter Your Choice For Update: ")

                # Update Name
                if choose == "1":

                    new_name = input(
                        "Enter Your New Name For Update :- "
                    )

                    student["name"] = new_name

                    print(
                        "Your New Name",
                        new_name,
                        "is Updated Successfully..."
                    )


                # Update Age
                elif choose == "2":

                    student["age"] = int(
                        input("Enter Your New Age For Update :- ")
                    )

                    print("Your New Age Is Updated Successfully...")


                # Update Course
                elif choose == "3":

                    student["course"] = input(
                        "Enter Your New Course For Updation :- "
                    )

                    print("Your New Course Updated Successfully...")


                # Update Marks
                elif choose == "4":

                    student["marks"] = float(
                        input("Enter Your New Marks For Updation :- ")
                    )

                    print("Your New Marks Updated Successfully...")


                # Exit Update
                elif choose == "5":

                    print("Updation Is Completed.....")
                    return


                else:

                    print("Please Choose Carefully And Try Again!")

            return

    print("Student Not Found!")


# Delete Student
def delete_stud():

    search = input("Enter Student Name For Delete :- ")

    for student in students:

        if student["name"].lower() == search.lower():

            students.remove(student)

            print("Student Deleted Successfully.....")
            return

    print("Student Not Found.....")


# Calculate Average Marks
def cal_marks_avg_stud():

    if len(students) == 0:

        print("Student Not Found!")
        return

    total = 0

    for student in students:

        total += student["marks"]

    average = total / len(students)

    print("Average Marks:", average)


# Main Menu

while True:

    print("\n" + "=" * 30)
    print(" Student Management System")
    print("=" * 30)

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Calculate Average Marks")
    print("7. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":

        add_stud()

    elif choice == "2":

        view_stud()

    elif choice == "3":

        search_stud()

    elif choice == "4":

        update_stud()

    elif choice == "5":

        delete_stud()

    elif choice == "6":

        cal_marks_avg_stud()

    elif choice == "7":

        print("Thank You! Program Exited.")
        break

    else:

        print("Invalid Choice! Please Try Again!")

