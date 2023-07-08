# desafio 75 tuplas com valores que eu posso botar
num = [int(input('digite um numero >>')),
       int(input('digite um numero >>')),
       int(input('digite um numero >>')),
       int(input('digite um numero >>'))]
print(f'o valor -9- apareceu {num.count(9)}')
if 3 in num:
    print(f'Há um 3 na posição {num.index(3)+1}\' ')
print('esses são os pares:', end="")
for n in num:
    if n % 2 == 0:
        print(n, end= ' ')
