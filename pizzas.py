def make_pizza(size, *toppings):
    print('Making a ' + str(size) + '-inch pizza with the following toppings:')
    for topping in toppings:
        print('-' + topping)

def make_pizza2(size, *toppings):
    print('Making another ' + str(size) + '-inch pizza with the following toppings:')
    for topping in toppings:
        print('-' + topping)

def make_pizza3(size, *toppings):
    print('Making a third ' + str(size) + '-inch pizza with the following toppings:')
    for topping in toppings:
        print('-' + topping)
