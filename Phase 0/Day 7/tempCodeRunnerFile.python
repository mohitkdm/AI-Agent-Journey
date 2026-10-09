# Expense Tracker


# Add Expense
def add_expense():
    try:
        title = input("Enter title: ")
        amount = int(input("Enter amount: "))

        with open("expenses.txt", "a") as file:
            file.write(title + "," + str(amount) + "\n")

        print("Expense Added Successfully!")


    except ValueError:
        print("Please Enter A Valid Amount.")

    except Exception as e:
        print("Error:", e)


# View Expenses
def view_expenses():
    try:
        with open("expenses.txt", "r") as file:
            expenses = file.readlines()

        if not expenses:
            print("No Expenses Found.")

        else:
            print("\n----- All Expenses -----")

            for expense in expenses:
                title, amount = expense.strip().split(",")

                print(title, "- ₹" + amount)


    except FileNotFoundError:
        print("No Expense File Found.")


# Calculate Total
def calculate_total():
    try:
        with open("expenses.txt", "r") as file:
            expenses = file.readlines()

        total = 0

        for expense in expenses:
            title, amount = expense.strip().split(",")

            total = total + int(amount)

        print("Total Expense = ₹", total)


    except FileNotFoundError:
        print("No Expenses Found.")

    except ValueError:
        print("Invalid Expense Data.")


# Main Menu
while True:

    try:
        print("\n=========================")
        print("      EXPENSE TRACKER")
        print("=========================")

        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Calculate Total")
        print("4. Exit")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            calculate_total()

        elif choice == "4":
            print("Thank You For Using Expense Tracker!")
            break

        else:
            print("Please Choose A Valid Option.")

    except Exception as e:
        print("Error:", e)