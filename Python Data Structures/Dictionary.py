#Create a dictionary storing student names and marks
students = {
    "Aryan": 85,
    "Priya": 90,
    "Rahul": 78
}

print(students)
#Add a new key-value pair to an existing dictionary
students = {
    "Aryan": 85,
    "Priya": 90,
    "Rahul": 78
}

students["Neha"] = 92

print(students)
#Delete a key-value pair from a dictionary
students = {
    "Aryan": 85,
    "Priya": 90,
    "Rahul": 78
}

del students["Rahul"]

print(students)

#Merge two dictionaries into one
dict1 = {
    "Aryan": 85,
    "Priya": 90
}

dict2 = {
    "Rahul": 78,
    "Neha": 92
}

merged_dict = {**dict1, **dict2}

print(merged_dict)
#Check if a key exists in a dictionary
students = {
    "Aryan": 85,
    "Priya": 90,
    "Rahul": 78
}

key = "Priya"

if key in students:
    print("Key exists")
else:
    print("Key does not exist")

#Count word frequency in a string using a dictionary
text = "apple banana apple mango banana apple"

words = text.split()
freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print(freq)
#Find the key with the maximum value in a dictionary
students = {
    "Aryan": 85,
    "Priya": 90,
    "Rahul": 78
}

max_key = max(students, key=students.get)

print("Key with maximum value:", max_key)
#Reverse keys and values in a dictionary
students = {
    "Aryan": 85,
    "Priya": 90,
    "Rahul": 78
}

reversed_dict = {}

for key, value in students.items():
    reversed_dict[value] = key

print(reversed_dict)
#Update the value for a specific key
students = {
    "Aryan": 85,
    "Priya": 90,
    "Rahul": 78
}

students["Aryan"] = 95

print(students)
#Update the value for a specific key
students = {
    "Aryan": 85,
    "Priya": 90,
    "Rahul": 78
}

students["Aryan"] = 95

print(students)
#Convert a list of tuples into a dictionary
data = [("Aryan", 85), ("Priya", 90), ("Rahul", 78)]

students = dict(data)

print(students)

