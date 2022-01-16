from OOPCourseItem import Item

class Phone(Item):
    def __init__(self, name: str = "", price: float = 0, quantity: int = 0, broken_phones: int = 0):
        super().__init__(name, price, quantity)
        self.broken_phones = broken_phones
        #actions to execute
        Phone.allItems.append(self)
    def __repr__(self):
        return f"{self.__class__.__name__}('Name: {self.name}, Price: {self.__price}, Quantity: {self.quantity}, Broken: {self.broken_phones}')"