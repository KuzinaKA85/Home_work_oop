from src.product import Product


class Category:
    """Класс, описывающий категорию продуктов"""

    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра"""

        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self):
        return f"{self.name}, количество продуктов: {sum(product.quantity for product in self.__products)} шт."

    def add_product(self, product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1

    @property
    def products(self):
        products_str = ""
        for product in self.__products:
            products_str = f"{str(product)}\n"
        return products_str

    @products.setter
    def products(self, new_product: Product):
        self.__products.append(new_product)
        Category.product_count += 1

    @property
    def products_in_list(self):
        return self.__products

    @products_in_list.setter
    def products_in_list(self, product: Product):
        self.__products.append(product)
        Category.product_count += 1
