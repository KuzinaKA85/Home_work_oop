from src.product import Product


class Smartphone(Product):

    def __init__(self, name, model, color, description, efficiency, memory, price, quantity):
        super().__init__(name, description, price, quantity)
        self.model = model
        self.color = color
        self.efficiency = efficiency
        self.memory = memory

    def __add__(self, other):
        if type(other) is Smartphone:
            return self.name + other.name
        raise TypeError


