angle1 = int(input("Enter Angle 1 : "))
angle2 = int(input("Enter Angle 2 : "))
angle3 = int(input("Enter Angle 3 : "))

if angle1 > 0:
    print("Angle 1 is Valid")
else:
    print("Angle 1 is Invalid")

if angle2 > 0:
    print("Angle 2 is Valid")
else:
    print("Angle 2 is Invalid")

if angle3 > 0:
    print("Angle 3 is Valid")
else:
    print("Angle 3 is Invalid")

if angle1 > 0 and angle2 > 0 and angle3 > 0:
    total = angle1 + angle2 + angle3
    print("Sum of Angles =", total)

    if total == 180:
        print("Triangle is Valid")
    else:
        print("Triangle is Invalid")
else:
    print("Triangle is Invalid")