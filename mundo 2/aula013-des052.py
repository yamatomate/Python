# desafio 52 leitor de numero primo
num = int(input('digite um numero e direi se ele é primo:'))
sera = 0
for c in range(1, num+1):
    if num % c == 0:
        sera = sera + 1
if sera <= 2:
    print(f'seu numero {num} é primo')
else:
    print(f'seu numero {num} não é primo')
