#Working with For loop
crews = ['luffy','name','chopper','robin']
for crews in crews:
	print(f"{crews.title()}, is a good crewmate")	
	print(f"It will be a great adventure {crews.title()}. \n")

print("This is from One Piece. (=^_^=)")

#Using range() function
for value in range(1, 5):
	print(value)

#Changing the set of numbers in lists
numbers = list(range(1,6))
print(numbers)

#Skipping steps in range
even_numbers = list(range(2, 11, 2))
print(even_numbers)

#Printing Squares of numbers
squares = []
for value in range(1,11):
	squares.append(value ** 2)

print(squares)

#list comprehension for same above code
squares = [value ** 2 for value in range(1,11)]
print(squares)

#Slicing the list
characters = ['kuroko','kagami','tetsuya','kise','aomine']
print(characters[0:3])

#Looping through Slice
characters = ['kuroko','kagami','tetsuya','kise','aomine']
print("Here are the characters in kuroko no basket anime: ")
for characters in characters[:3]:
	print(characters.title())

#Copying a list
my_foods = ['pizza','dumplings','ramen']
friend_foods = my_foods[:]

print(my_foods)
print(friend_foods)

#Defining a tuple
Dimension = (200, 50)
print(Dimension[0])
print(Dimension[1])

#Writing over a tuple
Dimension = (200, 50)
print(Dimension[0])
print(Dimension[1])

Dimension = (150, 90)
print(Dimension[0])
print(Dimension[1])




















