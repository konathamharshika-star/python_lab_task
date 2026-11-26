# Global balance
balance = 1000

# Function to deposit money
def deposit(amount):
    global balance
    balance += amount
    print("Deposited Amount:", amount)
    print("Updated Balance:", balance)

# Function using local balance
def local_balance():
    balance = 500
    print("Local Balance:", balance)

# Display original balance
print("Original Balance:", balance)
