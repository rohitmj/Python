""" 
Messages: Make a list containing a series of short text messages. Pass the
list to a function called show_messages(), which prints each text message.
"""

def show_messages(messages):
	for message in messages:
		msg = f"{message.title()}!"
		print(msg)

short_text_messages = ['message1','message2','message3']
show_messages(short_text_messages)

"""
Sending Messages: Start with a copy of your program from Exercise.
Write a function called send_messages() that prints each text message and
moves each message to a new list called sent_messages as it’s printed. After
calling the function, print both of your lists to make sure the messages were
moved correctly.
"""

def send_messages(messages,moved_messages):
	while messages:
		current_message = short_text_messages.pop()
		print(f"Current_message: {current_message}")
		moved_messages.append(current_message)

	for current_message in current_message:
		print(f"{current_message}")
	for moved_messages in moved_messages:
		print(f"{moved_messages}")

short_text_messages = ['message1','message2','message3']
moved_messages = []
send_messages(short_text_messages,moved_messages)

"""
Archived Messages: Start with your work from Exercise. Call the
function send_messages() with a copy of the list of messages. After calling the
function, print both of your lists to show that the original list has retained its
messages.
"""

def send_messages(messages,moved_messages):
	while messages:
		current_message = short_text_message.pop()
		print(f"Current_message: {current_message}")
		moved_messages.append(current_message)

	for current_message in current_message:
		print(f"{current_message}")
	for moved_messages in moved_messages:
		print(f"{moved_messages}")

short_text_message = ['message1','message2','message3']
moved_messages = []
send_messages(short_text_message[:],moved_messages)










