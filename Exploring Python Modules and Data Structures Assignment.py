#Task 1:


from datetime import datetime

# Contact management functions
contacts = []

def add_contact(name, phone):
    contact = {"name": name, "phone": phone}
    contacts.append(contact)
    return f"Contact {name} added."

def remove_contact(name):
    global contacts
    contacts = [contact for contact in contacts if contact["name"] != name]
    return f"Contact {name} removed."

def display_contacts():
    if not contacts:
        return "No contacts found."
    contact_list = "\n".join([f"Name: {contact['name']}, Phone: {contact['phone']}" for contact in contacts])
    return contact_list

# Main program logic
def main():
    while True:
        print("\nContact List Manager")
        print("1. Add Contact")
        print("2. Remove Contact")
        print("3. Display Contacts")
        print("4. Display Current Month and Year")
        print("5. Convert Date String to Datetime Object")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter contact phone: ")
            print(add_contact(name, phone))
        elif choice == '2':
            name = input("Enter contact name to remove: ")
            print(remove_contact(name))
        elif choice == '3':
            print(display_contacts())
        elif choice == '4':
            now = datetime.now()
            print(f"Current month and year: {now.strftime('%B %Y')}")
        elif choice == '5':
            date_str = input("Enter a date (YYYY-MM-DD): ")
            try:
                date_obj = datetime.strptime(date_str, "%Y-%m-%d")
                print(f"Converted date: {date_obj}")
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
