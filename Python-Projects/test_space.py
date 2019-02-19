#Try out space: Unexplained examples of things you can do in python

hero = "Martin Luther King Jr "
quote = ' "I have a dream "'
A_wise_mans_proclamation = hero + "once said" + quote
print(A_wise_mans_proclamation)

names = ['Milo', 'Phoenix', 'Peter', 'Emma']
print(names[0])
print(names[1])
print(names[2])
print(names[3])

places = ['Japan', 'Amsterdam', 'Castine', 'Dubai', 'Mt_View']
print(places)

print("\n")

print(sorted(places))

print("\n")

print(places)

print("\n")

print(sorted(places, reverse = True))

print("\n")

print(places)

print("\n")

places.reverse()
print(places)

print("\n")

places.reverse()
print(places)

print("\n")

places.sort()
print(places)

print("\n")

places.sort(reverse = True)
print(places)

print("\n")

car = 'subaru'
print(car == 'subaru')

print("\n")

alien_color = 'blue'
if alien_color == 'green':
    print("5 points achived")
if alien_color != 'green':
    print("10 points achived")

print("\n")

usernames = ['Tehdude', 'Robloxkidd9', 'Vartaxxx', 'Parzival', 'Admin']

for username in usernames:
    if username == "Admin":
        print("Hello Admin, Welcome back. Would you like a status report?")
    else:
         print("Hello " + username + ", Welcome back")

print("\n")

current_users = ["test", "test1", 'test2', 'test3', 'test4' ]

new_users = ['test1.0', 'test1', 'test5', 'test6']

for new_user in new_users:
    if new_user in current_users:
        print("Sorry, but that name is taken")
    else:
        print('The username ' + new_user + ' is available')

print("\n")

ordinal_numbers = list(range(1,10))

for num in ordinal_numbers:
    if num == 1:
        print('1st')
    if num == 2:
        print('2nd')
    if num == 3:
        print('3rd')
    elif num > 3:
        print(str(num) + 'th')

print("\n")

Hank = {'first_name': 'Hank', 'last_name': 'Anderson', 'city': 'Detroit'}

print("Lieutenant " + Hank['first_name'] + ' ' + Hank['last_name'] +
" lives in the city of " + Hank['city'])

print("\n")

rivers = {'egypt': 'nile', 'west virgina': 'potomac', 'india': 'ganges' }

for key, value in rivers.items():
    print('The '+ value.title() + ' runs through ' + key.title())
