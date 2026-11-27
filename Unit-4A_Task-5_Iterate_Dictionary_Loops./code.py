 Create a dictionary
student = {
    "name": "John",
    "age": 18,
    "branch": "CSE",
    "marks": 85
}

# Display dictionary
print("Student Dictionary:", student)

# Iterate through keys
print("\nDictionary Keys:")
for key in student:
    print(key)

# Iterate through values
print("\nDictionary Values:")
for value in student.values():
    print(value)

# Iterate through key-value pairs
print("\nDictionary Items:")
for key, value in student.items():
    print(key, ":", value)
