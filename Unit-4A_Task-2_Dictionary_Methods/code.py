# Create a sample dictionary
student = {
    "name": "John",
    "age": 18,
    "branch": "CSE",
    "marks": 85
}

# Display dictionary
print("Original Dictionary:", student)

# Display keys
print("Keys:", student.keys())

# Display values
print("Values:", student.values())

# Display items
print("Items:", student.items())

# Access value using get()
print("Name:", student.get("name"))

# Update dictionary
student.update({"marks": 95, "city": "Vijayawada"})
print("After Update:", student)

# Remove an element using pop()
student.pop("age")
print("After Pop:", student)
