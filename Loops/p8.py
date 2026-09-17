# Find sum of even numbers between 1 and 100

total_sum = 0

for i in range(1, 101):
    if i % 2 == 0:
        total_sum += i

print(f"The sum of even numbers between 1 and 100 is: {total_sum}")