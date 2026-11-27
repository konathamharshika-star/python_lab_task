 Create first dictionary
dict1 = {
    "name": "John",
    "age": 18,
    "branch": "CSE"
}

# Create second dictionary
dict2 = {
    "college": "ABC College",
    "marks": 90,
    "city": "Vijayawada"
}

# Display original dictionaries
print("First Dictionary:", dict1)
print("Second Dictionary:", dict2)

# Merge two dictionaries
dict1.update(dict2)

# Display merged dictionary
print("Merged Dictionary:", dict1)
