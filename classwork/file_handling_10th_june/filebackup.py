# Problem Statement:
# Read the contents of a source file and copy them
# into a destination file.
# Requirements:
# 1. Accept source file name from user
# 2. Accept destination file name from user
# 3. Read complete contents of source file
# 4. Write contents into destination file
# 5. Display success message
# ==========================================================

# Function to copy file
def copy_file(source_file, destination_file):

    try:
        # Open source file in read mode
        file1 = open(source_file, "r")

        # Read all contents
        data = file1.read()

        file1.close()

        # Open destination file in write mode
        file2 = open(destination_file, "w")

        # Write contents
        file2.write(data)

        file2.close()

        print("\nFile copied successfully.")
        print("All contents from", source_file,
              "have been copied to", destination_file)

    except FileNotFoundError:
        print("\nError: Source file not found!")


# Main Program
source_file = input("Enter Source File Name      : ")
destination_file = input("Enter Destination File Name : ")

copy_file(source_file, destination_file)