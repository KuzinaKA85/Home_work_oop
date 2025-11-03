from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный класс для всех продуктов"""

    @abstractmethod
    def __add__(self, other):
        pass
