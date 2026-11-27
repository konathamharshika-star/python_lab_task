# Program to demonstrate Dictionary Comprehension

# Create a list of numbers
numbers = [1, 2, 3, 4, 5]

# Create a dictionary using dictionary comprehension
squares = {x: x ** 2 for x in numbers}

# Display the dictionary
print("Original List:", numbers)
print("Square Dictionary:", squares)

# Create a dictionary of even numbers
even_numbers = {x: x ** 2 for x in numbers if x % 2 == 0}

# Display even numbers dictionary
print("Even Numbers Dictionary:", even_numbers)
