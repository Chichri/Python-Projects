classes = ['Fighter', 'Rogue', 'Bard', 'Cleric']
message = "My favorite class is the " + classes[2].title()
print(message)
#Classes is now a list containing these four items
#You can select items from the list for printing or other uses
#The index of a list begins at zero, making the third option, "Bard", the second

print("\n")
#Each print("\n") simply partions the output with a newline
#This makes it easier to read and compare to the code

classes.append('Wizard')
print(classes)
#The append function adds an item to the end of the list

print("\n")

classes.insert(4,'Druid')
print(classes)
#the insert function adds an item to where ever directed

#No print("\n") here becasue the following section was commented for convenice

#del classes[0]
#print(classes)
#del removes a directed item from the list
#Uncommenting this section would delete fighters from the list,
#I commented this to keep more items to work with for later

print("\n")

popped_classes = classes.pop()
print(classes)
print(popped_classes)
#pop() removes the last item on a list unless directed otherwise
#you can still work with the item as shown

print("\n")

second_pop = classes.pop(0)
print(classes)
print(second_pop)
#This pop removes the first item (rember that the index on a list begins with zero)

print("\n")

classes.remove('Rogue')
print(classes)
#Remove ... removes an item from the list like pop
#However, with remove, you only need to the the item, not the position of the items
#You can also work with removed items like in pop as shown below

print("\n")

classes.insert(0,'Rogue')
print(classes)
#Just putting back rogue so we have more to work with

print("\n")

removed_classes = 'Bard'
classes.remove('Bard')
print(classes)
print(removed_classes)
#As previously metioned, one can work with removed items like in pop

print("\n")

classes.insert(1, "Bard")
print(classes)
#Again, just giving us more to work with

print("\n")

classes.sort()
print(classes)
#sort shuffles the list around so its alphabetical


classes.sort(reverse=True)
print(classes)
#sort can also be configured to organize the list in reverse alphabetical order

print("\n")

print(sorted(classes))
print(classes)
#The sorted function can be used to temporarily sort lists,
#It displays the sorted version of the list without actually changing the order

print("\n")

print(classes)
classes.reverse()
print(classes)
#Reverse does exactlly what you'd think, it reverses the lists
#Unlike the reverse sort, this just flips the list backwards
#Reverse is permantant, although it can be undone by another reverse

print("\n")

print(len(classes))
#Len (short for length) determins the list's length (eg amount of items contained)
#For some reason, len counts starting with one as opposed to the index zero
#Handy for determening the length of the list when you're unsure after an event
