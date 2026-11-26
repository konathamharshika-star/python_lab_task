# Define a function
def calculate_marks(m1, m2, m3):
    total = m1 + m2 + m3
    average = total / 3
    return total, average

# Get marks from user
m1 = int(input("Enter marks of subject 1: "))
m2 = int(input("Enter marks of subject 2: "))
m3 = int(input("Enter marks of subject 3: "))

# Call the function
total, average = calculate_marks(m1, m2, m3)

# Display results
print("Total Marks:", total)
print("Average Marks:", average)
