# Problem Statement:
# Books available in a library are stored as a list of tuples.
# Each tuple contains the book name and number of copies available.
# Write a program to:
# • Display unavailable books (0 copies)
# • Find all books with more than 2 copies
# • Count available books (copies > 0)
# • Stop searching once a requested book is found
# Library book data (book name, number of copies)
books = [
    ("Python Basics", 5),
    ("Data Science", 0),
    ("Java Programming", 3),
    ("Machine Learning", 0)
]

# Display books that are not available (0 copies)
print("Unavailable Books:")
for book, copies in books:
    if copies == 0:   # check if book is unavailable
        print("-", book)

print()
# Display books having more than 2 copies
print("Books with more than 2 copies:")
for book, copies in books:
    if copies > 2:    # check availability greater than 2
        print("-", book)
print()
# Count total available books (copies > 0)
count = 0
for book, copies in books:
    if copies > 0:    # book is available
        count += 1    # increase counter
print("Total available books:", count)
print()
# Search for a book and stop when found
search_book = input("Enter book name to search: ")
found = False
# loop through each book
for book, copies in books:
    if book.lower() == search_book.lower():  # match ignoring case
        print("Book Found:", book, "-", copies, "copies")
        found = True
        break   # stop loop immediately once book is found

# if book not found
if not found:
    print("Book not found in library.")