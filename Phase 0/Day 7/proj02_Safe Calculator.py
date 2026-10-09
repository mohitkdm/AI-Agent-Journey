# Safe Calcuator  

while True:
    try:
        print("*----- Welcome To Safe Calculator -----*")
        print("1 For Add")
        print("2 For Sub")
        print("3 For Multiply")
        print("4 Divide")
        print("5 For Exit")

        choice=(input("Enter Your Choice : "))
        if choice=='5':
            print("Exit The Program.....")
            break
        elif choice not in ['1','2','3','4']:
            print("Please Choose Correct Option ")
            continue
        
        number1=int(input("Enter Your 1st Number : "))
        number2=int(input("Enter Your 2nd Number : "))

        if choice=='1':
            result=number1+number2
            print("Result : ",result)
        elif choice=='2':
            result=number1-number2
            print("Result : ",result)
        elif choice=='3':
            result=number1*number2
            print("Result : ",result)
        elif choice=='4':
            result=number1/number2
            print("Result : ",result)
        
    except ValueError:
        print("Please Enter the valid data .")
    except ZeroDivisionError:
        print("Can not divide by Zero(0)")
