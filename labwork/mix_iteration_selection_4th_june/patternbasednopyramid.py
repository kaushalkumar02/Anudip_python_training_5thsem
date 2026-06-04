n = int(input("Enter Number of Rows: "))

# forward pattern
i = 1
while i <= n:
    j = 1
    while j <= i:
        print(j, end="")
        j = j + 1
    print()
    i = i + 1

print()

# reverse pattern
i = n
while i >= 1:
    j = 1
    while j <= i:
        print(j, end="")
        j = j + 1
    print()
    i = i - 1