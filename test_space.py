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

print('\n')

print('A deli makes sandwichs')
print('\n')

sandwich_orders = ['Reuben', 'BLT', 'Grilled Cheese', 'Burger', 'Ham']
finished_sandwichs = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print('The ' + sandwich + ' is almost done')
    finished_sandwichs.append(sandwich)

print('\n')

while finished_sandwichs:
    finished_sandwich = finished_sandwichs.pop()
    print('The ' + finished_sandwich + ' is finished')


print('\n')

print('Today is a new day. The deli has run out of pastrami')
print('\n')

sandwich_orders2 = ['Pastrami', 'Grilled Cheese', 'Burger', 'Ham', 'Pastrami']
finished_sandwichs2 = []

while 'Pastrami' in sandwich_orders2:
    sandwich_orders2.remove('Pastrami')

while sandwich_orders2:
    sandwich2 = sandwich_orders2.pop()
    print('The ' + sandwich2 + ' is almost done')
    finished_sandwichs2.append(sandwich2)

print('\n')

while finished_sandwichs2:
    finished_sandwich2 = finished_sandwichs2.pop()
    print('The ' + finished_sandwich2 + ' is finished')

print('\n')

paris_total = 0
houston_total = 0
tokyo_total = 0

print('A poll on popular vaction destinations is issued')
print('\n')


poll = {'Joey': 'Paris', 'Alica': 'Tokyo', 'Chris': 'Paris', 'Sarah': 'Houston',
'Kian': 'Tokyo', 'Pablo': 'Paris'}

results = poll
print(results)

print('\n')

for place in poll.values():
    if place == 'Paris':
        paris_total += 1
    if place == 'Tokyo':
        tokyo_total += 1
    if place == 'Houston':
        houston_total += 1

if paris_total > tokyo_total and paris_total > houston_total:
    print('It seems that Paris is the most popular destination')
elif tokyo_total > paris_total and tokyo_total > houston_total:
    print('It seems that Tokyo is the most popular destination')
elif houston_total > paris_total and houston_total > tokyo_total:
    print('It seems that Houston is the most popular destination')

print('\n')

def display_message():
    print('In this chapter, I am learning about functions')

display_message()

def favorite_book(book):
    print('My favorite book is ' + book.title() + '!')

favorite_book('dune')

print('\n')

def make_shirt(size, text):
    print('To confirm, you want a size ' + size + ' t-shirt with the message: '
    + text + ' printed on it?')

make_shirt('large', 'all my vices are devices')

make_shirt(size='small', text='YEET')

def make_shirt(size='Large', text='I love Python!'):
    print('To confirm, you want a size ' + size + ' t-shirt with the message: '
    + text + ' printed on it?')

make_shirt()

print('\n')

def city_country(city, country):
    print(city.title() + ', ' + country.title())

city_country('oakland', 'usa')
city_country('pointe a pitre', 'guadelopue')
city_country('berlin', 'germany')

magicians = ['Chris Angel', 'David Copperfield', 'Harry Houdini']

def show_magicians(magicians):
    for magician in magicians:
        print(magician)

show_magicians(magicians = magicians)
