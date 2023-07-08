# desafio 81 vários números e seus pedidos
# 1 quantos números digitados; 2 lista decrescente; 3 se o valor 5 foi digitado
num = []
while True:
    num.append(int(input('|| Digite um numero >> ')))
    opc = str(input('deseja continuar? (S ou N) >> '))
    if opc in 'Nn':
        break
print(f'Foram digitados {len(num)} números, {sorted(num, reverse= True)}')
if 5 in num:
    print('o valor - 5 - foi digitado')
