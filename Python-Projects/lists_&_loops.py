phones = ['Apple','Samsung','Android']
for phone in phones:
    print(phone)
#For takes values in your list and assigns them to a variable
#This variable will then be looped for whatever task you gave it for each list values
#Looping in this fashion is extremly useful for elimnating reption in code
#Always indent when using for: failing to do so will produce errors

print("\n")
#It should be noted that I don't want this to loop, therfore its not indented

for phone in phones:
#Because of that print("\n"), I have to repeat that
#However, this allows my loops to separate, making it easier to read/compare

    print(phone +" is a company that makes phones")
    print("I can't wait to see " + phone + "'s' next phone" + "\n")
#for loops can be used for a variety of puropses and works with concatenation
#(That last term is pronounced con-cat-nation)

print("I wish razer phones were cheaper and more mainstream")
#Since this line isn't indented, it is not looped, much like the print("\n") above

print("\n")

for value in range(1,6):
    print(value)
#The range function generates a seires of numbers within the range dictated
#range will not generate the second number picked, stopping at the penultimante

print("\n")

numbers = list(range(1,6))
print(numbers)
#The list function can encompas a range and convert it directly to a list
#This is useful when dealing with lists with unwieldy lengths

even_numbers = list(range(2,11,2))
print(even_numbers)
#range can be maniuplated to affect the numbers it produces
#The 3rd # in range's parentheses will be added to each value, skipping to the sum
#Starting from an even number and adding 2, the range will now produce even numbers
#If we were to start from an odd number, the range would produce only odds

print("\n")

squares = []
for value in range(1, 11):
     square = value**2
     squares.append(square)

print(squares)
#The range function can be configured to produce almost any set of numbers
#In the program above, we made the var square to equal var value squared
#Python understands exponents as two asterisks followed by the exponent
#Here, value is each number produce by the range (1-10)
#Therefore square becomes the square of each number
#Finally, append fills the premade list until the last value is calculated
#Var square is uneccessary, but it makes for good demonstration

print("\n")

digits = list(range(1,11))
print(digits)
print(min(digits))
print(max(digits))
print(sum(digits))
#Statistics on a range can be easily detrmined through a number of functions
#The min, max, and sum functions all do exactlly what they sound like
#Don't forget to print the results if you want them to appear in the output
