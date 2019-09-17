message = input("tell me something and i'll repeat it to you\n")
print(message)
#This is the input fuction. It stores input from the user to a vairiable

print('\n')

name = input('Please enter your name\n')
print('Hello ' + name.title() + '!')
#The input function has many versitile uses. Here, it askes for a name.

print('\n')

age = input('How old are you?\n')
age = int(age)
if age >= 5:
    print('True')
#Remeber to coveret your input to int if you want to work with integers

print('\n')

if 5 % 3 == 2:
    print("True")
#In python, '%' is the Modulo operator. It returns the remainder of two numbers

print('\n')

number = input("Input a number and i'll tell you if it's even or odd\n")
number = int(number)
if number % 2 == 0:
    print(str(number) + ' is an even number.')
else:
    print(str(number) + ' is an odd number')
#Here, we've used the modulo operator to check if a number is even or odd
#We can do this becasue the remained of an even number divided by two is zero
#Therefore, an if statement alows us to check if the remainder is zero or not

print('\n')
