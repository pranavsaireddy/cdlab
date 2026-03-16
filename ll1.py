ll1 = {
'E': {'id':['T','E1'],'(':['T','E1']},
'E1':{'+':['+','T','E1'],')':[],'$':[]},
'T':{'id':['F','T1'],'(':['F','T1']},
'T1':{'*':['*','F','T1'],'+':[],')':[],'$':[]},
'F':{'id':['id'],'(':['(','E',')']}
}

def parse(tokens):
    stack=['$','E']
    tokens=tokens+['$']
    i=0

    while stack:
        top=stack.pop()
        cur=tokens[i]

        if top==cur:
            i+=1

        elif top in ll1 and cur in ll1[top]:
            stack+=ll1[top][cur][::-1]

        else:
            return False

    return i==len(tokens)

print("id + id * id:",parse(['id','+','id','*','id']))
print("id + * id:",parse(['id','+','*','id']))
