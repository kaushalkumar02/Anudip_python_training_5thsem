# Program to find the length of the longest continuous increasing sequence

n = int(input("Enter how many numbers: "))

mx = 1
cnt = 1

prev = int(input())

for i in range(n - 1):
    cur = int(input())

    if cur > prev:
        cnt += 1
    else:
        cnt = 1

    if cnt > mx:
        mx = cnt

    prev = cur

print("Length =", mx)