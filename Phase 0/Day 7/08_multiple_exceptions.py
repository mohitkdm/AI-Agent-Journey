try:
    number=int(input("Enter Number "))
    result=100/number
    print(result)
except ValueError:
    print("Enter The Correct/Valid Number")
except ZeroDivisionError:
    print("Enter The above 0 ")
    