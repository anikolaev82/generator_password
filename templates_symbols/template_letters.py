from random import choices
from abc import ABC


class TemplateSymbols(ABC):
    symbols = ''

    def __init__(self):
        if len(self.symbols) == 0:
            raise Exception("Не указаны символы")
        self.list_symbols = list(self.symbols)

    def get_symbols(self):
        return self.list_symbols

    def get_random(self, weigth=1):
        return list(choices(self.get_symbols(), k=weigth))

    def __str__(self):
        return self.__class__.__name__


class LetterUpper(TemplateSymbols):
    symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


class LetterLower(TemplateSymbols):
    symbols = 'abcdefghijklmnopqrstuvwxyz'


class Digits(TemplateSymbols):
    symbols = '0123456789'


class Symbols(TemplateSymbols):
    symbols = '!@#$%^&*()-_=+'
