# desafio 98 contagem coisada
from time import sleep


def contador(x, y, pas):
    print(f"De {x} a {y}; de {pas} em {pas}")
    for c in range(x, y, pas):
        sleep(1)
        print(f"{c}", end=" | ")
    print(' Fim')


contador(1, 10, 1)
contador(10, 1, -1)
com = int(input("Começa a contar aonde > "))
ter = int(input("termina a contar aonde > "))
passo = int(input("passos > "))
contador(com, ter, passo)
