class ContactManager:
    def __init__(self):
        self.contacts = []
    
    def addContact(self, contact):
        self.contacts.append(contact)


    def removeContact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print("----------------------------------------")
                print(f"Contact '{name}' removed successfully.")
                print("----------------------------------------")
                return
        print("----------------------------------------")    
        print(f"Contact '{name}' not found.")
        print("----------------------------------------")



    def searchContact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        
        return None
    


    def displayContacts(self):
        if len(self.contacts) == 0:
            print("----------------------------------------")
            print("No contacts found.")
            print("----------------------------------------")
        else:
            print("----------------------------------------")
            for contact in self.contacts:
                print(contact)
                print("----------------------------------------")