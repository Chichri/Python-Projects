with open('Desktop/Coding_Projects/Python-Projects/pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)

#Text files can store large amounts of data, so it is useful to enable your -
#-programs to read them
#The open() function is neccsiary to open any file to do anything with it
#open() returns an object representing the file, which is stored in file_object
#Once we have file_object, contents is assigned to the string in file_object -
#- through the use of the read() method. Then contents is printed
#I don't know why I had to list the path, only the file name should be required
#open() is supposed to search the directory the program is in for the file
#Keep in mind that diffrent machines/os's store files diffrently
#Sometimes it's useful to store path's to variables for easy distinction

print('\n')

file_path = 'Desktop/Coding_Projects/Python-Projects/pi_digits.txt'
with open(file_path) as file_object:
    for line in file_object:
        print(line)
#Sometimes you'll want to check each line of whats written in a file
#You might be looking for information or trying to modify the text
#Either way, a simple for loop can cycle through an entire file instantly
#(This is also an example of tying a filename/filepath to a vairable)

print('\n')

with open(file_path) as file_object:
    lines = file_object.readlines()
    for line in lines:
        print(line.rstrip())
#You'll notice that open() is continuing to need to be called to work
#This is because after the code excutes its purpose, the file is closed
#This is done to avoid complications and can be triggered manually with close()
#To work with the contents of a file after it's closed, they must be copied
#This can be done with the method readlines()
#readlines() copies lines within a file to a list, which persists after closing

print('\n)')

pi_string = ' '
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))
#This block of code works with the saved contents of pi_digits.txt
#Empty list pi_string is created to hold the each line of the text from lines
#Expect the lines have been stripped of right-ward whitespace with rstrip
#This is just a simple example of how we can work the the contents of a file

print('\n')

birthday = input('Enter your birthday in mmddyy format')
if str(birthday) in pi_string:
    print('Your birthday is in the first 30 digits of pi. Litteraly how.')
else:
    print('Your birthday is not in the first 30 digits of pi. Shocker.')
#Here's a classic, finding your birthday in the digits of pi
#This is done classicaly with the first million digits of pi, but I was lazy
#Either way, it's extremly simple to pick out specific occurances of text

print('\n')

filename = 'programing.txt'
with open(filename, 'w') as file_object:
    file_object.write('I like programing.')
with open(filename) as file_object:
    contents = file_object.read()
    print(contents)
#The file 'programing.txt' did not exist on my machine until I ran This
#open() will automatically create a called file if it does not exist
#Here, the opened file is another text file, empty because it's new
#Notice that open() here has two arguements
#The 'w' opens the file in write mode, where it can be modified with write()
#Without that second argument, open() defaults to read mode, as shown above
#Be careful with write mode: if the file already exists, it will be erased upon-
#- the returning of the file object

print('\n')

with open(filename, 'a') as file_object:
    file_object.write(' I also like music!')

with open(filename) as file_object:
    contents = file_object.read()
    print(contents)
#Providing the secondary argument 'a' opens the file in append mode
#This allows content to be added to a file without overwriting the contents
#Append mode does not erase the file after file_object is returned
#But write mode will create the file if it doesn't exist like write mode

print('\n')

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
#This is a try-except block
#try-except handle exceptions, objects created when your program crashs
#These exceptions divert the program so that it keeps running
#Here, an impossible operation is attempted (5/0)
#This produces the exception object ZeroDivisionError, which crashs the program
#Instead of a crash, we give it instructions of what to do to continue running
#In this case, the error instructions are to print 'You can't divide by zero'

print('\n')

print("Give me two numbers and I' divide them\n")
print("Enter 'q' to quit")

while True:
    first_number = input("First number: \n")
    if first_number == 'q':
        break
    second_number = input("Second number: \n")
    if second_number == 'q':
        break
    answer = int(first_number) / int(second_number)
    print(answer)
#This code is a simple division calculator
#With no error handling, the ZeroDivisionError will appear if second_number = 0
#Worse still, this appears in the traceback which is printed to the console
#tracebacks are meant to help you and only you to debug the programing
#tracebacks will confuse non-technical users and help attacks hack you program
#Therefore, you shouldn't let them appear in the final product

print('\n')

print("Let's do it again. Give me two numbers and I' divide them\n")
print("Enter 'q' to quit")

while True:
    first_number = input("First number: \n")
    if first_number == 'q':
        break
    second_number = input("Second number: \n")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero")
    else:
        print(answer)
#This is the same calculator, but with a try-except-else block on it
#Here, we check for errors in the answer, with an exception given just in case
#Upon a ZeroDivisionError being encountered, we print the previous error message
#Then we provide an else, or what the program should do with no error

print('\n')

filename = 'nonexistent.txt'
try:
    with open(filename) as file_object:
        contents = file_object.read()

except FileNotFoundError:
    msg = "Sorry, " + filename + " does not exist."
    print(msg)
#The FileNotFoundError is an extremly common error
#This error occurs either when the file doesn't exist or the path is incorrect
#Remeber: no tracebacks for the audience

print('\n')

filename = 'programing.txt'
with open (filename) as file_object:
    contents = file_object.read()
    words = contents.split()
    count = len(words)
    print('The file ' + filename + ' has approximatly ' + str(count) + ' words')
#We can do much more woth text using the split.() method
#split.() seperates text by spaces,storing the text between spaces in a list
#with the individual chunks of text, we can extricate words and work with them
#for example, we can count the words with len() and print that back output

print('\n')

path = 'Desktop/Coding_Projects/Python-Projects/'
def count_words(filname):
    with open(filename) as file_object:
        contents = file_object.read()
        words = contents.split()
        count = len(words)
        print('The file ' + filename + ' has approximatly '
        + str(count) + ' words')

filenames = [ path + 'pi_digits.txt', path+ 'programing.txt']
for filename in filenames:
    count_words(filename)
#Until now, we've only been using open to work with individual files
#This can be changed easily by using open() in a function
#That way, we can work with multipe files in one line

print('\n')

filename = 'nonexistent.txt'
try:
    with open(filename) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    pass
#Sometimes, even when you expect a certain error, you don't want to work with it
#pass allows an except block to have no output, to "fail silently"
#Sometimes the user doesn't need to know every kink in the program

print('\n')

import json

numbers = [1,2,3,4,5,6,7,8,9]

filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)
#This block of code uses the JSON module
#JSON (Javascript Object Notation) format was develped for Javascript, but has-
#- become common in many languages, including python
#The JSON module is quite useful for storing data within files
#The file is declared with the json file extension because it's customary
#json.dump() is a function that takes two arguments, some data and a file
#it then simply stores the data within that file in a "dump" of information
#This file has no output, but we've now stored numbers in numbers.json

print('\n')

with open(filename) as f_obj:
    numbers2 = json.load(f_obj)

print(numbers2)
#This code uses json.load(), allmost the extact opposite of json.dump()
#json.load() takes only one argument, the file
#It then load the data into wherever it is being assigned to

print('\n')

username = input('What is your name?')

filename = 'username.json'
with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)
    print("We'll remember you when you come back, " + username + '.\n')

print('\n')

query = input("Whats your name?")

with open(filename) as f_obj:
    checklist = json.load(f_obj)
if query in checklist:
    print("Yes, I remember you, you're " + query + "!")
else:
    print("No, I don't believe we've met before.")
#Here's an example of using both json.dump() and json.load() in conjunction
#Nothing particularly new, but note how they work so well together
#If you can't tell, I'm skimming the textbook a bit here

print('\n')

def ask():
    username = input('What is your username?')

    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("We'll remember you when you come back, " + username + '.\n')

def check():
    query = input("Whats your username?")

    with open(filename) as f_obj:
        checklist = json.load(f_obj)
    if query in checklist:
        print("Yes, I remember you, you're " + query + "!")
    else:
        print("No, I don't believe we've met before.")
#This is an example of refactoring
#Refactoring is when you take a program and break it down into function
#By doing this, you can improve the logic of the code and make it clearer
#It also aids the tracebacks and the debuging of the program as a whole
#when possible, refactor. No one wants large unwieldy blocks of code
