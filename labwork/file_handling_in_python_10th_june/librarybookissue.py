# Problem Statement:
# A library stores book information in books.txt.
# File Format:
# B101,Python Basics,5
# B102,Java Programming,2
# B103,Data Science,0
# B104,DBMS,3
# B105,Machine Learning,1
# B106,Operating Systems,4
# B107,Networking,2
# B108,Cyber Security,6
# B109,Cloud Computing,0
# B110,Web Development,3
#
# Requirements:
# 1. Display all books.
# 2. Search a book using Book ID.
# 3. Issue a book (decrease quantity by 1).
# 4. Return a book (increase quantity by 1).
# 5. Display unavailable books.
# 6. Display books requiring restocking (copies < 2).
# 7. Update the file after every issue/return operation.
# ==========================================================

# Function to display all books
def display_books():

    file = open("books.txt", "r")

    print("\nBook Records")
    print("-" * 40)

    for line in file:
        print(line.strip())

    file.close()


# Function to search book by ID
def search_book():

    book_id = input("Enter Book ID: ")

    file = open("books.txt", "r")

    found = False

    for line in file:

        data = line.strip().split(",")

        if data[0] == book_id:

            print("\nBook Found")
            print("Book ID   :", data[0])
            print("Book Name :", data[1])
            print("Copies    :", data[2])

            found = True
            break

    if found == False:
        print("Book not found!")

    file.close()


# Function to issue a book
def issue_book():

    book_id = input("Enter Book ID to Issue: ")

    file = open("books.txt", "r")
    books = []

    for line in file:
        books.append(line.strip().split(","))

    file.close()

    found = False

    for book in books:

        if book[0] == book_id:

            if int(book[2]) > 0:
                book[2] = str(int(book[2]) - 1)
                print("Book Issued Successfully.")
            else:
                print("Book Not Available.")

            found = True
            break

    if found == False:
        print("Book not found!")

    file = open("books.txt", "w")

    for book in books:
        file.write(book[0] + "," + book[1] + "," + book[2] + "\n")

    file.close()


# Function to return a book
def return_book():

    book_id = input("Enter Book ID to Return: ")

    file = open("books.txt", "r")
    books = []

    for line in file:
        books.append(line.strip().split(","))

    file.close()

    found = False

    for book in books:

        if book[0] == book_id:

            book[2] = str(int(book[2]) + 1)

            print("Book Returned Successfully.")

            found = True
            break

    if found == False:
        print("Book not found!")

    file = open("books.txt", "w")

    for book in books:
        file.write(book[0] + "," + book[1] + "," + book[2] + "\n")

    file.close()


# Function to display unavailable books
def unavailable_books():

    file = open("books.txt", "r")

    print("\nUnavailable Books")
    print("-" * 40)

    for line in file:

        data = line.strip().split(",")

        if int(data[2]) == 0:
            print(data[0], data[1])

    file.close()


# Function to display books requiring restocking
def restocking_books():

    file = open("books.txt", "r")

    print("\nBooks Requiring Restocking")
    print("-" * 40)

    for line in file:

        data = line.strip().split(",")

        if int(data[2]) < 2:
            print(data[0], data[1], "Copies:", data[2])

    file.close()


# Main Menu
while True:

    print("\n===== Library Book Issue System =====")
    print("1. Display All Books")
    print("2. Search Book by ID")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display Unavailable Books")
    print("6. Display Books Requiring Restocking")
    print("7. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        display_books()

    elif choice == 2:
        search_book()

    elif choice == 3:
        issue_book()

    elif choice == 4:
        return_book()

    elif choice == 5:
        unavailable_books()

    elif choice == 6:
        restocking_books()

    elif choice == 7:
        print("Program Ended.")
        break

    else:
        print("Invalid Choice! Please try again.")