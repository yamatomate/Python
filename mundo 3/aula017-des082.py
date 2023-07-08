# desafio 82
num = []
par = []
impar = []
while True:
    x = int(input(' || Digie um numero >> '))
    num.append(x)
    opc = str(input('deseja continuar \\S\\N\\ >> '))
    if x % 2 == 0:  # par
        par.append(x)
    else:
        impar.append(x)
    if opc in 'Nn':
        print('==='*5)
        break
print(f'Todos os numeros = {num}\nOs pares = {par}\nOs impares = {impar}')
