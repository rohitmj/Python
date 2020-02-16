#Input() function
name = input("Enter your name: ")
print(f"Your name is {name.title()}")



prompt = "Tell me about yourself"
#adding new string onto the end
prompt += "\nWhat is your first name: "
name = input(prompt)
print(f"\n Hello, {name}!")


#using int() to accept numerical input
height = input("How tall are you, in inches?\n")
height = int(height)
if height >= 48: 
	print("\n You will be able to ride")
else:
	print("\n You will be able to ride when you get old")



#Using modulo to find odd and even number
message = "Let's Play a game"
message += "\nEnter a number and I will tell you if its odd or even: "
number = input(message)
number = int(number)
if number % 2 == 0:
	print(f"\nThe number {number} is even.")
else:
	print(f"\nThe number {number} is odd.")



#Introducing while loops
current_number = 1
while current_number <= 5:
	print(current_number)
	current_number += 1

#letting the user choose when to quit
prompt = "\nTell me something and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
	message = input(prompt)
	print(message)



#Using a Flag
prompt = "\nTell me something and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "
active = True
while active:
	message = input(prompt)

	if message == 'quit':
		active = False
	else:
		print(message)

#Using break to exit a loop
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
	city = input(prompt)

	if city == 'quit':
		break
	else:
		print(f"I'd love to go to {city.title()}!")




#Using continue in a loop
current_number = 0
while current_number < 10:
	current_number += 1
	if current_number % 2 == 0:
		continue
	print(current_number)



#Using a while loop with lists and Dictionaries
#Moving items from one list to another

# Start with users that need to be verified,
# and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.
while unconfirmed_users:
	current_user = unconfirmed_users.pop()

	print(f"Verifying user: {current_user.title()}")
	confirmed_users.append(current_user)

# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
	print(confirmed_user.title())




#Filling dictionary with user input
responses = {}

#Set a flag to indicate that polling is active
polling_active = True

while polling_active:
	#prompt for person's name and response.
	name = input("\nWhat is your name? ")
	response = input("Which mountain would you like to climb someday? ")

	#Store response in dictionary
	responses[name] = response

	#Find out if anyone else is going to take the poll.
	repeat = input("Would you like to let another person respond? (yes/no) ")
	if repeat == 'no':
		polling_active = False

# Polling is complete. show the results
print("\n----- Poll Results -----")
for name, response in responses.items():
	print(f"{name} would like to climb {response}.")


