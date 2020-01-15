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
