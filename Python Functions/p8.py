#Function to find GCD of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print(gcd(12, 18))