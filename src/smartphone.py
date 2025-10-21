from src.product import Product


class Smartphone(Product):
    """ Класс-наследник, описывающий свойства продукта"""

    efficiency: float
    model: str
    memory: int
    color: str

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра"""

        super().__init__(name, description, price, quantity)
        self.model = model
        self.color = color
        self.efficiency = efficiency
        self.memory = memory

    def __add__(self, other) -> None:
        if type(other) is Smartphone:
            return self.name + other.name
        raise TypeError
