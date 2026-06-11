# Problem Statement:
# Design a Python program to calculate the area of a triangle using Heron's Formula.
# The program should accept the lengths of three sides from the user and display the area.
# The program must handle the following exceptional situations gracefully:
# 1. If the user enters a non-numeric value, display an appropriate error message.
# 2. If any side is zero or negative, inform the user that triangle sides must be greater than zero.
# 3. If the three sides cannot form a valid triangle according to Triangle Inequality Theorem,
#    notify the user that the triangle is invalid.
# 4. Ensure the program does not terminate abruptly due to invalid input.
# 5. Always display a message that the triangle area calculation process has been completed.

# Note:
# Heron's Formula:
# s = (a + b + c) / 2
# Area = √(s(s-a)(s-b)(s-c))

import math   # Import math module for square root function

try:
    # Step 1: Take input from user
    a = float(input("Enter side a: "))
    b = float(input("Enter side b: "))
    c = float(input("Enter side c: "))

    # Step 2: Check for zero or negative values
    if a <= 0 or b <= 0 or c <= 0:
        print("Error: Triangle sides must be greater than zero.")

    # Step 3: Check triangle validity using Triangle Inequality Theorem
    elif (a + b <= c) or (a + c <= b) or (b + c <= a):
        print("Error: The given sides do not form a valid triangle.")

    else:
        # Step 4: Calculate semi-perimeter
        s = (a + b + c) / 2

        # Step 5: Apply Heron's formula
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))

        # Step 6: Display result
        print("Area of triangle =", area)

except ValueError:
    # Handles non-numeric input
    print("Error: Please enter numeric values only.")

finally:
    # Step 7: Always executed
    print("Triangle area calculation process completed.")