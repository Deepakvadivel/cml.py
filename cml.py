print( "welcome to cml")
contact={}
def display_contact():
    print("name\t\tcontactnumber")
    for key in contact:
        print("{}\t\t{}".format(key,contact.get(key)))

while True:
    choice=int(input("1.add new contact \n 2.search contact \n 201.edit contact \n 202.delete contact \n 3.view contact \n 4.exit \n enter the choice: "))
    if choice == 1:
        name = str(input("enter the contact name :"))
        phone = int(input("enter the mobile number :"))
        contact[name]=phone
    elif choice ==2:
        s_name = str(input("enter the contact name :"))
        if s_name in contact:
            print(s_name,"s contact number is",contact[s_name])
        else:
            print("name is not found in contact book")
    elif choice == 201:
        edit_contact = input("enter the contact to be edited :")
        if edit_contact in contact:
            phone =int(input("enter the mobile number :"))
            contact[edit_contact]=phone
            print("contact updated")
            display_contact()
        else:
            print("name is not found in contact book")
    elif choice == 202:
        delete_contact= input("enter the name :")
        if delete_contact in contact:
            confirm = input("do you want to delete this contact y/n? ")
            if confirm == "y" or confirm == "Y":
                contact.pop(delete_contact)
            display_contact()
        else:
            print("name is not found in contact book")
    elif choice == 3:
        if not contact:
            print("empty contact book")
        else:
            display_contact()
    else:
        print("################### bye bye program is end ###################")
        break
