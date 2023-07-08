# desafio 70 caixa de supermecado
"""total gasto, quantos produtos custam mais de 1000 e nome do mais barato"""
print('====='*7)
print('Super lojão onde vc encontra tudo!')
print('====='*7)
c = 0
nome = 'limao'
preco = 0
maiorp = 0
menorp = 0
nomemp = 0
total = 0
while True:
    nome = str(input('Qual nome do seu produto >> '))
    preco = float(input('Qual o preço dele >> R$'))
    op = str(input('deseja continuar [S/N] >> ')).upper()
    total += preco
    c += 1
    if preco >= 1000:
        maiorp += 1
    if preco < menorp or c == 1:
        menorp = preco
        nomemp = nome
    if op == "N":
        break
print('===='*7)
print(f'No total a sua compra deu R${total}', end='')
if maiorp > 0:
    print(f', {maiorp} produtos passaram de R$1000', end='')
print(f' o nome do produto mais barato é {nomemp}, que custa {menorp}')
