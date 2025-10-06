def test_category_init(category1, category2):
    """Тестируем инициализацию категории продукта"""

    assert category1.name == "Смартфоны"
    assert (
        category1.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert len(category1.products) == 3

    """Тестируем подсчет количества категорий"""
    assert category1.category_count == 2
    assert category2.category_count == 2

    """Тестируем подсчет количества продуктов"""
    assert category1.product_count == 4
    assert category2.product_count == 4
