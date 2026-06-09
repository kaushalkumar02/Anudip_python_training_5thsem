a = float(input("Enter Side 1 : "))
b = float(input("Enter Side 2 : "))
c = float(input("Enter Side 3 : "))

# validation side 1
if a > 0:
    print("# Side 1 valid")
else:
    print("# Side 1 invalid")

# validation side 2
if b > 0:
    print("# Side 2 valid")
else:
    print("# Side 2 invalid")

# validation side 3
if c > 0:
    print("# Side 3 valid")
else:
    print("# Side 3 invalid")

if a > 0 and b > 0 and c > 0:

    # check triangle
    if (a + b > c) and (a + c > b) and (b + c > a):
        print("# Triangle is valid")

        # type of triangle
        if a == b and b == c:
            print("Equilateral Triangle")
        elif a == b or b == c or a == c:
            print("Isosceles Triangle")
        else:
            print("Scalene Triangle")

    else:
        print("# Not a Triangle")
else:
    print("# Invalid Input")