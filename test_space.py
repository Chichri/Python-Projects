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

print('\n')


magicians = ["Chris_Angel", "David_Copperfield", "Harry_Houdini"]
great_magicians = []

def show_magicians(magicians):
    for magician in magicians:
        print(magician)

show_magicians(magicians)

print('\n')

def make_great(magicians=magicians):
    for i in range(len(magicians)):
        magicians[i] = "The Great " + magicians[i]
        great_magicians.append(magicians[i])

make_great(magicians[:])
show_magicians(magicians)
print('\n')
show_magicians(great_magicians)

print('\n')

def make_great(magicians=magicians):
    for i in range(len(magicians)):
        magicians[i] = "The Great " + magicians[i]

make_great()
show_magicians(magicians)

print('\n')

def make_sandwich(*ingrediants):
    print('Making a sandwich with')
    for ingrediant in ingrediants:
        print('-' + ingrediant)

make_sandwich('lettuce','tomato')
make_sandwich('lettuce','tomato','bacon')
make_sandwich('lettuce','tomato', 'bacon','mayo')

print('\n')

def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('Cole', 'Lameyer',
location = 'Bay Area',
occupation = 'student',
age = '16')

print(user_profile)

def make_car(make, model, **features):
    car_info = {}
    car_info['Company'] = make
    car_info['Model'] = model
    for key, value in features.items():
        car_info[key] = value
    return car_info

car = make_car('Toyota','corrola', cheap = 'yes', airbag = 'maybe')
print(car)

print('\n')

class Restaurant():
    def __init__(init,name, cusine_type, numbers_served):
        init.name = name
        init.cusine_type = cusine_type
        init.numbers_served = numbers_served


    def describe_restaurant(init):
        print('The restaurant ' + init.name.title() + ' does ' +
        init.cusine_type.title() + '-style cusine.' + ' It has served ' +
        str(init.numbers_served) + ' people.')

    def open_restaurant(init):
        print('The restaurant ' + init.name.title() + ' is open.')

    def set_served(init, served):
        init.numbers_served = served

    def increment_served(init, people):
        init.numbers_served += people


los_cabalos = Restaurant('los cabalos', 'mexican', 0)
los_cabalos.set_served(143)
los_cabalos.increment_served(23)
los_cabalos.describe_restaurant()
los_cabalos.open_restaurant()
print(los_cabalos.name.title())
print(los_cabalos.cusine_type.title())
noodle_theroy = Restaurant('noodle theroy', 'thai-fusion', 0)
noodle_theroy.describe_restaurant()

print('\n')

class User():
    def __init__(init,first_name,last_name,user_name,login_attempts):
        init.first_name = first_name
        init.last_name = last_name
        init.user_name = user_name
        init.login_attempts = login_attempts

    def describe_user(init):
        print(init.first_name.title() + ' ' + init.last_name.title() +
        ' goes by ' + init.user_name + '. ' + str(init.login_attempts) + ' login attempts')

    def greet_user(init):
        print('Hello, ' +  init.first_name.title() + ' ' + init.last_name.title())

    def increment_logins(init):
        init.login_attempts += 1

    def reset_logins(init):
        init.login_attempts = 0

parzial = User('wade', 'watts', 'parzial', 0)
parzial.increment_logins()
parzial.describe_user()
parzial.reset_logins()
parzial.describe_user()
parzial.greet_user()

print('\n')

class IceCreamStand(Restaurant):
    def __init__(init, name, cuisine_type, numbers_served):
        super().__init__(name, cuisine_type, numbers_served)
        init.flavors =  []

    def stand(init):
        print(init.name, 'serves:')
        for flavor in init.flavors:
            print(flavor)


test = IceCreamStand('Smitten', 'ice cream', 0)
test.flavors = ['chocolate', 'vanilla', 'strawberry']
test.stand()

print('\n')

class Admin(User):
    def __init__(init,first_name,last_name,user_name,login_attempts):
        super().__init__(first_name,last_name,user_name,login_attempts)
        init.privileges = []

    def show_privileges(init):
        print(init.user_name + ' can:')
        for privilege in init.privileges:
            print(privilege)

ogg = Admin('oggden', 'morrow', 'The Great and Powerful Ogg', 0)
ogg.privileges = ['can edit', 'can ban', 'can monitor chat']
ogg.show_privileges()

print('\n')

class Car():
    def __init__(self, make, model, year, odometer):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = odometer

class Ebattery():
    def __init__(self, ebattery_size = 70):
        self.ebattery_size = ebattery_size

    def describe_ebattery(self):
        print('This car has a ' + str(self.ebattery_size) + ' kW ebattery.')

    def get_range(self):
        if self.ebattery_size == 70:
            range = 240
        elif self.ebattery_size == 80:
            range = 290
        message = ("This car has a range of " + str(range) + ' miles.')
        print(message)

    def update_battery(self):
        self.ebattery_size = 80

class ElectricCar(Car):
    def __init__(self, make, model, year, odometer):
        super().__init__(make, model, year, odometer)
        self.battery_size = 70
        self.ebattery = Ebattery()

    def describe_battery(self):
        print('This car has a ' + str(self.battery_size) + ' kW battery')

temp = ElectricCar('toyota', 'corola','1950', 0)
temp.ebattery.describe_ebattery()
temp.ebattery.update_battery()
temp.ebattery.describe_ebattery()

print('\n')

from collections import OrderedDict

glossary = OrderedDict()

glossary['ephemeral'] = 'temporary or insubstatial'
glossary['opulent'] = 'lavish, expensive'
glossary['gruntled'] = 'pleased, content'

for word, definition in glossary.items():
    print(word + ' means ' + definition)

print('\n')

from random import randint

class Die():
    def __init__(self, sides):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))

    def roll_10x(self):
        results = []
        for roll_num in range(10):
            result = randint(1, self.sides)
            results.append(result)
        print(results)



d6 = Die(6)
d6.roll_die()
d6.roll_10x()
d10 = Die(10)
d10.roll_die()
d10.roll_10x()
d20 = Die(20)
d20.roll_die()
d20.roll_10x()
