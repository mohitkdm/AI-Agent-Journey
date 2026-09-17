# Expense Tracker 

expenses=[]

# Add Expense

def add_expense():
    title=input("Enter Expense Title :- ")
    amount=int(input("Enter the Amount of Expense :- "))
    category=input("Enter the Category of Expense :- ")

    expense={
        "title":title,
        "amount":amount,
        "category":category
    }
    expenses.append(expense)
    print("Expense Add successfully ! ")

# View Expense

def view_expense():
    if len(expenses)==0:
        print("Sorry Expense Not Fount Yet ! ")
        return
    print("\n --- All Expense's --- ")
    for expense in expenses:
        print("Title :",expense["title"])
        print("Amount :",expense["amount"])
        print("Category :",expense["category"])
        print("-_-_-_-_-_-_-_-_-_-_-_-_-")

# Total Expense

def total_expense():
    total=0
    for expense in expenses:
        total+=expense["amount"]
    print("Total Expense Amount :",total)

# Higest Expense

def highest_expense():
    if len(expenses)==0:
        print("No Any Expense Now... ")
        return
    highest=expenses[0]
    for expense in expenses:
        if expense["amount"]>highest["amount"]:
            highest=expense
    print("\n --- Highest Expense --- ")
    print("Title :",highest["title"])
    print("Amount :",highest["amount"])
    print("Category :",highest["category"])
    print("*"*20)

# Category Wise Expense 

def category_wise_exp():
    category_expense={}
    for expense in expenses:
        category=expense["category"]
        amount=expense["amount"]

        if category in category_expense:
            category_expense[category]+=amount
        else:
            category_expense[category]=amount
    print("\n --- Category wise Expenses --- ")
    for category,amount in category_expense.items():
        print(category,"=",amount)

# Main Menu

while True:
    print("\n========== EXPENSE TRACKER ==========") 
    print("1. Add Expense") 
    print("2. View Expenses") 
    print("3. Total Expense") 
    print("4. Highest Expense") 
    print("5. Category-wise Expense") 
    print("6. Exit")

    choice = input("Enter Your Choice: ") 
    if choice == "1": 
        add_expense() 
    elif choice == "2": 
        view_expense() 
    elif choice == "3": 
        total_expense() 
    elif choice == "4": 
        highest_expense() 
    elif choice == "5": 
        category_wise_exp() 
    elif choice == "6": 
        print("Thank You! Expense Tracker Closed.") 
        break
    else: 
        print("Invalid Choice! Please Try Again.")