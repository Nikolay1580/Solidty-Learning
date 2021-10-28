import random


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


# lets make an instance
a_dog = Dog("john", 34, "Hunagrian, Vizlas")

print(a_dog.breed)

a_dog.sit()
# by using the dot we are giving it atributes, in this case they are the name, age, breed and the two methods.


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


restaurant = Restaurant("Nik's", "Italian")

restaurant.desrcibe()


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


my_car = Car("Skoda", "Octavia", "2021")

my_car.read_odometer()

# changing the value of le car
my_car.odometer = 32

# different output should be given
my_car.read_odometer()

"""
    In total there are 3 ways to modify Atrbitue values 
    #1 Directly modyfying it   
        Example: my_car.odometer = 32
    #2 Modifying through a Method 
        Example: line 59
    #3 Incrementing through Methods
        Example: line 62
"""

my_car.increment_odometer()
my_car.read_odometer()
