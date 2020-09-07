#Simple Function
def greet_user():
 	print("Hello User")

greet_user()

#Passing information to function
def greet_users(username):
	print(f"Hello, {username.title()}!")

greet_users('Jess')

#Multiple Arguments
def describe_animal(Animal_type,Animal_name):
	print(f"My animal is {Animal_type.title()} ")
	print(f"The {Animal_type.title()} name is {Animal_name.title()}")

describe_animal('Reindeer','chopper')

#Keyword arguments
def describe_animal(Animal_type,Animal_name):
	print(f"My animal is {Animal_type.title()} ")
	print(f"The {Animal_type.title()} name is {Animal_name.title()}")

describe_animal(Animal_type='Reindeer',Animal_name='chopper')

#Default Values
def describe_pet(pet_name, animal_type='dog'):
	print(f"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}.")
 
describe_pet(pet_name='willie')

#Returning a simple value
def get_formatted_name(first_name, last_name):
	full_name = f"{first_name} {last_name}"
	return full_name.title()

musician = get_formatted_name('jimi','hendrix')
print(musician)

#Making an argument optional
def get_name(first_name, last_name, middle_name=''):

	if middle_name:
		full_name = f"{first_name} {middle_name} {last_name}"
	else:
		full_name = f"{first_name} {last_name}"

	return full_name.title()

musician = get_name('jimi', 'hendrix')
print(musician)
musician = get_name('john', 'hooker', 'lee')
print(musician)

#Returning a dictionary
def build_person(first_name, last_name):
	person = {'first': first_name, 'last': last_name}
	return person

musician = build_person('Rohit','Mj')
print(musician)

#Returning a dictionary with age
def build_person(first_name, last_name, age=None):
	person = {'first': first_name, 'last': last_name}
	if age:
		person['age'] = age
	return person

musician = build_person('Rohit','Mj', age=21)
print(musician)

#Using a function with a while loop

def get_formatted_name(first_name, last_name):
	"""Return full name, neatly formatted."""
	full_name = f"{first_name {last_name}}"
	return full_name.title()

#This is an infinite loop!
while True:
	print("/nPlease tell me your name:")
	f_name = input("first_name: ")
	l_name = input("Last name: ")

	formatted_name = get_formatted_name(f_name, l_name)
	print(f"/nHello,{formatted_name}!")


#Adding a quit condition in the while loop

def get_formatted_name(first_name, last_name):
	"""Return full name, neatly formatted."""
	full_name = f"{first_name {last_name}}"
	return full_name.title()

while True:
	print("/nPlease tell me your name:")
	print("(enter 'q' at any time to quit)")

	f_name = input("First name: ")
	if f_name == 'q':
		break

	l_name = input("last_name: ")
	if l_name == 'q':
		break

	formatted_name = get_formatted_name(f_name, l_name)
	print(f"/nHello, {formatted_name}!")
	


