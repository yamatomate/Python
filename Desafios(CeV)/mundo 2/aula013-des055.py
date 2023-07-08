# desafio 55 de 5 pessoas quem é a mais gorda
from random import randint
masp = 0
mesp = 150
for c in range(0, 5):
    # peso = float(input('qual é o seu peso: '))
    peso = randint(45, 150)
    if peso > masp:
        masp = peso
    elif peso < mesp:
        mesp = peso
    # fim do loop
print(f'o mais pesado foi {masp} e o menos foi {mesp}')
