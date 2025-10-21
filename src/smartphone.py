from src.product import Product


class Smartphone(Product):

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.model = model
        self.color = color
        self.efficiency = efficiency
        self.memory = memory

    def __add__(self, other):
        if type(other) is Smartphone:
            return self.name + other.name
        raise TypeError
