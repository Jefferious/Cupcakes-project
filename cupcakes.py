from abc import ABC, abstractmethod
import csv
from pprint import pprint
def read_csv(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            pprint(row)

# read_csv("sample.csv")

class Cupcake(ABC):
    size = "regular"
    def __init__(self, name, price, flavor, filling, frosting):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.filling = filling
        self.frosting = frosting
        self.sprinkles = []

    def add_sprinkles(self, *args):
        for sprinkle in args:
            self.sprinkles.append(sprinkle)

    @abstractmethod
    def calculate_price(self, quantity):
        return quantity * self.price

# my_cupkake = Cupcake("Sunshine and rainbows", 2.99, "Red Velvet", "Strawberry jam", 'Chocholate')

# my_cupkake.add_sprinkles("Chocolate", "Toffee bits", "Yellow")

# print(my_cupkake.sprinkles)

class Mini(Cupcake):
    size = 'Mini'
    def __init__(self, name, price, flavor, filling, frosting):
        super().__init__(name, price, flavor, filling, frosting)
    
    def calculate_price(self, quantity):
        return quantity * self.price
    
class Regular(Cupcake):
    size = 'Regular'
    def __init__(self, name, price, flavor, filling, frosting):
        super().__init__(name, price, flavor, filling, frosting)
    
    def calculate_price(self, quantity):
        return quantity * self.price
    
class Large(Cupcake):
    size = 'Large'
    def __init__(self, name, price, flavor, filling, frosting):
        super().__init__(name, price, flavor, filling, frosting)
    
    def calculate_price(self, quantity):
        return quantity * self.price
    
cupcake_1 = Large("Orange", 4.99, "Orange peel", "Orange jam", "Orange cream cheese")
cupcake_1.add_sprinkles("Orange")
cupcake_2 = Mini("Super flowers", 1.49, "Poppy seed", "cherry syrup", "vanilla")
cupcake_3 = Regular("Pop", 2.99, "Poppy seed", "Bannana", "White cream cheese")
cupcake_4 = Large("Double Chocolate", 4.99, "chocolate", "chocolate", None)
cupcake_4.add_sprinkles("Strawberry")
cupcake_5 = Regular("Bland", 2.99, "Lemon", "Sand", "Sand")
# print(cupcake_2.flavor)
cupcake_list = [
    cupcake_1,
    cupcake_2,
    cupcake_3,
    cupcake_4,
    cupcake_5
]
def write_new_csv(file, cupcakes):
    with open(file, "w", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "filling", "sprinkles", "frosting"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for cupcake in cupcakes:
            if hasattr(cupcake, "filling"):
                writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "filling": cupcake.filling, "sprinkles": cupcake.sprinkles})
            else:
                writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles})

write_new_csv("sample.csv", cupcake_list)

def add_cupcake(file, cupcake):
    with open(file, "a", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if hasattr(cupcake, "filling"):
            writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "filling": cupcake.filling, "sprinkles": cupcake.sprinkles})
        else:
            writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles})

def get_cupcakes(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        reader = list(reader)
        return reader

def find_cupcake(file, name):
    for cupcake in get_cupcakes(file):
        if cupcake["name"] == name:
            return cupcake
        return None

def add_cupcake_dictionary(file, cupcake):
    with open(file, "a", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(cupcake)

def read_csv(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            pprint(row)