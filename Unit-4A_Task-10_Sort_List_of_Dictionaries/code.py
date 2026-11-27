# Create a list of dictionaries
students = [
    {"name": "John", "marks": 85},
    {"name": "David", "marks": 95},
    {"name": "Smith", "marks": 75},
    {"name": "Alice", "marks": 90}
]

# Display original list
print("Original Student Records:")
for student in students:
    print(student)

# Sort students by marks in ascending order
students.sort(key=lambda x: x["marks"])

# Display sorted list
print("\nStudents Sorted by Marks:")
for student in students:
    print(student)
