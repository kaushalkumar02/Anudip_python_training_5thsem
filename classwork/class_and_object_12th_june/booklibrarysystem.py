#5. Book Library System (Intermediate)
#  Problem Statement:
#  Create a Book class with attributes: 
# • Book ID 
#  • Title  
# • Author 
#  • Availability Status
#   Implement methods to: 
# • Issue a book.
#   • Return a book.
#   • Display book details. 
#  Prevent issuing a book that is already issued
# . Sample Output:
#  Book Issued Successfully. 
# Availability Status: Not Available 
# ---------------------------------------------------------
#create a book class with attributes
# ---------------------------------------------------------
# Problem Statement:
# Create a Book class with attributes:
# • Book ID
# • Title
# • Author
# • Availability Status
#
# Implement methods to:
# • Issue a book.
# • Return a book.
# • Display book details.
#
# Prevent issuing a book that is already issued.
#
# Sample Output:
# Book Issued Successfully.
# Availability Status: Not Available


# Book Class
class Book:
    # Constructor
    # -------------------------------------------------------------
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True

    # Method to issue a book
    # -----------------------------------------------------------------
    def issue_book(self):
        if self.available:
            self.available = False
            print("Book Issued Successfully.")
        else:
            print("Book is already issued.")

    # Method to return a book
    # -------------------------------------------------------------------
    def return_book(self):
        if not self.available:
            self.available = True
            print("Book Returned Successfully.")
        else:
            print("Book is already available in the library.")

    # Method to display book details
    # --------------------------------------------------------------------
    def display_details(self):
        print("\nBook Details")
        print("-" * 30)
        print("Book ID            :", self.book_id)
        print("Title              :", self.title)
        print("Author             :", self.author)

        if self.available:
            print("Availability Status: Available")
        else:
            print("Availability Status: Not Available")


# Main Program
# ------------------------------------------------------------------------
# Accept Book Details
book_id = input("Enter Book ID: ")
title = input("Enter Book Title: ")
author = input("Enter Author Name: ")
#------------------------------------------------------
# Create Book Object
book = Book(book_id, title, author)
#----------------------------------------------------
# Display Initial Details
book.display_details()
#----------------------------------------------------
# Issue the Book
print("\nIssuing Book...")
book.issue_book()
#----------------------------------------------------------
# Display Updated Details
book.display_details()
#-----------------------------------------------------
# Try Issuing Again
print("\nIssuing Book Again...")
book.issue_book()
#------------------------------------------------------
# Return the Book
print("\nReturning Book...")
book.return_book()
#----------------------------------------------------
# Display Final Details
book.display_details()