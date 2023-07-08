# desafio 86 fazendo uma matriz 3x3
from random import randint
l = linha = []
c = coluna = []
sompares = sp = 0
sotecol = s3c = 0
maiseli = msl = 0
for co in range(0, 3):
    for li in range(0, 3):
        #linha.append(int(input(f"Digite um numero -Li{li} | {co}Co- >> ")))
        linha.append(randint(1,100))
        if co == 1 and l[li] > msl:
            msl = l[li]
        if l[li]%2 == 0:
            sp += l[li]
        if li == 2:
            s3c += l[li]
    c.append(l[:])
    l.clear()
for co in range(0, 3):
    for li in range(0, 3):
        if li%2 == 0:
            print(f'{c[co][li]}', end='')
        else:
            print(f' | {c[co][li]} | ', end='')
    print('\n',end='')
print(f'A) a soma de todos os pares : {sp}\nB) soma da 3 coluna : {s3c}')
print(f'C) o maior valor da 2 linha: {msl}')
