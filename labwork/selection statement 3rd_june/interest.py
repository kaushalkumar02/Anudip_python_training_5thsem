p = float(input("Enter Principal : "))
r = float(input("Enter Rate : "))
t = float(input("Enter Time : "))

# validation principal
if p > 0:
    print("# Principal is valid")
else:
    print("# Principal is invalid")

# validation rate
if r > 0:
    print("# Rate is valid")
else:
    print("# Rate is invalid")

# validation time
if t > 0:
    print("# Time is valid")
else:
    print("# Time is invalid")

# calculation
if p > 0 and r > 0 and t > 0:
    si = (p * r * t) / 100
    print("# Simple Interest calculated")
    print("Simple Interest =", si)
else:
    print("# calculation not possible due to invalid input")