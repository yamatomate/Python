# desafio 106 mini programa de ajuda com cores
from time import sleep
def titulo(text=str("teste"), bord="=", tam_bord=int(56), normal=True):
    tam_bord= int(tam_bord)
    ta = len(text)
    print("\033[1;31;43m{}".format(bord*((tam_bord*2)+ta)))
    print(" "*tam_bord, end='')
    print(text)
    if normal:
        print(bord*((tam_bord*2)+ta), "\033[0;0;0m")
    else:
        print(bord*((tam_bord*2)+ta)) 
def cor(tema=str()):
    tema = str(tema)
    cores = {'amarelo':"\033[1;31;43m", 'verde':"\033[1;33;42m", 'vermelho':"\033[1;31;40m"}
    return cores[tema]

while True:
    titulo(text="ajuda interativa", tam_bord=51, normal=False)
    socorro = str(input("com qual comando está com duvida >{} ".format("\033[1;30;43m")))
    print("buscando", end='')
    for c in range(0,3):
        sleep(1)
        print(".", end='', flush=True)
    print()
    print("\033[7;37;40m",help(socorro))
    while True:
        rr = str(input(f"{cor(tema='amarelo')}deseja sair [S\\N] > "))
        if rr in "SsNn01":
            break
        print(f"{cor(tema='vermelho')}tente novamente")
    if rr in "Ss1":
            print("\033[0;0;0m")
            break