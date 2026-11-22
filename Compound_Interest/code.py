formula:

CI = P(1+\frac{R}{100})^T-P

p = float(input("Enter principal amount: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))

ci = p * (1 + r/100)**t - p

print("Compound Interest:", ci)
