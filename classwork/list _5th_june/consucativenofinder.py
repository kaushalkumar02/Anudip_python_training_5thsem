# Problem Statement:
# Find all consecutive number pairs from a given list and store them in a new list.

numbers = [4, 5, 6, 10, 11, 15, 16, 17]

pairs = []  # to store consecutive pairs

# check each number with next number
for i in range(len(numbers) - 1):

    # if difference is 1, they are consecutive
    if numbers[i] + 1 == numbers[i + 1]:
        print(numbers[i], "and", numbers[i + 1], "are consecutive")

        # store pair in tuple format
        pairs.append((numbers[i], numbers[i + 1]))

# display final list of pairs
print("Consecutive Pairs List:", pairs)