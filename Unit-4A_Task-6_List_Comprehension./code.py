# Program to demonstrate List Comprehension

# Create a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Create a list of squares using list comprehension
squares = [x ** 2 for x in numbers]

# Create a list of even numbers
even_numbers = [x for x in numbers if x % 2 == 0]

# Create a list of odd numbers
odd_numbers = [x for x in numbers if x % 2 != 0]

# Display the results
print("Original List:", numbers)
print("Squares:", squares)
print("Even Numbers:", even_numbers)
print("Odd Numbers:", odd_numbers)
