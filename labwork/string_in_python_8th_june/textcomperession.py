# Problem Statement:
# Text Compression Analyzer
# A compressed message is given: "AAABBBCCCDDDAAA"
# Tasks:
# 1. Count occurrences of each character
# 2. Create dictionary of character frequencies
# 3. Display unique characters
# 4. Find most frequent character
# 5. Create compressed output
# 6. Calculate compression ratio

text = "AAABBBCCCDDDAAA"

# 1. Character frequency dictionary
freq = {}
for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

# 2. Unique characters
unique_chars = list(freq.keys())

# 3. Most frequent character
most_frequent = max(freq, key=freq.get)

# 4. Create compressed output
compressed = ""
i = 0

while i < len(text):
    current_char = text[i]
    count = 1
    i += 1

    while i < len(text) and text[i] == current_char:
        count += 1
        i += 1

    compressed += current_char + str(count)

# 5. Lengths
original_length = len(text)
compressed_length = len(compressed)

# 6. Compression ratio
compression_ratio = ((original_length - compressed_length) / original_length) * 100

# Output
print("Original Text:", text)

print("\nCharacter Frequencies:")
for ch, count in freq.items():
    print(ch, "->", count)

print("\nUnique Characters:", unique_chars)
print("Most Frequent Character:", most_frequent)

print("Compressed Output:", compressed)
print("Original Length:", original_length)
print("Compressed Length:", compressed_length)
print("Compression Ratio: {:.2f}%".format(compression_ratio))