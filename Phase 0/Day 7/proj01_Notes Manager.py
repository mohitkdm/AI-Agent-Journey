# Notes Manager

notes=[]

# Add Notes
def add_note():
    title=input("Enter the Title of Notes :- ")
    desc=input("Enter the Notes details :- ")

    note={
        "title":title,
        "desc":desc
    }
    notes.append(note)
    print("Note Add Successfullyy...... ")

# View Notes
def view_note():
    if len(notes)==0:
        print("Note are not Yet..........")
    else:
        print("|| All Notes || ")
        for note in notes:
            print("Title : ",note["title"])
            print("Discription : ",note["desc"])
            print("-_-"*15)

# main menu
while True:
    print("---- Hello To Note Manager ----")
    print("1. For Add Note ")
    print("2. For View Note ")
    print("3. For Exit ")

    choice=(input("Enter Your Choice ... "))
    if choice=='1':
        add_note()
    elif choice=='2':
        view_note()
    elif choice=='3':
        print("Thanks For Using Notes Manager 🌹🌹 .")
        break
    else:
        print("Please Choose Correct Operation...")