# Simple Lexical Analyzer

def lexical_analyzer(text):
    state = 0
    token = ""

    for ch in text + " ":   # add space to process last token
        
        # State 0 : Start state
        if state == 0:
            if ch.isalpha():
                state = 1
                token += ch
                print("State 0 -> State 1 (Identifier start)")
            
            elif ch.isdigit():
                state = 2
                token += ch
                print("State 0 -> State 2 (Number start)")
            
            elif ch in "+-*/=":
                print("Operator:", ch)
            
            elif ch.isspace():
                continue

        # State 1 : Identifier
        elif state == 1:
            if ch.isalnum():
                token += ch
            else:
                print("Identifier:", token)
                token = ""
                state = 0
                print("State 1 -> State 0")
                
                if not ch.isspace():
                    if ch in "+-*/=":
                        print("Operator:", ch)

        # State 2 : Number
        elif state == 2:
            if ch.isdigit():
                token += ch
            else:
                print("Number:", token)
                token = ""
                state = 0
                print("State 2 -> State 0")
                
                if not ch.isspace():
                    if ch in "+-*/=":
                        print("Operator:", ch)


# Input program
text = input("Enter expression: ")
lexical_analyzer(text)
