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
#This is because after the code excutes it's purpose, the file is closed
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
