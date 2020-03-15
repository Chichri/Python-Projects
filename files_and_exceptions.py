with open('/Users/cole/Desktop/Coding_Projects/Python-Projects/pi_digits.txt') as file_object:
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

file_path = '/Users/cole/Desktop/Coding_Projects/Python-Projects/pi_digits.txt'
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
if birthday in pi_string:
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
