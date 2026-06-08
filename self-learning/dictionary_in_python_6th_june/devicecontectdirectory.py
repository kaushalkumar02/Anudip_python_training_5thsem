# --------------------------------------------------
# Problem Statement:
# Analyze a mobile contact directory and perform the following:
# 1. Display all contact names in alphabetical order.
# 2. Count the total number of contacts.
# 3. Search for a given contact name.
# 4. Create a list of contacts whose names start with a vowel.
# 5. Stop the search using break once the required
#    contact is found.
# --------------------------------------------------

# Sample Data
contacts = {
    "Amit": "9876543210",
    "Priya": "9876543211",
    "Rohan": "9876543212",
    "Neha": "9876543213",
    "Anjali": "9876543214",
    "Karan": "9876543215",
    "Pooja": "9876543216",
    "Arjun": "9876543217",
    "Sneha": "9876543218",
    "Rahul": "9876543219"
}

# --------------------------------------------------
# Validation Section
# --------------------------------------------------

is_valid = True

# Check whether contacts is a dictionary
if not isinstance(contacts, dict):
    print("Invalid data: Contacts should be stored in a dictionary.")
    is_valid = False

# Validate contact names and phone numbers
if is_valid:
    for name, number in contacts.items():

        # Name must be a string
        if not isinstance(name, str):
            print("Invalid contact name found.")
            is_valid = False
            break

        # Phone number must be a string
        if not isinstance(number, str):
            print(f"Invalid phone number for {name}.")
            is_valid = False
            break

        # Phone number must contain exactly 10 digits
        if not (number.isdigit() and len(number) == 10):
            print(f"Invalid phone number format for {name}.")
            is_valid = False
            break

# --------------------------------------------------
# Processing Section
# --------------------------------------------------

if is_valid:

    # Display names in alphabetical order
    sorted_contacts = sorted(contacts.keys())

    # Count total contacts
    total_contacts = len(contacts)

    # Search contact name
    search_name = "Neha"      # Example search

    found = False

    for name, number in contacts.items():

        if name.lower() == search_name.lower():
            found = True
            found_number = number
            break   # Stop searching once found

    # Contacts starting with a vowel
    vowel_contacts = [
        name for name in contacts
        if name[0].lower() in "aeiou"
    ]

    # --------------------------------------------------
    # Output Section
    # --------------------------------------------------

    print("Contact names in alphabetical order:")
    print(sorted_contacts)

    print("\nTotal number of contacts:")
    print(total_contacts)

    print("\nSearch Result:")
    if found:
        print(f"{search_name} found - {found_number}")
    else:
        print(f"{search_name} not found")

    print("\nContacts starting with a vowel:")
    print(vowel_contacts)