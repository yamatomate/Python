# desafio 86 fazendo uma matriz 3x3
from random import randint
l = linha = []
c = coluna = []
co = 0
li = 0
for co in range(0, 3):
    for li in range(0, 3):
        #linha.append(int(input(f"Digite um numero -Li{li} | {co}Co- >> ")))
        linha.append(randint(1,100))
    print(l)
    c.append(l[:])
    l.clear()
for co in range(0, 3):
    for li in range(0, 3):
        if li%2 == 0:
            print(f'{c[co][li]}', end='')
        else:
            print(f' | {c[co][li]} | ', end='')
    print('\n', end='')
    