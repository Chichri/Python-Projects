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
#A function in a class is a Method. Methods mostly act like normal fucntions
#The __init__ method is a special method within python that runs automatically
#__init__ is used to initialize 
