# Домашнее задание по ООП
## Описание
Интернет-магазин
## Установка
Клонируйте репозиторий: https://github.com/KuzinaKA85/Home_work_oop
## Установите зависимости:
- `pip install flake8`
- `pip install black`
- `pip install mypy`
- `pip install isort`
- `pip pytest`

## Реализованный функционал
1. Реализован класс Product
- Для класса Product определены следующие свойства:
название (name), описание (description), цена (price), количество в наличии (quantity).

2. Реализован класс Category
- Для класса Category определены следующие свойства:
название (name), описание (description),список товаров категории (products).

3. Реализован класс Smartphone
- класс-наследник от класса Product, расширен следующими свойствами: производительность (efficiency), модель (model), объем встроенной памяти (memory), цвет (color).

4. Реализован класс LawnGrass
- класс-наследник от класса Product, расширен следующими свойствами: страна-производитель (country), срок прорастания (germination_period), цвет (color).

5. В модулях ***main.py*** реализван код для проверки работы модулей ***product.py***, ***category.py***, ***utils.py***, ***product_iterator.py***, ***smartphone.py***, ***lawngrass.py***.

## Функции приложения
1. Функция ***read_json*** используется для чтения json-файла.

2. Функция ***create_objects_from_json*** создает объекты классов Product и Category.

 
## Тестирование модулей
Для тестирования модулей введите в терминале:
- ` pytest tests/test_product.py`
- ` pytest tests/test_category.py`
- ` pytest tests/test_product_iterator.py`
- ` pytest tests/test_smartphone.py`
- ` pytest tests/test_lawngrass.py`
