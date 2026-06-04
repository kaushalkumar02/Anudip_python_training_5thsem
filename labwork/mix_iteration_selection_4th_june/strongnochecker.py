# Strong Number Checker
# Sum of factorial of digits = number

n = int(input("Enter a Number: "))

temp = n
total = 0

while temp > 0:
    digit = temp % 10

    fact = 1
    i = 1
    while i <= digit:
        fact = fact * i
        i = i + 1

    total = total + fact
    temp = temp // 10

if total == n:
    print(n, "is a Strong Number")
else:
    print(n, "is not a Strong Number")