num = 7
guess = 0

while guess != num:
    guess = int(input("Guess the Number: "))

    if guess != num:
        print("Wrong Guess. Try Again.")

print("guess correct number.")