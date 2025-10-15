from src.category import Category


def test_category_init(category1, category2):
    """Тестируем инициализацию категории продукта"""

    assert category1.name == "Смартфоны"
    assert (
        category1.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert len(category1.products_in_list) == 3

    """Тестируем подсчет количества категорий"""
    assert category1.category_count == 2
    assert category2.category_count == 2

    """Тестируем подсчет количества продуктов"""
    assert category1.product_count == 4
    assert category2.product_count == 4


def test_products_property(category2):
    assert category2.products == '55" QLED 4K, 123000.0 руб. Остаток: 7 шт.\n'


def test_category_products_setter(category1, product2):
    assert len(category1.products_in_list) == 3
    category1.products_in_list = product2
    assert len(category1.products_in_list) == 4


def test_product_str(category1):
    assert str(category1) == "Смартфоны, количество продуктов: 27 шт."
