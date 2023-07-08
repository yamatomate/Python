dados = ["Pedro", 25]
pessoas = []
pessoas.append(dados[:])
dados = ["Maria", 34]
pessoas.append(dados[:])
print(pessoas)

pessoas = [["Pedro", 25], ["Maria", 34], ["josefino", 66], ["zeze", 2]]
for p in pessoas:
    print(f'nome:{p[0]} e idade:{p[1]}')
    print(p)
ma = pessoas[0][1]

print(ma)