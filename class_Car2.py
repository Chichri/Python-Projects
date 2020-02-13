class Car2():
    def __init__(self, make, model, year, odometer):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = odometer

    def set_odometer(self, mileage):
        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print("You can't roll back the odometer")

    def update_odometer(self, miles):
        if miles >= 0:
            self.odometer += miles
        else:
            print("You can't roll back the odometer")

    def get_descriptive_name(self):
        long_name = str(self.year) +  ' ' + self.make.title() + ' ' + self.model.title()
        return long_name

    def read_odometer(self):
        print('This car has ' + str(self.odometer) + ' miles on it.')

class Ebattery2():
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

class ElectricCar2(Car2):
    def __init__(self, make, model, year, odometer):
        super().__init__(make, model, year, odometer)
        self.battery_size = 70
        self.ebattery = Ebattery2()

    def describe_battery(self):
        print('This car has a ' + str(self.battery_size) + ' kW battery.')
