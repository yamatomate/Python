# desafio 40 implementando mais coisas ao des 35
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
    if n1 == n2 and n2 == n3:
        print("seu triangulo é equilatero")
    elif n1 == n2 or n2 == n3:
        print("seu trinagulo é isosceles")
    else:
        print("seu triangulo é escaleno")
else:
    print(f'os valores {n1} , {n2} e {n3} NÃO conseguem formar um triangulo')
