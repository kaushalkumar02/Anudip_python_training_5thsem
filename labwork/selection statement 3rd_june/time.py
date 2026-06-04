seconds = int(input("Enter Seconds : "))

if seconds >= 0:
    print("Valid Seconds")

    hours = seconds // 3600
    print("Hours =", hours)

    minutes = (seconds % 3600) // 60
    print("Minutes =", minutes)

    second = seconds % 60
    print("Seconds =", second)

else:
    print("Invalid Seconds")