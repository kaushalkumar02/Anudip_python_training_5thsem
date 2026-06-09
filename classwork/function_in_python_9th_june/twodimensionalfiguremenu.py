#problem statement
#create a python program which provide the menu to the user to select two dimensional figure circle, rectangle, square, triangle after selecting the   selected figure.
#user is again asked to select the operationprovide the inputog corresponding data for the figure after input of corresponding data again provide a menu to select the operation area parameter as per the data provideby user display
  #  the result of operation this task is repeated again again until user select the option to exit that figure 
#to import the module
import math

def circle_area(r):
    return math.pi * r * r

def circle_perimeter(r):
    return 2 * math.pi * r

def rectangle_area(l, b):
    return l * b

def rectangle_perimeter(l, b):
    return 2 * (l + b)

def square_area(s):
    return s * s

def square_perimeter(s):
    return 4 * s

def triangle_area(base, height):
    return 0.5 * base * height

def triangle_perimeter(a, b, c):
    return a + b + c

while True:
    print("\n===== MENU =====")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Square")
    print("4. Triangle")
    print("5. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        r = float(input("Enter radius: "))
        while True:
            print("\n1. Area")
            print("2. Perimeter")
            print("3. Back")
            op = int(input("Enter operation: "))

            if op == 1:
                print("Area =", circle_area(r))
            elif op == 2:
                print("Perimeter =", circle_perimeter(r))
            elif op == 3:
                break
            else:
                print("Invalid Choice")

    elif ch == 2:
        l = float(input("Enter length: "))
        b = float(input("Enter breadth: "))
        while True:
            print("\n1. Area")
            print("2. Perimeter")
            print("3. Back")
            op = int(input("Enter operation: "))

            if op == 1:
                print("Area =", rectangle_area(l, b))
            elif op == 2:
                print("Perimeter =", rectangle_perimeter(l, b))
            elif op == 3:
                break
            else:
                print("Invalid Choice")

    elif ch == 3:
        s = float(input("Enter side: "))
        while True:
            print("\n1. Area")
            print("2. Perimeter")
            print("3. Back")
            op = int(input("Enter operation: "))

            if op == 1:
                print("Area =", square_area(s))
            elif op == 2:
                print("Perimeter =", square_perimeter(s))
            elif op == 3:
                break
            else:
                print("Invalid Choice")

    elif ch == 4:
        while True:
            print("\n1. Area")
            print("2. Perimeter")
            print("3. Back")
            op = int(input("Enter operation: "))

            if op == 1:
                base = float(input("Enter base: "))
                height = float(input("Enter height: "))
                print("Area =", triangle_area(base, height))

            elif op == 2:
                a = float(input("Enter side1: "))
                b = float(input("Enter side2: "))
                c = float(input("Enter side3: "))
                print("Perimeter =", triangle_perimeter(a, b, c))

            elif op == 3:
                break

            else:
                print("Invalid Choice")

    elif ch == 5:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")