Names = ['Honda','Maruti','doflamingo','Luffy','zoro']
print(Names)

#Acessing only one
print(Names[3])

#Acessing only One with Capitalized word
print(Names[2].title())

#Returning Last item on the list
print(Names[-1])

#Using F-strings to create message and pull list values
message = f"My favorite one piece character is {Names[4].title()}."
print(message)

#Modify elements in the list
Names[0] = 'Sanji'
Names[1] = 'Chopper'
print(Names)

# Adding element in the list
Names.append('Nami')
print(Names)

#insert elements and giving them position
Names.insert(0,'Robin')
print(Names)

#Removing element
del Names[3]
print(Names)

#Removing item using pop() method
popped_names = Names.pop()
print(popped_names)

#Removing item using remove() method
Names.remove('Luffy')
print(Names)

#Organizing Lists

#Using sort method
Names.sort()
print(Names)

#Sorting in reverse 
Names.sort(reverse=True)
print(Names)

#Using sorted method
print(sorted(Names))

#Printing in reverse order
Names.reverse()
print(Names)

#Finding length of the list
 # >>> len(Names)


