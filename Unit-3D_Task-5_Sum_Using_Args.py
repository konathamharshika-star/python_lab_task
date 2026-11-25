# Define a function using *args
def calculate_sum(*args):
    total = sum(args)
    return total

# Call the function
result = calculate_sum(10, 20, 30, 40, 50)

# Display the result
print("Sum of values:", result)