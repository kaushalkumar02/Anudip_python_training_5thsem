'''Social Media Trend Analyzer 
Problem Statement 
Trending hashtags collected during an event are stored in a file named hashtags.txt. 
#AI 
#Python 
#AI 
#MachineLearning 
#DataScience 
#Python 
#AI 
#Coding 
#DataScience 
#Python 
Tasks 
1. Count occurrences of each hashtag.  
2. Display the top trending hashtag.  
3. Create a set of unique hashtags.  
4. Identify hashtags used more than twice.  
5. Generate a trend report file.  
Sample Output 
Hashtag Frequency: 
#AI : 3 
#Python : 3 
#MachineLearning : 1 
#DataScience : 2 
#Coding : 1 
 
Top Trending Hashtags: 
#AI 
#Python 
 
Unique Hashtags: 
{'#AI', '#Python', '#MachineLearning', '#DataScience', '#Coding'} 
 
Hashtags Used More Than Twice: 
#AI 
#Python 
 
Trend Report Generated Successfully.'''

# Social Media Trend Analyzer

# Function to analyze hashtags
def analyze_hashtags():

    try:
        # Open the file
        file = open("hashtags.txt", "r")

        # Read all hashtags
        hashtags = file.readlines()

        file.close()

        # Dictionary to store hashtag frequencies
        hashtag_freq = {}

        # Set to store unique hashtags
        unique_hashtags = set()

        # Count occurrences
        for tag in hashtags:

            tag = tag.strip()

            # Skip empty lines
            if tag == "":
                continue

            unique_hashtags.add(tag)

            if tag in hashtag_freq:
                hashtag_freq[tag] += 1
            else:
                hashtag_freq[tag] = 1

        # Display frequencies
        print("Hashtag Frequency:")

        for tag in hashtag_freq:
            print(tag, ":", hashtag_freq[tag])

        # Find highest frequency
        max_count = max(hashtag_freq.values())

        print("\nTop Trending Hashtags:")

        top_hashtags = []

        for tag in hashtag_freq:
            if hashtag_freq[tag] == max_count:
                top_hashtags.append(tag)
                print(tag)

        # Display unique hashtags
        print("\nUnique Hashtags:")
        print(unique_hashtags)

        # Hashtags used more than twice
        print("\nHashtags Used More Than Twice:")

        popular_tags = []

        for tag in hashtag_freq:

            if hashtag_freq[tag] > 2:
                popular_tags.append(tag)
                print(tag)

        if len(popular_tags) == 0:
            print("None")

        # Generate trend report file
        try:
            report = open("trend_report.txt", "w")

            report.write("Social Media Trend Report\n")
            report.write("-------------------------\n\n")

            report.write("Hashtag Frequency:\n")

            for tag in hashtag_freq:
                report.write(tag + " : " +
                             str(hashtag_freq[tag]) + "\n")

            report.write("\nTop Trending Hashtags:\n")

            for tag in top_hashtags:
                report.write(tag + "\n")

            report.close()

            print("\nTrend Report Generated Successfully.")

        except PermissionError:
            print("Permission denied while creating report file.")

        except Exception as e:
            print("File Writing Error:", e)

    except FileNotFoundError:
        print("Error: hashtags.txt file not found.")

    except PermissionError:
        print("Error: Permission denied while accessing file.")

    except Exception as e:
        print("Unexpected Error:", e)


# Function Call
analyze_hashtags()