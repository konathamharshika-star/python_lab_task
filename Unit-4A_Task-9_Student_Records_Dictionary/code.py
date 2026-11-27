# Create an empty dictionary
students = {}

# Get number of students
n = int(input("Enter number of students: "))

# Store student records
for i in range(n):
    print("\nEnter details of student", i + 1)

    roll_no = int(input("Enter Roll Number: "))
    name = input("Enter Student Name: ")
    marks = float(input("Enter Marks: "))

    students[roll_no] = {
        "name": name,
        "marks": marks
    }

# Display student records
print("\nStudent Records:")

for roll_no, details in students.items():
    print("\nRoll Number:", roll_no)
    print("Name:", details["name"])
    print("Marks:", details["marks"])

# Search for a student
search = int(input("\nEnter Roll Number to Search: "))

if search in students:
    print("Student Found!")
    print("Name:", students[search]["name"])
    print("Marks:", students[search]["marks"])
else:
    print("Student Not Found!")
