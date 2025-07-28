contacts = []

while True:
    print("\n--- Contact Book Menu ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contacts.append({"name": name, "phone": phone})
        print("Contact added successfully!")

    elif choice == '2':
        print("\n--- All Contacts ---")
        for contact in contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}")

    elif choice == '3':
        search_name = input("Enter name to search: ")
        found = False
        for contact in contacts:
            if contact["name"].lower() == search_name.lower():
                print(f"Found: {contact['name']} - {contact['phone']}")
                found = True
                break
        if not found:
            print("Contact not found.")

    elif choice == '4':
        print("Exiting Contact Book. Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
