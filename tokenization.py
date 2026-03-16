# Simple lexical analyzer for Python code

keywords = ["if","else","while","for","def","return","print","int","float"]
operators = ['+','-','*','/','=','>','<']
special_symbols = ['(',')','{','}','[',']',':',',']

file = open("sample.py","r")
code = file.read()

tokens = code.split()

for token in tokens:

    if token in keywords:
        print(token,"-> Keyword")

    elif token in operators:
        print(token,"-> Operator")

    elif token in special_symbols:
        print(token,"-> Special Symbol")

    elif token.isdigit():
        print(token,"-> Literal")

    elif token.startswith('"') or token.startswith("'"):
        print(token,"-> String")

    else:
        print(token,"-> Identifier")
