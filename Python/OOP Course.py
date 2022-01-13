class Item:
    #__init__ method is called automatically when an instance of the class is built
    #parameters given to init are mandatory. parameter variables can be set during initialization
    #as seen with quantity=0 in the argument line.
    def __init__(self, name, price, quantity=0):
        #creates name attribute for the created instance and assigns it to the variable passed into
        #the init method via argument name
        self.name = name
        self.price = price
        self.quantity = quantity
    #the self in the below method refers to the object itself being passed into the method;
    #EG item1 is passed into method calculate_total_price as the first argument
    #self must be included for methods in a classs
    def calculate_total_price(self, x, y):
        return x * y


item1 = Item("Phone",100)
phoneQuantity = input("How many phones do you want? ")
phoneQuantity = int(phoneQuantity)
item1.quantity = phoneQuantity
item2 = Item("Laptop",1000,3)
print(item1.name)
print(item2.name)
print(item1.quantity)
print(item2.quantity)
print(item1.price)
print(item2.price)