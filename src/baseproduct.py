from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный класс"""

    @abstractmethod
    def __add__(self, other):
        pass
