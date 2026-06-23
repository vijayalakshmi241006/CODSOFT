contacts = {}

while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email: ")
        address = input("Enter Address: ")

        contacts[name] = {
            "Phone": phone,
            "Email": email,
            "Address": address
        }

        print("Contact Added Successfully!")

    elif choice == "2":
        if not contacts:
            print("No Contacts Found!")
        else:
            for name, details in contacts.items():
                print("\nName:", name)
                print("Phone:", details["Phone"])
                print("Email:", details["Email"])
                print("Address:", details["Address"])

    elif choice == "3":
        name = input("Enter Name to Search: ")

        if name in contacts:
            print(contacts[name])
        else:
            print("Contact Not Found!")

    elif choice == "4":
        name = input("Enter Contact Name to Update: ")

        if name in contacts:
            phone = input("New Phone: ")
            email = input("New Email: ")
            address = input("New Address: ")

            contacts[name] = {
                "Phone": phone,
                "Email": email,
                "Address": address
            }

            print("Contact Updated!")
        else:
            print("Contact Not Found!")

    elif choice == "5":
        name = input("Enter Contact Name to Delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact Deleted!")
        else:
            print("Contact Not Found!")

    elif choice == "6":
        print("Exiting Contact Book...")
        break

    else:
        print("Invalid Choice!")
