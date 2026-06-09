# =====================================================
# PROBLEM STATEMENT:
# 2D Geometry Calculator Using Python Modules
# This program calculates Area and Perimeter of
# Circle, Square, and Rectangle using functions.
# =====================================================


# =====================================================
# MODULE PART (geometry.py equivalent)
# =====================================================

import math

# Circle Functions
def circle_area(r):
    return math.pi * r * r

def circle_perimeter(r):
    return 2 * math.pi * r

# Square Functions
def square_area(s):
    return s * s

def square_perimeter(s):
    return 4 * s

# Rectangle Functions
def rectangle_area(l, b):
    return l * b

def rectangle_perimeter(l, b):
    return 2 * (l + b)


# =====================================================
# MAIN PROGRAM PART (main.py equivalent)
# =====================================================

def get_positive_number(msg):
    while True:
        try:
            value = float(input(msg))
            if value > 0:
                return value
            else:
                print("Enter positive number only.")
        except ValueError:
            print("Invalid input! Enter numeric value.")


while True:

    print("\n===== 2D GEOMETRY CALCULATOR =====")
    print("1. Circle")
    print("2. Square")
    print("3. Rectangle")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # ---------------- CIRCLE ----------------
    if choice == '1':
        r = get_positive_number("Enter radius: ")

        while True:
            print("\n1. Area")
            print("2. Perimeter")
            print("3. Change Figure")

            op = input("Enter choice: ")

            if op == '1':
                print("Area of Circle =", round(circle_area(r), 2))

            elif op == '2':
                print("Perimeter of Circle =", round(circle_perimeter(r), 2))

            elif op == '3':
                break
            else:
                print("Invalid choice!")

            again = input("Do another operation? (Y/N): ").upper()
            if again != 'Y':
                break

    # ---------------- SQUARE ----------------
    elif choice == '2':
        s = get_positive_number("Enter side: ")

        while True:
            print("\n1. Area")
            print("2. Perimeter")
            print("3. Change Figure")

            op = input("Enter choice: ")

            if op == '1':
                print("Area of Square =", square_area(s))

            elif op == '2':
                print("Perimeter of Square =", square_perimeter(s))

            elif op == '3':
                break
            else:
                print("Invalid choice!")

            again = input("Do another operation? (Y/N): ").upper()
            if again != 'Y':
                break

    # ---------------- RECTANGLE ----------------
    elif choice == '3':
        l = get_positive_number("Enter length: ")
        b = get_positive_number("Enter breadth: ")

        while True:
            print("\n1. Area")
            print("2. Perimeter")
            print("3. Change Figure")

            op = input("Enter choice: ")

            if op == '1':
                print("Area of Rectangle =", rectangle_area(l, b))

            elif op == '2':
                print("Perimeter of Rectangle =", rectangle_perimeter(l, b))

            elif op == '3':
                break
            else:
                print("Invalid choice!")

            again = input("Do another operation? (Y/N): ").upper()
            if again != 'Y':
                break

    elif choice == '4':
        print("Thank you! Goodbye.")
        break

    else:
        print("Invalid figure choice!")
