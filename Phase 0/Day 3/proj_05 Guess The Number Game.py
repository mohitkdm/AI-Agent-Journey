fixnumber=int(input("Enter a Number to Fix : "))

attempts=0

while True:
    guessnumber=int(input("Enter Your Number : "))
    attempts=attempts+1

    if guessnumber==fixnumber:
        print("Correct Guess")
        print("Total Attempts",attempts)
        print(exit())

    else:
        print("Wrong Guess ... ")