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

def print_design(unprinted_designs, printed_designs):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print('Printing model: ' + current_design)
        printed_designs.append(current_design)

print('\n')

def show_printed_models(printed_designs):
    print('The following models have been printed: \n')
    for printed_design in printed_designs:
        print(printed_design)

unprinted_designs = ['D20', 'Master Sword', 'Bootleg Amibo']
printed_designs = []

print_design(unprinted_designs, printed_designs)
show_printed_models(printed_designs)
#In the previous segement, the function passed a list. What else can we do?
#Here, two lists are defined at the head of the segement
#Then, we write the first function, which passes and modifies the lists
#The second function prints the newly filled list

print('\n')

print_design(unprinted_designs[:], printed_designs)
#This little repeat doesn't do anything, it just demostrates slice notation
#slice notation duplicates a list for the use of a function,
#If a function modifies a list but you want it to remain intact, this is useful

print('\n')

def make_pizza(*toppings):
    print(toppings)

make_pizza('pepperoni')
make_pizza('pepperoni','olives','mushrooms')
#Notice that so far, arguments have been exact, any devation creating an error
#What if we don't know how many arguments they function will handle?
#Then we can make the function pass an arbitrary amount of arguements
#The '*' infront of the parameter lets it pass diffrent amount of arguements
#Note that these values are packed into a tuple, so no list attributes

print('\n')

def make_pizza(size, *toppings):
    print('Making a ' + str(size) + '-inch pizza with the following toppings:')
    for topping in toppings:
        print('-' + topping)

make_pizza(12, 'pepperoni')
print('\n')
make_pizza(16, 'pepperoni','olives','mushrooms')
#Positional and arbitrary arguments can be mixed, as shown above
#This can be used to handle a wide variety of situations

print('\n')

def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein', location = 'prinston',
field = 'physics')

print(user_profile)
#Sometimes, you'll want to pass an arbitrary argument without knowing the type-
#of data that you'll be reciving. This can be handled with a '**' parameter
#The '**' tells python to make an empty dictionary to store the vaules in as -
#oppsed to a tuple. Then, you can pack whatever name value pairs you want in it
#Then, once the dict'profile' is set up, you can give it any of the unforseen -
#key, value pairs that come from dict'user_info'. Handy!

print('\n')

import pizza

pizza.make_pizza(16, 'pepperoni', 'cheese')
#Okay, this is going to get complex
#Pizza is a module, a seperate file that you import into the current file
#Pizza.py only contains the make_pizza function from early, but importing pizza-
#-allows us to use all the code in that file as if it were in this oneself.
#This allows us to break up segements of code and let the master program focus -
#-on the true logic of the code
#functions in the module are called via the module_name.function_name() format
#you can also specifically import individual function from a module using this -
#format, from module_name import function_name,
#Functions imported in this manner do not need the module name before the call

from pizzas import make_pizza, make_pizza2, make_pizza3

make_pizza(16, 'pepperoni', 'cheese')
make_pizza2(16, 'pepperoni', 'cheese')
make_pizza3(16, 'pepperoni', 'cheese')
#You can also call multiple function using from by separating them with commas

from pizza import make_pizza as mp

mp(16, 'pepperoni', 'cheese')
#Here, we are using an alias
#Sometimes the name of an imported function will conflict with another function
#In this case, we use 'as' to asign it a nickname that we can use when calling

import pizza as p
#Modules can also be aliased
#Now, make_pizza would be called as p.make_pizza()
#Although the original would stil work seeing as we keep
