# Palindrome String

string = input("Enter a string: ")

reverse = string[::-1]

if string == reverse:
    print("It is a Palindrome")
else:
    print("It is Not a Palindrome")