import templates_symbols.template_letters
from templates_symbols.template_letters import TemplateSymbols, LetterUpper, LetterLower, Digits, Symbols
from abc import ABC, abstractmethod
from inspect import isclass
from random import shuffle, randint


class GenPass(ABC):
    __symb_pass = {}

    def __init__(self, length_pswd=6,  **kwargs):
        self.__length_pswd = length_pswd
        for v in kwargs.values():
            if isclass(v) and issubclass(v, TemplateSymbols):
                self.__symb_pass.setdefault(v, v())

    def get_templ_password(self):
        len_cls = len(self.__symb_pass)
        count_ever_cls = self.__length_pswd // len_cls
        odd = self.__length_pswd - count_ever_cls * len_cls
        if odd < 0:
            raise Exception("Ошибка, обратить к администратору")
        template_password = [count_ever_cls for i in range(len_cls)]
        for _ in range(odd):
            template_password[randint(0, len_cls - 1)] += 1
        return template_password

    def make_password(self):
        new_password = []
        template_password = self.get_templ_password()
        try:
            for i, cls in enumerate(self.__symb_pass.values()):
                new_password.extend(cls.get_random(template_password[i]))
            shuffle(new_password)
            return ''.join(new_password)
        except ZeroDivisionError:
            print("Не выбраны символы для пароля")

    def show(self):
        for k, v in self.__symb_pass.items():
            print(f"key = {k} value = {v}")

