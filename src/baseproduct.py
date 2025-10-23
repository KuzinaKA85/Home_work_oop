from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """ Абстрактный класс """

    def __add__(self, other):
        pass