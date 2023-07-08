# desafio 99 funçao retronar
from random import randint


def maior(*num):
    mm = 0
    for c in num:
        if c > mm:
            mm = c
    print(f"{num}\n{mm} é o maior entre eles")


maior(randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100))
