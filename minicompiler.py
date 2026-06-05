# Simple MINI Compiler Phases

import re

expr = input("Enter expression (a = b + c * d): ")

# 1. Lexical Analysis
tokens = re.findall(r'\w+|[=+*/()-]', expr)
print("\nTokens:", tokens)

# 2. Syntax (assume correct input)
lhs = tokens[0]
rhs = tokens[2:]

# 3. Semantic (simple type check)
print("\nSemantic: All variables assumed int")

# 4. Intermediate Code (TAC)
tac = []
temp = 1

if len(rhs) == 1:
    tac.append(f"{lhs} = {rhs[0]}")
else:
    t = f"t{temp}"
    tac.append(f"{t} = {rhs[0]} {rhs[1]} {rhs[2]}")
    tac.append(f"{lhs} = {t}")

print("\nTAC:")
for i in tac: print(i)

# 5. Optimization (Constant Folding)
opt = []
for line in tac:
    parts = line.split()
    if len(parts)==5 and parts[2].isdigit() and parts[4].isdigit():
        val = eval(parts[2]+parts[3]+parts[4])
        opt.append(f"{parts[0]} = {val}")
    else:
        opt.append(line)

print("\nOptimized TAC:")
for i in opt: print(i)

# 6. Target Code
print("\nAssembly:")
for line in opt:
    parts = line.split()
    if len(parts)==5:
        print(f"LOAD {parts[2]}")
        if parts[3]=='+': print(f"ADD {parts[4]}")
        if parts[3]=='-': print(f"SUB {parts[4]}")
        if parts[3]=='*': print(f"MUL {parts[4]}")
        if parts[3]=='/': print(f"DIV {parts[4]}")
        print(f"STORE {parts[0]}")
    else:
        print(f"LOAD {parts[2]}")
        print(f"STORE {parts[0]}")
