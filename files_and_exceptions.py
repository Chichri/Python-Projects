with open('/Users/cole/Desktop/Coding_Projects/Python-Projects/pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)

#Text files can store large amounts of data, so it is useful to enable your -
#-programs to read them
#The open() function is neccsiary to open any file to do anything with it
#open() returns an object representing the file, which is stored in file_object
#Once we have file_object, contents is assigned to the string in file_object -
#- through the use of the read() method. Then contents is printed
