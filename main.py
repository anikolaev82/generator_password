from templates_symbols.template_letters import LetterLower, LetterUpper, Digits, Symbols, TemplateSymbols
from genpass import GenPass


pswd = GenPass(13, l1=LetterUpper, l2=2, l4=Symbols)
for _ in range(10):
    print(pswd.make_password())

