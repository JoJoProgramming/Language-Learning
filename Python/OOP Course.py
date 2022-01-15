import csv

class Item:

    payRate = 0.8 #item cost after 20% discount
    allItems = []

    def __init__(self, name: str = "", price: float = 0, quantity: int = 0):
        #validations for received arguments
        assert price >= 0, f"Price {price} is not greater than 0!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than 0!"
        #assign to self instance
        self.name = name
        self.price = price
        self.quantity = quantity
        #actions to execute
        Item.allItems.append(self)  

    def determine_price(self):
        if self.name == "Phone":
            self.price = 100
        elif self.name == "Laptop":
            self.price = 1000

    def determine_discount(self):
        if self.name == "Phone":
            self.payRate = .8
        elif self.name == "Laptop":
            self.payRate = .7
        else:
            print("This option is invalid.")

    def calculate_total_price(self):
        self.price = self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.payRate
    
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
        return f"Item('Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}')"

class Phone(Item):
    pass

phone1 = Phone("jscPhonev10", 500, 5)
phone1.broken_phones = 1
phone2 = Phone("jscPhonev20", 700, 5)
phone2.broken_phones = 1