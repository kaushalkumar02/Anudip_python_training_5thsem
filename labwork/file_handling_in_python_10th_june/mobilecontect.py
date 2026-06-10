# Problem Statement:
# Contacts are stored in contacts.txt.
# File Format:
# Anuj,9876543210
# Rahul,9876543211
# Priya,9876543212
# Neha,9876543213
# Amit,9876543214
# Sneha,9876543215
# Karan,9876543216
# Pooja,9876543217
# Rohit,9876543218
# Anjali,9876543219
#
# Requirements:
# 1. Display all contacts.
# 2. Search a contact by name.
# 3. Add a new contact.
# 4. Update an existing contact number.
# 5. Delete a contact.
# 6. Display contacts whose names start with a vowel.
# 7. Save all modifications back to the file.
# ==========================================================

# Function to display all contacts
def display_contacts():

    file = open("contacts.txt", "r")

    print("\nContact List")
    print("-" * 30)

    for line in file:
        print(line.strip())

    file.close()


# Function to search contact
def search_contact():

    name = input("Enter Contact Name: ")

    file = open("contacts.txt", "r")

    found = False

    for line in file:

        data = line.strip().split(",")

        if data[0].lower() == name.lower():

            print("\nContact Found")
            print("Name   :", data[0])
            print("Number :", data[1])

            found = True
            break

    if found == False:
        print("Contact not found!")

    file.close()


# Function to add contact
def add_contact():

    name = input("Enter Name: ")
    number = input("Enter Mobile Number: ")

    file = open("contacts.txt", "a")

    file.write("\n" + name + "," + number)

    file.close()

    print("Contact Added Successfully.")


# Function to update contact
def update_contact():

    name = input("Enter Contact Name: ")

    file = open("contacts.txt", "r")

    contacts = []

    for line in file:
        contacts.append(line.strip().split(","))

    file.close()

    found = False

    for contact in contacts:

        if contact[0].lower() == name.lower():

            new_number = input("Enter New Mobile Number: ")

            contact[1] = new_number

            found = True

            print("Contact Updated Successfully.")
            break

    if found == False:
        print("Contact not found!")

    file = open("contacts.txt", "w")

    for contact in contacts:
        file.write(contact[0] + "," + contact[1] + "\n")

    file.close()


# Function to delete contact
def delete_contact():

    name = input("Enter Contact Name to Delete: ")

    file = open("contacts.txt", "r")

    contacts = []

    for line in file:

        data = line.strip().split(",")

        if data[0].lower() != name.lower():
            contacts.append(data)

    file.close()

    file = open("contacts.txt", "w")

    for contact in contacts:
        file.write(contact[0] + "," + contact[1] + "\n")

    file.close()

    print("Contact Deleted Successfully.")


# Function to display names starting with vowel
def vowel_contacts():

    file = open("contacts.txt", "r")

    print("\nContacts Starting With Vowel")
    print("-" * 35)

    for line in file:

        data = line.strip().split(",")

        if data[0][0].lower() in "aeiou":
            print(data[0], data[1])

    file.close()


# Main Menu
while True:

    print("\n===== Mobile Contact Directory System =====")
    print("1. Display All Contacts")
    print("2. Search Contact")
    print("3. Add New Contact")
    print("4. Update Contact Number")
    print("5. Delete Contact")
    print("6. Display Contacts Starting With Vowel")
    print("7. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        display_contacts()

    elif choice == 2:
        search_contact()

    elif choice == 3:
        add_contact()

    elif choice == 4:
        update_contact()

    elif choice == 5:
        delete_contact()

    elif choice == 6:
        vowel_contacts()

    elif choice == 7:
        print("Program Ended.")
        break

    else:
        print("Invalid Choice!")