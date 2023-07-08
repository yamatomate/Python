# desafio 62 PA usando while parte 2
"""para se calcular o ultimo termo da PA usa a expresão 1n+(posi-1)*razão"""
ini = int(input('digite onde começa sua PA: '))
raz = int(input('digite a razão da sua PA:'))
ultpa = ini + 10 * raz
cc = True
while cc:
    while ini != ultpa:
        print(f'{ini}; ', end='')
        ini = ini + raz
    # fim do basico
    res = int(input(f'\nquantas casa deseja ver ainda? '))
    ultpa = ini + res * raz
    if res <= 0:
        cc = False
