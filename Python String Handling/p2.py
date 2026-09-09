# Create a list of your 5 favorit movies
movies=['Mirzapur','KGF','Toxic','Spiderman','Saalar']

# add new movie to the list 
movie = input("Enter a new movie name: ")
movies.append(movie)
print("movies",movies)
#Remove the first movie from the list
movies.pop(0)
print("movies",movies)
# short a list of numbers in  ascendig order
numbers = [45, 12, 78, 23, 5]

numbers.sort()

print(numbers)

#Revrese a list
movies=['Mirzapur','KGF','Toxic','Spiderman','Saalar']
movies.reverse()
print("movies",movies)
# find the largest number of the list
numbers = [45, 12, 78, 23, 5]
largest = max(numbers)

print("Largest number:", largest)
#Merge two list into one
list1 = [1, 2, 3]
list2 = [4, 5, 6]

merged_list = list1 + list2

print(merged_list)
#Access the last element of a list without using index number.
my_list = [10, 20, 30, 40, 50]

print(my_list.pop())
#Create a nested list and access a specific inner element.
nested_list = [[1, 2], [3, 4], [5, 6]]

print(nested_list[1][0])
#Count how many times an element appears in a list
numbers = [1, 2, 3, 2, 4, 2, 5]

print(numbers.count(2))