# desafio 30 numero par ou impar
# num = int(input('digite um numero: ')
from random import randint

num = randint(1, 100)
# o '%' é resto de divisão
cond = num % 2
if cond == 0:
    print(f'seu numero {num} é par')
else:
    print(f'seu numero {num} é impar')
# print(num, cond)
print('acabo')
