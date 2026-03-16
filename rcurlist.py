import re

def parse(tokens):
    token = tokens.pop(0)

    if token == '[':
        lst = []
        while tokens[0] != ']':
            lst.append(parse(tokens))
        tokens.pop(0)
        return lst
    else:
        return int(token)


def print_tree(node, level=0):
    if isinstance(node, list):
        print("  "*level + "List")
        for child in node:
            print_tree(child, level+1)
    else:
        print("  "*level + str(node))


text = "[1 2 [3 4] 5]"

tokens = re.findall(r'\[|\]|\d+', text)

tree = parse(tokens)

print_tree(tree)
