#Create a tuple with 5 numbers.

numbers = (10, 20, 30, 40, 50)

print(numbers)

#Access the third element in a tuple.
numbers = (10, 20, 30, 40, 50)

print(numbers[2])
#Unpack a tuple into separate variables
data = (10, 20, 30)

a, b, c = data

print(a)
print(b)
print(c)
#Create a set of 5 fruits
fruits = {"Apple", "Banana", "Mango", "Orange", "Grapes"}

print(fruits)
#Add a new fruit to the set
fruits = {"Apple", "Banana", "Mango", "Orange", "Grapes"}

fruits.add("Pineapple")

print(fruits)
#Remove an element from a set
fruits = {"Apple", "Banana", "Mango", "Orange"}

fruits.remove("Banana")

print(fruits)
#Find union of two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}

result = set1.union(set2)

print(result)
#Find intersection of two sets
result = set1.intersection(set2)

print(result)
#Check if one set is a subset of another
set1 = {1, 2}
set2 = {1, 2, 3,4}

result = set1.issubset(set2)
#Convert a list with duplicate values into a set to remove duplicate
numbers={1,2,2,3,4,4,5}
unique_numbers=set(numbers)
print(unique_numbers)
