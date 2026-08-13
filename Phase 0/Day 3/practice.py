# print 1 To 100
'''
for i in range(1,101):
    print(i,end=" ")
'''

# Print 100 TO 1
'''
for i in range(100,0,-1):
    print(i,end=" ")
''' 

# Even Number 
'''
num=int(input("Enter a Number Here ... "))
for i in range(num+1):
    if i%2==0:
        print(i,end=" ")
'''

# Odd Number
'''
num=int(input("Enter a Number Here .. "))
for i in range(num+1):
    if i%2!=0:
        print(i,end=" ")
'''
# Sum of Even Number
'''
num=int(input("Enter Number Here "))
total=0
for i in range(num+1):
    if i%2==0:
        total=total+i
        print(i,end=" ")
print("Sum",total)
'''
# prime Number CHecker
'''
num=int(input("Enter Number Here "))
count=0
for i in range(1,num+1):
    if num%i==0:
        count=count+1
    print(i,end=" ")

if count==2:
    print("h",num,"Prime Number")
else:
    print("n",num,"Not Prime Number")
'''
# Reverse Number
'''
num=int(input("Enter Number Here "))
for i in range(num,0,-1):
    print(i,end=" ")
''' 
# Digit Count
'''
count=0
digit=int(input("Enter Here "))
for i in str(digit):
    count+=1

print("Total Digit",count)
'''

# PalliDrome Number Checker
'''
num=int(input("Enter Number Here "))
for i in range(1,num+1):
    if str(i)==str(i)[::-1]:
        print(i,end=" ")
'''

# Armstrong Number
'''
num=int(input("Enter Number Here.. "))

for i in range(1,num+1):
    count=0

    for j in str(i):
        count=count+int(j)**3

    if count==i:
        print(i," is Armstrong Number ")
else:
    print("And Other are Not Armstrong Number")
'''