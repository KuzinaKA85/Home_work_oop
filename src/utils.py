import json
import os
from typing import Any

from src.category import Category
from src.product import Product


def read_json(path: str) -> dict[Any, Any]:
    """Функция читает файл json"""
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="UTF-8") as file:
        data = json.load(file)
    return data


def create_objects_from_json(data: dict) -> list:
    """Функция создает объекты классов Product и Category"""

    categories = []
    for category in data:
        products = []
        for prod in category["products"]:
            products.append(Product(**prod))
        category["products"] = products
        categories.append(Category(**category))
    return categories
