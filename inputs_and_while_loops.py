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
else:
    print('False')
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

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
#This is a while loop
#While loops run each line of the loop while the condition is true
#This is handy for loops that need to trigger for multiple conditions

print('\n')

prompt = "remember the first program? It's back but now you can quit it"
prompt += "\nEnter 'quit' to end the program\n"
space = ''

while space != 'quit':
    space = input(prompt)
    print(space)
#This while loop runs infintely until it is given the string value 'quit'
#This works by assigin var space as an empty string
#The loop then checks the string each time, before print the users Input
#If the input is quit, the program ends. Elsewise, it prints to the console

print('\n')

prompt2 = "Third times the charm, right?"
prompt2 += "\nEnter 'quit' to end the program\n"
active = True
while active:
    space = input(prompt2)

    if space == 'quit':
        active = False
    else:
        print(space)
#The code above is identical to the previous segment, with once change
#Here we used a vairiable named active. This vairiable serves as a Flag
#Flags are vairiables that remain true/false under myraid conditions
#They are used as a tripwires to dectect changes in input and react to them

print('\n')

prompt3 = "Apparently the third time didn't do it. Here we go again."
prompt3 += "\nEnter 'quit' to end the program\n"

while True:
    entry = input(prompt3)
    if entry == 'quit':
        break
    else:
        print(entry)
#Once again, this section repeats what input is given to it
#However, this time it uses break to exit the inifinte loop
#When a loop starts with 'while True', it will run until it enounters a break
#Here break is ran when the string equal 'quit', exiting the loop

print('\n')

current_number2 = 0
while current_number2 < 10:
    current_number2 += 1
    if current_number2 % 2 ==0:
        continue

    print(current_number2)
#This is a segement of code from previous in the program
#Here, we have a vairable 'current_number2' assgined to zero
#current_number2 is increased by one, then checked for whether it's even or not
#If it is, the continue is ran, which restarts the loop from the beginning
#Since the print is put after the continue, only odd numbers are printed

print('\n')
