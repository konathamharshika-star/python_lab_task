class InvalidSpeedError(Exception):
    pass

try:
    speed = int(input("Enter vehicle speed: "))

    if speed < 0 or speed > 200:
        raise InvalidSpeedError("Invalid speed! Speed must be between 0 and 200.")

    print("Valid speed:", speed, "km/h")

except ValueError:
    print("Error: Please enter a valid number")

except InvalidSpeedError as e:
    print("Error:", e)
