base = float(input("Enter Base : "))
height = float(input("Enter Height : "))

side1 = float(input("Enter Side 1 : "))
side2 = float(input("Enter Side 2 : "))
side3 = float(input("Enter Side 3 : "))

# Validation for Base
if base > 0:
    print("# Base Valid")
else:
    print("# Base Invalid")

# Validation for Height
if height > 0:
    print("# Height Valid")
else:
    print("# Height Invalid")

# Validation for Side 1
if side1 > 0:
    print("# Side 1 Valid")
else:
    print("# Side 1 Invalid")

# Validation for Side 2
if side2 > 0:
    print("# Side 2 Valid")
else:
    print("# Side 2 Invalid")

# Validation for Side 3
if side3 > 0:
    print("# Side 3 Valid")
else:
    print("# Side 3 Invalid")

if base > 0 and height > 0 and side1 > 0 and side2 > 0 and side3 > 0:

    area = 0.5 * base * height
    print("# Area Calculated")
    print("Area =", area)

    perimeter = side1 + side2 + side3
    print("# Perimeter Calculated")
    print("Perimeter =", perimeter)

else:
    print("# Invalid Input")