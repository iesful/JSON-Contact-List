import json

# Will maybe add a command to allow the user to edit an existing contact.

# adds a contact to the list if one does not already exist
def add_contact(f_name, l_name, m_num=None, h_num=None, e_mail=None, address=None):
    
    new_contact = {'first_name': f_name, 'last_name': l_name, 'mobile_num':m_num,
                 'home_num': h_num, 'email': e_mail, 'address': address}

    # load json as python dict
    with open("contacts_list.json", "r") as file:
        contacts_infile = json.load(file)

    # iterate through each contact in list and verify that another
    # contact does not already exist w/ same info
    for entry in contacts_infile['contacts']:
        if entry['first_name'] == f_name and entry['last_name'] == l_name:
            print("\nA contact with this name already exists.")
            print("Contact not added.\n")
            break
    # if no break detected, add contact to list    
    else:
        with open("contacts_list.json", "w") as file:
            contacts_infile['contacts'].append(new_contact)
            json.dump(contacts_infile, file)
            
            print("\nContact successfully added.\n")

# delete specified contact from list
def delete_contact(first_name, last_name):
    # load json as python dict
    with open("contacts_list.json", "r") as file:
        contacts_infile = json.load(file)

    # enum through list of dicts
    for idx, entry in enumerate(contacts_infile['contacts']):
        # when match is found confirm deletion
        if entry['first_name'] == first_name and entry['last_name'] == last_name:
            verify = input("Are you sure you want to delete this contact? (y/n): ")
            # if verified, delete contact
            if verify.lower() == 'y':
                contacts_infile['contacts'].pop(idx)

                # write new contact list after confirmation
                with open("contacts_list.json", "w") as file:
                    json.dump(contacts_infile, file)

                print("\nContact successfully deleted.\n")
                break
            else:
                print("\nCancelling request...")
                break
    else:
        print("\nNo contact with that information found.\n")

# list all contacts in list
def list_contacts():
    # load json as python dict
    with open("contacts_list.json", "r") as file:
        contacts_infile = json.load(file)

    # iterate through all contacts in list and print in format
    for idx, entry in enumerate(contacts_infile['contacts'], 1):
        print(f"{idx}. {entry['first_name']} {entry['last_name']}\n"\
                f"\tMobile: {entry['mobile_num']}\n"\
                f"\tHome: {entry['home_num']}\n"\
                f"\tEmail: {entry['email']}\n"\
                f"\tAddress: {entry['address']}\n")

# search for contacts based on input
def search_contacts(first_name, last_name):
    # load json as python dict
    with open("contacts_list.json", "r") as file:
        contacts_infile = json.load(file)

    # keep track of search matches
    entries_found = 0
    list_of_found = []

    # iterate through list of contacts and note matches
    for entry in contacts_infile['contacts']:
        if first_name.lower() in entry['first_name'].lower() and last_name.lower() in entry['last_name'].lower():
            entries_found += 1
            list_of_found.append(entry)
    print(f"\nFound ({entries_found}) matches.")

    # iterate through list of matches and print
    for idx, contact in enumerate(list_of_found, 1):
        if first_name.lower() in contact['first_name'].lower() and last_name.lower() in contact['last_name'].lower():
            print(f"{idx}. {contact['first_name']} {contact['last_name']}\n"\
                f"\tMobile: {contact['mobile_num']}\n"\
                f"\tHome: {contact['home_num']}\n"\
                f"\tEmail: {contact['email']}\n"\
                f"\tAddress: {contact['address']}\n")