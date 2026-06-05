#TAC DATA STRUCTURES
# Input
exprs = []
while True:
    s = input()
    if s == 'done': break
    exprs.append(s)

tac = []
temp = 1

# TAC generation (simple split-based)
for line in exprs:
    l, r = line.split('=')
    l, r = l.strip(), r.strip().split()

    if len(r) == 1:
        tac.append(f"{l} = {r[0]}")
    else:
        t = f"t{temp}"; temp += 1
        tac.append(f"{t} = {r[0]} {r[1]} {r[2]}")
        tac.append(f"{l} = {t}")

# Print TAC
print("\nTAC:")
for i in tac: print(i)

# Quadruples
quad = []
for line in tac:
    l, r = line.split('=')
    l = l.strip(); r = r.strip().split()
    if len(r)==1:
        quad.append(('=', r[0], '-', l))
    else:
        quad.append((r[1], r[0], r[2], l))

print("\nQuadruples:")
for q in quad: print(q)

# Triples
trip = []
temp_map = {}

for i,(op,a,b,res) in enumerate(quad):
    if a in temp_map: a = f"({temp_map[a]})"
    if b in temp_map: b = f"({temp_map[b]})"
    trip.append((op,a,b))
    temp_map[res] = i

print("\nTriples:")
for i,t in enumerate(trip): print(i,t)

# Indirect Triples
print("\nIndirect Triples:")
for i,t in enumerate(trip): print(i,t)

# Assembly
print("\nAssembly:")
for line in tac:
    l,r = line.split('=')
    l = l.strip(); r = r.strip().split()
    if len(r)==1:
        print(f"MOV {l}, {r[0]}")
    else:
        print(f"MOV {l}, {r[0]}")
        if r[1]=='+': print(f"ADD {l}, {r[2]}")
        if r[1]=='-': print(f"SUB {l}, {r[2]}")
        if r[1]=='*': print(f"MUL {l}, {r[2]}")
        if r[1]=='/': print(f"DIV {l}, {r[2]}")
