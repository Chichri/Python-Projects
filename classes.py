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
