#Task 1 - Take a string input and print length
text = input("Enter a string: ")

print("Length =", len(text))
#Task 2 - Convert a sentence to lowercase
text= input("Enter a sentence: ")

print("Lower case:", text.lower())

#Task 3 - Replace spaces with underscores in a string

text = input("Enter a string: ")

print("Result:", text.replace(" ", "_"))

#Task 4 - Extract the first and last character of a string 
text = input("Enter a string: ")

print("First character:", text[0])
print("Last character:", text[-1])
#Task 5 - Reverse a string using slicing

text=input("Enter a string : ")
reverse_text = text[::-1]
print("Reversed string:", reverse_text)
#Task 6- Count how many times a letter appears in a string.
text = input("Enter a string: ")
letter = input("Enter a letter: ")

count = text.count(letter)

print("The letter appears", count, "times.")
#Task 7- Check if a word is present in a sentence.
sentence = input("Enter a sentence: ")
word = input("Enter a word: ")

if word in sentence:
    print("Word is present")
else:
    print("Word is not present")
#Task 8-Take name & age and print using f-string formatting
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"My name is {name} and I am {age} years old.")
#Task 9-Remove extra spaces from the start and end of a string
text = input("Enter a string: ")

print(text.strip())
#Task 10-Join a list of words into a single string with - between them

words = ["Python", "is", "easy"]

result = "-".join(words)

print(result)
 