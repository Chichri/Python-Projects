cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.lower())
#If statements are used to excute things based on whether conditions are True
#This statement prints bmw in upper case if bmw is on the list, which it is

print("\n")

test = 'True'
if test == 'True':
    print("True")
print(test == "True")
#This is a basic Conditional Test, also known as a Boolean expression
#The = operator assigns values. The == operator checks if value assigned is true
#In this fashion, an if statement can be shorted to withn the print function

print("\n")

lies = "something"
if lies != "something else":
    print("J'accuse!")
print(lies != "something eles")
#Adding a ! to the = operator makes it check whether the value assigned is false

print("\n")

if 'audi' in cars:
    print("An audi is a brand of car")
#In can be used to check whether a value is on a list

print("\n")

if 'Microsoft' not in cars:
    print("Microsoft does not make cars .... yet")
#not can be used to check whether a value is not on a list

print("\n")

dairy = ['Milk', 'Cheese']
if 'Milk' and 'Cheese' in dairy:
    print("Dairy products are tasty")
#and can be used to check multiple things at once

print("\n")

age = 18
if age <= 18:
    print("You are of voting age")
else:
    print("You are too young to vote")
#This is an else if statemnt. It provides other outcomes for the if statements
#This produces the first message. Lowering var 'age' changes it to the second

print("\n")

height = 6

if height > 6:
    print("You are too short for this ride")
elif height < 6:
    print("you are two tall for this ride")
elif height == 6:
    print("You can go on this ride")
else:
    print("You cannot go on this ride")
#This is an elif chain. Essentially an else if statement with multiple "ifs"
#The code evalutes each if untill it reach on the fits the requirements
#The code then skips the rest
#The else is not needed, unless a catch-all for the unforseen is needed

print("\n")

whatever = 5

if whatever == 5:
    print("Whatever")
if whatever > 3:
    print("Whatever 2: electric boogalo")
if whatever < 6:
    print("Whatever the third")
#if chains like these check multiple conditions and produce multiple outcomes
#Always omit the else on this type of chains

print("\n")

requested_toppings = ['mushrooms', 'peppers', 'olives']

for requested_topping in requested_toppings:
    if requested_topping == 'peppers':
        print("Sorry, we're out of peppers")

else:
    print("Adding " + requested_topping + ".")
