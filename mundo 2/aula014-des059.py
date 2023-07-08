# desafio 59 calculadora de soma e subtração
n1 = 0
n2 = 0
op = 4
while op != 5:
    if op == 1:
        soma = n1 + n2
        print(f'a soma de {n1} e de {n2} é igual a {soma}')
        print('===-===' * 5)
    elif op == 2:
        mult = n1 * n2
        print(f'a multiplicação de {n1} e de {n2} é igual a {mult}')
        print('===-===' * 5)
    elif op == 3:
        if n1 > n2:
            print(f'{n1} é o maior.')
            print('===-===' * 5)
        elif n1 < n2:
            print(f'{n1} é o maior.')
            print('===-===' * 5)
        else:
            print('os dois números são iguais.')
            print('===-===' * 5)
    elif op == 4:
        n1 = int(input('digite um numero: '))
        n2 = int(input('digite outro numero: '))
    print('[1]soma\n[2]multiplicação\n[3]maior\n[4]novos números\n[5]sair')
    op = int(input('Qual opção deseja tomar:'))
    while op not in range(1, 6):
        op = int(input('Opção invalida, Digite novamente >>'))
# fim
