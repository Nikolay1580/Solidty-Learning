import random


class Car:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        # we set an object with a preexisting value
        self.odometer = 0
        self.milage = 40

    def read_odometer(self):
        print(f"This {self.model} has a mileage of {self.odometer}")

    def change_odometer(self):
        self.odometer = self.milage

    def increment_odometer(self):
        for i in range(3):
            self.odometer += self.milage

# inheritence is so that we can build off new objects off of older ones to not constantly rewrite code.
# the new class is the child class whhile the og is the parent class
# now we make a class called electric car


"""
    Ignore until line x
    We see that electric cars have a lot of properties for their batteries so why not create another class called battery 
"""


class Battery:

    def __init__(self, battery_size):
        self.battery = battery_size

    def describe_battery(self):
        print(
            f"This battery has {self.battery} Killowats of power!")


class Electric_car(Car):

    # recalling the __init__ from the parent class
    def __init__(self, brand, model, year):
        # Alows us to use them
        super().__init__(brand, model, year)
        # assign atributes for the child class
        self.battery = Battery(60)

    """
    def describe_battery(self):
        print(f"This car has a battery capacity of {self.battery} Killowatts")
    """


# make an instance ]
my_car = Electric_car("Tesla", "Model S", "2020")

my_car.read_odometer()
my_car.battery.describe_battery()


class Restaurant:

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine = cuisine_type
        self.numbers_served = 0

    def desrcibe(self):
        print(
            f"The restaurant name is {self.name} and serves {self.cuisine} food!")

    def open(self):
        print(f"The restuarant is currently open")

    def set_number_served(self):
        self.numbers_served = random.randrange(0, 100)


class Ice_cream_stand(Restaurant):

    def __init__(self, name, cuisine_type, flavour):
        super().__init__(name, cuisine_type)
        self.flavour = flavour
        self.serve = Restaurant

    def show_flavour(self):
        print(f"The falvour of your ice cream is {self.flavour}")


niks_ice = Ice_cream_stand("Nik's ice", "Bulgarian", "chocolate")

niks_ice.show_flavour()
