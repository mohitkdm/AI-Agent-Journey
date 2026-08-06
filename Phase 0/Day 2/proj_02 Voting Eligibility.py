# Voting Eligibility

age=int(input("Please Enter Your Age Here... "))
if 0<age<18:
    print("Your are under 18 , So you can't Eligible for voting \n Please wait for complete 18...")
elif age>=18:
    print("You are Eligible For Voting ")
else:
    print("Please write carefully... ")