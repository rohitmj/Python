#A simple dictionary
alien = {'color':'yellow','points':5}
print(alien['color'])
print(alien['points'])

new_points = alien['points']
print(f"Your new points is {new_points} points!")

#Adding elements to the dictionary
alien_0 = {'color':'green','points': 10}
print(alien_0)

alien_0['x-position'] = 0
alien_0['y-position'] = 25
print(alien_0)

#Starting with empty dictionary
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

#Modifying values in a dictionary
alien_1 = {'color':'black'}
print(f"The color of alien is {alien_1['color']}")
alien_1['color'] = 'blue'
print(f"Now, The color of alien is {alien_1['color']}")  

#Determining and giving new values to alien movements
alien = {'x-position': 0 , 'y-position': 25 , 'speed':'medium'}
print(f" Original position: {alien['x-position']}")

#Now moving it to the right
#Determining how far is it from current speed
if alien['speed'] == 'slow':
	x_increment = 1
elif alien['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3

#Giving new position value
alien['x-position'] = alien['x-position'] + x_increment
print(f" New Position: {alien['x-position']}")

#Removing key value pairs
alien = {'color':'black','points': 5}
print(alien)
del alien['color']
print(alien)


#Storing Larger files
favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

language = favorite_languages['sarah']
print(f"Sarah favorite language is {language.title()}")


#Using get() to access values
alien = {'color':'black','name':'baka'}
point_value = alien.get('points','No value assigned')
print(point_value)


#Looping through dictionary
user_0 = {
 'username': 'Rohi333',
 'first': 'Rohit',
 'last': 'MJ',
 }

for key,value in user_0.items():
	print(f"\n Key: {key}")
	print(f"Value: {value}")

#Again
favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

for name,language in favorite_languages.items():
	print(f"{name.title()} favorite language is {language.title()}")

#Looping using keys() method
favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

friends = ['phil','sarah']
if name in friends:
 	language = favorite_languages[name].title()
 	print(f"\t{name.title()}, I see you love {language}!")

#keys() method isn’t just for looping: it actually returns a list of all
#the keys, and the line at u simply checks if 'erin' is in this list
if 'erin' not in favorite_languages.keys():
	print("Erin, Please take the poll")

#Looping through dictionary keys in particular order
favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
for name in sorted(favorite_languages.keys()):
 print(f"{name.title()}, thank you for taking the poll.")

#Set method to print out unique values only
#Without Set
print("The following languages have been mentioned:")
for language in favorite_languages.values():
 print(language.title())
#With set
for language in set(favorite_languages.values()):
	print(language.title())

#NESTING
one_piece = {'captain':'luffy','swordsman':'zoro'}
one_punch_man = {'powerful':'saitama','robot':'genos'}
black_clover = {'child1':'asta','child2':'yuno'}

anime = [one_piece,one_punch_man,black_clover]
for anime in anime:
	print(anime)

#Making empty list for storing aliens
aliens = []

#Make 30 aliens and add in the list
for alien_number in range(30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)

for aliens in aliens[:5]:
	print(aliens)

print(f"The total number of aliens are: {len(aliens)}")

#A Dicionary in a dictionary
users = {
		 'aeinstein': {
						 'first': 'albert',
						 'last': 'einstein',
						 'location': 'princeton',
					   },
		 'mcurie': {
					 'first': 'marie',
					 'last': 'curie',
					 'location': 'paris',
				   },
 		}

for username, user_info in users.items():
	print(f"\n Username: {username}")
	full_name = f"{user_info['first']} {user_info['last']}"
	location = user_info['location']
	print(f"\t Full name: {full_name.title()}")
	print(f"\t Location: {location.title()}")
	




















































