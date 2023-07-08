# desafio 100 omagaaa funçao para sortear e somar
from time import sleep
from random import randint


def sorteador(y, x):
    y.clear()
    while True:
        x -= 1
        sot = randint(0, 500)
        print(f"{sot};  ", end="", flush=True)
        y.append(sot)
        sleep(0.3)
        if x < 0:
            print()
            break
    return y


def somarpar(num):
    print(f"De de {len(num)} irei somar os pares:")
    par = 0
    for c in num:
        if c % 2 == 0:
            print(f">{c}< ", end='', flush=True)
            par += c
            sleep(0.3)
    sleep(0.3)
    print(f"= {par}")


caca = ["aijn ze da manga"]
sorteador(caca, 5)
print(caca)
somarpar(caca)
