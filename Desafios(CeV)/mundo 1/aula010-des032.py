"""faça um programa que leia um ano qualquer e diga se ele é bissexto"""
# desafio 32 ano bissexto
# ano = int(input('digite um ano qualquer:'))
from random import randint

ano = randint(2004, 2023)
cond = ano % 4
if cond == 0:
    print(f'o ano {ano} é um ano bissexto')
else:
    print(f'o ano {ano} não é um ano bissexto')
print(f'{ano} e {cond}')
