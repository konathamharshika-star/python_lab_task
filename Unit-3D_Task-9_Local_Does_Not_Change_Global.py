# Global counter
counter = 0

# Define a function
def increment():
    global counter
    counter += 1
    print("Counter:", counter)

# Call the function
increment()
increment()
increment()