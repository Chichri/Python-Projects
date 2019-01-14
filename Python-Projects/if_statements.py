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
