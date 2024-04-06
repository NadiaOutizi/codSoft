class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contact_list(self):
        if self.contacts:
            print("Contact List:")
            for index, contact in enumerate(self.contacts, start=1):
                print(f"{index}. Name: {contact.name}, Phone: {contact.phone_number},Address :{contact.address}")
        else:
            print("No contacts found.")

    def search_contact(self, search_term):
        found_contacts = []
        for contact in self.contacts:
            if (search_term.lower() in contact.name.lower()) or (search_term in contact.phone_number):
                found_contacts.append(contact)
        if found_contacts:
            print("Search Results:")
            for index, contact in enumerate(found_contacts, start=1):
                print(f"{index}. Name: {contact.name}, Phone: {contact.phone_number}")
        else:
            print("No contacts found.")

    def update_contact(self, index, updated_contact):
        old_contact = self.contacts[index]
        if updated_contact.name:
            old_contact.name = updated_contact.name
        if updated_contact.phone_number:
            old_contact.phone_number = updated_contact.phone_number
        if updated_contact.email:
            old_contact.email = updated_contact.email
        if updated_contact.address:
            old_contact.address = updated_contact.address

    def delete_contact(self, index):
        del self.contacts[index]

def main():
    contact_manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Quit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            new_contact = Contact(name, phone_number, email, address)
            contact_manager.add_contact(new_contact)
            print("Contact added successfully.")
        elif choice == '2':
            contact_manager.view_contact_list()
        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            contact_manager.search_contact(search_term)
        elif choice == '4':
            index = int(input("Enter index of contact to update: ")) - 1
            updated_name = input("Enter updated name (leave empty to keep the same): ")
            updated_phone_number = input("Enter updated phone number (leave empty to keep the same): ")
            updated_email = input("Enter updated email (leave empty to keep the same): ")
            updated_address = input("Enter updated address (leave empty to keep the same): ")
            updated_contact = Contact(updated_name, updated_phone_number, updated_email, updated_address)
            contact_manager.update_contact(index, updated_contact)
            print("Contact updated successfully.")
        elif choice == '5':
            index = int(input("Enter index of contact to delete: ")) - 1
            contact_manager.delete_contact(index)
            print("Contact deleted successfully.")
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
