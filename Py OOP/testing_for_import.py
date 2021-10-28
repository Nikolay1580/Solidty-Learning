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
        print(f"This car has a mileage of {self.odometer}")

    def change_odometer(self):
        self.odometer = self.milage

    def increment_odometer(self):
        for i in range(3):
            self.odometer += self.milage


class Dog:

    # we gave the dog some properties which almost all real life dogs have.
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    # giving the dog function or ability. In this case it will be to sit and roll. Functions inside classes are called methods.
    def sit(self):
        print(f"{self.name} is now sitting")

    def roll(self):
        print(f"{self.name} just rolled over!")


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
