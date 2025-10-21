from src.product import Product


class LawnGrass(Product):

    def __init__(self, name, description, germination_period, color, price, quantity, country):
        super().__init__( name, description, price, quantity)
        self.germination_period = germination_period
        self.color = color
        self.country = country

