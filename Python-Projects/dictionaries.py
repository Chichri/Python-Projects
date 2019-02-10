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

user_0 = {
'username': 'efermi',
'first': 'enrico',
'last': 'fermi',
}

for key, value in user_0.items():
    print("\nKey: " + key)
    print('Value: ' + value)
#As shown, it is possible to loop through dictionaries
#note that key and value are just variables, not some tool in Python
