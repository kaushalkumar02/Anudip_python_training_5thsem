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
    if ch in freq:
        freq[ch] = freq[ch] + 1
    else:
        freq[ch] = 1

# 2. Unique characters
unique_chars = []

for ch in text:
    if ch not in unique_chars:
        unique_chars.append(ch)

# 3. Most frequent character
max_char = ""
max_count = 0

for ch in freq:
    if freq[ch] > max_count:
        max_count = freq[ch]
        max_char = ch

# 4. Create compressed output
compressed = ""

for ch in freq:
    compressed = compressed + ch + str(freq[ch])

# 5. Original length
original_length = len(text)

# 6. Compressed length
compressed_length = len(compressed)

# 7. Compression ratio
compression_ratio = original_length / compressed_length

# OUTPUT
print("Text:", text)
print("Frequency Dictionary:", freq)
print("Unique Characters:", unique_chars)
print("Most Frequent Character:", max_char)
print("Compressed Output:", compressed)
print("Original Length:", original_length)
print("Compressed Length:", compressed_length)
print("Compression Ratio:", compression_ratio).format(compression_ratio))
