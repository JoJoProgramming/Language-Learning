class Item:
    pay_rate = 0.8 #item cost after 20% discount
    def __init__(self, name: str = "", price: float = 0, quantity: int = 0):
        #validations for received arguments
        assert price >= 0, f"Price {price} is not greater than 0!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than 0!"
        #assign to self instance
        self.name = name
        self.price = price
        self.quantity = quantity
    def determine_price(self):
        if self.name == "Phone":
            self.price = 100
    def calculate_total_price(self):
        self.price = self.price * self.quantity
    def apply_discount(self):
        self.price = self.price * Item.pay_rate


item1 = Item()
item1.name = input("What do you want to buy? ")
item1.determine_price()
item1.quantity = int(input("How many phones do you want to buy? "))
item1.calculate_total_price()
item1.apply_discount()
print(item1.price)

