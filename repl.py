from parser import parser
from interpreter import interp

def repl(prompt='lis.py> '):
    "A prompt-read-eval-print loop."
    while True:
        val = interp(parser.parse(input(prompt)))
        if val is not None: 
            print(lispstr(val))

def lispstr(exp):
    "Convert a Python object back into a Lisp-readable string."
    if isinstance(exp, list):
        return '(' + ' '.join(map(lispstr, exp)) + ')' 
    else:
        return str(exp)

repl()
