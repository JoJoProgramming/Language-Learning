class Item:
    def __init__(self, name: str, price: float, quantity: int = 0):
        #validations for received arguments
        assert price >= 0
        assert quantity >= 0
        #assign to self instance
        self.name = name
        self.price = price
        self.quantity = quantity
    def calculate_total_price(self):
        return self.price * self.quantity


item1 = Item("Phone",100)
item1Quant = input("How many phones do you want? ")
item1Quant = int(item1Quant)
item1.quantity = item1Quant
print(item1.calculate_total_price())