"""
10-3. Guest: Write a program that prompts the user for their name. When they
respond, write their name to a file called guest.txt.
"""

#Asking name from user
name = input("What's your name? ")

filename = 'guest.txt'

with open(filename, 'w') as f:
    f.write(name)

"""
10-4. Guest Book: Write a while loop that prompts users for their name. When
they enter their name, print a greeting to the screen and add a line recording
their visit in a file called guest_book.txt. Make sure each entry appears on a
new line in the file.
"""
filename = 'guest_book.txt'

print("Enter 'quit' when you are finished.")
while True:
    name = input("\nWhat's your name? ")
    if name == 'quit':
        break
    else:
        with open(filename, 'a') as f:
            f.write(f"{name}\n")
        print(f"Hi {name}, you've been added to the guest book.")

"""
10-5. Programming Poll: Write a while loop that asks people why they like
programming. Each time someone enters a reason, add their reason to a file
that stores all the responses.
"""
filename = 'Programming.txt'

print("Enter 'quit' when you are finished.")
while True:
    text = input("\nWhy you like programming? ")
    if text == 'quit':
        break
    else:
        with open(filename, 'a') as f:
            f.write(f"{text}\n")
        print(f"Like programming because {text}.")
        