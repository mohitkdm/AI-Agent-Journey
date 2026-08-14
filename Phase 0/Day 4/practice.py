# Hello print fun()
'''
def greet():
    name=input("Enter Your Name ")
    print("Hello",name)
greet()
'''

# Add Two Number
'''
def addition():
    a=int(input("Enter Ist Number "))
    b=int(input("Enter 2nd Number "))
    return a+b
print("The Answer is",addition())
'''

# Sub the number
'''
def substraction():
    a=int(input("Enter Ist Number "))
    b=int(input("Enter 2nd Number "))
    return a-b
print("The answer is",substraction())
'''

# Multiply Numbers
'''
def Multiplication():
    a=int(input("Enter Ist Number "))
    b=int(input("Enter 2nd Number "))
    return a*b
print("The answer is",Multiplication())
'''

# Division
'''
def division():
    a=int(input("Enter Ist Number "))
    b=int(input("Enter 2nd Number "))
    return a/b
print("The answer is",division())
'''

# Square 
'''
def square():
    number=int(input("Enter the Number for Square : "))
    return number**2

print("The Square is",square())
'''

# Cube
'''
def cube():
    number=int(input("Enter the Number for Square : "))
    return number**3

print("The Cube is",cube())
'''
    
# Even/Odd Checker
'''
def even_odd():
    number=int(input("Enter a Number Here... "))
    if number%2==0:
        print("The Number is Even")
    else:
        print("The Number is Odd")
even_odd()
'''

# Largest two Number
'''
def largest():
    number1=int(input("Enter Ist Number "))
    number2=int(input("Enter 2nd Number "))

    if number1>number2:
        print("Ist Number is Largest ",number1)
    else:
        print("2nd Number is Largest ",number2)
largest()
'''

# Largest of Three Number
'''
def largest():
    number1=int(input("Enter 1st Number "))
    number2=int(input("Enter 2nd Number "))
    number3=int(input("Enter 3rd Number "))

    if number1>number2 and number1>number3:
        print("1st Number is Greatest",number1)
    elif number2>number3:
        print("2nd Number is Greatest",number2)
    else:
        print("3rd Number is Greatest",number3)

largest()
'''

# Factorial
'''
def fac():
    fact=1
    number=int(input("Enter Your Number "))
    for i in range(1,number+1):
        fact*=i
    print(fact)

fac()
'''

# Prime Number Checker
'''
def is_prime():
    count=0
    number=int(input("Enter Number Here... "))
    if number>0:
        for i in range(1,number+1):
            if number%i==0:
                count+=1
        if count==2:
            print("Prime Number ",number)
        else:
            print("Not Prime Number ",number)
    else:
        print("Negative Are Not Access ")

is_prime()
'''

# Reverse Number
'''
def reverse():
    number=int(input("Enter a Number "))
    for i in range(number,0,-1):
        print(i,end=" ")
reverse()
'''

# Pallidrome
'''
def palidrome():
    user=input("Enter Here... ")
    if str(user)==str(user)[::-1]:
        print("Pallidrome",user)
    else:
        print("Not Pallidrome",user)

palidrome()
'''

# Calculate Percentage
def perc():
    usr=int(input("Total obtained number "))
    usrt=int(input("Total maximum number "))
    return (usr*100)/usrt

print("Percentage is ",perc())