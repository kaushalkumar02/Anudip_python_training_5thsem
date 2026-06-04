# Program to check whether a number is a Mountain Number

n = input("Enter a number: ")

up = False
down = False

for i in range(1, len(n)):
    if n[i] > n[i-1] and not down:
        up = True
    elif n[i] < n[i-1]:
        if up:
            down = True
    else:
        print("Not a Mountain Number")
        break
else:
    if up and down:
        print("Mountain Number")
    else:
        print("Not a Mountain Number")