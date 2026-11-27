# Program to count the frequency of each word in a sentence

# Get input from user
text = input("Enter a sentence: ")

# Create an empty dictionary
word_count = {}

# Split sentence into words
words = text.split()

# Count word frequency
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Display word frequencies
print("Word Frequency:")
for word, count in word_count.items():
    print(word, ":", count)
