# desafio 35 se 3 retas consgeuem formar um traingulo
"""n1 = int(input('digite um comprimento: '))
n2 = int(input('digite outro: '))
n3 = int(input('digite outroo numero: ')"""
n1 = 3
n2 = 4
n3 = 5
coda = (n1 + n2) > n3
codb = (n1 + n3) > n2
codc = (n2 + n3) > n1
if coda and codb and codc:
    print(f'os valores {n1} , {n2} e {n3} conseguem formar um triangulo')
else:
    print(f'os valores {n1} , {n2} e {n3} NÃO conseguem formar um triangulo')
