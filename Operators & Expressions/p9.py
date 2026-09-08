# Input age and marks
age = int(input("Enter age: "))
marks = int(input("Enter marks: "))

# Using AND operator
if age >= 18 and marks >= 50:
    print("Eligible")

# Using OR operator
if age < 18 or marks < 50:
    print("Not Eligible")