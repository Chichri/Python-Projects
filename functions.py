def greet_user():
    """Display a simple greeting."""
    print('Hello')

greet_user()
#A function is a block of code desgined to do a specifc job
#The keyword def defines greet_user() as a function
#The parentheses that come after are required. They potentially hold informtion
#Line 2 is a docsting. Docstrings document the function in the documentation
#Line 3 is the only actual code in the function, print('Hello'), so when the -
#-function is called, thats all that happens

print('\n')

def greet_user(username):
    print('Hello, ' + username.title() + '!')

greet_user('jesse')
greet_user('mark')
greet_user('larry')
#Here, we've modified the function greet_user() slightly to accept usernames
#Now, the function will expect a value for username, which is filled in later
#This will work for any value of username specified
#The variable username is called a parameter
#The value of 'jeese' in greet_user('jesse') is an argument, where a piece of -
#-information is passed down from the function call to the function

print('\n')

def describe_animal(animal_type, pet_name):
    print('I have a pet ' + animal_type  + '.')
    print('My ' + animal_type  + "'s name is " + pet_name.title() + '.' )

describe_animal('hamster', 'harry')
#This function uses positional arguements to handle more than one arguement
#Like most things in python, posistional arguements are logically put in order
#Simply call your parameters in the correct order separated by commas, and -
#-everything works as normal.

print('\n')

describe_animal(animal_type='hamster', pet_name='harry')
#This is a keyword arguement. The name and the value are directly associated
#Keyword arguements do not have to be ordered correctly

print('\n')

def describe_animal(pet_name, animal_type='dog'):
    print('I have a pet ' + animal_type + '.')
    print('My ' + animal_type + "'s name is " + pet_name.title() + '.' )

describe_animal('willie')
#I've re-written the function to include a default value, animal_type='dog'
#When the function is called, any instance of animal_type will be dog by default
#Therefore, all that needs to be filled in is the pet_name
#Defualt values do have to be ordered correctly as written here

print('\n')

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formated"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

bassist = get_formatted_name('john', 'entwhistle')
print(bassist)
#This functions returns a value, the concatetation of first_name and last_name
#Using this value, we can asign the function to a variable, then print it
#This seems compliated for a simple print, but can be useful in longer programs

print('\n')

def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + ' '+ middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name

    return full_name.title()

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

legend = get_formatted_name('jimi', 'hendrix')
print(legend)
#Through the use of if statements, you can make certain perameters optional
#Normaly, if you were to give the function a parameter and not use it in the -
#call, you would get a positional arguement error
#by making middle_names default value an empty string, you can make it optional
#The catch is that middle_name must be last, or else names without it fail

print('\n')

def build_person(first_name , last_name ):
    person = {'first': first_name, 'last': last_name}
    return person

everyman = build_person('John', 'Doe')
print(everyman)
#functions can be used with all manner of storig data, including dictionaries
#With this the first and last name are labled and we can easily add more info

print('\n')

while True:
    print('Tell me your name\n')
    f_name = input("First name:\n")
    l_name = input("Last name:\n")
    def person():
        print('Hello ' + f_name + ' ' + l_name + '!')
    person()
    break
#Here, we use a while loop with this function. The function prints a name
#Without the break and with no exit conditions, this loop would be infinte

print('\n')

def greet_users(names):
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['racter', 'ren', 'gaichu']
greet_users(usernames)
#This is a re written bit from the beginning. It greets people by passing a list
#Passing a list in a function means using the fuction to act on the items within
#Here, we've primed the function to take a list, assgined to parameter 'names'
#Using a for loop, we loop through the list, printing a greeting each time
#We then define the list as usernames, and sub that in for the parameter

print('\n')

unprinted_designs = ['D20', 'Master Sword', 'Bootleg Amibo']
printed_designs = []

def print_design(unprinted_designs, printed_designs):
    while unprinted_designs():
        current_design = unprinted_designs.pop()
        print('Printing model: ' + current_design)
        printed_designs.append(current_design)

print('\n')

def show_printed_models(printed_designs):
    print('The following models have been printed: \n')
    for printed_design in printed_designs:
        print(printed_design)

print_design()
show_printed_model(printed_desegins)
