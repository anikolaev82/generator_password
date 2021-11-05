from templates_symbols.template_letters import LetterLower, LetterUpper, Digits, Symbols
from genpass import GenPass

param = {
        "p": LetterUpper,
        "p2":LetterLower,
        "p3":Symbols
    }

pswd = GenPass(13, **param)

for _ in range(10):
    print(pswd.make_password())

pswd.write_password_to_file(100)