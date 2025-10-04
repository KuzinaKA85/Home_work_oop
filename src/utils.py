import json
import os

from src.product import Product
from src.category import Category


def read_json(path: str) -> dict:
    """ Функция читает файл json """
    full_path = os.path.abspath(path)
    with open(full_path, 'r', encoding='UTF-8') as file:
        data = json.load(file)
    return data


def create_objects_from_json(data: dict) -> list:
    """ Функция создает объекты классов Product и Category """

    categories = []
    for category in data:
        products = []
        for prod in category['products']:
            products.append(Product(**prod))
        category['products'] = products
        categories.append(Category(**category))
    return categories


if __name__ == '__main__':
    raw_data = read_json('../data/products.json')
    categories_data = create_objects_from_json(raw_data)
    print(categories_data)
