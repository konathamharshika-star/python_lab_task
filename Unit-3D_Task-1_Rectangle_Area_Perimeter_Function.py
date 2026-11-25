# Define a function
def rectangle(length, breadth):
    area = length * breadth
    perimeter = 2 * (length + breadth)
    return area, perimeter

# Get input from user
length = int(input("Enter length: "))
breadth = int(input("Enter breadth: "))

# Call the function
area, perimeter = rectangle(length, breadth)

# Display results
print("Area of Rectangle:", area)
print("Perimeter of Rectangle:", perimeter)