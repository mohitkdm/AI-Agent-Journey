# Else or Finally
# else
try:
    number=int(input("Enter the Number "))
    result=100/number
    print(result)

except ValueError:
    print("Enter The valid input ")
except ZeroDivisionError:
    print("Please Enter the above of 0 ")
else:
    print("Error Free Code..........")


# finally
try:
    number=int(input("Enter the Number "))
    result=100/number
    print(result)

except ValueError:
    print("Enter The valid input ")
except ZeroDivisionError:
    print("Please Enter the above of 0 ")
else:
    print("Error Free Code..........")
finally:
    print("Program finish")