'''A company wants to maintain backups of important documents. Create a program to copy the contents of 
one file into another. 
Sample Input/Data 
Source File (notes.txt) 
Python supports file handling. 
Functions improve code reusability. 
Dictionaries store data in key-value pairs. 
Tasks 
1. Read the contents of the source file.  
2. Copy the entire content to another file named backup.txt.  
3. Display a success message.  
4. Verify whether both files contain the same number of lines.  
Sample Output 
File copied successfully. 
 
Source File Lines: 3 
 
Backup File Lines: 3 
 
Verification Status: Successful'''

# File Copy Utility

# --------------------------------------------------
# Task 1: Read the contents of the source file
# --------------------------------------------------

# Open source file in read mode
source_file = open("notes.txt", "r")

# Read complete content from source file
content = source_file.read()

# Close source file
source_file.close()

# --------------------------------------------------
# Task 2: Copy the content to backup.txt
# --------------------------------------------------

# Open backup file in write mode
backup_file = open("backup.txt", "w")

# Write content into backup file
backup_file.write(content)

# Close backup file
backup_file.close()

# Display success message
print("File copied successfully.")

# --------------------------------------------------
# Task 3: Verify whether both files contain
# the same number of lines
# --------------------------------------------------

# Open source file again to count lines
source_file = open("notes.txt", "r")
source_lines = source_file.readlines()
source_file.close()

# Open backup file to count lines
backup_file = open("backup.txt", "r")
backup_lines = backup_file.readlines()
backup_file.close()

# Count lines in both files
source_count = len(source_lines)
backup_count = len(backup_lines)

print("\nSource File Lines:", source_count)
print("\nBackup File Lines:", backup_count)

# Verify the copy operation
if source_count == backup_count:
    print("\nVerification Status: Successful")
else:
    print("\nVerification Status: Failed")