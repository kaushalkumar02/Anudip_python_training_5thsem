import math

# -------- FUNCTIONS --------

def circle_area(r):
    return math.pi * r * r

def circle_perimeter(r):
    return 2 * math.pi * r

def square_area(s):
    return s * s

def square_perimeter(s):
    return 4 * s

def rectangle_area(l, b):
    return l * b

def rectangle_perimeter(l, b):
    return 2 * (l + b)

# -------- MAIN PROGRAM --------

while True:
    print("\n===== FIGURE MENU =====")
    print("1. Circle")
    print("2. Square")
    print("3. Rectangle")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        r = float(input("Enter radius: "))

        while True:
            print("\n1. Area")
            print("2. Perimeter")
            print("3. Back")

            op = int(input("Enter operation: "))

            if op == 1:
                print("Area of Circle =", circle_area(r))
            elif op == 2:
                print("Perimeter of Circle =", circle_perimeter(r))
            elif op == 3:
                break
            else:
                print("Invalid choice")

    elif choice == 2:
        s = float(input("Enter side: "))

        while True:
            print("\n1. Area")
            print("2. Perimeter")
            print("3. Back")

            op = int(input("Enter operation: "))

            if op == 1:
                print("Area of Square =", square_area(s))
            elif op == 2:
                print("Perimeter of Square =", square_perimeter(s))
            elif op == 3:
                break
            else:
                print("Invalid choice")

    elif choice == 3:
        l = float(input("Enter length: "))
        b = float(input("Enter breadth: "))

        while True:
            print("\n1. Area")
            print("2. Perimeter")
            print("3. Back")

            op = int(input("Enter operation: "))

            if op == 1:
                print("Area of Rectangle =", rectangle_area(l, b))
            elif op == 2:
                print("Perimeter of Rectangle =", rectangle_perimeter(l, b))
            elif op == 3:
                break
            else:
                print("Invalid choice")

    elif choice == 4:
        print("Program Ended")
        break

    else:
        print("Invalid choice")