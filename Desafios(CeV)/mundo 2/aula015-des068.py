# desafio 68 par ou impar
from random import randint
vv = 0
while True:
    jogador = int(input('escolha um numero >> '))
    pref = str(input('prefere par ou impar [P\\I]')).upper().strip()
    computador = randint(1, 100)
    resultado = jogador + computador
    # se o resultado deu par e o jogador escolheu par:
    if pref == 'P':
        if resultado % 2 == 0:
            print(f'vc apostou {jogador} e o pc {computador}. {resultado} é par vc ganhou')
            vv += 1
        else:
            print(f'vc apostou {jogador} e o pc {computador}. {resultado} é impar o pc ganhou')
            break
    if pref == 'I':
        if resultado % 2 > 0:
            print(f'vc apostou {jogador} e o pc {computador}. {resultado} é par vc ganhou')
            vv += 1
        else:
            print(f'vc apostou {jogador} e o pc {computador}. {resultado} é impar o pc ganhou')
            break
print(f'você acertou {vv} consecutivas')
