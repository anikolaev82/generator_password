from templates_symbols.template_letters import TemplateSymbols
from abc import ABC
from inspect import isclass
from random import shuffle, randint, choice


class AbcGenPass(ABC):
    __symb_pass = {}

    def __init__(self, length_pswd: int = 6,  **kwargs):
        if length_pswd < len(kwargs):
            length_pswd = len(kwargs)
        self.__length_pswd = length_pswd
        for v in kwargs.values():
            if isclass(v) and issubclass(v, TemplateSymbols):
                self.__symb_pass.setdefault(v, v())

    def __get_template_password(self):
        values = list(self.__symb_pass.values())
        template_password = values
        while len(template_password) < self.__length_pswd:
            template_password.append(choice(values))
            shuffle(template_password)
        return template_password

    def make_password(self):
        new_password = []
        template_password = self.__get_template_password()
        for i in template_password:
            new_password.extend(i.get_random())
        shuffle(new_password)
        return ''.join(new_password)

