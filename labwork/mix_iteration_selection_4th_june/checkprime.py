# Check prime or not and print all factors

n = int(input("Enter a Number: "))

i = 1
count = 0

print("Factors:", end=" ")

while i <= n:
    if n % i == 0:
        print(i, end=" ")
        count = count + 1
    i = i + 1

print()

if count == 2:
    print(n, "is a Prime Number")
else:
    print(n, "is not a Prime Number")