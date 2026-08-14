def calculator():
    number1=int(input("Enter Your First Number :-  "))
    number2=int(input("Enter Your Second Number :-  "))

    def add(a,b):
        return a+b
    def sub(a,b):
        return a-b
    def mul(a,b):
        return a*b
    def div(a,b):
        return a/b

    print("1. + for Addition \n 2. - for Substration \n 3. * for Multiplication \n 4. / for Division ")
    choose=input("Enter Your Perform Operation ")


    if choose=='+':
        print(add(number1,number2))
    elif choose=='-':
        print(sub(number1,number2))
    elif choose=='*':
        print(mul(number1,number2))
    elif choose=='/':
        print(div(number1,number2))

calculator()