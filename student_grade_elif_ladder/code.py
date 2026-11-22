code:
marks = int(input("Enter student marks: "))

if marks >= 90 and marks <= 100:
    print("A Grade")
elif marks >= 80:
    print("B Grade")
elif marks >= 70:
    print("C Grade")
elif marks >= 60:
    print("D Grade")
elif marks >= 0:
    print("Fail")
else:
    print("Invalid Marks")
