# =====================================================
# PROBLEM STATEMENT:
# Create a Python program which provides a menu to the user
# to select 2D figures (Circle, Rectangle, Square, Triangle).
# After selecting figure, user selects operation (Area/Perimeter).
# Program repeats until user exits.
# =====================================================


# =====================================================
# MODULE PART (simulating geometry module)
# =====================================================

import math

# Circle
def circle_area(r):
    return math.pi * r * r

def circle_perimeter(r):
    return 2 * math.pi * r

# Square
def square_area(s):
    return s * s

def square_perimeter(s):
    return 4 * s

# Rectangle
def rectangle_area(l, b):
    return l * b

def rectangle_perimeter(l, b):
    return 2 * (l + b)

# Triangle (simple formula: equilateral assumed for simplicity)
def triangle_area(b, h):
    return 0.5 * b * h

def triangle_perimeter(a, b, c):
    return a + b + c


# =====================================================
# MAIN PROGRAM PART
# =====================================================

def get_positive_number(msg):
    while True:
        try:
            val = float(input(msg))
            if val > 0:
                return val
            else:
                print("Enter positive number only!")
        except ValueError:
            print("Invalid input! Enter number.")


while True:

    print("\n===== 2D GEOMETRY CALCULATOR =====")
    print("1. Circle")
    print("2. Square")
    print("3. Rectangle")
    print("4. Triangle")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # ---------------- CIRCLE ----------------
    if choice == '1':
        r = get_positive_number("Enter radius: ")

        while True:
            print("\n1. Area")
            print("2. Perimeter")
            print("3. Change Figure")

            op = input("Enter operation: ")

            if op == '1':
                print("Area of Circle =", round(circle_area(r), 2))

            elif op == '2':
                print("Perimeter of Circle =", round(circle_perimeter(r), 2))

            elif op == '3':
                break
            else:
                print("Invalid choice!")

            again = input("Another operation? (Y/N): ").upper()
            if again != 'Y':
                break

    # ---------------- SQUARE ----------------
    elif choice == '2':
        s = get_positive_number("Enter side: ")

        while True:
            print("\n1. Area")
            print("2. Perimeter")
            print("3. Change Figure")

            op = input("Enter operation: ")

            if op == '1':
                print("Area of Square =", square_area(s))

            elif op == '2':
                print("Perimeter of Square =", square_perimeter(s))

            elif op == '3':
                break
            else:
                print("Invalid choice!")

            again = input("Another operation? (Y/N): ").upper()
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

            op = input("Enter operation: ")

            if op == '1':
                print("Area of Rectangle =", rectangle_area(l, b))

            elif op == '2':
                print("Perimeter of Rectangle =", rectangle_perimeter(l, b))

            elif op == '3':
                break
            else:
                print("Invalid choice!")

            again = input("Another operation? (Y/N): ").upper()
            if again != 'Y':
                break

    # ---------------- TRIANGLE ----------------
    elif choice == '4':
        print("\n1. Area")
        print("2. Perimeter")

        op = input("Enter operation: ")

        if op == '1':
            b = get_positive_number("Enter base: ")
            h = get_positive_number("Enter height: ")
            print("Area of Triangle =", triangle_area(b, h))

        elif op == '2':
            a = get_positive_number("Enter side A: ")
            b = get_positive_number("Enter side B: ")
            c = get_positive_number("Enter side C: ")
            print("Perimeter of Triangle =", triangle_perimeter(a, b, c))

        else:
            print("Invalid choice!")

    # ---------------- EXIT ----------------
    elif choice == '5':
        print("Thank you for using Geometry Calculator!")
        break

    else:
        print("Invalid figure choice!"))
