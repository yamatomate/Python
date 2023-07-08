#ajuda o cara na mega sena
from random import randint
mega = []
jogos = []
qua = int(input("quantos jogos vc quer >> "))
print("---"*6)
for c in range(0, qua):
    l = 0
    while True:
        num = randint(1, 60)
        if num not in jogos:
            jogos.append(num)
        if l >= 6:
            break
        l += 1
    mega.append(jogos[:])
    jogos.clear()
for c in range(0, qua):
    print(mega[c])
    