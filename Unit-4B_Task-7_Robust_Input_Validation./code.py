while True:
    try:
        age = int(input("Enter your age: "))

        if age < 0 or age > 120:
            print("Error: Age must be between 0 and 120.")
            continue

        print("Valid age:", age)
        break

    except ValueError:
        print("Error: Please enter a valid integer.")
