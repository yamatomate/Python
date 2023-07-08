# desafio 74 tupla com numeros aleatorios
from random import randint

tulipa = (randint(1, 50), randint(1, 50), randint(1, 50), randint(1, 50), randint(1, 50))
maior = menor = tulipa[0]
for c in range(0, len(tulipa)):
    print(f'-{tulipa[c]}-', end=' ')
    if tulipa[c] > maior:
        maior = tulipa[c]
    elif tulipa[c] < menor:
        menor = tulipa[c]
print(f'\nO maior = {maior} , o menor = {menor}')
