
def all():
    def add():
        number1=int(input("Enter 1st Number "))
        number2=int(input("Enter 2nd Number "))
        return number1+number2
    
    def sub():
        number1=int(input("Enter 1st Number "))
        number2=int(input("Enter 2nd Number "))
        return number1-number2
    
    def mul():
        number1=int(input("Enter 1st Number "))
        number2=int(input("Enter 2nd Number "))
        return number1*number2
    
    def div():
        number1=int(input("Enter 1st Number "))
        number2=int(input("Enter 2nd Number "))
        if number2==0:
            print("2nd number are not correct")
        else:
            return number1/number2
    
    def Even_odd():
        number1=int(input("Enter 1st Number "))
        if number1%2==0:
            print("The Number is Even",number1)
        else:
            print("The Number is Odd",number1)

    def prime():
        count=0
        number=int(input("Enter the Number "))
        if number<2:
            print("Negative are Not Valid ")
        else:
            for i in range(1,number+1):
                if number%i==0:
                    count+=1
            if count==2:
                print("Prime Number ",number)
            else:
                print("Not Prime Number",number)
    
    def Factorial():
        fact=1
        number=int(input("Enter the Number "))
        if number>=0:
            for i in range(1,number+1):
                fact*=i
            print("Factorial : ",fact)
        
        else:
            print("Negative Number are not allowed")

    def exit_():
        print("Exit ")

    choose=int(input("Enter Your Choose perform Task.. \n---- Choose Please--- \n1. Add\n 2. Subtract\n 3. Multiply\n 4. Divide\n 5. Even/Odd\n 6. Prime Check\n 7. Factorial\n 8. Exit\n :- "))
    if 1<=choose<=8:
        if choose==1:
            print("The Answer is ",add())
        elif choose==2:
            print("The Answer is ",sub())
        elif choose==3:
            print("The Answer is ",mul())
        elif choose==4:
            print("The Answer is ",div())
        elif choose==5:
            Even_odd()
        elif choose==6:
            prime()
        elif choose==7:
            Factorial()
        elif choose==8:
            exit_()
    else:
        print("Please Enter task Carefully.... ")

all()