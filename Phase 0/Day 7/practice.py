# File Handling

'''
# Create a file.
file=open("hey.txt",'w')
cont=file.write()
print(cont)
file.close()
'''
'''
# Write text to a file.
file=open("hey.txt",'w')
cont=file.write("Hello jii..... ")
print(cont)
file.close()
'''
'''
# Read a file.
file=open("hey.txt",'r')
cont=file.read()
print(cont)
file.close()
'''
'''
# Read first line.
file=open("hey.txt",'r')
cont=file.readline()
print(cont)
file.close()
'''
'''
# Read all lines.
file=open("hey.txt",'r')
cont=file.readlines()
print(cont)
file.close()
'''

# Append text.
# Count number of lines.
'''
file=open("hello.txt","r")
lines=file.readlines()
print(lines)
print("Total Lines :",len(lines))
file.close()
'''

# Count words in a file.
'''
file=open("hey.txt","r")
lines=file.read()
words=lines.split()
print(words)
print("Total Words :",len(words))
file.close()
'''

# Exception Handling
# Handle invalid integer input.
'''
try:
    number=int(input("Ener The Number :- "))
    print(number)
except ValueError:
    print("Invalid Value Input")
'''

# Handle division by zero.
'''
while True:
    try:
        number1=int(input("Enter the First Number :- "))
        number2=int(input("Enter the Second Number :- "))
        result=number1/number2
        print(result)
        break
    except ValueError:
        print("Please write valid data...")
    except ZeroDivisionError:
        print(number2,"Is zero so they can't divisior")
'''

# Handle multiple exceptions.
'''
while True:
    try:
        num1=int(input("Enter The 1st Number :- "))
        num2=int(input("Enter The 2nd Number :- "))
        Result=num1/num2
        print("Result : ",Result)
        break
    except ValueError:
        print("Please Enter The Valid Input Data")
    except ZeroDivisionError:
        print("Cannot divide By 0 ")
'''
# Use else with try.
'''
try:
    num1=int(input("Enter Number :- "))
    num2=int(input("Enter Number :- "))
    result=num1/num2
    print("Result",result)
except ValueError:
        print("Please Enter The Valid Input Data")
except ZeroDivisionError:
    print("Cannot divide By 0 ")
else:
    print("Error Free Code...... ")
'''

# Use finally.
'''
try:
    num1=int(input("Enter Number :- "))
    num2=int(input("Enter Number :- "))
    result=num1/num2
    print("Result",result)
except ValueError:
        print("Please Enter The Valid Input Data")
except ZeroDivisionError:
    print("Cannot divide By 0 ")
else:
    print("Error Free Code...... ")
finally:
     print("Program Run... ")
'''

# Raise a custom ValueError.
'''
try:
    age = int(input("Enter Your Age :- "))
    if age<0:
        raise ValueError("Age can not -ve ")
    print("Your Age :",age)
except ValueError as e:
    print("Error :",e)
'''

# Build a safe calculator.
while True:
    try:
        print("\n----- Safe Calculator -----")
        print("1. For Add")
        print("2. For Subtract")
        print("3. For Multiply")
        print("4. For Divide")
        print("5. For Exit")

        choice = input("Enter Your Choice :- ")

        if choice == '5':
            print("Program Complete....")
            break

        if choice not in ['1', '2', '3', '4']:
            print("Please choose a valid option.")
            continue

        num1 = int(input("Enter the 1st Number :- "))
        num2 = int(input("Enter the 2nd Number :- "))

        if choice == '1':
            result = num1 + num2

        elif choice == '2':
            result = num1 - num2

        elif choice == '3':
            result = num1 * num2

        elif choice == '4':
            result = num1 / num2

        print("Result :", result)

    except ValueError :
        print("Please Enter Valid Number")

    except ZeroDivisionError:
        print("Can't Divide by 0 ")
            