import json
from os.path import exists
from utils import *


def main():
    # present list of commands and take input
    user_input = input("\nWelcome to your contact list!\n\n" \
                            "The following is a list of usable commands:\n" \
                            "'add': Adds a contact.\n" \
                            "'delete': Deletes a contact.\n" \
                            "'list': List all contacts.\n" \
                            "'search': Searches for a contact by name.\n" \
                            "'q': Quits the program and saves the contact list.\n\n" \
                            "Type a command: ")

    # infinite loop to gather input
    while True:
        # if command == 'add' then ask for user input
        if user_input.lower() == 'add':
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            cont = input("Add numbers, email, and address? (y/n): ")

            if cont.lower() == 'y':
                # verifies mobile num
                mobile_num = input("Mobile Phone Number: ")
                while True:
                    for char in mobile_num:
                        if not char.isdigit() or len(mobile_num) != 10: 
                            mobile_num = input("\nInvalid entry!\nMobile Phone Number: ")
                            break
                    else:
                        break
                if mobile_num == "":
                    mobile_num = None

                # verifies home num    
                home_num = input("Home Phone Number: ")
                while True:
                    for char in home_num:
                        if not char.isdigit() or len(home_num) != 10: 
                            home_num = input("\nInvalid entry!\nHome Phone Number: ")
                            break
                    else:
                        break
                if home_num == "":
                    home_num = None

                # verifies email
                email = input("E-mail address: ")
                while True:
                    
                    if '@' not in email:
                        email = input("\nInvalid entry!\nE-mail address: ")
                    else: 
                        check = email.split('@')[1]
                        if '.' in check: break
                        else: email = input("\nInvalid entry!\nE-mail address: ")

                # verifies address
                address = input("Address: ")
                if address== "":
                    address = None

                add_contact(first_name, last_name, mobile_num, home_num, email, address)
            else:
                add_contact(first_name, last_name)

        # if command == 'delete' ask for input
        if user_input.lower() == 'delete':
            first_name = input("First Name: ")
            last_name = input("Last Name: ")

            delete_contact(first_name, last_name)

        # if command == 'list' list all contacts in list
        if user_input.lower() == 'list':
            list_contacts()

        # if command == 'search' search contacts based on input
        if user_input.lower() == 'search':
            first_name = input("First Name: ")
            last_name = input("Last Name: ")

            search_contacts(first_name, last_name)


        # if command == 'q' quit program
        if user_input.lower() == 'q':
            print("\nContacts saved successfully.\nQuitting program...")
            break

        user_input = input("Type a command: ")

# run if not imported
if __name__ == '__main__':
    # check if contacts list file exists in current dir
    file_exists = exists('contacts_list.json')

    if file_exists: main()
    # if file != exist, populate with test contact
    else:
        init_entry = {'contacts': [{'first_name':'John', 
                            'last_name':'Doe', 
                            'mobile_num':'1234567890', 
                            'home_num':'1234567890', 
                            'email':'doe@gmail.com', 
                            'address':'123 Apple Rd'}]}

        with open("contacts_list.json", "w") as file:
            json.dump(init_entry, file)
        
        print("\nNo contacts list detected.\n" \
            "Creating new contacts list...")
        main()