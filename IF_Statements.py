'''
if condition_test:
	do something

elif condition_test:
	do something

else:
	do something

'''


cars = ['audi','bmw','maruti','suzuki']
for cars in cars:
	if cars == "bmw":
		print(cars.upper())
	else:
		print(cars.title())
'''
-> checking value in cmd
>>> requested_toppings = ['mushrooms','onions','pineapple']
>>> 'mushrooms' in requested_toppings
True
>>> 'pepporoni' in requested_toppings
False


-> Using AND, OR operation to check values in cmds
 >>> age_0 = 22
>>> age_1 = 21
>>> age_0 >= 21 and age_1 >= 21
True
>>> age_0 = 18
>>> age_0 >= 21 or age_1 >= 21
True
'''

#Checking value is not in the list
banned_users = ['hinata','Rosette','Marshmallow']
user = 'marie'
if user not in banned_users:
	print(f'{user.title()}, you are not on the banned list')


#Checking age using if, elif, else
age = 12
if age < 4:
	print("Your admission cost is $0.")

elif age < 18:
	print('Your admission cost is $25.')

else:
	print('Your admission cost is $40.')

#Adding if else in lists 
Anime = ['One punch man','spiderman','One piece']
for Anime in Anime:
	if Anime == 'spiderman':
		print(f'Sorry, {Anime.title()} is not an Anime.')
	else:
		print(f'Yes, {Anime.title()} is Anime.')

print("\n Great!!!")


available_toppings = ['mushrooms', 'olives', 'green peppers',
 						'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print(f"Adding {requested_topping}.")
	else:
		print(f'Sorry, we dont have {requested_topping}.')

print("\nFinished making your pizza!")

