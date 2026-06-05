# Program: Remove all occurrences of a given number from a list

nums = []

print("Enter 20 numbers:")
for i in range(20):
    n = int(input(f"Number {i+1}: "))
    nums.append(n)

x = int(input("\nEnter number to remove from the list: "))

# Remove all occurrences
nums = [i for i in nums if i != x]

print("\nUpdated list:", nums)