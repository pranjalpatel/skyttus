# Generate the first N fibonacci numbers 

n = int(input("Enter the number of terms: "))

a, b = 0, 1

if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print(f"Fibonacci sequence: {a}")
else:
    print("Fibonacci sequence:", end=" ")
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()