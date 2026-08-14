def temperature_convertor():
    def cel_to_fah():
        C=int(input("Enter The Celsius To Convert Fahrenheit "))
        return (C * 9/5)+32

    def fah_to_cel():
        F=float(input("Enter The Fahrenheit To Convert Celsius "))
        return (F - 32) * 5/9

    choose=input("Enter Choose Your performing Task \n1. for Celsius To Convert Fahrenheit \n 2. for Fahrenheit To Convert Celsius \n ")
    if choose=="1":
        print(cel_to_fah())
    elif choose=="2":
        print(fah_to_cel())
    else:
        print("Please Select Carefully .................")

temperature_convertor()