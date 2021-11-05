from abstract.AbcGeneretorPassword import AbcGenPass
import templates_symbols.template_letters
from templates_symbols.template_letters import TemplateSymbols, LetterUpper, LetterLower, Digits, Symbols
from inspect import isclass
from random import shuffle, randint


class GenPass(AbcGenPass):

    def __init__(self, length_pswd=6,  **kwargs):
        super().__init__(length_pswd=length_pswd, **kwargs)

    def write_password_to_file(self, cnt_pswd=1, file=open("new_password", "w")):
        try:
            for _ in range(cnt_pswd):
                file.write(self.make_password() + "\n")
            file.close()
        except Exception:
            print("Ошибка при записи в файл")

    def show(self):
        for k, v in self.__symb_pass.items():
            print(f"key = {k} value = {v}")

