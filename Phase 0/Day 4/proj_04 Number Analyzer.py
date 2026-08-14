number=int(input("Enter a Number : "))
def is_even():
    if number%2==0:
        print("Even : ",True)
    else:
        print("Even : ",False)


def is_positive():
    if number>0:
        print("Positive :",True)
    elif number==0:
        print("Zero :",True)
    else:
        print("Negative :",True)


def is_prime():
    count = 0
    if number < 2:
        print("Prime :", False)
        return

    for i in range(1, number + 1):
        if number % i == 0:
            count += 1

    if count == 2:
        print("Prime :", True)
    else:
        print("Prime :", False)    


def is_Fac():
    fac=1
    if number<0:
        print("Factorial not Defined For this",number)
    else:
        for i in range(1,number+1):
            fac=fac*i
        print("factorial : ",fac)


def multiplication():
    for i in range(1,11):
        print(f"{number}X{i}={number*i}")


is_even()
is_positive()
is_prime()
is_Fac()
multiplication()