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
