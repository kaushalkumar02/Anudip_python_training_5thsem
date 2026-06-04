# Program to check whether a number is a Mirror Number or not

n = input("Enter number: ")

if len(n) % 2 != 0:
    print("Not a Mirror Number")
else:
    mid = len(n) // 2

    left = n[:mid]
    right = n[mid:]

    if left == right:
        print("Mirror Number")
    else:
        print("Not a Mirror Number")