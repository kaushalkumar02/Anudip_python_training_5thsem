# Program: Remove all occurrences of a given number from a list

numbers = []

print("Enter any 20 numbers : ")
for _ in range(20):
    numbers.append(int(input()))

element = int(input("Enter number to remove duplicates: "))

frequency = numbers.count(element)

if frequency == 0:
    print("element not found")

elif frequency == 1:
    print("no duplicates found")

else:
    numbers.reverse()

    removed = 0
    for i in range(len(numbers)):
        if numbers[i] == element and removed < frequency - 1:
            numbers[i] = None
            removed += 1

    numbers = [x for x in numbers if x is not None]
    numbers.reverse()

    print("After removing duplicates")
    print(numbers)