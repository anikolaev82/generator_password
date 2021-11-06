from genpass import GenPass
from templates.letterlower import LetterLower
from templates.letterupper import LetterUpper
from templates.digits import Digits
from templates.symbols import Symbols

param = {
        "p": LetterUpper,
        "p2":LetterLower,
        "p3":Symbols,
        "p4":Digits
    }

pswd = GenPass(9, **param)

for _ in range(10):
    print(pswd.make_password())

print(pswd.to_json(5000))
