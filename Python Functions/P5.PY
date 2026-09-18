#Function to check if a word is palindrome
def palindrome(word):
    return word == word[::-1]

print(palindrome("madam"))