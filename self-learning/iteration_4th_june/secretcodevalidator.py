# Program to check whether a 6-digit secret code is valid or not

n = input("Enter 6-digit code: ")

if len(n) != 6 or not n.isdigit():
    print("Invalid Code")
else:
    s1 = int(n[0]) + int(n[1]) + int(n[2])
    s2 = int(n[3]) + int(n[4]) + int(n[5])

    if s1 == s2:
        print("Valid Code")
    else:
        print("Invalid Code")