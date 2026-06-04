# Program to check whether every digit is exactly 1 greater than its previous digit

n = int(input("Enter a number: "))

t = n
a = t % 10
t = t // 10

ok = 1

while t > 0:
    b = t % 10

    if a != b + 1:
        ok = 0
        break

    a = b
    t = t // 10

if ok:
    print("Yes")
else:
    print("No")