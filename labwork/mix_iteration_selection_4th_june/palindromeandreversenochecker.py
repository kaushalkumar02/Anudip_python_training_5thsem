# Palindrome Number Checker

n = int(input("Enter a Number: "))

temp = n
rev = 0

while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp = temp // 10

print("Reverse:", rev)

if rev == n:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")