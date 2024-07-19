#final contact book code

#2nd code
import os

# Function to add a contact
def add(name, ph):
    contact[name] = ph
    save()

# Function to view all contacts
def view():
    if len(contact) == 0:
        print("Contact book is empty.")
    else:
        print("Contact Book:")
        for name, ph in contact.items():
            print(f"{name}: {ph}")

# Function to search for a contact
def search(name):
    if name in contact:
        print(f"Name: {name}, Phone Number: {contact[name]}")
    else:
        print(f"{name} not found in contacts.")

# Function to delete a contact
def delete(name):
    if name in contact:
        del contact[name]
        print(f"{name} has been deleted from contacts.")
        save()
    else:
        print(f"{name} not found in contacts.")

# Function to save contacts to a file
def save():
    with open("contacts.txt", "w") as file:
        for name, ph in contact.items():
            file.write(f"{name},{ph}\n")

# Function to load contacts from file
def load():
    global contact
    contact = {}
    if os.path.exists("contacts.txt"):
        with open("contacts.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                if line.strip():
                    name, ph = line.strip().split(',')
                    contact[name] = ph

# Main program loop
contact = {}
load()

while True:
    print("\nContact Book Menu:")
    print("1. Add  new contact")
    print("2. View all contacts")
    print("3. Search contact")
    print("4. Delete contact")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        name = input("Enter contact name: ")
        ph = input("Enter contact phone number: ")
        add(name, ph)
    elif choice == '2':
        view()
    elif choice == '3':
        name = input("Enter name to search: ")
        search(name)
    elif choice == '4':
        name = input("Enter name to delete: ")
        delete(name)
    elif choice == '5':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")