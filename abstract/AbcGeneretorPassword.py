from templates_symbols.template_letters import TemplateSymbols
from abc import ABC
from inspect import isclass
from random import shuffle, randint


class AbcGenPass(ABC):
    __symb_pass = {}

    def __init__(self, length_pswd: int = 6,  **kwargs):
        self.__length_pswd = length_pswd
        for v in kwargs.values():
            if isclass(v) and issubclass(v, TemplateSymbols):
                self.__symb_pass.setdefault(v, v())

    def __get_template_password(self):
        len_cls = len(self.__symb_pass)
        count_ever_cls = self.__length_pswd // len_cls
        odd = self.__length_pswd - count_ever_cls * len_cls
        template_password = [count_ever_cls for i in range(len_cls)]
        for _ in range(odd):
            template_password[randint(0, len_cls - 1)] += 1
        return template_password

    def make_password(self):
        new_password = []
        template_password = self.__get_template_password()
        try:
            for i, cls in enumerate(self.__symb_pass.values()):
                new_password.extend(cls.get_random(template_password[i]))
            shuffle(new_password)
            return ''.join(new_password)
        except ZeroDivisionError:
            print("Не выбраны символы для пароля")



