'''Digital Library Plagiarism Detector 
Problem Statement 
Two research abstracts are provided as strings. 
abstract1 = "Artificial intelligence is transforming education and healthcare."
abstract2 = "Healthcare and education are rapidly transforming through artificial intelligence." 
Tasks 
1. Convert both abstracts into sets of words.  
2. Identify common words.  
3. Identify unique words in each abstract.  
4. Calculate the percentage similarity.  
5. Display whether plagiarism review is required (similarity > 50%).  
Sample Output 
Common Words: 
{'artificial', 'intelligence', 'education', 'healthcare'} 
 
Unique Words in Abstract 1: 
{'is', 'transforming', 'and'} 
 
Unique Words in Abstract 2: 
{'are', 'rapidly', 'through', 'transforming'} 
 
Similarity Percentage: 
50.0% 
 
Plagiarism Review Required: 
No'''
# Digital Library Plagiarism Detector

# Research abstracts
abstract1 = "Artificial intelligence is transforming education and healthcare."
abstract2 = "Healthcare and education are rapidly transforming through artificial intelligence."

# Function to analyze similarity
def plagiarism_detector(abs1, abs2):

    try:
        # Convert to lowercase and remove full stops
        abs1 = abs1.lower().replace(".", "")
        abs2 = abs2.lower().replace(".", "")

        # Convert abstracts into sets of words
        set1 = set(abs1.split())
        set2 = set(abs2.split())

        # Find common words
        common_words = set1.intersection(set2)

        # Find unique words
        unique_abs1 = set1.difference(set2)
        unique_abs2 = set2.difference(set1)

        # Calculate similarity percentage
        similarity = (len(common_words) /
                     len(set1.union(set2))) * 100

        # Display results
        print("Common Words:")
        print(common_words)

        print("\nUnique Words in Abstract 1:")
        print(unique_abs1)

        print("\nUnique Words in Abstract 2:")
        print(unique_abs2)

        print("\nSimilarity Percentage:")
        print(round(similarity, 1), "%", sep="")

        print("\nPlagiarism Review Required:")

        if similarity > 50:
            print("Yes")
        else:
            print("No")

    except Exception as e:
        print("Error:", e)


# Function Call
plagiarism_detector(abstract1, abstract2)