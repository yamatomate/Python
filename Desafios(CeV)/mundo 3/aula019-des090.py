# deasfio 90 boletim com dicionario

b = boletim = {}
b['nome']  = str(input("Digite o nome do aluno: "))
b['media'] = float(input(f"Digite a média de {b['nome']}: "))
if b['media'] >= 7:
    b['situação'] = 'Aprovado'
elif 5 <= b['media'] < 7:
    b['situação'] = 'Recuperação'
else:
    b['situação'] = 'Reprovado'
for k, v in b.items():
    print(f'{k} é igual a {v}')
print(b)
