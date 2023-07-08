# desafio 61 PA usando while
"""para se calcular o ultimo termo da PA usa a expresão 1n+(posi-1)*razão"""
ini = int(input('digite onde começa sua PA: '))
raz = int(input('digite a razão da sua PA: '))
ultpa = ini + 10 * raz
while ini != ultpa:
    print(f'{ini}; ', end='')
    ini = ini + raz
# fim do loop
