# Contact Book

contacts={}

# Add Contact
def add_cont():
    name=input("Enter Your Name : ")
    phone=(input('Enter Your Phone Number : '))
    email=input("Enter Your Email : ")

    contacts[name]={
            "phone":phone,
            "email":email
    }
    print("Contact Added Successfully.. ")

# Search Contact
def search_cont():
    name=input("Enter Name For Search : ")
    if name in contacts:
        print("\n Contact Found ! ")
        print("Name",name)
        print("Phone",contacts[name]["phone"])
        print("Email",contacts[name]["email"])
        
    else:
        print("-- Contact Not Found --")

# Update Contact
def update_cont():
    name=input("Enter Name For Update : ")

    if name not in contacts:
        print("Contact Not  Found ")
        return
    
    while True:
            print("1. for Name ")
            print("2. for Phone Number ")
            print("3. for Email Id ")
            print("4. for Exit ")
            choose=input("Enter Your Operation for Update ")

            if choose=='1':
                new_name=input("Enter Your New Name : ")
                contacts[new_name]=contacts[name]
                del contacts[name]
                name=new_name
                print("Name Update SuccessFully! ")

            elif choose=='2':
                contacts[name]["phone"]=input("Enter Your New Phone Number : ")
                print("Phone Number Updated Successfully!")
            elif choose=='3':
                contacts[name]["email"]=input("Enter Your New Email ID : ")
                print("Email Updated Successfully!")
            elif choose == "4": 
                print("Update Finished.") 
                return
            else: print("Please Select Available Option.....")
        


# Delete Conatct
def delete_cont():
    name=input("Enter Name  For Delete : ")

    if name in contacts:
        del contacts[name]
        print("Contact delete Succeccfully ! ")
    else:       
        print("Contact Not Found ! ")

# View Contact
def view_cont():
    if len(contacts)==0:
        print("No Contact yet !...")
    else:
        print("\n -- Contact List --- ")
        for name,details in contacts.items():
            print("Name",name)
            print("Phone Number",details["phone"])
            print("Email Id",details["email"])
            print("---===---===---===---")

# Main Menu
while True:
    print("--- Contact Book --- ")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. View contact")
    print("6. Exit")

    choice=input("Enter Your Choice : ")
    if choice=='1':
        add_cont()
    elif choice=='2':
        search_cont()
    elif choice=='3':
        update_cont()
    elif choice=='4':
        delete_cont()
    elif choice=='5':
        view_cont()
    elif choice=='6':
        print("Thank You! Program Exited ")
        break
    else:
        print("Invalid Choice! Please try Again ")
