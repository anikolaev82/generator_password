from abc import ABC
from inspect import isclass
from random import shuffle, choice
from interface.abctemplate import AbcTemplate


class AbcGenPass(ABC):
    __symb_pass = ()

    def __init__(self, length_pswd: int = 6,  **kwargs):
        if length_pswd < len(kwargs):
            length_pswd = len(kwargs)
        self.__length_pswd = length_pswd
        temp = []
        for v in kwargs.values():
            if isclass(v) and issubclass(v, AbcTemplate):
                temp.append(v())
        self.__symb_pass = temp

    def get_classes(self):
        return [i.class_name for i in self.__symb_pass]

    def __get_template_password(self):
        template_password = []
        while len(template_password) < self.__length_pswd:
            template_password.append(choice(self.__symb_pass))
            shuffle(template_password)
        return template_password

    def make_password(self):
        new_password = []
        template_password = self.__get_template_password()
        for i in template_password:
            new_password.extend(i.get_random())
        shuffle(new_password)
        return ''.join(new_password)
