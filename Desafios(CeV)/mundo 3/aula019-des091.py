# desafio 91 joginho com 4 players
from random import randint
from time import sleep

j = {}
for c in range(1, 5):
    j[f'jogador {c}'] = randint(1,1000)
    caba = list(j.items())
    print(f"{caba[c-1][0]} fez {caba[c-1][1]} pontos")
    sleep(1)
jo = sorted(j.items(), key = lambda x:x[1], reverse = True)
con = 1
print('++-++'*5)
for c, k in jo:
    print(f"{con}\' lugar   {c} com {k} pontos")
    con += 1
    sleep(1)
