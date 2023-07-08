# 28 adivinhe um numero
from random import randint
from time import sleep
numsor = randint(0, 5)
numesc = int(input('de 0 a 5 que numero escolhi: '))
print('thinking')
sleep(3)
if numesc >= 6:
    print('BLZ DE 0 A 5')
if numsor == numesc:
    print(f'parabens voce acertou o numero ({numsor})')
else:
    print(f'melhore. o numero que eu escolhei foi {numsor}')
print('obrigado por jogar')
