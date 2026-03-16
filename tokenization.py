# Simple lexical analyzer for Python code

keywords = ["if","else","while","for","def","return","print","int","float"]
operators = ['+','-','*','/','=','>','<']
separators = ['(',')','{','}','[',']',':',',']

file = open("sample.py","r")
code = file.read()

tokens = code.split()

for token in tokens:

    if token in keywords:
        print(token,"-> Keyword")

    elif token in operators:
        print(token,"-> Operator")

    elif token in separators:
        print(token,"-> Separator")

    elif token.isdigit():
        print(token,"-> Number")

    else:
        print(token,"-> Identifier")
