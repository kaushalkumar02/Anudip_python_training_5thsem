# Problem Statement:
# Write a Python program using a class and object to calculate
# the area and perimeter of a rectangle with proper input validation.
class Rectangle:
    # Constructor
    def __init__(self, length, breadth):
        self.__length = length
        self.__breadth = breadth
    # Method to calculate area
    def area(self):
        return self.__length * self.__breadth
    # Method to calculate perimeter
    def perimeter(self):
        return 2 * (self.__length + self.__breadth)
    # Method to display results
    def display(self):
        print("\nRectangle Details")
        print("-----------------")
        print("Length    :", self.__length)
        print("Breadth   :", self.__breadth)
        print("Area      :", self.area())
        print("Perimeter :", self.perimeter())
# Main Program
while True:
    try:
        length = float(input("Enter the length of the rectangle: "))
        breadth = float(input("Enter the breadth of the rectangle: "))
        # Validation for positive values
        if length <= 0 or breadth <= 0:
            print("Error: Length and breadth must be greater than 0.\n")
            continue
        break
    except ValueError:
        print("Error: Please enter valid numeric values only.\n")
# Create object
rect = Rectangle(length, breadth)

# Display output
rect.display()