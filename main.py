from contact import Contact
from contact_manager import ContactManager


if __name__ == "__main__":
    manager = ContactManager()
    print("Contact Manager")
    while True:
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Remove Contact")
        print("4. Display Contacts")
        print("5. Exit")

        choice = int(input("Enter your choice (1-5): "))

        if choice == 1:
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            contact = Contact(name, phone, email)
            manager.addContact(contact)
            print("Contact added successfully.")

        elif choice == 2:
            name = input("Enter name to search: ")
            contact = manager.searchContact(name)
            if contact:
                print("----------------------------------------")
                print(f"Contact found:\n{contact}")
                print("----------------------------------------")
            else:
                print("----------------------------------------")
                print("Contact not found.")
                print("----------------------------------------")
        

        elif choice == 3:
            name = input("Enter name to search: ")
            manager.removeContact(name)

        elif choice == 4:
            manager.displayContacts()

        elif choice == 5:
            print("----------------------------------------")
            print("Exiting...")
            print("----------------------------------------")
            break

        else:
            print("----------------------------------------")
            print("Invalid choice. Please try again.")
            print("----------------------------------------")