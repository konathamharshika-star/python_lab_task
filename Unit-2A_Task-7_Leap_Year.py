# Example solution: leap year using nested if-else
year = int(input("Enter a year: "))

if year % 400 == 0:
    print(f"{year} is a leap year")
else:
    if year % 100 == 0:
        print(f"{year} is not a leap year")
    else:
        if year % 4 == 0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")


            # Example solution: leap year using if-elif-else ladder
year = int(input("Enter a year: "))

if year % 400 == 0:
    print(f"{year} is a leap year")
elif year % 100 == 0:
    print(f"{year} is not a leap year")
elif year % 4 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

    # Example solution: leap year using one combined condition
year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")