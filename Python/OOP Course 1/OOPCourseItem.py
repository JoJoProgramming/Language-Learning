import csv

class Item:

    payRate = 0.8 #item cost after 20% discount
    allItems = []

    def __init__(self, name: str = "", price: float = 0, quantity: int = 0):
        #validations for received arguments
        assert price >= 0, f"Price {price} is not greater than 0!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than 0!"
        #assign to self instance
        self.__name = name
        self.__price = price
        self.quantity = quantity
        #actions to execute
        Item.allItems.append(self)  

    @property
    def price(self):
        return self.__price

    def apply_discount(self):
        self.__price = self.__price * self.payRate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        while len(value) > 10:
            value = input("This name is too long, please try again: ")
        else:
            self.__name = value


    def __determine_price(self):
        if self.name == "Phone":
            self.__price = 100
        elif self.name == "Laptop":
            self.__price = 1000

    def determine_discount(self):
        if self.name == "Phone":
            self.payRate = .8
        elif self.name == "Laptop":
            self.payRate = .7
        else:
            print("This option is invalid.")



    
    @classmethod
    def initiate_from_csv(cls):
        with open('C:\Programs\Learning\Python\OOP Course CSV.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name = item.get('name'),
    
                price = float(item.get('price')),
                quantity = int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(x):
        try:
            float(x)
            return True
        except:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}('Name: {self.name}, Price: {self.__price}, Quantity: {self.quantity}')"
    

