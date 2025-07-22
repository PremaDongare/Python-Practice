contact=[]

def add_contact():
    name=input("Enter Name")
    phone=input("enter phone number")
    email=input("enter your email")

    contact.append({"name":name, "phone":phone, "email":email})
    print("contact added successfully")

def search_contact():
    name=input("enter the name to search")
    found = False
    for con in contact:
        if con["name"].lower() == name.lower():
            print(f"Name :{con['name']}, Phone:{con['phone']}, Email:{con['email']}\n" )
            found=True
            break
        if not found:
            print("Contact not found.\n")

def update_contact():
    name = input("enter the name to update contact")
    for con in contact:
        if con["name"].lower()== name.lower():
            con["phone"] = input("Enter new phone no: ")
            con["email"] = input("enter new email:")

            print("contact updated succ")
            return
        else:
            print("contact not found\n")

def delet_contact():
    name = input("enter name you want to delete")
    for con in contact:
        if con["name"].lower() == name.lower():
            contact.remove(con)

            print("contact deleted successfully")
            return
        else:
            print("contact not found:\n")

def view_contacts():
    if not contact:
        print("no contact to display")
    else:
        print("All contacts:")
        for con in contact:
            print(f"Name:{con['name']}, Phone:{con['phone']}, Email:{con['email']}")
        print()

while True:
    print("------ Contact Book ------")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. View All Contacts")
    print("6. Exit")

    choice = input("Enter your choice(1-6):")

    if choice == '1':
        add_contact()
    elif choice == '2':
        search_contact()
    elif choice == '3':
        update_contact()
    elif choice == '4':
        delete_contact()
    elif choice == '5':
        view_contacts()
    elif choice == '6':
        print("Exiting Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.\n")
