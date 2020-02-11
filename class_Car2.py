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
