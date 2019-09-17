alien_0 = {'color': 'green', 'points': 5}

print(alien_0)
print(alien_0['color'])
print(alien_0['points'])
#This is a dictionary. It stores information in key:value pairs
#Each key is connected to a value. Here, 'color' is connected to 'green'
#The key can be used to work with the value it holds, like with the print function
#Key:value pairs are separated within dictionaries by commas

print('\n')

alien_0['x_position'] = 0
alien_0['y_position'] = 25
alien_0['points'] = 10
print(alien_0)
#New Key pairs can be added to Dictionaries after its creation
#Key pairs can also be modified following their creation

print('\n')

alien_0['temporarykey'] = 'useless'
del alien_0['temporarykey']
print(alien_0)
#Key pairs can be removed through del

print('\n')

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

print("Sarah's favorite language is " +
favorite_languages['sarah'].title() + ".")
#As you can see, this dictionary has been broken into multiple lines.
#When your dictionary (or list or tuple) will exceed 80 chars, this is good form
#This rule is to help prevent extremly long lines of code that become tedious to read

print("\n")

for name in favorite_languages.keys():
    print(name.title())
#The for loops parameters assign the keys of the dictionary to var usernames
#note that key and value are in fact terms in python, not just named vairables

print("\n")

#Also note that dictionaries loop through keys by default, so this works too:
for name in favorite_languages:
    print(name.title())

print("\n")

friends = ['phil',]


if name in friends:
    print("Hey, " + name.title() + ', ' + "I see that your favorite laguage is "
    + favorite_languages[name].title())
#Here we can see that one can cross-refrence other lists with dictionaries

print("\n")

print("The following laguages have been metioned:")
for language in set(favorite_languages.values()):
    print(language.title())
#set removes repetion. Python was metioned twice, but we only need in once

print("\n")

user_0 = {
'username': 'efermi',
'first': 'enrico',
'last': 'fermi',
}

for key, value in user_0.items():
    print("\nKey: " + key)
    print('Value: ' + value)
#As shown, it is possible to loop through dictionaries with both keys and values
#items is required for the code to recognize the keys and values when used as such

print("\n")

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
#This is whats called nesting, storing dictionaries or the like in a lists
#Note that this doesn't work in some conditions, or in some languages at all

print("\n")

users = {
'aeinstein': {
'first': 'albert',
'last': 'einstein',
'location': 'princeton',
}
}

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull_name: " + full_name.title())
    print("\tLocation: " + location.title())
#This is another example of nesting, although here we nest a dict within a dict
#Notice how the program is structured to access the keys within the dicts
