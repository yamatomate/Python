# Desafio 72 tupla com nome de numeros por extesso sl o nome
de0a9 = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove")
de10a20 = ("dez", "onze", "doze", "treze", "quatorze", "quinze", "dezseis", "dezoito", "dezenove", "vinte")
num = 21
while True:
    while num not in range(0, 21):
        num = int(input('Digite um numero de 0 a 20 >>'))
        if num not in range(0, 21):
            print('valor invalido tente novamente')
    if num <= 9:
        print(f'você digitou o numero {de0a9[num]}')
    if num >= 10:
        print(f'você digitou o numero {de10a20[num-10]}')
    des = str(input('deseja continaur \\S\\N\\ >>'))
    if des in 'Nn':
        break
    num = 21
