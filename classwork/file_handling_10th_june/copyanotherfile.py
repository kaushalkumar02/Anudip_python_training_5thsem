# ==========================================================
# Program:
# Copy entire content from one file into another file
# ==========================================================
# Function to copy file content
def copy_file():

    source_file = input("Enter Source File Name      : ")
    destination_file = input("Enter Destination File Name : ")

    try:
        # Open source file in read mode
        file1 = open(source_file, "r")

        # Read complete content
        data = file1.read()

        file1.close()

        # Open destination file in write mode
        file2 = open(destination_file, "w")

        # Write content into destination file
        file2.write(data)

        file2.close()

        print("\nFile copied successfully.")
        print("All contents from", source_file,
              "have been copied to", destination_file)

    except FileNotFoundError:
        print("\nError: Source file not found!")

# Function Call
copy_file()