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

# check triangle or not
if a > 0 and b > 0 and c > 0:

    if (a + b > c) and (a + c > b) and (b + c > a):
        print("# Triangle is valid")
    else:
        print("# Triangle is not valid")
else:
    print("# Invalid input")