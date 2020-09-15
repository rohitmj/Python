"""
10-1. Learning Python: Open a blank file in your text editor and write a few
lines summarizing what you’ve learned about Python so far. Start each line
with the phrase In Python you can. . . . Save the file as learning_python.txt in
the same directory as your exercises from this chapter. Write a program that
reads the file and prints what you wrote three times. Print the contents once by
reading in the entire file, once by looping over the file object, and once by storing the 
lines in a list and then working with them outside the with block.
"""
filename = 'learning_python.txt'

with open(filename) as file_object:
	for line in file_object:
		print(line)
		print(line)
		print(line)


with open(filename) as file_object:
	lines = file_object.readlines()
	for line in lines:
		print(line.strip())

with open(filename) as file_object:
	lines = file_object.readlines()
	pi_string = ''
	for line in lines:
		pi_string += line.strip()

print(f"{pi_string}")

"""
10-2. Learning C: You can use the replace() method to replace any word in a
string with a different word. Here’s a quick example showing how to replace
'dog' with 'cat' in a sentence:
>>> message = "I really like dogs."
>>> message.replace('dog', 'cat')
'I really like cats.'
Read in each line from the file you just created, learning_python.txt, and
replace the word Python with the name of another language, such as C. Print
each modified line to the screen.
"""

filename = 'learning_python.txt'

with open(filename) as f:
    lines = f.readlines()

for line in lines:
    # Get rid of newline, then replace Python with C.
    line = line.rstrip()
    print(line.replace('Python', 'C'))