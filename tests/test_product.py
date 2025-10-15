def test_product_init(product1, product2):
    """Тестируем инициализацию продукта"""

    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.price == 180000.0
    assert product1.quantity == 5

    assert product2.name == '55" QLED 4K'
    assert product2.description == "Фоновая подсветка"
    assert product2.price == 123000.0
    assert product2.quantity == 7


def test_product_str(product1):
    assert str(product1) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_product_add(product1, product2):
    assert product1 + product2 == 1761000.0
