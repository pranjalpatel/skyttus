#Function to count vowels in a string
def count_vowels(text):
    count = 0
    vowels = "aeiouAEIOU"
    for ch in text:
        if ch in vowels:
            count += 1
    return count

print(count_vowels("Hello World"))