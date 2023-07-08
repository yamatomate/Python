# desafio 64 some mt de numero e para sair digite 999 e mostre qunatos numeros foram somados
cc = True
soma = 0
vez = 0
while cc:
    num = int(input('digite um numero >'))
    if num == 999:
        cc = False
    else:
        soma = (num + soma)
        vez = vez + 1
# fim do loop
print(f'a soma de todos os números = {soma} e foram realizadas {vez} somas')
