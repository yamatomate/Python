# desafio 58 jogo da adivinhação melhorado e refeito
from random import choice
from time import sleep

print('\033[0;33m='*21)
print('\033[;00m jogo da adivinhação')
print('\033[0;33m='*21)
print('\033[;00mDe 1 a 10 adivinhe\n\033[;37m(numeros fora disso serão\nreconhecidos e contará\ncomo uma jogada)')

vv = True
num = choice(range(1, 10))
tens = 0

while vv:
    plnum = int(input('\033[;00mdigite um numero: '))
    for c in range(0, 3):
        print('.', end='')
        sleep(0.5)
    if num == plnum:
        print(f'\nPARABÉNS! Você acertou o número que o computador pensou\nvocê levou {tens} tentativas para ganhar')
        vv = False
    else:
        print('\n\033[;32mtente de novo')
        tens = tens + 1
# fim
