# Simple Assembly Code Generator

expr = input("Enter expression: ").split()

reg = 1
stack = []
code = []

for token in expr:
    if token not in '+-*/':
        r = f"R{reg}"; reg += 1
        code.append(f"MOV {r}, {token}")
        stack.append(r)
    else:
        r2 = stack.pop()
        r1 = stack.pop()

        if token == '+': code.append(f"ADD {r1}, {r2}")
        if token == '-': code.append(f"SUB {r1}, {r2}")
        if token == '*': code.append(f"MUL {r1}, {r2}")
        if token == '/': code.append(f"DIV {r1}, {r2}")

        stack.append(r1)

print("\nAssembly Code:")
for i in code:
    print(i)

print("\nFinal result in", stack[-1])
