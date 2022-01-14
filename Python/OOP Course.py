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
    def __repr__(self):
        return f"Item('Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}')"
itemPhone = Item("Phone", 100, 1)
itemLaptop = Item("Laptop", 1000, 3)
itemCable = Item("Cable", 10, 5)
itemMouse = Item("Mouse", 50, 5)
itemKeyboard = Item("Keyboard", 75, 5)
print(Item.allItems)