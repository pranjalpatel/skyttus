#Electricity bill calculator.

units = int(input("Enter units: "))

if units <= 100:
    bill = units * 2
else:
    bill = units * 5

print("Bill =", bill)