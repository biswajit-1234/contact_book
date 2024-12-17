# Contactbook Project
def contact():
    contact={}
    print("name\t\tcontact number")
    def display_contact():
        for key in contact:
            print(f"Name is {contact.get(name)} and mobile number is{contact.get(phone)}")
    while True:
        choice=int(input("Enter\n 1.Add new contact\n 2. Search contact\n 3. Display contact \n 4. Edit contact\n 5.Delete contact\n 6.Exit\n Enter choice\n"))
        match choice:
            case 1:
                name=input("Enter the contact name:")
                phone=int(input("Enter the mobile number:"))
                contact[name]=phone
            case 2:
                search_name=input("Enter the contact name:")
                if search_name in contact:
                    print(search_name,"contact number is",contact[search_name])
                else:
                    print("Name is not found in contact book")
            case 3:
                if not  contact:
                    print("Empty contact book.")
                else:
                    display_contact()
            case 4 :
                edit_contact=input("Enter the contact to be edited")
                if edit_contact in contact:
                    phone=input("Enter mobile number:")
                    contact[edit_contact]=phone
                    print("Contact updated")
                    display_contact()
                else:
                    print("Name is not found in contact book")
            case 5:
                del_contact=input ("Enter contact to be deleted:")
                if del_contact in contact:
                    confirm=input("Do you wnat to delete this contact y/n?")
                    if confirm =="y" or confirm=="Y":
                        contact.pop(del_contact)
                    display_contact()
                else:
                     print("Name is not found in contact book")
            case 6:
                print("")
                break
contact()               