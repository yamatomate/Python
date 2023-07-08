"""for centroao in range(0, 10):
    print(f" -oi- ", end="")"""
inic = int(input('digite o começo: '))
fim = int(input('digite o final: '))
passo = int(input('qunatos passo deseja dar entre eles: '))
for cont in range(inic, fim+1, passo):
    print(cont, " ola :D")
