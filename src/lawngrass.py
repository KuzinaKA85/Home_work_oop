from src.product import Product


class LawnGrass(Product):
    """ Класс-наследник, описывающий свойства продукта"""

    country: str
    germination_period: str
    color: str

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра"""

        super().__init__(name, description, price, quantity)
        self.germination_period = germination_period
        self.color = color
        self.country = country

    def __add__(self, other) -> None:
        if type(other) is LawnGrass:
            return (self.price * self.quantity) + (other.price * other.quantity)
        raise TypeError
