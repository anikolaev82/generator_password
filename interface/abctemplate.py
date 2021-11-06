from random import choices
from abc import ABC


class AbcTemplate(ABC):
    _symbols = ''

    def __init__(self):
        if not isinstance(self._symbols, str):
            raise Exception("Value is not string")
        if len(self._symbols) == 0:
            raise Exception("Empty template")
        self.__list_symbols = list(self._symbols)

    def get_symbols(self):
        return self.__list_symbols

    def get_random(self, weigth=1):
        return list(choices(self.get_symbols(), k=weigth))

    @property
    def class_name(self):
        return self.__class__.__name__

    def __str__(self):
        return f"Class {self.__class__.__name__}, value {self.get_symbols()}"

