class Dog():
    """A simple atempt to model a dog."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting"""
        print(self.name.title() + ' is now siting!')

    def roll_over(self):
        """Simulate a dog rolling over."""
        print(self.name.title() + ' rolled over!')

my_dog = Dog('willie', 6)
print("My dog's name is " + my_dog.name.title() + '.')
print("My dog is " + str(my_dog.age) + ' years old.')
#This is a class. Classes are used to simulate real-world things and situations
#To do this, we write objects which define the genral behavior of the class
#Making an object is called instantation, making an instance of the class
#my_dog is an instance of the class Dog. The parameters will be explained bellow
#A function in a class is a Method. Methods mostly act like normal functions -
#- except for in the fashion that you call them.
#The __init__ method is a special method within python that runs automatically -
#- without being called.
#In __init__, self is passed automatically as well, meaning you only have to -
#- provide arguments for the last two parameters, age and name.
#The two variables defined at 4 are prefixed with self. Because of this, they -
#- are available to every method in the class and any instance of the class.
#Variables that are accessible through instances like this are called attributes
#Attributes within an instance are accesed by dot notation like in my_dog
#There are two other methods in Dog, sit and roll_over. They only need to be -
#called with the parameter self after we set an instance of Dog with the two -
#parameters for name and age. This is due to __init__ for complicated reasons

print('\n')
my_dog.sit()
my_dog.roll_over()
#This is how methods called. When calling a method, you give the name of the -
#-instance, and the method you want to call, separated by a dot.
#The method then takes the parameters of the instance and applies it to itself

print('\n')

your_dog = Dog('lucy', 3)
print('Your dogs name is ' + your_dog.name.title() + '.')
print('Your dog is ' + str(your_dog.age) + ' years old.')
your_dog.sit()
your_dog.roll_over()
#There is no limit on how many instances can be created
#The only rule is that each instance needs a unique variable name or a unique -
#-spot on whatever list or dictionary

print('\n')

class Car():
    def __init__(self, make, model, year, odometer):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = odometer

    def set_odometer(self, mileage):
        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print("You can't roll back the odometer")

    def update_odometer(self, miles):
        if miles >= 0:
            self.odometer += miles
        else:
            print("You can't roll back the odometer")

    def get_descriptive_name(self):
        long_name = str(self.year) +  ' ' + self.make.title() + ' ' + self.model.title()
        return long_name

    def read_odometer(self):
        print('This car has ' + str(self.odometer) + ' miles on it.')

my_car = Car('audi','a4', 2016, 0)
print(my_car.get_descriptive_name())
my_car.read_odometer()
my_car.update_odometer(3)
my_car.update_odometer(-2)
my_car.read_odometer()
my_car.set_odometer(23)
my_car.set_odometer(12)
my_car.read_odometer()
#class Car stores in variables to describe a car, including the odometer
#odometers change overtime and therefore, the attribute needs to be modifiable
#This is achived through methods update_odometer and set_odometer
#update_odometer adds the arguemen given to variable miles to self.odometer
#set_odometer changes the value of self.odometer to the arguement given
#note that an if else statement checks whether mileage is smaller then odometer
#This is because odometers are one-way and should not be reversable
#Conditions like these are easily applicable to methods

print('\n')

class Ebattery():
    def __init__(self, ebattery_size = 70):
        self.ebattery_size = ebattery_size

    def describe_ebattery(self):
        print('This car has a ' + str(self.ebattery_size) + ' kW ebattery.')

    def get_range(self):
        if self.ebattery_size == 70:
            range = 240
        elif self.ebattery_size == 80:
            range = 290
        message = ("This car has a range of " + str(range) + ' miles.')
        print(message)

class ElectricCar(Car):
    def __init__(self, make, model, year, odometer):
        super().__init__(make, model, year, odometer)
        self.battery_size = 70
        self.ebattery = Ebattery()

    def describe_battery(self):
        print('This car has a ' + str(self.battery_size) + ' kW battery.')


my_tesla = ElectricCar('tesla', 'model s', 2016, 0)
print(my_tesla.get_descriptive_name())
my_tesla.read_odometer()
#This is an example of inheritance
#Inheritance is the making a version of another class
#the new class will has the same attributes and methods, but can also add more
#The class thats doing the inheriting is called the child class, or subclass
#The class being inherited is called the parent class, or superclass
#in refrence to superclasses, the super() function is a special function
#super() links the parent class to the child class, callng init for ElectricCar
#Now, any instance of ElectricCar has access to the attributes of Car

print('\n')

my_tesla.describe_battery()
#This method utilizes an attriute that is unique to ElectricCar
#Adding attributes and method for customization is trivial as shown above

my_tesla.ebattery.describe_ebattery()
#When modeling objects, you may find your list of attributes becoming long
#Sometimes, some attributes may be grouped together for orginization
#This call uses an attribute declared in another class tied to class ElectricCar

my_tesla.ebattery.get_range()
#This method is like the one above, stored within another class
#Seeing as it ties directly in with the battery, it makes sense to include it -
#-in the separate class

print('\n')

from class_Car2 import Car2

my_new_car = Car2('audi','a4', 2016, 0)
print(my_new_car.get_descriptive_name())
#Like functions, classes can be imported from files as well
#Car2 is identical to Car, the name changed to avoid a naming issue
#The output is the exact same as the method called from class Car earlier

print('\n')

from class_Car2 import Ebattery2, ElectricCar2
import class_Car2

my_new_car2 = ElectricCar2('audi','a4', 2016, 0,)
print(my_new_car2.get_descriptive_name())
my_new_car3 = class_Car2.ElectricCar2('audi','a4', 2016, 0,)
print(my_new_car3.get_descriptive_name())
#Multiple classes can also be imported from modules as well
#You could also just import the entire module an call objects with dot notation

print('\n')

from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jen']= 'python'
favorite_languages['sarah']= 'c'
favorite_languages['edward']= 'ruby'
favorite_languages['phil']= 'python'

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title())
#OrderedDict is a class from the Python Standard Library
#Modules from the standard library can be imported with any Python install
#OrderedDict is a class that creates a Dictionary that keeps track of the order-
#- in which the key-pairs were added
#No curly brakets are needed because the dictionary is created by the class

#Classes are always named in CamelCaps, which is capitalizing the first letter-
#- of each word and having no underscores between them
#Instances and modules should have names that follow function styling, all -
#lowercase with underscores between words
#Imports should allways be at the top of the file in practice, and imports from-
#the Python Standard Library should go first before modules you've written
#Python Standard Library import lines should be separated from personal modules-
#-by a line of blank space
#
