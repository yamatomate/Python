# desafio 65 media de todos e alem disso quem é o maior e menor
cc = True
v = 0
soma = 0
maior = 0
menor = 0
while cc:
    num = int(input('digite um numero '))
    v = v + 1
    soma = num + soma
    sera = str(input('deseja continuar[n|s] ')).upper().strip()
    if sera == 'N':
        cc = False
    elif v == 1:
        menor = num
        maior = num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num
# fim loop
print(f'a media de todos esses numeros é {soma/v} e o maior é {maior} e o menor é {menor}')
