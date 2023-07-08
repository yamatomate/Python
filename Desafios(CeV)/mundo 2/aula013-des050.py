# desafio 50 soma de numeros pares apenas
y = 0
for c in range(0, 6):
    x = int(input('digite um numero: '))
    if x % 2 == 0:
        y = y + x
    # limao
print(y)
