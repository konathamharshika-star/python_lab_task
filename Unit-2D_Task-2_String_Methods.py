# String Methods

text = "  Hello Python Programming  "

# Upper
print("Upper:", text.upper())

# Lower
print("Lower:", text.lower())

# Strip
print("Strip:", text.strip())

# Split
words = text.split()
print("Split:", words)

# Join
result = "-".join(words)
print("Join:", result)

# Replace
result = text.replace("Python", "Java")
print("Replace:", result)
# Find
result = text.find("Python")
print("Find:", result)