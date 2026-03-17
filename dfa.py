code = input("Enter code: ")
keywords = ["if", "else", "while", "do"]
operators = ["==", "+", "-", "*", "/", "=", "<", ">"]
i = 0
n = len(code)
while i < n:
    if code[i].isspace():
        i += 1
        continue
    # IDENTIFIER / KEYWORD (show transitions)
    if code[i].isalpha():
        lexeme = ""

        while i < n and code[i].isalpha():
            if lexeme != "":
                print("{" + lexeme[-1] + "} -> {" + code[i] + "}")
            lexeme += code[i]
            i += 1

        if lexeme in keywords:
            print("{" + lexeme + "} -> KEYWORD")
        else:
            print("{" + lexeme + "} -> IDENTIFIER")
        continue
    # NUMBER (digit transitions)
    if code[i].isdigit():
        num = ""

        while i < n and code[i].isdigit():
            if num != "":
                print("{" + num[-1] + "} -> {" + code[i] + "}")
            num += code[i]
            i += 1

        print("{" + num + "} -> NUMBER")
        continue
    # MULTI-CHAR OPERATOR (==)
    if i + 1 < n and code[i:i+2] in operators:
        print("{" + code[i:i+2] + "} -> OPERATOR")
        i += 2
        continue
    # SINGLE OPERATOR
    if code[i] in operators:
        print("{" + code[i] + "} -> OPERATOR")
        i += 1
        continue
    # UNKNOWN
    print(code[i], "-> UNKNOWN")
    i += 1
